# CHANGELOG

## 2026-11-10｜V1.2—V1.7 研究归档
- 归档协议契约、Ontology、Environment Runtime、生态自治、世界模型/数字孪生和生态级 RSI 研究资料。
- 纳入 Markdown、CSV、JSON、YAML、SVG、威胁矩阵、验收矩阵与研究证据。
- 修复 V1.3—V1.7 主报告的 SVG 图片引用，并新增归档审查和二进制资产状态记录。

## 2026-11-10｜V1.8 跨生态联邦与 F0 治理
- 新增跨生态联邦拓扑、本地主权职责边界、多生态协同与跨域策略兼容设计。
- 新增身份、能力声明、信任向量、改进提案、证据包和本地采用回执契约。
- 新增 F0 治理章程、不可委托权限清单、成员生命周期、密钥与跨域授权模型。
- 新增 R0-R4 风险/审批矩阵、RACI、决策登记册、12 项 F0 Gate。
- 新增成员声明与 DataUseGrant Schema；验证矩阵 23 项、威胁矩阵 16 项，全部 NotRun。
- 新增 3 张 SVG 架构源图和 V1.8 二进制资产状态清单。
- V1.8 为架构研究和候选契约，不代表工程实现或双生态互操作验收。

## 2026-11-14｜V1.9-A 痕迹协作实证与架构增量（Candidate）
- 新增近期共享记忆、Substrate-centric、Waggle 局部规则、SwarmWorld 持久工件、协作收益边界和环境/意图消息分离研究。
- 新增 V1.9 主报告、7 项研究证据登记、22 项 Stigmergy 合成实验与验收设计、8 项基础候选 ADR、12 项基础威胁与治理边界。
- 补充共享状态通信通道、有界发现、来源感知排序、持久工件谱系、局部反应、选择性 A2A 和单 Agent 基线要求。

## 2026-11-14｜V1.9-B 跨生态能力发现与联邦目录（Candidate）
- 新增本地权威能力目录与联邦摘要目录双层架构，明确发现视图可最终一致、执行前授权必须由目标生态本地 PDP/PEP 决定。
- 新增能力广告与能力解析候选 JSON Schema、20 项 F1 验收矩阵及跨生态能力发现架构备忘录。
- 新增 Observation Runtime 设计：事件订阅、状态唤醒、游标续读、周期对账、命名空间隔离和审计。
- 补充 A2A、MCP、CloudEvents、Ontology、SPIFFE 的职责边界，以及 MACP Internet-Draft 的证据等级与本地自治适配原则。
- 新增 7680×4320 SVG 架构源图和独立证据登记；威胁矩阵扩展至 18 项，ADR 扩展至 10 项。
- 新增能力发现候选契约静态审查，登记 10 项 Schema/语义/授权缺口；两份 JSON 文件仅完成语法解析检查，未完成完整 Schema、密码学或互操作验证。
- 合成实验与验收共 42 项全部 NOT_RUN；10 项 ADR 全部 Candidate；F0 12 项 Gate 仍未通过；productionAllowed=false。

## 2026-11-14｜V1.9 能力发现契约静态审查与候选修复
- 对 CapabilityAdvertisement、CapabilityResolution 和生命周期事件 Schema 完成 JSON 语法静态回读。
- 新增机器可读 notAuthorization=true、VERIFIED 验证上下文、NAMED_DOMAINS 可见域约束、成本单位和证据等级约束。
- 增加候选资格与 attestation/revocation/freshness 状态组合约束；增加每个候选的来源水位、撤销 Epoch 和观察有效期。
- 增加分页请求字段和能力生命周期 CloudEvents 候选 Schema。
- 静态审查 10 项缺口：7 项已形成候选修复、1 项部分修复、2 项仍开放；签名密码学、时间单调性、完整 Draft 2020-12 Validator 与互操作测试仍未执行。
- F1 验收扩展至 30 项，V1.9 合成实验与验收共 52 项全部 NOT_RUN；productionAllowed=false。

- F1 能力发现/契约矩阵增加冲突状态优先级测试；INELIGIBLE 优先于 HOLD，F1 测试增至 31 项，V1.9 验收总数增至 53 项，全部 NOT_RUN。


## 2026-11-14｜V1.9-C WP-020 跨生态信任协议与能力授权链（Candidate）
- 新增 WP-020 架构决策备忘录、研究证据登记、静态审查与 10 项未决事项。
- 新增 Peer Trust Binding、Owner Delegation Grant、Capability Owner Attestation 三份候选 JSON Schema。
- 新增 27 项跨生态信任、Owner 签名、委托衰减、Token Exchange、DPoP、撤销与审计验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 信任与授权链架构源图。
- 新增 ADR-111—ADR-116；威胁矩阵扩展至 26 项；总候选 ADR 为 16 项。
- 默认双边显式信任、关闭传递信任；SPIFFE/OIDF 为可选适配；目标域本地 Authorization Server/PDP 保留最终授权权威。
- 六份候选 Schema 仅完成 JSON 语法解析检查；未完成完整 Draft 2020-12 Validator、密码学、父子委托语义和协议互操作测试。
- V1.9 合成实验与验收共 80 项全部 NOT_RUN；F0 未通过；productionAllowed=false；Runner 未启用。

- Peer Trust Binding 进一步要求 Trust Anchor 与 Trust Domain 显式绑定、双方对同一 agreementDigest 签署接受收据；R4 不进入 Agent 委托；WP-020 验收增至 27 项，V1.9 总验收增至 80 项，全部 NOT_RUN。


## 2026-11-15｜V1.9-D WP-021 跨生态目录一致性与撤销传播（Candidate）
- 新增 WP-021 架构备忘录、研究证据登记和静态审查/未决事项。
- 新增 Federation Revocation Event 与 Federation Sync Checkpoint 两份候选 JSON Schema。
- 新增 36 项目录一致性、事件幂等、撤销墓碑、事件缺口、快照恢复、Merkle 对账和网络分区验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 目录一致性与撤销传播架构源图。
- 新增 ADR-117—ADR-122；威胁矩阵扩展至 34 项；总候选 ADR 为 22 项。
- 采用 Peer Binding 专属连续 Feed、(source,id) 持久去重、有效撤销立即落墓碑、Gap 高风险 HOLD、完整签名快照恢复和 FCP 非权威中继边界。
- CloudEvents、Kubernetes Watch、etcd、Dynamo、RFC 9162 和 CRDT 作为技术证据；不把规范原语误写为项目已实现。
- 修正 WP-020 测试数量索引：27 项；V1.9 总验收 116 项全部 NOT_RUN。
- 八份候选 Schema 仅完成 JSON 语法检查；完整 Validator、密码学、语义和互操作测试未执行；F0 未通过；productionAllowed=false；Runner 未启用。

- 撤销事件契约补充 peerbindingid，新增两项 Feed 绑定负向测试；WP-021 验收增至 36 项，V1.9 总验收增至 116 项，全部 NOT_RUN。


## 2026-11-15｜V1.9-E WP-022 跨生态事件可信见证与多方一致性验证（Candidate）
- 新增 WP-022 架构备忘录、研究证据登记和静态审查/12 项未决事项。
- 新增 Witness Registry、Witness Quorum Policy、Checkpoint Cosignature Bundle、Fork Evidence Bundle 四份候选 JSON Schema。
- 新增 40 项 Witness 单调性、Quorum 交集、运营独立性、Monitor Gossip、分叉证据和隐私验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 多方见证与分叉检测架构源图。
- 新增 ADR-123—ADR-130；威胁矩阵扩展至 44 项；总候选 ADR 为 30 项。
- 候选设计：每生态独立透明证据日志、Witness 原子持久化与单调 Checkpoint、2q-n>f 交集条件、运营/故障域多样性、Monitor 旁路观察和人类争议治理。
- 研究证据包括 RFC 9162（Experimental）、RFC 9943（Proposed Standard）、C2SP Witness/Cosignature/Policy、Sigsum 和 Trillian；规范状态与适用边界均已登记。
- V1.9 总验收扩展至 156 项，全部 NOT_RUN；候选 JSON Schema 增至 12 份，仅完成 JSON 语法检查；架构源图增至 4 张。
- 未部署真实 Witness、透明日志、Quorum 或生产密钥；F0 未通过；productionAllowed=false；Runner 未启用。


## 2026-11-15｜V1.9-F WP-023 可信见证网络治理、密钥生命周期与灾难恢复（Candidate）
- 新增 WP-023 架构备忘录、研究证据登记和静态审查/15 项未决事项。
- 新增 Witness Lifecycle Event、Witness Key Lifecycle Record、Witness Recovery Snapshot Manifest、Trust Root Update Envelope 四份候选 JSON Schema。
- 新增 50 项成员生命周期、密钥轮换、根升级、状态恢复、Joint Quorum 和事故治理验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 可信见证网络治理与灾难恢复架构源图。
- 新增 ADR-131—ADR-140；威胁矩阵扩展至 56 项；总候选 ADR 为 40 项。
- 候选设计：OBSERVE_ONLY 成员准入、密钥用途隔离、Key Epoch 单调、旧根/新根双阈值升级、带外紧急恢复锚、外部 Checkpoint 对账、Joint Quorum 和失败隔离。
- 研究证据包括 TUF 1.0.37、Sigstore 官方安全模型、NIST SP 800-57 Rev.6 Initial Public Draft、C2SP Witness Protocol v1.1.0；严格区分最终规范、草案与社区规范。
- V1.9 总验收扩展至 206 项，全部 NOT_RUN；候选 JSON Schema 增至 16 份，仅完成 JSON 语法检查；架构源图增至 5 张。
- 未部署真实根密钥、Witness 密钥、HSM/KMS、备份系统或灾难恢复流程；V1.8 F0 未通过；productionAllowed=false；Runner 未启用。


## 2026-11-15｜V1.9-G WP-024 形式化验证与韧性评估（Candidate）
- 新增 WP-024 架构备忘录、研究证据登记、TLA+ 模型变量与性质目录、实验设计和静态审查。
- 新增 60 项 Quorum、状态擦除恢复、存储回滚、网络分区、恶意行为、共同故障域和策略迁移验收设计，全部 NOT_RUN。
- 新增 3 份候选 Schema：故障场景、实验运行记录和实验结果证据包。
- 新增 7680×4320 SVG 形式化验证与韧性评估架构源图。
- 新增 ADR-141—ADR-150；威胁矩阵扩展至 TH-66。
- 纳入 arXiv:2610.07759（2026-10-06 预印本）关于状态擦除恢复与 Quorum 交集的研究；明确其单阶段证书模型边界，不泛化为 Witness 协议已被证明不安全。
- 核心决策：Witness Quorum 不等同于 BFT 共识；签名前持久化；恢复防回滚；身份克隆隔离；故障/分区不得自动降低 q。
- V1.9 总验收扩展至 266 项，全部 NOT_RUN；候选 Schema 增至 19 份；架构源图增至 6 张。
- 未运行 TLC、确定性模拟、故障注入或真实恢复演练；V1.8 F0 未通过；productionAllowed=false；Runner 未启用。


## 2026-11-15｜V1.9-G WP-024-L0/L1 Quorum 穷举与恢复状态模型验证
- L0 对 n=4/7/10/13、q=2f+1 的全部不同 Quorum 集合对进行穷举，共 262,611 对；四组最小交集全部符合 2q-n=f+1。
- L1 Python BFS 有限状态参考模型对两种危险恢复配置分别探索 130,375 / 149,546 个状态，并找到 14 步冲突证书反例。
- 对释放前持久化+恢复隔离、释放前持久化+保留单调状态两种配置，分别探索 67,500 / 43,904 个状态，未发现有界反例。
- 新增 TLA+ WitnessRecovery 模型与三份 TLC 配置；TLC 尚未运行，Python BFS 结果不冒充 TLC 结果。
- 新增 L0/L1 验证报告、标准库 Python 参考检查器、穷举 CSV、模型结果 JSON 和反例轨迹。
- 新增 ADR-151—ADR-154；威胁矩阵扩展至 TH-70；静态未决事项共 53 项。
- 正式 60 项 WP-024 验收矩阵仍全部 NOT_RUN；生产授权关闭；Runner 未启用。


## 2026-11-16｜V1.9-H WP-024-L2 多 Checkpoint 原子性与成员迁移模型扩展（Candidate）
- 新增 WP-024-L2 研究备忘录，审查现有 WitnessRecovery TLA+ 最小模型的覆盖边界。
- 基于 C2SP Witness v1.1.0 明确多 Checkpoint Compare-and-Advance 原子推进要求；基于 TUF 1.0.37 细化 Trust Root 逐版本双阈值迁移。
- 核对 NIST SP 800-57 Rev.6 仍为 Initial Public Draft；明确不将草案表述为最终规范。
- 设计 Membership Epoch、Key Epoch、外部恢复锚、Joint Quorum 和 14 项 L2 最小验证场景。
- TLC、确定性模拟、故障注入与独立复核均未执行；正式 266 项验收仍 NOT_RUN，productionAllowed=false，Runner 未启用。


## 2026-11-16｜V1.9-I WP-025 多生态动态联盟形成与自治治理（Candidate）
- 新增 WP-025 架构研究备忘录，研究联邦式动态联盟、任务契约、能力准入、资源公平、价值归因和自治权边界。
- 纳入 2026 年自治 Agent 联盟结构综述、能力中心型联盟研究、Nature Machine Intelligence 多 Agent 对照评估、ACL MultiAgentBench、Stigmergy 多智能体实验、分布式资源分配综述和 Ostrom 嵌套治理原则。
- 新增 ECO-01—ECO-17 共 17 项候选验收场景，全部 NOT_RUN。
- 新增 ADR-155—ADR-160 共 6 项候选决策；威胁矩阵新增 TH-71—TH-82 共 12 项。
- 推荐联邦式动态联盟：任务驱动、Owner 本地准入、Charter 限定协调权、Stigmergy 作为状态底座、A2A 作为必要协商通道、ADS 负责生态内协调。
- 不新增生产 Schema 或 Runtime；未执行仿真、Shadow 或跨生态试点；V1.8 F0 未通过；productionAllowed=false；Runner 未启用。


## 2026-11-16｜V1.9-H WP-025 多生态动态联盟形成与自治治理（Candidate）
- 新增多生态动态联盟架构研究：联邦式临时联盟、Owner 本地准入、Coordinator 权限边界、资源公平、独立验证和解散治理。
- 新增 17 项动态联盟验收设计，全部 NOT_RUN。
- 新增 ADR-155—ADR-160；威胁矩阵扩展至 TH-82。
- 明确联盟不构成新主权主体；多 Agent 采用前必须与匹配预算的强单 Agent 基线比较。
- 本轮仅完成架构研究，不部署 Runtime、不运行真实跨生态任务。

## 2026-11-16｜V1.9-I WP-026 Coalition Charter 契约与生命周期（Candidate）
- 新增 WP-026 架构备忘录、研究证据登记和静态审查/12 项未决事项。
- 新增 Coalition Charter 与 Coalition Lifecycle Event 两份候选 JSON Schema；V1.9 总计 21 份。
- 新增 38 项 Charter、Owner 接受、状态机、租约/Fencing、授权分离和解散清算验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 联盟任务契约与生命周期架构源图。
- 新增 ADR-161—ADR-168；威胁矩阵扩展至 TH-94。
- 采用最小公共核心 + 版本化领域 Profile、多 Owner 同 Digest 接受、Charter 非授权、不可变版本、资源端 Fencing、幂等副作用和独立验收。
- 研究依据包括 W3C ODRL 2.2、PROV-O、CloudEvents、etcd 事务/API Guarantees、ZooKeeper Recipes 与 RFC 8785 JCS。
- V1.9 总验收扩展至 321 项，全部 NOT_RUN；ADR 共 68 项、威胁共 94 项、Schema 共 21 份、架构图共 7 张。
- 完整 JSON Schema Validator、签名验证、TLA+、Runtime 和真实跨生态试验均未执行；V1.8 F0 未通过；productionAllowed=false；Runner 未启用。

- 验收计数口径校准：总体验收主矩阵 02 含 STG-01—22 与 ECO-01—17 共 39 项；WP025 专项矩阵是 ECO 子集，不重复计数。V1.9 总计 319 项（39 + 31 + 27 + 36 + 40 + 50 + 60 + 36），全部 NOT_RUN。
- ADR/威胁登记去重：ADR-155—ADR-160、TH-71—TH-82 保留唯一记录；当前唯一候选 ADR 68 项、威胁 94 项。

- WP-026 补充 CloudEvents 1.0 事件封装检查：扩展属性保持小写，actor/signature 对象置于 data 负载；新增 2 项验收设计，WP-026 增至 38 项，V1.9 总验收增至 321 项，全部 NOT_RUN。
