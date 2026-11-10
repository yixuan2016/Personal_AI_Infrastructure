# G2 Schema 验证记录

验证器：Python `jsonschema` Draft 2020-12。

## Schema 自身检查
- AEE_ASCP_Context_1.1.0-RC0.schema.json：通过
- DM04_IFC0.2_profile_extensions_Additive_Overlay.schema.json：通过
- DM04_REST_ResponseContext_RC0.schema.json：通过
- Ontology_V3.1_Core_Additions.schema.json：通过
- Ontology_V3.1_DataSpaceContract_Profile.schema.json：通过
- Ontology_V3.1_Federation_Governance_Profile.schema.json：通过

## 样例检查
- IFC0.2 profile_extensions 正样例：通过
- AEE/ASCP Context 正样例：通过
- DM04 REST ResponseContext 正样例：通过
- OutputArtifact 正样例：通过
- Result 正样例：通过

## 负向样例
- criticality 使用未定义枚举 `mandatory`：正确拒绝
- Result 标记为 `Released` 但缺少 `release_decision_ref`：正确拒绝

## 边界
本记录仅证明本包 JSON Schema 的语法结构与所列正样例通过本地验证；不代表 OpenAPI 工具链验证、Owner 签署、双实现互操作或真实双站点测试通过。
