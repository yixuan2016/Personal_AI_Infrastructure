# 576｜Evidence字段逐项审查包：Target定位与Assertion核验

**状态：** Field-Level Design Review Candidate；Owner Feedback 22/22 Pending；No Approval

## 1. 对象边界

Evidence保存可定位、可追溯的证据引用和完整性信息；Assertion表达事实主张；Verification负责核验。Evidence存在、Digest匹配或来源可访问均不能自动证明Assertion为真。D-12为主决策，D-04/D-06提供目的与完整性约束。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| EVD-001 | `evidence_id` | evidence_id稳定且不可复用；撤回后是否保留审计身份。 | D-12 |
| EVD-002 | `evidence_kind` | evidence_kind受控分类能否区分原始材料、Receipt、摘录、观察记录和外部证明。 | D-12 |
| EVD-003 | `evidence_target_ref` | evidence_target_ref采用类型化目标；仅允许Registry批准的对象和子记录。 | D-12 |
| EVD-004 | `target_version_ref` | target_version_ref是否固定目标版本；动态目标如何保存核验时解析快照。 | D-12 |
| EVD-005 | `locator_schema_ref` | locator_schema_ref是否版本化；页码、段落、表格、消息和媒体坐标如何统一。 | D-12 |
| EVD-006 | `locator_payload` | locator_payload只保存定位坐标；不得包含Token、Cookie、签名URL秘密或绕过授权凭据。 | D-12 |
| EVD-007 | `target_content_digest` | target_content_digest摘要哪个目标版本及内容范围；算法与Scope必须明确。 | D-12 |
| EVD-008 | `locator_fragment_digest` | locator_fragment_digest摘要哪一片段；片段规范化和定位漂移如何处理。 | D-12 |
| EVD-009 | `excerpt_ref` | excerpt_ref指向可控摘录副本；访问权限、来源版本和保留规则如何继承。 | D-12 |
| EVD-010 | `excerpt_digest` | excerpt_digest覆盖摘录原始还是规范化文本；不能替代Target Digest。 | D-12 |
| EVD-011 | `integrity_state` | integrity_state只表达技术完整性/可验证性；不得映射为来源可信或Assertion Verified。 | D-12 |
| EVD-012 | `lifecycle_state` | lifecycle_state区分有效、过期、撤回、受限和删除；与integrity_state分离。 | D-12 |
| EVD-013 | `created_by_ref` | created_by_ref表示Evidence创建主体；不自动赋予Assertion核验权。 | D-12 |
| EVD-014 | `created_at` | created_at是Evidence创建时间；来源事件时间应另行定位。 | D-12 |
| EVD-015 | `recorded_at` | recorded_at记录进入系统时间；迟到证据和回填时间如何审计。 | D-12 |
| EVD-016 | `classification_ref` | classification_ref按目标和摘录中更严格级别继承；不得降级。 | D-04/D-12 |
| EVD-017 | `purpose_lineage_refs` | purpose_lineage_refs记录证据采集/使用目的；下游主张使用需独立Policy检查。 | D-04/D-12 |
| EVD-018 | `retention_profile_ref` | retention_profile_ref处理原件、摘录、摘要和审计引用的不同保留要求。 | D-12 |
| EVD-019 | `object_version` | object_version表示Evidence元数据修订；Target Version不能随之漂移。 | D-12 |
| EVD-020 | `withdrawal_reason_ref` | withdrawal_reason_ref区分来源撤权、目标错误、反证、定位失效和主体撤回。 | D-12 |
| EVD-021 | `deletion_state_ref` | deletion_state_ref区分内容删除、Projection撤除、引用失效和保留例外。 | D-12 |
| EVD-022 | `captured_at` | captured_at记录证据材料被捕获的时间；与创建和入库时间分离。 | D-12 |

## 3. 对象内一致性约束

- evidence_target_ref必须是受控类型化引用；target_version_ref固定核验目标版本。
- locator_schema_ref和locator_payload只负责定位，不承担访问授权。
- target_content_digest、locator_fragment_digest、excerpt_digest具有不同Scope，不可互相替代。
- integrity_state与lifecycle_state分离；来源可信度和Assertion Verification不由本对象单字段表达。
- created_by_ref不自动获得核验权；核验主体、方法、证据集合和异议应在相应核验流程中记录。
- withdrawal_reason_ref触发下游Assertion/Decision/Memory影响评估；deletion_state_ref需区分内容删除与引用失效。

## 4. 当前结论

22/22字段完成设计审查问题登记；Owner状态22/22 Pending；无Evidence/Assertion字段或核验状态获批。

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