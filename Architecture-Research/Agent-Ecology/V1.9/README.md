# Agent Ecology V1.9｜跨生态能力发现与目录联邦

**版本：** V1.9.0-Research-Candidate  
**日期：** 2026-11-14  
**性质：** 架构研究与候选契约；不是生产实现或互操作验收结论

## 本版本目标

V1.8 已形成多生态联邦治理与 F0 成员边界候选。V1.9 聚焦 F1：如何发现其他自治生态的 Agent 能力，并在不混淆发现、信任、授权和实时可用性的前提下完成候选协商。

## 核心结论

1. 本地权威能力目录由能力 Owner 所在生态维护。
2. 联邦摘要目录只用于发现候选，可采用最终一致同步。
3. 能力发现、能力证明、运行可用性、任务授权和执行回执必须分离。
4. 目标生态的本地 PDP/PEP 在副作用发生前重新授权。
5. 硬约束过滤先于软排序，软排序不得覆盖 DENY/HOLD。
6. Runtime 通过事件订阅、状态唤醒、游标续读和周期对账保障重新观察。
7. A2A、MCP、CloudEvents、Ontology、SPIFFE 各自承担不同职责，不互相替代。
8. FCP 不拥有成员域生产凭证，不构成全局超级 ADS 或全局信任根。

## 文件目录

- 00_V1.9_跨生态能力发现与目录联邦架构决策备忘录.md
- SOURCES.md
- contracts/capability-advertisement.schema.json
- contracts/capability-resolution.schema.json
- validation/F1_CAPABILITY_DISCOVERY_MATRIX.csv
- assets/00_V1.9_跨生态能力发现与观察Runtime.svg

## 状态边界

| 项目 | 状态 |
|---|---|
| 架构决策备忘录 | Candidate，待评审 |
| 能力广告 Schema | Candidate，待 JSON Schema 2020-12 正式验证 |
| 能力解析 Schema | Candidate，待 JSON Schema 2020-12 正式验证 |
| F1 验收矩阵 | 20 项，全部 NotRun |
| F0 治理 Gate | 12 项，全部 NotRun |
| 双生态互操作 | 未执行 |
| 真实部署 | 未开始 |
| 生产授权 | 未授予 |
| 工程实现 | 不在本版本范围 |

## 与 V1.8 的关系

V1.9 不替代 V1.8。V1.8 的 F0 治理章程、成员身份、Owner、根策略、密钥、撤销和退出机制仍是后续真实跨生态试点的前置条件。F0 未通过前，V1.9 只允许开展文档评审、静态契约审查和合成数据验证设计。
