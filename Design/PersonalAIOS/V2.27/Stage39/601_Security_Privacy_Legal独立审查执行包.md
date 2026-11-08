# 601｜Security/Privacy/Legal独立审查执行包

**状态：** Independent Professional Review Package Candidate；No Professional Opinion Imported

## 1. 审查原则

专业审查与Owner决策是两条并行且不可互相替代的责任链。Security/Privacy/Legal可以提出风险、控制要求、限制条件或“无法判断”；不能替M06批准语义、替M08批准实例写入、替M02签发物理删除、替M18作Policy决定，也不能替Personal Owner作个人主权决定。

## 2. 触发矩阵

| 专业领域 | 必须审查的议题 | 需要的材料 | 不可替代的Owner |
|---|---|---|---|
| Security | Locator凭据、Opaque Handle、权限绕过、加密密钥、备份、Digest、Provider网络边界、日志、沙箱、缓存 | 威胁模型、权限矩阵、密钥/备份/恢复说明、审计事件、负向案例 | M02/M15/M07及字段Owner |
| Privacy | Data Subject、Purpose、Consent、最小化、敏感分类、撤回、派生数据传播、Provider外发 | 数据流、目的清单、处理依据、数据类别、撤回/删除闭包、访问主体 | M18与适用Personal Owner |
| Legal | 第三方Rights、许可、合同/DPA、处理依据、跨境、Provider子处理商、Legal Hold、Retention例外 | 原始条款、适用地区、处理活动、合同版本、法律问题清单 | M18/M15/M02及适用业务Owner |

## 3. 与D-01至D-12的审查触发

- D-01/D-02：来源身份映射、Locator是否包含个人信息或访问秘密、第三方来源权限。
- D-03：不可变Snapshot与更正权、证据保全、Retention和删除冲突。
- D-04：Rights、Purpose、Consent、Processing Basis、数据主体与处理目的限制。
- D-05/D-07：物理存储位置、访问权限、密钥、备份、不可恢复删除和回执充分性。
- D-06：Digest完整性证明的边界，避免把摘要匹配误作来源真实性。
- D-08：派生闭包、Retention、Legal Hold、本人删除请求与历史引用。
- D-09：Provider合同、子处理商、实际Region、日志、训练再利用、人工访问和删除。
- D-10：外部副作用、重复处理、重试、对账与审计。
- D-11：Embedding/Index/Context权限继承、撤回和残留风险。
- D-12：Evidence定位、摘录最小必要、来源权威、个人信息和核验边界。

## 4. 专业意见记录Schema

每份专业意见至少记录：Review ID、Reviewer身份/专业角色、组织授权或专业资格依据、审查范围、基线Commit、材料版本、事实假设、适用标准/依据、风险等级、发现、必要控制、不可接受条件、无法判断事项、建议行动、有效期、复审触发器和原始意见引用。

## 5. 意见状态

NotRequested、Requested、InProgress、OpinionIssued、ClarificationRequired、UnableToConclude、ObjectionRaised、Superseded。专业意见不得映射为OwnerApproved。若专业审查提出未关闭的S0/S1风险，相关议题必须Blocked或限定范围，直到有权角色作出可审计处置。

## 6. 当前状态

当前没有新增Security/Privacy/Legal专业意见。所有专业审查均Pending；本包不构成法律意见、合规结论或风险接受。