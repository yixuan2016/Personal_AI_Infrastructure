# GitHub 归档续传状态

- **Repository:** `yixuan2016/Personal_AI_Infrastructure`
- **Working branch:** `docs/compute-base-g2-20261110`
- **Dedicated directory:** `Architecture-Research/Computing-Infrastructure/`
- **Related PR:** [#13 — G2-06.5—06.10 区域联邦、十星网络、故障恢复、硬件型号与 OEM 配置研究](https://github.com/yixuan2016/Personal_AI_Infrastructure/pull/13)
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
| G2-06.10 | 双区域十星 OEM 级整机配置、BOM、功率/液冷与采购验收 | RC0 候选，待完整 SKU/报价/现场测量 |

## G2-06.8 归档

- 3 份主要架构/演练/验收文档；1 份 ADR；2 份 Mermaid 图源。
- 故障注入验收矩阵 32 项；恢复证据与 Owner 签署矩阵 12 项。
- FailureEvidenceRecord JSON Schema 1 份；合成 JSON 示例 1 份。
- 11 个 G2-06.8 文件已从远端回读；JSON 语法、CSV 行数和 Mermaid 图源首行检查通过。
- 真实故障注入、双实现互操作和 Owner 签署未完成。

## G2-06.9 归档

- CPU/GPU/SSD/HDD/NIC/交换机候选型号和十星异构节点部署配置 2 份主文档。
- ADR 1 份；Mermaid 图源 1 份；硬件兼容矩阵 21 项；官方证据来源登记 16 项。
- 7 个 G2-06.9 文件已远端回读；型号关键字、CSV 行数和 Mermaid 图源首行检查通过。
- 型号仍需采购 SKU、OEM QVL、BIOS/固件、驱动、供货区域、功率和液冷验证。

## G2-06.10 本轮归档

- 双区域十星 OEM 级整机与配置参考架构：1 份。
- 功率液冷与机房基础设施预算模型：1 份。
- 单星配置卡与部署边界：1 份。
- ADR-G2-06.10-01：1 份。
- 双区域十星 OEM 部署与设施拓扑 Mermaid 图源：1 份。
- 十星设备 BOM 与端口配置清单：1 份 CSV。
- OEM 兼容性与采购验收矩阵：30 项。
- G2-06.10 README：1 份。
- 共新增 8 个 G2-06.10 文件，并更新本索引与归档状态。

### G2-06.10 主参考配置

每区域候选：
- A1/B1：1 套 HPE GB300 NVL72（Dell XE9712 / Lenovo 7DJV 为 OEM 替代）。
- A2/B2：1 套 Lenovo SC755 V5 + N1380，8 trays，2N2S 形成 16 个双路节点；EPYC 9976-S7/9756-S7 按地区供货和 OEM QVL 确认。
- A3/B3：2 台 Dell PowerEdge R7725xd + 40× KIOXIA LC9 E3.L 245.76TB/台。
- A4/B4：3 台 Dell PowerEdge R9815 通用/控制节点。
- A5/B5：2 台 Dell PowerEdge R9815 网络/边缘服务节点 + 2 台 800G Fabric 交换机（Quantum-X800 IB 或 Spectrum-6 Ethernet 二选一）。

### G2-06.10 已核实的关键功率口径

- HPE GB300 NVL72：132kW 名义 TDP、约 155kW EDPp、HPE 建议母线按 192kW 规划；8×33kW Power Shelf 合计 264kW 是输出容量，不是实际功耗。
- HPE QuickSpecs：Vertiv XDU1350 额定冷量 1.3MW，厂商说明最多支持 8 个该类机柜；CDU 冗余与现场水路仍待验证。
- Lenovo N1380：4×15kW PCS；N+1 DC chassis capacity 54kW；8 tray + 4 PCS 在 45°C 示例水流量 42.8L/min。
- Dell R7725xd + 40× KIOXIA LC9：Dell 公开技术简报估算服务器 + SSD 约 1.647kW/台，非现场实测。
- Quantum-X800 Q3400-RA：约 2.9kW 典型（passive cable），主动线缆最大约 7kW。
- Spectrum-6 SN6600：FRO 约 3.94kW、TRO 约 3.2kW 典型功耗。
- 以上指标边界不同，不能混合相加为区域总功率。

### G2-06.10 验证状态

- 8 个新增文件已提交至工作分支；本轮需继续远端回读校验。
- 设备候选、SKU 和公开规格有官方来源；完整采购 BOM、OEM QVL、地区报价、供货承诺、机柜/液冷/电力现场设计仍未完成。
- 72 GPU NVL72 方案与 8 GPU HGX/MI355X 节点方案为替代架构，不得混算。
- LC9 QLC 0.3 DWPD 只作为容量/读密集层候选，高写入事务数据需独立存储层。
- R9815、WAN 边界、OOB 管理交换机、CDU 冗余、UPS/PDU/变压器和辅助设备功耗仍待完整 OEM 配置和设施设计。

## 历史 133 项归档核验

此前准备的历史归档清单包含 133 个文件条目（Markdown、CSV、JSON Schema、示例、清单和 ZIP）。历史记录显示既有批量上传曾到 batch 05/14；目前仍未证明其余批次全部进入 GitHub。

- 尚未对照本地 `SOURCE_FILE_INVENTORY.csv` 完成 133 个路径的全量核验。
- 尚未逐项重算 SHA-256 并与 `SHA256SUMS.txt` 比对。
- 尚未完成所有 ZIP 的完整性测试和关键文档读取检查。
- 不得将本轮增量归档描述为历史 133 项全量归档已完成。

## PR 与分支原则

PR #13 持续跟踪本工作分支并保持 Draft。GitHub 显示可合并不代表应自动合并；工作分支与 main 的差异需在合并前单独审查，尤其是 main 新增提交、受保护路径和历史归档清单。


## G2-06.11 本轮新增归档

- 新增 11 个文件：阶段 README、网络分层设计、端口/光模块/线缆 BOM CSV、供电单线设计、液冷 P&ID 设计、五年 TCO CSV、ADR、38 项网络/电力/液冷联调验收矩阵和 3 份 Mermaid 图源。
- 网络主参考：每区域 Spectrum-6 SN6600 双平面 Ethernet/RoCE；Quantum-X800 Q3400-RA 双平面 InfiniBand 保留为条件性替代。两种路线不混成同一个 GPU Fabric。
- 网络隔离：GPU E-W、CPU North-South、Storage、Customer/WAN、Control/Support、OOB/Facility 分层。
- 电力：HPE GB300 的 8 个 Power Shelf 各由一条 Power Whip 供电；400V/60A 国际配置与 480V/60A 北美配置分开管理。A/B 支路映射须以 OEM 单线图为准。
- 液冷：设施一次侧经 CDU 换热，二次侧连接机柜 Manifold/冷板；XDU1350 内部泵 N+1 不等于 CDU 整机 N+1。
- TCO：仅建立变量和公式口径，等待正式 OEM 报价、PDU 实测、PUE/WUE、电价、水价、维保和折现率。
- 对 G2-06.10 的 HPE 端口描述作了纠偏：HPE QuickSpecs 为每 tray 2 个 ConnectX-8 IO modules、每模块 2 个 OSFP 物理接口，即每 tray 4 个物理 OSFP 接口；不再把它直接写成 4×800Gb/s 有效带宽。速率、模式和 rail map 仍须 OEM 确认。
- 3 个 Mermaid 图源已按单向/双向连线语法复核；供电图明确为每个 Power Shelf 一条 Whip，A/B 分组不提前假设。
- G2-06.11 所有文件仍为 RC0 候选，不代表采购冻结、施工图审查或现场验收完成。
