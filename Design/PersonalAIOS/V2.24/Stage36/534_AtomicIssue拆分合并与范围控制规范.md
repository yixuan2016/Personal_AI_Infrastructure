# 534｜Atomic Issue拆分、合并与范围控制规范

**状态：** Atomic Issue Governance Candidate

## 1. 设计目标

一个反馈可能同时触及字段语义、模块权威、Policy、契约和测试。若将其写成一个“大问题”，容易出现某个Owner批准了自己无权决定的内容，或一项局部批准被误读为整包批准。因此必须把反馈拆分为可独立决定、可独立追踪和可独立关闭的原子议题。

## 2. 拆分规则

1. 按不同决定权威拆分：M08实例责任、M06语义、M02物理保管、M18 Policy和Personal Owner个人授权不得混为一项。
2. 按不同变更对象拆分：字段、关系、状态机、Command、Query、Event、Policy和模块边界分别标识。
3. 按不同处理动作拆分：读取、存储、提取、索引、外发、保留、撤销和删除应分别审查。
4. 按不同基线范围拆分：不同Profile版本、Schema版本或历史决议不得混用。
5. 保留父子关系：同一反馈可生成多个Atomic Issue，并通过parent_feedback_ref保持来源关联。

## 3. 不应拆得过细的情形

如果多个字段共同表达一个不可分割的语义约束，且由同一权威决定、同一批准范围覆盖，可以形成一个Atomic Issue，但必须列出完整字段清单和明确边界。不得为了减少记录数量而合并不同Owner的决定权。

## 4. Issue Record字段

| 字段 | 说明 |
|---|---|
| issue_id | 全局唯一议题ID |
| parent_feedback_id | 原始反馈ID |
| issue_class | Factual/Semantic/Authority/Policy/Risk/Contract/Personal Sovereignty |
| decision_authority | 主决定权威 |
| co_reviewers | 必须会审角色 |
| baseline_ref | 精确父基线 |
| scope_refs | Field/Relation/Contract/Policy/Test引用 |
| problem_statement | 可验证的问题定义 |
| evidence_refs | 原始证据与专业意见 |
| options | 候选方案及代价 |
| status | Pending/InTriage/InReview/Blocked/Proposed/Approved/Rejected/Deferred |
| decision_ref | 正式Decision Record引用 |
| supersedes_ref | 被替代议题 |

## 5. 拆分示例

“Locator不稳定，建议换成新的来源ID并允许改写Snapshot”至少拆为：D-01身份命名空间；D-02 Locator历史与失效；D-03 Snapshot不可变与Correction。三个议题可能由不同权威决定，不得用一份笼统批准覆盖。

“删除时同时删除备份、索引和Evidence”至少拆为：M02物理删除；M07派生Projection传播；M18 Retention/Legal Hold；M06 Evidence语义保留边界。删除协调可以统一编排，但不能统一决定所有权威内容。

## 6. 关闭规则

Atomic Issue只有在决定权威、范围、证据、决议和后续影响全部记录后才可关闭。被拆分的父反馈只有在所有子议题均已解决或明确延期/拒绝时，才能标记为Dispositioned。任何一个子议题Blocked，父反馈必须显示未完全关闭。

## 7. 当前状态

本文件提供拆分规范，不生成实际Issue ID，不虚构反馈内容。