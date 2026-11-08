# 573｜KnowledgeAsset字段逐项审查包：内容版本与删除闭包

**状态：** Field-Level Design Review Candidate；Owner Feedback 16/16 Pending；No Approval

## 1. 对象边界

KnowledgeAsset是逻辑知识资产。逻辑身份、内容版本、对象元数据版本、来源版本和处理器版本必须分开。D-08为主决策，D-04/D-07提供权利和删除约束。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| KAS-001 | `knowledge_asset_id` | KnowledgeAsset逻辑身份是否稳定；与内容版本、展示名称和外部ID分离。 | D-08 |
| KAS-002 | `asset_kind` | asset_kind的分类边界、扩展规则和复合资产语义。 | D-08 |
| KAS-003 | `display_name` | display_name是否仅为展示元数据；改名不应改变身份或版本。 | D-08 |
| KAS-004 | `source_snapshot_refs` | source_snapshot_refs是否固定原始来源版本；合并资产如何保留多来源血缘。 | D-08 |
| KAS-005 | `raw_asset_refs` | raw_asset_refs指向逻辑RawAsset还是物理Handle；删除和保留责任如何继承。 | D-08 |
| KAS-006 | `current_asset_version_ref` | current_asset_version_ref是可变指针；并发更新、回滚和历史引用如何保证。 | D-08 |
| KAS-007 | `asset_versions` | asset_versions是否引用不可变内容版本；版本元数据、摘要和supersedes关系是否齐全。 | D-08 |
| KAS-008 | `lifecycle_state` | lifecycle_state与Current Version状态、Retention和Deletion状态是否正交。 | D-08 |
| KAS-009 | `classification_ref` | classification_ref如何从来源和处理结果继承；冲突时采用何种提升规则。 | D-04/D-08 |
| KAS-010 | `retention_profile_ref` | retention_profile_ref适用范围是逻辑资产还是每个版本；更严格规则如何传播。 | D-04/D-08 |
| KAS-011 | `created_by_ref` | created_by_ref记录资产创建者还是内容贡献者；多方贡献如何表达。 | D-08 |
| KAS-012 | `created_at` | created_at是逻辑资产创建时间还是首个内容版本时间。 | D-08 |
| KAS-013 | `updated_at` | updated_at是否只随对象元数据变化；内容更新应由Version表达。 | D-08 |
| KAS-014 | `object_version` | object_version与Content Version分离；并发修订和审计如何实现。 | D-08 |
| KAS-015 | `processing_purpose_refs` | processing_purpose_refs如何保留各派生用途的来源链；是否允许用途扩展。 | D-04/D-08 |
| KAS-016 | `deletion_dependency_refs` | deletion_dependency_refs是否枚举Chunk、Projection、缓存、Provider、导出、日志和备份。 | D-08 |

## 3. 对象内一致性约束

- knowledge_asset_id稳定；display_name可变但不能成为身份。
- current_asset_version_ref是当前指针，asset_versions是可引用的版本集合；历史版本不得原位覆盖。
- object_version表示对象元数据修订，不等于Content Version。
- source_snapshot_refs/raw_asset_refs构成来源血缘；合并资产须保留多来源链。
- processing_purpose_refs是用途血缘而非永久授权；每次读取/处理仍需当前Policy。
- deletion_dependency_refs必须可枚举到Chunk、Projection、Cache、Context、Provider、Export、Log、Backup和Evidence/Assertion引用。

## 4. 删除与更正规则

更正产生新版本并关联旧版本；回滚是Current Pointer重新指向经批准的历史版本或产生回滚版本，不能抹去中间版本。删除闭包需结合反向引用、Retention和Legal Hold，不能简单递归删除所有被引用对象。

## 5. 当前结论

16/16字段完成设计审查问题登记；Owner状态16/16 Pending；无KnowledgeAsset字段批准或版本模型正式批准。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 16/16 与Stage35原始台账一致 |
| 语义审查问题 | 16/16 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。