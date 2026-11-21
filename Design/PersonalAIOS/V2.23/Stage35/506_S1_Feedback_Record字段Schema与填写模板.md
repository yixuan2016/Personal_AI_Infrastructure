# 506｜S1 Feedback Record字段Schema与填写模板

**状态：** Record Schema Candidate；No Actual Owner Feedback Instance

## 1. 设计目标

Feedback Record记录一份原始反馈及其核验过程；Atomic Issue记录从反馈中拆出的单一决策问题；Decision Record记录有权Owner作出的明确结论。三者不得合并为一条自由文本备注。

## 2. Feedback Record字段

| 字段 | 必需 | 语义 |
|---|---|---|
| `feedback_record_id` | 是 | 稳定唯一ID |
| `baseline_id` | 是 | 反馈针对的基线，初始为V2.22-Draft |
| `source_record_ref` | 是 | 原始反馈或受控原件引用 |
| `source_type` | 是 | SignedReview/Email/Meeting/ModuleMemo/ProfessionalReview/Test/AIAnalysis |
| `received_at` | 是 | 接收时间 |
| `source_created_at` | 条件必需 | 原始材料形成时间 |
| `submitted_by_ref` | 是 | 提交者身份引用 |
| `claimed_role` | 是 | 提交者声明角色 |
| `verified_role` | 否 | 核验后的角色 |
| `identity_status` | 是 | Verified/Unverified/Rejected |
| `authority_scope_ref` | 否 | 决定权限范围 |
| `authority_status` | 是 | Verified/Unverified/NotDecisionAuthority |
| `raw_statement_ref` | 是 | 原始意见引用 |
| `normalized_summary` | 是 | 整理摘要，必须与原文分离 |
| `affected_object_refs` | 是 | 相关对象 |
| `affected_field_ids` | 否 | 相关字段ID |
| `affected_contract_refs` | 否 | 相关契约 |
| `evidence_refs` | 否 | 支持材料 |
| `privacy_classification` | 是 | 输入材料的访问/敏感分类 |
| `triage_status` | 是 | 反馈处理状态 |
| `reviewer_ref` | 否 | 归一复核人 |
| `supersedes_ref` | 否 | 被更正/替代的反馈 |
| `recorded_at` | 是 | 登记时间 |

## 3. Atomic Issue字段

每个反馈可拆出多个Atomic Issue，每个Issue只问一个可判定问题：
`issue_id`、`feedback_record_ref`、`issue_type`、`question`、`affected_field_or_relation`、`current_definition`、`requested_change`、`submitter_rationale`、`evidence_refs`、`decision_authority`、`consulted_owners`、`risk_level`、`dependencies`、`test_refs`、`triage_status`。

## 4. Decision Record关联

只有进入Owner审议并形成明确结论时，才建立495号规范中的Decision Record。Feedback Record不直接拥有`selected_option`；反馈提交者也不自动成为Decision Owner。

## 5. 填写模板

```yaml
feedback_record_id: FBR-S1-YYYY-NNN
baseline_id: PAILOS-AB-2.22-S1-OWNER-REVIEW-READINESS
source_record_ref: null
source_type: null
received_at: null
submitted_by_ref: null
claimed_role: null
verified_role: null
identity_status: Unverified
authority_scope_ref: null
authority_status: Unverified
raw_statement_ref: null
normalized_summary: null
affected_object_refs: []
affected_field_ids: []
affected_contract_refs: []
evidence_refs: []
privacy_classification: RestrictedUntilReviewed
triage_status: Received
reviewer_ref: null
supersedes_ref: null
```

## 6. 状态校验

- `identity_status=Unverified`时，不得把提交者写入正式Owner立场；
- `authority_status=NotDecisionAuthority`时，可作为专业输入，但不能作为批准；
- `source_type=AIAnalysis`时，必须标记`approval_eligible=false`；
- `raw_statement_ref`缺失时，不得把摘要作为正式反馈原件；
- `selected_option`和`approval_evidence_ref`属于Decision Record，不属于Feedback Record。

## 7. 合成示例

`FBR-S1-DEMO-001`仅用于说明字段结构，提交者、原始材料和意见均为虚构，不得导入正式审议台账。