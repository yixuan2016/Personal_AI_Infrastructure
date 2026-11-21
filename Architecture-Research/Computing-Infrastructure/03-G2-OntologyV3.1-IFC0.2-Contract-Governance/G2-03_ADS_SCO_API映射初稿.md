# G2-03 ADS / SCO / 六域 API 绑定初稿

**状态：** Proposed；基于现有 ADS_API_v1_OpenAPI_3.2.1_RC0.json 与 SCO_API_v1_OpenAPI_3.2.1_RC0.json 的职责映射，不代表接口实现或Owner签署。

## 1. ADS 的定位

ADS 不是单纯 API Gateway、策略网关或调度器。它负责联邦治理协调、共同语义与 Ontology/Profile 注册、参与方/信任关系协调、能力发现、跨域策略与共享数据治理视图、智能生态协调；并保留 ADS 自身执行、管理、考核与成长闭环。ADS 不代替各站点 IAM/PDP/PEP、Data Owner、Resource Owner 或 Acceptance Owner。

## 2. SCO 的定位

SCO 负责全局 TaskContract / ContractGraph / Plan / Saga / ActivationBarrier / Transaction Reconciliation 的任务生命周期协调。SCO 不签发站点本地 TaskClaim，不签发 LocalResourceLease / FencingToken，不覆盖站点本地 TaskStage 和执行事实。

## 3. API 责任映射

| 能力域 | ADS 协调职责 | SCO 协调职责 | 本地权威 |
|---|---|---|---|
| 联邦治理 | 成员、TrustAgreement 引用、ParticipantBinding、Profile/Namespace 注册与协调 | 消费已批准的成员/协议上下文 | 双方 Federation Governance Owner |
| 身份与授权 | 跨域信任/委托目录、授权上下文引用、撤销水位协调 | 携带合法身份上下文请求任务动作 | 各站点 IAM/PDP/PEP |
| 数据空间 | 目录发现、DataSpaceContract 协调、血缘/义务治理视图 | 将数据依赖纳入 TaskContract/Barrier | Data Owner / Connector / 本地 PEP |
| 算力星 | 能力目录、Provider/Offer 发现、Profile 语义协调 | 任务资源需求、Prepare/Commit 协调 | 资源所在地 Owner / Lease Authority |
| 联邦任务 | 提供治理/能力/环境引用 | ContractGraph、Plan、Saga、Barrier、对账 | Site Task Owner / Local Task Coordinator |
| 证据与验收 | 治理审计索引、共享语义和规则版本 | 汇总执行/验收/计量/结算关联视图 | Producer / Evidence / Independent Acceptance / Metering / Settlement Owner |

## 4. AEE/ASCP 横切绑定

AEE/ASCP Profile 通过 DM04 IFC0.2 `profile_extensions`、CloudEvents ASCP 扩展和 A2A Extension URI 提供引用上下文。其 URI 必须由项目控制域名注册；目前域名未确认，示例 URI 不能用于生产或跨站点激活。

## 5. 需要下一轮关闭的 API 问题

1. ADS 与 SCO 是否共同维护重复的 RequestEnvelope / GenericCommand 组件，需抽取单一共享契约来源。
2. 现有 API `security` scopes、OAuth2 token audience、mTLS 身份映射需形成统一 Security Profile。
3. DataSpaceContract 与 DataUseGrant 的端点和权威字段需明确分离。
4. SCO `Operation` 与 DM04 ResponseEnvelope 的绑定需补齐。
5. Local TaskClaim 和 LocalResourceLease 的 API Owner 不得落到 SCO 全局协调接口。
6. Ontology Profile Registry 需具备版本、状态、Owner、Digest、签署和弃用记录。
