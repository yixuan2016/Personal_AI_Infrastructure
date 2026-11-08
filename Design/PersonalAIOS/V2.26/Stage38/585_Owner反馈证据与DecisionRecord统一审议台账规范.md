# 585｜Owner反馈、证据与Decision Record统一审议台账规范

**状态：** Owner Review Intake Standard Candidate；No Actual Feedback Imported

## 1. 台账分层

必须分别维护四类记录：
1. Feedback Record：原始反馈事实、提交者、时间、原文和来源；
2. Atomic Issue：从反馈拆分出的单一可裁决问题；
3. Decision Record：有权Owner对明确问题作出的正式决定；
4. Evidence Record：支持反馈、事实判断、权限和批准有效性的来源证据。

一条反馈可拆为多个Atomic Issue；一个Atomic Issue可有多方反馈；一个Decision Record可覆盖多个字段，但必须明确字段范围及各字段处置。

## 2. 反馈准入

FeedbackReceived不等于InReview。必须核验提交者身份、组织角色、授权范围、所针对的基线Commit、反馈原文完整性和附件来源。未经核验的反馈保留原始记录，不能更新为OwnerApproved。

## 3. 证据等级候选

- E0：无可核验证据或仅口头转述；
- E1：提交者说明/截图/会议记录，尚未独立核验；
- E2：可追溯的一手文档、配置或系统记录；
- E3：有权Owner签署的明确决定及其授权证据；
- E4：决定、授权、基线、范围和生效条件均可独立复核的完整批准包。

证据等级是审议材料分级，不替代各专业领域的法律或安全判断。

## 4. Decision Record必填项

Decision ID、Atomic Issue ID、基线版本/Commit、Field ID/Relation/Contract、问题陈述、事实证据、候选方案、选择及理由、Owner身份/授权、必须会审意见、条件/例外、异议、消费者影响、Policy/Retention/Deletion影响、测试要求、生效范围、批准时间、复审触发器和Evidence Ref。

## 5. 142字段台账更新规则

- 保留514号原始台账为历史初始化基线，不直接覆盖历史；
- 新增更新版台账时保留原始Feedback Status、Proposed Disposition和Decision Status三个独立维度；
- 只有E3/E4且权限核验通过的批准，才允许将字段状态更新为OwnerApproved；
- 条件批准必须明确条件和到期/复审时间；
- 反对意见和少数意见必须保留，不以汇总结论覆盖；
- 每次变更都绑定前后版本和审计来源。

## 6. 当前事实

Stage35原始台账仍为142/142 Pending；截至本阶段没有新增真实Owner反馈、E3/E4批准证据或正式Decision Record。Stage38建立的是审议规则，不是伪造台账状态。