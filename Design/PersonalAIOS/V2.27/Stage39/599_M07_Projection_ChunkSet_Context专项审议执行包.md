# 599｜M07 Projection/ChunkSet/Context专项审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M07 Projection Owner（候选）

## 1. 审议目标与权限边界

确认M07对Embedding、Index、Context、Cache等派生Projection的构建、版本、可见性、撤销、失效和删除负责。M07的Projection不是源知识事实权威；M07不得降低源数据分类、用途或访问策略。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围，不表示该角色对所有字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| KAS-016 | deletion_dependency_refs | deletion_dependency_refs是否枚举Chunk、Projection、缓存、Provider、导出、日志和备份。 | D-08 | Medium |
| CHK-005 | chunk_set_id | chunk_set_id集合身份作用域、资产绑定和重建语义。 | D-11 | High |
| CHK-006 | chunk_set_version | chunk_set_version是否不可变；与Asset Content Version和Strategy Version关系。 | D-11 | High |
| CHK-007 | chunk_sequence | chunk_sequence是否从固定起点连续；重复、缺口和局部重排如何处理。 | D-11 | High |
| CHK-008 | content_ref | content_ref引用内容存储还是文本片段；权限与物理Handle如何隔离。 | D-11 | Medium |
| CHK-009 | text_digest | text_digest算法、规范化和Scope是否明确；摘要匹配不证明语义相同。 | D-11 | Medium |
| CHK-010 | locator_in_parent | locator_in_parent如何定位父内容版本；偏移单位和版本上下文是否明确。 | D-11 | Medium |
| CHK-011 | token_range | token_range依赖哪个Tokenizer及版本；跨模型Token范围是否可复现。 | D-11 | Medium |
| CHK-012 | character_range | character_range的字符编码、索引单位和Unicode规范化规则。 | D-11 | Medium |
| CHK-013 | chunk_strategy_ref | chunk_strategy_ref固定分块策略及版本；策略变化如何产生新Set。 | D-11 | Medium |
| CHK-014 | language_refs | language_refs支持多语言、混合语言和检测不确定性。 | D-11 | Medium |
| CHK-015 | classification_ref | classification_ref如何继承源资产分类；分块不得降低敏感级别。 | D-11 | High |
| CHK-016 | purpose_lineage_refs | purpose_lineage_refs保留处理目的和允许用途；检索用途是否重新授权。 | D-11 | High |
| CHK-017 | projection_state | projection_state区分生成、可见、过期、撤销、移除；不能代表权限批准。 | D-11 | High |
| CHK-022 | deletion_state_ref | deletion_state_ref覆盖索引、向量、缓存、Context和外部Projection清除状态。 | D-11 | Medium |

## 3. 必须回答的问题

1. ChunkSet是否只是集合/发布边界而非新OT？
2. 部分Chunk生成或Manifest不一致时能否阻止发布？
3. Projection是否固定源Asset/Chunk Version和Policy版本？
4. 撤回后Embedding、Index、Context和Cache如何失效？
5. Projection重建是否会在当前Policy下重新检查权限？
6. M07如何证明索引不可再返回撤回内容？
7. M07与M08的Chunk实例、M18的Policy和M02物理处置如何分工？

## 4. 必须提交的证据

1. CHK-005—017/022及KAS-016的Projection和删除依赖关系；
2. ChunkSet完整Manifest、版本、序列、成员数量和发布门禁；
3. Embedding/Index/Context/Cache Projection版本与源Asset/Chunk版本映射；
4. 权限继承、撤回传播、失效和重建契约；
5. M18 Policy与Projection读取路径的PEP检查证据；
6. M02物理存储、M15 Provider副本与M07 Projection删除边界。

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