# 465｜S1字段级Profile统一规范：字段类型、Cardinality、缺失语义与校验

**状态：** Field Contract Standard Candidate；No Physical Schema Freeze

## 1. 字段定义最小契约

每个字段必须有唯一`field_id`，并定义：`canonical_name`、`semantic_definition`、`value_type`、`cardinality`、`required_when`、`missing_semantics`、`authority_owner`、`write_policy`、`mutability`、`classification_ref`、`validation_rules`、`temporal_semantics`、`version_impact`、`lineage_behavior`、`deletion_behavior`和`compatibility_class`。缺少关键定义时只能标记Draft。

## 2. 规范类型词汇

| 类型 | 语义 | 约束 |
|---|---|---|
| `ObjectId<T>` | 某OT实例稳定身份 | 包含类型命名空间，不以展示名作为身份 |
| `Ref<T>` | 指向某个权威对象 | 目标类型明确；跨Owner只保存Ref |
| `SubrecordRef<T>` | 父对象下不可变子记录 | 由父Owner维护，不自动成为OT |
| `Enum<E>` | 有版本的受控枚举 | 新值需兼容审议 |
| `String` | 文本值 | 明确长度、规范化、语言和敏感度 |
| `URI` | 定位地址 | 不作为稳定身份 |
| `Digest` | 内容摘要 | 附算法、范围、规范化规则和时间 |
| `Instant` | 时间点 | 带时区/偏移，推荐RFC 3339 |
| `TimeInterval` | 时间区间 | 明确边界、时区和精度 |
| `SizeBytes` | 字节长度 | 单位固定为Byte |
| `OpaqueHandle<T>` | 受控能力句柄 | 不可解析为物理路径或密钥 |
| `StructuredValue` | 结构化值对象 | 必须有Schema ID和Version |
| `TypedRefUnion` | 多类型联合引用 | 必须且仅有一个主分支 |
| `Map<K,V>` | 键值集合 | Key受控，禁止无界任意载荷 |
| `Boolean` | 二值 | 不得用False代表Unknown |
| `Decimal` | 精确数值 | 明确精度、单位和舍入规则 |

## 3. Cardinality规范

- `1`：恰好一个，缺失即不合法；
- `0..1`：可选一个，缺失需有明确语义；
- `1..N`：至少一个，声明顺序是否有意义；
- `0..N`：可为空集合，Empty与Absent区分；
- `N:M`：通过显式关系记录表达，不以重复文本字段隐式表达。

## 4. 缺失语义

| 语义 | 含义 |
|---|---|
| Absent | 未提供或字段不存在 |
| Unknown | 有意义但当前未知，不得转为False |
| Null | 明确记录空值，仅适用于允许Null的字段 |
| NotApplicable | 当前对象/场景不适用 |
| Withheld | 有值但当前Actor无权查看 |
| Redacted | 内容已脱敏或按规则清除 |
| Empty | 明确空集合/空文本 |
| Invalid | 值违反约束，不得静默修复 |

## 5. 可变性类别

`ImmutableAfterCreate`（创建后不可更改）；`AppendOnly`（只允许追加）；`MutableWithHistory`（变更保留版本和审计）；`DerivedRebuildable`（可重建派生产物）；`Ephemeral`（有界临时记录，受Retention约束）。

## 6. 时间、引用与版本

`captured_at`、`acquired_at`、`observed_at`、`processed_at`、`recorded_at`、`effective_at`、`expires_at`不可互换。对象引用包含目标OT、对象ID和必要版本/子记录ID。`object_version`、`asset_version`、`run_version`、`schema_version`、`policy_version`、`contract_version`和`provider_version`分别治理。

## 7. 敏感度与校验

字段敏感度不得低于实际内容敏感度；标题、Locator、摘要、Digest、Embedding、日志和错误信息也可能敏感。每个字段至少定义格式校验、引用完整性、业务不变量、时间、权限和版本校验。校验失败返回稳定错误码，不得自动把Unknown转成默认值。

## 8. 兼容性分类

`AdditiveOptional`、`AdditiveRequired`、`SemanticChange`、`TypeChange`、`Rename`、`Deprecation`、`Removal`。除AdditiveOptional外，均需影响分析、迁移方案和目标Owner批准。


## 9. 引用目标解析与禁止隐式新增OT

字段表中的`Ref<T>`类型名称是语义目标别名，不自动代表一个已注册OT。Owner批准前，每个目标必须映射到现有Object Type Registry、受控词汇/配置目录、父对象子记录或明确的跨模块引用契约。映射未完成时标记`ReferenceTargetPending`，不得通过字段命名隐式创建新OT。

| 引用别名 | 允许的解析方向 | 本阶段约束 |
|---|---|---|
| Purpose / PolicyDecision / Actor | 既有治理与身份目录/OT | 复用既有权威，不新建类型 |
| DataClassification / RetentionProfile | 既有分类、保留策略目录 | 与208、113、226号规范对齐；不把Profile引用当作执行结果 |
| DataSubject | 既有Person/主体引用体系 | 支持多主体，不由当前用户替第三方授权 |
| SourceRightsRecord / SourceRightsSnapshot | 来源条款登记项或Source子记录 | 尚需M08/M18映射；不得新增独立OT |
| ProcessingBasis | 治理依据目录/受控枚举或引用 | 需M18/Privacy/Legal确认；不得伪造Consent |
| ProcessorDefinition / ProcessorVersion / ProviderProfile / Region | M15现有Provider/模型注册目录或外部标准引用 | 必须映射到既有目录和版本；不得创建新的知识资产权威 |
| ChunkingStrategyVersion | M08受控处理配置/版本目录 | 作为配置引用，不新增OT |
| SourceLocator / SourceSnapshot / KnowledgeAssetVersion / ChunkSet | 对应父OT的子记录 | 不单独登记为OT |
| DeletionState / IdempotencyScope / DigestRecord | 状态枚举、治理记录或契约封套 | 仅在现有规范中映射；不自动创建持久对象类型 |
| HostCustodyReceipt / OperationReceipt | M02能力调用回执或审计引用 | 不得与M17 ConnectorReceipt混同；原始回执由其实际Owner维护 |
| Language / Reason / DigestAlgorithm | 受控词汇表 | 采用版本化枚举，不自由扩展 |

如果现有目录中不存在某个目标，必须先在Owner审议材料中登记缺口，确定是字段、枚举、子记录、关系还是未来ACR候选。未完成这一步前，不得把该Ref当作已存在的OT或已批准接口。
