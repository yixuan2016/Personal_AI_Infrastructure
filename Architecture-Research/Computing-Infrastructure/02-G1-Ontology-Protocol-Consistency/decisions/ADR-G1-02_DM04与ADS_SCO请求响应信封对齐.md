# ADR-G1-02：DM04 与 ADS/SCO Request/Response Envelope 对齐

- 状态：Proposed，待 DM04 API Owner、ADS Owner、SCO Owner、Security Owner评审。
- 发现：DM04 IFC0.1语义要求caller_principal、workload_identity、audience、purpose、protocol_profile、expires_at等；ADS/SCO OpenAPI RC0 RequestEnvelope当前required主要为request_id、correlation_id、issued_at、api_version、schema_version、payload。caller_workload_id、participant_id、tenant_id等不足以替代完整安全上下文。
- 决策建议：保留现有api_version、schema_version、payload；在IFC0.2显式对齐安全上下文字段。联邦跨站点请求中caller_principal、workload_identity、audience、purpose、protocol_profile、expires_at必须可验证；状态变更需expected_state_version；高风险操作需payload_digest与signature_ref。
- Response：区分command_status与authoritative_state；补齐responder_site_id、object_ref、object_version、event_cursor、evidence_refs。Operation.status不能代替业务对象权威状态。
- 禁止：从URL猜audience；从participant_id推断caller_principal；从api_version推断protocol_profile；将purpose塞入非规范metadata。
- 兼容：未完成双边批准前，不宣称现有OpenAPI已符合DM04跨域安全契约；未满足安全上下文的高风险跨站点操作不得激活。
- 验收：双实现字段必需性、状态交叉表、签名覆盖、UNKNOWN恢复和向后兼容测试通过。

- 扩展封装补充：`criticality`归属于Profile扩展控制包装层，与profile_version/schema_ref/payload_digest同级；AEEContext `data`只放领域引用，避免控制元数据重复定义或由payload覆盖。
