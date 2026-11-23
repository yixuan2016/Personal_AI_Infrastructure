# IFC0.2 Request/Response Envelope 对齐增量（候选）

## 1. 当前问题
DM04 IFC0.1规范语义与ADS/SCO OpenAPI RC0的RequestEnvelope必需字段存在差异。不能将caller_workload_id当作完整workload_identity，也不能从participant_id推断caller_principal；audience、purpose、protocol_profile没有显式定义。

## 2. 请求字段建议
保留现有：request_id、correlation_id、issued_at、api_version、schema_version、payload。
补齐/明确：caller_principal、workload_identity、audience、purpose、protocol_profile、expires_at。
按操作条件必需：idempotency_key（副作用）、expected_state_version（状态变更）、payload_digest与signature_ref（高风险写操作）。

字段版本维度不可混淆：
- api_version：API逻辑接口版本。
- schema_version：具体运行时Schema版本。
- protocol_profile：双方协商的协议Profile。
- ontology_profile_ref/version：共同语义版本。
- contract_version：具体业务合同版本。

## 3. 响应字段建议
保留operation_id/status/accepted_at/status_url/retry_after_seconds/result_ref/error_ref等异步操作字段。
补齐DM04语义：responder_site_id、object_ref、object_version、command_status、authoritative_state、event_cursor、evidence_refs。
`command_status`表示命令执行生命周期；`authoritative_state`表示目标业务对象状态，二者不能合并。

## 4. 安全门禁
联邦跨站点写请求缺少主体、工作负载身份、Audience、Purpose、Profile或有效期时拒绝；高风险写请求缺少摘要/签名证据时隔离。超时UNKNOWN先查Owner，不盲重放。

## 5. 兼容路径
IFC0.2需双方API Owner、Security Owner签署；在批准前不得把新字段假设为对端支持。对不具备完整安全上下文的既有API操作，限于其已批准的本地/低风险范围，不可用隐式推断执行跨站点高风险动作。

## 6. Profile Extension 控制元数据归属
`criticality`属于扩展激活/兼容控制元数据，应放在每个Profile扩展包装层，与`profile_version`、`schema_ref`、`payload_digest`同级；不重复放入AEEContext业务`data`。AEEContext只携带环境、Ontology、Trace、Subscription、TaskClaim、ArtifactBinding、GovernanceContext等引用。这样可以避免两个criticality值不一致，也避免业务载荷覆盖协议控制策略。
