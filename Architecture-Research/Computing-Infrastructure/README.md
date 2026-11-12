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
