# 算力底座 G2 契约治理包

状态：Proposed / RC0；纯架构研究，不含工程实现代码。

## 核心决策
- Ontology V3.1 Core 候选新增 OutputArtifact、Result、DelegationGrant、HumanApproval。
- ParticipantBinding / TrustAgreement 属于 Federation Governance Profile；DataSpaceContract 属于 Data Space Profile。
- EventSubscription、TaskClaim、EnvironmentSpaceDescriptor、TraceRecord、ArtifactBinding、GovernanceContextRef 不进入 Core。
- DM04 IFC0.2 只增加可选 profile_extensions，不改变 IFC0.1 既有必需字段。
- G1 关于 IFC0.2 顶层增加身份字段的建议已撤回；见 G1_勘误与契约基线校正.md。
- ADS/SCO REST Binding 存在 RequestEnvelope 未引用、GenericCommand重复定义和 ResponseContext缺口。

## 核查事实
ADS：RequestEnvelope Path引用0次，GenericCommand引用24次。
SCO：RequestEnvelope Path引用0次，GenericCommand引用22次。
两者 GenericCommand required 5 fields / payload optional；RequestEnvelope required 6 fields / payload required。

## 交付文件
- G2_Ontology_V3.1与DM04_IFC0.2执行报告.docx / .md
- G1_勘误与契约基线校正.md
- Ontology_V3.1.0-RC0_核心本体修订提案.md
- DM04_IFC0.2与ADS_SCO_REST_Binding对齐提案.md
- G2-03_ADS_SCO_API映射初稿.md
- G2_Schema验证记录.md
- schemas/：6份JSON Schema
- matrices/：实体、关系、REST绑定、API缺口、Owner评审清单
- decisions/：ADR-G2-01、ADR-G2-02
- examples/：请求与响应样例
- diagrams/：SVG与8K PNG

## 验证边界
JSON Schema Draft 2020-12结构检查及正样例验证通过；不等于OpenAPI工具链验证、Owner签署、双实现互操作或真实双站点测试通过。

## G2-03 新增：ADS/SCO 全量接口映射
- ADS 40 operations / 38 paths；SCO 35 operations / 35 paths。
- 75个操作逐项映射到六域、Owner、Coordinator、权威对象、风险、前置条件和Ontology。
- 16项API契约缺口、15类状态机权威对象、19项REST Header/Envelope绑定。
- Excel、CSV、Word、Markdown、SVG和8K PNG见 `G2-03/`。
