# 584｜跨Owner权威冲突、决策依赖与升级规则

**状态：** Cross-Owner Governance Candidate

## 1. 冲突类型

- Semantic Conflict：同一字段/关系的语义定义不一致；
- Instance Authority Conflict：谁可创建/修改实例不一致；
- Policy Conflict：允许用途、访问和保留要求冲突；
- Physical Custody Conflict：逻辑记录与物理字节状态不一致；
- Temporal Conflict：时间/版本顺序无法一致解释；
- Consumer Conflict：Producer和Consumer对缺失值、状态或契约版本解释不同；
- Evidence Conflict：来源证据相互矛盾或批准证据不充分。

## 2. 权威边界

| 领域 | 权威候选 | 不可越权 |
|---|---|---|
| OT/Relation语义 | M06 | 不替M08写入实例事实 |
| OT实例与Snapshot | M08 | 不替M06定义本体语义 |
| 物理字节/Handle/备份 | M02 | 不决定数据处理目的 |
| Projection/Context | M07 | 不形成源知识事实权威 |
| Processor/Provider集成事实 | M15 | 不授予个人数据处理许可 |
| Rights/Purpose/Policy/Retention | M18 | 不伪造实际Provider/物理执行事实 |
| Connector Receipt原件 | M17 | 不自动确认Assertion真实性 |
| Assertion/专业事实 | M06与目标领域Owner | Evidence创建者不自动取得核验权 |

以上为候选权威边界，实际授权范围仍须由组织正式授权材料确认。

## 3. 决策冲突处理顺序

1. 冻结冲突字段/契约的扩大使用，保留原始事实和异议；
2. 拆分Atomic Issue，明确涉及的Field ID、关系、契约和数据范围；
3. 核验每个Owner的身份、授权范围和基线版本；
4. 区分事实争议、语义争议、Policy争议和方案偏好；
5. 收集E0—E4证据并记录反证；
6. 由主决定权威提出裁决，必要会审方出具专业意见；
7. 记录决定、条件、例外、异议和复审触发器；
8. 更新Field Ledger、Decision Register、Contract/Consumer/Test追踪和Manifest。

## 4. 不得采用的处理方式

- 以会议多数票替代有权Owner；
- 以最先回复者替代决定权威；
- 将会审意见等同批准；
- 将“暂时可用”视为语义定稿；
- 用默认值掩盖Owner意见冲突；
- 通过修改字段描述绕开OD/ACR；
- 由AI自动推断批准或代签Decision Record。

## 5. 升级与阻断

若主权威不明确、批准范围冲突、Security/Privacy/Legal提出未关闭的重大风险、跨模块责任无法分离或证据不足，则标记Blocked并升级到既定治理决策层。阻断必须说明影响范围和解除条件，不能无限扩大到无关场景。

## 6. 当前结论

本规则建立统一冲突处理路径，不对任何尚未提交的Owner意见预先裁决。