# ADR-G2-01：Ontology V3.1 Core 与 Profile 分层

- 状态：Proposed / RC0，待 Ontology Owner 与六域 Owner 签署。
- 决策：V3.1 以 Minor additive 方式演进 V3.0；不删除/重命名 V3.0 既有实体与关系。
- Core 新增：OutputArtifact、Result、DelegationGrant、HumanApproval。
- Federation Governance Profile 新增：ParticipantBinding、TrustAgreement。
- Data Space Profile 新增：DataSpaceContract。
- Runtime/Projection 不进入 Core：EventSubscription、TaskClaim、EnvironmentSpaceDescriptor、TraceRecord、ArtifactBinding、GovernanceContextRef。
- 理由：OutputArtifact/Result 是跨域任务成果与披露生命周期的通用语义；DelegationGrant/HumanApproval 是跨域信任与人类治理的通用语义。其余概念有明确的领域或运行时边界。
- 禁止：平行 Participant/Trust/Data Registry；平行 Artifact Registry；将TaskClaim升级为全局ResourceLease。
- 验收：Schema有效；V3.0到V3.1映射无破坏性变化；新增关系Owner、基数和撤销/有效期约束明确。
