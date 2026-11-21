# G2-06.11｜双区域十星网络互连、供电单线、液冷 P&ID 与五年 TCO RC0

- 项目：算力底座 / 星链式可信算力基础设施
- 核查日期：2026-11-14
- 状态：RC0 架构参考，待 OEM、网络、设施、存储、采购与安全 Owner 评审
- 范围：双区域十星；每区域一套 GB300 NVL72 主参考 GPU rack，另含 CPU/HPC、容量存储、控制和边缘节点
- 性质：纯架构研究、公开资料核对与参数化预算；不是施工图、设备配置单、采购订单或现场验收结论

## 本阶段文件

1. G2-06.11_双区域网络分层与拓扑设计.md
2. G2-06.11_端口映射光模块与线缆BOM.csv
3. G2-06.11_双路供电单线与支路容量设计.md
4. G2-06.11_液冷P&ID与监测联锁设计.md
5. G2-06.11_五年TCO参数化预算模型.csv
6. decisions/ADR-G2-06.11-01_GPU双平面Fabric与隔离策略.md
7. matrices/G2-06.11_网络电力液冷联调验收矩阵.csv
8. diagrams/G2-06.11_双区域网络拓扑.mmd
9. diagrams/G2-06.11_供电单线图.mmd
10. diagrams/G2-06.11_液冷P&ID图.mmd

## 核心结论

- GPU 训练网络采用 Plane-A / Plane-B 两个独立 Fabric；NCCL/通信运行时负责多平面负载均衡与故障隔离，不用普通 LAG 代替 GPU rail-aware 设计。
- 主参考优先评估 NVIDIA Spectrum-6 SN6600 Ethernet/RoCE 双平面；若训练/HPC 团队已有成熟 InfiniBand 运维能力且业务要求明确，则以 Quantum-X800 Q3400-RA 双平面作为替代。两条路线不混成一个 Fabric。
- HPE GB300 NVL72 QuickSpecs 显示每个 compute tray 有 2 个 ConnectX-8 IO modules，每个 IO board 具有 2 个 OSFP 物理接口；18 个 tray 对应 72 个 OSFP 物理接口。按两平面均分可形成每平面 36 个 rack-side 物理接口的初始布线假设；实际 port mode、每口速率、breakout 和 rail map 必须由 HPE/NVIDIA 书面端口表确认。物理接口数量不等于 72×800Gb/s 的已验证有效吞吐。
- CPU/North-South、Storage、Customer/WAN、OOB/设施管理分层；GPU East-West Fabric 不承载通用存储流量。
- GB300 电力采用 8 个 Power Shelf 分别接入 8 条 OEM 指定 power whip；400V/60A 国际版与 480V/60A 北美版是不同供电配置，不能按地区互换。上游 A/B 馈电映射由 OEM 单线图和电气工程师确认。
- 液冷采用设施一次侧—CDU 换热—设备二次侧—Manifold—冷板回路；HPE NVL72 与 Lenovo N1380 的设备二次侧回路分别设计，不默认共用同一二次液体。
- XDU1350 的三泵/N+1 泵模式不等于整台 CDU N+1；CDU 整机冗余需独立决策。
- TCO 不填虚构报价，使用可替换的 OEM 报价、平均 IT 负载、PUE、WUE、电价、维保和折现率输入。

## 与 G2-06.10 的重要修订

G2-06.10 的 HPE NVL72 端口说明曾将“每 tray 4×800G OSFP”作为推导性写法。G2-06.11 将其更正为：每 tray 2 个 ConnectX-8 IO modules、每模块 2 个 OSFP 物理接口，即每 tray 4 个物理 OSFP 接口；具体每口速率、port mode、breakout 与布线 rail 仍须 OEM 确认。不得将物理接口数量直接等同于 4×800Gb/s 有效带宽。

## TCO 计算口径

- IT 年能耗 = 参考满载 IT 功率（kW）× 8760 × 年等效利用率；如果直接使用全年实测平均功率，则不得再乘利用率。
- 设施年能耗 = IT 年能耗 × PUE。PUE 法与 UPS/冷机/CDU 等设施设备逐项功耗法二选一，禁止重复计入。
- 年水耗 = IT 年能耗 × WUE（L/kWh）；若直接用水表实测，则不再重复套用 WUE。
- 五年 TCO = 初始 CAPEX + 五年许可/维保/线路/场地/备件/电力/水耗的折现现值；折现率、价格增长率和残值按财务输入。
- 所有设备价格均留待 OEM/集成商正式报价，不用网上零售价格替代企业级交付报价。

## 冻结门禁

1. HPE/Dell/Lenovo 完整订货配置与端口连接表。
2. GPU NIC、交换机、OSFP 光模块、DAC/AOC、光纤、FEC、距离和固件互操作 QVL。
3. GPU Fabric 双平面故障切换、NCCL 通信效率与无 LAG 误用测试。
4. CPU/Storage/Customer/OOB 网络端口、路由、安全域与容量验证。
5. 电气工程师签署的电源单线图、保护整定、短路电流、接地和 UPS 运行方式。
6. CDU 一次/二次水路、热负载曲线、流量/压降、水质、泵冗余、漏液联锁和维护旁路验证。
7. OEM 报价、能源/水耗、维保、备件和五年 TCO。
8. 单星、区域、双区域端到端测试和独立见证。

## 官方资料

- NVIDIA NVL72 AI Factory：网络物理拓扑与多平面设计：https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/networking-physical-topologies.html
- NVIDIA NVL72 AI Factory：逻辑网络与 Fabric 角色：https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/network-logical-architecture.html
- HPE GB300 NVL72 QuickSpecs：https://www.hpe.com/us/en/collaterals/collateral.a50009244enw.html
- NVIDIA Quantum-X800 Q34xx 用户手册：https://networking-docs.nvidia.com/xdrswitcheshw/introduction
- NVIDIA Spectrum-6 SN6600 用户手册：https://networking-docs.nvidia.com/sn6000hw/specifications
- NVIDIA RoCE 技术指南：https://docs.nvidia.com/networking-ethernet-software/guides/esf-generic-config-guide/
- Vertiv XDU1350 Application and Planning Guide：https://www.vertiv.com/4908a3/globalassets/products/thermal-management/high-density-solutions/liebert-xdu-coolant-distribution-units/vertiv-liebert-xdu1350-coolant-distribution-unit-application-and-planning-guide-xdu1350b-sl-71309.pdf
- Vertiv XDU1350 Installation and Commissioning Guide：https://www.vertiv.com/4a15c9/globalassets/shared/liebert-xdu1350-coolant-distribution-unit-installation-and-commissioning-guide-sl-70625.pdf
- Lenovo N1380 Neptune Datasheet：https://lenovopress.lenovo.com/datasheet/en-us/ds0187-lenovo-thinksystem-n1380-neptune
