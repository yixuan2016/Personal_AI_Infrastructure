# 546｜D-08 KnowledgeAsset版本与删除闭包：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

KnowledgeAsset是逻辑知识资产。其名称、元数据、生命周期和当前版本指针可能变化，但内容版本、来源血缘和历史派生结果必须可追溯。删除一个KnowledgeAsset也不能只删除主记录：其Chunk、Embedding/Index Projection、缓存、上下文副本、导出物和Provider处理副本可能仍存在。

## 2. 关联字段与权威边界

- KAS-006 current_asset_version_ref
- KAS-007 asset_versions
- KAS-016 deletion_dependency_refs
- 联动KAS-004/005来源引用、KAS-008生命周期、KAS-009分类、KAS-010保留、KAS-014对象版本、KAS-015处理目的。
- 主决定权威候选：M08负责实例、版本引用和生命周期；M06负责版本及派生关系语义；必须会审M07 Projection、M18 Policy/Retention。物理字节删除由M02负责。

## 3. 必须回答的问题

1. KnowledgeAsset的稳定身份与内容版本身份如何区分？
2. asset_versions是版本记录引用、版本描述集合还是版本序列？每个版本是否不可变？
3. current_asset_version_ref是可变指针还是版本本身？指针更新如何保留历史？
4. 新版本由重新采集、重新提取、人工更正或合并产生时，如何表达原因和supersedes关系？
5. 不同版本的SourceSnapshot、RawAsset、ExtractionRun和Chunk如何关联？
6. deletion_dependency_refs是否能表达完整派生闭包，如何防止遗漏外部Provider和M07 Projection？
7. Retention、Legal Hold、Consent撤回与本人删除请求冲突时，如何表达待处理、受限和例外？
8. 逻辑删除、Projection移除、缓存清理、Provider删除和M02物理删除分别由谁确认？

## 4. 候选方案（不构成推荐或批准）

- A：KnowledgeAsset身份稳定，内容版本以不可变版本记录表达，当前版本只作为可变指针；版本血缘和删除依赖分别追踪。
- B：KnowledgeAsset按内容版本拆分为多个独立逻辑对象，再用系列关系聚合；历史语义显式，但会增加对象数量和跨版本治理复杂度。
- C：保留一个对象及版本数组，版本差异嵌入元数据；结构较轻，但必须证明版本项不可被覆盖且可被独立引用。

## 5. 必须提供的证据

- KAS-006/007/016现行Profile及所有消费者；
- 真实或合成的内容更新、更正、回滚、合并和历史引用场景；
- M07索引/Embedding/Context Projection清单及删除接口责任；
- M18 Retention、Legal Hold和撤回规则；
- M02物理副本与删除回执能力；
- Provider处理结果、导出、缓存和日志的副本清单。

## 6. 下游影响与测试

影响Knowledge查询、检索、Chunk、Embedding、Context、Evidence、RSI评估、导出和删除。消费者必须明确读取某个固定版本还是当前版本，不得把current pointer变化解释为历史内容被修改。

测试覆盖当前指针切换、历史版本仍可定位、版本内容覆盖拒绝、Correction追加、旧Chunk失效、跨版本Evidence引用、删除依赖遗漏、Legal Hold阻断、Provider副本未确认删除。

## 7. 阻断条件

版本身份和对象身份混淆；历史版本可被原位覆盖；当前指针没有并发控制；删除闭包无法枚举；M07/M18/M02责任未明确；外部副本无法核验。

## 8. 当前状态

本文件仅形成D-08审议准备包。没有真实Owner反馈、正式Decision Record或批准证据；KAS字段继续保持Stage35台账状态。