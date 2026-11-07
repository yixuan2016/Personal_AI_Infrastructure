# 469｜OT-KNOWLEDGE-ASSET：KnowledgeAsset字段级Profile修订候选

**对象类型：** OT-KNOWLEDGE-ASSET；**类别：** C1权威持久对象候选  
**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）；**状态：** Proposed；M08/M06/M18/M07 Review Pending

## 1. 对象职责

KnowledgeAsset是M08管理的逻辑知识资产身份及其不可变内容版本集合。它可由一个或多个SourceSnapshot/RawAsset形成，也可作为复合文档、笔记、导出或受控整理结果。它不是原始字节、Chunk、Embedding、Assertion或MemoryItem。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| KAS-001 | `knowledge_asset_id` | ObjectId<OT-KNOWLEDGE-ASSET> / 1 | 是 | Immutable | M08生成 |
| KAS-002 | `asset_kind` | Enum<KnowledgeAssetKind> / 1 | 是 | MutableWithHistory | Document/Note/Record/Collection |
| KAS-003 | `display_name` | String / 0..1 | 否 | MutableWithHistory | 可能敏感，按Purpose裁剪 |
| KAS-004 | `source_snapshot_refs` | Ref<SourceSnapshot> / 0..N | 否 | AppendOnly | 来源快照精确引用 |
| KAS-005 | `raw_asset_refs` | Ref<OT-RAW-ASSET> / 0..N | 否 | AppendOnly | 原始字节逻辑资产引用 |
| KAS-006 | `current_asset_version_ref` | SubrecordRef<KnowledgeAssetVersion> / 1 | 是 | MutableWithHistory | 当前内容版本 |
| KAS-007 | `asset_versions` | SubrecordRef<KnowledgeAssetVersion> / 1..N | 是 | AppendOnly | 不可变版本集合 |
| KAS-008 | `lifecycle_state` | Enum<KnowledgeAssetLifecycle> / 1 | 是 | MutableWithHistory | Active/Superseded/Retired/Restricted |
| KAS-009 | `classification_ref` | Ref<DataClassification> / 1 | 是 | MutableWithHistory | 不低于输入最高敏感度 |
| KAS-010 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 是 | MutableWithHistory | 具体期限另行批准 |
| KAS-011 | `created_by_ref` | Ref<Actor> / 1 | 是 | Immutable | 创建主体 |
| KAS-012 | `created_at` | Instant / 1 | 是 | Immutable | 创建时间 |
| KAS-013 | `updated_at` | Instant / 1 | 是 | MutableWithHistory | 更新/状态变化时间 |
| KAS-014 | `object_version` | Version / 1 | 是 | AppendOnly | 聚合根版本 |
| KAS-015 | `processing_purpose_refs` | Ref<Purpose> / 0..N | 否 | AppendOnly | 历史处理用途，不构成未来许可 |
| KAS-016 | `deletion_dependency_refs` | Ref<DerivedAsset> / 0..N | 系统维护 | MutableWithHistory | 派生依赖闭包 |

## 3. KnowledgeAssetVersion子记录

该子记录不新增OT。字段候选：`asset_version_id`、`asset_version_number`、`normalized_content_ref`、`normalized_content_digest`、`normalization_profile_ref`、`content_media_type`、`language_refs`、`content_locator_ref`、`input_source_snapshot_refs`、`input_raw_asset_refs`、`created_at`、`created_by_ref`、`supersedes_version_ref`、`change_reason_ref`、`classification_ref`。

内容版本不可原位覆盖。版本变化必须说明是内容变化、人工修订还是规范化规则变化。仅Parser/OCR/模型版本变化，不自动创建新的原件内容版本，应创建新ExtractionRun和派生版本。

## 4. 处理状态与质量状态分离

Processing State：Queued/Processing/Ready/Failed/Partial/Quarantined。  
Quality Assessment：Unassessed/Reviewed/Accepted/Rejected/NeedsReview。  
Assertion Verification由M06管理，不能在KnowledgeAsset字段中设置Verified作为事实状态。

## 5. 版本规则与负向验收

内容实质变化创建新KnowledgeAssetVersion；处理器升级创建新ExtractionRun和新ChunkSet；展示名/标签变化更新逻辑资产元数据并保留历史；SourceSnapshot新增时追加血缘。禁止Parser升级覆盖原件、Ready推导Verified、将历史Purpose当授权白名单、Chunk/Embedding脱离资产版本。