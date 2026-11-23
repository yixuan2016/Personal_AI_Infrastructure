# DM04 IFC0.2 与 ADS/SCO REST Binding 对齐提案

**日期：** 2026-11-10  
**基线：** V2.9-RC9.2-DM04-IFC0.1；ADS/SCO OpenAPI 3.2.1 RC0；AEE/ASCP V1.1-RC0；G0 架构评审  
**状态：** Proposed；不代表双方批准或正式冻结  
**范围：** 纯架构契约研究，不编写工程实现代码

## 1. 关键决策

**IFC0.2 的 DM04 增量仍仅为可选 `profile_extensions`。** 不增加新的 IFC0.1 顶层必需字段，不改变既有业务状态机和幂等语义。G1 曾提出的顶层安全字段补齐建议已由《G1 勘误与契约基线校正》撤回。

IFC0.2 扩展包装结构：
- URI Key：双方登记的 Profile URI；
- `profile_version`：Profile 语义版本；
- `schema_ref`：Profile Schema URI；
- `criticality`：`required` / `optional`，属于扩展控制包装层；
- `payload_digest`：当前 Profile `data` 的规范化摘要；
- `data`：按 `schema_ref` 验证的 Profile 数据，只放引用和允许的扩展元数据。

AEE Context 的 `data` 不得重复放置 `criticality`，不得携带 Grant/Bearer Token、ResourceLease、FencingToken、原始数据或 Artifact 正文。

## 2. 源文件核查结果

ADS OpenAPI RC0 与 SCO OpenAPI RC0 均定义 `RequestEnvelope`，但 Path 未引用该组件；实际有 24 个 ADS Path 和 22 个 SCO Path 引用 `GenericCommand`。两份 `GenericCommand` 均要求五个字段（request_id、correlation_id、issued_at、api_version、schema_version），而 `payload` 是可选；`RequestEnvelope` 则要求六个字段并要求 `payload`。

因此存在 REST Binding 组件未绑定和 Schema 语义重复的问题。该问题属于 ADS/SCO REST Binding RC1 的整理事项，不能用改变 IFC0.2 的方式掩盖。

## 3. 逻辑 RequestEnvelope 到 REST 的安全绑定

| 逻辑字段 | REST / 安全上下文映射 | 约束 |
|---|---|---|
| request_id | GenericCommand.request_id | 必须存在并回显 |
| correlation_id | GenericCommand.correlation_id | 全链路一致 |
| issued_at | GenericCommand.issued_at | UTC RFC3339；校验时钟偏差 |
| api_version | GenericCommand.api_version | API 版本，不代表 Profile |
| schema_version | GenericCommand.schema_version | Runtime Schema 版本，不代表 Ontology |
| payload | GenericCommand.payload / operation-specific body | 对现有端点保持兼容；RC1 统一具体载荷 Schema |
| caller_principal | 由目标服务验证 OAuth2 主体及受信任身份映射生成 | 不信任 body 中自报 principal |
| workload_identity | 由已验证 workload 身份、OAuth2 client 与按协议要求的 mTLS 绑定生成 | caller_workload_id 仅为声明，必须与验证结果一致 |
| audience | 由已验证访问令牌 audience 与服务注册资源标识匹配 | 不得仅从 URL 推断 |
| purpose | 从显式操作目的及 TaskContract / DataSpaceContract / DataUseGrant 的权威引用解析 | reason 不等于 purpose；无法解析则拒绝敏感操作 |
| protocol_profile | 来自双方已协商、已登记的协议/Profile 会话 | 不得从 api_version 或 schema_version 推断 |
| expires_at | 复用现有可选 expires_at | 联邦请求必须校验有效期；不得缺省延长 |
| idempotency_key | 统一采用已定义的 Idempotency-Key 或 body 字段 | 两者同时出现必须相等；副作用操作必需 |
| expected_state_version | REST 条件请求 If-Match / 强 ETag，映射到目标对象版本 | 更新/状态变更必需；创建操作按操作契约处理 |
| payload_digest | 现有 payload_digest | 高风险写操作必需；签名覆盖规范化请求与扩展 |
| signature_ref | 已验证签名/证明上下文中的证据引用 | 不把签名算法或凭证塞入 Profile data |
| profile_extensions | IFC0.2 可选扩展字段 | 双端协商、注册、验 Schema、验 Digest 后才可用 |

## 4. 请求处理顺序

1. 解析 API / Schema / Profile 版本，检查双方支持能力。
2. 验证 OAuth2 Token、Issuer、Audience、主体、工作负载身份及按信任协议要求的 mTLS 绑定。
3. 解析请求目的并绑定合同/Grant；无法解析或与权威对象不一致时拒绝。
4. 校验 expires_at、幂等键、expected_state_version、payload_digest 和签名证据。
5. 若包含 profile_extensions，逐 URI 检查注册状态、版本、criticality、Schema 和摘要。
6. 对每个被引用的对象在目标站点本地 PDP/PEP 重新授权。
7. 只有所有前置门禁满足后，才进入业务副作用阶段。
8. 超时且可能已产生副作用时返回 Unknown / ReconciliationRequired，先查询权威状态，不盲目重放。

## 5. 响应契约与 REST Binding 缺口

DM04 逻辑 ResponseEnvelope 要求 `request_id`、`responder_site_id`、`object_ref`、`object_version`、`command_status`、`authoritative_state`、`event_cursor`、`evidence_refs`。

当前 ADS/SCO `Operation` 只包含 `operation_id`、`status`、`accepted_at`、`status_url`、`retry_after_seconds`、`result_ref`、`error_ref`；没有完整实现逻辑 ResponseEnvelope。Operation.status 是命令处理状态，不是业务对象状态。

建议 ADS/SCO REST Binding RC1 定义独立 `ResponseContext`：
- `request_id`、`responder_site_id`；
- `object_ref`、`object_version`；
- `command_status`（与 Operation.status 映射）；
- `authoritative_state`（包含 authority_ref、state_value、state_version、as_of、freshness）；
- `event_cursor`、`evidence_refs`。

`ResponseContext` 属于 Response Binding 整理，不属于 IFC0.2 的 `profile_extensions`。Accepted 只表示受理；Running / WaitingForApproval 表示处理中；Succeeded 仍需关联对象权威状态和证据；Unknown 必须对账。

## 6. API 文档版本治理

当前 ADS/SCO 文件声明 OpenAPI 3.2.1；DM04 冻结候选包的参考 REST 绑定采用 OpenAPI 3.1.1，并明确 3.2.1 工具链尚待验证。G2 不预先宣称任何版本已通过工具链。应使用同一套 Parser、Validator、Generator 与两套独立实现做对照，选定双方实际支持的共同版本。

## 7. 兼容与发布规则

- IFC0.1：继续作为既有兼容候选基线。
- IFC0.2：只增加可选 `profile_extensions`；双方 API Owner、Security Owner、AEE/ASCP Profile Owner 签署前不得发送。
- ADS/SCO REST Binding RC1：解决 RequestEnvelope 未引用、GenericCommand 重复定义、请求身份/用途上下文映射和 ResponseContext 缺口；独立版本评审，不冒充 IFC0.2 已完成。
- 任何未知 `required` 扩展、Schema/Digest 错误、身份或 Audience 不匹配，在副作用前拒绝。
- 未知 `optional` 扩展可忽略并审计，但不得改变业务授权。
