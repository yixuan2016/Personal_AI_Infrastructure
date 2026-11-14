# ADR-G2-06.9-01｜异构硬件候选与分层配置策略

- **状态：** Proposed，待硬件/OEM/站点/能源 Owner 评审
- **日期：** 2026-11-13
- **范围：** 双区域十星 CPU、GPU、存储、网络和设施设备候选

## 决策

1. 十星采用异构节点组合，不要求十颗星硬件完全一致。
2. CPU 候选纳入 AMD EPYC 9006 SP7（9956/9996/9966/9756）与 Intel Xeon 6980P 对照；新平台必须完成 OEM/BIOS/QVL 验证。
3. GPU 分为 NVIDIA Blackwell Ultra（GB300 NVL72/HGX B300）与 AMD Instinct MI350（MI355X OAM/MI350P PCIe）两条候选路线，分别建立驱动、互连和软件基线。
4. NVIDIA Vera Rubin NVL72 作为前瞻路线，不作为当前已验证基线。
5. 存储按 Gen6/Gen5 NVMe 热温层与高容量 HDD 冷层分级；Micron 9650、9550、Solidigm D7-PS1010、Kioxia CM7-V、Seagate Mozaic 4+ 纳入候选。
6. GPU Scale-out 网络采用 InfiniBand 或 Ethernet 两条路线独立验证；Quantum-X800 与 Spectrum-6/Spectrum-X 不视为可无条件互换。
7. Broadcom Tomahawk 6 作为交换 ASIC 候选，整机交换机型号必须由 OEM 另行确认。
8. 机柜功率、液冷、光模块、线缆和设施联锁属于配置冻结的硬门槛。
9. 厂商公开规格不等于采购可得性、OEM 兼容性或现场验收通过。

## 不采用的方案

- 不为十颗星套用完全相同的标准 BOM。
- 不用单 GPU 峰值或单交换芯片带宽代表集群有效能力。
- 不将 OAM 模块与 PCIe 加速卡直接互换。
- 不将机柜级 NVL72 与 8-GPU HGX 节点视为同类设备。
- 不在没有真实任务测试和设施核算前冻结采购数量。

## 待验证假设

- EPYC 9006 SP7 OEM 平台可以在目标地区提供稳定供货与长期维护。
- NVIDIA 与 AMD GPU 两条路线均能满足目标任务，并有明确的运维/软件兼容边界。
- PCIe Gen6 SSD 可在目标主机平台发挥有效性能，不被主机/网络/文件系统瓶颈限制。
- 800G InfiniBand 或 Ethernet 可按站点网络拓扑实现所需的端到端性能和隔离。
- 目标站点具备高功率 GPU 设备所需的供电、液冷和安全条件。

## 验收证据

正式 OEM SKU、QVL、供货承诺、驱动/固件兼容矩阵、任务基准、机柜功率与液冷报告、端到端网络测量、存储故障恢复报告、独立见证和 Owner 签署。
