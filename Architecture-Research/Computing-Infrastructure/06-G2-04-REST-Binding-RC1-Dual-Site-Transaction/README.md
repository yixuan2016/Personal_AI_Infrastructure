# G2-04｜REST Binding RC1 与双站点交易状态机

状态：候选架构设计，待 Owner 评审与双实现验证；纯架构研究，不含工程实现代码。

## 交付
- G2-04.1 REST Binding RC1 候选规范
- G2-04.2 双站点联邦任务交易状态机与 Activation Barrier
- G2-04.3 Saga 故障恢复与补偿协议
- 4 份 CSV：REST Header、交易状态迁移、40 项故障注入验收、回执事件契约
- 6 份 JSON Schema、4 份 JSON 示例
- Mermaid 时序图/状态机源文件、SVG 架构图、7680×5120 PNG
- Word 综合报告、Excel 验收矩阵

## 核心不变量
1. SCO 对全局编排状态负责，Site Owner 对本地资源/执行事实负责。
2. 必需站点未全部 Commit，不得激活 Activation Barrier。
3. TaskClaim 与 ResourceLease 分离；Lease/FencingToken 由本地 Lease Authority 签发。
4. Unknown 不是 Failed；先 Reconcile，再决定重试或补偿。
5. Operation Accepted 不代表业务对象完成。
6. 结果、独立验收、计量、结算由不同权威主体签发。
7. 共享环境中的状态、事件、回执是协作事实；A2A 消息不是唯一事实源。

## 未完成
Owner 签署、REST Binding OpenAPI RC1、统一工具链验证、两套独立实现、双站点故障注入、真实部署验证。
