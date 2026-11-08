# 571｜SourceSnapshot字段逐项审查包：不可变采集与Correction

**状态：** Field-Level Design Review Candidate；Owner Feedback 22/22 Pending；No Approval

## 1. 子记录边界

SourceSnapshot是M08管理的不可变采集子记录候选，不是新增OT。它固定某个Source在一次采集时点所观察/获取的状态。更正应追加新的Snapshot或Correction关系，不得原位覆盖已采集历史。D-02/D-03/D-04/D-06/D-07共同约束。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| SNP-001 | `snapshot_id` | snapshot_id是否不可变且唯一；内容相同的重复采集如何表达。 | D-03 |
| SNP-002 | `source_ref` | source_ref是否固定Source身份；来源后续更名或合并是否影响历史Snapshot。 | D-03 |
| SNP-003 | `snapshot_sequence` | snapshot_sequence作用域、递增规则、并发采集和缺号语义是否明确。 | D-03 |
| SNP-004 | `capture_state` | capture_state区分计划、进行中、部分、成功、失败和校验失败；失败快照能否被消费。 | D-03 |
| SNP-005 | `captured_at` | captured_at记录采集动作发生时间；时间来源、精度和可信度如何表达。 | D-03 |
| SNP-006 | `acquired_at` | acquired_at记录内容获取时间还是外部时间；与captured_at为何不同。 | D-03 |
| SNP-007 | `capture_method` | capture_method是否受控；人工、Connector、API、文件导入和批量同步如何区分。 | D-03 |
| SNP-008 | `captured_locator_ref` | captured_locator_ref是否固定采集时Locator；失效或凭据过期不应改写历史。 | D-02 |
| SNP-009 | `external_version_token` | external_version_token由外部系统提供还是本地推断；不稳定Token如何标注。 | D-03 |
| SNP-010 | `raw_asset_refs` | raw_asset_refs是否只引用已登记RawAsset；部分捕获和多文件组成如何表达。 | D-03 |
| SNP-011 | `captured_bytes_digest` | captured_bytes_digest摘要的字节范围、规范化、算法和校验主体是否明确。 | D-06 |
| SNP-012 | `digest_scope` | digest_scope是否版本化、可枚举；压缩、封装、分段和多文件场景如何定义。 | D-06 |
| SNP-013 | `rights_snapshot_ref` | rights_snapshot_ref是否保存采集时权利状态及来源；不能被当前权利覆盖。 | D-04 |
| SNP-014 | `purpose_ref` | purpose_ref是否对应本次采集目的；目的变更是否触发重新授权。 | D-04 |
| SNP-015 | `policy_decision_ref` | policy_decision_ref是否绑定Actor、Source、Action、Purpose和采集时Policy版本。 | D-04 |
| SNP-016 | `applicable_basis_refs` | applicable_basis_refs区分Consent、合同、法定义务等依据；多依据冲突如何处理。 | D-04 |
| SNP-017 | `data_subject_refs` | data_subject_refs是否继承并可修正；主体不明时是否限制后续处理。 | D-04 |
| SNP-018 | `classification_ref` | classification_ref是否记录采集时分类；分类升级如何触发派生数据重评。 | D-04 |
| SNP-019 | `retention_profile_ref` | retention_profile_ref是否固定采集时适用的保留规则版本和触发起点。 | D-04 |
| SNP-020 | `capture_actor_ref` | capture_actor_ref记录实际执行人或服务；委托、代理和自动化身份如何审计。 | D-07 |
| SNP-021 | `recorded_at` | recorded_at与captured_at分离的目的、时钟来源和不可回填规则。 | D-07 |
| SNP-022 | `snapshot_manifest_digest` | snapshot_manifest_digest覆盖哪些Snapshot组成项；清单本身如何防篡改和验证。 | D-06 |

## 3. 不可变性约束

- Snapshot ID与Sequence在Source作用域内唯一；并发采集需有明确排序和冲突处理。
- capture_state描述采集过程，不能把失败/部分采集包装为有效完整Snapshot。
- captured_at、acquired_at、recorded_at分别表达采集动作、内容获取和系统登记时间。
- external_version_token是来源提供的事实或明确标注的本地推断，不能伪装成权威版本。
- raw_asset_refs、captured_bytes_digest、digest_scope和snapshot_manifest_digest必须覆盖一致的成员范围。
- rights_snapshot_ref固定采集时权利证据；当前权利变化不能改写历史Snapshot，但会影响后续使用。
- policy_decision_ref必须对应采集时Actor、Action、Purpose、Source和Policy版本。

## 4. Correction与删除

Correction必须保留被更正Snapshot及其原始证据引用，记录原因、发起主体、依据和关联的新记录。不可变不等于永不删除；Retention、Legal Hold和删除请求须按D-07处理，必要时保留最小审计元数据。

## 5. 当前结论

22/22字段完成设计审查问题登记；Owner状态22/22 Pending；SourceSnapshot仍为子记录候选，不新增OT，不批准任何Snapshot字段变更。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 22/22 与Stage35原始台账一致 |
| 语义审查问题 | 22/22 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。