# 算力底座｜G1 Ontology 与协议契约一致性报告

**日期：** 2026-11-10\
**关联基线：** Ontology
V3.0（V2.2详细架构）；V2.9-RC9.2-DM04-IFC0.1；AEE/ASCP
V1.1.0-RC0；ADS/SCO OpenAPI RC0\
**阶段：** G1-01 至 G1-04 候选设计\
**状态：**
已形成字段映射与问题清单；待Owner评审、签署、Schema工具链验证和双实现互操作\
**性质：** 纯架构研究，不包含工程实现代码

------------------------------------------------------------------------

## 0. 执行结论 {#0-执行结论}

本轮形成四个G1工作包的候选成果：

-   G1-01：DM04 IFC0.1与ADS/SCO OpenAPI RC0字段兼容矩阵。
-   G1-02：AEE/ASCP六对象逐字段Ontology/DM04映射及Ontology缺口清单。
-   G1-03：A2A 1.0、CloudEvents 1.0.2、FWSX协议分层矩阵。
-   G1-04：DM04 48项 + AEE/ASCP 18项 = 66项双站点互操作验收总矩阵。

当前所有66项测试仍为待执行。本报告不声称接口已正式冻结、Owner已签署或双站点互操作已通过。

## 1. G1-01：DM04与ADS/SCO Envelope一致性 {#1-g1-01dm04与adssco-envelope一致性}

### 1.1 关键发现 {#11-关键发现}

DM04
IFC0.1统一请求契约要求：`request_id`、`correlation_id`、`caller_principal`、`workload_identity`、`audience`、`purpose`、`protocol_profile`、`issued_at`、`expires_at`。有副作用操作需`idempotency_key`；状态变更需`expected_state_version`；高风险操作需`payload_digest`与`signature_ref`。

ADS/SCO OpenAPI
RC0的RequestEnvelope当前必需字段主要为：`request_id`、`correlation_id`、`issued_at`、`api_version`、`schema_version`、`payload`。其字段中有`caller_workload_id`、`participant_id`、`tenant_id`、`expires_at`、`payload_digest`等，但多个字段不是必需项，且没有完整表达DM04所要求的主体、Audience、Purpose和Protocol
Profile。

因此，二者存在语义与必需性差异，不能直接视为同一契约。

### 1.2 对齐原则 {#12-对齐原则}

1.  保留ADS/SCO现有`api_version`、`schema_version`和`payload`；它们与DM04安全上下文字段是不同维度。
2.  IFC0.2候选明确对齐`caller_principal`、`workload_identity`、`audience`、`purpose`、`protocol_profile`、`expires_at`。
3.  `caller_workload_id`不能自动替代完整`workload_identity`；`participant_id`不能推断`caller_principal`。
4.  状态变更显式绑定`expected_state_version`；高风险请求摘要覆盖扩展块并关联`signature_ref`。
5.  响应中区分`command_status`与`authoritative_state`。Accepted/Pending/Unknown均不能被误判为业务成功。
6.  补齐`responder_site_id`、`object_ref`、`object_version`、`event_cursor`、`evidence_refs`等响应字段。

### 1.3 兼容决策 {#13-兼容决策}

IFC0.2应作为显式候选版本，经双方API Owner与Security
Owner签署后启用。未对齐安全上下文的跨站点高风险操作不得通过隐式推断放行。既有IFC0.1本地操作不应被无故破坏。

## 2. G1-02：六对象逐字段映射 {#2-g1-02六对象逐字段映射}

### 2.1 映射类型 {#21-映射类型}

-   直接映射：使用Ontology V3.0已有核心实体/关系。
-   关联投影：AEE/ASCP对象只保存既有权威对象引用，不创建新权威库。
-   Profile/Runtime扩展：为缺失语义定义受控扩展，但仍由既有Domain
    Owner负责。

### 2.2 六对象的目标映射 {#22-六对象的目标映射}

  AEE/ASCP对象                 Ontology V3.0映射                                                             规范定位                  禁止事项
  ---------------------------- ----------------------------------------------------------------------------- ------------------------- ----------------------------------
  EnvironmentSpaceDescriptor   Participant、TrustDomain、Site、DataProduct、OntologyProfile、PolicyProfile   非权威组合描述符          不建第二成员名册/信任根/数据空间
  TraceRecord                  CloudEvents + TaskRun、PolicyDecision、Incident等                             事件语义投影              不建第二事件库、不双写事件ID
  EnvironmentSubscription      Principal、DataUseGrant、PolicyDecision + FWSX运行时订阅                      授权下的投递资源          不把游标当事实、不扩大字段投影
  TaskClaim                    TaskStage、TaskRun、PolicyDecision                                            本地TaskStage认领子记录   不等同ResourceLease/FencingToken
  ArtifactBinding              EvidenceRecord、ResultRef、OutputArtifactRef、AcceptanceRecord                成果/证据关联             不建第二Artifact Registry
  GovernanceContextRef         Principal、PolicyDecision、DataUseGrant、DelegationGrant                      请求级上下文引用          不成为Bearer Token或全局PDP

### 2.3 Ontology缺口 {#23-ontology缺口}

V3.0实体清单需处理ParticipantBinding、TrustAgreement、DataSpaceContract、DelegationGrant、HumanApproval、OutputArtifact、Result等概念缺口。

这些概念不应全部升级为Core实体：

-   Governance/Security
    Profile：ParticipantBinding、TrustAgreement、DelegationGrant、HumanApproval。
-   Data Space Profile：DataSpaceContract。
-   Evidence/Result Profile：OutputArtifactRef、ResultRef。
-   Runtime Schema：EventSubscription、TaskClaim。
-   AEE/ASCP
    DTO/关联投影：EnvironmentSpaceDescriptor、ArtifactBinding、GovernanceContextRef、TraceRecord。

其中OutputArtifact在V3.0关系中被引用但未列入核心实体；Result在DM04有独立生命周期而在V3.0实体清单中缺失。这是必须关闭的本体一致性问题。

## 3. G1-03：协议兼容 {#3-g1-03协议兼容}

### 3.1 CloudEvents {#31-cloudevents}

复用CloudEvents 1.0.2信封：

-   id → trace_id
-   source → source/issuer
-   type → trace_type
-   subject → subject_ref
-   time → occurred_at
-   dataschema → payload_schema_ref
-   data → payload

DM04扩展siteid、aggregateid、aggregateversion、sequence、correlationid、causationid、signature_ref。事件顺序只保证单一权威聚合内单调，不承诺跨联邦全局总序。

建议在ASCP事件Profile显式增加epistemic_status：fact/inference/proposal/decision。缺失或冲突时不能把模型推断升级为事实。

### 3.2 FWSX {#32-fwsx}

FWSX负责投递、游标、重试、重放、积压和跨站点传输；事件源Owner决定订阅是否获准；目标站点PDP/PEP复核；Artifact引用读取再次授权。

采用至少一次投递、Inbox幂等消费和cursor补拉，不承诺网络恰好一次投递。

### 3.3 A2A {#33-a2a}

-   AgentCard
    `capabilities.extensions[]`声明扩展URI、description、required、params。
-   请求级`A2A-Extensions`激活扩展；未协商激活的必需扩展不得执行副作用。
-   Message与Artifact使用扩展URI及metadata。
-   Task仅用metadata承载AEE引用，不添加核心协议未定义的Task.extensions\[\]。
-   A2A Task ID与SCO TaskRun ID建立可追踪映射，不强行合并。
-   A2A Task状态不能覆盖DM04
    Prepare、PartialCommit、UNKNOWN、Acceptance、Settlement等业务状态。

## 4. G1-04：66项验收体系 {#4-g1-0466项验收体系}

继承DM04原48项接口互操作测试，并叠加AEE/ASCP
18项增量测试，形成66项统一验收总表。编号、优先级、环境、预期结果、状态、验收证据和执行记录均保留。

建议分为四道测试门：

-   Gate A：契约与Schema（请求信封、字段、版本、签名、幂等）。
-   Gate B：Ontology与对象权威（引用、版本、Owner、状态、映射）。
-   Gate C：协议互操作（CloudEvents、FWSX、A2A、重复/乱序/撤销）。
-   Gate D：双站点故障与恢复（WAN分区、UNKNOWN、Saga、回滚、双实现）。

P0未全部通过不得进入正式互操作验收；任何未授权数据访问、非Owner签发Lease、旧FencingToken执行、未知权限默认放行均为零容忍。

## 5. G1候选决策 {#5-g1候选决策}

-   ADR-G1-01：AEE/ASCP六对象与Ontology V3.0映射原则。
-   ADR-G1-02：DM04与ADS/SCO Request/Response Envelope对齐。
-   ADR-G1-03：A2A、CloudEvents与FWSX协议分层。

以上均为Proposed，待Owner评审与签署。

## 6. 当前状态 {#6-当前状态}

已生成：

-   6对象字段级映射表（逐字段）。
-   Ontology缺口与修订建议。
-   IFC0.1与ADS/SCO OpenAPI兼容矩阵。
-   ResponseEnvelope状态语义交叉表。
-   A2A/CloudEvents/FWSX协议兼容矩阵。
-   66项双站点互操作验收总矩阵。
-   3份ADR、Word/Markdown报告和架构图。

未完成：

-   Ontology Owner批准新增/补齐的Profile语义。
-   DM04 API Owner批准IFC0.2字段与响应状态对齐。
-   A2A/CloudEvents/FWSX Profile Owner签署。
-   Schema/OpenAPI/A2A工具链验证。
-   双实现互操作与真实双站点故障注入。

**准确状态：G1一致性设计候选稿已形成；尚未冻结正式契约，66项测试全部待执行。**
