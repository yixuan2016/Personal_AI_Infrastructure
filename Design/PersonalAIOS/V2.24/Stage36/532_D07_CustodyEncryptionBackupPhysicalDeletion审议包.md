# 532｜D-07 Custody/Encryption/Backup/Physical Deletion：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

逻辑资产存在不等于物理资产仍可访问；标记为Deleted也不代表备份、缓存、Provider副本和密钥材料已完成处置。Custody、Encryption、Backup、Retention、Legal Hold和Physical Deletion必须形成可核验责任链。

## 2. 关联字段与权威边界

- RAW-012 custody_state
- RAW-013 encryption_profile_ref
- RAW-020 custody_receipt_refs
- 联动RAW-004 physical_handle_ref、RAW-015 retention_profile_ref及RAW-019 deletion_state_ref。

主决定权威候选：M02 Physical Custodian；必须会审M18（Retention/Policy）、Security；涉及个人数据或不可恢复删除时引入Privacy/Legal和Personal Owner。

## 3. 必须回答的问题

1. custody_state表达的是M02对物理副本的保管状态，还是混合了逻辑资产生命周期？
2. encryption_profile_ref指向算法策略、密钥配置还是实际密钥？必须禁止把密钥材料本身暴露在Profile中。
3. 备份副本、灾备副本、临时副本和Provider副本如何枚举并关联？
4. 删除请求如何区分逻辑撤销、在线副本删除、备份到期、密钥销毁和外部Provider删除？
5. custody_receipt_refs由谁签发，回执应证明哪些范围、时间和执行结果？

## 4. 候选方案（不构成推荐或批准）

- A：M02对物理Custody、Encryption、Backup和Physical Deletion形成独立权威闭环，M08只维护逻辑状态与回执引用；边界清楚但协作契约较多。
- B：以统一Deletion/Custody Orchestration协调M02、M07、M18和Provider，但各模块仍保留自身权威；便于端到端管理，需防止协调器越权。
- C：按存储介质和副本类型分阶段完成删除并分别回执；可审计性强，但必须明确最终关闭条件和超期风险接受权。

## 5. 必须提供的证据

- M02 Custody、加密、密钥轮换、备份和恢复能力说明；
- 物理副本、备份副本、缓存、派生索引和Provider副本清单；
- Retention、Legal Hold、Consent撤回和删除请求的策略依据；
- 删除回执字段、签发身份、作用范围、时间戳和失败语义；
- 密钥销毁、备份自然过期和不可恢复删除的专业审查意见。

## 6. 下游影响与测试

影响所有原始资产读取、复制、导出、备份、恢复、派生、缓存和删除流程。M08只能记录请求和回执，不能代替M02证明物理操作已完成；M18决定策略边界，不代替M02执行。

测试覆盖Custody未知、加密配置缺失、密钥轮换失败、备份副本遗漏、删除回执缺失、Legal Hold阻断、Provider副本未清理和部分删除后的状态表达。

## 7. 阻断条件

物理副本清单不完整；密钥责任不明；回执不能证明删除范围；Retention与Legal Hold冲突未决；把逻辑Tombstone误认为物理删除完成。

## 8. 当前状态

本文件仅形成D-07审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；关联字段继续保持Pending状态。