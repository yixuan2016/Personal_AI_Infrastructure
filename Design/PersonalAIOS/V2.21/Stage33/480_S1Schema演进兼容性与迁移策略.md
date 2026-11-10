# 480｜S1 Schema演进、兼容性与迁移策略

**状态：** Schema Evolution Candidate；No Physical Migration Authorized

## 1. 演进原则

字段语义先于物理Schema。任何字段新增、改名、改类型、拆分、合并、废弃或删除，必须评估对象Owner、契约、事件、查询、索引、派生资产、测试、治理和历史数据。不得通过静默默认值掩盖语义变化。

## 2. 变更分类

| 类型 | 示例 | 兼容风险 | 必须措施 |
|---|---|---|---|
| AdditiveOptional | 新增可选字段 | 低/中 | Schema Version、默认缺失语义 |
| AdditiveRequired | 新增必填字段 | 高 | 旧记录补齐、写入门禁、双读/双写评估 |
| SemanticChange | purpose_refs改为历史血缘 | 高 | 新字段/新语义版本、旧字段弃用映射 |
| TypeChange | String改TypedRef | 高 | 迁移规则、数据质量检查 |
| Rename | 字段规范名调整 | 中/高 | Alias周期、消费者迁移 |
| Deprecation | 停止推荐字段 | 中 | Deprecation Window、替代字段 |
| Removal | 删除字段 | 高 | 消费者无引用证明、Owner批准 |

## 3. Schema Version规则

每个OT Profile有独立`schema_version`；每个API/Command/Event有独立`contract_version`或`payload_schema_version`。字段增加不应随意改变对象`object_version`语义；Schema Version升级与数据实例Version升级分开。

## 4. 兼容策略

- Reader优先兼容当前和明确支持的前一版本。
- Writer只写当前已批准版本。
- 新字段默认Optional，除非安全/正确性要求必须Required并提供迁移方案。
- 字段改名使用有期限Alias，不永久双写。
- 语义变化必须新字段或新版本，不得复用旧字段名表达新含义。
- Event消费者忽略未知Optional字段；未知Required语义应拒绝处理。
- 旧版本重放不得绕过当前Policy、Tombstone和删除状态。

## 5. S1关键迁移建议

1. `source_version_ref`拆为`external_version_token`和`source_snapshot_ref`。
2. Evidence的`source_ref`/`knowledge_asset_ref`逐步由类型化`evidence_target_ref`替代。
3. `purpose_refs`明确为历史处理用途，不能表达未来授权。
4. Digest拆分目标内容、片段、Excerpt和处理输出摘要。
5. KnowledgeAsset内容版本与Processor/ExtractionRun版本分离。
6. Source Locator改为可多值、可变且保留历史的子记录集合。

上述仅为迁移建议；未批准前不得覆盖旧字段或改变现有数据。

## 6. 迁移、回滚与负向验收

迁移流程：`Inventory Consumers → Approve Semantic Change → Define Mapping → Build Synthetic Fixtures → Dry-run Validation → Dual Read (if needed) → Controlled Write Cutover → Verify Lineage/Policy → Deprecate Old Field → Remove After Approval`。本阶段不执行真实数据迁移或Schema部署。

每项迁移定义回滚窗口、备份/快照、版本边界和数据修复方案。语义错误不能只靠数据库回滚解决；已发出Event或Provider副作用需执行补偿和对账并保留审计。

禁止字段改名导致消费者静默读空、Required字段无历史补齐策略、旧Event覆盖新状态、旧字段语义被复用或迁移绕过Rights/Policy/Tombstone。


## 7. OF-006既有字段到本阶段候选字段映射

以下映射用于保留312、343—345号历史候选语义，不代表已批准迁移。原字段在Owner批准前不得删除或覆盖。

| 既有候选字段 | 本阶段候选映射 | 说明 |
|---|---|---|
| Source: `source_kind` | `source_kind` | 保留，枚举需版本化 |
| Source: `provider_or_origin` | `source_authority_ref` + `origin_identity_ref` | 拆分原始权威主体与稳定来源身份 |
| Source: `locator` | `locator_refs` | 从单一定位改为可变历史子记录集合 |
| Source: `acquired_at` | SourceSnapshot.`acquired_at` | 采集时间属于一次采集，不是稳定Source身份 |
| Source: `source_version_ref` | Snapshot.`external_version_token` + SnapshotRef | 区分Provider版本令牌与本地Snapshot身份 |
| Source: `integrity_digest` | Snapshot/RawAsset对应Digest | 摘要必须绑定实际内容范围 |
| Source: `rights_ref` | `source_rights_refs` + Snapshot.`rights_snapshot_ref` | 区分当前条款登记与采集时条款快照 |
| Source: `purpose_ref` | Snapshot.`purpose_ref` | Purpose绑定一次采集，不成为Source永久许可 |
| RawAsset: `storage_handle_ref` | `physical_handle_ref` | 受M02管理的Opaque Handle |
| RawAsset: `content_digest` | `byte_digest` | 明确原始字节范围/算法 |
| RawAsset: `media_type` | `media_type_declared` + `media_type_detected` | 来源声明与内容检测分离 |
| RawAsset: `size_bytes` | `byte_size` | 规范单位Byte |
| RawAsset: `encryption_key_ref` | `encryption_profile_ref` + M02密钥能力 | M08不持有密钥材料或直接密钥权威 |
| RawAsset: `custodian_ref` | M02 Physical Custodian角色引用 + `custody_state` | 保管责任与资产IA分离 |
| RawAsset: `retention_ref` | `retention_profile_ref` | 与既有RetentionPolicy/目录映射 |
| KnowledgeAsset: `asset_kind` | `asset_kind` | 保留 |
| KnowledgeAsset: `source_refs` | `source_snapshot_refs` + `raw_asset_refs` | 精确到快照和原始逻辑资产 |
| KnowledgeAsset: `content_version` | `asset_versions` + `current_asset_version_ref` | 内容版本子记录化 |
| KnowledgeAsset: `processing_state` | `processing_state` | 保留，但与Quality/Verification分离 |
| KnowledgeAsset: `language` | Version.`language_refs` | 语言属于内容版本 |
| KnowledgeAsset: `index_refs` | Projection/Index引用 | 索引不成为知识资产权威 |
| KnowledgeAsset: `retention_ref` | `retention_profile_ref` | 保留策略引用 |
| Chunk: `parent_asset_ref` | `knowledge_asset_ref` + `asset_version_ref` | 必须指向精确父版本 |
| Chunk: `parser_version_ref` | `extraction_run_ref` → `processor_version_ref` | 处理器版本经Run追溯 |
| Chunk: `locator_offsets` | `locator_in_parent` | 明确坐标系/编码/索引基准 |
| Chunk: `content_digest` | `text_digest` | Chunk文本摘要，不替代父资产Digest |
| Chunk: `embedding_ref` | Projection引用 | Embedding由Projection Owner维护 |
| Chunk: `rebuildability_state` | `projection_state` + 重建规则 | 新旧状态语义需逐项确认 |
| ExtractionRun: `pipeline_ref` | `processor_ref` + `processor_version_ref` | Pipeline/Processor目录需统一映射 |
| ExtractionRun: `input_asset_version` | `input_refs` | 每个输入携带精确版本 |
| ExtractionRun: `started/ended_at` | `started_at` / `completed_at` | 结束时间允许失败/取消场景 |
| ExtractionRun: `model_version_ref` | `processor_version_ref`及Provider引用 | 模型版本和Provider版本分离 |
| Evidence: `source_ref` / `knowledge_asset_ref` | `evidence_target_ref` | 使用类型化联合目标 |
| Evidence: `source_version_ref` | `target_version_ref` | 绑定目标类型和精确版本 |
| Evidence: `locator` | `locator_payload` + `locator_schema_ref` | 坐标结构和版本显式化 |
| Evidence: `supports_or_refutes_refs` | M06 Evidence—Assertion关系 | 不由M08 Evidence对象持有语义核验权 |
| Evidence: `integrity_digest` | `target_content_digest` / `locator_fragment_digest` | 拆分目标与片段摘要 |
| Evidence: `access_scope` | Classification + 当前Policy裁决 | Scope不代替PEP |
| Evidence: `confidence`（若存在） | M06核验/不确定性语义 | 不在M08 Evidence字段中表达事实可信度 |

任何无法一对一映射的旧字段都需标记`MigrationMappingPending`，由M08与M06共同审议；不得通过自动字段改名掩盖语义变化。
