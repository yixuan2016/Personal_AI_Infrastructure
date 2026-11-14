# Ontology V3.1.0-RC0 核心本体修订提案

**日期：** 2026-11-10  
**基线：** Ontology V3.0（算力底座 V2.2 详细架构）  
**状态：** Proposed / RC0，待 Ontology Owner、六域 Owner 与架构委员会评审  
**变更类型：** Minor 候选；只增加概念和约束，不重命名、不删除 V3.0 核心实体或关系

## 1. 修订目标

V3.0 已覆盖主体、地理、算力、网络、存储、内存、能源、能力、任务、信任、授权、数据、证据与治理，并确立稳定 URI、版本、来源和事件语义。G1 发现 OutputArtifact 在关系中被引用但未列入核心实体，DM04 又有 Result 生命周期操作；同时 DelegationGrant 与 HumanApproval 缺少明确的独立对象表达。

V3.1 的目标是补齐这些跨域语义，不把 AEE/ASCP 的运行时 DTO 变成新的 Core 实体。

## 2. Core 新增实体（四项）

| 新增实体 | 归属 | 核心作用 | 与既有对象的边界 |
|---|---|---|---|
| OutputArtifact | Core / Evidence | 描述任务产出的不可变成果引用、版本、摘要、生产者、来源和分类 | 不等同 EvidenceRecord；不新建 Artifact Registry；正文仍归 Artifact Owner |
| Result | Core / Evidence | 表达任务结果的业务状态、成果引用、证据引用和披露状态 | 不等同 AcceptanceRecord；接受结论由独立验收方签发 |
| DelegationGrant | Core / Trust & Authorization | 表达主体代表另一主体执行的委托链、受众、动作、范围、用途和期限 | 不等同 DataUseGrant 或 ResourceLease |
| HumanApproval | Core / Governance | 绑定具体对象摘要、审批人、范围、决定、条件、期限与证据 | 不替代 PDP/PEP、资源 Owner 决定或独立验收 |

## 3. Domain Profile 新增概念（三项）

### 3.1 Federation Governance Profile

- `ParticipantBinding`：Participant 与 TrustDomain / Federation 的可撤销绑定记录。Participant 本身仍由原 Participant Owner 管理。
- `TrustAgreement`：双方签署的信任协议，定义适用参与方、协议 Profile、允许范围、义务、有效期和撤销引用。它不是 TrustDomain 的别名。

### 3.2 Data Space Profile

- `DataSpaceContract`：数据产品/数据集版本、提供方、使用方、用途、动作、地域、保留、转授权、删除和审计义务的签署合同。
- `DataUseGrant` 仍是具体主体、具体动作和具体用途的访问授权；合同存在不等于当前访问自动获准。

## 4. 运行时对象与投影对象（不进入 Core）

| 概念 | 归属 | 处理 |
|---|---|---|
| EventSubscription | FWSX Runtime | 投递订阅状态与游标，不代表数据授权 |
| TaskClaim | Site Runtime / TaskStage Profile | 本地阶段认领，不等同 ResourceLease 或 FencingToken |
| EnvironmentSpaceDescriptor | AEE/ASCP DTO | 组合权威引用的非权威视图 |
| TraceRecord | CloudEvents ASCP Projection | 事件信封与领域事实投影，不建第二事件库 |
| ArtifactBinding | Evidence/Result Association | 关联 Artifact / Result / Evidence，不建全局 Registry |
| GovernanceContextRef | Request-scoped Profile | 请求上下文引用，不是 Bearer Token 或全局 PDP |

## 5. 核心关系增量

1. `TaskRun PRODUCES OutputArtifact`。
2. `TaskRun PRODUCES Result`。
3. `Result REFERENCES OutputArtifact`（0..N）。
4. `Result SUPPORTED_BY EvidenceRecord`（1..N，按结果类型定义最小证据要求）。
5. `AcceptanceRecord EVALUATES TaskRun / Result / OutputArtifact`。
6. `Result RELEASED_BY PolicyDecision`；披露仍需 Result Owner 与目标站点 PEP 授权。
7. `DelegationGrant DELEGATES_FROM Principal TO Principal`，并关联 Audience、Scope、Purpose、有效期和签署证据。
8. `HumanApproval APPROVES_OR_REJECTS SubjectRef`，必须绑定 Subject Digest、Scope、Policy Version 和 Expiry。
9. `ParticipantBinding BINDS Participant TO TrustDomain/Federation`。
10. `TrustAgreement AGREES_BETWEEN Participant`（双边或多方），并引用双方签署证据。
11. `DataSpaceContract COVERS DataProduct / DatasetVersion`，并约束后续 DataUseGrant。

## 6. 公共元数据与权威引用规则

所有持久化权威对象至少应表达：
- 稳定 `id`（URI/URN，不使用易变名称作为主键）；
- 不可变 `version`；
- `schema_version` 与 `ontology_profile_ref`；
- `issuer_ref` / `owner_ref`；
- `created_at`，必要时 `updated_at`；
- `source_ref` / `provenance_ref`；
- 适用对象的 `content_digest`、`signature_ref`、`valid_from`、`valid_until`、`revocation_ref`。

`owner_ref` 必须指向可解析的权威主体，并声明 `authority_scope`；显示名、租户名或单纯 `participant_id` 不得充当 Owner 证明。对象的 Owner 仍由六域权威矩阵决定，不因 ADS 聚合展示而转移。

## 7. 事件事实与认知状态分离

事件的 `event_category` 与 `assertion_kind` 分开：
- `event_category`：ObservedEvent、ProjectionEvent、ForecastEvent、CounterfactualEvent、ProposalEvent、DecisionEvent、ExecutionEvent、RiskEvent、GovernanceEvent、FederationEvent。
- `assertion_kind`：`fact`、`inference`、`forecast`、`counterfactual`、`proposal`、`decision`。

例如 ForecastProduced 可以是 ForecastEvent + forecast；ExecutionCompleted 应是 ExecutionEvent + fact。未知或冲突的 assertion_kind 不得升级为事实，不得触发资源承诺、授权、计量或结算。

## 8. 版本与迁移

- 版本建议：`3.1.0-rc0`，不是正式发布。
- V3.0 Core 实体 ID、既有关系和既有字段保持不变。
- 新增实体/关系为兼容增量；不改变既有必需字段语义。
- V3.0 对象迁移到 V3.1 时，旧对象仍可由 V3.0 Profile 解析；新增字段缺失不得被推断为已审批、已委托或已发布。
- 新 Profile URI 只有在项目受控域名、Schema URI、Owner、Digest、签署和兼容窗口登记后才能启用。当前域名未确认，本文 URI 均为命名模板。
- V3.1 RC0 通过语义评审、Schema 校验、映射回归和双实现解析测试后，才能申请 RC1。

## 9. 不在本次修订范围

不引入第二套 Participant Registry、Trust Registry、PDP、Lease Authority、事件总线或 Artifact Registry；不改变六域划分；不改变 ADS/SCO/站点的既有责任边界；不定义工程数据库表或实现代码。
