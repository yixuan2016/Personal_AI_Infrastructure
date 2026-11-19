# 528｜D-03 Snapshot不可变与Correction：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

Snapshot的价值在于固定某一时间点所观察或取得的来源状态。如果允许原位修改采集时间、Locator、Digest、Rights或Policy引用，历史证据就会失去可信性。但不可变也不能被误解为永远不能撤销访问、删除物理副本或纠正错误。

## 2. 关联字段与权威边界

SNP-001至SNP-022共22项子记录字段，重点包括snapshot_id、source_ref、snapshot_sequence、capture_state、captured_at、captured_locator_ref、raw_asset_refs、captured_bytes_digest、rights_snapshot_ref、purpose_ref、policy_decision_ref和snapshot_manifest_digest。

主审议候选：M08负责子记录实例与生命周期，M06负责子记录语义；必须会审M02（字节与物理保管）和M18（处理依据与保留）。

## 3. 必须回答的问题

1. 不可变约束覆盖哪些字段和生命周期阶段？创建封套是否允许采集过程中更新状态？
2. 采集失败、部分完成、重复采集和内容变化分别如何表达？
3. Correction应创建新的Snapshot并通过supersedes/correction关系指向旧记录，还是采用其他追加式机制？
4. 如何区分记录纠错、原始内容变化、权限撤销、保留到期和物理删除？
5. Snapshot与RawAsset字节、Digest、Manifest之间的完整性关系由谁确认？

## 4. 候选方案（不构成推荐或批准）

- A：Snapshot创建后内容封套不可变，纠错通过新Snapshot/更正记录表达；历史最清晰，但需要管理版本链。
- B：允许限定字段在采集完成前更新，完成后冻结；操作弹性较高，但必须定义冻结时点。
- C：对部分元数据允许受控修订并保留完整修订日志；灵活但容易扩大可变边界，必须有字段白名单和复核。

## 5. 必须提供的证据

- Snapshot采集生命周期、失败和重试场景；
- 22个子记录字段的不可变性分类及字段级理由；
- 原位修正与追加更正的审计差异；
- RawAsset、M02 Handle、Digest和Manifest引用关系；
- Rights撤销、Retention到期、删除请求与历史证据保留冲突的处理规则。

## 6. 下游影响与测试

影响Source历史视图、RawAsset、KnowledgeAsset、ExtractionRun、Evidence、审计和删除传播。所有消费者必须读取明确版本，不得默认最新Snapshot代表历史采集状态。

测试覆盖完成后原位修改拒绝、采集未完成状态迁移、重复采集、Correction追加、旧版本引用稳定、撤销与物理删除分离、Manifest Digest一致性。

## 7. 阻断条件

冻结时点不清；无法区分更正和覆盖；快照引用可被重写；删除与证据保留冲突未决；没有M02对原始字节的保管边界。

## 8. 当前状态

本文件仅形成D-03审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；22项子记录字段继续保持Pending状态。