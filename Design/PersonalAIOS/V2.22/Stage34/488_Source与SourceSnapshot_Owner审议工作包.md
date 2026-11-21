# 488｜Source与SourceSnapshot Owner审议工作包

**状态：** Field-level Review Pack Prepared；Owner Decision Pending  
**审议对象：** Source、SourceSnapshot  
**本包字段定义数：** 37

## 1. 对象边界与权威候选

Source身份与一次采集事实分离；Locator可变、Snapshot不可变；Source Rights与当前处理依据分离。

候选角色沿用312号OF-006既有分配：IA=M08；TDA/SA=M06。凡涉及M02物理保管、M18策略治理、M15 Provider/Region、M17 Receipt或M07 Projection/Context的议题，必须由对应模块在其权限范围内独立审议。此处复述候选角色不构成新增批准。

## 2. 字段逐项审议清单

以下清单逐项对应V2.21字段Profile，不表示任何字段已获批准。每个字段至少核对：语义定义、类型、Cardinality、必填条件、缺失语义、可变性、写入权威、敏感度、校验、版本影响、血缘、删除和兼容性。

| Field ID | 字段 | Owner审议焦点 | 应提供的证据 | 候选审议方 |
|---|---|---|---|---|
| `SRC-001` | `source_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `SRC-002` | `source_kind` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `SRC-003` | `source_authority_ref` | 区分原始事实/资源权威、平台提供者、采集者和本地维护者 | 权威主体目录映射、冲突处理规则 | M06 / M08 |
| `SRC-004` | `origin_identity_ref` | 确认命名空间、权威实例、外部资源ID的稳定组合与本地导入例外 | 身份组合示例、碰撞与合并规则 | M06 / M08 |
| `SRC-005` | `locator_refs` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `SRC-006` | `availability_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `SRC-007` | `lifecycle_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `SRC-008` | `source_rights_refs` | 区分来源许可/合同条款与Consent、Processing Basis及当前Policy | 来源权利登记映射、历史快照和撤销示例 | M18 / M08；Privacy/Legal |
| `SRC-009` | `data_subject_refs` | 确认多主体表达、第三方最小化、主体识别不确定性及权限裁剪 | 合成多主体案例、访问矩阵和主体权利路径 | M18；Privacy/Legal |
| `SRC-010` | `classification_ref` | 确认对象/字段/片段/派生物分类继承与提高规则，禁止降级 | 分类目录映射、继承/提高案例 | M18；Security/Privacy |
| `SRC-011` | `created_by_ref` | 确认Actor/Service身份、发起者与执行者区分及审计最小化 | 身份目录映射、授权主体和审计事件样例 | M08 / M18 |
| `SRC-012` | `created_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `SRC-013` | `updated_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `SRC-014` | `object_version` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `SRC-015` | `supersedes_source_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `SNP-001` | `snapshot_id` | 身份生成、命名空间唯一性、不可变性及跨系统碰撞处理 | ID注册规则、唯一性约束和创建责任证据 | M08 / M06 |
| `SNP-002` | `source_ref` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `SNP-003` | `snapshot_sequence` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `SNP-004` | `capture_state` | 确认枚举版本、正交状态维度、合法迁移和不可逆历史 | 状态转换表、非法迁移案例和事件映射 | M08 / M06；涉及治理时M18 |
| `SNP-005` | `captured_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `SNP-006` | `acquired_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `SNP-007` | `capture_method` | 确认语义定义、基数、必填条件、缺失/空值、可变性、校验与兼容分类 | 字段词汇/Schema映射、合成实例和消费者影响 | M08 / M06 |
| `SNP-008` | `captured_locator_ref` | 确认定位值的敏感性、历史追加、失效语义、坐标版本及凭据隔离 | Locator Schema、脱敏样例、失效/重定位流程 | M08；必要时M17 |
| `SNP-009` | `external_version_token` | 确认版本作用域、单调性、并发守卫及与Schema/Contract版本分离 | 版本规则、并发冲突和迁移样例 | M08 / M06 |
| `SNP-010` | `raw_asset_refs` | 确认引用目标已在既有注册表解析、精确版本和血缘基数可校验 | 对象类型映射、版本引用样例和血缘图 | M08 / M06 |
| `SNP-011` | `captured_bytes_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `SNP-012` | `digest_scope` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |
| `SNP-013` | `rights_snapshot_ref` | 区分来源许可/合同条款与Consent、Processing Basis及当前Policy | 来源权利登记映射、历史快照和撤销示例 | M18 / M08；Privacy/Legal |
| `SNP-014` | `purpose_ref` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `SNP-015` | `policy_decision_ref` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `SNP-016` | `applicable_basis_refs` | 确认用途/处理依据/Consent/PolicyDecision各自独立，不将历史用途当作未来许可 | Purpose目录映射、PEP决策证据和撤销传播 | M18；Privacy/Legal |
| `SNP-017` | `data_subject_refs` | 确认多主体表达、第三方最小化、主体识别不确定性及权限裁剪 | 合成多主体案例、访问矩阵和主体权利路径 | M18；Privacy/Legal |
| `SNP-018` | `classification_ref` | 确认对象/字段/片段/派生物分类继承与提高规则，禁止降级 | 分类目录映射、继承/提高案例 | M18；Security/Privacy |
| `SNP-019` | `retention_profile_ref` | 确认保留策略引用、期限来源、例外与删除传播，不在Profile中硬编码期限 | Retention Profile目录和例外审批路径 | M18；Privacy/Legal |
| `SNP-020` | `capture_actor_ref` | 确认Actor/Service身份、发起者与执行者区分及审计最小化 | 身份目录映射、授权主体和审计事件样例 | M08 / M18 |
| `SNP-021` | `recorded_at` | 确认事件时间与登记时间分离、时区/精度、可缺失条件和不可回填规则 | 时间语义表、边界案例和审计样例 | M08 / M06 |
| `SNP-022` | `snapshot_manifest_digest` | 确认算法、版本、规范化、输入范围、生成主体及侧信道风险 | Digest规范、范围样例、重算/不匹配处理 | M08 / M06；涉及原始字节时M02 |

## 3. 本对象关键审议焦点

1. SRC-003/004：Source Authority与Origin Identity不能混为Provider账号或M08采集者。
2. SRC-005与SNP-008：Locator历史引用必须可追溯且不泄露凭据。
3. SNP-005/006/021：captured_at、acquired_at、recorded_at分别表达观察、获取和登记时间。
4. SNP-013/014/015/016：历史Rights Snapshot、当前Purpose、PolicyDecision和适用处理依据必须正交。
5. SNP-010/011/012/022：多部件原始资产、Digest范围和Manifest完整性必须一致。

## 4. 必须形成原子决策的议题

- Source身份命名空间与外部资源唯一性
- SourceAuthority多值及冲突
- Locator保留/失效/受限读取
- Snapshot不可变与Correction机制
- Rights Snapshot与当前Rights/Consent/Processing Basis
- 多主体与第三方隐私
- Capture Partial/Failed/Quarantined语义

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
