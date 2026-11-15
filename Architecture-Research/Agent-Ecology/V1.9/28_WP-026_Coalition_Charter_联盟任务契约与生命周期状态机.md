# WP-026｜Coalition Charter 联盟任务契约与生命周期状态机

**版本：** Agent Ecology V1.9 / WP-026  
**日期：** 2026-11-16  
**状态：** Candidate / Research Design  
**上位工作包：** WP-020—WP-025  
**范围：** 联盟公共契约、领域扩展、Owner 接受、成员 Epoch、生命周期事件、任务租约、Fencing Token、变更/解散和独立验收  
**不包含：** 生产 Runtime、真实跨生态授权、支付结算系统、生产密钥、Runner 或真实业务副作用

## 0. 执行摘要

WP-025 已提出联邦式动态联盟：任务驱动形成、成员 Owner 本地准入、Stigmergy 承载协作状态、A2A 补充必要协商、ADS 负责生态内协调、独立验证和人类治理守住边界。WP-026 将这一组织模型进一步收敛为可验证的任务契约和状态机。

**核心决策：采用“最小公共核心 + 版本化领域 Profile”的 Coalition Charter；Charter 记录协作范围和各方接受，不是权限凭证，不替代成员域本地 PDP/PEP。**

本轮形成八项候选机制：

1. 每个联盟由 Task Owner 发布任务 Charter 和维护权威生命周期账本；这不赋予其其他成员域的根权限。
2. 成员 Owner、数据 Owner、资源 Owner 和目标域 Policy Owner 分别对自己负责的范围签名接受；同一 Charter Digest 才能形成 READY。
3. Charter 使用不可变版本和摘要链；任何范围、数据用途、成员角色、预算或风险级别变化都产生新版本，受影响 Owner 重新接受。
4. Coordinator 只有协调权，不得签发成员授权、改变数据策略、修改 Owner 根治理或代替独立验收。
5. 每个成员的实际执行仍须由目标资源/数据域本地 PDP/PEP 在副作用发生前核验；Charter 本身永远不是 Permit。
6. 任务租约由 Task Owner 或 Resource Owner 的权威服务签发；所有副作用携带单调 Fencing Token 和幂等 Operation ID，资源 Owner 拒绝过期持有者。
7. 执行联盟、独立验证方、价值归因和人类问责分离；贡献评分不能自动改变信任、授权或资源所有权。
8. 联盟解散必须完成凭证撤销、租约释放、资源回收、数据处置、工件归档和争议冻结，不以状态标记 CLOSED 代替清算。

## 1. 设计边界与术语

### 1.1 Coalition Charter

Coalition Charter 是某一具体任务的版本化协作契约，描述任务目标和验收标准、参与成员及角色、能力/资源/数据范围、Purpose、Audience、禁止动作、Coordinator 权限、预算和租约、Owner 接受要求、有效期、撤销条件和审计证据。

Charter 不能自行授予成员对其他生态数据、工具或资源的访问权，也不能将联盟成员的权限合并成一个超级权限。

### 1.2 Charter、Grant、Lease、Permit 和 Evidence 必须分离

| 对象 | 解决的问题 | 权威主体 | 不代表什么 |
|---|---|---|---|
| Coalition Charter | 本任务如何协作、范围和责任是什么 | Task Owner 发布，各相关 Owner 接受 | 不等于执行授权 |
| Owner Grant | 某主体可发布/委托哪些能力或权限 | 能力/数据/资源 Owner | 不等于目标域已允许本次执行 |
| Task/Resource Lease | 某一时段内谁可持有任务槽位或资源 | Task Owner / Resource Owner | 不等于数据或工具 Permit |
| Local Permit | 某主体能否对特定资源执行特定动作 | 目标域本地 PDP/PEP | 不由联盟投票或 Charter 自动产生 |
| Fencing Token | 阻止旧租约持有者在新持有者接管后继续写入 | Lease Authority + 资源 Owner 校验 | 不是授权或身份凭证 |
| Evidence Bundle | 证明谁做了什么、输入输出和验收结果 | 事件/工件来源方与独立验证方 | 不自动证明所有权或价值份额 |

### 1.3 角色边界

- **Task Owner：** 目标、范围、成功标准、Charter 发布、任务租约和最终接受/终止的责任主体。
- **Member Owner：** 对本域 Agent、能力、凭证、数据和资源的加入、授权、暂停、退出负责。
- **Data Owner：** 决定数据资产、用途、接收方、保留期和输出约束。
- **Resource Owner：** 决定资源配额、租约、Fencing Token 的有效性和副作用接受规则。
- **Target-domain Policy Owner：** 管理本地 PDP/PEP、风险策略和 Permit。
- **Coordinator：** 组织分工、排序、状态汇总、重试建议；无权改变成员授权。
- **Independent Verifier：** 独立检查关键成果，不由执行联盟自我签发可信验收。
- **Human Governance：** 处理根策略、重大审批、争议、否决、接管和最终问责。

同一组织可能兼任多个 Owner 角色，但 Charter 必须显式记录角色和签署范围；不能因组织相同而默认角色授权互通。

## 2. 契约结构：最小公共核心 + 领域 Profile

完全统一的大 Schema 会把领域语义固化在生态底座，造成版本耦合；完全独立的领域契约又会导致成员、Owner 接受、版本、撤销、租约和审计字段无法互操作。

**推荐采用最小公共核心 + 版本化领域 Profile。**

公共核心必须统一：
- Charter ID、Coalition ID、版本、Epoch、前序 Digest；
- Task Owner、任务目标、风险级别和验收标准；
- 成员主体、所属 Domain、角色、能力证据和 Membership Epoch；
- Coordinator 权限边界；
- 资源/数据范围引用、Purpose、Audience 和禁止动作；
- 预算、租约、Fencing 要求和幂等命名空间；
- 必需的 Owner 接受角色、独立验证要求、人类审批要求；
- 有效期、撤销条件、生命周期事件流和审计证据；
- notAuthorization=true、notOwnershipTransfer=true。

领域 Profile 负责 PDS 中小学教育、TWS 中医康养、PDM 高等教育、FBS 未来商业等领域的术语、本体引用、数据分类、任务验收指标、合规规则和资源单位。Profile 必须带版本和 Schema URI，不得重定义公共核心的安全语义。未知的关键 Profile 或版本不兼容时，相关成员加入或副作用进入 HOLD。

## 3. Charter 版本、摘要和接受收据

### 3.1 不可变版本

每个 Charter 版本是不可变对象：
- charterVersion 和 charterEpoch 单调递增；
- 新版本包含 previousCharterDigest；
- charterDigest 覆盖规范化的 Charter 主体和所有安全相关字段；
- 接受收据绑定 charterDigest、charterVersion、charterEpoch、role、scopeDigest、policyDigest 和 Key Epoch；
- 不能原地修改已接受版本。

规范化编码候选采用 JCS（RFC 8785）作为 JSON 摘要输入；需补充跨语言测试向量、Unicode/数字边界和字段排除规则。JSON Schema 不能证明签名正确或摘要计算正确。

### 3.2 多方接受

- Task Owner 发布 Charter 候选版本。
- 每个成员的 Member Owner 对加入角色、能力和本域执行边界签署接受。
- Data Owner 对 Asset、Purpose、Audience、Retention 和 Output Constraint 签署接受。
- Resource Owner 对资源、数量、预算、时段和租约条件签署接受。
- 目标域 Policy Owner 仍须在执行前按本地策略签发 Permit。
- 关键任务要求 Independent Verifier 对验证职责、证据范围和利益冲突声明签署接受。
- 所有必需接受必须绑定同一 Charter Digest；不同 Digest 的签名不能拼成一个 READY。

多 Owner 跨域接受不是分布式原子事务。部分接受或网络超时期间，联盟必须保持 ADMISSION_PENDING/HOLD，不得假装全局提交或回滚已完成。

### 3.3 修改影响分析

任务目标、成功标准、风险等级、成员、角色、能力、数据资产、Purpose、Audience、预算、租约、Coordinator 权限、独立验证要求或人类审批要求变化，都必须生成新 Charter 版本。受影响 Owner 重新签署；任何签名不能跨版本复用。无法证明影响范围时，按所有相关 Owner 重新接受处理。

## 4. 联盟生命周期状态机

### 4.1 状态定义

| 状态 | 含义 | 允许的动作 |
|---|---|---|
| DRAFT | Task Owner 本地草拟，尚未对外形成义务 | 编辑本地草稿 |
| PROPOSED | 固定版本已发布，等待参与方审阅 | 发现、评估、拒绝或提出修改 |
| ADMISSION_PENDING | 收集 Owner 接受、能力证明、撤销新鲜度和本地资格 | 验证证据、补齐接受、HOLD |
| READY | 所有必需接受绑定同一 Digest，硬门禁通过 | 申请激活、建立租约 |
| ACTIVE | 联盟在批准范围内运行 | 协作、提交工件、申请本地 Permit |
| PAUSED | Task Owner/安全 Owner 暂停 | 只读审计、修复、重新审批 |
| DEGRADED | 成员、租约、撤销水位、能力或依赖出现异常 | 限制操作、重规划、退出或重配 |
| RECONFIGURING | 变更 Charter、成员或资源 | 生成新版本并重新接受 |
| WINDING_DOWN | 正在撤销权限、释放资源和归档证据 | 清算、交接、数据处置 |
| CLOSED | 清算完成、审计归档、无有效临时租约 | 只读查询 |
| ABORTED | 激活前取消或失败 | 归档原因和已产生证据 |
| QUARANTINED | 发现签名冲突、来源分叉、越权或证据完整性问题 | 隔离、调查和人工治理 |

### 4.2 合法转换

- DRAFT → PROPOSED：Task Owner 发布不可变 Charter 版本。
- PROPOSED → ADMISSION_PENDING：进入身份、Owner、能力、撤销、数据和资源准入核验。
- ADMISSION_PENDING → READY：所有必需 Owner 接受同一 Digest，硬门禁通过。
- READY → ACTIVE：任务 Owner 激活；预先授权的低风险自动激活须受明确策略和人类治理授权约束。
- ACTIVE → PAUSED：Task Owner、成员 Owner 或本地安全门禁触发暂停。
- ACTIVE → DEGRADED：关键成员退出、租约过期、撤销水位过期、资源不足或能力证据失效。
- PAUSED → ACTIVE：重新检查授权、成员 Epoch、撤销新鲜度、租约和策略后，由有权主体恢复。
- DEGRADED → RECONFIGURING 或 WINDING_DOWN：不得自动假定原联盟仍具备完整能力。
- RECONFIGURING → ADMISSION_PENDING：新 Charter 版本发布，受影响 Owner 重新接受。
- ACTIVE/PAUSED/DEGRADED → WINDING_DOWN：任务完成、取消、到期或 Owner 终止。
- WINDING_DOWN → CLOSED：凭证、租约、资源、数据和审计清单全部完成。
- 任一非终态 → QUARANTINED：安全证据冲突、签名分叉、未授权副作用或治理违规。
- DRAFT/PROPOSED/ADMISSION_PENDING/READY → ABORTED：激活前由有权主体取消。

QUARANTINED 不允许自动回到 ACTIVE；必须经独立审查，进入 RECONFIGURING、WINDING_DOWN 或 ABORTED。

### 4.3 状态机安全不变量

1. 没有同一 Charter Digest 的所有必需接受，状态不得进入 READY。
2. 没有目标域本地 Permit，状态为 ACTIVE 也不得产生受保护副作用。
3. 任何关键字段变更必须产生新版本；旧签名不能自动继承。
4. 任何成员退出/撤销都必须增加 Membership Epoch 或撤销对应成员绑定；旧凭证不能继续通过 PEP。
5. DEGRADED、QUARANTINED 和 WINDING_DOWN 不得执行新增高风险副作用。
6. CLOSED 必须有清算证据；不能仅凭任务状态或 Coordinator 声称完成。
7. 执行联盟不得成为自己的独立验证方；关键结果必须由独立主体验证。
8. Charter、联盟投票、贡献分数和声誉均不得覆盖 Owner DENY、撤销墓碑或人类否决。

## 5. 任务租约、Fencing Token 与防止双重副作用

### 5.1 为什么 TTL Lease 不够

租约到期只能说明协调服务不再承认旧持有者；网络分区或进程暂停可能使旧 Agent 仍继续运行。如果资源端只检查客户端是否“曾经持有租约”，旧持有者可能在新成员接管后继续写入。

### 5.2 候选机制

- Lease Authority 对特定 Task/Resource Namespace 签发单调递增的 fencingToken。
- Token 绑定 taskId、coalitionId、charterVersion、memberId、resourceScope、leaseId 和有效期。
- 每次资源副作用都携带 fencingToken 与 operationId。
- 资源 Owner 在本地事务中比较 token 与该资源命名空间已接受的最高 token；低于最高值的请求拒绝。
- operationId 在资源 Owner 的幂等记录中唯一；重复请求返回原结果，不重复产生副作用。
- fencingToken 只在其 Authority/Resource Namespace 内比较，不跨不同 Owner 或资源命名空间比较。
- 租约、Fencing Token 和本地 Permit 是三个不同检查；三者全部通过才可执行。

**核心规则：资源 Owner 必须执行 fencing 检查。只由 Agent 自己检查租约状态，不能阻止失联后的旧进程继续写入。**

### 5.3 任务与资源租约分离

Task Lease 防止多个联盟同时接管同一任务的同一效果命名空间；Resource Lease 控制某一资源的并发占用、配额和时间窗；数据访问许可由 Data Owner/目标域 PDP 单独签发，不从 Task Lease 推导。高风险副作用必须使用幂等 operationId；无法保证幂等或 fencing 的外部系统应进入人工确认或禁止自动重试。

## 6. 准入与运行协议

1. Task Owner 生成 Charter Draft，声明任务目标、验收、风险、范围和预算。
2. 能力发现只返回候选成员；每个成员必须提交 Owner Attestation、能力证据和当前 Membership/Key Epoch。
3. 每个 Owner 按自己管理的资产、能力或资源范围作出接受/拒绝。
4. 接收域本地 PDP 评估 Purpose、Action、Resource、Audience、风险、撤销水位和新鲜度。
5. Coalition Admission Gate 执行硬门禁：身份有效、信任关系有效、Owner 接受齐全、撤销状态新鲜、数据用途合规、资源可用、角色无冲突。
6. 只有硬门禁全部通过，才运行组合优化；收益评分、声誉或资源价格不得抵消任何 DENY/HOLD。
7. Charter 进入 READY 后，Task Owner 激活并取得 Task Lease；成员各自取得所需的最小本地 Permit。
8. Runtime 通过 Stigmergy 发布状态/工件痕迹；A2A 只处理需要明确协商的交互。
9. 每次副作用前由 PEP 复核 Permit、Membership Epoch、撤销状态、租约、Fencing Token 和幂等 Operation ID。
10. 结果由独立验证方检查；Task Owner 最终接受、拒绝或要求返工。

## 7. 资源、数据和价值归因

### 7.1 资源预算

预算按 CPU/GPU、存储、网络、模型调用、工具调用、人工审查和时间窗分类。每个 Resource Owner 只承诺自己控制的配额；联盟不得合并或转让成员根资源权限。稀缺资源优先采用配额、优先级、加权公平队列、租约和反饥饿策略。竞价/价格机制是可选扩展，不作为公共核心默认机制；不得让经济评分覆盖安全硬门禁。资源超预算、配额冲突或 Owner 撤销资源时，联盟进入 DEGRADED 并重新规划。

### 7.2 数据用途与领域本体

Charter 引用数据资产 ID、Ontology/Schema 版本、Purpose、Audience、保留期和输出约束。Data Owner 的接受只覆盖明确的数据用途和接收方；不能通过联盟关系推导跨域二次用途。领域 Profile 可引用 PDS、TWS、PDM、FBS 本体；公共核心不固化领域业务术语。未知本体版本、关键字段或跨域语义映射不一致时，相关操作 HOLD。任何数据转换、摘要或输出都需保留来源和活动链，避免把推导结果误认为原始事实。

### 7.3 贡献和价值

采用可审计事件与工件证据描述谁提供输入、能力、资源和活动，生成了哪些输出工件，哪些 Agent/组织对活动负责，谁独立验证质量和验收条件，以及哪些争议、返工、失败和外部成本尚未结清。

贡献记录不是权限、所有权、法律责任或经济结算的自动判定。争议期间冻结相关结算建议，不冻结必要的安全撤销和数据保护动作。

## 8. 变更、成员退出与联盟解散

成员退出事件记录生效时间、Membership Epoch、影响任务、未完成工作和凭证撤销引用。新成员只能接续经 Owner 授权的持久工件和任务状态，不能继承旧成员令牌、会话、私钥、租约或 Permit。关键成员退出时联盟进入 DEGRADED，重评能力覆盖和风险。

Charter 变更必须新建版本；受影响 Owner 重新接受。变更未完成时只允许既定范围内的安全收尾，不允许扩大副作用。

关闭前必须完成：停止新增任务分配；撤销临时 Grant、Permit 和访问令牌；释放 Task/Resource Lease 并使旧 Fencing Token 失效；回收资源配额和工具会话；按 Data Owner 规则归还、删除或保留数据副本并保存处置证据；归档工件、事件、模型输出、来源和验收记录；处理未完成任务、责任交接和争议；冻结争议中的价值归因/结算；由 Task Owner 与相关 Owner 完成关闭确认；追加 CLOSED 事件并保留只读审计。

## 9. 主要威胁与控制

| 威胁 | 控制 |
|---|---|
| Charter 重放或旧版本恢复 | charterDigest + version + epoch；受影响 Owner 重新接受；旧版本不自动激活 |
| Coordinator 越权 | 固定 COORDINATION_ONLY；本地 PDP/PEP 和 Owner Grant 独立 |
| 成员凭证残留 | Membership Epoch、撤销传播、Lease/Fencing、凭证不可继承 |
| 任务双重执行 | Task Owner 作用域租约、Fencing Token、幂等 Operation ID |
| 旧租约持有者继续写 | Resource Owner 对 token 做事务性单调比较 |
| 多方签署不同 Charter | 所有接受绑定同一 Digest；不拼接不同版本签名 |
| 自我验收 | 独立验证主体与执行主体分离，并审查运营控制域 |
| 数据用途扩张 | Data Owner 接受绑定 Asset/Purpose/Audience/Retention；目标域本地执行 |
| 资源垄断或饥饿 | Owner 配额、公平队列、反饥饿和资源上限 |
| 解散后残留访问 | 清算清单、凭证撤销、资源回收和数据处置证明 |
| 贡献证据操纵 | PROV-O 风格来源链、签名事件、独立验收和争议冻结 |
| 领域 Schema 漂移 | 公共核心稳定、领域 Profile 版本化、未知关键 Profile HOLD |

## 10. 验收矩阵摘要（36 项，全部 NOT_RUN）

覆盖 Charter 核心字段、Digest、版本链、签署角色、多方同摘要接受、授权分离、Coordinator 权限、Owner/Data/Resource/Target Policy、变更重签、旧签名重放、Epoch、状态机合法/非法转换、事件序列缺口、Task/Resource Lease、Fencing Token、幂等 Operation ID、双重执行、公平性、Purpose/Audience、领域 Profile、独立验收、贡献争议、成员退出、凭证撤销和解散清算。详细用例见 validation/WP026_COALITION_CHARTER_LIFECYCLE_MATRIX.csv。所有项目保持 NOT_RUN；本轮未运行 Runtime 或真实副作用。

## 11. 观测指标

- Charter Digest 不一致率、Owner 接受完整率、重新签署耗时；
- 从成员撤销到各 PEP 拒绝的延迟；
- 租约竞争次数、Fencing Token 拒绝次数、旧持有者副作用数（安全目标为 0）；
- operationId 重放次数、重复副作用数（安全目标为 0）；
- 任务等待时间、资源利用率、配额偏差、饥饿率；
- 联盟相对单 Agent 的质量增益、协调开销、成本和延迟；
- 独立验证覆盖率、利益冲突告警、争议处理时间；
- 解散清算完成率、残留凭证数、未释放租约数和未处置数据副本数。

## 12. 候选 ADR（待评审）

| ADR | 主题 | 候选决策 |
|---|---|---|
| ADR-161 | Charter 结构 | 采用最小公共核心 + 版本化领域 Profile；Profile 不得改变核心安全语义 |
| ADR-162 | Charter 与授权分离 | Charter 仅记录协作契约和各方接受；notAuthorization=true，执行必须经过目标域本地 PDP/PEP |
| ADR-163 | 不可变版本与接受 | Charter 版本不可变；接受收据绑定 Digest、Version、Epoch、Role、Scope Digest 和 Key Epoch |
| ADR-164 | 任务租约与 Fencing | Task/Resource Lease 由权威 Owner 签发；资源 Owner 事务性拒绝低于最高已接受值的 Fencing Token |
| ADR-165 | 幂等副作用 | 外部副作用必须携带 Owner-scoped operationId；无法幂等的动作进入人工确认或禁止自动重试 |
| ADR-166 | 独立验收 | 关键结果由执行联盟之外的独立验证主体验收；控制域独立性需要单独证据 |
| ADR-167 | 解散清算 | CLOSED 必须满足凭证撤销、租约释放、资源回收、数据处置、审计归档和争议状态检查 |
| ADR-168 | 证据与价值分离 | 使用来源/活动/主体工件链记录贡献；贡献分数不自动授予权限、信任、所有权或结算权 |

以上全部 Candidate，未获正式批准。

## 13. 未决问题（12 项）

1. 公共核心最小必填字段应由哪些领域共同冻结？
2. Task Owner 失联、破产或无权继续维护账本时，如何通过带外治理更换 Charter Authority？
3. 多个 Data Owner 对组合数据用途的限制冲突时，采用拒绝优先还是更严格约束求交集？
4. 领域 Profile 的发布、弃用、兼容窗口和语义迁移由谁治理？
5. Fencing Token 应由 Task Owner、Resource Owner 还是独立租约服务签发？如何避免多 Authority 竞争？
6. 对无法支持幂等键或 fencing 的遗留工具，哪些操作可允许自动化？
7. 运营域、管理域、KMS 域和部署域的独立性如何进行可审计证明？
8. 独立验证方的费用、资源和潜在利益冲突如何治理？
9. 贡献证据与实际经济价值之间如何避免把相关性误当因果？
10. 解散后数据保留、删除和审计留存之间如何按领域法律与 Owner 策略协调？
11. 低风险自动组盟的阈值、规模和可撤销条件如何由人类治理批准？
12. 多生态联盟出现争议时，技术状态冻结、业务连续性和最终裁决的顺序如何定义？

## 14. 本轮结论

WP-025 解决“生态如何形成动态联盟”；WP-026 解决“联盟如何被各方明确接受、受限运行、变更、交接并正确关闭”。

**推荐把 Coalition Charter 作为联盟层的协作契约，把 Owner Grant/Local Permit 作为权限层，把 Lease/Fencing 作为并发副作用控制层，把 Evidence/Independent Review 作为可信验收层。四者不可合并成一个万能联盟 Token。**

该结构既支持 PDS、TWS、PDM、FBS 等不同业务领域的领域 Profile，也维持 ADS 生态内协调职责和各企业/数据/资源 Owner 的自治边界。

WP-026 当前仅完成候选架构研究和契约草案；36 项验收全部 NOT_RUN；8 项 ADR Candidate；12 项未决事项开放；V1.8 F0 未通过；productionAllowed=false；Runner 未启用。

## 15. 原始资料

1. W3C ODRL Information Model 2.2 Recommendation：https://www.w3.org/TR/odrl-model/
2. W3C PROV-O Recommendation：https://www.w3.org/TR/prov-o/
3. CloudEvents Specification：https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
4. etcd v3.6 API Transactions：https://etcd.io/docs/v3.6/learning/api/
5. etcd API Guarantees：https://etcd.io/docs/v3.6/learning/api_guarantees/
6. ZooKeeper Recipes and Solutions：https://zookeeper.apache.org/doc/current/recipes.html
7. JSON Canonicalization Scheme (JCS), RFC 8785：https://www.rfc-editor.org/rfc/rfc8785.html
