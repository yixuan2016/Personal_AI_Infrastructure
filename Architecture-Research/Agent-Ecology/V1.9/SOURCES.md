# V1.9｜研究证据与引用边界

**检索截止：** 2026-11-14  
**用途：** 支持跨生态能力发现、共享环境观察和协议边界研究  
**原则：** 证据类型、发布日期、成熟度与适用边界必须同时记录。

## 1. 直接相关的 Stigmergy / Shared-State 研究

### 1.1 Unprompted coordination through shared memory in LLM agents

- 作者：Pekka Abrahamsson、Muhammad Waseem、Esa Karjalainen、Petrus Jussila、Henri Hansen、Jussi Rasku、Bilhanan Silverajan、Kai-Kristian Kemell
- 机构：Tampere University
- 日期：2026-11-09
- 原始链接：https://arxiv.org/abs/2611.12412
- 类型：arXiv 预印本；双实现复现与扩展
- 研究设计：每个实验世界包含 4 个 Agent、20 个操作步骤、一个共享 Key-Value Store；其中 2 个 Agent 分别持有互补计算信息，另外 2 个执行独立任务；提示没有告知 Agent 存在其他参与者或要求协作。
- 证据：研究团队在两套独立实现中复现共享状态上的跨 Agent 读取与联合任务成功；无共享存储对照不能完成互赖任务。结果显示，是否写入中间结果、是否在伙伴写入后再次观察共享空间，受模型和工作流程提示影响。
- 重要限制：环境是短算术任务和小型共享 KV Store；每个世界只有 4 个 Agent、20 步；任务文本提供共同键名线索；“读取他人输出”不等于证明 Agent 有协作意图；模型、推理强度、API 端点和解析差异影响实验结果；论文指出仍需开放权重模型和更复杂任务验证。
- 对架构的启发：把共享状态视为通信通道；Runtime 必须有事件唤醒、游标续读和周期性重读，不能只依赖模型主动检查；按任务/域/目的隔离命名空间，并记录读写审计。
- 成熟度：E3-受控实验与双实现复现；非企业级部署证据。

## 2. 群体自组织与持久工件

### 2.1 SwarmWorld: Stigmergic technological evolution in societies of language-model agents

- 作者：Subhadeep Pal、Fiona Y. Wang、Markus J. Buehler
- 日期：2026-08-26
- 原始链接：https://arxiv.org/abs/2608.26081
- 类型：研究预印本；仿真环境实验
- 研究设计：初始同质的 LLM Agent 在共享空间中探索资源、加工材料、测试、构建持久工件，并生成由确定性模拟器评估的可执行控制器；Agent 被移除后，环境在未见扰动下检验结果。
- 主要发现：共享社会形成更广泛、韧性更强的技术组合；个体最强工件仍可能由孤立搜索获得；角色会随环境成熟而分化；物理痕迹协作与显式交互对生态持续演化的作用不同。
- 重要限制：研究结论依赖特定模拟世界、动作/材料 Schema 和评价函数；不能直接外推到企业流程、跨组织信任、生产安全或长期运维。
- 对架构的启发：区分 Agent 的认知提案与环境中的可验证结果；持久工件、可继承改进和确定性评价应分开管理。
- 成熟度：E2/E3-仿真研究；非真实生产验证。

## 3. 跨 Agent 协议与发现

### 3.1 Multi-agent Collaboration Protocol Suites Architecture

- 文档：draft-li-dmsc-macp-07
- 发布：2026-11-02
- 原始链接：https://datatracker.ietf.org/doc/html/draft-li-dmsc-macp-07
- 类型：IETF Internet-Draft / Work in Progress；个人草案，不代表 IETF 背书或正式标准。
- 可参考内容：Agent Gateway、本地能力目录、能力解析、能力摘要跨节点同步、增量更新和最终一致视图。
- 关键限制：草案提出 Agent Management Center 作为集中式信任锚；本项目不采用其作为全局超级信任根。草案还明确指出，完成初始 onboarding 并不免除 Agent 间运行时授权；交互级授权机制不在 AAAP 范围内。
- 对架构的启发：可参考“本地目录 + 摘要同步 + 网关侧候选解析”；保留各生态独立身份根、授权服务和本地 PEP。
- 成熟度：E1-协议草案；不得标记为正式标准。

## 4. Agent-to-Agent 与工具协议

### 4.1 A2A Protocol

- 官方规范：https://a2a-protocol.org/latest/specification/
- Agent Card：https://a2a-protocol.org/latest/specification/agent-card/
- 任务生命周期：https://a2a-protocol.org/latest/topics/life-of-a-task/
- 可参考内容：Agent Card、能力声明、Task/Message、异步任务状态、AUTH_REQUIRED、任务订阅和推送。
- 关键限制：AUTH_REQUIRED 只表示任务等待授权；A2A 不替实现方定义授权范围、凭证表示、有效期和撤销语义。
- 对架构的启发：A2A 用于 Agent 发现和任务协商；本地 PDP/PEP 与 Owner 决定实际授权。
- 成熟度：开放协议规范；具体版本兼容仍需锁定。

### 4.2 Model Context Protocol 2026-07-28

- 官方发布说明：https://blog.modelcontextprotocol.io/posts/2026-07-28/
- 类型：官方协议版本说明。
- 可参考内容：无状态请求核心、Multi Round-Trip Requests、Header 路由、工具目录缓存提示、授权发行者校验、凭证发行者绑定、Tasks 扩展。
- 关键限制：MCP 解决 Agent 与工具/资源服务交互，不定义跨生态成员治理和能力 Owner 权威。
- 对架构的启发：将工具调用和 Agent 间任务协商分开；凭证按发行者和受众绑定，不在 Agent 链路或共享环境中传播长期秘密。
- 成熟度：官方规范版本说明；迁移时需逐项核对 SDK 与服务端支持。

## 5. 事件与工作负载身份

### 5.1 CloudEvents

- 官方仓库：https://github.com/cloudevents/spec
- 当前发布版本：Core Specification v1.0.2。
- 可参考内容：事件封套中的 source、id、type、subject、dataschema 等字段；同一 source 下 source+id 唯一；事件可携带 Schema 引用。
- 关键限制：CloudEvents 只定义事件描述与互操作封套，不证明业务事件真实、授权充分或状态机正确。
- 对架构的启发：用事件 ID 做去重，用来源域和 Owner 聚合序号处理因果；敏感业务正文优先通过受控引用访问。
- 成熟度：CNCF 已发布规范。

### 5.2 SPIFFE / SVID

- 官方文档：https://spiffe.io/docs/latest/deploying/svids/
- 概念说明：https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- 可参考内容：工作负载身份、短期 X.509-SVID/JWT-SVID、Workload API 和信任 Bundle。
- 关键限制：工作负载身份只证明主体身份/来源，不等于业务 Purpose 授权、DataUseGrant 或人类审批。
- 对架构的启发：可作为跨生态工作负载身份的实现候选，但不强制所有成员生态采用 SPIFFE。
- 成熟度：开放身份规范与成熟工程生态；仍需结合本地 PKI/信任根设计。

## 6. 证据等级

| 等级 | 含义 | 允许的表述 |
|---|---|---|
| E0 | 概念或架构假设 | 候选、建议、待验证 |
| E1 | 标准/协议草案/规范文本 | 规范定义或草案提出；不代表落地成功 |
| E2 | 可复现原型或受控仿真 | 原型/仿真中观察到 |
| E3 | 受控实验、基准或独立复现 | 在明确实验条件下验证 |
| E4 | 多环境真实部署与独立审计 | 仅在证据齐备时使用生产验证表述 |

**禁止推断：** 论文发表不等于技术成熟；Internet-Draft 不等于正式标准；协议具备字段不等于实现互操作；目录可发现不等于有授权；仿真成功不等于生产安全。
