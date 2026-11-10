# 470｜OT-EXTRACTION-RUN：ExtractionRun字段级Profile

**对象类型：** OT-EXTRACTION-RUN；**类别：** C2有界运行记录候选；**候选IA：** M08；**候选TDA/SA：** M06（依据312号OF-006角色分配）  
**状态：** Proposed；M02/M08/M06/M18/M15 Review Pending

## 1. 对象职责

ExtractionRun记录一次有界、可追踪的解析/抽取/转写/规范化任务。它说明“系统如何处理输入”，不证明输出内容正确，也不成为长期事实来源。运行记录须有明确输入版本、处理器版本、配置摘要、Purpose、Policy和输出引用。

## 2. 字段级Profile

| Field ID | 字段 | 类型 / 基数 | 必填 | 可变性 | 权威/校验 |
|---|---|---|---|---|---|
| EXT-001 | `extraction_run_id` | ObjectId<OT-EXTRACTION-RUN> / 1 | 是 | Immutable | M08生成 |
| EXT-002 | `run_kind` | Enum<ExtractionKind> / 1 | 是 | Immutable | Parse/OCR/Transcribe/Normalize |
| EXT-003 | `input_refs` | TypedRefUnion / 1..N | 是 | Immutable | 每个输入带精确版本 |
| EXT-004 | `input_digest_refs` | Ref<DigestRecord> / 1..N | 是 | Immutable | 对应每个输入范围 |
| EXT-005 | `processor_kind` | Enum<ProcessorKind> / 1 | 是 | Immutable | Parser/OCR/ASR/Extractor |
| EXT-006 | `processor_ref` | Ref<ProcessorDefinition> / 1 | 是 | Immutable | 处理器身份 |
| EXT-007 | `processor_version_ref` | Ref<ProcessorVersion> / 1 | 是 | Immutable | 处理器精确版本 |
| EXT-008 | `configuration_digest` | Digest / 1 | 是 | Immutable | 配置摘要，不存秘密配置 |
| EXT-009 | `purpose_ref` | Ref<Purpose> / 1 | 是 | Immutable | 当前运行用途 |
| EXT-010 | `actor_or_service_ref` | Ref<ActorOrService> / 1 | 是 | Immutable | 发起/执行主体 |
| EXT-011 | `policy_decision_ref` | Ref<PolicyDecision> / 1 | 是 | Immutable | 运行前PEP决策 |
| EXT-012 | `provider_profile_ref` | Ref<ProviderProfile> / 0..1 | 外部处理时 | Immutable | Provider身份/条款版本 |
| EXT-013 | `provider_region_ref` | Ref<Region> / 0..1 | Provider处理时 | Immutable | 实际处理区域 |
| EXT-014 | `started_at` | Instant / 0..1 | 开始运行时 | Immutable | 实际开始时间 |
| EXT-015 | `completed_at` | Instant / 0..1 | 终态时 | Immutable | 完成/失败时间 |
| EXT-016 | `run_state` | Enum<RunState> / 1 | 是 | MutableWithHistory | Queued/Running/Succeeded/Failed/Partial/Cancelled |
| EXT-017 | `output_refs` | TypedRefUnion / 0..N | 有输出时 | AppendOnly | 输出对象及版本 |
| EXT-018 | `output_manifest_digest` | Digest / 0..1 | 有输出清单时 | Immutable | 输出集合完整性 |
| EXT-019 | `error_class` | Enum<RunErrorClass> / 0..1 | 失败/部分时 | Immutable | 稳定错误类别 |
| EXT-020 | `retry_of_ref` | Ref<OT-EXTRACTION-RUN> / 0..1 | 重试时 | Immutable | 原Run引用 |
| EXT-021 | `idempotency_scope_ref` | Ref<IdempotencyScope> / 1 | 是 | Immutable | 不暴露原始幂等秘密 |
| EXT-022 | `correlation_id` | String / 1 | 是 | Immutable | 跨模块追踪 |
| EXT-023 | `resource_usage_summary` | StructuredValue / 0..1 | 采集到时 | Immutable | 最小化资源/用量信息 |
| EXT-024 | `retention_profile_ref` | Ref<RetentionProfile> / 1 | 是 | Immutable | 运行记录保留规则 |
| EXT-025 | `object_version` | Version / 1 | 是 | AppendOnly | 运行状态版本 |

## 3. 状态约束

Run创建后按状态机推进。Succeeded必须有输出校验记录；Partial必须列出已完成与缺失输出；Failed不得发布部分输出为Ready；Cancelled记录取消主体与原因；Unknown Provider Outcome不得伪装为Failed或Succeeded。

## 4. 幂等与安全边界

幂等范围由`run_kind + input_refs/versions + processor_version + configuration_digest + purpose_ref`组成。相同范围可复用既有结果；输入、处理器、配置或Purpose变化时创建新Run。Parser/OCR/ASR运行环境需具备资源限额、超时、网络默认关闭、文件系统隔离、宏/脚本禁用、恶意文件隔离和Prompt Injection数据边界。

## 5. 负向验收

无精确输入版本；处理器版本缺失；无Purpose/PolicyDecision；输出无摘要/引用；部分成功被标记Succeeded；重试覆盖原Run；文档指令触发工具或网络动作。
