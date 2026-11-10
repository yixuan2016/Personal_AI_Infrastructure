# Agent Ecology V1.8｜跨生态联邦进化与多生态协同治理

**版本：** V1.8-Architecture-Draft  
**日期：** 2026-11-10  
**性质：** 架构研究与候选契约，不是生产实现或互操作验收结论

## 本版本核心命题
从“单个生态内部自治”扩展为“多个自治生态之间协同进化”。不是把多个 ADS 合并成一个超级 ADS，而是建立联邦协作协议和本地主权执行：每个生态保留自己的身份体系、Ontology、数据权属、业务规则、风险策略和生产执行权；联邦层仅支持发现、协商、交换经授权的能力声明与证据，并传播可供本地独立评估的改进候选。

## 设计结论
1. 每个 Ecology Domain 拥有本地 ADS、Environment Runtime、Ontology、策略权威、数据/资源 Owner 和 PEP/PDP。
2. Federation Coordination Plane（FCP）只提供成员/能力发现、契约协商、证据索引、事件路由和兼容性评估；不持有成员域生产凭证。
3. 共同环境中的状态、任务工件和可验证事件是协作主线；A2A 是交互/传输机制，不是信任根。
4. 跨域策略使用 ALLOW / DENY / ABSTAIN；硬约束 DENY 优先，关键 ABSTAIN 进入 HOLD。
5. 改进提案可跨域传播，但每个接收生态独立验证、Shadow、审批、Canary、采用或拒绝。
6. 信任采用多维、上下文相关、带时效的向量，不使用可被单一高分抵消的信誉总分。
7. 默认只交换最小化元数据、签名证据摘要和经授权的模式；不默认交换原始轨迹、私有记忆或模型梯度。
8. 人类治理外环保留根策略、根身份、权限上限和生产授权权。

## 文件
- `00_总体架构与决策.md`
- `01_联邦拓扑与职责边界.md`
- `02_信任契约与改进生命周期.md`
- `03_策略兼容与知识交换.md`
- `04_安全威胁与实施验收.md`
- `05_API事件与错误码.md`
- `contracts/federation-contracts.schema.json`
- `validation/validation-matrix.csv`
- `validation/threat-matrix.csv`
- `assets/00_跨生态联邦总体架构.svg`
- `assets/01_改进提案生命周期.svg`
- `SOURCES.md`
- `STATUS.md`

## 状态
架构候选已形成；Schema/接口待评审；15 项验证和 12 项威胁测试均为 NotRun；未进行真实双生态部署、生产授权或现场互操作验证。
