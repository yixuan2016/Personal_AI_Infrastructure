# 597｜M18 Policy Authority专项审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M18 Policy Authority（候选）

## 1. 审议目标与权限边界

确认M18对Purpose、Policy、Consent、Processing Basis、Approval、Classification、Retention和PEP裁决规则的权威。来源Rights、历史Purpose、当前Consent和一次PolicyDecision不得合并成永久授权。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围，不表示该角色对所有字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| SRC-008 | source_rights_refs | source_rights_refs如何表达多重权利、地域/用途限制、有效期和撤回。 | D-04 | Medium |
| SRC-009 | data_subject_refs | data_subject_refs是否最小化；多主体、未知主体和身份纠错如何表达。 | — | Medium |
| SRC-010 | classification_ref | classification_ref是否由权威分类体系提供；来源分类变化如何传播到派生物。 | — | Medium |
| SNP-013 | rights_snapshot_ref | rights_snapshot_ref是否保存采集时权利状态及来源；不能被当前权利覆盖。 | D-03/D-04 | High |
| SNP-014 | purpose_ref | purpose_ref是否对应本次采集目的；目的变更是否触发重新授权。 | D-03/D-04 | High |
| SNP-015 | policy_decision_ref | policy_decision_ref是否绑定Actor、Source、Action、Purpose和采集时Policy版本。 | D-03/D-04 | High |
| SNP-016 | applicable_basis_refs | applicable_basis_refs区分Consent、合同、法定义务等依据；多依据冲突如何处理。 | D-03/D-04 | High |
| SNP-017 | data_subject_refs | data_subject_refs是否继承并可修正；主体不明时是否限制后续处理。 | D-03 | Medium |
| SNP-018 | classification_ref | classification_ref是否记录采集时分类；分类升级如何触发派生数据重评。 | D-03 | Medium |
| SNP-019 | retention_profile_ref | retention_profile_ref是否固定采集时适用的保留规则版本和触发起点。 | D-03 | Medium |
| RAW-014 | classification_ref | classification_ref是否与源Snapshot分类保持可解释的继承/提升关系。 | — | Medium |
| RAW-015 | retention_profile_ref | retention_profile_ref绑定哪一版本；Legal Hold、例外和保留起点如何确定。 | — | Medium |
| KAS-009 | classification_ref | classification_ref如何从来源和处理结果继承；冲突时采用何种提升规则。 | — | Medium |
| KAS-010 | retention_profile_ref | retention_profile_ref适用范围是逻辑资产还是每个版本；更严格规则如何传播。 | — | Medium |
| KAS-015 | processing_purpose_refs | processing_purpose_refs如何保留各派生用途的来源链；是否允许用途扩展。 | — | Medium |
| KAS-016 | deletion_dependency_refs | deletion_dependency_refs是否枚举Chunk、Projection、缓存、Provider、导出、日志和备份。 | D-08 | Medium |
| EXT-009 | purpose_ref | purpose_ref绑定本次运行的具体目的；不能继承成永久通用授权。 | D-09 | Medium |
| EXT-011 | policy_decision_ref | policy_decision_ref是否绑定输入、Action、Purpose、Provider、Region和Policy版本。 | D-09 | High |
| EXT-012 | provider_profile_ref | provider_profile_ref固定合同/能力/子处理商条款版本；Profile更新不得改写历史。 | D-09 | High |
| EXT-013 | provider_region_ref | provider_region_ref区分请求地区、计算地区、存储/日志/人工访问地区。 | D-09 | High |
| EXT-024 | retention_profile_ref | retention_profile_ref覆盖输入副本、输出、日志、临时文件和Provider缓存的哪一范围。 | — | Medium |
| CHK-015 | classification_ref | classification_ref如何继承源资产分类；分块不得降低敏感级别。 | D-11 | High |
| CHK-016 | purpose_lineage_refs | purpose_lineage_refs保留处理目的和允许用途；检索用途是否重新授权。 | D-11 | High |
| CHK-020 | retention_profile_ref | retention_profile_ref是否继承更严格规则；Chunk保留不能超过源依据。 | — | Medium |
| CHK-022 | deletion_state_ref | deletion_state_ref覆盖索引、向量、缓存、Context和外部Projection清除状态。 | D-11 | Medium |
| EVD-016 | classification_ref | classification_ref按目标和摘录中更严格级别继承；不得降级。 | — | Medium |
| EVD-017 | purpose_lineage_refs | purpose_lineage_refs记录证据采集/使用目的；下游主张使用需独立Policy检查。 | — | Medium |
| EVD-018 | retention_profile_ref | retention_profile_ref处理原件、摘录、摘要和审计引用的不同保留要求。 | — | Medium |
| EVD-021 | deletion_state_ref | deletion_state_ref区分内容删除、Projection撤除、引用失效和保留例外。 | — | Medium |

## 3. 必须回答的问题

1. Rights、Purpose、Consent、Processing Basis、Approval和PolicyDecision分别由谁维护？
2. 历史PolicyDecision是否可能被错误复用为未来请求授权？
3. Purpose缺失、Rights Unknown、Consent撤回或Classification Unknown时如何Fail Closed？
4. 分类升级如何传播到Chunk、Embedding、Context、Cache、Provider和Evidence？
5. Retention、Legal Hold和删除请求冲突时谁裁决、谁执行、谁提供证据？
6. Provider实际Region和子处理商变化是否触发重新评估？
7. M18如何避免代替Personal Owner决定个人价值/目标或代替M02确认物理删除？

## 4. 必须提交的证据

1. Purpose/Policy/Consent/Processing Basis/Classification/Retention目录和版本；
2. SRC-008/009/010、SNP-013—019、RAW-014/015等来源和采集治理字段的依据链；
3. EXT-009/011/012/013/024的运行时Purpose、Policy、Provider/Region与Retention绑定；
4. KAS/CHK/EVD派生物的分类、用途血缘、撤回和删除传播矩阵；
5. PEP输入输出、拒绝/Unknown案例、Policy版本和决策有效期；
6. Privacy/Legal对具体处理目的、地区和数据类别的专业意见。

## 5. 必须记录的边界与反例

- 说明该模块实际能决定的事项，以及明确不能决定的事项；
- 以合成数据给出允许、拒绝、Unknown、部分失败和撤销案例；
- 对外部能力声明与实际运行事实进行区分；
- 对历史版本、当前版本和派生副本分别给出证据；
- 不得将“系统暂时支持”写成“Owner已批准”。

## 6. 输出要求

提交材料至少包括：逐字段/逐议题意见、原始证据引用、事实假设、建议处置、反方风险、权限边界、会审需求、未决问题、条件和复审触发器。若无权批准，明确标记为专业意见或会审意见，不写OwnerApproved。

## 7. 当前结论

本包为审议执行材料；尚无真实Owner反馈、正式会议结论或批准证据。未审议字段保持Pending；不产生Profile Delta，不授权工程实现。