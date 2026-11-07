# 510｜M02 Physical Custodian专项反馈与物理保管边界

**父基线：** V2.22-Draft / 00—503  
**目标基线：** V2.23-Draft / 00—523  
**状态：** Candidate / Pending；不推断Owner批准，不授权工程实现

## 1. 目的
确认M02对RawAsset物理字节、Opaque Handle、密钥/加密、宿主访问、备份、物理删除和Custody Receipt的责任。

## 2. 审议范围
- Handle签发、绑定、权限、过期、撤销和读取授权。
- Digest算法、字节范围、容器语义和重算方式。
- Custody State与逻辑Lifecycle正交。
- Encryption Profile、密钥轮换、备份副本、物理删除、回执和异常恢复。

## 3. 权威边界与控制要求
- M08只维护逻辑资产身份和血缘，不把路径/URL当作物理授权。
- M02不决定KnowledgeAsset语义、Evidence—Assertion关系或个人Purpose。
- 主存删除不等于备份/Provider副本已删除。

## 4. 所需证据与验收
- M02能力契约、Handle生命周期、访问授权、密钥治理、备份清单、删除流程、回执Schema。
- 缺少物理回执或副本范围证据时，不得声称物理销毁完成。

**统一状态声明：** 本文件为审议准备材料；未取得真实Owner原始反馈和有效批准证据前，相关事项保持Pending/Proposed，不得升级为Approved或Freeze。
