# 491｜ExtractionRun Owner审议工作包

**状态：** Field-level Review Pack Prepared；Owner Decision Pending  
**审议对象：** ExtractionRun  
**本包字段定义数：** 25

## 1. 对象边界与权威候选

ExtractionRun是一次有界处理记录；运行成功不等于输出真实、正确或已被核验。

候选角色沿用312号OF-006既有分配：IA=M08；TDA/SA=M06。凡涉及M02物理保管、M18策略治理、M15 Provider/Region、M17 Receipt或M07 Projection/Context的议题，必须由对应模块在其权限范围内独立审议。此处复述候选角色不构成新增批准。

## 2. 字段逐项审议清单

以下清单逐项对应V2.21字段Profile，不表示任何字段已获批准。每个字段至少核对：语义定义、类型、Cardinality、必填条件、缺失语义、可变性、写入权威、敏感度、校验、版本影响、血缘、删除和兼容性。

| Field ID | 字段 | Owner审议焦点 | 应提供的证据 | 候选审议方 |
|---|---|---|---|---|
| `EXT-001` | `extraction_run_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `EXT-002` | `run_kind` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `EXT-003` | `input_refs` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `EXT-004` | `input_digest_refs` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `EXT-005` | `processor_kind` | 确认处理器/版本/Provider/实际区域/配置摘要与每次Invocation绑定 | Processor目录、Provider条款版本、区域与外发审查记录 | M15 / M18；Security |
| `EXT-006` | `processor_ref` | 确认处理器/版本/Provider/实际区域/配置摘要与每次Invocation绑定 | Processor目录、Provider条款版本、区域与外发审查记录 | M15 / M18；Security |
| `EXT-007` | `processor_version_ref` | 确认处理器/版本/Provider/实际区域/配置摘要与每次Invocation绑定 | Processor目录、Provider条款版本、区域与外发审查记录 | M15 / M18；Security |
| `EXT-008` | `configuration_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `EXT-009` | `purpose_ref` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `EXT-010` | `actor_or_service_ref` | 确认Actor/Service身份、发起者与执行者区分及审计最小化 | 身份目录映射、授权主体和审计事件样例 | M08 / M18 |
| `EXT-011` | `policy_decision_ref` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `EXT-012` | `provider_profile_ref` | 确认处理器/版本/Provider/实际区域/配置摘要与每次Invocation绑定 | Processor目录、Provider条款版本、区域与外发审查记录 | M15 / M18；Security |
| `EXT-013` | `provider_region_ref` | 确认处理器/版本/Provider/实际区域/配置摘要与每次Invocation绑定 | Processor目录、Provider条款版本、区域与外发审查记录 | M15 / M18；Security |
| `EXT-014` | `started_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `EXT-015` | `completed_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `EXT-016` | `run_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `EXT-017` | `output_refs` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `EXT-018` | `output_manifest_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `EXT-019` | `error_class` | 确认失败分类、UnknownOutcome、重试/幂等作用域和跨模块追踪 | 错误码目录、同Key不同Payload及未知结果案例 | M08 / M15 |
| `EXT-020` | `retry_of_ref` | 确认失败分类、UnknownOutcome、重试/幂等作用域和跨模块追踪 | 错误码目录、同Key不同Payload及未知结果案例 | M08 / M15 |
| `EXT-021` | `idempotency_scope_ref` | 确认失败分类、UnknownOutcome、重试/幂等作用域和跨模块追踪 | 错误码目录、同Key不同Payload及未知结果案例 | M08 / M15 |
| `EXT-022` | `correlation_id` | 确认失败分类、UnknownOutcome、重试/幂等作用域和跨模块追踪 | 错误码目录、同Key不同Payload及未知结果案例 | M08 / M15 |
| `EXT-023` | `resource_usage_summary` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `EXT-024` | `retention_profile_ref` | 确认保留策略引用、期限来源、例外与删除传播，不在Profile中硬编码期限 | Retention Profile目录和例外审批路径 | M18；Privacy/Legal |
| `EXT-025` | `object_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |

## 3. 本对象关键审议焦点

1. EXT-003/004：所有输入必须绑定精确版本和对应Digest范围。
2. EXT-006/007/008：Processor、Processor Version与配置摘要不可混用，配置摘要不得泄露秘密。
3. EXT-009/011：每次运行必须绑定当前Purpose和运行前PolicyDecision。
4. EXT-012/013：Provider与Region记录实际Invocation，不允许以默认区域代替实际处理地。
5. EXT-016/017/018/019：Succeeded/Partial/Failed/UnknownOutcome必须可区分，输出清单可校验。
6. EXT-020/021：重试创建新Run并保留retry_of；幂等键不同Payload必须拒绝。

## 4. 必须形成原子决策的议题

- Processor目录和版本治理
- Provider/Region/Retention/训练再利用条款
- 沙箱、网络、文件系统和恶意文件隔离
- UnknownOutcome与外部副作用对账
- Partial输出发布限制
- 资源用量和日志最小化

每项议题应单独登记Decision ID，不得用“本对象整体通过”掩盖字段级保留意见。建议至少形成以下结论之一：Retain、Revise、Split、Merge、Deprecate、Remove、Defer、Need-ACR或Blocked。

## 5. 需要提交的审议证据

- 当前Profile版本和字段清单；
- 引用目标在既有Object Type Registry/词汇目录/父对象子记录中的解析证据；
- 字段权威、写入者、读取者及PEP控制映射；
- 正向和负向合成样例；
- 对下游Command/Query/Event、Projection、删除和备份恢复的影响；
- 异议、例外、风险接受及批准范围。

## 6. 审议结束条件

1. 每个字段均有审议状态和处置建议；
2. 所有Required/Unknown/Withheld/Empty等缺失语义得到明确处理；
3. 跨Owner字段均有实际有权Owner确认或明确标记Blocked；
4. 所有未决项均有责任人、依赖、后续动作和目标版本；
5. 批准结论有可核验的Approval Evidence Ref。

## 7. 当前结论

本包仅完成审议准备。没有真实Owner决议证据时，所有字段仍为Proposed，所有OT仍为Candidate。不得把本清单当作签署表或冻结批准。
