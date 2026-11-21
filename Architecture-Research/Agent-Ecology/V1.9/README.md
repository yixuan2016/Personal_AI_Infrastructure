# Agent Ecology V1.9｜痕迹协作实证、能力发现、信任、撤销传播与可信见证

**版本状态：候选研究版 0.4｜日期：2026-11-16**

V1.9 不重写 V1.3 已建立的痕迹协作概念，也不替代 V1.4 Environment Runtime、V1.5 生态自治、V1.6 世界模型、V1.7 RSI 和 V1.8 跨生态联邦治理。本版本由九个互补工作流组成：A 线研究 Stigmergy 实证、共享环境、持久工件和局部反应；B 线研究跨生态能力发现、联邦摘要目录与 Observation Runtime；C—G 线分别研究 WP-020 信任授权、WP-021 目录撤销、WP-022 多方见证、WP-023 成员治理与恢复、WP-024 形式化验证；H 线研究 WP-025 多生态动态联盟；I 线研究 WP-026 Coalition Charter 与联盟生命周期。九条线共同回答：如何让 Agent 通过可信环境状态协作，并在动态联盟中保持本地数据权威、授权边界、资源公平和人类治理。

## 文件导航

- 00_V1.9_痕迹协作实证进展与架构增量研究.md：A 线主研究报告与架构建议。
- 01_研究证据登记.csv：7 项论文/研究证据、实验、复现材料、成熟度和架构启发。
- 02_合成实验与验收矩阵.csv：39 项总体验收主矩阵，其中 STG-01—22 为 Stigmergy 实验，ECO-01—17 为动态联盟场景；WP-025 专项矩阵是这 17 项的独立视图，不重复计数。
- 03_架构决策记录.md：68 项候选 ADR（ADR-101—ADR-168）。
- 04_威胁与治理边界.csv：94 项共享环境、跨生态发现、身份授权、撤销传播、可信见证和动态联盟威胁。
- 05_跨生态能力发现与目录联邦架构决策备忘录.md：B 线本地权威目录、联邦摘要目录、能力广告、候选解析和本地授权边界。
- 06_研究证据与引用边界.md：跨生态能力发现、协议和身份研究证据。
- 08_能力发现契约静态审查与缺口清单.md：能力发现契约的 10 项静态审查缺口与候选修复记录。
- 09_WP-020_跨生态信任协议与能力授权链设计.md：双边信任、Owner 签名、委托衰减、令牌交换、密钥轮换和撤销协议。
- 10_WP-020_研究证据登记.md：SPIFFE、OpenID Federation、OAuth、DPoP、JWS/JWT、JCS 规范证据。
- 11_WP-020_信任协议静态审查与未决事项.md：WP-020 的 10 项未决事项和静态检查边界。
- 12_WP-021_跨生态能力目录一致性与撤销传播协议.md：目录同步、事件序列、撤销墓碑、快照恢复、反熵和网络分区安全。
- 13_WP-021_研究证据登记.md：CloudEvents、Kubernetes Watch、etcd、Dynamo、RFC 9162 与 CRDT 证据。
- 14_WP-021_静态审查与未决事项.md：36 项验收设计的静态审查边界和 10 项开放问题。
- 15_WP-022_跨生态事件可信见证与多方一致性验证.md：Witness、Quorum Policy、Monitor Gossip、Fork Evidence 和争议治理设计。
- 16_WP-022_研究证据登记.md：RFC 9162、C2SP Witness/Cosignature/Policy、Sigsum、RFC 9943 和 Trillian 证据。
- 17_WP-022_静态审查与未决事项.md：40 项验收设计边界和 12 项开放问题。
- 18_WP-023_可信见证网络治理与灾难恢复.md：成员生命周期、密钥轮换、信任根升级、备份恢复、Joint Quorum 和灾难恢复 Runbook。
- 19_WP-023_研究证据登记.md：TUF、Sigstore、NIST SP 800-57、C2SP Witness 的规范状态和适用边界。
- 20_WP-023_静态审查与未决事项.md：50 项验收设计边界和 15 项开放问题。
- 21_WP-024_跨生态可信见证网络形式化验证与韧性评估.md：Quorum 语义、恢复安全预算、形式化性质、模拟和故障注入方案。
- 22_WP-024_研究证据登记.md：2026 年状态擦除恢复预印本、C2SP、PBFT、FoundationDB、Jepsen 和 TLA+ 证据。
- 23_WP-024_TLA+模型变量与性质目录.md：有限状态模型变量、动作、不变量和反例模型目录。
- 24_WP-024_实验设计与静态审查.md：60 项验证设计、静态检查边界和 12 项未决问题。
- 25_WP-024-L0L1_组合穷举与恢复状态模型验证报告.md：262,611 组 Quorum 集合对穷举及 Python BFS 有界状态验证结果。
- 26_WP-024-L2_多检查点原子性与成员迁移模型扩展.md：多 Checkpoint 原子推进、Epoch 绑定、Joint Quorum 和外部恢复锚模型扩展。
- 27_WP-025_多生态动态联盟形成与自治治理架构.md：动态联盟形成、准入硬门禁、资源公平、独立验收和自治边界。
- 28_WP-026_Coalition_Charter_联盟任务契约与生命周期状态机.md：联盟公共契约、领域 Profile、多方接受、Lease/Fencing、变更与解散清算。
- 29_WP-026_研究证据登记.md：ODRL、PROV-O、CloudEvents、etcd、ZooKeeper 和 JCS 证据边界。
- 30_WP-026_静态审查与未决事项.md：38 项验收设计的静态边界和 12 项开放问题。
- contracts/：能力广告、能力解析、能力生命周期事件、Peer Trust Binding、Owner Delegation Grant、Capability Owner Attestation、Federation Revocation Event、Federation Sync Checkpoint、Witness Registry、Witness Quorum Policy、Checkpoint Cosignature Bundle、Fork Evidence Bundle 候选 JSON Schema（21 份）。
- validation/F1_CAPABILITY_DISCOVERY_MATRIX.csv：31 项 F1 能力发现、资格一致性与事件契约验收矩阵。
- validation/WP020_TRUST_PROTOCOL_VALIDATION_MATRIX.csv：27 项跨生态信任、委托、令牌与撤销验收设计。
- validation/WP021_CATALOG_CONSISTENCY_REVOCATION_MATRIX.csv：36 项目录一致性、事件幂等、撤销传播、快照恢复和分区安全验收设计。
- validation/WP022_MULTI_WITNESS_QUORUM_MATRIX.csv：40 项 Witness 单调性、Quorum 交集、独立性、Gossip、分叉证据和隐私验收设计。
- validation/WP023_WITNESS_GOVERNANCE_RECOVERY_MATRIX.csv：50 项成员生命周期、密钥轮换、根升级、状态恢复、Joint Quorum 和事故治理验收设计。
- validation/WP024_WITNESS_RESILIENCE_MATRIX.csv：60 项 Quorum、状态恢复、网络分区、恶意行为、共同故障域和策略迁移验收设计。
- validation/WP025_DYNAMIC_COALITION_MATRIX.csv：17 项动态联盟形成、准入、资源公平、退出和价值归因验收设计。
- validation/WP026_COALITION_CHARTER_LIFECYCLE_MATRIX.csv：38 项 Charter、Owner 接受、状态机、租约/Fencing、授权分离和解散清算验收设计。
- assets/00_V1.9_跨生态能力发现与观察Runtime.svg：7680×4320 SVG 架构源图。
- assets/01_WP-020_跨生态信任协议与授权链.svg：7680×4320 SVG 信任与授权链架构源图。
- assets/02_WP-021_目录一致性与撤销传播架构.svg：7680×4320 SVG 目录同步与撤销传播架构源图。
- assets/03_WP-022_跨生态事件可信见证与多方一致性验证.svg：7680×4320 SVG 多方见证与分叉检测架构源图。
- assets/04_WP-023_可信见证网络治理与灾难恢复.svg：7680×4320 SVG 成员治理、密钥生命周期和恢复架构源图。
- assets/05_WP-024_可信见证网络形式化验证与韧性评估.svg：7680×4320 SVG 数学模型、形式化检查、确定性模拟、故障注入和独立审查架构源图。
- assets/06_WP-026_Coalition_Charter_联盟任务契约与生命周期架构.svg：7680×4320 SVG 动态联盟契约、Owner 接受、状态机、Fencing 和独立验收架构源图。
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

本版引用的研究包括预印本、已发表论文、协议草案、正式规范和受控仿真实验。论文报告的实验结果不等于本项目已复现、已部署或已通过验收。总体验收主矩阵 39 项（Stigmergy 22 项 + 动态联盟 17 项）、F1 能力发现 31 项、WP-020 27 项、WP-021 36 项、WP-022 40 项、WP-023 50 项、WP-024 60 项、WP-026 38 项，V1.9 共 321 项全部 NOT_RUN；68 项 ADR 全部 Candidate；94 项威胁全部 Candidate。V1.8 F0 12 项 Gate 仍全部 NotRun；没有真实领域数据授权、Runtime 执行或生产写入。

二十一份候选 JSON Schema 已确认 JSON 语法有效，但尚未完成完整 Draft 2020-12 Validator、密码学签名验证、跨字段语义验证和协议互操作测试。静态审查的 10 项缺口中，7 项已形成候选契约修复，1 项部分修复，2 项仍开放。productionAllowed=false。


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


## WP-022｜跨生态事件可信见证与多方一致性验证

- 每个生态保留自己的透明证据日志，不建立全局超级日志；日志默认只登记摘要和最小元数据。
- Witness 对每个 Log Origin 持久保存最新 Checkpoint，验证 Log 签名、treeSize 单调性、rootHash 和 Merkle Consistency Proof；状态检查、更新和签名必须原子化。
- Quorum Policy 绑定 Peer Binding 和策略版本；同时核验公钥、运营域、故障域和 Key Epoch。
- 在固定成员与拜占庭假设下，Quorum 交集候选条件为 2q-n>f；该公式不证明真实运营独立性，也不抵御超过 f 的串谋。
- Monitor 直接从多个 Witness 获取最新 Checkpoint；Gossip 用于传播与发现冲突，不构成全局共识。
- Fork Evidence 固定冲突 Checkpoint、签名、Proof、Witness 响应、Policy Version 和独立验证结果；争议由人类治理外环处理。
- WP-022 验收设计 40 项全部 NOT_RUN；12 项静态未决事项开放；未部署真实 Witness、透明日志或生产密钥。


## WP-023｜可信见证网络治理、密钥生命周期与灾难恢复

- Witness 成员先经身份核验和 OBSERVE_ONLY，再进入 ACTIVE；暂停、隔离、退出与重新加入均通过追加式生命周期事件表达。
- Trust Root、Witness、Log、Backup、Transport 密钥用途隔离；根密钥离线多方分持，日常 Witness 密钥受控托管。
- 正常 Root Rotation 逐版本验证旧根和新根阈值；根失陷时使用事前登记的带外 Emergency Recovery Anchors。
- 历史签名验证区分检测时间、最早疑似泄露时间、确认时间和撤销时间；证据不足时返回 INDETERMINATE。
- 快照签名不代表快照最新；恢复必须与外部 Witness Checkpoint、WAL 水位、Root/Registry/Policy Version 和 Key Epoch 对账。
- Witness 成员替换采用 OBSERVE_ONLY 与 Joint Quorum；恢复连续性无法证明时保持 QUARANTINED/HOLD。
- WP-023 验收设计 50 项全部 NOT_RUN；15 项静态未决事项开放；未部署真实根密钥、HSM/KMS、Witness 备份或灾难恢复流程。


## WP-024｜可信见证网络形式化验证与韧性评估

- Witness Quorum 明确定位为跨生态透明证据的多方观察/签署门槛，不等同于完整 BFT 状态机共识。
- 将状态擦除恢复、身份克隆、持久化与签名竞态、存储回滚、非对称分区和共同故障域纳入验证模型。
- 参数网格：n=4/7/10/13；f=1/2/3/4；q=3/5/7/9；最小交集为 2/3/4/5。
- 新增 TLA+ Witness 恢复模型源文件及三份 TLC 配置；TLC 尚未运行。
- 新增确定性模拟、Jepsen 风格故障历史与独立 Checker 的分层验证方案。
- 新增 60 项正式验收设计，全部 NOT_RUN；新增 3 份候选 Schema；WP-024 静态未决事项 16 项。
- 新增 ADR-141—ADR-154；威胁矩阵扩展至 TH-70。
- 不因分区或恢复失败降低 Quorum 门槛；不能证明状态连续性时隔离身份。


## WP-024-L0/L1｜已执行的有界预验证
- L0：4 组 Quorum 参数、262,611 个不同集合对完成穷举；最小交集全部符合 2q-n=f+1。
- L1：Python BFS 两种危险恢复配置发现 14 步冲突证书反例；两种安全恢复配置未发现有界反例。
- 已新增 TLA+ 模型与三份 TLC 配置，但 TLC 尚未执行。
- 详细执行结果见 25_WP-024-L0L1_组合穷举与恢复状态模型验证报告.md。
- 60 项正式验收矩阵仍全部 NOT_RUN；有界参考模型结果不等于生产安全证明。


## WP-025｜多生态动态联盟形成与自治治理
- 联盟是临时协作结构，不是新的主权主体；不设全局永久大联盟或超级编排器。
- 采用联邦式动态联盟：Task Owner 保留目标与验收权；各成员 Owner 保留本域能力、数据、资源和执行授权权。
- 身份、Owner 证明、目标域本地授权、撤销新鲜度、数据用途和资源资格为不可交易硬门禁。
- 多 Agent 方案必须与同工具、同预算的强单 Agent 基线比较；协作增益不足以覆盖成本时不形成联盟。
- 执行、独立验证、价值归因和人类问责分离；贡献评分不自动提升权限。
- WP-025 专项验收矩阵 17 项全部 NOT_RUN（与总体验收主矩阵中的 ECO-01—ECO-17 为同一批场景，不重复计数）；6 项 ADR（ADR-155—ADR-160）Candidate；12 项威胁（TH-71—TH-82）Candidate。

## WP-026｜Coalition Charter 联盟任务契约与生命周期
- 采用最小公共核心 + 版本化领域 Profile；领域 Profile 不得改变公共核心安全语义。
- Charter 记录任务范围、角色、责任和 Owner 接受，不是 Grant、Permit、Lease 或结算指令。
- 多方接受必须绑定同一 Charter Digest / Version / Epoch；跨 Owner 部分接受不视为全局原子提交。
- Charter 变更产生新版本；受影响 Owner 重新接受；旧签名不得跨版本复用。
- Task/Resource Lease 与本地 Permit 分离；Fencing Token 必须在资源 Owner 端事务性校验；副作用携带幂等 operationId。
- CLOSED 必须有凭证撤销、租约释放、资源回收、数据处置和审计归档证据。
- WP-026 验收矩阵 38 项全部 NOT_RUN；2 份候选 Schema；8 项 ADR（ADR-161—ADR-168）Candidate；12 项威胁（TH-83—TH-94）Candidate；12 项语义缺口 OPEN。


## 论文研究计划

- 31_Agent_Ecology_CCF-B论文研究计划与首篇论文设计.md：Agent Ecology 全景研究计划、首篇 AAMAS 期刊论文定位、理论模型、研究问题、可证伪假设、对照实验、统计方法、论文系列规划与投稿门禁。
- 当前仅为研究计划和实验设计；首篇论文实验尚未完成，不代表已投稿或发表。

- 32_相关工作比较矩阵与新颖性审查.md：首篇论文的直接相关研究比较、机制差异、新颖性主张边界、潜在审稿质疑和最小实证证据要求。

## V1.9｜21 份候选 JSON Schema 静态审查

- [33_V1.9_21份候选JSON_Schema元模型与互操作静态审查.md](./33_V1.9_21份候选JSON_Schema元模型与互操作静态审查.md)：逐一核对 21 份 Schema，列出 4 项 P0、10 项 P1 协议与互操作缺口。
- JSON 语法 21/21 解析成功；完整 Draft 2020-12 Validator、密码学、Policy Validator 和跨语言互操作仍 NOT_RUN。
- 21 份 Schema 继续保持 Candidate；321 项验收仍 NOT_RUN；F0 未通过；productionAllowed=false。

