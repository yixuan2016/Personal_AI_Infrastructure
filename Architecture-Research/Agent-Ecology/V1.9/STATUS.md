# V1.9 状态记录

- 版本：Agent Ecology V1.9｜Stigmergy、能力发现、跨生态信任、撤销传播与可信见证
- 日期：2026-11-15
- 状态：Candidate / Draft
- 工作分支：research/agent-ecology-v1.9-stigmergy-20261114
- 基线：PR #12 的 V1.8 分支 HEAD 4e337089470076b25058a7c47edaacab77bcaa58

## 工作流 A｜Stigmergy 与共享环境
- 主研究报告、7 项研究证据登记、22 项合成实验与验收矩阵、8 项基础候选 ADR、12 项基础威胁与治理边界已入库。
- 22 项合成实验全部 NOT_RUN。

## 工作流 B｜跨生态能力发现与联邦目录
- 能力发现与目录联邦架构决策备忘录及独立研究证据边界已入库。
- 能力广告、能力解析和能力生命周期 CloudEvents JSON Schema：3 份 Candidate；JSON 语法已通过解析检查，但未完成 Draft 2020-12 完整验证。
- F1 能力发现与契约验收矩阵：31 项，全部 NOT_RUN。
- WP-020 信任协议验证矩阵：27 项，全部 NOT_RUN。
- 新增 Observation Runtime、联邦目录新鲜度、撤销水位、A2A/MCP/CloudEvents/SPIFFE 协议边界设计。
- 新增 7680×4320 SVG 架构源图。
- 新增 2 项候选 ADR：ADR-109、ADR-110。
- WP-020 新增 6 项候选 ADR：ADR-111—ADR-116。
- 新增能力发现契约静态审查：10 项缺口；7 项形成候选修复、1 项部分修复、2 项仍开放；完整 Validator 与密码学验证未执行。

## 工作流 C｜WP-020 跨生态信任协议
- 新增跨生态信任协议与能力授权链设计备忘录、研究证据登记、静态审查与未决事项。
- 新增 Peer Trust Binding、Owner Delegation Grant、Capability Owner Attestation 三份候选 JSON Schema（V1.9 总计六份）。
- 新增 WP-020 验收矩阵 27 项，全部 NOT_RUN。
- 新增 7680×4320 SVG 信任与授权链架构源图。
- Peer Trust Binding 增加 Trust Domain 锚绑定、双边签名收据与 agreementDigest 一致性要求；R4 不允许 Agent 委托。
- 新增 6 项候选 ADR（ADR-111—ADR-116），威胁矩阵扩展至 26 项。

## 总体边界
- 合成实验与验收：156 项，全部 NOT_RUN。
- 架构决策：30 项，全部 Candidate，未获正式批准。
- 威胁与治理边界：44 项，全部 Candidate。
- V1.8 F0 Gate：12 项全部 NotRun，F0 未通过。
- 生产实现：未开始；本轮不包含工程代码。
- 真实数据：未导入；未获得任何新增数据共享授权。
- Runtime/双生态/生产测试：未执行。
- 人类审批、独立评估、Owner 签署：未取得。
- Runner：未启用；生产凭证未接入。
- WP-020 实际双边信任关系：未建立；真实根密钥/Owner 密钥：未接入；OAuth 令牌交换：未运行。
- 主线：未修改；V1.9 作为 stacked review 候选增量，不直接合并 main。
- productionAllowed=false

## 验收边界
- 研究资料入库不等于研究结论已在本项目复现。
- JSON 语法解析通过不等于 JSON Schema 完整验证或密码学验证。
- 静态文件回读不等于实验执行。
- Git Blob Manifest 只记录 Git 对象标识，不代替 SHA-256 校验。
- 所有未执行项必须保持 NOT_RUN；不得将候选 ADR 解释为已批准决策。
- WP-020 10 项静态未决事项均未关闭；JSON 语法检查不等于完整 Schema 或密码学验证。


## 工作流 D｜WP-021 跨生态目录一致性与撤销传播
- 新增 WP-021 架构备忘录、研究证据登记、静态审查与 10 项未决事项。
- 新增 Federation Revocation Event 与 Federation Sync Checkpoint 两份候选 JSON Schema（V1.9 总计八份）。
- 新增 WP-021 验收矩阵 36 项，全部 NOT_RUN。
- 新增 7680×4320 SVG 目录一致性与撤销传播架构源图。
- 新增 6 项候选 ADR（ADR-117—ADR-122）；威胁矩阵扩展至 34 项。
- 候选约束：Peer Binding 专属连续 Feed、(source,id) 持久幂等去重、撤销墓碑只增不减、Gap 高风险 HOLD、完整签名快照恢复、FCP 仅中继与反熵。
- 未部署事件总线、未运行撤销传播实验、未开展 Merkle Proof 或跨接收方 Gossip 互操作。

## WP-021 阶段快照（历史记录）
- 合成实验与验收：116 项，全部 NOT_RUN。
- 架构决策：22 项，全部 Candidate，未获正式批准。
- 威胁与治理边界：34 项，全部 Candidate。
- 候选 JSON Schema：8 份，仅完成 JSON 语法检查；完整 Draft 2020-12 Validator、语义和密码学验证未执行。
- 架构源图：3 张 7680×4320 SVG。
- WP-021 10 项静态未决事项均未关闭。


## 工作流 E｜WP-022 跨生态事件可信见证与多方一致性验证
- 新增 WP-022 架构备忘录、研究证据登记、静态审查与 12 项未决事项。
- 新增 Witness Registry、Witness Quorum Policy、Checkpoint Cosignature Bundle、Fork Evidence Bundle 四份候选 JSON Schema（V1.9 总计十二份）。
- 新增 WP-022 验收矩阵 40 项，全部 NOT_RUN。
- 新增 7680×4320 SVG 多方见证与分叉检测架构源图。
- 新增 8 项候选 ADR（ADR-123—ADR-130）；威胁矩阵扩展至 44 项。
- 候选约束：生态自治透明证据日志、Witness 单调 Checkpoint、原子持久化、2q-n>f Quorum 交集、运营/故障域独立性、Monitor 旁路 Gossip、Fork Evidence 固定与人类争议裁决。
- 研究参考：RFC 9162（Experimental）、RFC 9943（Proposed Standard）、C2SP Witness/Cosignature/Policy 社区规范、Sigsum 和 Trillian。
- 未部署 Witness 网络、透明日志或真实密钥；未运行 Quorum、分叉或 Gossip 故障注入。

## WP-022 阶段快照（历史记录）
- 合成实验与验收：156 项，全部 NOT_RUN。
- 架构决策：30 项，全部 Candidate，未获正式批准。
- 威胁与治理边界：44 项，全部 Candidate。
- 候选 JSON Schema：12 份，仅完成 JSON 语法检查；完整 Draft 2020-12 Validator、语义和密码学验证未执行。
- 架构源图：4 张 7680×4320 SVG。
- WP-021 10 项与 WP-022 12 项静态未决事项均未关闭。


## 工作流 F｜WP-023 可信见证网络治理、密钥生命周期与灾难恢复
- 新增 WP-023 架构备忘录、研究证据登记、静态审查与 15 项未决事项。
- 新增 Witness Lifecycle Event、Witness Key Lifecycle Record、Witness Recovery Snapshot Manifest、Trust Root Update Envelope 四份候选 JSON Schema（V1.9 总计十六份）。
- 新增 WP-023 验收矩阵 50 项，全部 NOT_RUN。
- 新增 7680×4320 SVG 可信见证网络治理与灾难恢复架构源图。
- 新增 10 项候选 ADR（ADR-131—ADR-140）；威胁矩阵扩展至 56 项。
- 候选约束：Witness 身份核验与 OBSERVE_ONLY、密钥用途隔离、Key Epoch 单调、正常根升级双阈值、紧急带外恢复锚、外部 Checkpoint 对账、Joint Quorum 和恢复失败隔离。
- 研究证据：TUF 1.0.37、Sigstore Security Model、NIST SP 800-57 Rev.6 IPD、C2SP Witness Protocol v1.1.0；规范状态与适用边界已登记。
- 未部署真实根密钥、Witness 密钥、HSM/KMS、备份系统或灾难恢复流程；未执行恢复演练。

## 总体边界（V1.9 当前权威汇总｜WP-023）
- 合成实验与验收：206 项，全部 NOT_RUN（22 + 31 + 27 + 36 + 40 + 50）。
- 架构决策：40 项（ADR-101—ADR-140），全部 Candidate，未获正式批准。
- 威胁与治理边界：56 项（TH-01—TH-56），全部 Candidate。
- 候选 JSON Schema：16 份；仅完成 JSON 语法解析，完整 Draft 2020-12 Validator、语义和密码学验证未执行。
- 架构源图：5 张 7680×4320 SVG。
- WP-021、WP-022、WP-023 静态未决事项合计 37 项，均未关闭。
- V1.8 F0 Gate：12 项全部 NotRun，F0 未通过。
- 生产实现未开始；未接入生产密钥、真实数据、HSM/KMS 或 Runner。
- productionAllowed=false；Runner 未启用。


## 工作流 G｜WP-024 形式化验证与韧性评估
- 新增 WP-024 架构备忘录、研究证据登记、TLA+ 模型变量与性质目录、实验设计和静态审查。
- 新增 3 份候选 Schema：故障场景、实验运行记录、实验结果证据包（V1.9 总计十九份）。
- 新增 WP-024 验收矩阵 60 项，全部 NOT_RUN。
- 新增 7680×4320 SVG 形式化验证与韧性评估架构源图。
- 新增 10 项候选 ADR（ADR-141—ADR-150）；威胁矩阵扩展至 66 项。
- 核心新约束：Witness Quorum 不等同于 BFT 共识；状态擦除恢复、身份克隆、签名前持久化和恢复防回滚必须独立建模。
- 参数网格：n=4/7/10/13；f=1/2/3/4；q=3/5/7/9；最小交集为 2/3/4/5。
- 研究证据：arXiv:2610.07759（2026-10-06 预印本）、C2SP Witness Protocol、PBFT、Proactive Recovery、FoundationDB Simulation、Jepsen、TLA+ TLC。
- 未运行 TLC、确定性模拟、分布式故障注入、密码学互操作或真实恢复演练。

## 总体边界（V1.9 当前权威汇总｜WP-024）
- 合成实验与验收：266 项，全部 NOT_RUN（22 + 31 + 27 + 36 + 40 + 50 + 60）。
- 架构决策：54 项（ADR-101—ADR-154），全部 Candidate，未获正式批准。
- 威胁与治理边界：70 项（TH-01—TH-70），全部 Candidate。
- 候选 JSON Schema：19 份；仅完成 JSON 语法解析，完整 Draft 2020-12 Validator、语义和密码学验证未执行。
- 架构源图：6 张 7680×4320 SVG。
- WP-021、WP-022、WP-023、WP-024 静态未决事项合计 53 项，均未关闭。
- V1.8 F0 Gate：12 项全部 NotRun，F0 未通过。
- 生产实现未开始；未接入生产密钥、真实数据、HSM/KMS 或 Runner。
- productionAllowed=false；Runner 未启用。


## 工作流 G 增补｜WP-024-L0/L1 Quorum 穷举与恢复状态模型验证
- L0 已实际穷举 n=4/7/10/13、q=2f+1 的全部不同 Quorum 集合对，共 262,611 对；四组最小交集均符合 2q-n=f+1。
- L1 Python BFS 有限状态参考模型：n=4、Byzantine={W1}、q=3；释放后持久化+重置 ACTIVE，探索 130,375 状态并找到 14 步反例；释放前持久化+回滚后仍 ACTIVE，探索 149,546 状态并找到 14 步反例。
- 释放前持久化+恢复隔离，探索 67,500 状态未发现有界反例；释放前持久化+保留单调状态，探索 43,904 状态未发现有界反例。
- 新增可执行 TLA+ 源文件及三份 TLC 配置；TLC 尚未运行。Python BFS 结果不冒充 TLC 结果。
- 新增 L0/L1 报告、Python 参考检查器、Quorum 穷举 CSV、恢复模型 JSON 和反例轨迹。
- 新增 ADR-151—ADR-154；威胁矩阵扩展至 TH-70；WP-024 静态未决事项扩展至 16 项。
- 关键结论：签名前持久化仍不足以抵御可回滚存储；恢复无法证明防双签状态连续性时，必须隔离原身份。

