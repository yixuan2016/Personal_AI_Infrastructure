# 527｜D-02 Locator多值、历史与失效：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

Locator可能是URL、文件位置、消息定位符、数据库记录地址或其他可解析引用。当前定位符、采集时定位符、历史定位符和访问凭据不是同一概念。把Locator当作永久身份或授权凭据，会造成失效、泄密、错误回溯和权限绕过。

## 2. 关联字段与权威边界

- SRC-005 locator_refs
- SNP-008 captured_locator_ref
- 主审议候选：M08负责Locator引用维护，M06负责Locator语义；必须会审M18及Security；涉及Connector读取时引入M17。

## 3. 必须回答的问题

1. locator_refs是当前可用引用集合、历史引用集合，还是两者兼有？如何区分主用、备用、失效和撤销？
2. SNP-008是否记录采集当时使用的精确Locator快照，而不是回写为当前Locator？
3. Locator的有效期、发现时间、最后验证时间和失效原因应由谁记录？
4. 访问令牌、Cookie、签名URL、个人路径等秘密是否明确禁止进入普通Locator字段？
5. Locator重定向、域名变更、资源迁移和内容替换如何保留历史语义？

## 4. 候选方案（不构成推荐或批准）

- A：Locator采用引用对象/引用记录，当前与历史版本分开管理；可追溯性强，但需要完整引用生命周期治理。
- B：Locator作为Source上的多值字段并附状态和时间；结构较轻，但历史版本、快照和凭据隔离要求更严格。
- C：只保留单一当前Locator，历史定位信息只放入Snapshot；实现简单，但对来源迁移和多入口场景支持有限。

## 5. 必须提供的证据

- 各类Source的Locator样例和格式约束；
- 重定向、失效、撤销、迁移、同一内容多Locator和同一Locator内容变化样例；
- M17 Connector读取契约及凭据处理边界；
- Locator中秘密信息、个人路径和敏感参数的风险分析；
- 历史Snapshot与当前Source定位符的对账样例。

## 6. 下游影响与测试

影响Source查询、Connector读取、Snapshot采集、Evidence定位、审计回溯和删除流程。消费者必须知道读取的是当前Locator还是历史Locator，不能把可访问性当作合法授权。

测试覆盖Locator新增/失效/撤销、重定向、内容替换、凭据泄漏拦截、历史Locator保留、SNP-008不可被当前Locator覆盖、未授权读取拒绝。

## 7. 阻断条件

Locator语义未区分当前与历史；凭据可能被明文保存；来源访问权限未知；M17读权限与M18处理授权混淆；历史快照无法追溯采集时引用。

## 8. 当前状态

本文件仅形成D-02审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；关联字段继续保持Pending状态。