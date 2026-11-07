# 477｜S1逐对象Owner审议矩阵与决策记录模板

**状态：** Owner Review Preparation；No Owner Approval Recorded

## 1. 角色定义

IA负责实例创建、更新和生命周期；TDA负责字段、类型、状态和约束；SA负责Ontology/Assertion/Evidence关系语义；Physical Custodian负责物理字节、密钥、宿主访问和物理删除；Projection Owner负责Chunk索引、Embedding、Context等派生视图；Policy Authority负责Purpose/Policy/Approval登记和PEP策略；Source Authority负责原始来源内容或外部资源的权威。

## 2. 逐对象审议矩阵

| 对象 | 候选IA | 候选TDA/SA | 必须会审 | 决策焦点 |
|---|---|---|---|
| OT-SOURCE | M08 | M06 | M02、M18、M17 | Source唯一性、Authority、Locator、Rights、Snapshot |
| SourceSnapshot子记录 | M08 | M06 | M02、M18、M17 | 不可变性、采集封套、外部版本、字节保管 |
| OT-RAW-ASSET | M08 | M06 | M02、M18 | 逻辑资产/物理保管、Opaque Handle、Digest、去重、删除 |
| OT-KNOWLEDGE-ASSET | M08 | M06 | M02、M18、M07 | 内容版本、处理版本、分类、Purpose、派生关系 |
| OT-EXTRACTION-RUN | M08 | M06 | M02、M15、M18、Security | 处理器版本、Provider、Region、沙箱、幂等、失败 |
| OT-CHUNK | M08 | M06 | M07、M18 | 父版本、ChunkSet发布、Embedding权限、失效/删除 |
| OT-EVIDENCE | M08 | M06 | M17、M18 | TargetRef、Locator、Digest、Excerpt、Assertion关系权威 |

## 3. 逐对象审议问题

### OT-SOURCE
1. 稳定身份命名空间如何定义？
2. SourceAuthority是否允许多值，如何区分外部提供者和原始事实权威？
3. Locator历史如何保留、失效和受限读取？
4. Rights Snapshot与当前Rights状态如何关联？
5. SourceSnapshot作为子记录是否满足身份、生命周期和审计要求？

### OT-RAW-ASSET
1. M02返回的Opaque Handle有哪些生命周期和访问边界？
2. RawAsset Digest算法和范围如何统一？
3. 跨租户去重是否允许，如何防止存在性泄露？
4. 物理删除回执如何证明字节退出主存、备份和副本？
5. M08逻辑删除和M02物理删除如何对账？

### OT-KNOWLEDGE-ASSET
1. 内容版本和处理版本是否严格分离？
2. 复合知识资产如何表达多Source/RawAsset输入？
3. `processing_purpose_refs`是否明确仅为历史血缘？
4. Processing State与Quality Assessment是否独立？
5. 删除原始输入后，派生内容是否可继续保留及依据是什么？

### OT-EXTRACTION-RUN
1. Run记录保留范围和保留期限如何确定？
2. Parser/OCR/ASR配置摘要如何避免秘密泄露？
3. Provider/Region/Retention如何绑定具体Invocation？
4. Partial/UnknownOutcome的终态如何处理？
5. 运行中Rights/Consent撤销如何Fence？

### OT-CHUNK
1. Chunk是否绑定唯一Asset Version和Run？
2. ChunkSet是否作为子记录管理？
3. Embedding是否作为Projection而非新增OT？
4. Chunk级分类如何继承/提高？
5. Chunk/Embedding如何参与删除闭包？

### OT-EVIDENCE
1. EvidenceTargetRef联合分支是否足够？
2. Locator Schema如何版本化和重定位？
3. 是否允许Excerpt，策略由谁决定？
4. M08与M06关系维护边界如何落账？
5. Receipt/Observation目标如何保持原Owner权威？

## 4. 决策记录模板

每项决策记录：`decision_id`、`object_type_id`、`field_or_relation_id`、`question`、`options`、`recommended_option`、`owner_module`、`attendees`、`decision`、`rationale`、`scope`、`effective_version`、`approval_evidence_ref`、`decided_at`、`follow_up_actions`。

## 5. 审议状态与争议升级

状态词汇：`NotScheduled`、`Prepared`、`InReview`、`OwnerApproved`、`ApprovedWithConditions`、`Rejected`、`Deferred`。只有真实会议/书面确认和可追踪证据才能标记OwnerApproved。当前所有议题均为Prepared/Pending。

跨模块冲突先明确各自权威边界，再提交架构决策；不得以多数意见替代法定授权，也不得由M08单方决定M02/M06/M18权责。影响OD的议题必须进入OD决策台账。


## 6. OF-006既有多维权威分配的遵循

本阶段严格沿用312号OF-006角色分配：六个对象的候选实例维护责任/IA为M08；类型定义权威TDA为M06；语义权威SA为M06；原始字节Physical Custodian为M02；Policy Authority为M18。Provider/平台标准引用外部规范或M15目录。字段级Profile是TDA审议材料，不因文档作者或实例维护模块而改变TDA归属。

若后续Owner希望调整TDA/SA，必须提交明确的架构变更和决策证据，不能在字段表中静默改写角色分配。