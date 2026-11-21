# 531｜D-06 Digest与Integrity语义：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

多个Digest字段可能针对不同内容范围：原始字节、采集字节、证据目标内容或Locator片段。若不声明算法、规范化方式、范围、计算时点和比较对象，Digest相等或不等都可能被错误解释。Digest匹配不等于来源可信，更不等于断言真实。

## 2. 关联字段与权威边界

- RAW-008 byte_digest；RAW-009 digest_algorithm；RAW-010 digest_scope；RAW-011 integrity_state；
- SNP-011 captured_bytes_digest；SNP-012 digest_scope；
- EVD-007 target_content_digest；EVD-008 locator_fragment_digest。

主审议候选：M06负责Digest/Integrity语义；必须会审M02（实际字节和存储完整性）、M08（字段与证据实例记录）及Security。

## 3. 必须回答的问题

1. byte_digest与captured_bytes_digest的对象范围和计算时点是否不同？
2. target_content_digest与locator_fragment_digest分别针对完整目标内容还是定位片段？
3. digest_scope是否表达字节范围、编码、规范化、压缩/解压和分段规则？
4. 算法升级、算法淘汰、摘要重算和历史兼容如何处理？
5. integrity_state仅表示完整性校验结果，还是错误地混入来源真实性或Assertion Verification？

## 4. 候选方案（不构成推荐或批准）

- A：所有Digest都绑定算法、范围、版本和被摘要对象引用；解释力强，但需要严格字段契约。
- B：定义统一Digest Envelope并由不同对象引用；减少重复，但必须避免把不同目标和范围压成同一摘要语义。
- C：按对象分别保留Digest字段并制定统一语义词汇；迁移成本较低，但需要跨对象一致性审查。

## 5. 必须提供的证据

- 每种Digest的输入字节、范围、算法、编码和计算时点说明；
- 同一内容不同格式、压缩、换行和片段定位的测试向量；
- M02完整性校验回执和错误处理记录；
- Evidence Target、Locator Fragment与原始内容的对应样例；
- 算法迁移、历史摘要验证和重新计算策略。

## 6. 下游影响与测试

影响Snapshot、RawAsset、Evidence、ExtractionRun、备份校验和审计。消费者必须读取Digest Scope和Algorithm，禁止只比较摘要字符串。

测试覆盖算法不匹配、范围不匹配、片段边界变化、内容格式化变化、摘要损坏、历史算法淘汰、完整性失败和将Digest误判为真实性的负向场景。

## 7. 阻断条件

Digest没有明确目标对象或范围；不同Digest字段被混用；算法版本不可追溯；完整性与真实性/核验状态混淆；M02无法提供实际字节校验依据。

## 8. 当前状态

本文件仅形成D-06审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；关联字段继续保持Pending状态。