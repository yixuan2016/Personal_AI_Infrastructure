# Agent Ecology 321 项与 Stigmergy 实证验收任务包（Codex / macOS）

- 任务包版本：1.0
- 建立日期：2026-11-23
- 任务分支：codex/agent-ecology-stigmergy-acceptance-20261123
- 验收基线仓库：yixuan2016/Personal_AI_Infrastructure
- 基线分支：integration/agent-ecology-v1.9-mainline-clean-20261121
- 基线提交：8d2f10969a33e92bf701b20589cfc3f4ba5548c1
- 任务包性质：研究候选与隔离验收；不是生产发布授权
- 总原则：先执行、后判定；证据先于状态；未执行不得标记 PASS

## 1. Codex 的总任务

在 macOS 隔离环境中，完成 Agent Ecology V1.9 的 321 个唯一验收项，以及与 PALOS T07/T08、Stigmergy、HAR WP-HA-24/WP-HA-25 的跨仓库集成验证。产出可复现的机器证据、失败清单、差异报告和验收结论。

必须将以下工作视为一个整体，但分别保留各自权威来源与验收状态：

1. Agent Ecology V1.9：321 个唯一验收 ID。
2. Agent Ecology 协议：21 份候选 JSON Schema、4 项 P0、10 项 P1、36 条 P0 Policy Validator 候选向量。
3. WP-024：60 项韧性矩阵、L0/L1 有界参考模型、TLA+ TLC 检查。
4. PALOS T07/T08：E05 12 个、E13 24 个 D0 合成样本，30 条 Oracle 规则，36 条样本覆盖映射。
5. PALOS Oracle 权威边界：25 条向量（8 正例、17 反例）。
6. PALOS Mock PDP/PEP：33 项内存隔离测试。
7. HAR：WP-HA-24（18 事件恢复契约、30 项融合验收、16 项生命周期映射）；WP-HA-25（17 项依赖缺口、27 项权威映射、29 项集成验收）。

不要将不同矩阵的数量相加后重复计数。321 项以本任务包内的 321_ACCEPTANCE_REGISTER.csv 为唯一执行登记表；ECO-01 至 ECO-17 在主矩阵与 WP-025 专项矩阵重复呈现，只计一次，两个来源都要保留。

## 2. 强制安全边界

### 允许

- 仅使用 macOS 本地隔离环境、合成数据、内存模拟器和离线参考模型。
- 运行 Python、Rust、TLA+、JSON Schema 和本地单元测试。
- 在独立 Codex 执行分支中修改研究候选 Schema、测试夹具、验证器和文档。
- 记录真实失败、缺少依赖、环境阻塞和未执行事项。
- 在用户可审查的独立 PR 中提交证据与研究变更。

### 禁止

- 不启用生产 Runner，不调用生产 PALOS Runtime。
- 不连接真实 Provider、真实业务端口、真实账户、真实密钥或真实业务数据。
- 不执行有外部副作用的工具调用、网络写入、短信、电话、邮件、支付或部署。
- 不把 GitHub Actions 的失败 Job、无步骤 Job 或没有日志的 Job 当作测试失败或通过。
- 不自动合并 PR，不推送到 main，不重写历史，不强制推送。
- 不运行 git reset --hard、git clean -fd、破坏性数据库迁移或清空用户目录的命令。
- 不为了让测试通过而降低安全断言、删除负向用例、放宽 fail-closed 规则或改写预期结果。
- 不把静态解析、Schema 文件存在、代码可导入、测试被收集，误报为动态验收 PASS。

### 网络策略

默认禁止网络出站。只允许使用已缓存依赖与仓库已有锁文件。确实缺少依赖时先记录 BLOCKED、报告所需包名和固定版本，等待人工批准；不得私自安装未固定版本或访问外部服务。

## 3. 状态词汇与证据规则

每个验收 ID 只能处于以下状态：

- PASS：执行了明确的命令/测试，断言全部满足，证据文件已保存，并可由独立检查复核。
- FAIL：测试确实执行，且实际结果违反预期。
- BLOCKED：因依赖、环境、权限、工具或前置条件无法执行；必须说明阻塞原因及解除条件。
- NOT_RUN：尚未尝试执行。

禁止使用“完成”“看起来正常”“文件已存在”等自然语言替代状态。任何状态变更都必须有证据路径、执行提交 SHA、命令、退出码和执行时间。负向测试中，被测系统正确拒绝危险请求，属于测试 PASS，而不是 FAIL。

所有证据存放于执行仓库的 artifacts/agent-ecology-stigmergy/<run-id>/ 目录。每项测试保存独立 JSON 记录；大日志按文件保存，并在记录中写明 SHA-256。证据文件不得包含密钥、个人数据或生产标识。

## 4. 仓库与基线

### A. Agent Ecology 源仓库

- 仓库：yixuan2016/Personal_AI_Infrastructure
- 基线分支：integration/agent-ecology-v1.9-mainline-clean-20261121
- 基线提交：8d2f10969a33e92bf701b20589cfc3f4ba5548c1
- 当前验收矩阵位于 Architecture-Research/Agent-Ecology/V1.9/ 下。

### B. PALOS 源仓库

- 仓库：yixuan2016/palos
- 基线分支：research/palos-t07-t08-ecology-stigmergy-v1.1-20261122
- 已核验基线提交：1aed11298c972cfed10dc19c2abfb67f123a6623
- D0 校验脚本：scripts/research/validate_t07_t08_d0.py
- Oracle 权威边界脚本：scripts/research/validate_oracle_authority_boundary.py
- Mock PDP/PEP：scripts/research/mock_oracle_pdp_pep.py

Codex 应在本机分别克隆/检出以上仓库，并在开始时记录实际 HEAD；若远端分支已变化，不得静默覆盖本任务包的基线，应先生成 compare 报告并等待人工确认更新基线。

### C. HAR 集成研究仓库

- 仓库：yixuan2016/HybridArchitectureResearch
- 分支：main
- 已合并研究：WP-HA-24 PR #105、WP-HA-25 PR #127。
- 执行前读取这两个工作包的当前矩阵，不复制成新的权威矩阵，不把“已合并研究文件”当成“验收已通过”。

## 5. macOS 环境预检

在任何代码修改或测试执行前，生成 preflight.json，至少包含：

- macOS 版本、硬件架构（uname -m）、CPU 核心数、内存、磁盘可用空间。
- Git、Python、Java、Rust/Cargo、TLA+ TLC 的版本与实际路径。
- 三个仓库的远端 URL（脱敏）、分支名、HEAD SHA、工作区状态。
- Python 虚拟环境位置、已安装依赖清单、锁文件摘要。
- 网络出站状态、生产凭证检测结果（只记录是否存在，不读取或输出秘密值）。
- 是否发现未提交改动；若存在，停止清理操作并保护现场。

建议预检命令：sw_vers；uname -a；uname -m；sysctl -n hw.ncpu；df -h；git status --short；git rev-parse HEAD；python3 --version；python3 -m pip list --format=json；java -version；cargo --version；which tlc。

用户当前使用 macOS；本任务不要求 Windows，也不得把 Windows 构建列为阻断条件。

若机器资源不足，优先串行执行；不得通过增加并发导致测试结果不稳定。

## 6. 分阶段执行计划

### Phase 0 — 基线与安全预检

1. 读取本任务包与源矩阵，验证 321 个唯一 ID。
2. 记录三个仓库的基线 SHA、工作区状态和依赖版本。
3. 检查是否存在真实凭证；只报告存在/不存在，不读取秘密。
4. 确认网络出站默认关闭、生产 Runner 未启用。
5. 创建独立执行分支，例如 codex/execute-agent-ecology-stigmergy-20261123；不得直接改动基线分支。

验收：preflight.json、baseline-compare.md、环境锁定清单齐备。

### Phase 1 — Agent Ecology 21 份 Schema

1. 枚举 Architecture-Research/Agent-Ecology/V1.9/contracts/ 下的 21 份候选 Schema。
2. 先做 JSON 语法解析，再做 Draft 2020-12 元 Schema 验证。
3. 解析全部本地 $ref；检查循环引用、悬空引用、重复 $id、未定义字段、错误的类型/格式。
4. 为每份 Schema 保存独立验证结果和总报告。
5. 不得因 JSON 语法解析通过就标记 Schema PASS。

必须关闭的 4 项 P0：

- AE-SCH-P0-01：Trust Root 更新模式必须对 NORMAL_DUAL_THRESHOLD 与 EMERGENCY_OUT_OF_BAND_RECOVERY 建立互斥证据门禁；正常模式校验旧根/新根阈值、Key Epoch、签名时间和独立 Custody Domain；紧急模式要求事前登记且独立保管的 Recovery Anchor；两种模式均绑定 Root Digest、单调版本、有效期和防回滚证据。
- AE-SCH-P0-02：WitnessLifecycleEvent 必须有签名、Issuer 身份/Key Epoch、事件摘要和合法状态迁移约束。
- AE-SCH-P0-03：WitnessKeyLifecycleRecord 必须有签名、最终事件摘要，并绑定 witnessId、keyId、keyEpoch、keyFingerprint、keyPurpose、lifecycleSequence。
- AE-SCH-P0-04：WitnessQuorumPolicy 必须验证真实 Quorum 数学关系、成员集合去重、不同 Operator/Failure Domain 和 Policy Digest 绑定。

必须处理的 10 项 P1：CloudEvents 扩展命名与类型；CoalitionLifecycleEvent 条件分支属性；Charter Digest 与 Owner Acceptance 签名 Profile；PeerTrustBinding 默认禁止传递信任；Witness Registry ACTIVE 独立性证据；Quorum/Policy/Owner 签名封装一致性；Owner Delegation 父子权限衰减；Witness/Key 生命周期时序；FederationSyncCheckpoint 有效期和快照连续性；Lifecycle Event 状态机运行时验证。

P0/P1 修复必须配正反例。危险输入必须 fail-closed。修复前后均保留测试证据，不得只修改 Schema 使旧夹具通过。

### Phase 2 — Policy Validator 与形式化验证

1. 找到并核验 36 条 P0 Policy Validator 候选向量；逐条执行，保存判定输入、输出和规则版本。
2. 验证 Trust Root、Witness、Quorum、Owner、Revocation、Checkpoint 和联盟生命周期的不变量。
3. 复核 WP-024 L0/L1 Python BFS 参考模型；重新执行并与既有报告逐项比对。
4. 找到仓库中的 TLA+ 模型、配置文件和 TLC JAR；记录版本与 SHA。
5. 对三个既定配置执行 TLC；若 TLC 未安装且无缓存，记 BLOCKED，不得下载未知二进制绕过网络策略。
6. 将 TLC 状态空间/反例与 Python BFS 对照；对每个反例给出最小复现和修复前后差异。
7. WP-024 的 60 项正式矩阵逐项登记；已有 L0/L1 报告不能替代 TLC 或正式矩阵验收。

重点检查 Safety 与 Liveness 分离：安全性失败不得由吞吐、延迟或任务质量得分抵消；活性指标不得掩盖重复执行、越权或旧 Worker 写入。

### Phase 3 — PALOS D0 数据与 Oracle

在 PALOS 仓库根目录执行：

1. python3 scripts/research/validate_t07_t08_d0.py --root . --require-jsonschema
2. python3 scripts/research/validate_oracle_authority_boundary.py --root . --require-jsonschema
3. python3 scripts/research/mock_oracle_pdp_pep.py

预期覆盖基线：

- D0 样本 36 条：E05=12、E13=24；逐样本 SHA-256 与全文件 SHA-256 必须匹配。
- Oracle Registry 30 条；Coverage 36 条；样本 Oracle ID 与 Coverage 逐项一致。
- Oracle 权威边界 25 条：8 个正例、17 个反例；正例验证允许的评估/授权边界，反例验证禁止越权。
- Mock PDP/PEP 33 项：必须逐项执行，不允许仅通过 unittest discovery 或导入成功代替执行。
- 另有 36 条 P0 Policy Validator 候选向量，独立计数，不混入 321 项。

当前独立复核已确认 D0 文件内容、逐样本哈希、Manifest 哈希和映射关系一致；这仅是远端数据完整性复核，不等于本机脚本已执行。完整 Draft 2020-12 验证、25 条 Oracle 向量和 33 项 Mock 测试仍须在本机实际执行。

若脚本输出 NOT_RUN、MISSING_REQUIRED、BLOCKED 或缺少依赖，必须保留原始输出，不得改写为 PASS。

### Phase 4 — Stigmergy E05/E13 对照实验

严格遵循 PALOS 研究预注册文件：
docs/research-gap-closure/31-T07-T08-AgentEcology与Stigmergy研究深化与E05-E13预注册方案V1.1.md

使用 D0 数据集：
docs/research-gap-closure/35-PALOS-T07-T08-D0合成Pilot样本集V0.1.jsonl

禁止擅自改动样本、Oracle 预期、实验条件或成功阈值。若发现设计缺陷，先记录偏差并创建新版本预注册，不得事后修改预期来迎合结果。

对照组至少区分：

- 单 Agent 基线；
- A2A 点对点通信；
- 共享黑板/共享状态；
- Stigmergy 持久痕迹与事件触发协作。

对照原则：

- 相同任务、模型/工具版本、总 Token 或计算预算、超时和重试预算；
- 使用配对随机种子，记录随机种子和实验顺序；
- 分离质量、Safety、Liveness、成本和延迟；不得把它们合成一个可互相补偿的总分；
- 多轮重复，报告均值、中位数、方差、置信区间和效应量；样本量不足时明确报告功效不足；
- 记录 p50/p95 时延、Token、消息/痕迹数、上下文膨胀、重复工作、任务成功率、故障恢复时间、撤销传播时间、越权尝试和审计完整性；
- 对并发写、重复事件、乱序、因果环、痕迹污染、过期痕迹、租约过期、旧 Worker、网络分区、Agent 崩溃与恢复进行故障注入。

必须验证的结论不是“Stigmergy 一定更好”，而是：在什么任务复杂度、Agent 数量、失败率、共享状态延迟和治理要求下，Stigmergy 优于 A2A；在什么条件下它更差或需要混合通信。

E05/E13 的 36 条 D0 样本是 Pilot 输入，不得将 36 条样本直接等同于 36 次独立统计重复。必须按预注册设计执行多轮配对实验，并说明外推边界。

### Phase 5 — Agent Ecology 321 项逐项验收

唯一登记表：execution/321_ACCEPTANCE_REGISTER.csv。

对每个 test_id：

1. 找到原始场景、预期结果、严重度和证据要求。
2. 定位对应实现/模型/契约和测试入口。
3. 编写或复用确定性测试；保留原始 test_id，不得重编号。
4. 先运行单项测试，再按工作包运行组测试，最后执行回归。
5. 生成独立 evidence JSON，记录命令、退出码、实际输出、执行 SHA、时间、环境、日志路径与 SHA-256。
6. 更新登记表 actual_status；每个状态变更必须有 evidence_ref。
7. 对 FAIL 建立缺陷条目、最小复现、根因、修复提交和回归证据。
8. 对 BLOCKED 写明具体缺少的依赖、权限或前置条件及解除办法。
9. 不可执行的项目保持 BLOCKED/NOT_RUN；不得通过静态审查代替运行。

工作包顺序：BASE-STG → F1 → WP-020 → WP-021 → WP-022 → WP-023 → WP-024 → WP-025 → WP-026。执行时允许发现依赖关系并调整，但必须记录理由。

### Phase 6 — HAR 跨工作包集成

从 HAR main 读取 WP-HA-24 与 WP-HA-25 最新矩阵，并建立 source_test_id → HAR_test_id → PALOS_test_id 的映射。

必须检查：

- 事件类型、聚合根、版本范围、权威源、消费者、幂等键、持久动作、重放与对账、授权边界。
- Trace/Artifact/State/Workflow 生命周期的权威映射；不得将痕迹等同于事实或授权。
- 任务认领、Lease、Fencing Epoch、幂等收据、恢复检查点、撤权传播和审计证据的一致性。
- ADS/PALOS/Agent Ecology/Workflow 的对象映射和语义不等价约束。
- 跨域 Owner、数据权属、信任关系和策略版本变化后的失效行为。

WP-HA-24/25 文件已经合并进 HAR main，不等于 18+30+16+17+27+29 项验收通过。保留 HAR 自己的测试 ID 和状态，不要把它们合并进 321 的计数。

### Phase 7 — 最终审计与交付

必须生成：

- preflight.json
- baseline-compare.md
- schema-validation-report.json
- policy-validator-report.json
- wp024-formal-verification-report.md
- palos-d0-validation.json
- oracle-authority-boundary-report.json
- mock-pdp-pep-report.json
- stigmergy-e05-e13-experiment-report.md
- 321_ACCEPTANCE_REGISTER.csv（执行后的最终版本）
- 321_ACCEPTANCE_SUMMARY.json
- cross-repo-contract-mapping.csv
- failure-and-blocker-register.csv
- reproducibility-manifest.json
- FINAL_ACCEPTANCE_REPORT.md

最终报告必须同时给出：PASS、FAIL、BLOCKED、NOT_RUN 数量；不得把 BLOCKED 和 NOT_RUN 从分母中剔除。所有 321 项均 PASS 且 P0/P1 协议门禁关闭、关键安全性质通过、HAR 跨仓库映射无未决权威冲突，才可以提出“验收完成”建议。否则只能报告部分完成，并列出阻断项。

## 7. 当前已知基线与不可误报事项

- Agent Ecology 九份 CSV 原始合计 338 行；ECO-01 至 ECO-17 重复出现 17 次；去重后 321 个唯一验收 ID。
- 321 项在本任务包建立时均为 NOT_RUN。
- 21 份候选 Schema 的 JSON 语法解析曾通过，但 Draft 2020-12 完整验证未执行。
- 当前静态审查记录 4 项 P0、10 项 P1；68 项 ADR Candidate、94 项 Threat Candidate、85 项静态未决事项 OPEN。
- WP-024 L0/L1 有界 Python 参考模型已有报告；TLA+ TLC 未运行；WP-024 正式 60 项仍 NOT_RUN。
- PALOS D0 数据集独立远端完整性复核通过，但本机验证脚本尚未执行。
- PALOS Oracle 25 条权威边界向量尚未执行。
- PALOS Mock PDP/PEP 有 33 个测试方法；现有 GitHub Actions Job 在产生测试步骤前失败，不能据此判断代码 PASS 或 FAIL。
- 不要复跑/启用生产 Runner；本地 macOS 运行才是本任务目标。

## 8. 分支、提交与合并规则

1. 本任务包分支只存放任务说明、执行登记表和证据 Schema。
2. Codex 执行代码与修复必须另开执行分支，基于经人工确认的基线。
3. 每个逻辑修复独立提交；提交信息包含工作包和测试 ID。
4. 每次修改 Schema、模型、授权逻辑、Oracle 或 RSI，必须同步更新契约、迁移/兼容说明、测试、状态和 CHANGELOG。
5. 不得自动合并到 main、不得自动启用 Auto Merge、不得把 Draft PR 转 Ready。
6. 执行完成后提交独立 Draft PR，由人类审查证据、风险、差异和回滚方案。

## 9. 可直接交给 Codex 的执行指令

你是本项目的隔离验收执行工程师。请严格按本文件执行，不要只总结计划。

先完成 Phase 0，确认 macOS 环境、三个仓库的实际 SHA、工作区和依赖。随后按 Phase 1–7 逐阶段执行。每完成一个阶段，先生成机器证据和阶段报告，再继续下一阶段。

必须实际运行测试；不得只创建测试文件、只做静态分析、只写验收报告。不能执行的事项必须标记 BLOCKED 或 NOT_RUN，并解释原因。不得伪造日志、哈希、退出码、统计结果或 PASS。

全程只使用合成数据和本地隔离模拟器；生产 Runner、真实 Provider、真实凭证、真实业务数据和外部副作用一律禁止。保护现有工作区，不执行破坏性清理，不自动合并任何分支。

最终交付完整证据包、321 项逐项登记表、Stigmergy E05/E13 实验报告、跨仓库映射、失败与阻塞清单，以及一份可供人类评审的最终报告。