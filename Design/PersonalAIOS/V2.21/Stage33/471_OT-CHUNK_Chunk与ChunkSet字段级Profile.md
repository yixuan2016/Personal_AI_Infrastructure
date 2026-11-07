# 471｜OT-CHUNK：Chunk与ChunkSet字段级Profile

**对象类型：** OT-CHUNK；**类别：** C3派生持久资产候选；**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）  
**状态：** Proposed；M08/M06/M18/M07 Review Pending

## 1. 对象职责

Chunk是某个KnowledgeAsset精确内容版本经指定ExtractionRun生成的派生片段。Chunk不独立成为原始来源，不是Assertion，不是MemoryItem。Chunk必须能追溯到父资产版本、处理运行、分段策略和精确父文档坐标。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| CHK-001 | `chunk_id` | ObjectId<OT-CHUNK> / 1 | 是 | Immutable | M08生成 |
| CHK-002 | `knowledge_asset_ref` | Ref<OT-KNOWLEDGE-ASSET> / 1 | 是 | Immutable | 父逻辑资产 |
| CHK-003 | `asset_version_ref` | SubrecordRef<KnowledgeAssetVersion> / 1 | 是 | Immutable | 精确父内容版本 |
| CHK-004 | `extraction_run_ref` | Ref<OT-EXTRACTION-RUN> / 1 | 是 | Immutable | 生成本Chunk的Run |
| CHK-005 | `chunk_set_id` | SubrecordId<ChunkSet> / 1 | 是 | Immutable | 集合身份，不新增OT |
| CHK-006 | `chunk_set_version` | Version / 1 | 是 | Immutable | ChunkSet版本 |
| CHK-007 | `chunk_sequence` | Integer / 1 | 是 | Immutable | 集合内排序序号 |
| CHK-008 | `content_ref` | OpaqueHandle<DerivedContent> / 1 | 是 | MutableWithHistory | 受控内容引用 |
| CHK-009 | `text_digest` | Digest / 1 | 是 | Immutable | Chunk文本摘要 |
| CHK-010 | `locator_in_parent` | StructuredLocator / 1 | 是 | Immutable | 精确父版本坐标 |
| CHK-011 | `token_range` | StructuredValue / 0..1 | 适用时 | Immutable | Tokenizer及版本明确 |
| CHK-012 | `character_range` | StructuredValue / 0..1 | 适用时 | Immutable | 字符编码/索引基准明确 |
| CHK-013 | `chunk_strategy_ref` | Ref<ChunkingStrategyVersion> / 1 | 是 | Immutable | 分段策略精确版本 |
| CHK-014 | `language_refs` | Ref<Language> / 0..N | 适用时 | Immutable | 多语言片段支持 |
| CHK-015 | `classification_ref` | Ref<DataClassification> / 1 | 是 | MutableWithHistory | 不低于父资产/片段实际敏感度 |
| CHK-016 | `purpose_lineage_refs` | Ref<Purpose> / 1..N | 是 | AppendOnly | 历史处理用途，不等于当前授权 |
| CHK-017 | `projection_state` | Enum<ProjectionState> / 1 | 是 | MutableWithHistory | Building/Published/Stale/Restricted/Invalidated/Deleted |
| CHK-018 | `supersedes_chunk_ref` | Ref<OT-CHUNK> / 0..1 | 否 | Immutable | 新集合替代旧Chunk时引用 |
| CHK-019 | `created_at` | Instant / 1 | 是 | Immutable | 创建时间 |
| CHK-020 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 是 | MutableWithHistory | 保留/清理策略 |
| CHK-021 | `object_version` | Version / 1 | 是 | AppendOnly | 状态版本 |
| CHK-022 | `deletion_state_ref` | Ref<DeletionState> / 0..1 | 否 | MutableWithHistory | 删除传播状态 |

## 3. ChunkSet子记录与Embedding

ChunkSet不新增OT。字段候选：`chunk_set_id`、`knowledge_asset_ref`、`asset_version_ref`、`extraction_run_ref`、`chunking_strategy_ref`、`expected_chunk_count`、`published_chunk_count`、`manifest_digest`、`set_state`、`created_at`、`published_at`。发布采用集合级门禁，避免部分Chunk已Published而整体未验证。

Embedding、Vector Index、Search Projection均不是本阶段新增OT。它们必须记录Chunk/Asset Version、Embedding Model/Version、维度、配置摘要、索引版本、Purpose/Policy边界和失效状态。模型升级创建新Projection版本，不修改Chunk。

## 4. 发布条件与负向验收

所有必需Chunk完成、父版本一致、Run成功、Digest有效、分类/权限继承完成、当前Policy允许、ChunkSet Manifest完整后，方可Published。部分发布必须标记Partial并限制下游消费。禁止Chunk无父版本、Embedding绕过源Policy、ChunkSet部分失败被整体标记Published或Parser升级改写原件。