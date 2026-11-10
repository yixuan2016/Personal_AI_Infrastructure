# ADR-G2-02：DM04 IFC0.2 与 ADS/SCO REST Binding 分离治理

- 状态：Proposed，待 DM04 API、ADS API、SCO API、Security 与 AEE/ASCP Profile Owner评审。
- 决策A：DM04 IFC0.2只增加可选profile_extensions，不改变IFC0.1既有必需字段。
- 决策B：caller_principal、workload_identity、audience从经过验证的OAuth2/mTLS身份上下文绑定；不得由请求体自报值建立权威。
- 决策C：purpose从显式操作目的及TaskContract/DataSpaceContract/DataUseGrant解析；reason不是purpose。
- 决策D：protocol_profile独立协商；不从api_version/schema_version推断。
- 决策E：ADS/SCO REST Binding RC1单独解决RequestEnvelope未引用、GenericCommand被多路径复用、payload必需性差异、ResponseContext缺口和OAS版本选择。
- 事实：ADS 24个Path、SCO 22个Path引用GenericCommand；两者RequestEnvelope组件当前Path引用0次。GenericCommand required 5字段且payload可选；RequestEnvelope required 6字段且payload必需。
- 禁止：将G1已撤回的“IFC0.2新增顶层身份字段”作为基线；未协商Profile扩展不得发送。
- 验收：REST绑定矩阵、OAuth2/mTLS映射、IFC0.1回归、IFC0.2双端协商、ResponseContext映射和双实现契约测试通过。
