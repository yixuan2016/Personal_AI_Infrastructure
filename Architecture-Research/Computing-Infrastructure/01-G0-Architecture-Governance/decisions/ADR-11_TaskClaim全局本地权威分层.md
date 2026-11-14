# ADR-11：TaskClaim 全局/本地权威分层

- 状态：Proposed（待 SCO Owner、Site A/B Task Owner、Compute Owner 评审）
- 关联：AEE/ASCP V1.1-RC0；DM04 IFC0.1
- 决策：SCO 负责全局 TaskContract、ContractGraph、Plan、Saga 与 ActivationBarrier 汇总；站点 Local Task Coordinator 签发本地 TaskClaim；资源所在地 Lease Authority 独立签发 LocalResourceLease/FencingToken。
- 作用域：TaskClaim 唯一性限定 `(site_id, site_task_ref, stage_ref)`；claim_epoch 仅任务认领域有效。
- 禁止：SCO 代签本地 TaskClaim；TaskClaim/claim_epoch 替代资源 Lease/FencingToken；ActivationBarrier 被解释为本地执行许可。
- 理由：避免全局协调服务与站点执行权威双重写入，保持分区自治与资源安全。
- 迁移：V1.0 TaskClaimLease 兼容读取；新对象使用 TaskClaim；旧 fencing_token 字段不得映射为资源 token。
- 验收：并发认领仅一个成功；旧 claim_epoch 写入被拒绝；Site A claim 不可用于 Site B；资源 Lease 仍由本地 Lease Authority 签发。
- 签署：SCO Owner、Site A Task Owner、Site B Task Owner、Compute Resource Owner。
