# 536｜Decision Record字段Schema与批准有效性规则

**状态：** Decision Record Schema Candidate

## 1. 目的

为D-01至D-07建立统一、可审计的决议记录结构，确保每项决议都能回答：谁在什么权限下，对哪个版本、哪些对象和字段，基于什么证据，作出了什么结论，并留下哪些条件、异议和后续影响。

## 2. Decision Record最小字段

| 字段 | 必填 | 说明 |
|---|---|---|
| decision_id | 是 | 全局唯一决策编号 |
| issue_id | 是 | 对应Atomic Issue |
| parent_feedback_id | 是 | 原始反馈来源 |
| baseline_ref | 是 | 精确基线、Commit和版本 |
| scope_refs | 是 | Field/Relation/Contract/Policy范围 |
| decision_question | 是 | 单一、可回答的问题 |
| decision_authority | 是 | 正式决定角色 |
| authority_evidence_ref | 是 | 授权范围证据 |
| participants | 是 | 参会、会审及专业审查角色 |
| options_considered | 是 | 选项、优劣和反方意见 |
| selected_disposition | 是 | Approved/Rejected/Deferred/Blocked等 |
| rationale | 是 | 决定依据 |
| evidence_refs | 是 | 原始事实、专业意见和批准证据 |
| conditions | 否 | 附条件批准要求 |
| risk_acceptance_ref | 否 | 经授权的风险接受 |
| dissent_refs | 否 | 保留的异议 |
| effective_scope | 是 | 生效范围、时间和限制 |
| impact_refs | 是 | Profile、契约、消费者和测试 |
| approval_evidence_ref | 条件必填 | 正式批准材料 |
| independent_review_ref | 是 | 独立证据复核 |
| supersedes_ref | 否 | 被替代的旧决议 |

## 3. 批准有效性

正式OwnerApproved必须同时满足：身份已核验、角色授权覆盖本议题、基线与范围明确、决议措辞明确、批准人确认、原始证据完整、条件与异议已记录、独立复核完成。缺少任一项，不得标记为正式批准。

## 4. 状态模型

Draft、Submitted、InReview、ClarificationRequired、Proposed、ApprovedWithConditions、OwnerApproved、Rejected、Deferred、Blocked、Superseded。不得从Draft直接跳到OwnerApproved；不得将ApprovedWithConditions当作无条件批准。

## 5. 与其他治理对象的区别

Decision Record记录某个Owner对精确问题的决定；ACR记录架构变更审查；OD记录顶层架构决策；Profile Delta记录字段或契约的前后差异；Test Record记录实际验证结果。它们相互引用，但不能互相替代。

## 6. AI辅助边界

AI可以帮助整理问题、比较选项、检查缺项和生成草稿；不得代替Owner签署、生成批准证据、推断沉默为同意、自动修改Decision Status或把建议方案升级为生效基线。

## 7. 当前状态

本文件仅定义Schema和批准门槛，尚无Stage36正式Decision Record。