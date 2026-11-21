# Agent Ecology｜CCF B 类论文研究计划与首篇论文设计

**版本：研究计划候选稿 0.1**  
**日期：2026-11-16**  
**学术目标：优先 CCF B 类，尽快形成可投稿的原创研究论文**  
**首选期刊：Autonomous Agents and Multi-Agent Systems（AAMAS，CCF B，人工智能）**  
**研究状态：计划与形式化设计阶段；尚未完成首篇论文实验，不代表已投稿或已发表。**

---

## 1. 研究计划总目标

本研究计划以 Agent Ecology（智能体生态）为统一研究对象，完整覆盖五个相互关联的研究方向：

1. **理论：** 自治智能体、共享环境、协作痕迹、持久工件、局部反应规则与生态级行为之间的关系。
2. **架构：** 五平面 Agent Environment、Stigmergy 优先协作、A2A 选择性直连、Ontology 语义约束和 Environment Runtime。
3. **治理：** 主体身份、Owner 权威、动态授权、风险门禁、独立验证、人类治理外环和可审计执行。
4. **进化：** 局部策略学习、生态知识积累、RSI 候选生成、Shadow、独立评估、审批与回滚。
5. **联邦生态：** 多生态自治、跨域能力发现、双边信任、动态联盟、资源公平和跨生态共同进化。

总目标不是将所有已有设计直接写入一篇论文，而是建立可验证的理论框架，选择一项具有清晰新颖性和实验可行性的核心问题，形成首篇高质量论文；其余方向按独立研究问题和证据成熟度逐步形成后续成果。

## 2. 首篇论文正式定位

### 2.1 暂定题目

**英文：** Governed Stigmergic Coordination for Agent Ecosystems: A Five-Plane Environment Model and Empirical Evaluation

**中文：** 面向智能体生态的治理型痕迹协作：五平面环境模型与实证评估

### 2.2 论文类型与目标

- 类型：原创研究论文（Regular / Original Research Paper）。
- 首选：Autonomous Agents and Multi-Agent Systems（AAMAS）期刊常规投稿。
- 目标类别：依据 CCF 2026 第七版目录，AAMAS 会议和 AAMAS 期刊均列于人工智能 B 类。
- 会议路线：AAMAS 2027 主会论文截止日期为 2026-10-08，当前已过；不得将已关闭的主会投稿窗口当作可用计划。AAAI Fast Track 仅适用于满足其先前 AAAI 投稿和评审条件的论文，不作为默认路径。
- 不以赶截稿为理由降低理论、实验、复现和独立审查标准。

CCF 目录是推荐目录，不应被解释为对单篇论文质量或机构评价结果的保证。投稿前应再次核验期刊目录、投稿指南和具体征稿状态。

### 2.3 核心研究主张

传统多智能体系统常以主体间消息、中心化编排或共享黑板组织协作。Agent Ecology 研究一种治理型环境协作模式：智能体通过持久、类型化、可追溯且受权限约束的共享环境状态、痕迹和工件间接协调；环境运行时负责有界发现、语义校验、来源验证、授权检查和权威状态提交；直接 A2A 通信只在明确的协商、委派和同步条件下补充使用。

论文需要证明的不是“共享环境一定优于消息通信”，而是：

**在任务具有可复用中间成果、主体动态变化或跨域协作需求时，具有明确状态权威、来源谱系、有界发现和本地治理门禁的痕迹协作，能否在相同资源预算下改善协作质量、持续性和治理安全；并明确其不适用或收益不足的任务边界。**

## 3. 研究缺口与新颖性边界

### 3.1 必须承认的已有研究

以下研究已覆盖部分相邻问题，不能将其贡献重新包装为本研究的首创：

- 经典 Stigmergy 与多智能体环境协调研究，已讨论通过环境修改实现间接协调。
- Blackboard Multi-Agent Systems（2025）已将共享黑板用于 LLM 多智能体信息发现。
- ScaleMAS（2026）已研究 substrate-centric coordination、持久共享数据底座、有界检索和 Agent 退出后的信息保留。
- SwarmWorld（2026）已研究 LLM Agent 通过环境痕迹、持久工件和可继承成果形成群体演化。
- 共享记忆的受控研究已表明，跨主体共享状态可能形成隐式通信通道；访问、行为影响与主动通信意图必须区分。
- 2026 年多智能体系统综述已提出 Agent 五模块架构和多维评价框架。因此不能笼统宣称“首次提出统一多智能体架构”。

### 3.2 本研究拟建立的差异

| 相关研究侧重 | Agent Ecology 拟研究的增量 |
|---|---|
| 共享黑板或共享记忆 | 将共享环境拆分为五个具有不同权威、语义、一致性和访问约束的平面 |
| 共享状态促进协作 | 区分 State、Trace、Intent、Command、Event、Artifact 和 Evidence，防止语义混淆 |
| Agent 通过共享数据发现任务 | 有界发现、来源感知排序、Owner 权威校验和访问审计一体化 |
| 工件持久化 | 工件生命周期与 Agent 生命周期分离，并验证生产者退出后的接续能力 |
| 多 Agent 协作性能 | 同预算单 Agent、A2A、共享黑板、基础 Stigmergy 和治理型环境的对照评估 |
| Agent 自治或联邦协作 | 发现、信任、授权和执行分离；接收生态保留本地 Owner/PDP/PEP 最终授权权 |

### 3.3 可主张与不可主张

可主张的候选贡献：
- 一种面向自治和联邦生态的治理型痕迹协作形式化模型；
- 一种五平面环境架构及类型化状态转换规则；
- 一套将任务表现、协作成本、主体退出韧性和治理安全联合评价的实验设计；
- 在明确任务、模型、预算和威胁条件下得到的实证结果。

在证据出现之前，不得主张：
- 首次提出 Stigmergy、共享黑板或环境中心协作；
- 已证明 Agent Ecology 在所有任务上优于单 Agent 或 A2A；
- 已完成真实双生态互操作、生产部署或生产安全验证；
- 已完成 321 项正式验收或 68 项 ADR 的批准。

## 4. 理论模型：Governed Agent Ecology

### 4.1 系统定义

将一个 Agent Ecology 表示为：

\[
\mathcal{AE} =
\langle \mathcal{A}, \mathcal{O}, \mathcal{E},
\mathcal{P}, \mathcal{L}, \mathcal{F} \rangle
\]

其中：

- \(\mathcal{A}\)：自治 Agent 集合，包含身份、能力、生命周期和局部策略。
- \(\mathcal{O}\)：权威 Owner 集合，分别拥有其领域状态、数据、资源和授权边界。
- \(\mathcal{E}\)：共享环境，包含 State、Trace、Artifact、Semantic、Governance 五个逻辑平面。
- \(\mathcal{P}\)：身份、用途、访问、执行、风险和审批策略。
- \(\mathcal{L}\)：局部反应规则，依据授权局部视图提出有限动作。
- \(\mathcal{F}\)：跨生态关系，包括能力发现、双边信任、证据交换、动态联盟和本地采用规则。

### 4.2 五平面环境

| 平面 | 状态对象 | 权威与约束 |
|---|---|---|
| State 状态平面 | 经 Owner 接受的事实、任务状态和资源状态 | 仅由相应 Owner/Runtime 接受的命令改变权威状态 |
| Trace 痕迹平面 | 观察、变化、协作信号、因果引用和来源记录 | 不能把意图伪装成事实；保留追加式来源与审计 |
| Artifact 工件平面 | 中间结果、证据包、方案、代码、知识和版本 | 持久化、可验证、可追溯；执行前必须经过独立安全门禁 |
| Semantic 语义平面 | Ontology、Schema、类型映射和检索索引 | 版本化、兼容审查、权限过滤；语义相似不等于授权 |
| Governance 治理平面 | 身份、Owner、授权、用途、风险、撤销和审计 | PDP/PEP 与人类治理保留最终决策权 |

五平面是逻辑职责划分，不预设必须部署为五套独立服务，也不将其与微服务数量等同。

### 4.3 局部观察与受控提交

Agent \(i\) 在时刻 \(t\) 的观察视图：

\[
o_i^t =
\operatorname{Filter}
(\mathcal{E}_t, scope_i, k_i, B_i, \tau_i, P_i)
\]

其中 scope 为授权范围，\(k_i\) 为结果条数上限，\(B_i\) 为字节/Token 预算，\(\tau_i\) 为新鲜度约束，\(P_i\) 为访问策略。

Agent 根据局部视图提出动作：

\[
u_i^t = \pi_i(o_i^t, goal_i)
\]

动作只有经过语义校验、身份验证、Owner 授权、风险门禁和必要的人类审批，才可进入权威提交：

\[
\mathcal{E}_{t+1} =
\operatorname{Commit}_{Owner,PDP,PEP}
(\mathcal{E}_t,u_i^t)
\]

若验证失败，则返回 DENY 或 HOLD，不产生权威状态变化；拒绝原因和必要证据进入可审计痕迹。

### 4.4 Stigmergy 与 A2A 的分工

- Stigmergy：默认持久协调机制。一个主体对环境的合法修改，会改变其他主体后续可见的授权状态、痕迹和工件。
- A2A：在协商、委派、澄清、交接和同步确认等需要明确主体间交互的场景使用。
- MCP：承担 Agent 到工具/资源服务的垂直接入，不等同于 Agent 间协作。
- 共享环境不能退化为所有 Agent 可读取的全局聊天记录或无限制广播。

### 4.5 关键不变量

1. **权威性：** Agent 提案不直接等于权威状态；权威变更必须经过 Owner/Runtime 提交。
2. **授权安全：** 每次受保护读取、写入和副作用动作均需通过当前有效授权。
3. **意图/事实分离：** Intent、Command、Event、State、Artifact、Evidence 不能互相冒充。
4. **有界观察：** 每次检索受权限、数量、字节、Token 和新鲜度上限约束。
5. **来源闭包：** 被接受的 Trace/Artifact 必须具有来源、版本、验证状态和必要的因果链。
6. **工件持续性：** Agent 退出不自动删除已提交且仍允许保留的工件；新 Agent 不继承旧 Agent 凭证。
7. **跨域权力不放大：** 来源生态的批准不替代接收生态批准；委托权限不得超过父授权。
8. **执行与验证分离：** 关键成果不能由执行主体自行签发独立可信证明。
9. **进化受控：** 局部学习和 RSI 只能生成候选，经隔离实验、Shadow、独立评估、人类审批和回滚门禁后申请采用。

## 5. 研究问题与可证伪假设

### RQ1：协作质量与资源效率

在任务、模型、工具和总推理预算匹配时，治理型痕迹协作相较于单 Agent、A2A 直接通信和共享黑板，是否改善任务成果质量、重复劳动和协作成本？

- H1a：对于存在中间成果复用和多源证据整合的任务，持久工件与有界发现能降低重复劳动。
- H1b：对于强顺序依赖、低并行性或无需共享中间成果的任务，多 Agent 可能不优于单 Agent。
- H1c：选择性 A2A 可能改善必须明确协商的任务，但不应成为所有协作步骤的默认通道。

### RQ2：持久性与动态主体韧性

当 Agent 退出、失联、替换或重新加入时，持久工件、来源谱系和状态续读能否提高任务接续成功率并降低恢复成本？

- H2a：工件生命周期与 Agent 生命周期分离，可提高生产者退出后的成果可用性。
- H2b：仅保留共享消息而缺乏来源、版本和依赖关系，不能保证成果可安全接续。

### RQ3：治理安全与污染抵抗

在过期痕迹、恶意痕迹、重放、Sybil/串谋、越权读取和跨域授权缺失条件下，治理型环境是否能保持关键安全不变量？

- H3a：来源感知验证、撤销检查和本地 PDP/PEP 能降低错误或过期痕迹被用于高风险动作的概率。
- H3b：A2A 消息、Agent 口头确认或联盟 Charter 均不能替代 Owner 的有效授权。
- H3c：安全不变量必须独立评价，不能被任务成功率或平均成本抵消。

### RQ4：局部进化与联邦自治（首篇论文的扩展研究）

局部反应规则、RSI Shadow 和动态联盟能否提升生态适应性，同时保持权限不放大、Owner 主权不转移和独立验证？

该问题进入后续论文或首篇论文的扩展实验，不在缺少实验数据时作为首篇论文已证明的结论。

## 6. 对照实验设计

### 6.1 对照组

| 组别 | 方法 | 作用 |
|---|---|---|
| B0 | 强单 Agent | 参考性能与成本基线 |
| B1 | A2A 直接消息协作 | 测量显式消息通信的收益和开销 |
| B2 | 全局共享黑板 | 测量共享上下文增长与读取负担 |
| B3 | 基础 Stigmergy / 有界共享底座 | 测量环境痕迹与持久工件的作用 |
| B4 | Stigmergy + 选择性 A2A | 测量混合协作的边际收益 |
| B5 | 完整五平面治理型 Agent Ecology | 测量语义、来源、授权、审计与环境提交机制的联合效果 |

B5 是首篇论文的候选方法组；若研究原型无法实现其中某一机制，必须缩小论文主张，不得用架构图代替实验实现。

### 6.2 首批合成任务

- T1 多源证据整合：验证跨主体证据发现、工件复用和来源谱系。
- T2 生产者退出与任务接续：验证 Agent 退出后成果持久性及后继主体恢复。
- T3 资源冲突与任务承诺：验证共享状态冲突、重复工作和 Owner 裁决。
- T4 过期/恶意痕迹注入：验证来源校验、隔离、撤销和高风险 HOLD。
- T5 跨生态能力发现：验证能力目录发现与目标域本地授权分离。

所有数据均使用合成数据，不接入真实个人、企业或生产业务数据。

### 6.3 消融实验

在 B5 上分别移除以下机制，测量单项机制的贡献：

- A1 移除来源谱系与来源感知排序；
- A2 移除 top-k、字节/Token 上限；
- A3 移除本地 Owner 授权门禁（只在隔离仿真中进行负向安全测试）；
- A4 将持久工件改为临时消息；
- A5 移除语义类型区分；
- A6 移除选择性 A2A 触发条件。

消融实验不允许在真实生产系统中移除安全门禁。

### 6.4 控制变量与复现纪律

- 固定模型版本、模型端点、温度、最大输出、系统提示、工具 Schema、解析器和运行时版本。
- 所有组使用同一任务集、初始环境快照、工具集合和总推理预算。
- 预先登记随机种子、实验单元、排除规则、停止规则和统计方法。
- 每次运行生成 Run Manifest、输入/输出哈希、事件日志、失败记录、模型调用统计和分析脚本。
- 至少使用多个任务类别和模型配置；具体数量通过先导实验与统计功效分析确定，不事先编造样本量。
- 保留负向结果和不适用任务；不得只选择有利任务报告。
- 研究原型应独立于生产主线；不启用 Runner、不连接真实业务数据、不自动修改生产代码。

## 7. 指标与统计分析

### 7.1 任务与成果质量

- Task Success Rate：任务成功率。
- Accepted Artifact Rate：被独立验收的成果比例。
- Evidence Completeness：证据来源和因果链完整度。
- Error Propagation：错误痕迹被后续主体采用并传播的程度。

### 7.2 效率与成本

- Total Inference Tokens：总推理 Token。
- Cost per Accepted Result：每个被验收成果的成本。
- End-to-end Latency：端到端时延。
- Duplicate Work Rate：重复劳动率。
- Read Burden：每个 Agent 的读取条数、字节和 Token。
- Coordination Overhead：协作协议、检索、状态同步和协调所占资源。

### 7.3 韧性与持续性

- Agent Churn Recovery：Agent 退出后的恢复成功率。
- Artifact Survival：生产者退出后的工件可用性。
- Recovery Latency：任务接续所需时间。
- Stale Trace Ratio：过期痕迹占比。
- Conflict Resolution Rate：冲突被正确识别并由权威主体处理的比例。

### 7.4 治理与安全

- Unauthorized Read/Write：越权读取/写入次数，关键安全目标为 0。
- Unauthorized Side Effect：未授权副作用次数，关键安全目标为 0。
- Revocation Enforcement Latency：撤销生效延迟。
- Provenance Completeness：来源完整率。
- Independent Verification Rate：关键成果独立验证比例。
- False HOLD / False DENY：误拦截率，需与安全漏放分开统计。

### 7.5 统计方法

- 以任务实例和随机种子配对比较各组。
- 报告均值/中位数、方差或分布、95% 置信区间、效应量和样本数。
- 对多组比较采用适当的多重比较校正。
- 根据数据分布选择配对检验、非参数检验或混合效应模型。
- 先导实验后开展统计功效分析，再冻结正式样本规模。
- 预先定义主指标、次指标和 P0 安全失败判定；禁止用综合平均分掩盖单项安全违规。

## 8. 论文结构建议

1. Introduction：研究背景、问题、贡献和适用边界。
2. Related Work：Stigmergy、Blackboard、Shared Memory、Substrate-centric MAS、Agent Environment、Governed/Federated MAS。
3. Problem Formulation：Agent Ecology 定义、系统假设和威胁模型。
4. Governed Five-Plane Environment：五平面模型、权威边界、类型化状态转换和局部观察。
5. Coordination Protocol：Stigmergy 主通道、选择性 A2A、工件谱系和本地授权。
6. Experimental Methodology：任务集、基线、变量、预算控制和复现协议。
7. Results：任务质量、成本、韧性、安全和消融结果。
8. Discussion：收益条件、失败场景、生态自治与扩展性。
9. Limitations and Threats to Validity：模型偏差、任务覆盖、外部效度和仿真边界。
10. Conclusion：理论和工程启示。

建议主文优先呈现核心模型、关键不变量、实验方法和主要结果；完整 Schema、扩展威胁矩阵、运行清单和附加轨迹放入可复现补充材料。

## 9. 论文系列规划

为保持研究完整性，同时避免一篇论文过度膨胀或重复切片，规划为三个可独立验证的研究主题：

### Paper 1｜治理型痕迹协作与五平面环境（首篇）

- 核心：理论模型、五平面环境、治理型 Stigmergy、同预算对照实验。
- 重点：协作收益、持久工件、主体退出接续、痕迹污染和本地授权。
- 目标：AAMAS 期刊常规原创研究论文（CCF B）。

### Paper 2｜联邦可信协作与形式化韧性验证

- 核心：双边信任、能力发现与执行授权分离、撤销传播、Witness、Quorum、状态擦除恢复。
- 重点：形式化性质、TLA+ 模型检查、确定性模拟、故障注入和独立 Checker。
- 发表前提：完成真实可运行的模型检查和独立复核；当前 262,611 组 Quorum 穷举与 Python BFS 只作为有界预验证，不替代 TLC 或分布式系统实测。

### Paper 3｜动态联盟、生态经济与受控进化

- 核心：联盟形成、Owner 自治、资源公平、贡献归因、局部策略进化和 RSI 治理。
- 重点：联盟相对单 Agent 的边际价值、权限边界、独立验收和 Shadow 进化。
- 发表前提：形成独立研究问题、独立实验和足够的新证据，不将 Paper 1 的同一组结果简单拆分重投。

## 10. 研究阶段计划与质量门禁

| 阶段 | 目标交付 | 通过条件 |
|---|---|---|
| P0 研究冻结 | 问题定义、标题、主张、相关工作矩阵 | 与现有工作差异明确；不宣称未证实的新颖性 |
| P1 理论形式化 | 定义、状态转换、威胁模型、不变量 | 关键对象和边界无语义冲突 |
| P2 实验协议 | 任务集、B0—B5、消融、指标、统计方案 | 预算匹配、随机种子和排除规则预注册 |
| P3 研究原型 | 独立合成环境、可重复运行脚本、Run Manifest | 不连接生产数据；运行可重复 |
| P4 正式实验 | 多任务、多配置、失败与负向结果 | 结果完整、统计方法正确 |
| P5 独立复核 | 独立 Checker、复现实验、威胁审查 | 关键结果可复现；P0 安全违规为零 |
| P6 论文写作 | 完整英文论文、附录、复现包 | 每项主张都有直接证据 |
| P7 投稿 | 目标期刊格式、投稿信息表、伦理和披露 | 完成作者确认、版权和投稿政策核验 |

**时间安排（研究目标，不是发表承诺）：**
- 第 1—2 周：P0、P1、相关工作和预注册。
- 第 3—4 周：P2、合成任务与研究原型。
- 第 5—6 周：P3、P4 先导和正式实验。
- 第 7 周：P5 独立复核与统计分析。
- 第 8 周：P6 英文论文和内部审稿。
- 之后根据实验缺口决定是否进入 P7；若核心结果未通过，不以时间为由强行投稿。

## 11. 期刊要求与合规事项

### 11.1 AAMAS 期刊

- 期刊范围覆盖多智能体协作、自组织、环境、Ontology、信任与信誉、Agent 学习和系统验证。
- 常规投稿类型包括 Original Research / Regular Paper。
- 每篇常规投稿需附 1—2 页 Information Sheet，明确主张、证据、最相关工作和与既有发表成果的差异。
- 若使用 AI 工具参与假设或方法设计，应按期刊要求在 Methods 或合适位置说明；人类作者对最终稿、数据、引用和结论承担责任。
- 需提供可编辑源文件、完整参考文献、数据可用性说明和作者贡献等投稿材料。

### 11.2 AI 辅助研究披露

AI 工具不能列为论文作者。若 AI 工具参与提出研究假设、方法设计或实验设计，应根据目标期刊/会议的具体政策披露工具及版本、使用方式和必要提示信息。最终研究决策、实验执行、数据分析、引用核查和论文责任必须由人类作者承担。

### 11.3 双盲与重复投稿

- 会议投稿须遵循对应年份双盲政策和 AI 辅助技术政策。
- 不得将实质相同的论文同时投向多个存档发表渠道。
- 期刊扩展会议论文时必须明确新增理论、证明、实验和讨论内容。
- 不得通过把同一实验拆成多篇高度重叠论文来追求发表数量。

## 12. 当前证据状态与明确限制

截至 2026-11-16：

- Agent Ecology V1.2—V1.9 已形成研究资料链；V1.9 的 321 项验收设计仍全部 NOT_RUN。
- 68 项 ADR 均为 Candidate，94 项威胁均为 Candidate。
- 21 份候选 JSON Schema 仅完成 JSON 语法解析；完整 Draft 2020-12 验证、语义、密码学和互操作测试未完成。
- WP-024-L0 已完成 262,611 组 Quorum 集合对穷举；WP-024-L1 Python BFS 对危险恢复配置发现 14 步反例；TLC 尚未运行。
- V1.8 F0 的 12 项 Gate 仍全部 NotRun；F0 未通过。
- 没有真实双生态生产验证、真实业务数据授权、生产密钥接入或生产写权限。
- productionAllowed=false；Runner 未启用。
- 研究计划、架构设计、静态审查和有限状态预验证均不能冒充完整实验或生产验证。

## 13. 首轮立即执行事项

1. 冻结 Paper 1 的题目、核心主张和 RQ1—RQ3。
2. 建立 Related Work 对照矩阵，逐项比较 Stigmergy、Blackboard、ScaleMAS、SwarmWorld、共享记忆研究和 2026 多智能体综述。
3. 将五平面模型转化为正式定义、状态转换规则和可检查不变量。
4. 从现有 STG/ECO 验收矩阵中选取与 Paper 1 直接相关的实验子集，形成独立论文实验协议。
5. 完成先导实验和统计功效分析后，再冻结样本量与阈值。
6. 只有在实验结果、复现材料和独立复核达到门槛后，才形成可投稿稿件。

---

## 参考资料与官方入口

### CCF 与期刊
- CCF 第七版推荐目录（2026）：https://www.ccf.org.cn/Academic_Evaluation/By_category/
- CCF 人工智能方向目录：https://www.ccf.org.cn/Academic_Evaluation/AI/
- AAMAS 期刊主页：https://link.springer.com/journal/10458
- AAMAS 期刊 Aims and Scope：https://link.springer.com/journal/10458/aims-and-scope
- AAMAS 期刊 Submission Guidelines：https://link.springer.com/journal/10458/submission-guidelines

### 会议
- AAMAS 2027 Main Track：https://warwick.ac.uk/fac/sci/dcs/aamas2027/calls/call-for-main-track/
- AAMAS 2027 Submission Instructions：https://warwick.ac.uk/fac/sci/dcs/aamas2027/guidelines-and-policies/instructions/

### 直接相关研究
- Blackboard Multi-Agent Systems for Information Discovery in Data Science（2025）：https://research.google/pubs/blackboard-multi-agent-systems-for-information-discovery-in-data-science/
- LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science（2025）：https://arxiv.org/abs/2510.01285
- Scaling Multi-Agent Intelligence with Substrate-Centric Coordination（2026）：https://arxiv.org/abs/2610.16120
- SwarmWorld: Stigmergic Technological Evolution in Societies of Language-Model Agents（2026）：https://arxiv.org/abs/2608.26081
- Unprompted Coordination through Shared Memory in LLM Agents（2026）：https://arxiv.org/abs/2611.12412
- Capable Language Models Can Outgrow the Benefits of Collaboration（2026）：https://doi.org/10.1038/s42256-026-01268-y
- Autonomous Agents and Multi-Agent Systems: A Comprehensive Review（2026）：https://doi.org/10.1007/s10462-026-11731-2

**文档状态：** Candidate / Research Plan。本文是研究规划与实验设计，不包含虚构实验结果，不代表论文已完成、已投稿或已获得录用。
