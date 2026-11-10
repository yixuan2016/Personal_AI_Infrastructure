# 512｜跨Owner联合审议会议规程与议程

**状态：** Joint Review Protocol Candidate；No Meeting Decision Recorded

## 1. 会议目标

跨Owner会议用于解决一个议题涉及多个权威角色时的边界和依赖，不以会议人数或多数表决替代权威分工。会议必须提前明确决策问题、决定Owner、会审方和需要提供的证据。

## 2. 会议前准备

至少提前一个工作周期提供：
- 议题ID、对象/字段/关系ID和V2.22 Profile版本；
- 原始反馈和独立整理摘要；
- 事实证据、反方意见和待确认假设；
- 决策权威及会审角色；
- 当前定义、拟议选项和影响分析；
- 关联契约、消费者、Policy、测试和删除闭包；
- 需要的Security/Privacy/Legal意见。

材料未齐时标记`PreReadIncomplete`，不得把会议安排当作审议完成。

## 3. 建议议程（120分钟）

| 时间 | 环节 | 输出 |
|---|---|---|
| 0—10分钟 | 确认基线、范围和决策权限 | 会议范围确认 |
| 10—25分钟 | 陈述原始反馈与事实 | 事实/观点分离 |
| 25—45分钟 | 逐项解释当前设计和依赖 | 语义澄清 |
| 45—70分钟 | 权威Owner分别陈述 | 各自权限范围内意见 |
| 70—90分钟 | 比较方案、反方风险和控制 | 选项及风险矩阵 |
| 90—105分钟 | 形成原子处置或明确未决 | Decision/Issue状态 |
| 105—115分钟 | 指定证据、行动Owner和期限 | Action Register |
| 115—120分钟 | 逐字确认决议文本 | 会议决议草案 |

## 4. 会议角色

- Decision Owner：对该原子问题有决定权的角色；
- Co-review Owner：对依赖/接口有权威的模块Owner；
- Professional Reviewer：Security/Privacy/Legal等独立审查；
- Facilitator：控制范围和时间，不替代决策；
- Recorder：记录原始意见、异议和决议；
- Evidence Reviewer：会后复核批准证据与影响传播。

## 5. 会议结论类别

`DecisionMade`、`ConditionalDecision`、`ClarificationRequired`、`NoConsensus`、`AuthorityConflict`、`Deferred`、`Blocked`。只有有权Owner确认的明确决议才可创建OwnerApproved Decision Record；会后草稿必须由决策Owner确认。

## 6. 异议处理

异议必须记录原始观点、提出者角色、证据、风险和建议。不得为了会议纪要简洁而删除少数意见。若不同权威Owner的意见无法协调，按494号升级，不得通过多数票覆盖。

## 7. 会后关闭

Recorder形成决议草稿；Decision Owner确认；Evidence Reviewer核对身份/范围/版本；影响分析Owner更新Profile差异、契约、测试和台账。没有上述证据时会议状态只能是`NotesCaptured`或`PendingConfirmation`。

## 8. 当前状态

本规程为会议方法候选，不表示已召开会议或形成任何新Owner决议。