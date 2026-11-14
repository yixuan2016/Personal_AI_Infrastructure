# Agent Ecology V1.9｜痕迹协作实证、能力发现、信任与撤销传播

**版本状态：候选研究版 0.2｜日期：2026-11-15**

V1.9 不重写 V1.3 已建立的痕迹协作概念，也不替代 V1.4 Environment Runtime、V1.5 生态自治、V1.6 世界模型、V1.7 RSI 和 V1.8 跨生态联邦治理。本版本由三个互补工作流组成：A 线研究 Stigmergy 实证、共享环境、持久工件和局部反应；B 线研究跨生态能力发现、联邦摘要目录与 Observation Runtime；C 线研究双边信任、Owner 签名、委托衰减和目标域本地授权。三条线共同回答：如何让 Agent 通过可信环境状态协作，同时保持本地数据权威、授权边界和人类治理。

## 文件导航

- 00_V1.9_痕迹协作实证进展与架构增量研究.md：A 线主研究报告与架构建议。
- 01_研究证据登记.csv：7 项论文/研究证据、实验、复现材料、成熟度和架构启发。
- 02_合成实验与验收矩阵.csv：22 项 Stigmergy 合成对照实验。
- 03_架构决策记录.md：16 项候选 ADR（ADR-101—ADR-116）。
- 04_威胁与治理边界.csv：26 项共享环境、跨生态发现与身份授权威胁。
- 05_跨生态能力发现与目录联邦架构决策备忘录.md：B 线本地权威目录、联邦摘要目录、能力广告、候选解析和本地授权边界。
- 06_研究证据与引用边界.md：跨生态能力发现、协议和身份研究证据。
- 08_能力发现契约静态审查与缺口清单.md：能力发现契约的 10 项静态审查缺口与候选修复记录。
- 09_WP-020_跨生态信任协议与能力授权链设计.md：双边信任、Owner 签名、委托衰减、令牌交换、密钥轮换和撤销协议。
- 10_WP-020_研究证据登记.md：SPIFFE、OpenID Federation、OAuth、DPoP、JWS/JWT、JCS 规范证据。
- 11_WP-020_信任协议静态审查与未决事项.md：WP-020 的 10 项未决事项和静态检查边界。
- 12_WP-021_跨生态能力目录一致性与撤销传播协议.md：目录同步、事件序列、撤销墓碑、快照恢复、反熵和网络分区安全。
- 13_WP-021_研究证据登记.md：CloudEvents、Kubernetes Watch、etcd、Dynamo、RFC 9162 与 CRDT 证据。
- 14_WP-021_静态审查与未决事项.md：34 项验收设计的静态审查边界和 10 项开放问题。
- contracts/：能力广告、能力解析、能力生命周期事件、Peer Trust Binding、Owner Delegation Grant、Capability Owner Attestation、Federation Revocation Event、Federation Sync Checkpoint 候选 JSON Schema（8 份）。
- validation/F1_CAPABILITY_DISCOVERY_MATRIX.csv：31 项 F1 能力发现、资格一致性与事件契约验收矩阵。
- validation/WP020_TRUST_PROTOCOL_VALIDATION_MATRIX.csv：27 项跨生态信任、委托、令牌与撤销验收设计。
- validation/WP021_CATALOG_CONSISTENCY_REVOCATION_MATRIX.csv：36 项目录一致性、事件幂等、撤销传播、快照恢复和分区安全验收设计。
- assets/00_V1.9_跨生态能力发现与观察Runtime.svg：7680×4320 SVG 架构源图。
- assets/01_WP-020_跨生态信任协议与授权链.svg：7680×4320 SVG 信任与授权链架构源图。
- assets/02_WP-021_目录一致性与撤销传播架构.svg：7680×4320 SVG 目录同步与撤销传播架构源图。
- STATUS.md：本版本状态和禁止越过的门禁。
- GITHUB_BLOB_MANIFEST.md：Git Blob 标识清单；Git Blob SHA 不等同于文件 SHA-256。

## 本版关键结论

1. Stigmergy 不等于共享黑板，也不等于把所有 Agent 对话搬进共享记忆。核心是持久环境状态、可追溯痕迹/工件、局部观察和后续行动之间的反馈闭环。
2. 共享状态默认视为通信通道；即使没有协作意图或显式 A2A 消息，也可能发生跨主体信息访问与影响。
3. 环境检索必须有界；每次读取采用 top-k 和权限/来源/新鲜度过滤，不能要求每个 Agent 读取全量群体记录。
4. 持久工件必须脱离原生产者继续存在，并保留来源、版本、引用和验证证据。
5. A2A 用于明确的主体间协商、委派和交互；痕迹协作仍作为默认的持久协调机制。MCP 继续承担 Agent-to-Tool 的垂直工具接入。
6. 学习型局部规则只能在隔离环境中训练和评估；运行时继续执行确定性校验、授权、过期、冲突处理和人类治理门禁。
7. 多 Agent 不是默认最优。每类任务必须与单 Agent 基线在相同总推理预算、工具和评估条件下比较。
8. 能力发现目录与能力 Owner 本地权威目录分离；联邦摘要可以最终一致，执行前授权必须由目标生态本地 PDP/PEP 决定。
9. 共享环境的重新观察由 Runtime 通过订阅、唤醒、游标续读和周期对账保障，不依赖模型自发重读。
10. A2A、MCP、CloudEvents、Ontology、SPIFFE 及本地 PDP/PEP 责任边界清晰；任何协议消息均不自动构成授权。

## 证据边界

本版引用的研究包括预印本、已发表论文、协议草案、正式规范和受控仿真实验。论文报告的实验结果不等于本项目已复现、已部署或已通过验收。Stigmergy 合成实验 22 项、F1 能力发现与契约验收 31 项、WP-020 信任协议验收 27 项、WP-021 目录一致性与撤销传播验收 36 项，共 116 项全部 NOT_RUN；22 项 ADR 全部 Candidate；34 项威胁全部 Candidate。V1.8 F0 12 项 Gate 仍全部 NotRun；没有真实领域数据授权、Runtime 执行或生产写入。

八份候选 JSON Schema 已确认 JSON 语法有效，但尚未完成完整 Draft 2020-12 Validator、密码学签名验证、跨字段语义验证和协议互操作测试。静态审查的 10 项缺口中，7 项已形成候选契约修复，1 项部分修复，2 项仍开放。productionAllowed=false。


## WP-020｜跨生态信任协议

- 默认采用双边显式 Trust Binding；各生态独立 Trust Anchor；不自动传递信任。
- SPIFFE/SVID 是可选工作负载身份适配；OpenID Federation 是可选信任链适配；两者均不替代业务授权。
- 能力 Owner 或获授权 Publisher 签名能力声明；JWS/JCS 仅证明声明来源和完整性，不授予调用权限。
- Owner Delegation Grant 是发布/委托权限对象，不是任务执行令牌；子委托必须单调衰减。
- 目标域本地 Authorization Server/PDP 决定是否签发短期、受众绑定凭证；Token Exchange 仅表达 Subject/Actor 委托上下文。
- DPoP/mTLS 可用于发送方约束；撤销状态按来源域独立维护 Epoch。
- WP-020 验收设计 27 项全部 NOT_RUN；10 项静态未决事项开放；无真实密钥、生产令牌或跨域授权启用。


## WP-021｜跨生态能力目录一致性与撤销传播

- 目录发现允许最终一致；安全撤销采用来源域签名事件、单调墓碑和接收域本地执行门禁。
- 每条 Peer Binding 安全控制 Feed 使用独立连续序列；(source,id) 持久去重；跨 Domain/Stream 不比较序列。
- 已验证撤销立即写入墓碑；事件 Gap 不推进连续水位并阻断高风险跨域动作。
- 历史压缩后要求来源域签名的完整可查询撤销快照、Snapshot Digest、Merkle Root 和连续性证据；不能仅凭 Root 或消息 ACK 认为撤销状态完整。
- Merkle 反熵差异定位与 RFC 9162 追加历史一致性证明分开使用；RFC 9162 为 Experimental RFC，Gossip / split-view 仍需独立验证。
- Freshness Budget 由目标域 Policy Owner 配置；FCP 离线时本地 PEP / Kill Switch 仍可 DENY。
- WP-021 验收设计 36 项全部 NOT_RUN；10 项未决事项开放；未部署消息总线或真实撤销 Feed。
