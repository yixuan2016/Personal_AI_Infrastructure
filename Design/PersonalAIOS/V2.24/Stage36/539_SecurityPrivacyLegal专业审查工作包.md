# 539｜Security/Privacy/Legal专业审查工作包

**状态：** Independent Review Package Candidate；No Professional Opinion Imported

## 1. 目的

D-01至D-07涉及来源身份、定位符、个人数据、处理依据、物理存储、完整性和删除，部分风险不能由普通业务Owner单独判断。专业审查应独立出具意见，明确依据、范围、条件和未决问题。

## 2. 专业审查触发矩阵

| 专业领域 | 重点议题 | 必须提供的材料 |
|---|---|---|
| Security | Locator凭据、Handle访问、加密、密钥、备份、摘要完整性 | 威胁模型、权限边界、密钥管理、审计与恢复证据 |
| Privacy | Data Subject、Purpose、Consent、最小化、撤回和派生传播 | 数据流、目的清单、授权范围、Retention和删除闭包 |
| Legal | 第三方Rights、许可条款、处理依据、跨境/Provider条款、Legal Hold | 原始条款、适用地区、处理活动和法律问题清单 |

## 3. 审查范围

- D-01/D-02：身份映射、来源权限、Locator是否含个人信息或访问秘密；
- D-03：Snapshot不可变与更正权、保留期限、证据保全和删除冲突；
- D-04：Rights、Purpose、Consent、Processing Basis及外发限制；
- D-05：物理存储位置、访问能力、加密和多副本风险；
- D-06：完整性证据的准确表述，防止将Digest误作真实性证明；
- D-07：备份、密钥销毁、Legal Hold、不可恢复删除和回执充分性。

## 4. 专业意见格式

每份意见至少包含Reviewer身份与专业角色、适用范围、资料版本、事实假设、审查依据、风险等级、发现、必要控制、不可接受条件、建议行动、复审触发器和意见有效期。若资料不足，必须明确写出“无法判断”及所需补充材料。

## 5. 权威边界

Security/Privacy/Legal意见不能替代M08实例权威、M06语义批准、M02物理保管决定、M18 Policy Authority决定或Personal Owner个人授权。反过来，Owner批准也不能豁免必须进行的专业审查。

## 6. 高风险处理

涉及未授权外发、密钥暴露、不可逆删除、第三方数据权利不明或Consent撤回未传播时，应暂停相关处理动作并Fail Closed。风险接受必须由有权角色作出，不能由文档作者或AI代签。

## 7. 当前状态

Stage36未取得新的专业审查意见。所有专业审查状态继续Pending。