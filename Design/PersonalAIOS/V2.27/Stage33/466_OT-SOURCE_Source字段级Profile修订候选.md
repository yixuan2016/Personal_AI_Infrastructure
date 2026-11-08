# 466｜OT-SOURCE：Source字段级Profile修订候选

**对象类型：** OT-SOURCE；**类别：** C1权威持久对象候选；**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）  
**状态：** Proposed；M08/M02/M18 Owner Review Pending

## 1. 对象职责

Source标识稳定来源主体或外部资源身份，回答“来源是谁、原始来源权威是谁、通过哪些定位方式可以访问”。Source不代表某次采集，不代表本地文件字节，不代表内容真实，也不授予未来处理权限。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| SRC-001 | `source_id` | ObjectId<OT-SOURCE> / 1 | 是 | ImmutableAfterCreate | M08生成，全局唯一 |
| SRC-002 | `source_kind` | Enum<SourceKind> / 1 | 是 | MutableWithHistory | M08受控枚举 |
| SRC-003 | `source_authority_ref` | Ref<ActorOrProvider> / 1 | 是 | MutableWithHistory | 原始来源权威，不默认指向M08 |
| SRC-004 | `origin_identity_ref` | StructuredValue / 1 | 是 | ImmutableAfterCreate | 命名空间、外部主体、稳定资源ID |
| SRC-005 | `locator_refs` | SubrecordRef<SourceLocator> / 0..N | 否 | AppendOnly | Locator可失效，不作为唯一身份 |
| SRC-006 | `availability_state` | Enum<SourceAvailability> / 1 | 是 | MutableWithHistory | Reachable/Unavailable/Unknown/Revoked |
| SRC-007 | `lifecycle_state` | Enum<SourceLifecycle> / 1 | 是 | MutableWithHistory | Registered/Active/Superseded/Retired |
| SRC-008 | `source_rights_refs` | Ref<SourceRightsRecord> / 0..N | 否 | AppendOnly | 来源条款/许可证/合同，不等于Consent |
| SRC-009 | `data_subject_refs` | Ref<DataSubject> / 0..N | 否 | MutableWithHistory | 适用时多主体、受限读取 |
| SRC-010 | `classification_ref` | Ref<DataClassification> / 1 | 是 | MutableWithHistory | 不低于来源内容敏感度 |
| SRC-011 | `created_by_ref` | Ref<Actor> / 1 | 是 | ImmutableAfterCreate | 登记Actor，不代表来源权威 |
| SRC-012 | `created_at` | Instant / 1 | 是 | ImmutableAfterCreate | M08记录时间 |
| SRC-013 | `updated_at` | Instant / 1 | 是 | MutableWithHistory | 每次变更更新 |
| SRC-014 | `object_version` | Version / 1 | 是 | AppendOnly | 单调递增 |
| SRC-015 | `supersedes_source_ref` | Ref<OT-SOURCE> / 0..1 | 否 | ImmutableAfterCreate | 仅经审议的身份纠错/合并 |

## 3. SourceLocator嵌入式子记录

SourceLocator不是独立OT。字段候选：`locator_id`、`locator_kind`、`locator_value_ref`（敏感值受控）、`namespace_ref`、`valid_from`、`valid_to`、`observed_at`、`availability_state`、`credential_profile_ref`（不存凭据）、`last_verified_at`、`recorded_at`。Locator历史采用AppendOnly；更新时新增记录并将旧记录标记失效，不覆盖历史。

## 4. 身份约束

`origin_identity_ref`至少包含`authority_namespace`、`authority_instance_ref`和`external_resource_id`。本地导入没有外部ID时，使用受控LocalImportNamespace和本地稳定ID。不得使用文件名、URL、标题或内容Digest作为唯一身份。

## 5. 不变量

1. Source ID不因Locator变化而改变。
2. 同一外部对象的不同内容版本属于同一Source的不同Snapshot。
3. 同URL不同内容不能覆盖旧Snapshot。
4. Source可达不等于Rights允许、Consent有效或Policy Allow。
5. 同字节不等于同Source、同主体或同权利。
6. Source Retired不自动删除历史Snapshot。

## 6. 决策待Owner确认

SourceKind枚举范围、Provider命名空间唯一性、多主体策略、Source合并/拆分规则、SourceRightsRecord目标类型、Locator敏感值保管方式、Retired与Withdrawn的精确定义。以上均未获批准。