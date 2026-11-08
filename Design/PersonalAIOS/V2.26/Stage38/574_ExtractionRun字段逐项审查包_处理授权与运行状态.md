# 574｜ExtractionRun字段逐项审查包：处理授权与运行状态

**状态：** Field-Level Design Review Candidate；Owner Feedback 25/25 Pending；No Approval

## 1. 对象边界

ExtractionRun记录一次处理尝试的事实，不等于逻辑任务、Processor定义或Provider合同。输入、配置、授权、外部执行、输出持久化和业务发布必须可区分。D-09/D-10为主决策，D-04贯穿用途和授权。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| EXT-001 | `extraction_run_id` | extraction_run_id是否为单次尝试ID；逻辑任务ID和Provider Operation ID是否另设。 | D-09/D-10 |
| EXT-002 | `run_kind` | run_kind如何区分采集、抽取、转换、摘要、嵌入等处理意图。 | D-09/D-10 |
| EXT-003 | `input_refs` | input_refs是否固定对象及版本；多输入顺序和缺失输入如何表达。 | D-08/D-10 |
| EXT-004 | `input_digest_refs` | input_digest_refs是否覆盖全部输入及规范化Scope；防止输入漂移。 | D-08/D-10 |
| EXT-005 | `processor_kind` | processor_kind是否为受控类别；本地/外部/人工混合流水线如何表达。 | D-09/D-10 |
| EXT-006 | `processor_ref` | processor_ref指向逻辑处理器、部署还是服务实例；身份层级必须明确。 | D-09 |
| EXT-007 | `processor_version_ref` | processor_version_ref如何固定模型/服务版本；静默升级和灰度路由如何留证。 | D-09 |
| EXT-008 | `configuration_digest` | configuration_digest覆盖哪些参数；秘密、令牌和个人数据不得进入普通摘要明文。 | D-09 |
| EXT-009 | `purpose_ref` | purpose_ref绑定本次运行的具体目的；不能继承成永久通用授权。 | D-04/D-09 |
| EXT-010 | `actor_or_service_ref` | actor_or_service_ref区分发起主体、执行主体和Provider；委托关系如何追踪。 | D-04/D-09 |
| EXT-011 | `policy_decision_ref` | policy_decision_ref是否绑定输入、Action、Purpose、Provider、Region和Policy版本。 | D-04/D-09 |
| EXT-012 | `provider_profile_ref` | provider_profile_ref固定合同/能力/子处理商条款版本；Profile更新不得改写历史。 | D-09 |
| EXT-013 | `provider_region_ref` | provider_region_ref区分请求地区、计算地区、存储/日志/人工访问地区。 | D-09 |
| EXT-014 | `started_at` | started_at由本地还是Provider记录；时钟偏差和重试尝试如何处理。 | D-09/D-10 |
| EXT-015 | `completed_at` | completed_at表示外部执行结束还是本地落库完成；未知结果不得伪造完成时间。 | D-09/D-10 |
| EXT-016 | `run_state` | run_state是否把调度、外部执行、结果持久化和业务发布分离。 | D-10 |
| EXT-017 | `output_refs` | output_refs是否仅包含已登记且可验证的输出；部分输出如何隔离。 | D-10/D-11 |
| EXT-018 | `output_manifest_digest` | output_manifest_digest覆盖哪些输出及顺序；如何证明输出集合完整。 | D-10/D-11 |
| EXT-019 | `error_class` | error_class是否区分可重试、不可重试、未知结果和部分副作用。 | D-10 |
| EXT-020 | `retry_of_ref` | retry_of_ref表示直接前序尝试还是逻辑重试链；循环和分叉如何处理。 | D-10 |
| EXT-021 | `idempotency_scope_ref` | idempotency_scope_ref绑定任务、输入版本、配置和Provider；键有效期如何管理。 | D-10 |
| EXT-022 | `correlation_id` | correlation_id跨模块与Provider串联是否稳定且避免碰撞/敏感信息泄露。 | D-10 |
| EXT-023 | `resource_usage_summary` | resource_usage_summary区分单次尝试、逻辑任务和Provider账单；估算与实耗分离。 | D-09/D-10 |
| EXT-024 | `retention_profile_ref` | retention_profile_ref覆盖输入副本、输出、日志、临时文件和Provider缓存的哪一范围。 | D-09/D-10 |
| EXT-025 | `object_version` | object_version只表示Run记录修订；不能代替状态迁移历史。 | D-09/D-10 |

## 3. 对象内一致性约束

- extraction_run_id标识单次尝试；correlation_id标识跨组件链路；Provider Operation ID是外部服务标识，不能混用。
- 输入引用与Digest必须固定到具体版本和Scope。
- processor_ref/version、configuration_digest、provider_profile_ref和provider_region_ref分别表达处理器身份、版本、配置、Provider条款和实际区域事实。
- purpose_ref和policy_decision_ref必须绑定本次Run；历史授权不构成永久许可。
- run_state必须区分本地调度、Provider执行、输出持久化和业务发布。
- UnknownOutcome期间output_refs不得进入可检索/可发布状态。
- retry_of_ref与idempotency_scope_ref需要稳定作用域；重复副作用必须对账。
- resource_usage_summary需区分估算、单次尝试实耗和Provider账单。

## 4. 当前结论

25/25字段完成设计审查问题登记；Owner状态25/25 Pending；无Provider、Region、Retry策略或ExtractionRun字段获批。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 25/25 与Stage35原始台账一致 |
| 语义审查问题 | 25/25 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。