# 552｜KnowledgeAsset派生依赖清单与删除闭包治理

**状态：** Deletion Closure Design Candidate；No Deletion Execution

## 1. 目的

D-08要求删除KnowledgeAsset时，不只检查主记录，还要识别所有可从该资产恢复、检索、展示、推理或再次处理其内容的派生副本。删除闭包必须从依赖图计算并由各物理/逻辑权威分别确认，不能由M08单方面宣告完成。

## 2. 派生依赖范围

| 层级 | 典型依赖 | 责任候选 |
|---|---|---|
| 来源与原始资产 | SourceSnapshot、RawAsset、物理副本 | M08、M02 |
| 知识版本 | KnowledgeAsset Content Version、历史版本 | M08、M06 |
| 加工运行 | ExtractionRun输入/输出、临时文件 | M08、M15 |
| 分块 | Chunk、ChunkSet成员和内容引用 | M08、M06 |
| 语义投影 | Embedding、Index、Search Cache、Context Projection | M07 |
| 交付副本 | Export、下载副本、报告、生成文件 | 具体交付模块及Owner |
| 外部处理 | Provider输入、输出、缓存、日志、支持工单和子处理商副本 | M15、Provider、M18 |
| 证据与主张 | Evidence、Assertion引用、决策记录和审计记录 | M08、M06及目标Owner |
| 可靠性副本 | Backup、Replica、Archive、Disaster Recovery | M02及对应系统Owner |

## 3. 删除闭包的计算原则

1. 从目标KnowledgeAsset和指定版本出发，沿所有正向派生边遍历。
2. 对每个依赖记录对象身份、版本、数据类型、位置/权威、用途、分类、Retention、Policy和可删除能力。
3. 对反向引用进行影响分析，识别仍被Evidence、Assertion、Decision或其他资产引用的对象。
4. 区分“必须删除的内容副本”“需要失效的检索/投影视图”“依法或依规保留的审计证据”和“需要保留但限制访问的记录”。
5. 任何依赖未知、Provider副本不明或副本清单不完整时，闭包状态不得标记Complete。

## 4. 删除状态分层

RequestReceived、ScopeResolved、PolicyEvaluated、DependencyEnumerated、DeletionDispatched、ProviderPending、ProjectionPending、PhysicalCustodyPending、ReceiptVerified、ExceptionsRecorded、ClosureVerified。它们是跨模块流程阶段候选，不是新增OT状态字段的批准。

逻辑Tombstone、检索不可见、在线字节删除、备份到期、Provider删除、密钥销毁和审计保留必须分别记录。部分完成必须显式显示未完成项和责任Owner。

## 5. 例外与冲突

Legal Hold、法定留存、争议保全、审计要求和安全调查可能限制立即删除。例外必须明确法律/Policy依据、对象范围、保留期限、访问隔离、批准角色和复审时间。例外不是默许无限保留，也不能由AI自行判定。

## 6. 关闭证据

闭包关闭至少需要：依赖清单快照、各模块处置回执、Provider/子处理商回执、Projection移除确认、M02物理处置回执、未完成项和例外记录、独立复核。没有物理回执时，不得表述为物理删除已完成。

## 7. 当前状态

本文件只设计删除闭包治理，不执行真实删除，不改变任何Retention或Legal Hold政策。