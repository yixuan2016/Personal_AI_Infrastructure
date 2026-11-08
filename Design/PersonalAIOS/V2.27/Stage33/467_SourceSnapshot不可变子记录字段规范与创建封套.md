# 467｜SourceSnapshot不可变子记录字段规范与创建封套

**父对象：** OT-SOURCE；**分类：** M08管理的不可变子记录候选，不是独立OT  
**状态：** Proposed；M08/M06/M02/M18 Review Pending

## 1. 设计定位

SourceSnapshot记录某一Source在某次采集时实际获得的内容版本和上下文。它解决稳定来源身份、易变Locator、外部版本令牌和本地捕获版本混淆的问题。Snapshot创建后不可原位改写；重新采集必须创建新Snapshot。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填条件 | 可变性 | 校验/责任 |
|---|---|---|---|---|---|
| SNP-001 | `snapshot_id` | SubrecordId / 1 | 总是 | Immutable | M08生成，父对象内唯一 |
| SNP-002 | `source_ref` | Ref<OT-SOURCE> / 1 | 总是 | Immutable | 指向父Source |
| SNP-003 | `snapshot_sequence` | Integer / 1 | 总是 | Immutable | 父Source内单调递增 |
| SNP-004 | `capture_state` | Enum<CaptureState> / 1 | 总是 | AppendOnly | Captured/Partial/Failed/Quarantined |
| SNP-005 | `captured_at` | Instant / 0..1 | 实际捕获时 | Immutable | 内容实际被观察/捕获时间 |
| SNP-006 | `acquired_at` | Instant / 1 | 系统获取时 | Immutable | 系统取得资源时间 |
| SNP-007 | `capture_method` | Enum<CaptureMethod> / 1 | 总是 | Immutable | Manual/Connector/Device/Import |
| SNP-008 | `captured_locator_ref` | SubrecordRef<SourceLocator> / 0..1 | 有定位时 | Immutable | 当次使用的Locator历史记录 |
| SNP-009 | `external_version_token` | String / 0..1 | Provider提供时 | Immutable | ETag/Revision，不作为本地ID |
| SNP-010 | `raw_asset_refs` | Ref<OT-RAW-ASSET> / 0..N | 有原始字节时 | AppendOnly | 附件/部件可多值 |
| SNP-011 | `captured_bytes_digest` | Digest / 0..1 | 有字节时 | Immutable | 明确算法和字节范围 |
| SNP-012 | `digest_scope` | Enum<DigestScope> / 0..1 | 有Digest时 | Immutable | RawBytes/Container/Manifest |
| SNP-013 | `rights_snapshot_ref` | Ref<SourceRightsSnapshot> / 0..1 | 可获得条款快照时 | Immutable | 历史观察，不代表当前权利 |
| SNP-014 | `purpose_ref` | Ref<Purpose> / 1 | 总是 | Immutable | 本次采集Purpose |
| SNP-015 | `policy_decision_ref` | Ref<PolicyDecision> / 1 | 总是 | Immutable | 采集前PEP决策 |
| SNP-016 | `applicable_basis_refs` | Ref<ProcessingBasis> / 0..N | 适用时 | Immutable | Consent仅在适用时引用 |
| SNP-017 | `data_subject_refs` | Ref<DataSubject> / 0..N | 识别到主体时 | Immutable | 支持多主体 |
| SNP-018 | `classification_ref` | Ref<DataClassification> / 1 | 总是 | Immutable | 采集时分类快照 |
| SNP-019 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 总是 | Immutable | 期限由治理决策 |
| SNP-020 | `capture_actor_ref` | Ref<Actor> / 1 | 总是 | Immutable | 人/服务主体 |
| SNP-021 | `recorded_at` | Instant / 1 | 总是 | Immutable | M08登记时间 |
| SNP-022 | `snapshot_manifest_digest` | Digest / 0..1 | 多部件封装时 | Immutable | Snapshot清单摘要 |

## 3. 创建封套与不可变性

创建前完成Actor识别、Purpose声明、来源权利查询、适用处理依据检查、最小化、M18 Policy/PEP判定和必要Approval。Capture结果分为Captured、Partial、Failed或Quarantined；不得把部分捕获标记为完整。

捕获后不允许更新`captured_at`、`external_version_token`、Digest、原始目标和Purpose。发现录入错误时新增Correction记录并保留原值；重新获取内容时创建新Snapshot。

## 4. 版本规则

Snapshot ID是本地稳定身份；`snapshot_sequence`仅在Source内部排序；`external_version_token`是Provider给出的外部令牌；`asset_version`属于KnowledgeAsset；四者不可互换。

## 5. 负向验收

旧Snapshot不得被新抓取覆盖；URL变化不生成新Source；无Purpose/PolicyDecision不得创建完整Snapshot；Digest通过不得推导来源可信；Snapshot删除/撤销需触发下游依赖闭包。