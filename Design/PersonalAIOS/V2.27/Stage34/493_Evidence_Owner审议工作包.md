# 493｜Evidence Owner审议工作包

**状态：** Field-level Review Pack Prepared；Owner Decision Pending  
**审议对象：** Evidence  
**本包字段定义数：** 22

## 1. 对象边界与权威候选

M08维护Evidence身份、类型化目标、定位和完整性；M06维护Evidence—Assertion语义关系及核验。

候选角色沿用312号OF-006既有分配：IA=M08；TDA/SA=M06。凡涉及M02物理保管、M18策略治理、M15 Provider/Region、M17 Receipt或M07 Projection/Context的议题，必须由对应模块在其权限范围内独立审议。此处复述候选角色不构成新增批准。

## 2. 字段逐项审议清单

以下清单逐项对应V2.21字段Profile，不表示任何字段已获批准。每个字段至少核对：语义定义、类型、Cardinality、必填条件、缺失语义、可变性、写入权威、敏感度、校验、版本影响、血缘、删除和兼容性。

| Field ID | 字段 | Owner审议焦点 | 应提供的证据 | 候选审议方 |
|---|---|---|---|---|
| `EVD-001` | `evidence_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `EVD-002` | `evidence_kind` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `EVD-003` | `evidence_target_ref` | 确认完整性仅针对精确目标/片段，不推导Assertion已核验 | 目标版本、Locator、Digest及M06交接证据 | M06 / M08 |
| `EVD-004` | `target_version_ref` | 确认完整性仅针对精确目标/片段，不推导Assertion已核验 | 目标版本、Locator、Digest及M06交接证据 | M06 / M08 |
| `EVD-005` | `locator_schema_ref` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `EVD-006` | `locator_payload` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `EVD-007` | `target_content_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `EVD-008` | `locator_fragment_digest` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `EVD-009` | `excerpt_ref` | 确认完整性仅针对精确目标/片段，不推导Assertion已核验 | 目标版本、Locator、Digest及M06交接证据 | M06 / M08 |
| `EVD-010` | `excerpt_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `EVD-011` | `integrity_state` | 确认完整性仅针对精确目标/片段，不推导Assertion已核验 | 目标版本、Locator、Digest及M06交接证据 | M06 / M08 |
| `EVD-012` | `lifecycle_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `EVD-013` | `created_by_ref` | 确认Actor/Service身份、发起者与执行者区分及审计最小化 | 身份目录映射、授权主体和审计事件样例 | M08 / M18 |
| `EVD-014` | `created_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `EVD-015` | `recorded_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `EVD-016` | `classification_ref` | 确认对象/字段/片段/派生物分类继承与提高规则，禁止降级 | 分类目录映射、继承/提高案例 | M18；Security/Privacy |
| `EVD-017` | `purpose_lineage_refs` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `EVD-018` | `retention_profile_ref` | 确认保留策略引用、期限来源、例外与删除传播，不在Profile中硬编码期限 | Retention Profile目录和例外审批路径 | M18；Privacy/Legal |
| `EVD-019` | `object_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `EVD-020` | `withdrawal_reason_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `EVD-021` | `deletion_state_ref` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `EVD-022` | `captured_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |

## 3. 本对象关键审议焦点

1. EVD-003/004：唯一主Target分支及精确Target Version必须同时存在。
2. EVD-005/006：Locator Schema和坐标载荷必须可版本化、可解析。
3. EVD-007/008/010：目标摘要、片段摘要和Excerpt摘要不能互换。
4. EVD-009/016/017：Excerpt最小必要；分类和历史Purpose不替代当前Policy。
5. EVD-011/012/020/021：完整性、生命周期、撤销和删除是独立状态维度。
6. Receipt/Observation目标必须引用实际Owner原件，不复制权威。

## 4. 必须形成原子决策的议题

- EvidenceTargetRef联合分支与目标类型注册
- Locator解析和重定位
- Digest范围/算法/规范化
- Excerpt准入与最小必要
- M06 Assertion关系/核验权威
- M17 Receipt及Observation原Owner引用

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
