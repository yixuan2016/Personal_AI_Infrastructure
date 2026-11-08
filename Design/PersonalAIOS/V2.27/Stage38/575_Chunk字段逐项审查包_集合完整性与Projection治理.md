# 575｜Chunk字段逐项审查包：集合完整性与Projection治理

**状态：** Field-Level Design Review Candidate；Owner Feedback 22/22 Pending；No Approval

## 1. 对象边界

Chunk是知识内容的分块派生对象；ChunkSet在当前基线仅是集合/发布边界候选，不是新OT。Embedding、Index、Context Cache属于Projection，不是事实权威。D-11为主决策，D-08/D-04提供版本与授权约束。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| CHK-001 | `chunk_id` | chunk_id是否全局唯一且不可复用；重新分块产生新身份还是更新旧对象。 | D-11 |
| CHK-002 | `knowledge_asset_ref` | knowledge_asset_ref是否指向稳定资产身份；读取时是否必须同时固定版本。 | D-08/D-11 |
| CHK-003 | `asset_version_ref` | asset_version_ref必须绑定Chunk实际来源内容版本，禁止指向动态Current。 | D-08/D-11 |
| CHK-004 | `extraction_run_ref` | extraction_run_ref是否指向已核验终态Run；UnknownOutcome输出不得发布。 | D-08/D-11 |
| CHK-005 | `chunk_set_id` | chunk_set_id集合身份作用域、资产绑定和重建语义。 | D-11 |
| CHK-006 | `chunk_set_version` | chunk_set_version是否不可变；与Asset Content Version和Strategy Version关系。 | D-11 |
| CHK-007 | `chunk_sequence` | chunk_sequence是否从固定起点连续；重复、缺口和局部重排如何处理。 | D-11 |
| CHK-008 | `content_ref` | content_ref引用内容存储还是文本片段；权限与物理Handle如何隔离。 | D-11 |
| CHK-009 | `text_digest` | text_digest算法、规范化和Scope是否明确；摘要匹配不证明语义相同。 | D-11 |
| CHK-010 | `locator_in_parent` | locator_in_parent如何定位父内容版本；偏移单位和版本上下文是否明确。 | D-11 |
| CHK-011 | `token_range` | token_range依赖哪个Tokenizer及版本；跨模型Token范围是否可复现。 | D-11 |
| CHK-012 | `character_range` | character_range的字符编码、索引单位和Unicode规范化规则。 | D-11 |
| CHK-013 | `chunk_strategy_ref` | chunk_strategy_ref固定分块策略及版本；策略变化如何产生新Set。 | D-11 |
| CHK-014 | `language_refs` | language_refs支持多语言、混合语言和检测不确定性。 | D-11 |
| CHK-015 | `classification_ref` | classification_ref如何继承源资产分类；分块不得降低敏感级别。 | D-04/D-11 |
| CHK-016 | `purpose_lineage_refs` | purpose_lineage_refs保留处理目的和允许用途；检索用途是否重新授权。 | D-04/D-11 |
| CHK-017 | `projection_state` | projection_state区分生成、可见、过期、撤销、移除；不能代表权限批准。 | D-11 |
| CHK-018 | `supersedes_chunk_ref` | supersedes_chunk_ref表达替代/修订而非覆盖；跨Set引用是否允许。 | D-11 |
| CHK-019 | `created_at` | created_at记录Chunk生成时间而非父内容时间。 | D-11 |
| CHK-020 | `retention_profile_ref` | retention_profile_ref是否继承更严格规则；Chunk保留不能超过源依据。 | D-11 |
| CHK-021 | `object_version` | object_version与Chunk内容版本/ChunkSet版本分离。 | D-11 |
| CHK-022 | `deletion_state_ref` | deletion_state_ref覆盖索引、向量、缓存、Context和外部Projection清除状态。 | D-11 |

## 3. 对象内一致性约束

- chunk_id稳定；knowledge_asset_ref指向逻辑资产，asset_version_ref固定内容版本。
- extraction_run_ref必须指向可核验终态Run；UnknownOutcome或部分失败输出不可发布。
- chunk_set_id/version/sequence与Manifest一致，集合完整性须可证明。
- content_ref、text_digest、locator_in_parent、token_range和character_range使用一致的内容版本和坐标单位。
- classification_ref和purpose_lineage_refs不得降级；Projection读取仍需当前Policy。
- projection_state不等于访问批准；deletion_state_ref必须覆盖Index、Embedding、Cache和Context等副本。
- supersedes_chunk_ref表达替代关系，不得覆盖旧Chunk或导致历史Evidence漂移。

## 4. 当前结论

22/22字段完成设计审查问题登记；Owner状态22/22 Pending；不新增ChunkSet OT，不批准Projection状态或权限契约。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 22/22 与Stage35原始台账一致 |
| 语义审查问题 | 22/22 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。