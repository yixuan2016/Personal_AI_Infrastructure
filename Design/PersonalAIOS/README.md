# Personal AI Life OS 设计研究归档

本目录汇总个人 AI Life OS / 个人数智底座的分阶段架构与治理研究。这里的 Stage/V 版本是研究与审议基线，不代表工程实现、Owner 签认或生产验收。

## 版本导航

| 版本 | 阶段 | 内容 | GitHub 状态 |
|---|---|---|---|
| [V2.21](./V2.21/README.md) | Stage33 | 六类核心 OT 字段级 Profile、关系/生命周期、Command/Query/Event 与迁移规范 | PR #1 已合入 main；六个 OT 仍 Candidate，56 项负向测试 0 执行 |
| [V2.22](./V2.22/README.md) | Stage34 | 六类对象 Owner 审议操作化、Security/Privacy/Legal 审查与 56 项负向测试准备 | PR #2 Open / Draft，堆叠在 V2.21 |
| [V2.23](./V2.23/README.md) | Stage35 | Owner 反馈接收、Atomic Issue、跨 Owner 决策与 142 字段处置台账 | PR #3 Open / Draft，堆叠在 V2.22 |
| [V2.24](./V2.24/README.md) | Stage36 | D01—D07 首批高风险决策审议、权利/目的/同意分离、证据包与批准有效性 | PR #16 Open / Draft，堆叠在 V2.23 |
| [V2.25](./V2.25/README.md) | Stage37 | D08—D12 知识资产版本/删除闭包、Provider/Region、ExtractionRun UnknownOutcome/Retry、ChunkSet 发布、EvidenceTarget/Assertion 核验 | 本次增量 PR #17 Draft，堆叠在 V2.24 |

## 版本边界

- V2.21—V2.24 是连续研究版本；后续 V2.26—V2.27 分支继续推进 Stage38—39，待完成逐版本资产审计与堆叠评审。
- 领域本体/字段 Profile、数据权属、Purpose、Consent、Processing Basis、Physical Handle、Digest/Integrity、Custody 与删除等候选设计，仍须对应 Owner 和 Security/Privacy/Legal 责任方审议。
- 文档、Schema 候选、负向测试设计和静态审计不能替代正式批准、标准验证器执行、运行时测试或生产授权。
- 任何实现或迁移必须遵循独立的产品工程仓库和发布门禁；本研究归档不自动授权代码实施。

## Stage36（V2.24）重点入口

- [Stage36 总体计划](./V2.24/Stage36/524_第三十六阶段总体计划_S1首批高风险决策审议包与Owner证据就绪.md)
- [D01—D07 跨决策依赖与审议顺序](./V2.24/Stage36/533_D01至D07跨决策依赖与审议顺序矩阵.md)
- [字段决策契约消费者测试追踪](./V2.24/Stage36/537_字段决策契约消费者测试追踪矩阵.md)
- [负向测试覆盖深化计划](./V2.24/Stage36/538_D01至D07负向测试覆盖深化计划.md)
- [Security/Privacy/Legal 专业审查工作包](./V2.24/Stage36/539_SecurityPrivacyLegal专业审查工作包.md)
- [Stage36 退出门禁](./V2.24/Stage36/542_第三十六阶段审议就绪度阻断项与退出门禁.md)
- [V2.24 基线 Manifest](./V2.24/Stage36/543_第三十六阶段结论与V2.24首批高风险决策准备基线Manifest.md)
