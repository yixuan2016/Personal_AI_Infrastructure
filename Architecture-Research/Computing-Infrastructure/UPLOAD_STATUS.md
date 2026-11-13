# GitHub 归档续传状态

- **Repository:** `yixuan2016/Personal_AI_Infrastructure`
- **Working branch:** `docs/compute-base-g2-20261110`
- **Dedicated directory:** `Architecture-Research/Computing-Infrastructure/`
- **Related PR:** [#13 — G2-06.5—06.8 区域联邦、十星容量网络与故障恢复研究](https://github.com/yixuan2016/Personal_AI_Infrastructure/pull/13)
- **Merge policy:** 本阶段只向工作分支增量提交；未合并 main，未修改工程代码。

## 已归档阶段

| 阶段 | 内容 | 状态 |
|---|---|---|
| G0/G1/G2-03 | 六域权威、Ontology/协议一致性、ADS/SCO API 映射 | 历史候选资料，按原状态保留 |
| G2-04 | REST Binding、双站点交易状态机、Activation Barrier、Saga | RC1 候选，待 Owner 评审与互操作 |
| G2-05/06 | RCP 区域协调层、跨区域协议、事件一致性与恢复 | RC0 候选，待 Owner 评审 |
| G2-06.7 | 十星控制面容量与跨区域网络模型 | RC0 候选，待现场测量 |
| G2-06.8 | 双区域十星故障注入、自治恢复与独立验收 | RC0 候选，待批准和实测 |

## G2-06.8 本轮新增

- 故障遏制与自治恢复架构、故障注入与恢复演练手册、独立见证与十星验收门禁：3 份主要设计文档。
- ADR：1 份。
- Mermaid 图源：2 份。
- 故障注入验收矩阵：32 项。
- 恢复证据与 Owner 签署矩阵：12 项。
- FailureEvidenceRecord JSON Schema：1 份。
- 合成 JSON 示例：1 份。
- 本轮共新增 11 个 G2-06.8 文件，并更新本索引与归档状态。

## 本轮远端回读检查

- 11 个 G2-06.8 文件均可从工作分支回读。
- 1 份 Schema 与 1 份合成示例通过 JSON 语法解析。
- 两份 CSV 分别回读 32 项和 12 项数据行。
- 两份 Mermaid 图源已检查首行图类型。
- Markdown 文档均可回读。
- 上述检查不等于完整 JSON Schema 规范校验、Mermaid 渲染、双实现互操作或真实故障注入。

## 尚未完成的验证

1. JSON Schema 需进入统一工具链做 Draft 2020-12 完整验证。
2. Mermaid 图需在仓库文档渲染链路实际构建检查。
3. G2-06.8 需在批准的隔离环境执行单故障与组合故障演练。
4. 需要站点、区域、资源、数据、网络、设施和安全 Owner 签署。
5. 需要第二套独立实现和独立见证报告。
6. RTO/RPO、撤销最大陈旧窗口、容量和网络 SLO 需要真实环境测量。

## 历史 133 项归档核验

此前准备的历史归档清单包含 133 个文件条目（Markdown、CSV、JSON Schema、示例、清单和 ZIP）。历史记录显示既有批量上传曾到 batch 05/14；目前仍未证明其余批次全部进入 GitHub。

因此必须继续保留以下未完成状态：

- 尚未对照本地 `SOURCE_FILE_INVENTORY.csv` 完成 133 个路径的全量核验。
- 尚未逐项重算 SHA-256 并与 `SHA256SUMS.txt` 比对。
- 尚未完成所有 ZIP 的完整性测试和关键文档读取检查。
- 不得将本轮增量归档描述为历史 133 项全量归档已完成。

## 当前 PR 与分支原则

PR #13 持续跟踪本工作分支。PR 维持 Draft，供后续审阅；不因文件已推送或 GitHub 显示 mergeable 就自动合并 main。若 main 有新提交，先检查差异和冲突，再决定是否同步。
