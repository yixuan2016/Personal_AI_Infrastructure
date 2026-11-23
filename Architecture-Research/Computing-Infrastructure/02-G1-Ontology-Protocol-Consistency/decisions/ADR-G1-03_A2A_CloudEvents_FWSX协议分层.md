# ADR-G1-03：A2A、CloudEvents 与 FWSX 的协议分层

- 状态：Proposed，待协议/Profile Owner评审。
- 决策：CloudEvents负责事件信封；AEE/ASCP定义事件语义投影；FWSX负责订阅投递、游标、重试和重放；A2A负责Agent消息、任务交互和Artifact交接；DM04负责领域业务状态与权威。
- A2A：AgentCard capabilities.extensions[]声明；请求通过A2A-Extensions激活；Message/Artifact可使用extensions[]与metadata；Task只用metadata承载Profile引用，不增加未定义的Task.extensions[]。
- CloudEvents：id/source/type/subject/time/dataschema/data映射TraceRecord；DM04扩展siteid/aggregateid/aggregateversion/sequence/correlationid/causationid/signature_ref。
- FWSX：至少一次投递、Inbox幂等、按cursor补拉；不承诺网络恰好一次；不改变事实Owner、不授权Artifact读取。
- 禁止：A2A Task状态覆盖DM04 Saga；FWSX成为事件事实Owner；订阅权限自动继承为Artifact读取权。
- 验收：未知事件零副作用、重复投递单次逻辑效果、sequence gap补拉、扩展未激活副作用前拒绝、A2A Task ID与SCO TaskRun可追踪映射。
