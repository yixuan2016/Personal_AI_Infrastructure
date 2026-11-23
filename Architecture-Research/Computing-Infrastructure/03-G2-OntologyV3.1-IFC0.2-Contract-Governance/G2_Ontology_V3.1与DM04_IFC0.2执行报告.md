# 算力底座 G2 执行报告
## Ontology V3.1 × DM04 IFC0.2 × ADS/SCO REST Binding

**日期：** 2026-11-10  
**阶段：** G2-01 / G2-02 完成候选设计，G2-03 启动  
**状态：** Proposed / RC0，待 Owner 评审签署  
**工作边界：** 纯架构研究与契约设计，不编写工程实现代码

## 0. 执行结论

本轮基于 Ontology V3.0、DM04 IFC0.1、ADS/SCO OpenAPI 3.2.1 RC0、AEE/ASCP V1.1-RC0 与 G0 治理备忘录，形成：
1. Ontology V3.1.0-RC0 核心实体和 Profile 修订候选；
2. DM04 IFC0.2 只增加可选 `profile_extensions` 的契约增量；
3. G1 勘误，撤回 IFC0.2 顶层增加身份字段的错误建议；
4. ADS/SCO REST Binding 缺口与逻辑 RequestEnvelope 映射；
5. AEE/ASCP 与六域 API 职责绑定初稿；
6. 6 份 JSON Schema / 增量 Schema、请求/响应样例、实体/关系/接口矩阵、2 份 ADR 和架构图。

## 1. G1 勘误：IFC0.2 不改变 IFC0.1 必需字段

既有 G0 已明确：IFC0.2 仅提出可选 `profile_extensions`，不改变 IFC0.1 已有必需字段；双方签署前不得发送扩展。G1 曾建议把 caller_principal、workload_identity、audience、purpose、protocol_profile 等作为 IFC0.2 顶层必需字段，该建议与G0不一致，现正式撤回。

## 2. 新发现：ADS/SCO REST Binding 存在组件未绑定

源文件核查：
- ADS OpenAPI 3.2.1 RC0：RequestEnvelope 组件 Path 引用 0 次；GenericCommand 引用 24 次。
- SCO OpenAPI 3.2.1 RC0：RequestEnvelope 组件 Path 引用 0 次；GenericCommand 引用 22 次。
- 两份 GenericCommand required 均为 request_id、correlation_id、issued_at、api_version、schema_version；payload 可选。
- 两份 RequestEnvelope required 均为上述字段再加 payload。
- RequestEnvelope 与 GenericCommand 的字段集合和必需性并不一致。
- DM04 参考 REST Binding 使用 OpenAPI 3.1.1，而 ADS/SCO 文件声明 3.2.1；工具链共同版本尚未验证。

因此，逻辑 RequestEnvelope 与 REST body 必须通过明确 Binding Profile 连接，不能仅靠同名组件推断一致。

## 3. DM04 IFC0.2 的正确范围

IFC0.2 只增加可选 `profile_extensions`：
- URI Key：注册的 Profile URI；
- profile_version；
- schema_ref；
- criticality（位于扩展包装层）；
- payload_digest（针对该 Profile data）；
- data（按 schema_ref 校验）。

AEE Context data 只携带环境、本体、Trace、Subscription、TaskClaim、ArtifactBinding、GovernanceContext 的引用；不携带授权凭证、Bearer Token、资源Lease、FencingToken、原始数据或Artifact正文。criticality 不重复放进 AEEContext data。

## 4. 逻辑 RequestEnvelope 的 REST 安全映射

- caller_principal：由目标服务验证 OAuth2 主体及信任映射产生。
- workload_identity：由已验证 workload、OAuth2 client 与按需 mTLS 绑定产生；caller_workload_id 仅作声明性提示。
- audience：由经过验证的 Token aud 与服务注册资源标识匹配，不从 URL 猜测。
- purpose：从显式操作目的及 TaskContract / DataSpaceContract / DataUseGrant 解析；reason 不等于 purpose。
- protocol_profile：双方已协商、已登记的 Profile；不从 api_version/schema_version 推断。
- expires_at：复用已有可选字段，但联邦请求必须校验。
- idempotency_key：副作用操作必需；header/body 同时存在必须一致。
- expected_state_version：通过 If-Match / ETag 映射；状态更新必须有并发版本约束。
- payload_digest：高风险操作必需；签名覆盖规范化请求与 profile_extensions。
- signature_ref：由已验证的签名/证明上下文提供，不放入 AEE data。

## 5. ResponseEnvelope 缺口

当前 Operation 只有 operation_id、status、accepted_at、status_url、retry_after_seconds、result_ref、error_ref；它不能单独代表 DM04 ResponseEnvelope。REST Binding RC1 需独立定义 ResponseContext，将命令处理状态与业务对象权威状态分离。Accepted 只表示受理；Unknown 必须对账，不盲目重放。

## 6. Ontology V3.1 候选决策

### 6.1 Core 新增四项
- OutputArtifact：不可变成果引用与摘要，不建第二Artifact Registry。
- Result：业务结果与披露生命周期，不替代独立AcceptanceRecord。
- DelegationGrant：主体委托链、Audience、Actions、Scope、Purpose、Expiry与撤销。
- HumanApproval：绑定精确Subject Digest、Scope、Approver、Decision、Expiry和Evidence。

### 6.2 Profile 新增三项
- ParticipantBinding、TrustAgreement：Federation Governance Profile。
- DataSpaceContract：Data Space Profile，和DataUseGrant明确分离。

### 6.3 保留为 Runtime / Projection
EventSubscription、TaskClaim、EnvironmentSpaceDescriptor、TraceRecord、ArtifactBinding、GovernanceContextRef 不进入 Core。

## 7. ADS / SCO / 六域边界

ADS 负责联邦治理协调、共同语义与Profile注册、能力发现、跨域治理视图和智能生态协调；保留自身执行、管理、考核与成长闭环。SCO 负责全局 TaskContract / ContractGraph / Plan / Saga / ActivationBarrier / 对账。站点本地 IAM/PDP/PEP、TaskClaim、ResourceLease、FencingToken、数据披露、证据与独立验收权威不转移。

## 8. 质量验证

本包执行了 JSON Schema Draft 2020-12 Schema 自身结构检查，并对请求扩展、AEE Context、ResponseContext 正反样例做了验证。该验证只证明本次候选 Schema 与样例内部一致，不等于 OpenAPI 工具链验证、双实现互操作或真实双站点测试。

## 9. 待评审与放行条件

1. Ontology Owner 批准 Core 新增实体及关系。
2. Evidence/Acceptance Owner 确认 OutputArtifact / Result / Acceptance 边界。
3. IAM/Security Owner 确认 DelegationGrant / HumanApproval 规则。
4. DM04、ADS、SCO、Security、AEE/ASCP Profile Owner 共同评审 IFC0.2 和 REST Binding RC1。
5. 正式控制域名、URI Namespace Owner 和签署台账完成注册。
6. 选定双方工具链共同支持的 OpenAPI 版本。
7. IFC0.1 回归、IFC0.2 双端协商、负向安全测试、双实现互操作通过。
8. 真实双站点故障注入、UNKNOWN 对账、撤销传播、回滚和证据链验收完成。

**准确状态：G2-01 / G2-02 候选设计已形成；G2-03 已形成初稿。尚未正式冻结、未部署、未完成双实现互操作，未推送 GitHub。**
