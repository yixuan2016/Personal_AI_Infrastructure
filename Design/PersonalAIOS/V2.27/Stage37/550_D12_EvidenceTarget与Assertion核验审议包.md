# 550｜D-12 Evidence Target与Assertion核验：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

Evidence负责保存可定位、可追溯的证据引用与完整性信息；Assertion负责表达某个主体提出的事实主张及其核验状态。Evidence Target如果没有明确类型、版本和定位坐标，无法稳定复核；如果把Evidence存在或Digest匹配直接映射为Assertion Verified，就会把技术完整性错误地提升为事实真实性。

## 2. 关联字段与权威边界

- EVD-003 evidence_target_ref
- EVD-004 target_version_ref
- EVD-005 locator_schema_ref
- EVD-006 locator_payload
- EVD-007 target_content_digest
- EVD-008 locator_fragment_digest
- EVD-009 excerpt_ref
- EVD-010 excerpt_digest
- EVD-011 integrity_state
- EVD-020 withdrawal_reason_ref

主决定权威候选：M06负责Evidence/Assertion语义与核验状态；M08负责Evidence实例、版本引用和生命周期；M17负责Receipt原件及Connector来源事实；目标对象Owner负责确认目标内容的业务权威。

## 3. 必须回答的问题

1. evidence_target_ref允许指向哪些已注册对象和子记录？如何拒绝未注册或含糊目标？
2. target_version_ref是否必须固定目标版本，哪些目标允许指向动态当前版本？
3. locator_schema_ref和locator_payload如何表达页码、段落、时间戳、消息ID、表格单元格或媒体时间轴？
4. Locator是否仅用于定位而不承担访问授权？敏感路径和凭据如何隔离？
5. target_content_digest、locator_fragment_digest和excerpt_digest分别摘要什么内容？
6. integrity_state如何表达可验证、失效、未知或无法访问，而不混入Assertion状态？
7. Assertion的提出、支持、反驳、核验、撤回和过期由谁负责？
8. Evidence撤回、目标版本被替代或目标删除时，相关Assertion如何重新评估？

## 4. 候选方案（不构成推荐或批准）

- A：Evidence Target采用类型化引用并固定版本，Locator通过版本化Schema表达；Assertion核验由独立流程处理。
- B：允许目标引用动态解析，但每次核验都保存解析结果和目标版本快照；适用于动态来源，但审计要求更高。
- C：只保存URL/文本片段和摘要；实现简单，但无法可靠支持复杂目标、版本变更和长期复核。

## 5. 必须提供的证据

- Evidence Target联合类型目录和允许目标Registry；
- 不同媒介Locator Schema及合成定位样例；
- M17 Receipt原件引用和来源身份说明；
- Digest Scope、算法和目标版本对应关系；
- Assertion核验流程、责任人、反证和撤回案例；
- Evidence失效、撤回、删除与派生结论更新规则。

## 6. 下游影响与测试

影响事实主张、长期记忆、知识问答、决策证据、审计和RSI评估。任何面向用户的事实结论都必须能区分“存在证据引用”“证据可定位”“完整性已校验”“来源已确认”“Assertion已核验”。

测试覆盖目标不存在、目标版本漂移、Locator解析歧义、片段摘要不匹配、Digest匹配但来源未知、Evidence撤回、Assertion未重新核验、Receipt权威错误和删除后残留结论。

## 7. 阻断条件

目标类型不受控；目标版本不明确；Locator被误当作授权；Digest语义混淆；Assertion核验由Evidence创建者自动完成；撤回后下游结论未更新。

## 8. 当前状态

本文件仅形成D-12审议准备包。没有真实Owner反馈或批准证据；EVD-003至EVD-011及EVD-020继续保持Pending。