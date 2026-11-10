# 495｜S1字段处置台账与原子决策记录Schema

**状态：** Decision Ledger Schema Candidate；No New Decision Recorded

## 1. 目的

将Owner审议结果转化为可审计的原子决策，避免把一场会议、一份邮件或一个Profile状态当成不可分解的批准。台账同时记录字段处置、决策证据、依赖、异议和基线传播。

## 2. 双层台账

### 2.1 Field Disposition Record

| 字段 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `disposition_id` | Stable ID | 是 | 字段处置记录唯一身份 |
| `baseline_id` | Ref<Baseline> | 是 | 产生该处置的父基线 |
| `object_type_id` | OT ID | 是 | 六个既有OT之一 |
| `field_id` | Field ID | 是 | 指向唯一字段 |
| `profile_version` | Version | 是 | 被审议Profile版本 |
| `review_status` | Enum | 是 | Prepared/InReview/ClarificationRequired/OwnerApproved等 |
| `proposed_disposition` | Enum | 是 | Retain/Revise/Split/Merge/Deprecate/Remove/Defer/NeedACR/Blocked |
| `owner_module_id` | Module ID | 是 | 具有该项决定权的Owner |
| `reviewer_refs` | Ref集合 | 是 | 会审人员/角色 |
| `rationale` | Text | 是 | 事实和理由 |
| `evidence_refs` | Ref集合 | 是 | 依据和样例 |
| `impact_refs` | Ref集合 | 是 | 受影响字段/关系/契约/测试 |
| `approval_evidence_ref` | Ref | 条件必需 | Owner批准证据 |
| `effective_version` | Version | 批准后必需 | 生效基线/契约版本 |
| `supersedes_ref` | Ref | 适用时 | 被替代的旧处置 |
| `recorded_at` | Instant | 是 | 登记时间 |

### 2.2 Atomic Decision Record

每个原子决策至少包含：`decision_id`、`decision_type`、`question`、`options`、`recommended_option`、`selected_option`、`decision_owner`、`authority_basis`、`attendees`、`decision_text`、`rationale`、`scope`、`conditions`、`exceptions`、`effective_version`、`approval_evidence_ref`、`decided_at`、`follow_up_actions`、`impact_analysis_ref`、`supersedes_ref`。

## 3. 状态与处置分离

审议状态描述“走到哪一步”；处置描述“建议怎么处理”；批准状态描述“有权Owner是否明确接受”。例如：
- `InReview + ProposedRetain`：正在审议，建议保留；
- `ClarificationRequired + ProposedRevise`：需要补充信息；
- `OwnerApproved + Retain`：仅当批准证据有效时成立；
- `Blocked + NeedACR`：需架构变更，不可直接改基线。

## 4. 不允许的简化

- 不允许只写“Profile Approved”而不列批准字段范围；
- 不允许将参会人全部视为决策人；
- 不允许把沉默、未回复或口头赞同当批准；
- 不允许由文档作者替Owner填写`selected_option`；
- 不允许删除被拒绝的选项和历史版本；
- 不允许以一个字段批准推导所有下游字段/契约批准。

## 5. 质量校验

批准记录必须通过：Owner身份核验、权限范围核验、版本核验、对象/字段范围核验、决议文本明确性、条件可验证性、证据可访问性、影响传播完整性和独立复核。缺少任何一项时，状态不得为OwnerApproved。

## 6. 合成示例（非真实决策）

`decision_id=S1-REV-EXAMPLE-001`、`field_id=SRC-005`、`review_status=InReview`、`proposed_disposition=ProposedRevise`、`selected_option=null`、`approval_evidence_ref=null`。该示例仅演示字段结构，不代表任何Owner提出或批准了修改。
