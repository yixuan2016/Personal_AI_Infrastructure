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