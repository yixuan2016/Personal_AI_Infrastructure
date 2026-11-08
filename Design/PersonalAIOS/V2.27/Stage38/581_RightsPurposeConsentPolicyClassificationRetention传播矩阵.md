# 581｜Rights、Purpose、Consent、Policy、Classification与Retention传播矩阵

**状态：** Governance Propagation Candidate；No Policy Approved

## 1. 六类治理语义必须分离

- Rights：来源/内容可被何种方式使用的权利和限制；
- Purpose：当前处理/访问动作的具体目的；
- Consent：主体表达的同意及其范围、有效期和撤回；
- Processing Basis：处理活动的适用依据，不等同于Consent；
- Policy Decision：针对Actor、Action、Resource、Purpose和Context的具体裁决；
- Classification：数据敏感级别和处理保护要求；
- Retention：数据/副本/记录应保留多久以及例外规则。

这些概念互相约束，但不能合并为一个authorized=true。

## 2. 传播矩阵

| 来源对象 | 派生对象 | 必须保留/重新评估的治理信息 |
|---|---|---|
| Source | SourceSnapshot | Rights Snapshot、Purpose、Basis、Policy、Data Subject、Classification |
| SourceSnapshot | RawAsset | 来源权利和分类血缘、保留依据、物理保管约束 |
| RawAsset | KnowledgeAsset | 分类不降级、Purpose来源、Retention约束和可用权利范围 |
| KnowledgeAsset | ExtractionRun | 本次Actor/Action/Purpose/Processor/Provider/Region Policy |
| ExtractionRun | Chunk | 处理目的血缘、分类、输入版本和处理结果约束 |
| Chunk | Embedding/Index/Context Projection | 当前读取Policy、源分类、Purpose、撤回和删除状态 |
| 任一目标 | Evidence/Excerpt | 目标分类、采集目的、访问授权、摘录保留与来源链 |
| Evidence | Assertion/Decision/Memory | 证据可用性、核验状态和下游用途重新评估 |

## 3. 运行时检查

创建派生数据时检查处理授权；读取派生数据时检查当前访问授权；跨用途复用时重新评估Purpose和Policy；分类升级时传播到所有派生副本；Consent撤回时按适用Basis和法律/Policy规则评估，而不是无条件删除或无条件继续处理。

## 4. 冲突处理

- 多个Rights来源冲突：保留全部来源，采用经授权的权威冲突流程。
- Consent存在但处理Basis不充分：不能自动放行。
- Policy允许但Retention到期：不能仅凭Policy Decision继续保留。
- Classification未知：不得默认最低敏感级别。
- Purpose缺失：不应默认“通用用途”。
- 历史Policy Decision：只能证明当时裁决，不能替代当前裁决。

## 5. 当前结论

本矩阵为D-04及D-08至D-12的治理传播候选，不批准任何处理目的、Provider或数据用途。