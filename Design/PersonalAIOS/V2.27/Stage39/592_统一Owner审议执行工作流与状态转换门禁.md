# 592｜统一Owner审议执行工作流与状态转换门禁

**状态：** Integrated Review Workflow Candidate；No Session Executed

## 1. 五类记录必须分离

| 记录类型 | 回答的问题 | 产生条件 |
|---|---|---|
| Feedback Record | 谁在何时通过什么来源表达了什么意见？ | 收到真实原始材料 |
| Review Prompt | 设计中有哪些问题需要Owner回答？ | 设计审查产生；不代表反馈 |
| Atomic Issue | 从真实反馈拆出的单一可裁决问题是什么？ | 反馈来源、身份、权限完成核验并进入分诊 |
| Decision Record | 有权Owner对精确问题作出了什么决定？ | 正式审议形成明确决定 |
| Profile/Contract Delta | 经批准的定义具体如何变化？ | 有效Decision Record批准变更后 |

## 2. 端到端流程

Baseline Confirmed → Feedback Received → Source Preserved → Identity Verified → Authority Scope Verified → Triage → Atomic Issue Created → Decision Owner/Co-reviewers Assigned → Pre-read Ready → Owner Review → Decision Text Confirmed → Evidence Audit → Impact Assessment → Delta Proposed → Owner Approval → Propagation → Independent Audit → Baseline Candidate Review。

该流程允许无决议结束：ClarificationRequired、Deferred、Blocked、Rejected或NoConsensus均是合法结果，不得为追求关闭率强行批准。

## 3. 状态机边界

### Feedback Record状态

Received、IdentityUnverified、AuthorityUnverified、InTriage、ClarificationRequested、AcceptedForReview、RejectedAsOutOfScope、Superseded。反馈状态不表示决策状态。

### Review Prompt状态

Open、PreparedForOwner、AnsweredWithEvidence、ClarificationNeeded、NotApplicableWithRationale、Superseded。Review Prompt可以由真实审议回答，但不能自行变成Owner反馈。

### Atomic Issue状态

DraftedFromVerifiedFeedback、InTriage、Assigned、PreReadReady、InReview、ClarificationRequired、ProposedDisposition、DecisionPending、Blocked、Deferred、Rejected、ResolvedWithEvidence。未有真实反馈时不创建正式Atomic Issue。

### Decision Record状态

Draft、Submitted、InReview、ClarificationRequired、Proposed、ApprovedWithConditions、OwnerApproved、Rejected、Deferred、Blocked、Superseded。OwnerApproved必须满足E3；条件未完成不得计入无条件冻结完成。

### Delta状态

Identified、Drafted、ImpactAssessed、AwaitingOwnerApproval、Approved、Propagated、Audited、Rejected、Deferred、Blocked。只有Approved之后才允许进入受控候选基线；只有Propagated且Audited后才可进入冻结评估。

## 4. 不允许的状态跳转

- 不允许Received直接跳到OwnerApproved；
- 不允许Review Prompt直接创建Decision Record并写成批准；
- 不允许未核验身份/权限的反馈创建Owner立场；
- 不允许ProposedDisposition覆盖Decision Status；
- 不允许ApprovedWithConditions被当作无条件Approved；
- 不允许Delta Drafted直接进入正式基线；
- 不允许AI摘要、会议安排或沉默触发状态升级。

## 5. 暂停与Fail Closed

若身份、权限、基线、来源、数据范围或专业意见缺失，相关议题停留在ClarificationRequired/Blocked。阻断范围应精确到字段、对象、动作、Provider、Region和数据范围，不无依据扩大，也不缩小到无法控制风险。

## 6. 关闭条件

一个Atomic Issue只有在决定权威、范围、证据、决议文本、条件/异议、消费者影响和独立复核齐备后才可关闭。父Feedback Record只有在所有子Issue均有明确处置后才可标记Dispositioned；存在未决子Issue时必须显示部分关闭而非完全关闭。

## 7. 当前状态

本流程是V2.27执行规程候选。Stage39没有真实Owner Session、Feedback Record、Atomic Issue或Decision Record实例。