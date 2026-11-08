# 513｜S1六对象跨Owner高风险决策地图

**状态：** Cross-owner Decision Map Candidate

## 1. 目的

将六个对象中的高风险议题与决定权威、会审角色和下游影响绑定，避免反馈进入后只由最先接收的模块处理。地图中的Owner均为候选角色，须以实际授权确认。

## 2. 决策地图

| 决策ID | 问题 | 主决定权威候选 | 必须会审 | 关联字段/对象 | 默认阻断条件 |
|---|---|---|---|---|---|
| D-01 | Source外部身份与本地ID组合 | M06/M08 | Source Authority | SRC-001/003/004 | 身份命名空间不明 |
| D-02 | Locator多值、历史与失效 | M08/M06 | M18、Security | SRC-005、SNP-008 | 凭据/隐私风险不明 |
| D-03 | Snapshot不可变与Correction | M08/M06 | M02、M18 | SNP-001—022 | 可原位覆盖历史 |
| D-04 | Rights/Purpose/Consent分离 | M18 | M06、Privacy/Legal | SRC-008、SNP-013—016 | 当前处理依据未知 |
| D-05 | RawAsset物理Handle | M02 | M08、Security | RAW-004 | 无有效Opaque Handle |
| D-06 | Digest与Integrity语义 | M06/M02 | M08、Security | RAW-008—011、EVD-007/008 | 范围/算法/目标不明 |
| D-07 | Custody/Encryption/Backup | M02 | M18、Security | RAW-012/013/020 | 物理责任不明 |
| D-08 | KnowledgeAsset版本与删除闭包 | M08/M06 | M07、M18 | KAS-006/007/016 | 派生物清单不完整 |
| D-09 | ExtractionRun Provider/Region | M15/M18 | M08、Security/Privacy/Legal | EXT-006—013 | 实际处理地/条款未知 |
| D-10 | ExtractionRun UnknownOutcome/Retry | M08/M15 | M06 | EXT-016/019—022 | 外部副作用未对账 |
| D-11 | ChunkSet发布与Projection权限 | M08/M07/M18 | M06 | CHK-005—017/022 | 集合不完整或权限降级 |
| D-12 | Evidence Target与Assertion核验 | M06/M08 | M17/目标Owner | EVD-003—011/020 | 目标/版本或权威不明 |

## 3. 审议顺序

优先解决D-01至D-07的身份、来源、权利和物理保管问题，再处理D-08至D-11的派生链，最后处理D-12 Evidence语义交接。此顺序是依赖建议，不表示下游议题在上游批准后自动批准。

## 4. 共同门禁

所有决策必须有明确问题、候选方案、事实证据、反方风险、权威Owner、条件/例外、影响范围、测试追踪和批准证据。涉及个人主权或已批准OD时，须按相应决策流程单独处理。

## 5. 当前状态

12项高风险决策均为审议议题，不是已经作出的决策。实际Owner代表、反馈和批准证据待接收。