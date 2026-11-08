# 600｜M17 Receipt/Connector原件权威专项审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M17 Connector/Receipt Authority（候选）

## 1. 审议目标与权限边界

确认M17对Connector采集事实、Receipt原件和来源回执的保管与解释边界。Evidence可以引用Receipt，但不得复制并形成第二个Receipt权威；M06负责Evidence/Assertion语义，M08负责Evidence实例记录。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围，不表示该角色对所有字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| SRC-005 | locator_refs | locator_refs是否支持多值、历史、优先级和失效；凭据是否与定位信息隔离。 | D-02 | Medium |
| SNP-008 | captured_locator_ref | captured_locator_ref是否固定采集时Locator；失效或凭据过期不应改写历史。 | D-02/D-03 | Medium |
| EVD-002 | evidence_kind | evidence_kind受控分类能否区分原始材料、Receipt、摘录、观察记录和外部证明。 | — | Medium |
| EVD-003 | evidence_target_ref | evidence_target_ref采用类型化目标；仅允许Registry批准的对象和子记录。 | D-12 | High |
| EVD-004 | target_version_ref | target_version_ref是否固定目标版本；动态目标如何保存核验时解析快照。 | D-12 | High |
| EVD-005 | locator_schema_ref | locator_schema_ref是否版本化；页码、段落、表格、消息和媒体坐标如何统一。 | D-12 | High |
| EVD-006 | locator_payload | locator_payload只保存定位坐标；不得包含Token、Cookie、签名URL秘密或绕过授权凭据。 | D-12 | High |
| EVD-007 | target_content_digest | target_content_digest摘要哪个目标版本及内容范围；算法与Scope必须明确。 | D-06/D-12 | High |
| EVD-008 | locator_fragment_digest | locator_fragment_digest摘要哪一片段；片段规范化和定位漂移如何处理。 | D-06/D-12 | High |
| EVD-009 | excerpt_ref | excerpt_ref指向可控摘录副本；访问权限、来源版本和保留规则如何继承。 | D-12 | High |
| EVD-010 | excerpt_digest | excerpt_digest覆盖摘录原始还是规范化文本；不能替代Target Digest。 | D-12 | High |

## 3. 必须回答的问题

1. Receipt原件由哪个模块保存，如何证明引用仍指向原件？
2. Evidence中的excerpt或Digest是否会被误认为Receipt原件？
3. Connector采集时间、入库时间和来源事件时间如何区分？
4. Locator是否可能包含Token、Cookie、签名URL或其他访问秘密？
5. 来源回执失效或被撤回时，Evidence/Assertion如何收到影响事件？
6. M17的专业事实如何与M06语义、M08实例、M18 Policy边界分离？

## 4. 必须提交的证据

1. Connector/Receipt原件类型、稳定标识、来源系统和原始时间；
2. Receipt签名、完整性、版本、原件引用和可追溯性证据；
3. Source Locator、Connector重定向、授权凭据隔离和采集失败记录；
4. EVD-003—010中引用Receipt时的目标类型、版本、Locator和Digest规则；
5. 原始Receipt撤回、来源不可访问和法律保留时的处理边界。

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