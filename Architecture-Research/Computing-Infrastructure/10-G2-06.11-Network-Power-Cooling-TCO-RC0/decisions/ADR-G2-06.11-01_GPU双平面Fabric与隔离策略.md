# ADR-G2-06.11-01｜GPU 双平面 Fabric 与隔离策略

- 状态：Proposed
- 日期：2026-11-14
- 评审范围：GPU Fabric、CPU North-South、Storage、WAN、Control/OOB、设施管理网络

## 背景

双区域十星包含 72-GPU NVL72、CPU/HPC、容量存储、控制节点和跨区域业务。若所有流量汇聚到单一 Ethernet/IB Fabric，将造成拥塞域、故障域、租户边界和安全域混杂。GB300 GPU Collective 对带宽、时延、拓扑和拥塞高度敏感，普通以太网 LAG 不等同于 rail-aware multi-plane。

## 决策候选

### 方案 A：Spectrum-6 Ethernet/RoCE 双平面
- 每区域 Plane-A/Plane-B 各 1 台 SN6600，形成两个独立 GPU Compute Fabric。
- GPU tray NIC 连接按 HPE/NVIDIA port map 均匀分布到两个平面。
- NCCL/通信运行时负责跨平面负载均衡与故障隔离。
- RoCE 的 PFC/ECN、buffer、DSCP/PCP、QoS、拥塞控制和端到端版本必须一起验证。
- CPU Converged、Storage、WAN、OOB 仍独立设计，不能因都使用 Ethernet 就合并为一个拥塞域。

### 方案 B：Quantum-X800 InfiniBand 双平面
- 每区域 Plane-A/Plane-B 各 1 台 Q3400-RA，形成独立 IB Fabric。
- 使用受支持的 ConnectX-8 IB 模式、UFM/SM、线缆和 NIC 固件。
- Storage/WAN 使用独立 Ethernet 网络或经过明确验证的协议网关。
- 适合现有 IB 训练/HPC 能力较强的团队。

## 当前建议

以方案 A 作为主参考，方案 B 保留为条件性替代。理由：
1. 十星是跨 GPU、CPU/HPC、存储、企业业务与 WAN 的混合基础设施，Ethernet 便于分层互联与企业网络治理。
2. NVIDIA NVL72 Enterprise RA 提供 Spectrum-based GPU RDMA Fabric、rail-optimized topology 与多平面示例。
3. Spectrum-6 SN6600 的端口与吞吐规格满足单 rack 起步的候选评估，但最终 port map、oversubscription 和扩展 leaf/spine 仍需验证。
4. 不能将 RoCE 复杂性低估；若团队无成熟 RoCE 运维能力，IB 可能更稳妥。

## 关键隔离原则

- Plane-A 与 Plane-B 物理分离；不跨平面 LAG/MLAG/堆叠。
- GPU E-W 不承载 Storage/Checkpoint 主流量。
- Storage Fabric 与 CPU North-South 逻辑和容量分别核算。
- OOB/BMC/设施管理物理隔离；租户网络不能直达。
- WAN 不作为默认 GPU collective 传输网络。
- Region A/B 的 GPU Fabric 不默认跨区合并为单一训练域。
- ADS/RCP 只获取遥测和资源可用状态，不直接更改交换机配置或设备安全策略；网络 Owner 保留配置与变更审批权。

## 待验证假设

1. HPE NVL72 72 个 tray-side OSFP 物理接口可按每 plane 36 个接口均匀拆分，且 OEM 端口表支持该 rail map。
2. SN6600 与 HPE ConnectX-8 在目标 NOS/固件/光模块组合上互操作。
3. 单 rack 起步每 plane 一台 SN6600 足以满足无阻塞目标；扩展到多 rack 时需要额外 leaf/spine。
4. 双平面在单交换机、单光链路、单 NIC、单线缆故障下能按预期退化。
5. RoCE 的 PFC/ECN/拥塞策略能够避免 pause storm 和队列相互影响。
6. Storage/CPU 交换机端口与带宽满足 Checkpoint、模型加载和数据服务目标。

## 验收门禁

- OEM 签署的端口/rail/光模块/线缆映射；
- 双平面拓扑和故障域图；
- 单平面停机、单交换机维护、单链路失效测试；
- NCCL all-reduce、all-gather、broadcast、all-to-all 基准；
- RoCE PFC/ECN、队列、缓冲、拥塞和多租户隔离测试，或 IB fabric 对应验证；
- Storage/Checkpoint 与 GPU collective 并发压测；
- WAN 分区/恢复测试；
- OOB 隔离、配置审计和回滚测试；
- 网络 Owner、平台 Owner、GPU Owner 与独立见证签署。

## 后果

正面：故障域、拥塞域和权限边界清晰；单平面失效不必立即丧失全部 GPU 互联能力。

代价：设备、光模块、线缆和运维成本提高；两平面需要独立监控、容量规划、变更窗口和故障演练。
