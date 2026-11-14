# Personal AI Infrastructure｜算力底座架构研究归档

**归档日期：** 2026-11-10  
**仓库路径：** `Architecture-Research/Computing-Infrastructure/`  
**性质：** 架构研究与机器可读契约候选资料；不包含生产实现代码，不代表 Owner 已签署或真实双站点测试通过。

## 1. 归档范围

本目录独立保存算力底座与双站点联邦互操作相关资料，不修改仓库根目录、PAI 核心文件、既有 Packs、Releases 或安全配置。

| 目录 | 内容 | 当前状态 |
|---|---|---|
| `00-Source-Baselines/` | DM04 跨域交易接口与数据契约冻结候选基线 | RC0 候选 |
| `01-G0-Architecture-Governance/` | 六域权威责任、签署边界、URI 治理 | 待双方 Owner 签署 |
| `02-G1-Ontology-Protocol-Consistency/` | Ontology、DM04、A2A、CloudEvents、FWSX 分层一致性 | 候选，66 项验收待执行 |
| `03-G2-OntologyV3.1-IFC0.2-Contract-Governance/` | Ontology V3.1、IFC0.2、ADS/SCO API、75 操作映射 | RC0 候选；待评审 |
| `04-AEE-ASCP-V1.0-RC0/` | AEE/ASCP V1.0 初始契约评审 | RC0 候选 |
| `05-AEE-ASCP-V1.1-RC0-Dual-Site-Interop/` | 六域映射、双站点联邦互操作、18 项增量验收 | RC0 候选，待执行 |
| `06-G2-04-REST-Binding-RC1-Dual-Site-Transaction/` | REST Binding RC1、交易状态机、Activation Barrier、Saga、40 项故障注入 | RC1 候选，待评审 |
| `archives/` | G0/G1/G2/AEE-ASCP 原始完整 ZIP 包 | 历史附件；非唯一交付 |
| `manifests/` | 文件清单、SHA-256、来源与版本状态 | 本次归档生成 |

## 2. 研究演进关系

- **G0：** 固定六域权威与签署边界，明确 SCO/ADS/站点本地 Owner 的责任分离。
- **G1：** 校正 Ontology 与协议映射，分清 A2A、CloudEvents、FWSX、DM04 的协议层次。
- **G2：** 推进 Ontology V3.1、DM04 IFC0.2 增量提案和 ADS/SCO REST Binding；完成 75 个 operation 逐项映射及 16 项契约缺口识别。
- **G2-04：** 将契约治理落实到 REST Header、幂等、ETag、强类型响应、跨站点 Prepare/Commit、Activation Barrier、Saga 恢复和独立验收。

## 3. 全局架构不变量

1. ADS 是横向协同治理与共同语义层，不是单纯网关或调度器；但不能替代资源/数据 Owner 的最终授权。
2. SCO 管理跨站点合同、计划、Saga 与全局交易投影；不签发本地 ResourceLease/FencingToken，不绕过 Site LCP / PDP / PEP。
3. TaskClaim 与 ResourceLease 分离；两者都不能替代 PolicyDecision。
4. 目录登记 ≠ 能力验证 ≠ 发布 ≠ 领域采用 ≠ 运行可用。
5. 数据可发现 ≠ 可读取 ≠ 可训练；DataUseGrant 由 Data Owner 签发，目标站点 PEP 每次访问复核。
6. Operation Accepted ≠ 业务对象成功；Unknown ≠ Failed，必须先向原权威 Owner 对账。
7. 结果提交 ≠ 独立验收；验收 ≠ 最终结算。
8. 多 Agent 协作以共享环境中的持久状态、事件、claim、回执和证据为主；A2A 消息是协商/唤醒通道，不是唯一事实源。
9. 高风险动作保留人类外环治理、审批、否决、接管和最终问责权。

## 4. 本次 G2-04 重点

- `Idempotency-Key`：非幂等副作用 POST 必需；同 key 不同 digest 返回 409。
- `If-Match / ETag`：更新已有对象必需；缺失 428，版本冲突 412。
- `X-Request-ID` / `X-Correlation-ID`：与逻辑 Envelope 字段一致。
- `ResponseContext`：分离 Operation 命令状态与业务对象权威状态。
- `Activation Barrier`：所有必需站点 CommitReceipt、Policy、Grant、Trust、Attestation、撤销水位和本地 Ready 回执通过才允许激活。
- `Saga`：部分 Commit 不启动；Unknown 先对账；补偿以 Stop/Release/Reconcile 回执追加事实。
- `40 项故障注入矩阵`：覆盖重复请求、部分成功、网络分区、撤销缺口、旧 FencingToken、验收和结算争议等。

## 5. 版本与验证声明

所有阶段文件均保留其原始状态标签。RC0/RC1、Proposed、Candidate、待签署、待验证等状态不因归档或推送而自动升级。Schema 结构检查、静态矩阵和图表生成不等于 OpenAPI 工具链互操作、Owner 签署、真实部署或双站点验收通过。

## 6. 后续放行顺序

1. ADS/SCO API Owner 与六域 Owner 审核 G2-03 75 操作映射。
2. REST Binding RC1 转为机器可读 OpenAPI，统一工具链验证。
3. Site A/B 签署本地 Reservation/Lease/TaskRun 权威边界与 Barrier 条件。
4. 执行 G1 66 项与 G2-04 40 项测试，增加两套独立实现互操作证据。
5. 故障注入通过、证据链齐全、回滚/补偿有效后，才考虑正式冻结。

## 7. 目录使用约定

- 本目录只放算力底座架构研究、契约、图表、验收矩阵和版本证据。
- 不放个人 MEMORY、私密聊天记录、凭据、密钥、真实访问令牌、客户数据或本地私有目录。
- 不覆盖仓库既有 README、安全配置、PAI 受保护文件或其他 Pack。
- 原始 ZIP 仅用于完整包下载；可审查源文件以目录内的 Markdown、CSV、JSON Schema、SVG、Word、Excel 为准。


## G2-06.5 / G2-06.6 区域联邦研究

- [G2-06.5 区域协调层详细设计](07-G2-06.6-Regional-Federation-Protocol-RC0/G2-06.5_区域协调层详细设计.md)：区域协调平面、目录分片、故障自治与验收。
- [G2-06.6 跨区域协议与数据契约](07-G2-06.6-Regional-Federation-Protocol-RC0/G2-06.6_跨区域协议与数据契约规范.md)：API 操作、请求信封、身份、数据边界与错误模型。
- [G2-06.6 事件与一致性契约](07-G2-06.6-Regional-Federation-Protocol-RC0/G2-06.6_跨区域事件与一致性契约.md)：CloudEvents 信封、Owner epoch/sequence、快照修复与撤销传播。
- [G2-06.6 Saga 与恢复协议](07-G2-06.6-Regional-Federation-Protocol-RC0/G2-06.6_Saga与恢复协议.md)：跨区域 Prepare/Commit、Activation Barrier、补偿和恢复。

以上均为 RC0 架构候选，待 Owner 评审和双实现互操作验证。


- [G2-06.7 十星控制面容量与跨区域网络模型](07-G2-06.6-Regional-Federation-Protocol-RC0/G2-06.7_十星控制面容量与跨区域网络模型.md)：控制面容量、跨区域网络、数据位置、GPU Fabric、存储与设施约束。


## G2-06.8 双区域十星故障注入与自治恢复

- [G2-06.8 阶段目录](08-G2-06.8-Fault-Injection-Recovery-RC0/README.md)：故障域、自治恢复状态机、故障注入、独立见证与验收门禁。
- [双区域十星故障注入与自治恢复架构](08-G2-06.8-Fault-Injection-Recovery-RC0/G2-06.8_双区域十星故障注入与自治恢复架构.md)：故障遏制、Owner 权威、恢复条件与安全停止边界。
- [故障注入与恢复演练手册](08-G2-06.8-Fault-Injection-Recovery-RC0/G2-06.8_故障注入与恢复演练手册.md)：10 类重点演练场景及组合故障顺序。
- [独立见证与十星验收门禁](08-G2-06.8-Fault-Injection-Recovery-RC0/G2-06.8_独立见证与十星验收门禁.md)：Gate 0—4、双实现互操作和证据链要求。

G2-06.8 当前为 RC0 候选方案；文件归档不代表真实故障注入或十星现场验收已完成。


## G2-06.9 十星硬件型号与异构节点参考配置

- [G2-06.9 阶段目录](09-G2-06.9-Hardware-Reference-Architecture-RC0/README.md)：CPU/GPU/存储/网络设备候选型号和阶段边界。
- [十星 CPU/GPU/存储/网络设备型号参考选型](09-G2-06.9-Hardware-Reference-Architecture-RC0/G2-06.9_十星CPU_GPU存储网络设备型号参考选型.md)：AMD EPYC 9006 SP7、Intel Xeon 6980P、NVIDIA GB300/HGX B300、AMD MI355X/MI350P、Micron 9650/9550、Seagate Mozaic 4+、Quantum-X800、Spectrum-6 等候选型号。
- [十星异构节点与区域部署配置](09-G2-06.9-Hardware-Reference-Architecture-RC0/G2-06.9_十星异构节点与区域部署配置.md)：控制/通用、GPU、存储、网络和设施节点角色。

G2-06.9 型号来自厂商官方资料核查；均为候选，不代表采购、OEM 兼容认证或现场验收通过。


## G2-06.10 双区域十星 OEM 级设备配置与基础设施预算

- [G2-06.10 阶段目录](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/README.md)：OEM 整机、十星角色、功率/液冷预算和采购验收边界。
- [双区域十星 OEM 级整机与配置参考架构](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/G2-06.10_双区域十星OEM级整机与配置参考架构.md)：HPE GB300 NVL72、Dell XE9712、Lenovo 7DJV、SC755 V5/N1380、R7725xd、R9815、XE9780L/XE9785L 等平台。
- [功率液冷与机房基础设施预算模型](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/G2-06.10_功率液冷与机房基础设施预算模型.md)：区分设备实际功耗、PSU/Power Shelf 容量、EDPp、母线规划和 CDU 冷量。
- [十星设备 BOM 与端口配置清单](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/matrices/G2-06.10_十星设备BOM与端口配置清单.csv)：按区域、星位和设备域列出候选数量、端口和待确认项。
- [OEM 兼容性与采购验收矩阵](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/matrices/G2-06.10_OEM兼容性与采购验收矩阵.csv)：30 项 QVL、功率、液冷、网络、采购与验收检查。
- [单星配置卡与部署边界](10-G2-06.10-OEM-BOM-Power-Cooling-RC0/G2-06.10_单星配置卡与部署边界.md)：A1—A5、B1—B5 角色与 Owner 边界。

G2-06.10 当前为 RC0 候选配置；完整订货 SKU、QVL、区域报价、现场功率/液冷测量和设施验收尚未完成。


## G2-06.11 双区域十星网络互连、供电单线、液冷 P&ID 与五年 TCO

- [G2-06.11 阶段目录](10-G2-06.11-Network-Power-Cooling-TCO-RC0/README.md)：网络、端口/光模块、供电、液冷、TCO 与验收门禁。
- [双区域网络分层与拓扑设计](10-G2-06.11-Network-Power-Cooling-TCO-RC0/G2-06.11_双区域网络分层与拓扑设计.md)：Spectrum-6 RoCE 双平面主参考、Quantum-X800 InfiniBand 替代、CPU North-South、Storage、WAN 和 OOB 隔离。
- [端口映射、光模块与线缆 BOM](10-G2-06.11-Network-Power-Cooling-TCO-RC0/G2-06.11_端口映射光模块与线缆BOM.csv)：按区域和网络平面列出物理接口、线缆与光模块计数口径。
- [双路供电单线与支路容量设计](10-G2-06.11-Network-Power-Cooling-TCO-RC0/G2-06.11_双路供电单线与支路容量设计.md)：HPE 8×Power Shelf/Whip、UPS/PDU A/B、N1380 PCS、发电机、计量和安全边界。
- [液冷 P&ID 与监测联锁设计](10-G2-06.11-Network-Power-Cooling-TCO-RC0/G2-06.11_液冷P&ID与监测联锁设计.md)：设施一次侧、CDU、设备二次侧、Manifold、冷板、泵冗余和漏液硬联锁。
- [五年 TCO 参数化预算模型](10-G2-06.11-Network-Power-Cooling-TCO-RC0/G2-06.11_五年TCO参数化预算模型.csv)：设备/网络/供配电/液冷/软件/运维报价与能耗水耗输入模板，不填虚构价格。
- [ADR-G2-06.11-01 GPU 双平面 Fabric 与隔离策略](10-G2-06.11-Network-Power-Cooling-TCO-RC0/decisions/ADR-G2-06.11-01_GPU双平面Fabric与隔离策略.md)：主参考 Ethernet/RoCE，IB 条件性替代。
- [网络、电力、液冷联调验收矩阵](10-G2-06.11-Network-Power-Cooling-TCO-RC0/matrices/G2-06.11_网络电力液冷联调验收矩阵.csv)：38 项验收与证据要求。
- [双区域网络拓扑图源](10-G2-06.11-Network-Power-Cooling-TCO-RC0/diagrams/G2-06.11_双区域网络拓扑.mmd)、[供电单线图源](10-G2-06.11-Network-Power-Cooling-TCO-RC0/diagrams/G2-06.11_供电单线图.mmd)、[液冷 P&ID 图源](10-G2-06.11-Network-Power-Cooling-TCO-RC0/diagrams/G2-06.11_液冷P&ID图.mmd)。

G2-06.11 为 RC0 架构参考；端口速率/Breakout、光模块料号、完整支路 A/B 映射、正式施工 P&ID、设备 QVL、现场实测和 OEM/设施签署仍待完成。


## G2-06.12 双区域十星 OEM 采购规格与机房工程输入条件

- [G2-06.12 阶段目录](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/README.md)：RFQ技术需求、OEM响应、机房工程输入、地区法规、设备负载、液冷/网络回填、FAT/SAT和风险登记。
- [十星工程采购技术需求书](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_十星工程采购技术需求书_RFQ.md)：GPU/CPU/HPC/存储/控制/网络/供配电/液冷/安全/服务与五年TCO的OEM询价要求。
- [OEM设备响应与偏差矩阵](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_OEM设备响应与偏差矩阵.csv)：28项供应商响应、核验和Owner分工。
- [机房工程输入条件基线](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_机房工程输入条件基线.md)：机柜空间/结构、电力、冷却、水资源、网络、消防和站点数据清单。
- [区域法规与标准适用性矩阵](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_区域法规与标准适用性矩阵.csv)：全球参考、中国大陆与北美适用性分支；待具体站点和AHJ确认。
- [设备负载与设施容量输入表](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_设备负载与设施容量输入表.csv)：分开记录IT负载、设施负载、额定容量与待测功耗。
- [液冷OEM数据回填表](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_液冷OEM数据回填表.csv)：热负载、温度、流量、压降、水质、泵与CDU冗余。
- [网络端口与光链路回填模板](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_网络端口与光链路回填模板.csv)：逐端口、模块、线缆、FEC、QoS、QVL和链路证据。
- [采购验收与FAT/SAT门禁矩阵](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_采购验收与FAT_SAT门禁矩阵.csv)：35项采购、站点、工厂、现场和双区域验收门禁。
- [采购与工程风险登记册](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_采购与工程风险登记册.csv)：14项关键风险及预防/回退。
- [决策记录与开放问题](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_决策记录与开放问题.md)、[官方资料与证据登记册](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/G2-06.12_官方资料与证据登记册.md)。
- [采购工程门禁流程](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/diagrams/G2-06.12_采购工程门禁流程.mmd)、[双区域十星场地逻辑布局](11-G2-06.12-OEM-RFQ-Site-Engineering-RC0/diagrams/G2-06.12_双区域十星场地逻辑布局.mmd)。

G2-06.12 为 RC0/RFQ 草案，不是已冻结采购订单、合同技术附件或施工图。站点国家/城市、OEM正式SKU/BOM/QVL、功率/热工曲线、SC tray兼容性、法规与许可仍待确认。


## G2-06.13 双区域十星站点选址、能源资源可行性与五年投资模型

- [G2-06.13 阶段目录](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/README.md)：选址框架、评分模型、现场尽调、供电/水/网络、双区域独立性、五年TCO与门禁。
- [双区域站点选址决策框架](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_双区域站点选址决策框架.md)：单站点100分评分、硬性否决门槛、A/B组合独立性评分和S0—S8阶段门。
- [站点评分权重与打分规则](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_站点评分权重与打分规则.csv)：电力25、水资源/冷却15、网络15、灾害12、法规10、经济10、建设8、服务5。
- [站点尽调数据采集模板](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_站点尽调数据采集模板.csv)：地块、供电、水务、运营商、气候、灾害、法规、工程和商务数据。
- [供电容量与并网可行性评估](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_供电容量与并网可行性评估.md)：firm MW、送电日期、输电扩建、费率、冗余、负荷和计量边界。
- [水资源冷却与气候适配评估](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_水资源冷却与气候适配评估.md)：水权/供水、旱情、WUE、8760小时热工仿真、CDU与设备水路边界。
- [网络运营商与物理路由多样性验证](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_网络运营商与物理路由多样性验证.md)：双运营商物理路由、管道/入楼/PoP多样性和跨区SLO。
- [双区域独立性与共同故障域评估](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_双区域独立性与共同故障域评估.md)：电网、流域、光纤、灾害、供应链和身份/密钥共同依赖。
- [设备负载能源与容量测算输入表](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_设备负载能源与容量测算输入表.csv)、[五年TCO与单位有效算力成本模型](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_五年TCO与单位有效算力成本模型.csv)：不填虚构功率/报价，按OEM和站点证据回填。
- [站点风险登记册](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_站点风险登记册.csv)、[站点尽调与选址门禁矩阵](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_站点尽调与选址门禁矩阵.csv)。
- [ADR-01双区域站点选择原则](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_ADR-01双区域站点选择原则.md)、[官方资料与证据登记册](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/G2-06.13_官方资料与证据登记册.md)。
- [站点筛选与投资决策流程](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/diagrams/G2-06.13_站点筛选与投资决策流程.mmd)、[双区域资源与故障域逻辑图](12-G2-06.13-Dual-Region-Site-Selection-Energy-TCO-RC0/diagrams/G2-06.13_双区域资源与故障域逻辑图.mmd)。

G2-06.13 当前为RC0筛选框架。候选国家/城市/园区/地块尚未指定；未取得项目级firm MW、取水/排水许可、运营商物理路由证明、现场工程报告和正式报价，不形成站点选定或投资批准结论。


## G2-06.14 双区域候选区域筛选与资源条件横向比较

- [G2-06.14 阶段目录](13-G2-06.14-Regional-Candidate-Comparison-RC0/README.md)：中国大陆、美国与跨境双区域路线的区域长名单和桌面初筛。
- [双区域候选区域筛选与横向比较报告](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_双区域候选区域筛选与横向比较报告.md)：候选池、政策/能源/水/网络初筛、工作负载分工和下一轮证据任务。
- [中国大陆候选区域初筛矩阵](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_中国大陆候选区域初筛矩阵.csv)：呼和浩特—和林格尔—乌兰察布、庆阳、中卫、贵安及需求侧枢纽对照。
- [美国候选区域初筛矩阵](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_美国候选区域初筛矩阵.csv)：MISO、PJM俄亥俄/北弗吉尼亚、ERCOT西部、华盛顿/俄勒冈。
- [双区域组合路线与故障域分析](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_双区域组合路线与故障域分析.md)：中国同国、美国同国、中国+美国跨国三条路线并行评估。
- [候选区域证据缺口与核验任务](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_候选区域证据缺口与核验任务.csv)：22项utility、水务、运营商、地块、合规和TCO核验任务。
- [ADR-02候选区域筛选与双区域路线](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_ADR-02候选区域筛选与双区域路线.md)：建议决策及待业主确认事项。
- [官方证据与政策登记册](13-G2-06.14-Regional-Candidate-Comparison-RC0/G2-06.14_官方证据与政策登记册.md)：国家发改委、国家能源局、内蒙古能源局、NERC、ERCOT、MISO、PJM、EIA、USGS和华盛顿州政府原始来源。
- [候选区域筛选与双区域决策流程](13-G2-06.14-Regional-Candidate-Comparison-RC0/diagrams/G2-06.14_候选区域筛选与双区域决策流程.mmd)。

G2-06.14当前为RC0区域长名单和桌面初筛；未取得园区/地块级firm MW、送电日期、供水/排水许可、端到端光纤物理路由、地勘/许可和正式报价，不做正式100分区域排名、不冻结国家/城市组合、不形成投资批准。


## G2-06.15 候选园区与基础设施资源尽调

- [G2-06.15 研究目录](14-G2-06.15-Park-Level-Due-Diligence-RC0/README.md)：园区级分型、官方许可与公用事业资料、地块证据缺口、项目RFI与新增D门禁。
- [园区尽调方法论](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_园区级尽调与方法论.md)：P1园区/P2运营项目/P3审批项目/P4可交易地块/P5限制样本；不把既有项目容量当本项目资源。
- [中国大陆园区与项目样本台账](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_中国大陆园区与项目样本台账.csv)：和林格尔、乌兰察布、庆阳、中卫、贵安。
- [美国园区与项目样本台账](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_美国园区与项目样本台账.csv)：Altoona、New Albany、Loudoun/Ashburn、Abilene、Quincy、Hillsboro。
- [20项工程证据缺口](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_电力水资源网络工程证据缺口矩阵.csv)：电力、水务、光纤、土地、许可、结构、TCO与双区域独立性。
- [园区/utility/水务/运营商/OEM RFI](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_公用事业园区运营商RFI问询清单.md)：用于向项目资源拥有方索取可审计的书面答复。
- [高密GPU与液冷机房工程准入规范](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_高密GPU与液冷机房工程准入规范.md)。
- [政策许可与风险特殊事项](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_政策许可与风险特殊事项.md)：中卫项目许可、美国New Albany/Loudoun/Hillsboro新建限制、Quincy/Grant PUD大型负荷排队。
- [ADR-G2-06.15-01](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_站点决策与独立性ADR.md)、[官方证据登记册](14-G2-06.15-Park-Level-Due-Diligence-RC0/G2-06.15_官方证据来源登记册.md)。
- [园区级D/E/W/F/S硬门禁流程图](14-G2-06.15-Park-Level-Due-Diligence-RC0/diagrams/G2-06.15_园区尽调与否决门禁.mmd)。

状态：RC0/公开资料桌面尽调；尚无本项目可交易地块、firm MW、水权、双运营商物理路由或地块专业工程验收；不签发选址/采购/施工放行。


## G2-06.16｜双区域十星自建/高密托管/租赁设施自建IT路线比较

- [G2-06.16 阶段目录](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/README.md)：三路线工程架构、设施所有权与控制权、同口径五年TCO、工程准入、SLA、独立故障域和验收。
- [三路线决策报告](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_三路线工程架构与决策报告.md)：A完全自建、B高密托管入驻、C租赁Powered Shell + 自建IT；另以公有云GPU作为外部成本对照，不等同NVLink物理机柜。
- [设施与控制权RACI矩阵](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_设施与控制权RACI矩阵.csv)：20项建筑/供配电/CDU/硬联锁/网络/数据/授权/审计等职责。
- [高密GPU入驻技术准入清单](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_高密GPU入驻技术准入清单.md)：GB300 Whip、真实供电、CDU一次/二次侧、水质、满液点载荷、OOB/双Fabric、退租与FAT/SAT。
- [托管合同与服务SLA关键条款](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_托管合同与服务SLA关键条款.md)：合同技术输入，非正式法律意见。
- [五年TCO计算与边界规则](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_五年TCO计算与边界规则.md)、[24项TCO变量回填模板](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_TCO变量回填模板.csv)：M1—M5计费模式避免租赁/电费/PUE/水耗重复计入。
- [三路线100分评价权重](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_路线评分与硬门槛.csv)：9项维度、硬性否决优先；无项目证据不实际打分。
- [32项FAT/SAT与故障注入验收矩阵](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_FAT_SAT与故障注入验收矩阵.csv)。
- [跨区域自治与运营故障域](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_跨区域自治与运营故障域.md)：设施硬联锁在本地优先，Site LCP/Owner保持IT资源权威，ADS/RCP不越权控制供电冷却。
- [18项风险与回退](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_风险与回退登记册.csv)、[22项供应商RFI问题](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_供应商RFI回应模板.csv)。
- [ADR-03自建托管混合路线](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_ADR-03自建托管混合路线.md)、[官方资料与证据](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_官方资料与证据登记册.md)。
- [三路线设施归属架构图](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/diagrams/G2-06.16_三路线设施归属拓扑.mmd)、[工程与合同决策门禁图](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/diagrams/G2-06.16_工程与合同决策门禁.mmd)。

G2-06.16 = RC0 / Proposed。暂建议优先验证C、以A为长期对照、B为高密可交付的快速备选；尚无任何项目级firm MW/液冷容量/地块租约/正式报价/FAT/SAT，不能宣称已完成最终方案选定或成本最优。

- [G2-06.16 文件交付清单及SHA-256](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/G2-06.16_交付清单与SHA256校验记录.md)、[逐文件SHA256SUMS](15-G2-06.16-Build-Colo-Hybrid-Decision-RC0/SHA256SUMS.txt)：本轮16个正文/CSV/图源文件的远端UTF-8内容哈希。阶段共18个文件（16研究文件+2校验文件）；不替代完整仓库ZIP验包。
