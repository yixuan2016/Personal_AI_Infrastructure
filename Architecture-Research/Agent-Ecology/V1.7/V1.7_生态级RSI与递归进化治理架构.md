# Agent Ecology V1.7
## 生态级 RSI 与递归进化治理架构
**版本：V1.7 架构设计版｜日期：2026年11月10日｜范围：架构研究、进化治理、模型验证、数据契约与验收设计；不编写工程实现代码**

> V1.7 承接 V1.4 Environment Runtime、V1.5 Ecosystem Autonomy 和 V1.6 Ecosystem World Model。目标不是让系统无约束地修改自己，而是让 ADS 在人类定义的目标、授权和风险边界内，能够发现问题、提出改进、进行独立验证、分阶段采用并从真实结果中学习。任何模型、Agent 或 RSI 引擎都不得自行修改人类根策略、身份根信任、审批权或生产授权边界。

![V1.7 生态级 RSI 全景架构](assets/00_V1.7_生态级RSI全景架构_8k.png)

---

# 执行摘要

V1.6 让 Agent Ecology 能够建立生态状态模型、预测未来并在数字孪生中进行反事实推演。V1.7 进一步回答：当系统发现自身存在问题时，如何提出改进？如何证明改进真的有效？如何避免只优化测试分数？如何让下一轮改进继承已验证的经验，同时不让系统逐步扩大自身权限？

V1.7 的核心定义：**递归自我改进不是系统对自己说“我变得更好了”，而是一个受约束、可证伪、可追溯、可回滚的改进候选不断经过独立验证和治理授权的过程。**

本版本形成九个核心模块：
1. Ecosystem Observability：生态观测与证据采集；
2. Self-Diagnosis：问题诊断与根因假设；
3. Improvement Design：改进方案生成和差异化搜索；
4. Evolution Sandbox：隔离的候选改进环境；
5. Digital Twin Validation：调用 V1.6 世界模型进行情景和反事实验证；
6. Independent Evaluation：独立评估、隐藏测试和对抗验证；
7. Evolution Governance：风险分级、授权、审批和发布控制；
8. Progressive Adoption：Shadow、Canary、分阶段采用和回滚；
9. Recursive Learning：把真实结果转化为下一轮改进证据。

**关键边界：**
- Environment 仍是真实生态状态的唯一权威来源。
- World Model/Twin 只负责预测和模拟，不具有生产写入权。
- RSI 只能创建 `EvolutionProposal`，不能自行批准 `EvolutionRelease`。
- 评估器与改进生成器必须保持组织、数据和权限上的独立性。
- 人类治理外环拥有根策略、身份根信任、审批门槛、预算上限、否决、接管和最终问责权。
- 任何自我改进都必须有固定基线、隐藏留出集、回归测试、版本签名、变更差异和回滚路径。

---

# 94. V1.7 目标、范围与 RSI 定义

## 94.1 目标

- 将生态运行证据转化为可追溯的问题假设，而不是让 Agent 凭主观反思决定改造方向。
- 建立统一的改进对象模型，支持从记忆、技能、提示词、工作流、工具路由、Agent 拓扑到受限代码的分级演进。
- 建立候选版本隔离环境，保证候选变化不会直接影响生产 Environment。
- 复用 V1.6 Digital Twin 对候选策略做回放、仿真、反事实和压力测试。
- 让评估器独立于改进生成器，并通过隐藏测试、交叉评估和元评估降低自我确认偏差。
- 将质量、成本、可靠性、安全、公平、韧性、可维护性和可逆性纳入多目标评价。
- 形成风险分级的 Shadow、审批、Canary、有限发布、监控和回滚流程。
- 支持 ADS、领域生态和个人助理各自成长，同时通过授权证据交换可复用改进。

## 94.2 RSI 的工作定义

RSI（Recursive Self-Improvement）是一个迭代过程：系统基于自身历史运行证据提出改进候选；候选在独立环境中被验证；只有满足预先定义的证据、风险和治理条件才可能被采用；被采用的版本成为下一轮改进的对象。递归不意味着无限自修改，也不意味着每轮必须改变模型权重或源代码。

## 94.3 必须区分的四类活动

| 活动 | 定义 | 是否属于完整 RSI |
|---|---|---|
| Self-Refinement | 在单次任务内修订答案、计划或输出 | 否，属于局部自校正 |
| Continual Adaptation | 从经验更新记忆、技能、策略或配置 | 不一定，取决于是否有可验证的跨任务改进闭环 |
| Agent/Workflow Evolution | 修改工具、工作流、角色分工、路由和协作拓扑 | 可以构成 RSI 的一层 |
| Recursive Self-Improvement | 改进机制本身也进入下一轮被改进对象，并由独立评估证明净收益 | 是，完整 RSI 的关键特征 |

## 94.4 非目标

- 不追求“完全无人监管”的自我进化。
- 不把模型自评、自我奖励或内部打分当作独立证据。
- 不允许 Agent 自行改变根策略、身份根信任、生产凭证和审批规则。
- 不将一次基准提升直接等同于真实生态长期收益。
- 不把无限搜索、无限递归或无限算力视为默认能力。
- 不将跨领域知识共享等同于共享所有原始数据和私有上下文。
- 不在本版本进入生产代码自动改写和自动部署；只定义受治理架构与验收边界。

---

# 95. RSI 进化层级与修改对象分级

![V1.7 RSI 进化层级与修改对象](assets/26_V1.7_RSI进化层级与修改对象_8k.png)

## 95.1 六级进化层级

| 层级 | 名称 | 改进对象 | 典型例子 | 证据要求 |
|---|---|---|---|---|
| R0 | Task Self-Refinement | 单次任务输出 | 计划修订、结果纠错 | 任务验收 |
| R1 | Experience Evolution | 记忆、技能、经验 | 保存已验证技能、替换过期知识 | 跨任务留出评估 |
| R2 | Harness Evolution | 提示词、工具描述、工作流、路由 | 优化工具选择与任务分解 | 固定基线、回归集、Shadow |
| R3 | Agent Architecture Evolution | Agent 角色、联盟拓扑、能力组合 | 调整专家 Agent 和交接关系 | 数字孪生、对抗与领域验证 |
| R4 | Improvement-Process Evolution | 诊断器、生成器、评估器流程 | 改进假设生成、搜索和评估方法 | 元评估、隐藏测试、独立审查 |
| R5 | Ecosystem-Level Co-Evolution | 跨领域公共能力和生态协调策略 | ADS 与多个领域的协同演进 | 多域验证、人类治理、有限发布 |

R0–R3 主要改进被优化对象；R4 开始改进“如何改进”；R5 则涉及多个领域主体的共同演化。R5 不意味着 ADS 可以接管领域内部的专业决策。

## 95.2 修改对象风险分级

| 变更类别 | 示例 | 初始风险 | 默认治理要求 |
|---|---|---|---|
| C0 内容级 | 单次输出、草稿、临时计划 | 低 | 任务验收 |
| C1 经验级 | 记忆、知识条目、技能候选 | 低—中 | 来源、时效、跨任务留出测试 |
| C2 Harness 级 | Prompt、工具描述、工作流、路由配置 | 中 | 版本化、回归、Shadow、回滚 |
| C3 结构级 | Agent 角色、联盟拓扑、能力契约 | 中—高 | Twin、领域 Owner 评审、Canary |
| C4 执行机制级 | 规划器、调度器、诊断器、评估器实现 | 高 | 独立评估、红队、审批、受限发布 |
| C5 权限根级 | 根策略、身份信任根、审批规则、生产凭证 | 禁止自改 | 仅人类治理主体可发起和批准 |

**重要：风险等级由影响范围、可逆性、数据敏感度、外部副作用和权限影响共同决定，不由变更对象名称单独决定。** C5 是禁止 RSI 自主修改的治理边界。

---

# 96. 总体架构：Ecosystem Recursive Evolution Architecture

![V1.7 递归进化双闭环架构](assets/27_V1.7_递归进化双闭环架构_8k.png)

## 96.1 九个逻辑模块

| 模块 | 主要责任 | 不拥有的权限 |
|---|---|---|
| Observability & Evidence | 收集运行指标、Trace、失败案例、反馈和证据 | 不直接改写生产策略 |
| Diagnosis Engine | 聚类异常、提出根因假设、识别瓶颈 | 不自行确认根因 |
| Improvement Designer | 生成候选变更、差异和预期收益 | 不批准候选 |
| Evolution Sandbox | 运行候选版本、隔离资源和工具 | 不持有生产凭证 |
| Twin Validation | 回放、仿真、反事实和压力测试 | 不修改真实状态 |
| Independent Evaluator | 独立评估、隐藏测试、对抗检查 | 不接受生成器覆盖评分 |
| Governance Engine | 风险分级、策略检查、审批路由 | 不替代人类根策略权威 |
| Progressive Release | Shadow、Canary、发布和回滚 | 不越过审批门槛 |
| Recursive Learning | 汇总采用结果、失败与漂移，更新候选知识 | 不将未验证经验升级为事实 |

## 96.2 两个闭环

**A. 智能体内环——进化执行闭环**

`Observe → Diagnose → Hypothesize → Design → Sandbox → Simulate → Evaluate → Learn`

负责发现问题、提出方案、实验验证和形成下一轮候选。

**B. 人类外环——风险治理闭环**

`Scope → Authorize → Review → Approve/Deny → Release Gate → Monitor → Revoke/Rollback`

负责限定目标、风险、预算、数据范围、授权期限和发布条件，保留否决、接管与问责权。

两个闭环通过 `EvolutionProposal`、`EvaluationEvidence`、`ApprovalRecord` 和 `ReleaseRecord` 交换结构化证据，不通过 Agent 私聊来替代治理契约。

## 96.3 不把逻辑模块直接等同于微服务

V1.7 初期采用模块化架构：状态、证据、模型和治理边界先清晰，执行部署可以共置。只有当负载隔离、权限隔离、独立伸缩、团队所有权或故障域要求成立时，才渐进拆分服务。RSI 不能为了“架构看起来先进”而自动增加微服务数量。

---

# 97. 改进发现与诊断引擎

## 97.1 诊断信号

- Outcome Gap：任务目标与真实验收之间的差距；
- Repeated Failure：重复失败模式与重试风暴；
- Resource Inefficiency：单位质量成本、资源空转与排队；
- Coordination Friction：Agent 交接、重复工作和状态冲突；
- Trust/Quality Drift：能力信誉、校准和质量随时间变化；
- Governance Friction：审批延迟、误授权、过度阻断和审计缺口；
- Knowledge Debt：过期知识、冲突知识、未验证经验堆积；
- Resilience Gap：故障扩散、单点依赖和恢复时间上升。

## 97.2 根因假设不是事实

诊断器输出 `Hypothesis`，必须包括：支持证据、反证、数据缺口、可能混杂因素、置信区间或可信度说明、建议实验。诊断器不能仅凭一个相关性指标认定根因，也不能把用户偏好、领域规则或安全约束误判为低效率。

## 97.3 问题优先级

建议使用多维排序而非单一分数：
- 影响范围；
- 发生频率；
- 任务关键程度；
- 风险严重性；
- 证据充分度；
- 可逆性；
- 预期改进价值；
- 试验成本。

高影响但证据不足的问题先进入观测和验证，不得直接变成生产变更。

---

# 98. 改进设计与候选搜索

## 98.1 Improvement Proposal 结构

每个候选至少包含：
- `proposal_id` 与父候选/基线版本；
- 目标问题、诊断假设和证据引用；
- 变更对象、完整差异、影响面和依赖；
- 预期收益及可能负面影响；
- 风险等级、数据范围、预算和有效期限；
- 评估计划、隐藏测试策略和停止条件；
- 回滚工件、回滚触发阈值和责任主体；
- 作者、模型、工具链、时间和签名。

## 98.2 多样化候选而非单一路径

- 生成多个结构不同的候选，不只微调参数；
- 保留当前最优候选和多个非支配候选；
- 保留失败案例和负面结果，避免重复探索；
- 对候选做依赖、冲突和组合兼容分析；
- 对高风险候选采用“最小差异”原则；
- 允许提出“不变更”作为基线选项。

## 98.3 改进搜索预算

每轮递归必须绑定：Token/算力预算、仿真预算、真实试验预算、时间上限、最大候选数、最大递归深度、失败重试次数和停止条件。预算耗尽时保留最优已验证版本，不得无限继续。

---

# 99. 独立评估与反自我欺骗机制

![V1.7 独立评估与反自我欺骗机制](assets/28_V1.7_独立评估与反自我欺骗机制_8k.png)

## 99.1 评估器独立性

改进生成器不能同时控制：评估数据、隐藏测试、评分规则、阈值、审批人和发布权限。评估器必须在身份、工具权限、数据访问、版本和责任链上与生成器分离。

## 99.2 证据层级

1. E0 自我声明或语言模型自评；
2. E1 同一模型/同一数据上的自测；
3. E2 固定基准与自动回归；
4. E3 隐藏留出集和独立评估器；
5. E4 数字孪生、对抗测试和历史回放；
6. E5 Shadow 真实流量对照；
7. E6 有限生产试点与独立验收。

不同用途需要不同证据门槛。E0/E1 只能用于形成候选，不能作为高风险发布证据。

## 99.3 多目标评估

- Quality：任务正确性与领域验收；
- Reliability：成功率、波动和故障恢复；
- Cost：Token、算力、外部 API 和人工成本；
- Latency：端到端时延和尾延迟；
- Safety：越权、数据泄露、工具滥用和不安全输出；
- Fairness：任务机会、资源分配和领域影响；
- Resilience：故障下的降级、隔离和恢复；
- Maintainability：复杂度、可解释性和运维负担；
- Reversibility：回滚速度、数据兼容和副作用可逆性。

安全、合规、授权和数据边界属于硬约束，不能用更高任务得分抵消。

## 99.4 反 Goodhart / Reward Hacking

- 隐藏测试集和随机留出集；
- 训练/选择/最终评估数据严格分离；
- 不同模型和不同评估器交叉复核；
- 元评估：检查评估器是否真的区分好坏候选；
- 对抗性测试与反例搜索；
- 指标之外的真实用户/领域验收；
- 长期回归与遗忘测试；
- 对基准过拟合、奖励投机和评估污染设置告警。

## 99.5 递归稳定性监测

每一轮都要观察：候选质量是否提升、方差是否增大、错误是否累积、能力是否遗忘、Agent 多样性是否下降、成本是否失控、评估器是否被优化器操纵、领域目标是否被公共目标挤压。连续多轮无净收益、评估分歧异常或安全指标恶化时，暂停递归。

---

# 100. 进化沙箱与数字孪生验证

## 100.1 沙箱隔离原则

- 候选代码/配置在独立命名空间运行；
- 只使用合成数据、脱敏数据或明确授权的快照；
- 生产凭证、根密钥和真实外部副作用接口不可见；
- 网络默认拒绝，仅开放明确的仿真服务；
- 资源、时长、并发和存储均有限额；
- 所有执行记录、文件差异、模型版本和随机种子均可追溯。

## 100.2 与 V1.6 世界模型的关系

V1.6 提供基线快照、模型版本、仿真分支和反事实结果；V1.7 将 `EvolutionProposal` 编译成候选干预，在孪生中运行对照组和实验组，分析收益分布、不确定性、敏感性和潜在副作用。V1.7 不重新建立一套 Twin，而是消费 V1.6 的能力与契约。

## 100.3 验证顺序

1. 静态差异和契约检查；
2. 单元/组件回归（如适用）；
3. 历史回放；
4. 数字孪生多情景仿真；
5. 隐藏留出集评估；
6. 对抗与故障注入；
7. Shadow 对照；
8. 人类审批；
9. 限定范围 Canary；
10. 独立验收与扩大/停止决策。

---

# 101. 发布治理：Shadow、Canary、Rollback

![V1.7 进化发布治理与回滚流程](assets/29_V1.7_进化发布治理与回滚流程_8k.png)

## 101.1 状态机

`DRAFT → PROPOSED → TRIAGED → SANDBOXED → SIMULATED → EVALUATED → SHADOW → REVIEW_PENDING → APPROVED → CANARY → LIMITED_RELEASE → MONITORED → ADOPTED`

异常状态：`REJECTED`、`QUARANTINED`、`PAUSED`、`ROLLED_BACK`、`EXPIRED`。

状态转换必须有角色权限、证据和事件记录；候选作者不能自行完成所有状态转换。

## 101.2 分级审批

| 风险 | 例子 | 最低审批要求 |
|---|---|---|
| L0 | 单次任务输出修正 | 任务验收 |
| L1 | 个人记忆/技能候选 | 数据Owner规则与用户可见控制 |
| L2 | 工作流、工具路由、提示词变化 | 独立评估 + Shadow + 责任Owner |
| L3 | Agent 拓扑、跨域资源策略 | 领域Owner + ADS治理 + 独立安全审查 |
| L4 | 规划器、执行器、评估器核心逻辑 | 人类审批 + 红队 + 限定Canary + 可回滚 |
| L5 | 根策略、身份根信任、生产授权根 | RSI 禁止发起自动变更；仅人类治理主体依法定/组织程序处理 |

## 101.3 回滚触发

- 质量显著下降或领域验收失败；
- 安全/隐私/授权事件；
- 模型漂移或不确定性超限；
- 成本、时延或资源预算超阈值；
- 公平性或领域影响恶化；
- 回滚工件不完整或数据迁移不兼容；
- 关键 Owner 撤销授权。

回滚必须包含版本恢复、状态/数据兼容、外部副作用核对、密钥/授权撤销、审计留存和事后复盘。

---

# 102. ADS、领域生态与个人助理的多层成长闭环

## 102.1 三类成长主体

| 主体 | 可进化对象 | 保留权力 |
|---|---|---|
| Personal Assistant | 个人记忆、偏好、技能、工具使用方式 | 用户对个人数据、主动联系和授权的控制 |
| Domain Ecology | 专业 Agent、领域技能、业务流程、领域策略候选 | 领域 Owner 的专业规则、数据权属和验收责任 |
| ADS Ecosystem Core | 公共协作契约、跨域调度模板、共享语义、通用评估方法 | 人类治理外环的根策略、跨域授权和否决权 |

## 102.2 跨域改进传播

ADS 可以发布 `ImprovementPattern`（经过验证的改进模式），领域主体可以：接受、适配、拒绝、延迟验证或提出反例。共享模式必须携带来源、版本、适用范围、证据等级、已知失败、数据要求和撤回机制。

**ADS 的 RSI 不会自动升级所有端口。** 领域端必须自行验证并确认采用。领域内部的专业知识和用户私有数据不因共享改进模式而自动出域。

## 102.3 共同进化中的防垄断

- 不让单一高信誉 Agent 长期垄断改进提案或评估角色；
- 保留多样化候选和少数派意见；
- 让新 Agent 有受限试验和证明能力的路径；
- 对跨域公共能力设置适用范围和版本兼容；
- 记录不同领域的收益/损失，不以 ADS 平均收益掩盖局部伤害。

---

# 103. 递归预算、停止条件与失效安全

## 103.1 每轮必须有预算

- 最大递归深度；
- 最大候选数量；
- 每个候选最大仿真次数；
- Token/GPU/CPU/外部 API 预算；
- 墙钟时间上限；
- 人工评审预算；
- 真实试验流量上限；
- 回滚和事故处置资源预留。

## 103.2 停止条件

- 达到预算或时间上限；
- 连续多轮没有超过最小有意义改进幅度；
- 安全、公平或稳定性指标恶化；
- 评估器可信度不足或测试被污染；
- 数据漂移、领域状态不完整或模型分布外；
- 候选差异不可解释、无法回滚或缺少责任主体；
- 人类治理主体发出暂停/撤权指令。

## 103.3 失效安全状态

当评估系统、世界模型、审批服务或审计链不可用时，默认不发布新版本；已批准的稳定版本继续运行，必要时降级到上一个已验证配置。不能因为治理服务故障而自动切换到“无人审批模式”。

---

# 104. 安全威胁与反操纵控制

| 威胁 | 失效表现 | 核心控制 |
|---|---|---|
| Evaluator Hacking | 生成器操纵评估器或测试 | 独立评估、隐藏集、元评估 |
| Reward Hacking | 优化代理指标而损害真实目标 | 多目标硬约束、真实验收 |
| Self-Confirming Loop | 生成器和评估器互相证明正确 | 角色隔离、外部证据、反例 |
| Diversity Collapse | 候选和 Agent 趋于单一策略 | 多样性约束、保留非支配候选 |
| Catastrophic Forgetting | 新版本破坏旧能力 | 长期回归、遗忘测试、回滚 |
| Model/Knowledge Poisoning | 错误经验被循环放大 | 来源证明、证据等级、隔离 |
| Permission Escalation | 自我改进扩大工具/数据权限 | 根策略不可变、Mandate衰减、PEP |
| Recursive Cost Explosion | 递归成本不断上升 | 预算上限、停止条件、成本告警 |
| Cross-Domain Leakage | 共享改进携带私有数据 | 最小投影、Owner授权、脱敏 |
| Supply-Chain Attack | 候选依赖或工件被替换 | 签名、哈希、SBOM/来源追溯 |
| Rollback Failure | 变更无法恢复或副作用重复 | 预先演练、补偿计划、状态核对 |
| Human Automation Bias | 审批人过度信任模型 | 显示分歧、限制、反证和替代方案 |

---

# 105. V1.7 机器可读数据契约与事件目录

## 105.1 核心数据对象

| 对象 | 关键字段 | 权威责任 |
|---|---|---|
| ImprovementProblem | problem_id、signals、hypotheses、evidence_refs、scope | Diagnosis Registry |
| EvolutionProposal | proposal_id、baseline_ref、change_set、risk_tier、budget、rollback_ref | Evolution Registry |
| CandidateArtifact | artifact_id、proposal_id、version、hash、signature、dependencies | Artifact Registry |
| ExperimentPlan | experiment_id、baseline、treatment、metrics、holdout_ref、stop_conditions | Experiment Registry |
| EvaluationEvidence | evidence_id、evaluator_id、dataset_ref、metrics、limitations、signature | Independent Evaluation |
| GovernanceDecision | decision_id、proposal_id、authority、decision、conditions、expiry | Governance Registry |
| ShadowObservation | shadow_id、candidate_version、traffic_scope、outcome_refs、drift | Shadow Monitor |
| ReleaseRecord | release_id、candidate_version、approval_ref、canary_scope、rollback_ref | Release Manager |
| RollbackRecord | rollback_id、release_id、trigger、restored_version、side_effect_check | Runtime/Governance |
| ImprovementPattern | pattern_id、source_domain、evidence_level、scope、limitations、adoption_status | ADS Knowledge Registry |

## 105.2 事件目录

- `evolution.problem.detected.v1`
- `evolution.hypothesis.proposed.v1`
- `evolution.proposal.created.v1`
- `evolution.candidate.generated.v1`
- `evolution.sandbox.started.v1`
- `evolution.sandbox.completed.v1`
- `evolution.experiment.started.v1`
- `evolution.experiment.completed.v1`
- `evolution.evaluation.completed.v1`
- `evolution.evaluation.disputed.v1`
- `evolution.governance.approved.v1`
- `evolution.governance.rejected.v1`
- `evolution.shadow.started.v1`
- `evolution.shadow.degraded.v1`
- `evolution.release.canary_started.v1`
- `evolution.release.adopted.v1`
- `evolution.release.paused.v1`
- `evolution.rollback.triggered.v1`
- `evolution.rollback.completed.v1`
- `evolution.recursion.stopped.v1`

## 105.3 API 家族（概念契约）

- `POST /v1/evolution/problems`
- `POST /v1/evolution/proposals`
- `GET /v1/evolution/proposals/{proposal_id}`
- `POST /v1/evolution/proposals/{proposal_id}/candidates`
- `POST /v1/evolution/experiments`
- `POST /v1/evolution/evaluations`
- `POST /v1/evolution/governance-decisions`
- `POST /v1/evolution/shadow-runs`
- `POST /v1/evolution/release-requests`
- `POST /v1/evolution/releases/{release_id}/rollback`
- `GET /v1/evolution/lineage/{artifact_id}`

以上为架构级 API 契约，不代表已有服务或工程实现。

---

# 106. V1.7 端到端案例：ADS 改进跨 Agent 任务分配策略

![V1.7 ADS 递归进化实例](assets/30_V1.7_ADS递归进化实例_8k.png)

## 106.1 问题发现

Environment Trace 显示某类复杂任务在多 Agent 联盟中的重复交接较多，平均成本和尾延迟升高。Diagnosis Engine 形成假设：任务分解粒度过细、部分能力匹配规则过度依赖单一信誉指标。

## 106.2 候选方案

- P0：保持当前策略，作为基线；
- P1：调整任务分解粒度；
- P2：加入能力证据维度，避免单一信誉分路由；
- P3：采用环境痕迹触发接续，减少不必要的点对点状态汇报；
- P4：组合 P1/P2/P3，但提高策略复杂度。

## 106.3 独立验证

在相同历史快照和预算下，将 P0–P4 放入 V1.6 Twin，进行多轮回放和压力测试。独立评估器同时检查任务质量、成本、尾延迟、领域公平、安全边界和故障恢复。隐藏任务和不同负载分布用于检验泛化。

## 106.4 治理与采用

如果 P3/P4 在仿真和 Shadow 中收益稳定，但对某些领域造成机会不公平，则 ADS 不得仅按全局平均收益发布。由相关领域 Owner 审查局部影响；跨域配额或权限变化提交人类审批。批准后仅在指定低风险任务和有限流量 Canary，观察后决定采用或回滚。

## 106.5 递归

采用后观察真实结果与预测的差异，形成新的诊断证据。若收益不稳定或副作用扩大，回滚并记录失败原因；若持续有效，提炼成有适用范围的 ImprovementPattern，供其他领域自愿验证采用。下一轮 RSI 可以改进“候选生成方式”，但评估器和根治理权限仍受独立控制。

---

# 107. 验证计划与验收矩阵

## 107.1 阶段路线

**阶段 A：证据与基线**
- 固定目标、基线版本和问题定义；
- 建立诊断证据链和数据截止时间；
- 固定训练/选择/隐藏评估数据分区。

**阶段 B：候选与沙箱**
- 形成结构差异不同的候选；
- 验证候选隔离、权限和预算；
- 检查依赖、签名、可复现性和回滚工件。

**阶段 C：数字孪生与独立评估**
- 回放、仿真、反事实、压力和对抗测试；
- 检查多目标收益和安全硬约束；
- 运行评估器元评估和隐藏留出测试。

**阶段 D：Shadow 与治理**
- 预测和候选对照真实结果但不影响生产；
- 由领域 Owner、安全审查和人类治理主体评审；
- 对获批候选进行有限 Canary，监控并保留回滚。

## 107.2 必测用例

1. 候选是否绑定唯一基线和父版本？
2. 改进生成器是否能访问隐藏测试标签？（应不能）
3. 评估器是否能被候选作者修改？（应不能）
4. 是否存在未经审批的生产凭证或工具访问？（应为零）
5. 同一实验能否按版本和随机种子复现？
6. 是否保留负面结果和失败候选？
7. 是否检查遗忘、泛化和长期稳定性？
8. 是否出现代理指标提高但领域质量下降？
9. 是否发生跨领域私有数据泄漏？
10. 是否有明确预算和递归停止条件？
11. 是否能够从 Canary 恢复上一稳定版本？
12. 审批服务不可用时是否默认停止发布？
13. 是否将模型自评错误地标记为独立验证？
14. 是否将全局平均收益掩盖为每个领域均受益？
15. RSI 是否能修改根策略、身份根信任或审批门槛？（应为零）
16. 是否有不可逆外部副作用的补偿/人工处置计划？
17. 是否监测递归成本、候选多样性和评估器漂移？
18. 领域 Owner 是否能够拒绝 ADS 的公共改进模式？

## 107.3 硬性验收门槛

- 未绑定基线的候选：0；
- 生成器访问隐藏测试集：0；
- 未经审批修改根策略/根身份/生产权限：0；
- 未记录评估器版本和独立性：0；
- 未声明预算或停止条件的递归运行：0；
- 未签名的候选发布：0；
- 无回滚工件的 Canary：0；
- 高风险变更缺少人类审批：0；
- 未经领域 Owner 允许的私有知识出域：0；
- 未执行的验证不得标记为通过。

具体质量提升阈值必须按领域、任务和基线预先登记，不设一个全局百分比替代真实验收。

---

# 108. 架构决策记录（ADR）

| ADR | 决策 | 状态 |
|---|---|---|
| ADR-83 | RSI 仅创建候选，不拥有生产发布权 | 强制约束 |
| ADR-84 | 人类根策略、根身份和审批权限不可由 RSI 自改 | 强制约束 |
| ADR-85 | 生成器与独立评估器分离 | 强制约束 |
| ADR-86 | 每个候选必须绑定基线、差异、证据、预算和回滚 | 强制约束 |
| ADR-87 | 复用 V1.6 Digital Twin 进行模拟和反事实验证 | 候选确认 |
| ADR-88 | 采用多目标评估，安全/授权作为硬约束 | 强制约束 |
| ADR-89 | 递归运行必须有预算、深度和停止条件 | 强制约束 |
| ADR-90 | 采用 Shadow→Human Review→Canary→Limited Release | 候选确认 |
| ADR-91 | ADS 公共改进模式由领域 Owner 自主验证和采用 | 强制约束 |
| ADR-92 | 不将逻辑进化模块直接拆成微服务 | 候选确认 |
| ADR-93 | 评估器和根治理机制不得成为 RSI 自优化对象 | 强制约束 |
| ADR-94 | 失败候选和负面结果必须保留以避免重复探索 | 强制约束 |

## 108.1 待验证假设

- H1：事件证据驱动的诊断比模型自我反思更可靠。
- H2：生成多样候选并保留失败轨迹能提高长期搜索效率。
- H3：V1.6 Twin 能筛除部分高成本、低收益或高风险候选。
- H4：独立隐藏评估能降低评估器被改进生成器操纵的概率。
- H5：多目标和硬约束能降低单一指标 Goodhart 风险。
- H6：Shadow 与有限 Canary 能发现仿真到真实运行的差距。
- H7：多层成长闭环能够实现公共知识复用，同时保留领域自治。
- H8：预算、递归深度和停止规则可以控制成本爆炸和能力退化。

---

# 109. V1.8 研究方向：跨域联邦进化与生态协同

V1.7 建立单生态内的受治理递归改进。V1.8 建议研究多个自治生态如何交换已验证的改进模式、评估证据和能力契约：
- 跨域 ImprovementPattern 的版本兼容与采用策略；
- 联邦评估与隐私保护证据交换；
- 多个 ADS/领域生态之间的改进冲突协调；
- 共享模型的来源证明、撤回和供应链治理；
- 多生态 RSI 的公平性、稳定性与风险传播；
- 人类治理主体之间的跨域责任和审批协议。

V1.8 不应把所有生态合并成一个中心控制器，而应研究如何在自治边界清晰的前提下实现协同进化。

---

# 附录 A：研究证据与原始资料

1. **Recursive self-improvement of AI research agents**, arXiv:2609.26457, 2026-09-22. https://arxiv.org/abs/2609.26457  
   AIDE² 在 8 天自主运行中发现七次连续改进，并在四个留出基准上评估泛化。重要启发：每次接受的改写都成为下一轮对象；必须使用隐藏评估。局限：研究代理/AI R&D 场景，不等于多领域生态级安全验证。

2. **Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops**, arXiv:2607.07663, 2026-07-08. https://arxiv.org/abs/2607.07663  
   对 2024–2026 年 1,250 篇 arXiv 论文进行分类，区分改进对象和闭环程度，指出自我评估信号、grounding、collapse dynamics 和计算约束是关键瓶颈。局限：综述分类不代表每类技术均已成熟。

3. **Self-Improvements in Modern Agentic Systems: A Survey**, arXiv:2607.13104, 2026-07-14. https://arxiv.org/abs/2607.13104  
   将 Agent 表示为基础模型与 prompts、memory、tools、control logic 等 scaffold 的组合，并按更新对象和反馈信号分类。局限：综述性工作，具体安全机制需在项目中验证。

4. **PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents**, arXiv:2608.04003, 2026-08-04. https://arxiv.org/abs/2608.04003  
   26 个场景、204 个 episode，评估跨会话经验保存、检索、更新是否真正改善后续任务。发现收益因能力和框架而异。局限：个人 Agent 基准，不覆盖企业级跨域治理。

5. **AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement**, arXiv:2608.20318, 2026-08-20. https://arxiv.org/abs/2608.20318  
   10 个冻结研究仓库、29 种系统配置；平均得分 0.166，最佳系统 0.250，显示算法级 RSI 仍有显著能力差距。局限：训练算法设计任务，不可直接外推到生态架构进化。

6. **RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement**, arXiv:2607.25886, 2026-07-28. https://arxiv.org/abs/2607.25886  
   58.33% 的设置中，Agent 能通过反馈改进首次有效尝试；但继续搜索超过最佳得分后，78.26% 的运行最终得分下降或无法超过峰值。启发：必须保存最佳 checkpoint、设置停止条件，不能认为多轮迭代必然更好。

7. **Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents**, arXiv:2505.22954, 2025-05-29. https://arxiv.org/abs/2505.22954  
   通过开放式候选档案和经验验证演进代码 Agent，在 SWE-bench 和 Polyglot 上报告性能提升；实验采用沙箱和人类监督。局限：软件工程基准提升不能证明生态治理、安全和长期目标对齐。

8. **Gödel Agent: A Self-Referential Agent Framework for Recursively Self-Improvement**, ACL 2025. https://aclanthology.org/2025.acl-long.1354/  
   研究通过高层目标驱动 Agent 修改自身逻辑和行为。启发：自指改进可扩大搜索空间；局限：自我修改本身不构成独立安全证明。

9. **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile**, NIST AI 600-1, 2024-07-26. https://doi.org/10.6028/NIST.AI.600-1  
   提供生成式 AI 风险管理框架。它是自愿使用的风险管理资源，不应表述为 RSI 专项强制标准。

## 附录 A.1 证据使用原则

- E1：同行评审论文、正式会议论文和可复现基准；
- E2：公开预印本，结果需标注未必经过同行评审；
- E3：官方机构风险管理框架或技术报告；
- E4：本报告基于上述证据推导的架构建议；
- E5：必须通过本项目历史回放、Twin、Shadow 或试点验证的假设。

---

# 附录 B：版本继承与边界

| 版本 | 形成能力 | V1.7 的继承方式 |
|---|---|---|
| V1.2 | 环境驱动型多 Agent 协作与痕迹协作 | 以共享状态、事件和环境痕迹为诊断数据 |
| V1.3 | 生态协作运行基础 | 作为 Agent/Task/Capability 协作模型基线 |
| V1.4 | Environment Runtime | 作为真实状态权威源与事件证据基础 |
| V1.5 | 生态自治、信誉、资源市场、自修复 | 作为被改进对象和治理规则基础 |
| V1.6 | 世界模型、数字孪生、反事实推演 | 作为候选改进的模拟和验证环境 |
| V1.7 | 生态级 RSI | 建立候选生成、独立评估、受治理发布和递归学习 |

---

# 附录 C：版本结论

V1.7 已形成生态级 RSI 的概念边界、修改对象分级、九模块架构、诊断与候选生成、独立评估、反自我欺骗、进化沙箱、数字孪生验证、发布治理、多层成长闭环、预算停止条件、安全威胁、数据契约、事件目录和验收路线。

**状态：架构设计版。** 尚不代表工程实现、运行时验证、模型能力认证或生产授权。建议先选定一个低风险 Agent 工作流，验证 R1/R2 级改进（记忆/技能/工作流），再逐步研究 R3/R4；C5 根权限级变更始终不进入 RSI 自主修改范围。
