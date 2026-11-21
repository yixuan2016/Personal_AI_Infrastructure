# 492｜Chunk与ChunkSet Owner审议工作包

**状态：** Field-level Review Pack Prepared；Owner Decision Pending  
**审议对象：** Chunk  
**本包字段定义数：** 22

## 1. 对象边界与权威候选

Chunk是精确KnowledgeAsset Version经指定ExtractionRun生成的派生片段；ChunkSet是父对象子记录，Embedding是可重建Projection。

候选角色沿用312号OF-006既有分配：IA=M08；TDA/SA=M06。凡涉及M02物理保管、M18策略治理、M15 Provider/Region、M17 Receipt或M07 Projection/Context的议题，必须由对应模块在其权限范围内独立审议。此处复述候选角色不构成新增批准。

## 2. 字段逐项审议清单

以下清单逐项对应V2.21字段Profile，不表示任何字段已获批准。每个字段至少核对：语义定义、类型、Cardinality、必填条件、缺失语义、可变性、写入权威、敏感度、校验、版本影响、血缘、删除和兼容性。

| Field ID | 字段 | Owner审议焦点 | 应提供的证据 | 候选审议方 |
|---|---|---|---|---|
| `CHK-001` | `chunk_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `CHK-002` | `knowledge_asset_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-003` | `asset_version_ref` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `CHK-004` | `extraction_run_ref` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `CHK-005` | `chunk_set_id` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-006` | `chunk_set_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `CHK-007` | `chunk_sequence` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `CHK-008` | `content_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-009` | `text_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `CHK-010` | `locator_in_parent` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `CHK-011` | `token_range` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-012` | `character_range` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-013` | `chunk_strategy_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-014` | `language_refs` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-015` | `classification_ref` | 确认对象/字段/片段/派生物分类继承与提高规则，禁止降级 | 分类目录映射、继承/提高案例 | M18；Security/Privacy |
| `CHK-016` | `purpose_lineage_refs` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `CHK-017` | `projection_state` | 确认派生投影可重建、权限不低于源资产且撤销后失效 | Projection Owner映射、重建与失效闭包 | M07 / M08；M18 |
| `CHK-018` | `supersedes_chunk_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `CHK-019` | `created_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `CHK-020` | `retention_profile_ref` | 确认保留策略引用、期限来源、例外与删除传播，不在Profile中硬编码期限 | Retention Profile目录和例外审批路径 | M18；Privacy/Legal |
| `CHK-021` | `object_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `CHK-022` | `deletion_state_ref` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |

## 3. 本对象关键审议焦点

1. CHK-002/003/004：父Asset、精确Asset Version和ExtractionRun必须一致。
2. CHK-005/006/007：ChunkSet身份、版本和序号应支持完整Manifest校验。
3. CHK-008/009/010：内容引用、文本Digest和父文档Locator坐标必须可复核。
4. CHK-011/012/013：Token/Character范围须绑定Tokenizer、编码和分段策略版本。
5. CHK-015/016/017：分类不得低于源内容；Purpose Lineage不是当前授权；Projection State可失效。
6. CHK-020/022：保留和删除状态必须传播到Embedding、Index、Context及备份。

## 4. 必须形成原子决策的议题

- Chunk/ChunkSet发布完整性门禁
- 父版本与Run一致性
- 坐标系、编码和Tokenization版本
- Embedding/Index投影权威
- 分类与Purpose传播
- 撤销、失效、删除和重建

每项议题应单独登记Decision ID，不得用“本对象整体通过”掩盖字段级保留意见。建议至少形成以下结论之一：Retain、Revise、Split、Merge、Deprecate、Remove、Defer、Need-ACR或Blocked。

## 5. 需要提交的审议证据

- 当前Profile版本和字段清单；
- 引用目标在既有Object Type Registry/词汇目录/父对象子记录中的解析证据；
- 字段权威、写入者、读取者及PEP控制映射；
- 正向和负向合成样例；
- 对下游Command/Query/Event、Projection、删除和备份恢复的影响；
- 异议、例外、风险接受及批准范围。

## 6. 审议结束条件

1. 每个字段均有审议状态和处置建议；
2. 所有Required/Unknown/Withheld/Empty等缺失语义得到明确处理；
3. 跨Owner字段均有实际有权Owner确认或明确标记Blocked；
4. 所有未决项均有责任人、依赖、后续动作和目标版本；
5. 批准结论有可核验的Approval Evidence Ref。

## 7. 当前结论

本包仅完成审议准备。没有真实Owner决议证据时，所有字段仍为Proposed，所有OT仍为Candidate。不得把本清单当作签署表或冻结批准。
