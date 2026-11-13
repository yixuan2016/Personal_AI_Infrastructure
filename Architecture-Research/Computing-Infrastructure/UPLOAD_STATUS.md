# GitHub 归档续传状态

- **Repository:** `yixuan2016/Personal_AI_Infrastructure`
- **Working branch:** `docs/compute-base-g2-20261110`
- **Dedicated directory:** `Architecture-Research/Computing-Infrastructure/`
- **Related PR:** [#13 — G2-06.5—06.9 区域联邦、十星网络、故障恢复与硬件型号研究](https://github.com/yixuan2016/Personal_AI_Infrastructure/pull/13)
- **Merge policy:** 仅向工作分支增量提交；本轮未合并 main，未修改工程代码。

## 已归档阶段

| 阶段 | 内容 | 状态 |
|---|---|---|
| G0/G1/G2-03 | 六域权威、Ontology/协议一致性、ADS/SCO API 映射 | 历史候选资料，按原状态保留 |
| G2-04 | REST Binding、双站点交易状态机、Activation Barrier、Saga | RC1 候选，待 Owner 评审与互操作 |
| G2-05/06 | RCP 区域协调层、跨区域协议、事件一致性与恢复 | RC0 候选，待 Owner 评审 |
| G2-06.7 | 十星控制面容量与跨区域网络模型 | RC0 候选，待现场测量 |
| G2-06.8 | 双区域十星故障注入、自治恢复与独立验收 | RC0 候选，待批准和实测 |
| G2-06.9 | 十星 CPU/GPU/存储/网络设备型号与异构节点配置 | RC0 候选，待 OEM/QVL/设施核验 |

## G2-06.8 本轮归档

- 故障遏制与自治恢复架构、故障注入与恢复演练手册、独立见证与十星验收门禁：3 份主要设计文档。
- ADR：1 份；Mermaid 图源：2 份。
- 故障注入验收矩阵：32 项；恢复证据与 Owner 签署矩阵：12 项。
- FailureEvidenceRecord JSON Schema：1 份；合成 JSON 示例：1 份。
- 11 个 G2-06.8 文件已从远端回读；Schema 与示例通过 JSON 语法解析；CSV 行数和 Mermaid 图源首行检查通过。
- 这些检查不等于完整 Schema 工具链验证、图表渲染、双实现互操作或真实故障注入。

## G2-06.9 本轮归档

- 十星 CPU/GPU/存储/网络设备型号参考选型：1 份。
- 十星异构节点与区域部署配置：1 份。
- ADR：1 份；硬件拓扑 Mermaid 图源：1 份。
- 硬件型号与兼容性核验矩阵：21 项；设备候选与证据来源登记：16 项。
- 共新增 7 个 G2-06.9 文件，并更新本索引与归档状态。
- 7 个文件已从远端回读；两份 CSV 行数、图源首行和型号关键字已检查。
- 型号信息来自厂商官方产品页/数据表；仍需采购 SKU、OEM QVL、BIOS/固件、驱动、供货区域、功率和液冷验证。

## G2-06.9 已核实的候选型号

- CPU：AMD EPYC 9956/9996/9966/9756；Intel Xeon 6980P。
- GPU：NVIDIA GB300 NVL72、HGX B300；AMD Instinct MI355X OAM、MI350P PCIe；NVIDIA Vera Rubin NVL72 作为前瞻观察项。
- SSD/HDD：Micron 9650/9550、Solidigm D7-PS1010、KIOXIA CM7-V、Seagate Mozaic 4+ 44TB。
- 网络：NVIDIA Quantum-X800 Q3400-RA/Q3401-RD、Spectrum-6 SN6600/SN6800、ConnectX-8；Broadcom Tomahawk 6 仅作为交换 ASIC 候选，未认定为交换机整机 SKU。

## 验证边界

1. 尚未执行完整 JSON Schema Draft 2020-12 工具链验证和 Mermaid 渲染构建。
2. 尚未执行两套独立实现互操作、真实网络故障注入或现场十星验收。
3. 尚未获得站点、区域、资源、数据、网络、设施、安全与 OEM Owner 的正式签署。
4. 所有 RTO/RPO、撤销最大陈旧窗口、功率、液冷、吞吐和网络 SLO 仍需现场测量。
5. 设备型号明确不等于采购完成、OEM 兼容认证或部署完成；当前不冻结十星采购 BOM。

## 历史 133 项归档核验

此前准备的历史归档清单包含 133 个文件条目（Markdown、CSV、JSON Schema、示例、清单和 ZIP）。历史记录显示既有批量上传曾到 batch 05/14；目前仍未证明其余批次全部进入 GitHub。

- 尚未对照本地 `SOURCE_FILE_INVENTORY.csv` 完成 133 个路径的全量核验。
- 尚未逐项重算 SHA-256 并与 `SHA256SUMS.txt` 比对。
- 尚未完成所有 ZIP 的完整性测试和关键文档读取检查。
- 不得将本轮增量归档描述为历史 133 项全量归档已完成。

## PR 与分支原则

PR #13 持续跟踪本工作分支并保持 Draft。GitHub 显示可合并不代表应自动合并；工作分支与 main 的差异需在合并前单独审查，尤其是 main 新增提交、受保护路径和历史归档清单。
