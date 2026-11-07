# 468｜OT-RAW-ASSET：RawAsset字段级Profile

**对象类型：** OT-RAW-ASSET；**类别：** C1逻辑原始资产候选  
**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）；**物理保管：** M02  
**状态：** Proposed；M02/M08/M18 Review Pending

## 1. 对象职责

RawAsset表示系统登记的一份原始字节内容资产及其逻辑身份。它不是物理文件路径，不是密钥容器，也不是KnowledgeAsset或Evidence。M08维护逻辑身份和来源血缘；M02负责物理字节、加密、备份、密钥和受控访问能力。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| RAW-001 | `raw_asset_id` | ObjectId<OT-RAW-ASSET> / 1 | 是 | Immutable | M08生成 |
| RAW-002 | `raw_asset_kind` | Enum<RawAssetKind> / 1 | 是 | Immutable | File/Attachment/Media/Archive/StructuredPayload |
| RAW-003 | `source_snapshot_refs` | Ref<SourceSnapshot> / 1..N | 是 | AppendOnly | 精确快照引用，不合并权利边界 |
| RAW-004 | `physical_handle_ref` | OpaqueHandle<PhysicalBlob> / 1 | 是 | MutableWithHistory | M02签发，不暴露路径/密钥 |
| RAW-005 | `byte_size` | SizeBytes / 1 | 是 | Immutable | 非负整数，单位Byte |
| RAW-006 | `media_type_declared` | String / 0..1 | 否 | Immutable | 来源声明值，仅作提示 |
| RAW-007 | `media_type_detected` | String / 1 | 是 | Immutable | 内容检测值，保留检测器版本 |
| RAW-008 | `byte_digest` | Digest / 1 | 是 | Immutable | 原始字节摘要 |
| RAW-009 | `digest_algorithm` | Enum<DigestAlgorithm> / 1 | 是 | Immutable | 算法白名单及版本 |
| RAW-010 | `digest_scope` | Enum<DigestScope> / 1 | 是 | Immutable | 明确字节范围/容器结构 |
| RAW-011 | `integrity_state` | Enum<IntegrityState> / 1 | 是 | MutableWithHistory | Unverified/Intact/Changed/Unavailable |
| RAW-012 | `custody_state` | Enum<CustodyState> / 1 | 是 | MutableWithHistory | M02物理保管状态受控投影 |
| RAW-013 | `encryption_profile_ref` | Ref<EncryptionProfile> / 1 | 是 | MutableWithHistory | 仅引用配置，不存密钥 |
| RAW-014 | `classification_ref` | Ref<DataClassification> / 1 | 是 | MutableWithHistory | 原始内容分类 |
| RAW-015 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 是 | MutableWithHistory | 具体期限另行批准 |
| RAW-016 | `created_by_ref` | Ref<Actor> / 1 | 是 | Immutable | 登记主体 |
| RAW-017 | `created_at` | Instant / 1 | 是 | Immutable | 逻辑登记时间 |
| RAW-018 | `object_version` | Version / 1 | 是 | AppendOnly | 乐观并发版本 |
| RAW-019 | `deletion_state_ref` | Ref<DeletionState> / 0..1 | 否 | MutableWithHistory | 删除/撤销传播状态 |
| RAW-020 | `custody_receipt_refs` | Ref<HostCustodyReceipt> / 0..N | 适用时 | AppendOnly | M02操作回执/审计引用 |

## 3. 物理保管契约

M08只能通过M02授权的Opaque Handle请求读取、验证、复制或删除。M08不得保存任意文件系统路径、密钥材料或绕过Host Permission。M02不得因为物理保存字节而取得Source、KnowledgeAsset或Assertion语义权威。

## 4. 重复内容规则

Digest相同可作为内容去重候选，不代表来源、主体、Rights、Purpose、分类或保留策略相同。跨主体/租户/安全域的物理去重必须避免通过命中/未命中响应泄露其他主体是否持有相同内容。

## 5. 删除与待决项

RawAsset逻辑删除和物理字节销毁是两个可审计步骤。删除流程须记录M02执行回执、KnowledgeAsset/Chunk/Evidence/Projection依赖和备份例外。待确认事项包括Opaque Handle格式、Custody State映射、加密配置引用、跨租户去重、Digest算法白名单、删除回执结构和物理清除验证方法。

## 6. 负向验收

M08读取密钥；RawAsset路径作为稳定ID；Digest相同导致权利合并；M08逻辑删除后物理副本仍可读取；物理保管成功被误认为KnowledgeAsset已核验。