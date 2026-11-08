# 605｜Owner审议Session、会议纪要与决议确认模板

**状态：** Session Record Template Candidate；No Session Held

## 1. Session Record必填信息

| 字段 | 说明 |
|---|---|
| session_id | 实际安排并召开后分配；不得预造已召开记录 |
| baseline_id / baseline_commit | 审议所依据的精确基线 |
| session_date / timezone | 实际召开时间及时区 |
| agenda_refs | D-01至D-12、Atomic Issue及Review Prompt引用 |
| facilitator_ref / recorder_ref | 主持人和记录者 |
| independent_reviewer_ref | 独立证据复核者，不由原始整理者兼任 |
| participants | 参会者、组织角色、模块、授权范围和出席状态 |
| decision_owner_refs | 每项议题的实际决定权威 |
| co_reviewers / professional_reviewers | 会审和专业审查角色 |
| pre_read_status | Complete/Incomplete及缺项 |
| meeting_outcome | DecisionMade/ConditionalDecision/ClarificationRequired/NoConsensus/AuthorityConflict/Deferred/Blocked |

## 2. 会前准入

- 确认V2.26基线及Commit；如基线已变化，重新确认议题适用版本。
- 核验参会者身份、模块角色和授权范围；参会不等于有决定权。
- 每个议题有精确Field/Relation/Contract范围、当前定义、候选方案、反方风险和依赖。
- 原始反馈与整理摘要分离；证据缺口、专业审查缺口和消费者影响清单提前提供。
- 缺少决定权威或关键证据时，可以召开澄清会，但不得进入批准环节。

## 3. 会议纪要结构

### A. 事实陈述

记录原始事实、来源、证据、时间和适用版本；不在事实段落中混入建议结论。

### B. Owner立场

按每位有权Owner分别记录：明确立场原文、授权范围、选择、理由、条件、例外、保留意见和未决事项。不得将多人观点合并成“大家同意”。

### C. 专业审查意见

Security/Privacy/Legal意见单独记录，标明审查范围、依据、风险和无法判断事项；不得写成业务Owner批准。

### D. 决议文本

逐字记录拟议决定；必须列明Decision ID、Atomic Issue ID、Field/Relation/Contract范围、基线Commit、生效范围、条件、例外、复审触发器和拒绝的选项。

### E. 异议与行动项

保留少数意见、证据分歧、责任人、期限、依赖和关闭证据。

## 4. 决议确认流程

Recorder形成草稿 → Decision Owner核对决议措辞和精确范围 → 参与者核对各自意见是否被准确记录 → 独立Reviewer核验身份/授权/基线/证据 → 创建正式Decision Record → 更新反馈和影响追踪台账。

未取得Decision Owner明确确认时，会议结果只能是NotesCaptured或PendingConfirmation。

## 5. 录音与隐私

默认不要求录音。若确需录音/转录，必须事先确认参与者告知、授权、访问范围、保留期限和删除责任；会议材料不得包含不必要的个人或第三方敏感信息。

## 6. 当前状态

本模板仅供未来真实会议使用。Stage39没有召开Owner会议，不生成虚构参会者、纪要或决议。