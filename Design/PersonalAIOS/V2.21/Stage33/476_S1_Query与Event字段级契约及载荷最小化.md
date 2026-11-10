# 476｜S1 Query与Event字段级契约及载荷最小化

**状态：** Logical Query/Event Contract Candidate；No API Implementation

## 1. Query统一输入封套

`query_id`、`query_type`、`actor_ref`、`purpose_ref`、`target_refs`、`requested_field_set`、`requested_version_ref`、`scope_ref`、`policy_context_ref`、`as_of_time`、`pagination_ref`、`correlation_id`。

Query必须指定Purpose和字段范围；全文读取与元数据读取使用不同字段集/Policy；不得因已登录就返回所有内容。

## 2. Query目录

| Query | Owner | 核心输入 | 返回边界 |
|---|---|---|---|
| ResolveSource | M08 | Source identity/Locator | 身份摘要、Locator状态、Availability |
| GetSourceSnapshotMetadata | M08 | SourceRef + Snapshot ID | 快照元数据、版本、分类，不默认全文 |
| GetRawAssetHandle | M02 | RawAssetRef、Purpose、Actor | 经PEP批准的短期Opaque Handle |
| GetKnowledgeAssetByPurpose | M08 | AssetRef、Purpose、FieldSet | 只返回被允许字段/内容 |
| GetKnowledgeAssetVersion | M08 | AssetRef + VersionRef | 精确版本元数据和受控内容引用 |
| GetExtractionRun | M08 | RunRef | 输入输出Ref、Processor Version、状态、最小错误 |
| GetChunkSetByPurpose | M08 | AssetVersion、Purpose | 当前权限下可用Chunk集合及Freshness |
| GetEvidenceLocator | M08 | EvidenceRef、Purpose | TargetRef、目标版本、Locator和Integrity |
| ResolveEvidenceTarget | 目标Owner编排 | EvidenceTargetRef | 通过目标Owner返回最小必要目标数据 |
| GetS1Lineage | M08 | ObjectRef、Depth、Purpose | 可追踪血缘，不返回无关正文 |

## 3. Query响应封套

`query_id`、`result_refs`、`resolved_versions`、`returned_field_set`、`redaction_summary`、`policy_decision_ref`、`as_of_time`、`next_page_token`、`data_classification`、`correlation_id`。若结果受限，使用Withheld/Redacted等明确语义，避免泄露内容存在性。

## 4. Event统一封套

`event_id`、`event_type`、`event_version`、`aggregate_ref`、`aggregate_version`、`producer_module_id`、`occurred_at`、`recorded_at`、`payload_schema_version`、`data_classification`、`purpose_ref`（适用时）、`correlation_id`、`causation_id`、`payload`。

## 5. Event目录

| Event | Producer | 最小Payload |
|---|---|---|
| SourceRegistered | M08 | SourceRef、Version、SourceKind |
| SourceLocatorChanged | M08 | SourceRef、LocatorRef、Locator State |
| SourceSnapshotCaptured | M08 | SourceRef、SnapshotRef、Capture State、Classification |
| RawAssetRegistered | M08 | RawAssetRef、SnapshotRefs、DigestRef、Custody State |
| KnowledgeAssetCreated | M08 | AssetRef、VersionRef、Classification |
| KnowledgeAssetVersionCreated | M08 | AssetRef、Old/New VersionRef、Change Reason |
| ExtractionRunStarted | M08 | RunRef、Input VersionRefs、Processor Version |
| ExtractionRunCompleted | M08 | RunRef、OutputRefs、Run State、Manifest Digest |
| ChunkSetPublished | M08 | ChunkSetRef、Asset Version、RunRef、Count/Manifest |
| ChunkSetInvalidated | M08 | ChunkSetRef、Reason、Affected Projection Refs |
| EvidenceRegistered | M08 | EvidenceRef、TargetRef、Target Version、Integrity State |
| EvidenceIntegrityChanged | M08 | EvidenceRef、Old/New State、Reason |
| SourceRightsChanged | M08/M18 | SourceRef、RightsRef、Effective Time、Impact Scope |
| S1DeletionPropagationStarted | M08/M18 | RequestRef、TargetRef、Scope、Sequence |

## 6. Event最小化、重放与顺序

Event默认传Ref、版本、状态和最小摘要；不传原始正文、完整邮件/语音、密钥、完整Excerpt、任意Prompt或可恢复敏感字段。消费者需要更多内容时，必须向权威Owner发起Query并重新执行Policy。

消费者按Event ID去重，按Aggregate Version检查顺序；旧Event不能覆盖新状态或Tombstone。重放仅用于重建派生视图，不自动重发外部动作、不恢复撤销授权、不使已删除内容复活。以上为逻辑契约候选。

## 7. 跨Owner事件的权威Producer、协调者与消费者边界（审查补充）

为避免联合参与被误解为联合持有权威状态，事件必须遵循“事实由权威Owner发布、协调者只发布自身协调事实、消费者只更新本域派生视图”的规则。

| 事实域 | 权威Producer | 可发布的事实事件 | 非权威参与方边界 |
|---|---|---|---|
| Source与Snapshot登记、采集元数据 | M08 | SourceRegistered、SourceSnapshotCaptured | M18可发布独立Policy/Rights决策事件；不得代替M08改写Source事实 |
| 来源权利/处理依据登记（以既有治理分工为准） | 经Owner确认的权利登记Owner；Policy裁决由M18 | SourceRightsRecordChanged（登记事实）/ PolicyDecisionIssued（策略裁决） | M08仅引用并消费；若登记Owner尚未明确，事件保持Candidate，不得先行指定M08或M18 |
| Policy Decision | M18 | PolicyDecisionIssued、PolicyDecisionRevoked | M08/M02/M06按授权消费；不得发布M18权威裁决的替代事件 |
| Physical Custody与物理删除回执 | M02 | PhysicalCustodyChanged、PhysicalDeletionReceiptIssued | M08发起请求并消费回执，不得发布“物理删除已完成”权威事实 |
| Evidence与KnowledgeAsset元数据 | M08 | EvidenceRegistered、KnowledgeAssetVersionCreated | M06维护Assertion—Evidence关系及Verification事实，不得由M08代发核验结果 |
| Assertion Verification | M06 | AssertionVerificationChanged | M08只消费最小必要结果，不复制为Evidence权威字段 |
| 删除/撤销传播协调 | 发起请求的Owner发布DeletionPropagationRequested；各数据/投影Owner分别发布本域执行结果 | DeletionPropagationRequested、DeletionStepCompleted、DeletionPropagationCompleted（仅协调汇总） | 协调汇总不得替代各Owner执行回执；未收到必需回执时不得宣告Completed |

### 7.1 事件发布规则

1. 每个事件定义唯一`authoritative_producer_module_id`，不得使用含糊的`M08/M18`联合Producer标记。
2. 若事件需要跨Owner协同，使用独立的Request/Command/Correlation关联；每个Owner对自己权威范围内的状态变更单独发布事实事件。
3. 协调者可发布Workflow/Propagation状态，但必须引用各Owner的结果事件或回执，并明确该状态是汇总状态而非底层对象权威状态。
4. 事件消费者只能更新本域Projection；遇到冲突时回查权威Owner，不以事件到达顺序覆盖权威状态。
5. `SourceRightsRecordChanged`的真实登记Owner仍需在Owner审议矩阵确认；`PolicyDecisionIssued`始终由M18发布。未完成Owner映射前，前者不得进入Frozen Contract。
6. 删除传播的`Completed`仅表示已定义范围内全部必需步骤均有可验证回执；若存在法律保留、备份延迟或不可达副本，必须显式返回Partial/Blocked及例外范围。

### 7.2 本阶段决策状态

以上为契约澄清候选，用于消除Producer字段歧义；不改变既有IA/TDA/SA/Physical Custodian/Policy Authority分配，不新增OT/OF，不构成真实Owner批准或API实现。需由M02/M06/M08/M18确认各自事件目录后方可冻结。

