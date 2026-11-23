# ADR-13：DM04 IFC0.2 profile_extensions 增量提案

- 状态：Proposed（待 DM04 API Owner、双方 Security Owner、AEE/ASCP Profile Owner评审）
- 决策：在 IFC0.2 中为 RequestEnvelope 增加可选 profile_extensions；不改变 IFC0.1 既有必需字段。
- 结构：以 Profile URI 为键，携带 profile_version、schema_ref、criticality、payload_digest、data。
- 语义：data 仅携带 AEE/ASCP 引用，不携带 Grant/Bearer Token/Lease/数据正文。
- 安全：未知 required URI 拒绝；未知 optional URI 忽略并审计；Schema/Digest 失败拒绝；引用解析时目标站点本地 PDP/PEP 再授权。
- 兼容：双方未协商 IFC0.2 前不得发送该字段；若扩展是安全执行前提，则暂停操作。
- 幂等：高风险请求摘要覆盖扩展块；同幂等键但扩展内容变化按既有冲突语义处理。
- 验收：IFC0.1 客户端无字段仍兼容；IFC0.2 双实现能验证摘要、版本、required/optional行为；未知关键扩展零副作用。
