# 472｜OT-EVIDENCE：Evidence字段级Profile修订候选

**对象类型：** OT-EVIDENCE；**类别：** C1证据资产候选；**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）  
**语义关系/核验Owner：** M06；**状态：** Proposed；M08/M06/M17/M18 Review Pending

## 1. 对象职责

Evidence是对一个精确、类型化目标的可复核定位及完整性登记。M08维护Evidence身份、目标引用、Locator、Digest、受控Excerpt和生命周期；M06维护Evidence与Assertion的语义关系及核验。Evidence本身不等于Assertion已被证明。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| EVD-001 | `evidence_id` | ObjectId<OT-EVIDENCE> / 1 | 是 | Immutable | M08生成 |
| EVD-002 | `evidence_kind` | Enum<EvidenceKind> / 1 | 是 | Immutable | Direct/Derived/Receipt/Observation |
| EVD-003 | `evidence_target_ref` | TypedRefUnion / 1 | 是 | Immutable | 必须且仅有一个主目标分支 |
| EVD-004 | `target_version_ref` | TypedVersionRef / 1 | 是 | Immutable | 精确目标/Receipt/Observation版本 |
| EVD-005 | `locator_schema_ref` | Ref<LocatorSchemaVersion> / 1 | 是 | Immutable | 定位结构版本 |
| EVD-006 | `locator_payload` | StructuredLocator / 1 | 是 | Immutable | 页码/时间/字段路径等坐标 |
| EVD-007 | `target_content_digest` | Digest / 1 | 是 | Immutable | 目标版本内容摘要 |
| EVD-008 | `locator_fragment_digest` | Digest / 0..1 | 有片段校验时 | Immutable | 定位片段摘要 |
| EVD-009 | `excerpt_ref` | OpaqueHandle<ControlledExcerpt> / 0..1 | 允许摘录时 | MutableWithHistory | 最小必要、受控存储 |
| EVD-010 | `excerpt_digest` | Digest / 0..1 | 有Excerpt时 | Immutable | 摘录摘要，不替代目标摘要 |
| EVD-011 | `integrity_state` | Enum<EvidenceIntegrity> / 1 | 是 | MutableWithHistory | Unverified/Intact/Changed/Unresolvable/Unavailable |
| EVD-012 | `lifecycle_state` | Enum<EvidenceLifecycle> / 1 | 是 | MutableWithHistory | Active/Restricted/Withdrawn/Expired/DeletionPending |
| EVD-013 | `created_by_ref` | Ref<Actor> / 1 | 是 | Immutable | 创建主体 |
| EVD-014 | `created_at` | Instant / 1 | 是 | Immutable | 创建时间 |
| EVD-015 | `recorded_at` | Instant / 1 | 是 | Immutable | M08登记时间 |
| EVD-016 | `classification_ref` | Ref<DataClassification> / 1 | 是 | MutableWithHistory | 不低于目标/摘录敏感度 |
| EVD-017 | `purpose_lineage_refs` | Ref<Purpose> / 1..N | 是 | AppendOnly | 证据生成/读取用途历史 |
| EVD-018 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 是 | MutableWithHistory | 具体期限待批准 |
| EVD-019 | `object_version` | Version / 1 | 是 | AppendOnly | Evidence状态版本 |
| EVD-020 | `withdrawal_reason_ref` | Ref<Reason> / 0..1 | 撤销时 | Immutable | 撤销原因分类 |
| EVD-021 | `deletion_state_ref` | Ref<DeletionState> / 0..1 | 删除时 | MutableWithHistory | 删除传播状态 |

| EVD-022 | `captured_at` | Instant / 0..1 | 来源/采集时间可确定时 | Immutable | 材料实际被捕获或观察的时间，与Evidence登记时间分离 |

## 3. EvidenceTargetRef联合分支

- `SourceSnapshotTarget`：`source_ref + snapshot_id`；
- `KnowledgeAssetVersionTarget`：`knowledge_asset_ref + asset_version_id`；
- `ConnectorReceiptTarget`：`receipt_ref + receipt_version`，Receipt原件由M17维护；
- `ObservationTarget`：`observation_ref + observation_version`，Observation权威由其Owner维护。

目标类型必须与目标引用一致；不允许用自由文本URL替代目标身份。一个Evidence只能有一个主Target；辅助上下文另用`context_target_refs`。

## 4. Locator、Digest与M06交接

Locator必须绑定目标版本、坐标系、索引基准、单位、解析器/Schema版本和必要时间基准。Digest必须说明算法、输入范围、规范化规则和生成主体。目标摘要、片段摘要、Excerpt摘要和处理输出摘要不可互换。

M08发布EvidenceRegistered后，M06通过受控Query读取必要元数据/定位信息，并维护Evidence—Assertion关系。M08不得写Assertion Verification；M06不得修改Evidence Locator或M17 Receipt原件。

## 5. 负向验收

Evidence没有精确Target Version；Locator无法解析却标记Intact；Digest通过被解释为Assertion Verified；Receipt原件被M08复制成权威；Excerpt超过最小必要范围；反驳证据被隐藏。
