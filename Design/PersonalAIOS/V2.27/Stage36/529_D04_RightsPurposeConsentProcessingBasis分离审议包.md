# 529｜D-04 Rights/Purpose/Consent/Processing Basis分离：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

来源权利、处理目的、个人同意、其他处理依据和Policy决策是不同概念。若将其压缩为一个authorized布尔值，会掩盖第三方权利、目的限制、法律依据、同意撤回和策略执行之间的差异。某个Source可读取，不代表允许存储、提取、索引、发给Provider或用于RSI。

## 2. 关联字段与权威边界

- SRC-008 source_rights_refs
- SNP-013 rights_snapshot_ref
- SNP-014 purpose_ref
- SNP-015 policy_decision_ref
- SNP-016 applicable_basis_refs
- 必要时联动SNP-017 data_subject_refs、SNP-018 classification_ref和SNP-019 retention_profile_ref

主决定权威候选：M18（Policy Authority）；必须会审M06、Privacy/Legal。个人数据的授权、同意和最终主权确认由Personal Owner本人作出，不能由模块Owner或AI代替。

## 3. 必须回答的问题

1. source_rights_refs记录来源权利声明、许可条款还是权利主体引用？如何保存版本和适用范围？
2. purpose_ref是否绑定具体处理活动，而不是泛化为“个人助理用途”？
3. Consent是否由个人本人或合法授权主体明确授予，并支持范围、期限和撤回？
4. applicable_basis_refs如何表示Consent以外的处理依据，如何处理依据冲突？
5. policy_decision_ref是否记录某次具体决策的输入、策略版本、结果和理由？
6. Purpose变化、Consent撤回、Rights变化和Retention到期如何触发派生资产、Provider副本及缓存的限制或删除？

## 4. 候选方案（不构成推荐或批准）

- A：Rights、Purpose、Consent、Processing Basis、Policy Decision分别建模并通过引用关联；语义清晰、可审计，但需要跨对象治理。
- B：保留独立概念，但通过统一授权评估封套聚合展示；改善使用体验，但底层决策来源必须可拆分。
- C：采用轻量授权记录并在Policy中展开；只有完整保留来源、范围、期限、撤回和依据语义时才可考虑。

## 5. 必须提供的证据

- 来源许可原文、权利主体、适用地区、期限和再利用条款；
- 个人数据类别、Data Subject、目的清单和个人授权记录；
- 适用法律/政策意见及其版本、范围和专业责任人；
- Policy Decision输入输出、策略版本、拒绝原因和审计样例；
- 撤回、目的变更、删除、Provider外发和派生数据传播场景。

## 6. 下游影响与测试

影响所有接入、存储、提取、索引、上下文组装、外部模型调用、RSI评估、导出和删除流程。授权必须按具体动作、目的、数据范围、主体和期限判断。

测试覆盖无Consent、Consent过期、Consent撤回、Purpose不匹配、Rights限制再利用、Processing Basis缺失、Policy拒绝、Provider超范围和派生物权限继承。

## 7. 阻断条件

无法证明适用处理依据；把读取权限等同于处理授权；把AI推断等同于个人同意；Rights与Consent混淆；撤回后派生数据和Provider副本没有处理路径。

## 8. 当前状态

本文件仅形成D-04审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；关联字段继续保持Pending状态。