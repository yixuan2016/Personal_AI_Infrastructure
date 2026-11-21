# 490｜KnowledgeAsset Owner审议工作包

**状态：** Field-level Review Pack Prepared；Owner Decision Pending  
**审议对象：** KnowledgeAsset  
**本包字段定义数：** 16

## 1. 对象边界与权威候选

KnowledgeAsset是逻辑知识资产身份及内容版本集合；处理器版本变化不等于原始内容版本变化。

候选角色沿用312号OF-006既有分配：IA=M08；TDA/SA=M06。凡涉及M02物理保管、M18策略治理、M15 Provider/Region、M17 Receipt或M07 Projection/Context的议题，必须由对应模块在其权限范围内独立审议。此处复述候选角色不构成新增批准。

## 2. 字段逐项审议清单

以下清单逐项对应V2.21字段Profile，不表示任何字段已获批准。每个字段至少核对：语义定义、类型、Cardinality、必填条件、缺失语义、可变性、写入权威、敏感度、校验、版本影响、血缘、删除和兼容性。

| Field ID | 字段 | Owner审议焦点 | 应提供的证据 | 候选审议方 |
|---|---|---|---|---|
| `KAS-001` | `knowledge_asset_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `KAS-002` | `asset_kind` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `KAS-003` | `display_name` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `KAS-004` | `source_snapshot_refs` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `KAS-005` | `raw_asset_refs` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `KAS-006` | `current_asset_version_ref` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `KAS-007` | `asset_versions` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `KAS-008` | `lifecycle_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `KAS-009` | `classification_ref` | 确认对象/字段/片段/派生物分类继承与提高规则，禁止降级 | 分类目录映射、继承/提高案例 | M18；Security/Privacy |
| `KAS-010` | `retention_profile_ref` | 确认保留策略引用、期限来源、例外与删除传播，不在Profile中硬编码期限 | Retention Profile目录和例外审批路径 | M18；Privacy/Legal |
| `KAS-011` | `created_by_ref` | 确认Actor/Service身份、发起者与执行者区分及审计最小化 | 身份目录映射、授权主体和审计事件样例 | M08 / M18 |
| `KAS-012` | `created_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `KAS-013` | `updated_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `KAS-014` | `object_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `KAS-015` | `processing_purpose_refs` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `KAS-016` | `deletion_dependency_refs` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |

## 3. 本对象关键审议焦点

1. KAS-004/005：多SourceSnapshot/RawAsset输入与权利边界保留。
2. KAS-006/007：current_asset_version_ref必须指向asset_versions中的精确不可变版本。
3. KAS-008/009/010：生命周期、分类、保留分别治理，不能互相推导。
4. KAS-015：processing_purpose_refs仅表示历史处理用途，不授予未来处理权限。
5. KAS-016：删除依赖必须覆盖Chunk、Embedding、Summary、Context、Cache和Provider派生物。

## 4. 必须形成原子决策的议题

- 复合资产多来源血缘
- 内容版本与处理版本分离
- Processing State/Quality/Verification正交
- 历史Purpose与当前授权
- 删除依赖闭包与派生资产重建

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
