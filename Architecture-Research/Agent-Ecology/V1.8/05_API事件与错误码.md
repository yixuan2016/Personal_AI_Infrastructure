# 05｜API、事件与错误码（候选）

## 1. API 候选目录
| 方法 | 路径 | 用途 |
|---|---|---|
| POST | /federation/v1/members/claims | 提交成员生态身份声明 |
| GET | /federation/v1/members/{domain_id} | 查询成员声明和撤销状态 |
| POST | /federation/v1/capabilities/advertisements | 发布能力广告 |
| POST | /federation/v1/tasks/negotiate | 协商跨域任务契约 |
| POST | /federation/v1/policy/compatibility-checks | 请求策略兼容评估 |
| POST | /federation/v1/improvements/proposals | 发布改进提案 |
| POST | /federation/v1/evidence/bundles | 提交证据包索引 |
| POST | /federation/v1/adoptions/receipts | 提交本地采用回执 |
| POST | /federation/v1/revocations/events | 发布撤销事件 |

建议 HTTPS + mTLS/工作负载身份、签名内容摘要和版本化路径；技术栈可替换，但契约语义不得弱化。

## 2. 事件目录
FederationMemberRegistered、FederationMemberSuspended、CapabilityAdvertised、CapabilityAttestationRevoked、FederatedTaskProposed、FederatedTaskAuthorized、FederatedTaskStateChanged、PolicyCompatibilityEvaluated、ImprovementProposalPublished、EvidenceBundleVerified、ImprovementShadowStarted、ImprovementCanaryStarted、ImprovementAdoptedLocally、ImprovementRevoked、FederationDomainQuarantined。

事件只声明发生了什么，不代表订阅者已授权执行事件建议的动作。

## 3. 错误码
| 错误码 | 含义 | 默认处理 |
|---|---|---|
| FED-1001 | 未知成员域 | DENY |
| FED-1002 | 身份凭证无效/过期 | DENY |
| FED-1003 | 能力声明签名错误 | QUARANTINE |
| FED-1101 | 能力版本不兼容 | HOLD |
| FED-1102 | Ontology 映射缺失 | HOLD |
| FED-1201 | 本地策略 DENY | DENY |
| FED-1202 | 策略判定 ABSTAIN | HOLD |
| FED-1203 | 策略版本过期 | HOLD |
| FED-1301 | 证据包摘要不匹配 | QUARANTINE |
| FED-1302 | 独立评估证据不足 | HOLD |
| FED-1401 | 事件重复/幂等冲突 | RECONCILE |
| FED-1402 | 事件水位缺口 | RECONCILE |
| FED-1501 | 撤销状态不可达 | HOLD |
| FED-1601 | 导出策略禁止 | DENY |
| FED-1602 | DataUseGrant 缺失 | DENY |
| FED-1701 | 超出跨域速率限制 | RETRY_AFTER |
| FED-1801 | 生态隔离/熔断 | DENY |
| FED-1901 | 版本降级或未知关键字段 | HOLD |

## 4. 幂等与一致性
所有创建/变更请求包含 idempotency_key、request_digest、actor_domain、policy_version 和 expires_at。事件消费者按 (producer_domain,event_id) 去重，并检查单个 Owner 聚合内的 sequence/watermark。不能跨 Owner 比较序列号，也不能用接收时间替代事件因果关系。
