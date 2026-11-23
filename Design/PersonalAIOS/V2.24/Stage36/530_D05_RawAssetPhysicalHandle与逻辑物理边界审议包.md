# 530｜D-05 RawAsset Physical Handle与逻辑/物理边界：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

RawAsset是逻辑资产对象，物理字节可能位于本地文件系统、加密卷、对象存储或其他受控介质。若把绝对路径、Bucket URL或存储供应商地址直接写成权威Handle，会暴露部署细节并将逻辑资产耦合到物理位置。

## 2. 关联字段与权威边界

- RAW-004 physical_handle_ref
- 联动RAW-001 raw_asset_id、RAW-005 byte_size、RAW-008 byte_digest、RAW-012 custody_state和RAW-020 custody_receipt_refs。
- 主决定权威候选：M02 Physical Custodian；必须会审M08（逻辑资产身份）、M06（类型语义）和Security。M08不得代替M02签发或管理物理Handle。

## 3. 必须回答的问题

1. physical_handle_ref是否始终为不透明引用，而不暴露宿主路径、密钥或可直接访问的URL？
2. Handle由谁签发、解析、授权、轮换和撤销？
3. 一个RawAsset是否允许多个物理副本、备份副本或迁移副本？如何区分主副本与备份？
4. Handle失效、介质迁移、加密密钥轮换和灾难恢复时，逻辑raw_asset_id是否保持稳定？
5. 物理删除完成由谁提供回执，M08如何对账而不自行宣告删除？

## 4. 候选方案（不构成推荐或批准）

- A：M02独立管理Handle Registry，M08仅保存Opaque Handle引用；隔离清晰，但需要稳定的跨模块解析契约。
- B：M02提供受控Storage Gateway并返回能力受限的短期引用；访问控制更细，但需要定义续期、审计和失败语义。
- C：Handle由M08保存的逻辑存储标识映射到M02内部位置；可以降低调用复杂度，但必须保证M02仍是物理位置和操作的唯一权威。

## 5. 必须提供的证据

- M02物理存储、Handle Registry和权限接口的权威说明；
- 本地、加密卷、对象存储、备份和迁移的Handle样例；
- Handle不可猜测、不可越权访问、可撤销和可轮换的安全证据；
- RawAsset与多副本、备份和物理位置的关系样例；
- 删除、恢复、密钥轮换和Custody Receipt的端到端责任链。

## 6. 下游影响与测试

影响RawAsset读取、ExtractionRun输入、KnowledgeAsset导入、备份恢复、导出、删除和审计。消费者不得绕过M02直接拼接物理路径或访问底层存储。

测试覆盖无效Handle、过期Handle、跨用户访问、路径泄漏、未经授权读取、迁移后逻辑ID稳定、备份副本标记和删除回执缺失。

## 7. 阻断条件

Handle可直接绕过Policy；M02未确认签发权；逻辑与物理删除被混为一谈；没有回执；多副本关系无法完整枚举。

## 8. 当前状态

本文件仅形成D-05审议准备包。尚未记录真实Owner反馈、正式Decision Record或批准证据；RAW-004继续保持Pending状态。