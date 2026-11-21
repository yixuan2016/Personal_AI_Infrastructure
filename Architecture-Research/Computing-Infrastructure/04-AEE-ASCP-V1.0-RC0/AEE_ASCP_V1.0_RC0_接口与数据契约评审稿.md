# ADS Environment Extension（AEE）与 Stigmergic Collaboration Profile（ASCP）

## V1.0.0-RC0 接口与数据契约评审稿 {#v100-rc0-接口与数据契约评审稿}

**项目：** 算力底座 / ADS 智能生态协同\
**版本：** AEE 1.0.0-RC0；ASCP 1.0.0-RC0\
**日期：** 2026-11-10\
**文档性质：** 架构研究与机器可读契约候选稿\
**状态：** RC0，待架构评审；非生产实现、非互操作验收结论

------------------------------------------------------------------------

## 1. 本版定位与继承关系 {#1-本版定位与继承关系}

本稿作为《环境驱动型多 Agent 协作架构研究报告
V1.2》的增量契约附录，不重写既有 ST-01---ST-05。

-   ST-01 继续定义共享环境的空间、数据平面、所有权和部署边界。
-   ST-02
    继续定义七类基础痕迹、痕迹信封、生命周期、因果、幂等和版本策略。
-   ST-03 继续定义
    Observe---Filter---Match---Authorize---Claim---Plan---Execute---Submit---Verify---Accept
    运行闭环。
-   ST-04 继续定义 ADS 跨域治理、共同语义、动态授权和领域责任边界。
-   ST-05 继续定义 RSI 的评估、回放、Shadow、Canary、审批和回滚。

本稿仅补足六个环境协作对象的机器可读结构、Ontology 映射、事件增量目录及
A2A 扩展映射。

### 1.1 版本分离 {#11-版本分离}

  版本维度           本稿建议值                  说明
  ------------------ --------------------------- --------------------------
  AEE Profile        1.0.0-RC0                   环境对象与跨对象引用契约
  ASCP Profile       1.0.0-RC0                   痕迹协作行为与事件约束
  JSON Schema        Draft 2020-12               机器校验方言
  Ontology Profile   由领域声明                  不与 AEE 版本共用版本号
  A2A Protocol       Agent Card 声明的兼容版本   不修改 A2A 核心对象

正式发布前必须替换治理域
URI、明确签名配置、通过契约测试并获得架构委员会批准。

## 2. 六个核心对象 {#2-六个核心对象}

  对象                      定位                                       Ontology 处理                              权威主体
  ------------------------- ------------------------------------------ ------------------------------------------ --------------------------------------
  EnvironmentSpace          环境空间、范围、分层和访问边界             AEE 扩展实体                               空间 Owner；ADS 维护跨域目录
  TraceRecord               七类协作痕迹的标准化记录                   复用 ST-02，不另造事实实体                 痕迹发布者；事实 Owner 保留事实权威
  EnvironmentSubscription   Agent 对环境事件的订阅契约                 AEE 扩展实体                               订阅者与环境服务
  TaskClaimLease            对一个 Task/Stage 的短期执行认领权         AEE 扩展实体                               SCO
  ArtifactBinding           将环境痕迹、任务与成果注册表对象关联       复用 Artifact/Evidence/Checkpoint 等实体   成果 Owner
  GovernanceContext         身份、策略判定、授权和义务的上下文引用包   组合引用，不是授权凭证                     ADS 协调；本地 PDP/PEP 和 Owner 执行

### 2.1 不可混淆的边界 {#21-不可混淆的边界}

1.  `TaskClaimLease` 只解决"谁获得某个任务阶段的执行认领权"，不代表获得
    GPU、存储、网络或数据访问权。
2.  `ResourceLease` 仍由本地资源 Owner/LCP 签发；不得由 SCO 或 ADS
    代签。
3.  `ArtifactBinding`
    只保存引用、版本、摘要和治理元数据，不复制成果正文。
4.  `GovernanceContext` 是短时上下文快照和引用集合，不是 bearer
    token，不得单独作为放行凭证。
5.  `TraceRecord` 是协作信号；不得把模型推断、预测或提案伪装成 Owner
    已签发的事实。
6.  `EnvironmentSpace` 不改变数据所有权；跨域可见性必须通过数据 Owner
    批准的投影和本地 PEP。

## 3. 通用对象元数据 {#3-通用对象元数据}

六个对象继承 V2.3 Ontology V3.0 的通用字段语义：

-   `id`：不可变、全局唯一标识。
-   `object_type`：对象类型。
-   `schema_version`：本对象 Schema 版本。
-   `ontology_profile_version`：使用的 Ontology Profile 版本。
-   `issuer_id`：发布/签发主体。
-   `owner_id`：权属主体；本稿六类对象均要求明确。
-   `created_at`、`updated_at`：创建和更新时间。
-   `valid_from`、`valid_until`：适用时的有效期。
-   `status`：对象状态。
-   `source_ref`：来源或权威记录引用。
-   `content_digest`：算法与摘要值。
-   `signature_ref`：条件必需的签名或证明引用。
-   `classification`：数据分类。
-   `labels`：非权威检索标签。

`schema_version`、`ontology_profile_version`、A2A 协议版本和 Agent
自身版本必须分别管理。

## 4. 对象契约 {#4-对象契约}

### 4.1 EnvironmentSpace {#41-environmentspace}

必需字段：

  字段                     类型                   约束
  ------------------------ ---------------------- --------------------------------------------------------------------------------
  `environment_ref`        URI                    稳定空间引用
  `space_type`             Enum                   `agent_private` / `domain_collaboration` / `cross_domain` / `governance_audit`
  `scope`                  Object                 明确租户、领域、站点或主体范围
  `owner_id`               ID                     空间权属主体
  `trust_domain_ref`       URI                    信任域引用
  `ontology_profile_ref`   URI                    语义 Profile 引用
  `access_policy_ref`      URI                    访问策略引用
  `data_plane_allowlist`   Array`<Enum>`{=html}   允许承载的逻辑数据平面
  `parent_space_ref`       URI                    可选父空间
  `status`                 Enum                   `active` / `suspended` / `retired`

四类空间与五个数据平面正交：空间回答"谁可以访问"，数据平面回答"数据承担什么职责"。

### 4.2 TraceRecord {#42-tracerecord}

复用 ST-02 的痕迹信封，不另造一套字段语义。

必需字段：`trace_id`、`trace_type`、`schema_version`、`source`、`actor_id`、`domain_id`、`occurred_at`、`recorded_at`、`subject_ref`、`environment_ref`、`payload_schema_ref`、`payload`、`classification`、`visibility`、`policy_ref`、`purpose`。

七类
`trace_type`：`Observation`、`Intent`、`Task`、`Artifact`、`Dependency`、`Risk`、`Decision`。

可靠性字段：`causation_id`、`correlation_id`、`parent_trace_ids`、`sequence_no`、`idempotency_key`、`evidence_refs`、`content_digest`、`signature_ref`、`expires_at`。

痕迹记录追加写入。证伪、撤销、替代和隔离通过新事件表达，不原位改写历史。

### 4.3 EnvironmentSubscription {#43-environmentsubscription}

必需字段：`subscription_ref`、`subscriber_ref`、`environment_ref`、`purpose`、`filters`、`delivery_mode`、`policy_ref`、`status`、`created_at`、`expires_at`。

`filters` 仅允许声明式过滤：痕迹类型、领域引用、Ontology
Profile、主体类型、最高数据分类和优先级范围。禁止在订阅表达式中执行任意代码或任意
SQL。

投递模式：`pull`、`push`、`stream`。推送目标只保存受控引用，不在公共痕迹中暴露敏感回调地址或凭证。

### 4.4 TaskClaimLease {#44-taskclaimlease}

必需字段：`claim_lease_ref`、`task_ref`、`holder_agent_ref`、`issued_by_ref`、`claim_epoch`、`fencing_token`、`issued_at`、`expires_at`、`max_expires_at`、`state`、`policy_decision_ref`、`idempotency_key`。`stage_ref` 在任务阶段级认领时提供；任务级认领可省略。

状态：`active`、`expired`、`released`、`revoked`、`unknown`。

规则：

-   同一任务/阶段的有效认领由 SCO 原子签发。
-   `claim_epoch` 和 `fencing_token` 单调递增。
-   旧 token 的迟到写入必须被拒绝。
-   续租受最大期限和任务预算约束。
-   租约过期不自动等同任务失败；必须先检查副作用和待对账状态。
-   不得将此租约解释为 `ResourceLease` 或 `DataUseGrant`。

### 4.5 ArtifactBinding {#45-artifactbinding}

必需字段：`binding_ref`、`environment_ref`、`artifact_ref`、`artifact_version`、`content_digest`、`producer_ref`、`task_ref`、`access_policy_ref`、`binding_state`。

可选字段：`evidence_refs`、`verification_ref`、`acceptance_ref`、`parent_artifact_refs`、`lineage_ref`。

`binding_state`：`published`、`pending_verification`、`verified`、`accepted`、`superseded`、`revoked`。

Artifact Registry / 成果 Owner
对成果版本和内容摘要负责；独立验证者负责验证；授权验收主体负责采纳。生产者不能单方面把成果状态改为
`accepted`。

### 4.6 GovernanceContext {#46-governancecontext}

必需字段：`context_ref`、`subject_ref`、`environment_ref`、`purpose`、`requested_actions`、`policy_refs`、`policy_decision_refs`、`evaluated_at`、`valid_until`、`decision`、`revalidation_required`。

可选字段：`grant_refs`、`obligations`、`delegation_ref`、`risk_ref`、`revocation_ref`、`correlation_id`。

`decision`：`Permit`、`Deny`、`NotApplicable`、`Indeterminate`、`RequireApproval`、`StepUp`、`Redact`、`Defer`。

治理上下文只表达某次评估的引用和约束。每次敏感数据读取、Artifact URI
解析、任务认领、工具调用和跨域操作仍由本地 PEP
重新检查。策略服务不可用时，高风险动作 fail-closed。

## 5. 一致性与权威模型 {#5-一致性与权威模型}

  对象                      一致性要求                       写入权威                 传播方式
  ------------------------- -------------------------------- ------------------------ ------------------------
  EnvironmentSpace          版本化；策略变更使用 CAS/审批    空间 Owner               最终一致投影
  TraceRecord               追加写、不可变、可去重           发布者；原始事实 Owner   至少一次投递、幂等消费
  EnvironmentSubscription   订阅版本和游标持久化             订阅者/环境服务          至少一次投递
  TaskClaimLease            单任务/阶段强约束原子认领        SCO                      状态事件与对账
  ArtifactBinding           版本化、摘要校验、不可静默覆盖   成果 Owner               引用同步
  GovernanceContext         短时有效、按动作重验             PDP/授权 Owner           撤销事件加本地收敛

不得承诺端到端 exactly-once。建议采用事务性 Outbox、Inbox
去重、至少一次投递、幂等消费者和外部副作用对账。

## 6. Ontology V3.0 映射 {#6-ontology-v30-映射}

  AEE 对象                  既有实体/契约                                                   处理方式
  ------------------------- --------------------------------------------------------------- --------------------------------------
  EnvironmentSpace          Participant、Tenant、TrustDomain、Site、Policy                  新增 AEE 扩展实体；引用既有权威主体
  TraceRecord               事件信封、EvidenceRecord、Lineage                               复用 ST-02；事实仍由原 Issuer 负责
  EnvironmentSubscription   AgentCapability、Policy、Participant                            新增 AEE 扩展实体
  TaskClaimLease            TaskRun、TaskStage、ResourceLease                               新增任务认领扩展实体；与资源租约分离
  ArtifactBinding           EvidenceRecord、Checkpoint、DatasetVersion、Artifact Registry   仅新增关联，不复制成果内容
  GovernanceContext         Policy、PolicyDecision、DataUseGrant、Credential、Attestation   组合引用，不建立新的授权权威

## 7. 事件目录增量 {#7-事件目录增量}

### 7.1 建议新增 AEE 事件 {#71-建议新增-aee-事件}

-   `EnvironmentSpaceCreated`
-   `EnvironmentSpacePolicyChanged`
-   `TracePublished`
-   `TraceSuperseded`
-   `TraceQuarantined`
-   `SubscriptionCreated`
-   `SubscriptionPaused`
-   `SubscriptionRevoked`
-   `TaskClaimAcquired`
-   `TaskClaimRenewed`
-   `TaskClaimExpired`
-   `TaskClaimReleased`
-   `ArtifactBound`
-   `ArtifactVerificationRecorded`
-   `GovernanceContextEvaluated`

### 7.2 复用既有事件，不重复注册 {#72-复用既有事件不重复注册}

-   `RevocationIssued`
-   `ReconciliationCompleted`
-   `HumanOverride`
-   `DataUseGrantRevoked`
-   `ExecutionReceiptPublished`
-   `AcceptanceRecorded`
-   `LeaseReleased`
-   `TaskCancellationConfirmed`

事件信封至少包含 `id`、`source`、`type`、`subject`、`time`、`dataschema`
和 `data`。事件载荷引用 AEE/ASCP
Schema。事件是发生事实的记录；查询端可建立当前状态投影，但不得回写或覆盖原始事件。

## 8. A2A 扩展映射 {#8-a2a-扩展映射}

A2A 核心协议保持不变。AEE 扩展 URI 必须由 ADS 治理域正式持有；下列
`example.invalid` 仅为占位符。

### 8.1 Agent Card {#81-agent-card}

扩展声明放入 `AgentCard.capabilities.extensions`。扩展 URI
应包含版本；破坏性变化必须发布新的
URI。若扩展声明为必需而对端不支持，交互必须失败，不得静默降级。

### 8.2 Message 与 Artifact {#82-message-与-artifact}

Message/Artifact 使用扩展 URI 声明和 URI 命名空间下的 metadata 承载
`environment_ref`、`trace_refs`、`artifact_binding_ref` 和
`governance_context_ref` 等引用。

### 8.3 Task {#83-task}

A2A Task 使用 `metadata[extension_uri]` 承载
`global_task_ref`、`sco_task_run_ref`、`task_claim_lease_ref` 和
`environment_ref`。A2A Task ID 与算力底座 GlobalTaskId / SCO TaskRun ID
必须保留映射关系，不得假设三者相同。

A2A Artifact ID 可能只在其 Task 范围内唯一；必须另存 Artifact Registry
的全局 `artifact_ref` 和版本。

## 9. API 职责映射 {#9-api-职责映射}

  接口域          主要操作                                     权威边界
  --------------- -------------------------------------------- --------------------------------
  ADS API         环境目录、Profile、能力/语义注册、策略评估   ADS 不替 Owner 批准数据使用
  SCO API         任务依赖、认领、续租、提交、验收编排         SCO 管任务，不签发物理资源租约
  FWSX            痕迹投影、订阅事件、跨站点同步、对账         不成为全局事实库
  A2A             Agent 发现、消息、任务交互、Artifact 交接    不取代 SCO TaskRun
  Owner/LCP/PEP   本地数据授权、资源租约、执行回执和访问门禁   本地权威不可被 ADS 接管

### 9.1 候选 API 操作映射

| API 域 | 方法与路径（候选） | 操作 | 关键约束 |
|---|---|---|---|
| ADS | `GET /ads/v1/environment-spaces` | 查询环境空间目录 | 仅返回授权元数据投影 |
| ADS | `POST /ads/v1/environment-spaces:register` | 注册空间目录项 | 空间 Owner 证明权属；注册不授予访问权 |
| FWSX | `POST /fwsx/v1/traces` | 发布痕迹 | Schema、来源、策略、幂等和速率门禁 |
| FWSX | `GET /fwsx/v1/traces/{trace_id}` | 读取痕迹 | 每次读取重新鉴权 |
| FWSX | `POST /fwsx/v1/traces:query` | 条件查询 | 强制按空间、领域、分类和目的过滤 |
| FWSX | `POST /fwsx/v1/subscriptions` | 创建订阅 | 订阅不等于读取授权 |
| FWSX | `GET /fwsx/v1/subscriptions/{subscription_id}/events` | 拉取事件 | 游标持久化、至少一次投递 |
| SCO | `POST /sco/v1/tasks/{task_id}:claim` | 任务认领 | CAS、claim_epoch、fencing_token |
| SCO | `POST /sco/v1/task-claim-leases/{lease_id}:heartbeat` | 认领续租 | 当前 holder、token、最大租期校验 |
| SCO | `POST /sco/v1/task-claim-leases/{lease_id}:release` | 释放任务认领 | 旧 token 失效；不代表释放物理资源 |
| Artifact Registry | `POST /artifact-registry/v1/bindings` | 创建成果绑定 | 不复制成果正文；校验版本和摘要 |
| Artifact Registry | `GET /artifact-registry/v1/bindings/{binding_id}` | 查询成果绑定 | 引用解析时重新鉴权 |
| ADS / Policy | `POST /ads/v1/governance-contexts:evaluate` | 生成治理上下文引用 | 返回策略决策引用；本地 PEP 仍需重验 |

以上路径为接口设计候选，不代表服务已存在。所有写请求应支持 `Idempotency-Key`；聚合对象更新应携带 `If-Match` 或等价版本号。错误响应至少包含 `error_code`、`category`、`retryable`、`safe_action`、`correlation_id` 和 `policy_version`。

## 10. 安全与失效控制 {#10-安全与失效控制}

  风险               强制控制
  ------------------ ---------------------------------------------
  痕迹投毒           来源认证、隔离区、独立验证、速率限制
  重放与重复副作用   稳定事件 ID、幂等键、Inbox、目标系统对账
  越权读取           每次引用解析重新鉴权；字段级投影
  双重认领           CAS、租约、单调 fencing token
  旧执行者写入       拒绝旧 fencing token；必要时对账
  订阅泄漏           目的绑定、字段过滤、短期授权、撤销
  事件循环           因果深度、最大任务数、预算、冷却和死信
  策略服务不可用     高风险动作 fail-closed
  RSI 越权           候选生成与评估分离；Shadow/Canary/审批/回滚
  语义不兼容         Profile 兼容矩阵；未知动作和权限默认拒绝

## 11. 验收矩阵 {#11-验收矩阵}

  编号        测试                   通过条件
  ----------- ---------------------- --------------------------------------------------------------
  AEE-AT-01   六类对象 Schema 校验   合法样例通过；缺失必填字段和非法枚举被拒绝
  AEE-AT-02   Ontology 映射          不重复创建 TaskRun、ResourceLease、Artifact 等既有权威实体
  AEE-AT-03   A2A 扩展协商           Agent Card 声明与 Message/Artifact metadata 可互操作
  AEE-AT-04   A2A Task 映射          A2A Task ID、GlobalTaskId、SCO TaskRun ID 可双向追踪但不混同
  AEE-AT-05   并发认领               两个 Agent 同时认领同一阶段，仅一个有效
  AEE-AT-06   旧租约提交             旧 fencing token 被拒绝
  AEE-AT-07   重复投递               同一事件重复 10 次不产生重复业务副作用
  AEE-AT-08   撤销授权               撤销后新的敏感读取被拒绝
  AEE-AT-09   网络分区恢复           本地低风险自治保持；跨域高风险动作挂起；恢复后对账
  AEE-AT-10   策略服务故障           高风险动作 fail-closed
  AEE-AT-11   Artifact 版本冲突      保留父版本，显式创建新版本，不静默覆盖
  AEE-AT-12   循环触发               达到预算/深度上限后停止扩散并留痕

所有通过结果必须有测试运行 ID、Schema
版本、测试主体、时间、证据引用和独立验收记录。当前这些是验收要求，不代表已经完成测试。

## 12. 待架构委员会确认的决策 {#12-待架构委员会确认的决策}

1.  AEE/ASCP 正式治理域 URI 与命名空间。
2.  Agent、环境、痕迹、任务认领和成果的 ID 生成与租户隔离规则。
3.  签名算法、密钥轮换、签名覆盖字段和时间戳信任策略。
4.  订阅投递的默认模式、回放窗口、游标保留和死信责任主体。
5.  TaskClaimLease 的默认租期、续租上限和 fencing token 权威存储。
6.  环境空间的保留期限、审计留存和跨域数据驻留要求。
7.  AEE 与 Ontology V3.0 RC0 的兼容 Profile 及迁移窗口。

## 13. 本版状态结论 {#13-本版状态结论}

**已继承：** V1.2 的
ST-01---ST-05、七类痕迹、任务状态机、Outbox/Inbox、PDP/PEP、RSI
受控发布原则。

**本版新增候选：** 六个对象的 Schema、Ontology 映射、AEE
事件增量目录、A2A 扩展映射和 12 项验收用例。

**尚未确认：** 治理域
URI、签名配置、具体传输绑定、租期参数和生产保留策略。

**禁止标记为：** 正式冻结、生产可用、互操作已通过或性能已达标。

------------------------------------------------------------------------

## 附录 A：建议文件清单

-   `AEE_ASCP_V1.0_RC0_接口与数据契约评审稿.md`
-   `schemas/AEE_ASCP_V1.0_RC0.schema.json`
-   `mappings/Ontology_V3_AEE映射矩阵.csv`
-   `mappings/AEE事件扩展目录.csv`
-   `examples/A2A_AEE_Extension_示例.json`
-   `MANIFEST_SHA256.txt`

## 附录 B：规范参考

-   A2A Protocol：Agent Card、Message、Task、Artifact 与 Extensions
    官方规范。
-   JSON Schema Draft 2020-12。
-   算力底座 V2.3 Ontology V3.0 数据字典（RC0 候选）。
-   算力底座 DM04 事件目录与 Schema 契约。
-   环境驱动型多 Agent 协作架构研究报告 V1.2。
