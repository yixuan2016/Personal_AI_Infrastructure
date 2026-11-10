# A2A / CloudEvents / FWSX 分层互操作规范（候选）

## 协议分工
- Ontology：实体、关系、权威语义。
- DM04：领域操作、状态机、幂等、错误和交易契约。
- CloudEvents：事件信封。
- FWSX：事件交付、cursor、重试、重放。
- A2A：Agent发现、消息、Task交互、Artifact交接。
- AEE/ASCP：跨上述组件的Profile语义和引用绑定。

## A2A 1.0
AgentCard声明capabilities.extensions[]；请求头A2A-Extensions按请求激活；Message/Artifact使用extensions[]和metadata；Task仅用metadata承载AEE引用，不添加核心协议未定义字段。A2A Task状态不覆盖DM04状态机。

## CloudEvents 1.0.2
id/source/type/subject/time/dataschema/data映射TraceRecord。DM04扩展站点、聚合、版本、序号、因果与签名引用。单聚合内单调，不承诺全局总序。

## FWSX
事件源Owner授权订阅，目标站点PDP/PEP复核；FWSX负责投递和游标。至少一次投递，Inbox幂等；cursor补拉；撤销停止后续投递。事件订阅不授予Artifact正文读取权。

## 安全失败行为
未知事件类型：存档告警、不触发副作用。签名失败：隔离。Schema不兼容：拒绝业务效果。重复事件：Inbox去重。Sequence gap：按cursor补拉并对账。未知撤销水位：高风险操作暂停。
