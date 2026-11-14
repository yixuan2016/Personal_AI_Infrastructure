# ADR-G1-01：AEE/ASCP 六对象与 Ontology V3.0 的映射原则

- 状态：Proposed，待 Ontology Owner、六域 Owner、AEE/ASCP Profile Owner评审。
- 决策：六对象不是六个新的Ontology Core实体。采用直接映射、关联投影、Profile扩展三类方式。
- 直接映射：TaskContract、TaskRun、TaskStage、PolicyDecision、DataUseGrant、ResourceLease、EvidenceRecord、AcceptanceRecord、MeteringRecord、SettlementRecord、OntologyProfile、PolicyProfile等。
- 关联投影：EnvironmentSpaceDescriptor、TraceRecord、ArtifactBinding、GovernanceContextRef。
- Profile/Runtime扩展：ParticipantBinding、TrustAgreement、DataSpaceContract、DelegationGrant、HumanApproval、EventSubscription、TaskClaim、OutputArtifactRef、ResultRef。
- 禁止：新建第二套参与方名册、信任根、事件库、全局Lease Authority、全局PDP、Artifact Registry。
- 验收：六对象字段均能追溯至Ontology实体/关系或明确标注Profile DTO；每个引用有Owner、版本、有效期和重新鉴权规则。
