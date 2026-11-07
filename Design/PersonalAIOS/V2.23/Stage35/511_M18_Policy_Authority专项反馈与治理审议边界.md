# 511｜M18 Policy Authority专项反馈与治理审议边界

**状态：** Policy Review Workstream Candidate；M18 Owner Feedback Pending

## 1. 审议目标

核验M18对Purpose、Policy、Consent、Processing Basis、Approval、Classification、Retention和PEP裁决规则的权威，确保来源Rights、历史Purpose、当前Consent和一次PolicyDecision不被混为永久许可。

## 2. 核心概念必须分离

| 概念 | 表达什么 | 不能推导什么 |
|---|---|---|
| Source Rights | 来源/Provider许可或合同权利 | 不自动授权任意个人处理目的 |
| Purpose | 某次处理希望达到的目的 | 不自动构成合法处理依据 |
| Consent | 适用场景下的同意记录 | 不替代其他处理依据或策略约束 |
| Processing Basis | 某次处理适用的依据记录 | 不等于Provider允许所有处理 |
| PolicyDecision | 在特定时间、Actor、资源、Purpose和Policy版本下的裁决 | 不永久授权未来请求 |
| Approval | 对特定高风险动作的明确批准 | 不扩大到未列明范围 |
| Classification | 数据敏感级别与访问约束 | 不因派生为摘要/Embedding而自动降低 |
| Retention | 保留规则和例外 | 不等于物理删除已经完成 |

## 3. 重点字段与链路

SRC-008/009/010；SNP-013—019；RAW-014/015；KAS-009/010/015/016；EXT-009/011/012/013/024；CHK-015/016/020/022；EVD-016/017/018/021均应核对当前Policy与历史Lineage的分离。

## 4. 必须回答的问题

1. Purpose目录由谁维护，如何版本化和废止？
2. Source Rights如何引用原始条款和适用版本？
3. Consent、Processing Basis和PolicyDecision如何保持独立？
4. PolicyDecision如何绑定Actor、Resource、Action、Purpose、Policy Version和时间？
5. Policy Unknown、Rights Unknown、Consent Withdrawn时如何Fail Closed？
6. 分类如何从源资产传播到Chunk、Embedding、摘要、Context、缓存和Provider？
7. Retention例外、Legal Hold和删除请求冲突时如何升级？
8. Provider Region、训练再利用、人工访问和日志使用如何进入审查？
9. 对历史数据重新处理时，是否必须重新做当前Policy评估？
10. 如何证明撤销已传播到派生物而非只更新源对象？

## 5. M18不可越权清单

M18不代替M02执行物理删除，不维护M08对象实例，不替M06定义Evidence语义，不代替Personal Owner确认个人目标/价值，不把专业审查意见伪装成法律结论。

## 6. 所需证据

Purpose/Policy/Consent/Retention目录、PEP输入输出契约、Policy版本、审查记录、撤销传播图、Provider条款映射和合成拒绝案例。涉及法律解释的事项必须由适当专业人员确认适用范围。

## 7. 当前结论

M18专项意见待真实反馈；本文件不批准任何Purpose、Policy、Consent、Retention期限或Provider处理安排。