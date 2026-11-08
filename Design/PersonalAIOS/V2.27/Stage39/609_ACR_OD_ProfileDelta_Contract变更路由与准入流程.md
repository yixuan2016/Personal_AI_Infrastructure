# 609｜ACR/OD/Profile Delta/Contract变更路由和准入流程

**状态：** Change Governance Execution Route Candidate；No New Change Approved

## 1. 变更路由决策表

| 变化类型 | 主审议权威 | 必须会审 | 路由 |
|---|---|---|---|
| 仅文字澄清且语义不变 | 文档/字段Owner；M06复核语义不变 | M08（如影响实例解释） | Editorial Clarification |
| 字段语义、类型、基数、缺失、可变性、校验变化 | M06 TDA/SA候选；M08核对实例事实 | 专项Owner按字段域 | Field/Profile Delta |
| 实例写入、生命周期、版本或状态迁移变化 | M08 IA候选 | M06及相关模块 | Instance/State Contract Delta |
| Physical Handle、密钥、备份、Custody、物理删除变化 | M02 | M08、M18、Security/Legal | Physical/Retention Delta |
| Purpose、Consent、Processing Basis、Policy、Classification、Retention变化 | M18 | Personal Owner（适用时）、Privacy/Legal及数据Owner | Policy/Governance Delta |
| Processor/Provider/Region/子处理商/外部副作用变化 | M15事实权威 + M18授权权威 | M08、Security/Privacy/Legal | Provider/Execution Delta |
| Embedding/Index/Context/Cache/Projection变化 | M07 | M08、M18、M06 | Projection/Consumer Delta |
| Connector Receipt原件、采集事实和回执变化 | M17 | M08、M06、目标Owner | Receipt/Source Evidence Delta |
| Command/Query/Event载荷、错误、幂等、并发、兼容性变化 | 契约Owner | Producer、Consumer、M06/M08及相关专业Owner | Contract Change |
| OT数量、对象粒度、全局权威、模块边界或已批准OD变化 | 架构决策流程 | 受影响模块Owner、Personal Owner | ACR；触及OD时进入OD流程 |
| 个人主权、本人目标、价值、Consent或最终确认权变化 | Personal Owner本人 | M18及适用专业审查 | OD/Personal Sovereignty Decision（按既有流程） |

## 2. Profile Delta准入

每项Delta必须引用真实Feedback Record、Atomic Issue、正式Decision Record、前后定义、Field/Relation/Contract范围、Owner、批准证据、消费者影响、Policy/Retention/Deletion影响、测试映射、迁移/回滚和Supersedes链。未获批准的差异只可标Proposed，不覆盖正式定义。

## 3. Contract变更准入

必须识别Producer、全部已知Consumer、读写方向、载荷Schema/Event版本、错误语义、Unknown处理、幂等/并发、权限检查、缓存/删除传播和回滚。消费者清单不完整时兼容性标Unknown并按高风险处理。

## 4. ACR/OD触发

沿用V2.23/516与V2.22/496：改变OT数量、对象粒度、父子关系、唯一权威注册表、模块责任边界、OF-006角色分配或已批准OD时，不得仅作为普通Profile Delta。OD-01=A、OD-02=A、OD-04=B保持既有状态；OD-03继续Pending。任何个人主权变化由Personal Owner本人确认。

## 5. 传播与回滚

批准后依次更新Profile、Relation/Registry、Command/Query/Event、Policy、Consumer、Retention/Deletion、Test、文档索引和Manifest。回滚通过新修订表达，不覆盖历史；涉及外部副作用、已发布Projection或物理数据时必须有补偿与对账计划。

## 6. 当前结论

Stage39未批准任何ACR、OD、Profile Delta或Contract Change；本文件只规定未来变更路径。