# 549｜D-11 ChunkSet发布与Projection权限：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

Chunk不是孤立文本片段，而是某个KnowledgeAsset内容版本在特定ExtractionRun和Chunk Strategy下产生的派生集合成员。若集合尚未完整生成就被索引或检索，可能出现缺块、重复、版本混杂或权限不一致。Embedding、Index和Context Projection属于派生视图，不是新的事实权威。

## 2. 关联字段与权威边界

- CHK-005 chunk_set_id
- CHK-006 chunk_set_version
- CHK-007 chunk_sequence
- CHK-008 content_ref
- CHK-009 text_digest
- CHK-010 locator_in_parent
- CHK-011/012 token_range/character_range
- CHK-013 chunk_strategy_ref
- CHK-014 language_refs
- CHK-015 classification_ref
- CHK-016 purpose_lineage_refs
- CHK-017 projection_state
- CHK-022 deletion_state_ref

主决定权威候选：M08负责Chunk实例与集合成员；M07负责Embedding/Index/Context Projection；M18负责访问策略、Purpose和撤回；M06定义集合与分块语义。

## 3. 必须回答的问题

1. ChunkSet是发布封套、逻辑集合还是新OT？本阶段不得未经OD/OT流程将其升格为OT。
2. chunk_set_version如何与KnowledgeAsset Content Version及ExtractionRun绑定？
3. 如何证明集合完整：成员数、序列连续性、清单摘要、重复检测和失败成员如何表达？
4. ChunkSet何时从Building进入Ready/Published，谁有权触发？
5. 旧ChunkSet与新ChunkSet并存时，检索默认使用哪个版本？
6. classification_ref和purpose_lineage_refs如何从源资产及运行授权传播？
7. Projection在生成、刷新、撤销、失效和删除时如何与Chunk版本对齐？
8. 权限撤回后，如何确保Embedding/Index/Cache不继续暴露原内容？

## 4. 候选方案（不构成推荐或批准）

- A：ChunkSet作为不可变发布清单，只有完整性验证通过后才整体发布；Projection引用明确Set Version。
- B：Chunk可增量发布，但每个成员必须有可见性门禁和集合完成状态；吞吐较好，消费者复杂度更高。
- C：不建立显式ChunkSet发布边界，由消费者自行拼装Chunk；结构轻，但容易产生版本混合和部分可见风险。

## 5. 必须提供的证据

- Chunk Strategy、集合清单、序列和Manifest样例；
- M07 Projection构建、索引刷新、缓存和删除契约；
- M18分类、Purpose、权限继承和撤回策略；
- KnowledgeAsset版本切换及旧集合下线场景；
- 不完整集合、重复Chunk和Projection失败的处理规则。

## 6. 下游影响与测试

影响搜索、向量检索、上下文组装、Agent读取、Evidence定位、导出和删除。消费者必须明确Set Version和Projection Version，不得将局部成功视为集合整体发布。

测试覆盖集合成员缺失、序列重复、Manifest不匹配、跨版本混合、未授权Chunk进入Index、权限撤回后Projection残留、旧版本仍被默认检索和删除状态不同步。

## 7. 阻断条件

集合完整性无法证明；Projection不携带源版本；分类/Purpose继承不清；权限撤回不能传播；ChunkSet概念被擅自升级为新OT。

## 8. 当前状态

本文件仅形成D-11审议准备包。没有真实Owner反馈或批准证据；CHK-005至CHK-017及CHK-022继续保持Pending。