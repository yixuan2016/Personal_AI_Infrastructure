# 475｜S1 Command字段级契约与写入守卫

**状态：** Logical Command Contract Candidate；No API Implementation

## 1. Command统一封套

| 字段 | 类型 | 必需 | 语义 |
|---|---|---|---|
| `command_id` | ObjectId<Command> | 是 | 唯一命令身份 |
| `command_type` | Enum<CommandType> | 是 | 命令名称/版本 |
| `target_object_type_id` | OT ID | 是 | 明确目标类型 |
| `target_object_id` | ObjectId | 是 | 目标实例 |
| `target_owner_module_id` | Module ID | 是 | 唯一写入权威Owner |
| `actor_ref` | Ref<Actor> | 是 | 发起主体 |
| `purpose_ref` | Ref<Purpose> | 是 | 本次操作用途 |
| `expected_object_version` | Version | 适用时必需 | 乐观并发守卫 |
| `requested_change` | StructuredValue | 是 | 明确字段级变化 |
| `source_refs` | Ref集合 | 适用时 | 来源/输入 |
| `evidence_refs` | Ref集合 | 适用时 | 决策依据 |
| `policy_context_ref` | Ref<PolicyContext> | 是 | 触发PEP评估 |
| `approval_refs` | Ref集合 | 适用时 | 具体高风险批准 |
| `consent_refs` | Ref集合 | 适用时 | 仅适用Consent时引用 |
| `owner_confirmation_ref` | Ref | 适用时 | 本人确认 |
| `idempotency_key` | Opaque String | 是 | 在作用域内避免重复副作用 |
| `correlation_id` | String | 是 | 跨模块追踪 |
| `requested_at` | Instant | 是 | 发起时间 |

## 2. Command目录与字段守卫

| Command | 目标OT | Owner | 必须字段/守卫 |
|---|---|---|---|
| RegisterSource | OT-SOURCE | M08 | source_kind、source_authority_ref、origin_identity_ref、Actor、Purpose、Policy |
| UpdateSourceLocator | OT-SOURCE | M08 | source_ref、new_locator、Expected Version、变更原因 |
| RecordSourceSnapshot | Source子记录 | M08 | source_ref、capture_method、Purpose、PolicyDecision、Capture Actor、Rights/Basis引用 |
| RegisterRawAsset | OT-RAW-ASSET | M08 | SnapshotRefs、M02 Opaque Handle、Size、Detected Media Type、Digest Scope |
| CreateKnowledgeAsset | OT-KNOWLEDGE-ASSET | M08 | asset_kind、输入Refs、分类、Purpose、Policy |
| CreateKnowledgeAssetVersion | KnowledgeAsset子记录 | M08 | asset_ref、new content ref/digest、Expected Version、change_reason |
| StartExtractionRun | OT-EXTRACTION-RUN | M08 | 输入版本、Processor Version、Config Digest、Purpose、Policy、Idempotency |
| CompleteExtractionRun | OT-EXTRACTION-RUN | M08 | RunRef、OutputRefs、Output Digest、Actual State、ErrorClass |
| PublishChunkSet | ChunkSet子记录 | M08 | Asset Version、RunRef、Manifest、Policy、Expected Version |
| RegisterEvidence | OT-EVIDENCE | M08 | EvidenceTargetRef、Target Version、Locator Schema、Digest、Purpose |
| VerifyEvidenceIntegrity | OT-EVIDENCE | M08 | EvidenceRef、Target Version、Digest Scope、校验证据 |
| RestrictKnowledgeAsset | OT-KNOWLEDGE-ASSET | M08 | AssetRef、scope、reason、Policy/Tombstone、Expected Version |

## 3. Command结果封套

Command结果至少返回`command_id`、`accepted/rejected`、`target_ref`、`new_object_version`（适用时）、`result_state`、`event_refs`、`error_code`、`retry_advice`和`correlation_id`。结果Accepted不等于业务任务完成。

## 4. 统一拒绝条件

Actor未知、Purpose缺失、Target Owner不匹配、引用类型不匹配、Expected Version冲突、Policy Deny、必要Consent/Approval缺失、Rights Unknown、Tombstone命中、输入版本不可解析、幂等冲突时，必须拒绝或进入明确人工复核状态。

## 5. 跨Owner能力调用

M08不得直接更新M02 Physical Custody、M06 Assertion Verification、M18 PolicyDecision或M17 Receipt；只能调用目标Owner契约并保留返回Ref。跨Owner工作流按Saga协调，不能宣称全局原子事务。以上Command为逻辑候选，不代表API/数据库Schema已实现。