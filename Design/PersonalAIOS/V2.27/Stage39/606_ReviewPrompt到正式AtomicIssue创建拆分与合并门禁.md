# 606｜Review Prompt到正式Atomic Issue的创建、拆分与合并门禁

**状态：** Atomic Issue Intake Gate Candidate；0 Formal Issue Created in Stage39

## 1. 核心区分

Review Prompt是设计者依据Profile和风险分析提出的问题，例如569号矩阵中的142条问题。它不来自Owner，不表示存在争议，也不自动获得Issue ID。

正式Atomic Issue必须来源于一份真实Feedback Record，且原始材料、提交者身份、权限范围和基线版本已完成必要核验。不能把142条Review Prompt批量转换为142条Issue。

## 2. 创建条件

同时满足以下条件才可创建正式Issue：
1. 有真实Feedback Record和可回溯原始材料；
2. 反馈来源和提交者身份已核验，或明确记录其未核验且只作为非决定性输入；
3. 明确反馈针对的基线Commit和对象范围；
4. 将事实、观点、建议、异议、条件和批准声明分开；
5. 单一问题可用一个明确问题句表达；
6. 决定权威和必须会审角色可以识别；否则先创建Authority Clarification；
7. Issue不把提交者建议预设为正确结论。

## 3. 拆分规则

- 不同决定权威必须拆分：M06语义、M08实例、M02物理、M18 Policy、M15 Provider事实、M07 Projection、M17 Receipt和Personal Owner个人主权不得合并为一项批准。
- 不同变更对象应分别标记：Field、Relation、State Transition、Command、Query、Event、Policy、Module Boundary。
- 不同动作分别处理：Read、Write、Capture、Extract、Index、External Egress、Retain、Revoke、Delete。
- 不同基线、Profile或Contract版本不得混用。
- 一个不可分割的语义约束可以覆盖多个字段，但必须由同一权威决定并列出精确字段清单。

## 4. 合并规则

只有同一来源/同一事实链、同一决定权威、同一基线、同一变更对象且共享同一批准范围时，才可考虑合并。不同Owner意见、不同处理动作、不同风险级别或不同条件不得为了减少Issue数量而合并。

## 5. Issue Record最小字段

issue_id、parent_feedback_id、baseline_ref、issue_class、decision_authority、co_reviewers、scope_refs、problem_statement、current_definition_ref、requested_change、submitter_rationale、evidence_refs、options、risk_level、dependencies、test_refs、status、decision_ref、supersedes_ref。

Issue ID由正式Issue Registry分配；本文件不预设或占用编号。

## 6. 关闭规则

Issue关闭需要Decision Record或明确的Rejected/Deferred/Blocked处置证据。父Feedback只有在所有子Issue均有处置时才能标记Dispositioned；若存在未决子Issue，必须显示PartialDisposition或Open。

## 7. 当前状态

Stage39没有真实反馈输入，因此正式Atomic Issue数量为0。142条Review Prompt仅供审议，不得在台账中伪装为正式Issue。