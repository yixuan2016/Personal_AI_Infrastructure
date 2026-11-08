# 551｜KnowledgeAsset内容版本模型与更正规则

**状态：** Version Model Candidate；No Profile Delta Approved

## 1. 设计目标

为KnowledgeAsset建立稳定逻辑身份与不可变内容版本之间的清晰关系，使任意一次检索、ExtractionRun、Chunk发布、Evidence引用或用户复核，都能明确回答“使用的是哪一个内容版本”。本模型深化D-08，不新增OT/OF，也不预先批准字段扩展。

## 2. 身份与版本分离

- KnowledgeAsset ID：代表逻辑知识资产的持续身份，不因内容更新而改变。
- Content Version：代表该资产在某一时点的具体内容状态，应可独立引用并保持不可变。
- Object Version：代表KnowledgeAsset元数据、生命周期或当前指针的修订，不等于Content Version。
- Source Snapshot Version：代表来源采集时点，不等于KnowledgeAsset Content Version。
- ExtractionRun Version/Processor Version：描述加工过程和工具版本，不等于输入内容版本。

## 3. KAS-006与KAS-007语义候选

KAS-007 asset_versions应表达可追溯的内容版本集合；每个版本必须能关联输入SourceSnapshot/RawAsset、产生该版本的ExtractionRun或人工更正来源、内容摘要、创建时间和更正/替代关系。上述是语义要求，不代表当前字段已经完整承载全部属性；如需新增字段、子记录或新对象，必须单独走ACR/OD及Owner批准。

KAS-006 current_asset_version_ref是当前默认版本指针。指针更新不得修改旧版本内容；更新必须产生可审计的对象修订，并记录触发原因、决策主体和生效时间。

## 4. 版本状态与转换候选

Candidate → Validated → Current → Superseded → Retained/Expired → DeletionPending → Deleted/DeletionBlocked。该序列仅为语义候选；版本状态、资产生命周期和物理保管状态必须正交，不能把一个枚举混合所有状态。

失败或部分完成的ExtractionRun不得生成可发布的Current Version。人工更正应生成新版本或追加更正关系，不得原位改写历史内容。

## 5. 指针更新与并发

多个处理流程可能并行产生候选版本。必须定义冲突检测、预期父版本、提交顺序、Owner决策和回滚语义。禁止“最后写入者获胜”静默覆盖Current Version；冲突时保留候选并进入人工或策略裁决。

## 6. 历史可复现

任何下游对象都应固定其输入版本：ExtractionRun记录输入引用和Digest；Chunk绑定Asset Version与Run；Evidence绑定目标版本；Projection绑定ChunkSet版本。只保存“最新”或“当前”引用不足以重建历史。

## 7. 更正、撤回与删除

更正表示历史内容存在错误并产生新的权威版本；撤回表示某证据/主张不再可用或不再被支持；删除表示依照适用规则处置对象及其副本。三者不能互相替代。Legal Hold、保留义务和安全限制必须单独表达。

## 8. 当前状态

本模型供D-08审议。KAS-006/007仍为Pending；没有新增字段、OT或正式Profile Delta获批。