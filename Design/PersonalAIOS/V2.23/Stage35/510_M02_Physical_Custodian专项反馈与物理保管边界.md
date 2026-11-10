# 510｜M02 Physical Custodian专项反馈与物理保管边界

**状态：** Physical Custody Review Candidate；M02 Owner Feedback Pending

## 1. 审议目标

确认M02对RawAsset物理字节、Opaque Handle、密钥/加密能力、宿主访问、备份副本、物理删除和Custody Receipt的真实责任边界。M08只维护逻辑资产身份和血缘，不得把路径、URL或对象存储Key当作物理保管授权。

## 2. 核心审议议题

| 议题 | 必须明确 | 不能接受的模糊表达 |
|---|---|---|
| Handle签发 | 谁签发、作用域、绑定资产、权限、过期和撤销 | “有一个storage path即可” |
| Handle读取 | 谁可读取、何时PEP检查、是否支持一次性能力 | “M08可以直接访问文件” |
| 字节完整性 | Digest算法、字节范围、容器/压缩语义和重算方式 | “Hash相同就证明内容可信” |
| Custody State | 物理存在、隔离、损坏、归档、待删除等状态 | 与逻辑Lifecycle混成一个枚举 |
| Encryption | Profile、密钥权威、轮换、撤销和恢复 | M08保存密钥材料 |
| Backup | 副本范围、加密、恢复、删除传播和保留例外 | “主库删掉即全部删除” |
| Physical Deletion | 删除命令、异步状态、回执、备份和Provider副本 | “API返回成功即销毁完成” |
| Receipt | 回执原件、签名、对象范围和证据留存 | M08复制回执成为第二权威 |

## 3. 与142字段的关联

重点核对RAW-004 `physical_handle_ref`、RAW-008—010 Digest字段、RAW-011 `integrity_state`、RAW-012 `custody_state`、RAW-013 `encryption_profile_ref`、RAW-015 `retention_profile_ref`、RAW-019 `deletion_state_ref`、RAW-020 `custody_receipt_refs`，以及SNP-010/011/012、KAS-016、CHK-020/022和EVD-021的跨对象影响。

## 4. M02决策边界

M02决定物理能力、访问句柄、字节保管、密钥、备份、物理删除和物理回执；M02不决定KnowledgeAsset语义、Evidence—Assertion关系、个人Purpose或M18 Policy。M02的物理回执可被其他对象引用，但原件权威必须保持在M02。

## 5. 关键负向场景

- 无有效Handle却将RawAsset标记Available；
- Handle过期后M08绕过M02访问；
- 主存删除后备份副本仍可恢复；
- 删除请求没有覆盖缓存、快照和归档副本；
- Digest算法或范围不明却标记Integrity Intact；
- M08自行写入CustodyReceipt或密钥状态；
- 物理删除回执没有覆盖对象版本或副本范围。

## 6. 所需证据

M02能力契约、Handle生命周期、访问授权、加密与密钥治理、备份清单、删除流程、回执Schema、异常恢复和合成示例。任何“不可恢复删除”承诺必须有对应技术和审计证据。

## 7. 当前结论

M02专项审议尚未取得真实Owner意见或批准证据。相关字段继续Candidate；不得宣称物理删除能力、备份删除或密钥边界已经冻结。