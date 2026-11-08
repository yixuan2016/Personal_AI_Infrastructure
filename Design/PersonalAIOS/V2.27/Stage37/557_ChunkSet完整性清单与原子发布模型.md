# 557｜ChunkSet完整性清单与原子发布模型

**状态：** ChunkSet Publication Model Candidate；No New OT Approved

## 1. 设计目标

D-11要求检索消费者只能看到可证明完整、版本一致且通过权限检查的Chunk集合。ChunkSet在本阶段仅作为Chunk的集合/发布边界候选，不自动成为独立OT。

## 2. 集合身份与绑定关系

一个ChunkSet应明确绑定：
- KnowledgeAsset稳定身份及Content Version；
- ExtractionRun身份及终态；
- Chunk Strategy及其版本；
- ChunkSet自身集合版本；
- 成员清单、成员数量和顺序规则；
- 内容摘要与Manifest Digest；
- Classification、Purpose Lineage和Retention引用；
- 生成与验证时间、发布主体及发布依据。

如现有字段不能承载这些信息，应先标记Schema Gap并走变更治理，不得静默扩展CHK字段或新增OT。

## 3. 完整性检查

发布前至少检查：成员数与Manifest一致；sequence无重复和缺口；chunk_id唯一；每个Chunk绑定同一资产内容版本、ExtractionRun和Strategy；内容引用可解析；Digest Scope明确；权限与Purpose血缘齐全；失败成员和孤儿成员已处理。

## 4. 原子发布候选

- Building：集合生成中，消费者不可见；
- ValidationPending：成员已登记，等待完整性和权限核验；
- ReadyToPublish：校验完成，等待发布授权；
- Published：完整集合对授权消费者可见；
- Superseded：被新集合替代，历史仍可追溯；
- Revoked/DeletionPending：访问被撤销或进入删除流程。

这些是候选状态，不等于已批准的CHK-017枚举。状态迁移须有M08/M07/M18责任分工和审计记录。

## 5. 原子性与部分失败

默认建议以完整集合为可见性边界。若部分成员失败，整个集合保持不可发布，除非Owner明确批准一种可解释的部分集合语义，并确保消费者可见其缺失范围。不得以部分成功伪装完整发布。

## 6. 版本并存

新ChunkSet发布后，旧集合可进入Superseded，但不应立即删除其历史身份。查询必须明确选择版本策略：固定版本、当前Published版本或时间点版本。Evidence引用必须能够固定具体Chunk/Set Version。

## 7. 当前状态

本文件只提供ChunkSet发布模型候选。没有新增OT、没有正式字段变更，也没有集合发布测试执行。