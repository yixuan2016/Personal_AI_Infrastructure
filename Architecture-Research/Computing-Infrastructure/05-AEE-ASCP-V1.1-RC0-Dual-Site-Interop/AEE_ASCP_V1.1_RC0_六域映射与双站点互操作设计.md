# 算力底座｜AEE / ASCP V1.1-RC0 {#算力底座aee--ascp-v11-rc0}

## 六域映射与双站点联邦互操作设计

**日期：** 2026-11-10\
**版本：** AEE/ASCP V1.1.0-RC0\
**上位契约基线：** V2.9-RC9.2-DM04-IFC0.1\
**继承研究：** 环境驱动型多 Agent 协作架构报告 V1.2；AEE/ASCP
V1.0.0-RC0\
**文档性质：** 纯架构研究、契约映射和互操作验证设计\
**状态：** 候选设计，待双方 Owner
与架构委员会评审；非工程实现、非真实部署、非生产验收

------------------------------------------------------------------------

## 0. 执行结论 {#0-执行结论}

V1.1 的核心结论是：**AEE/ASCP 应作为横切六个接口域的扩展
Profile，而不是新增第七个接口域，也不是第二套环境平台、事件总线、租约权威或授权引擎。**

本版将 AEE/ASCP V1.0 六个对象映射到 V2.9-RC9.2-DM04
既有权威体系，完成双站点协作流程、网络分区行为、A2A 1.0
扩展激活规则和增量验收矩阵。

### 0.1 本轮冻结候选 {#01-本轮冻结候选}

1.  六域接口与权威边界保持不变。
2.  `EnvironmentSpace` 调整为非权威 `EnvironmentSpaceDescriptor`。
3.  `TraceRecord` 作为 CloudEvents 1.0.2 的 ASCP
    语义投影，不另建平行事件库。
4.  `EnvironmentSubscription` 映射为事件源授权下的订阅资源；FWSX
    只负责投递、游标和重放。
5.  `TaskClaimLease` 更名为
    `TaskClaim`，只在站点本地任务阶段内生效；不代表算力资源 Lease。
6.  `ArtifactBinding` 作为 Evidence/Result/Artifact
    的关联，不新增成果权威库。
7.  `GovernanceContext` 作为请求上下文引用，不成为授权凭证或全局 PDP。
8.  A2A 1.0 扩展通过 Agent Card 声明、请求级 `A2A-Extensions` 激活；Task
    只使用 metadata，不添加核心协议未定义的 extensions 数组。
9.  复用 DM04 已有 48 项测试，新增 18 项 AEE/ASCP 专项测试；合计 66
    项候选检查。
10. 所有真实测试状态仍为"待执行"，本报告不声称双站点互操作已通过。

## 1. 基线与范围 {#1-基线与范围}

### 1.1 继承关系 {#11-继承关系}

  基线                               本版处理
  ---------------------------------- --------------------------------------------------------------------------
  环境驱动型多 Agent 协作架构 V1.2   继承 ST-01 环境、ST-02 痕迹、ST-03 运行时、ST-04 ADS 治理、ST-05 RSI
  AEE/ASCP V1.0.0-RC0                继承六个对象的业务意图；修正重复权威和对象命名
  V2.9-RC1 六域接口                  继承六域分权、统一请求信封、身份委托、本地策略门禁、Saga、事件和错误语义
  V2.9-RC9.2-DM04-IFC0.1             作为本版上位契约；复用 48 项验收矩阵、事件、错误、状态与兼容规则

DM04
当前属于"冻结候选基线"：接口、Schema、事件、错误和验收矩阵已形成，但
Owner 签署、工具链验证、双实现互操作和真实双站点测试仍待执行。

### 1.2 非目标 {#12-非目标}

-   不新建第七个接口域。
-   不新建全局 Lease Authority、全局授权引擎或全局事务管理器。
-   不改变 DSP 的数据目录、合同和传输边界。
-   不把 A2A Task 状态机替代 SCO/DM04 的任务 Saga。
-   不把 FWSX 变成事件事实权威或跨域数据授权方。
-   不编写工程代码，不宣称真实站点已部署。

## 2. 总体架构决策：AEE/ASCP 横切六域 {#2-总体架构决策aeeascp-横切六域}

AEE/ASCP 是协议 Profile 和语义映射层，定义 Agent
如何发现环境、订阅授权痕迹、关联任务与证据、携带治理上下文。它横切六个既有接口域：

1.  联邦治理：成员、信任协议、Profile、参与方绑定和退出。
2.  身份与授权：工作负载身份、委托、PDP/PEP、Grant 与撤销。
3.  数据空间：目录、数据合同、传输和用途审计。
4.  算力星：能力、报价、预留、资源 Lease 和执行环境证明。
5.  联邦任务：TaskContract、Plan、Prepare、Commit、Saga、对账和补偿。
6.  证据与验收：ExecutionReceipt、Evidence、Result、Acceptance、Metering、Settlement、Dispute。

### 2.1 两个横切技术组件 {#21-两个横切技术组件}

-   **FWSX（事件交付适配层）：**
    可负责事件分发、订阅游标、重试、重放、跨站点传输和积压管理；不拥有事件的业务事实，不批准数据用途，不改变事件源
    Owner 的权威。
-   **A2A（Agent 间协议）：** 负责 Agent 发现、消息、任务交互和 Artifact
    交接；不替代六域业务接口，不授予跨站点数据或资源权限。

ADS/SCO 是跨域协调和治理能力，不接管站点本地 IAM/PDP/PEP、数据
Owner、资源 Lease Authority 或独立业务验收方。

## 3. 六个 AEE 对象的 V1.1 规范映射 {#3-六个-aee-对象的-v11-规范映射}

### 3.1 EnvironmentSpace → EnvironmentSpaceDescriptor {#31-environmentspace--environmentspacedescriptor}

**性质：非权威组合描述符。**

建议字段：

-   `environment_ref`
-   `federation_profile_ref`
-   `trust_agreement_ref`
-   `participant_binding_refs`
-   `site_refs`
-   `data_space_contract_refs`
-   `ontology_profile_ref`
-   `policy_profile_ref`
-   `owner_refs`
-   `valid_from` / `valid_until`
-   `descriptor_version`

权威来源分别是联邦治理方、站点治理方、数据 Owner 和 Ontology Owner。ADS
可解析和缓存描述符，但不得把它作为新的成员名册、数据空间、信任根或授权数据库。

V1.0 的 `EnvironmentSpace` 保留为兼容别名；V1.1 新建对象使用
`EnvironmentSpaceDescriptor`。描述符过期或来源不一致时必须重新解析，不能猜测补全。

### 3.2 TraceRecord → CloudEvents ASCP 投影 {#32-tracerecord--cloudevents-ascp-投影}

**性质：既有事件信封上的领域语义 Profile，不另建第二事件库。**

字段映射： \| ASCP 语义 \| CloudEvents / DM04 映射 \| \|\-\--\|\-\--\|
\| `trace_id` \| CloudEvents `id` \| \| `source` \| CloudEvents `source`
\| \| `trace_type` \| CloudEvents `type` 的受控命名空间语义 \| \|
`subject_ref` \| CloudEvents `subject` \| \| `occurred_at` \|
CloudEvents `time` \| \| `payload_schema_ref` \| CloudEvents
`dataschema` \| \| `payload` \| CloudEvents `data` \| \| `site_id` \|
DM04 扩展 `siteid` \| \| `aggregate_id` \| DM04 扩展 `aggregateid` \| \|
`aggregate_version` \| DM04 扩展 `aggregateversion` \| \| `sequence_no`
\| 聚合内单调序号扩展 \| \| `correlation_id` / `causation_id` \| DM04
因果与关联扩展 \| \| `signature_ref` \| 事件签名引用扩展 \|

规则：

-   CloudEvents `id` 是唯一事件标识，不再额外生成不同的 `trace_id`。
-   每个事件由其业务事实 Owner 发布；FWSX 不得改写
    `source`、`subject`、`data` 或签名。
-   Observation、Intent、Risk、Decision
    等语义必须标记事实/推断/提案/决策类别；模型推断不得伪装成 Owner
    已签发事实。
-   不承诺全局事件总序；只保证单一权威聚合内的序号和因果关系。
-   未知事件可以安全存档和告警，但不得触发副作用。

### 3.3 EnvironmentSubscription → EventSubscription {#33-environmentsubscription--eventsubscription}

**性质：事件源授权下的订阅资源。**

订阅字段：`subscription_ref`、`subscriber_principal`、`source_domain`、`environment_ref`、`event_type_filters`、`purpose`、`classification_ceiling`、`projection_profile`、`delivery_mode`、`cursor`、`expires_at`、`status`。

权威和责任：

-   订阅者提出订阅；
-   事件源 Owner 决定是否允许该主体订阅该事件投影；
-   目标站点本地 PDP/PEP 复核；
-   FWSX 只负责投递、游标、重试和重放。

订阅成功不代表有权读取事件载荷中的所有字段，也不代表有权读取 Artifact
URI。事件字段投影与 Artifact 引用解析必须分别授权。

### 3.4 TaskClaimLease → TaskClaim {#34-taskclaimlease--taskclaim}

**性质：站点本地任务阶段的执行认领记录，不是资源租约。**

V1.1 将规范名称更改为 `TaskClaim`，建议字段：

-   `claim_ref`
-   `global_task_ref`
-   `site_task_ref`
-   `stage_ref`
-   `site_id`
-   `holder_agent_ref`
-   `claim_epoch`
-   `issued_at`
-   `expires_at`
-   `max_expires_at`
-   `state`
-   `policy_decision_ref`
-   `idempotency_key`

关键边界：

-   全局任务由 SCO 维护 Saga 协调视图。
-   每个站点的本地任务协调器对本地 TaskStage 做原子认领。
-   `claim_epoch`
    只在本地任务阶段范围内单调递增，用于拒绝旧认领者的任务状态写入。
-   `LocalResourceLease.fencing_token` 仍由资源所在地 Lease Authority
    签发，用于保护物理资源。
-   `claim_epoch` 不得作为 GPU、存储、网络或设施资源的 fencing token。
-   DataUseGrant 仍由数据 Owner 授权。
-   不建立第二个全局 Lease Authority。

V1.0 的 `TaskClaimLease` 仅作为迁移别名；旧 `fencing_token`
字段不得直接映射成资源 Lease 的 token。

### 3.5 ArtifactBinding → Evidence / Result 关联 {#35-artifactbinding--evidence--result-关联}

**性质：关联引用，不新增 Artifact Registry 权威。**

`ArtifactBinding` 仅保留
`artifact_ref`、`artifact_version`、`content_digest`、`producer_ref`、`task_ref`、`evidence_ref`、`result_ref`、`acceptance_ref`
和访问策略引用。

成果正文、版本和摘要由既有 Artifact/Evidence Owner 管理；Result
是否允许披露由既有 Result Review/DecideRelease 控制；业务是否接受由独立
Acceptance Owner 决定。

A2A Artifact ID 可能只在 A2A Task 范围内唯一，必须映射到 DM04 的全局
Artifact/Evidence 引用，不得将 A2A Artifact ID 直接当作跨站点全局 ID。

### 3.6 GovernanceContext → Request Context Reference {#36-governancecontext--request-context-reference}

**性质：请求上下文引用，不是授权凭证。**

字段：`governance_context_ref`、`subject_ref`、`purpose`、`policy_decision_ref`、`grant_refs`、`delegation_ref`、`risk_ref`、`evaluated_at`、`valid_until`、`revalidation_required`。

规则：

-   DM04 `RequestEnvelope` 中的
    `caller_principal`、`workload_identity`、`audience`、`purpose`、`issued_at`、`expires_at`、`protocol_profile`
    等仍是基础权威字段。
-   GovernanceContext 只能引用评估记录、Grant 和委托关系，不可作为
    bearer token。
-   每次敏感数据读取、Artifact URI
    解析、任务认领、资源动作和跨域操作仍需目标站点本地 PDP/PEP 再检查。
-   远端 Permit 不能覆盖本地 Deny；ADS 不得替目标站点签发本地权限。

## 4. DM04 请求信封的兼容策略 {#4-dm04-请求信封的兼容策略}

不直接向 IFC0.1 的既有必需字段添加破坏性字段。

**首选方案：** 由双方把可选 `profile_extensions` 映射作为 DM04 IFC0.2 的
Minor 候选增量。键为双方认可的 AEE/ASCP Profile URI，值为受 Schema
约束的 `AEEContext`。原有必需字段保持不变。

`AEEContext` 最小字段：

-   `environment_ref`
-   `ontology_profile_ref`
-   `trace_refs`
-   `subscription_ref`（条件必需）
-   `task_claim_ref`（条件必需）
-   `artifact_binding_ref`（条件必需）
-   `governance_context_ref`
-   `criticality`

**兼容回退：** 在双方尚未签署 IFC0.2 前，只能使用 IFC0.1
已明确允许的操作级 metadata/扩展点；若该操作没有合法扩展点，则不发送 AEE
扩展字段，或暂停该跨域操作。不得依赖未知字段被对端"碰巧接受"。

未知非关键扩展可忽略并留痕；影响身份、权限、受众、用途、数据分类、地域、资源边界或副作用的关键扩展必须拒绝或隔离。

## 5. A2A 1.0 扩展绑定 {#5-a2a-10-扩展绑定}

依据 A2A 当前规范，AEE/ASCP 不修改 A2A 核心对象：

1.  Agent 声明支持扩展：`AgentCard.capabilities.extensions[]`，每项含
    `uri`、`description`、`required`、`params`。
2.  扩展按请求激活：客户端在 HTTP `A2A-Extensions` 请求头中声明
    URI；服务端只激活自己支持且本次协商成功的扩展，并在响应中回显成功激活项。
3.  Message：使用 `extensions[]` 和以扩展 URI 为键的 `metadata`。
4.  Artifact：使用 `extensions[]` 和以扩展 URI 为键的 `metadata`。
5.  Task：使用 `metadata` 承载 AEE 引用；不添加 A2A 核心协议未定义的
    Task `extensions[]` 字段。
6.  A2A Task State 只表达 A2A 协议生命周期，不映射覆盖 DM04 的
    Prepare、PartialCommit、ActivationBarrier、UNKNOWN、Acceptance、Settlement
    等领域状态。
7.  对跨站点高风险动作，若请求未成功激活所需
    Profile，必须在产生副作用前拒绝或转为授权协商状态。

扩展 URI 必须由项目控制的稳定域名或永久标识管理；文档中的
`https://ads.example.invalid/...`
仅是占位符，正式发布前必须替换。不要使用 A2A 官方命名空间冒充官方扩展。

## 6. 六域接口复用与增量 {#6-六域接口复用与增量}

  六域         复用既有操作                                                                                                                AEE/ASCP 增量                                   不得新增的权威
  ------------ --------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------- ------------------------------------
  联邦治理     Join、TrustAgreement、Profile、Participant.Bind/Review/Revoke、Exit                                                         Profile 附带 AEE/ASCP 版本、环境描述符引用      第二套成员名册/信任根
  身份与授权   AuthenticateWorkload、ResolveParticipantBinding、Delegation、Policy.Evaluate/DecisionStatus                                 GovernanceContextRef、请求目的与扩展激活状态    全局 PDP、远端本地 Grant
  数据空间     Catalog.Query、Contract.Negotiate/Agree/Terminate、Transfer、Usage.Report                                                   事件投影订阅引用、字段最小化投影                绕过数据合同的事件数据通道
  算力星       Capability.Discover、Capacity.Quote、Reservation、Lease、Attestation                                                        Agent 发现可引用能力证据和站点上下文            ADS 代签资源 Lease
  联邦任务     Task.Create/Validate/Plan/Prepare/Commit/Suspend/Cancel/GetStatus/WatchEvents/Reconcile/Compensate                          本地 TaskClaim、Trace 因果关联、A2A Task 映射   全局 TaskClaim Lease Authority
  证据与验收   Evidence.PublishReference/RetrieveAuthorized、Result.Stage/Review/DecideRelease/Release、Acceptance、Metering、Settlement   ArtifactBinding 关联和 Trace 引用               第二套 Artifact Registry、自行验收

FWSX 是横切事件投递适配层，不构成第七接口域。A2A 是 Agent
通信协议，不替代六域接口。

## 7. 双站点参考部署 {#7-双站点参考部署}

### 7.1 每个站点必须自治保留 {#71-每个站点必须自治保留}

-   本地 IAM、工作负载身份验证、参与方映射和本地 PDP/PEP。
-   本地 Data Owner、连接器、DataUseGrant 和数据用途审计。
-   本地资源目录、调度器、Lease Authority、FencingToken 和设施安全联锁。
-   本地任务协调器、TaskStage、TaskClaim 和执行回执。
-   本地 Outbox/Inbox、事件缓冲、游标、审计和恢复能力。
-   本地 Evidence/Result/Acceptance 权威和计量来源。

### 7.2 联邦层提供 {#72-联邦层提供}

-   ADS：成员、信任、Profile、共同语义和跨域治理协调。
-   SCO：全局任务计划、ContractGraph 关联、Saga 协调和对账视图。
-   FWSX：事件投递、订阅游标、补拉和跨站点传输。
-   A2A：Agent 发现、消息和任务交互。
-   以上能力均不能替代站点本地权威。

## 8. 双站点端到端流程 {#8-双站点端到端流程}

1.  **互信建立：** 双方治理方完成 Join、TrustAgreement、Participant
    Binding 和 Profile 解析。
2.  **Profile 协商：** 双方声明 AEE/ASCP、DM04、Ontology Profile 和 A2A
    兼容版本。
3.  **环境解析：** ADS 组合生成
    EnvironmentSpaceDescriptor，引用真实权威，不复制信任根或数据合同。
4.  **Agent 身份：** 目标站点验证工作负载身份、参与方映射和委托链。
5.  **订阅建立：** Agent 提交订阅目的、事件过滤和分类上限；事件源 Owner
    与本地 PDP/PEP 审核后，FWSX 建立投递游标。
6.  **痕迹发布：** 事件源以 CloudEvents 信封发布 Trace；FWSX
    投递授权投影；消费者通过 Inbox 去重。
7.  **任务规划：** SCO 建立全局 TaskContract/Plan/Saga
    视图，按站点拆分本地 TaskStage。
8.  **本地认领：** Site A/B 各自本地任务协调器原子签发
    TaskClaim；不创建跨站点全局任务锁。
9.  **数据与算力准备：** Data Owner 签发用途 Grant；资源 Owner 进行
    Quote/Reservation 并签发 LocalResourceLease。
10. **激活门禁：** SCO 聚合检查 ActivationBarrier；任何关键项
    Fail/Unknown 均不得进入启动阶段。
11. **本地再授权：** 每站点执行前再次检查
    Grant、Lease、FencingToken、撤销水位、数据分类和设施安全联锁。
12. **执行与证据：** Agent 执行并提交 ExecutionReceipt、Evidence/Result
    引用；A2A 只传递必要的引用和交互内容。
13. **披露与验收：** Result 经过披露审查；独立验收方签发
    AcceptanceRecord。
14. **计量结算：** Owner 原始 MeteringRecord
    进入对账，结算方依据合同、计量和验收形成 Settlement。
15. **闭环复盘：** Trace、事件、审批、回执、证据和决策进入可审计链；RSI
    候选进入独立评估、Shadow、审批和回滚链。

## 9. 网络分区与故障降级矩阵 {#9-网络分区与故障降级矩阵}

  故障场景            Site A                                              Site B                           联邦层/恢复要求
  ------------------- --------------------------------------------------- -------------------------------- ----------------------------------------------------------------
  A-B WAN 分区        已有有效本地 Lease 内的低风险任务可按本地策略继续   同左                             跨域新授权、跨域新提交暂停；事件本地缓冲
  ADS 不可用          本地 IAM/PDP/PEP 继续履行本地权威                   同左                             不得因 ADS 不可用而默认放行高风险动作
  FWSX 不可用         Outbox 持久化，保留游标                             Inbox 不丢弃已接收事件           恢复后按 cursor 补拉；重复事件去重
  远端写操作超时      本地权威查询实际状态                                本地权威查询实际状态             状态记为 UNKNOWN；禁止盲目重放
  远端撤销传播延迟    Owner 本地立即执行撤销                              对撤销水位未知的高风险动作暂停   恢复后同步撤销事件、对账水位和未完成任务
  事件乱序/缺口       按 aggregate sequence 检测                          按 aggregate sequence 检测       补拉快照/事件；不构建虚假的全局顺序
  Artifact 授权撤销   新读取由本地 PEP 拒绝                               新读取由本地 PEP 拒绝            已经披露的数据不能保证远程收回；按合同处理缓存、删除和下游义务
  单站点恢复          先恢复本地权威状态、租约和审计                      对端仍按本地策略运行             对账完成后恢复跨域 Saga；不自动重放不确定副作用

### 9.1 关键降级原则 {#91-关键降级原则}

-   本地已签发且未过期的资源 Lease 仍由本地 Lease Authority
    决定是否有效。
-   本地低风险续行必须在事先授权的离线范围、预算和有效期内。
-   不能确认远端 Grant、撤销水位、Lease 或签署状态时，不得用缓存的联邦
    Permit 替代本地检查。
-   断网期间产生的事件先本地持久化；恢复后使用幂等和对账恢复，不假设
    exactly-once。
-   数据已被读取或复制后，撤销不能保证"远程收回"；必须通过数据合同、缓存策略、密钥管理和删除证明控制后续风险。

## 10. AEE/ASCP 专项增量验收矩阵 {#10-aeeascp-专项增量验收矩阵}

本版新增 18 项专项测试，编号 AEE-001---AEE-018。DM04-001---DM04-048
原矩阵保持不变。

  编号      场景                                          预期结果                                                          优先级
  --------- --------------------------------------------- ----------------------------------------------------------------- --------
  AEE-001   环境描述符由不同权威引用拼装                  不产生第二套成员、信任或数据权威                                  P0
  AEE-002   环境描述符中的 Participant Binding 已撤销     解析结果标记失效，不允许继续跨域动作                              P0
  AEE-003   AEE Profile 版本未协商                        按 Profile 兼容策略拒绝或降级为不含扩展的安全流程                 P0
  AEE-004   TraceRecord 映射 CloudEvents                  id/source/type/subject/time/dataschema/data 一致，无双重事件 ID   P0
  AEE-005   未知 ASCP Trace Type 到达                     安全存档、告警，不触发任务或副作用                                P0
  AEE-006   同一 Trace 经 FWSX 重复投递                   Inbox 去重，业务副作用只发生一次                                  P0
  AEE-007   Trace 的事实/推断标签缺失或冲突               隔离或标为未验证，不升级为事实                                    P0
  AEE-008   订阅请求超出用途或分类上限                    源 Owner/PDP 拒绝或脱敏投影，不扩大字段范围                       P0
  AEE-009   订阅撤销后继续投递                            停止后续投递，游标与撤销事件可审计                                P0
  AEE-010   A/B 两 Agent 同时认领同一站点 TaskStage       仅一个 TaskClaim 有效                                             P0
  AEE-011   Site A TaskClaim 被误用为 Site B 资源 Lease   Site B Lease Authority 拒绝                                       P0
  AEE-012   旧 TaskClaim claim_epoch 提交状态             本地任务协调器拒绝旧 epoch                                        P0
  AEE-013   ArtifactBinding 引用不存在或摘要不符          隔离引用，不接受成果                                              P0
  AEE-014   Artifact 引用被转发到无权站点                 目标站点 PEP 拒绝读取                                             P0
  AEE-015   GovernanceContext 过期或 Grant 已撤销         重新评估；本地 Deny 优先                                          P0
  AEE-016   A2A 请求未激活必需 AEE 扩展                   在副作用前拒绝或要求重新协商                                      P0
  AEE-017   A2A Task ID 与 SCO TaskRun ID 不同            映射可追踪，不强行合并 ID 或状态机                                P1
  AEE-018   A-B 断网期间发生事件缺口与部分提交            状态 UNKNOWN；恢复后按 Owner 权威对账，不盲重放                   P0

### 10.1 通过门槛 {#101-通过门槛}

-   所有 P0 用例通过后，才可进入受控试点。
-   P1 用例须有明确风险接受和补齐期限。
-   未授权成功次数为零。
-   双重资源承诺次数为零。
-   旧 TaskClaim epoch 和旧资源 FencingToken 均不得成功写入。
-   重复外部副作用为零。
-   关键状态与授权审计覆盖率目标为
    100%，必须以测试证据实测，不得仅凭设计声明。
-   每项测试必须记录运行 ID、站点、实现版本、Profile/Schema
    版本、输入摘要、结果、证据引用、缺陷和验收人。

## 11. 版本兼容与迁移 {#11-版本兼容与迁移}

  V1.0 对象/字段                   V1.1 规范处理                   迁移约束
  -------------------------------- ------------------------------- ---------------------------------------------------
  `EnvironmentSpace`               `EnvironmentSpaceDescriptor`    兼容读取旧别名；新写入用新类型
  `TraceRecord.trace_id`           CloudEvents `id`                不生成第二个 ID；旧字段只作为别名
  `EnvironmentSubscription`        `EventSubscription`             引用源 Owner 的订阅和授权状态
  `TaskClaimLease`                 `TaskClaim`                     旧字段迁移到 claim_ref；不映射 LocalResourceLease
  `TaskClaimLease.fencing_token`   `claim_epoch`（任务范围）       禁止映射到资源 Lease fencing token
  `ArtifactBinding`                Evidence/Result/Artifact 关联   不复制正文，不新建全局 Registry
  `GovernanceContext`              `GovernanceContextRef`          不迁移为 bearer token 或全局 Grant

版本独立管理：AEE/ASCP Profile、DM04 API、JSON Schema、Ontology
Profile、A2A
Protocol、Policy/Grant、TaskContract、ResourceProfile。任务创建时固定版本引用；运行中不得静默升级。

## 12. ADR 决策记录 {#12-adr-决策记录}

  ADR          决策                     候选结论                                           状态
  ------------ ------------------------ -------------------------------------------------- ------------
  AEE-ADR-01   是否新增第七接口域       否；AEE/ASCP 横切六域                              建议冻结
  AEE-ADR-02   EnvironmentSpace 权威    组合描述符，引用现有权威                           建议冻结
  AEE-ADR-03   TraceRecord 存储         CloudEvents ASCP 投影，不另建事件库                建议冻结
  AEE-ADR-04   FWSX 定位                事件交付适配层，不拥有事实或授权                   建议冻结
  AEE-ADR-05   TaskClaim 权威           站点本地任务协调器签发                             建议冻结
  AEE-ADR-06   TaskClaim 与资源 Lease   完全分离；claim_epoch 不可替代资源 fencing token   建议冻结
  AEE-ADR-07   GovernanceContext        请求上下文引用，不是凭证                           建议冻结
  AEE-ADR-08   A2A 扩展                 遵循 A2A 1.0 的声明与请求级激活                    建议冻结
  AEE-ADR-09   DM04 请求信封扩展        `profile_extensions` 作为 IFC0.2 可选 Minor 候选   待双方评审
  AEE-ADR-10   双站点一致性             本地权威 + Saga 协调视图 + 事件最终一致            建议冻结

## 13. 实施前研究与验收路线 {#13-实施前研究与验收路线}

  阶段                工作                                                 退出条件
  ------------------- ---------------------------------------------------- --------------------------------
  G0 架构评审         六域映射、对象权威、Owner/RACI、Profile URI          双方 Owner 确认职责矩阵
  G1 契约验证         Schema、A2A 扩展、CloudEvents、请求信封兼容          机器校验与双方工具链验证通过
  G2 双实现互操作     两套独立实现执行 DM04 48 项 + AEE 18 项              字段、状态、错误和事件语义一致
  G3 故障与安全验证   WAN 分区、ADS/FWSX 故障、撤销、UNKNOWN、重放、越权   P0 全通过；缺陷闭环
  G4 受控试点评审     审计、回滚、资源与数据 Owner 签署                    人类治理审批后才可试点
  G5 正式发布评审     生产 SLO、容量、恢复目标、审计和风险接受             正式发布门禁全部签署

### 13.1 Owner/RACI 最低清单 {#131-ownerraci-最低清单}

-   Federation Governance Owner：双方成员准入、信任协议和 Profile。
-   IAM/Security Owner：身份、委托、密钥、撤销和本地 PDP/PEP。
-   Data Owner：数据合同、Grant、用途、披露和删除义务。
-   Compute Resource
    Owner：Offer、Quote、Reservation、Lease、FencingToken 和设施联锁。
-   SCO/Task Owner：TaskContract、Plan、Saga、TaskClaim 和对账视图。
-   Evidence/Acceptance
    Owner：ExecutionReceipt、Evidence、Result、Acceptance、Metering 和
    Settlement。
-   Agent Owner：能力声明、A2A 扩展支持、订阅目的和 Agent 行为边界。

ADS 可以协调这些 Owner，但不能代替他们签署或承担本地事实权威。

## 14. 当前状态与下一步 {#14-当前状态与下一步}

**已形成：**

-   V1.0 六对象到 DM04 六域的映射修正；
-   六域权威边界和接口复用矩阵；
-   CloudEvents/ASCP 事件映射；
-   A2A 1.0 扩展激活约束；
-   TaskClaim 与 LocalResourceLease 分离；
-   双站点故障降级和恢复规则；
-   18 项 AEE/ASCP 增量验收用例；
-   参考架构图、Schema 候选、CSV 和样例。

**尚未完成：**

-   双方正式 Owner 签署；
-   正式扩展 URI；
-   DM04 IFC0.2 `profile_extensions` 是否纳入；
-   Schema/OpenAPI/A2A 工具链互操作验证；
-   两套独立实现；
-   真实双站点故障注入和安全验收。

**本轮准确状态：架构设计与评审资料已形成；测试待执行；未推送
GitHub；未部署。**

------------------------------------------------------------------------

## 附录 A：A2A 1.0 官方扩展规范参考 {#附录-aa2a-10-官方扩展规范参考}

-   A2A Extensions：`https://a2a-protocol.org/dev/topics/extensions/`
-   A2A Specification：`https://a2a-protocol.org/latest/specification/`
-   A2A Agent
    Card：`https://a2a-protocol.org/latest/specification/agent-card/`

A2A 扩展声明位于 AgentCard 的 capabilities.extensions；扩展请求通过
`A2A-Extensions` 激活；Message 和 Artifact 可使用扩展 URI 与
metadata；Task 通过 metadata
承载扩展上下文。扩展不得修改核心对象定义或枚举。

## 附录 B：交付文件

-   `AEE_ASCP_V1.1_RC0_六域映射与双站点互操作设计.md`
-   `AEE_ASCP_V1.1_RC0_六域映射与双站点互操作设计.docx`
-   `schemas/AEE_ASCP_V1.1_RC0_Profile.schema.json`
-   `mappings/AEE_ASCP_六域权威映射矩阵.csv`
-   `mappings/AEE_ASCP_对象迁移与复用矩阵.csv`
-   `mappings/AEE_ASCP_事件与DM04映射.csv`
-   `tests/AEE_ASCP_18项双站点增量验收矩阵.csv`
-   `examples/A2A_1.0_AEE_ASCP_扩展示例.json`
-   `diagrams/AEE_ASCP_六域嵌入双站点架构.svg`
-   `diagrams/AEE_ASCP_六域嵌入双站点架构_8K.png`
-   `diagrams/AEE_ASCP_双站点协作流程.mmd`
-   `MANIFEST_SHA256.txt`
