# 604｜V2.26基线Feedback Record接收模板与原始材料保全规范

**状态：** Feedback Intake Template V2.27 Candidate；No Actual Feedback Instance

## 1. 适用基线

本模板用于接收针对V2.26-Draft的真实Owner反馈。默认父基线：

- baseline_id：PAILOS-AB-2.26-S1-12DEC-142FIELD-CONSOLIDATION
- baseline_ref：docs/personal-ai-life-os-v2.26
- baseline_commit：311842a8ee2b345345d75b3802ec384a26d6552f

若反馈针对其他Commit、Profile版本或文档，必须另行填写精确版本，不得默认沿用上述值。V2.23/506旧模板保留为历史，不直接覆盖。

## 2. Feedback Record Schema

| 字段 | 必需 | 语义 |
|---|---|---|
| feedback_record_id | 是 | 真实输入登记后分配的稳定ID；不得预造 |
| baseline_id / baseline_commit | 是 | 反馈针对的精确基线与Commit |
| source_record_ref | 是 | 受控原始材料引用 |
| source_type | 是 | SignedReview/Email/Meeting/ModuleMemo/ProfessionalReview/Test/AIAnalysis |
| received_at / source_created_at | 是/条件 | 接收时间与原始材料形成时间分离 |
| submitted_by_ref / claimed_role | 是 | 提交者身份引用及自述角色 |
| verified_role | 核验后 | 经身份/组织目录核验的角色 |
| identity_status | 是 | Verified/Unverified/Rejected |
| authority_scope_ref | 条件 | 该角色对具体对象/字段/决策的授权范围 |
| authority_status | 是 | Verified/Unverified/NotDecisionAuthority |
| raw_statement_ref | 是 | 原始意见原件或受控引用 |
| normalized_summary | 是 | 独立整理摘要，不得替代原文 |
| affected_object_refs | 是 | 涉及对象/子记录 |
| affected_field_ids / relation_ids / contract_refs | 条件 | 精确变更范围 |
| claimed_decision_ids | 条件 | 提交者提及的既有决策，不代表其已批准 |
| evidence_refs | 条件 | 支持材料及反证 |
| privacy_classification | 是 | 原始材料访问分类 |
| triage_status | 是 | Received等反馈处理状态 |
| reviewer_ref | 核验后 | 归一结果复核人 |
| supersedes_ref | 条件 | 更正/替代的旧Feedback Record |
| recorded_at / original_digest | 是 | 登记时间与原始材料完整性信息 |

## 3. 空白模板（不代表真实反馈）

~~~yaml
feedback_record_id: null
baseline_id: PAILOS-AB-2.26-S1-12DEC-142FIELD-CONSOLIDATION
baseline_commit: 311842a8ee2b345345d75b3802ec384a26d6552f
baseline_ref: docs/personal-ai-life-os-v2.26
source_record_ref: null
source_type: null
received_at: null
source_created_at: null
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
relation_ids: []
contract_refs: []
claimed_decision_ids: []
evidence_refs: []
privacy_classification: RestrictedUntilReviewed
triage_status: Received
reviewer_ref: null
supersedes_ref: null
recorded_at: null
original_digest: null
approval_eligible: false
~~~

## 4. 原始材料保全

- 原始邮件、签署文件、会议决议或工作记录只读保存；更正以追加Correction记录，不覆盖原文。
- 普通Git仓库只存受控引用、摘要和非敏感元数据；涉及个人信息、第三方秘密、凭据、法律特权或高敏材料的原件放在经授权的受控位置。
- 记录来源身份、来源创建时间、接收时间、摘要算法/范围、访问控制和保管链。
- AI整理摘要必须与原始陈述分离，并保留可回溯关系；AIAnalysis不得作为Owner批准证据。
- 截图、转述或复制文本不得自动证明发件人身份、权限或原始上下文完整。

## 5. 接收与核验状态

Received → IdentityUnverified / AuthorityUnverified → InTriage → AcceptedForReview / ClarificationRequested / RejectedAsOutOfScope / Superseded。该状态机不等于Decision Record状态。身份未核验时不得形成正式Owner立场；无决定权的专业输入可保留，但不能批准字段。

## 6. 当前状态

本模板已锚定V2.26基线。Stage39尚未收到真实反馈；没有创建Feedback Record实例，没有导入原始材料，也没有新增批准。