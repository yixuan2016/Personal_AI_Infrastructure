# 501｜S1 Owner审议关闭条件与批准证据质量审计

**状态：** Review Closure Gate Candidate

## 1. 关闭不是“会议结束”

议题关闭必须同时证明：决定权威正确、审议范围明确、决议文本可执行、证据真实可追溯、影响已传播、遗留条件有责任人和期限。没有这些要素时只能标记Pending/Deferred/Blocked。

## 2. 关闭检查矩阵

| 检查项 | 通过标准 | 失败处理 |
|---|---|---|
| Authority | 决策人对该字段/关系/策略具有明确权限 | 转交正确Owner |
| Scope | 决议列明Field ID/Relation/Contract ID和版本 | 拆分原子议题 |
| Evidence | 存在可核验签署/书面确认/正式决议 | 保持Pending |
| Rationale | 说明依据、风险、反方意见和选择理由 | 补充材料 |
| Conditions | 条件可测试、有责任人和期限 | ApprovedWithConditions但不计入冻结完成 |
| Exceptions | 例外有范围、到期和补偿控制 | 不接受无期限例外 |
| Impact | 下游对象、契约、Policy、测试和文档已更新 | 退回传播 |
| Compatibility | 旧版本读写、迁移和回滚影响已说明 | 进入ACR |
| Independent Review | 非提案人复核证据和传播 | 补做独立复核 |
| Auditability | 原始记录、版本和Supersedes链保留 | 不得关闭 |

## 3. 证据质量等级

- **E0 — Unsupported**：无来源或不可核验转述；
- **E1 — Context**：讨论记录、草稿、背景材料；
- **E2 — Owner Statement**：身份和权限可确认的Owner明确陈述，但范围或签署形式仍需核实；
- **E3 — Formal Approval Evidence**：签署或正式书面/会议决议，明确决策人、范围、版本、日期和条件；
- **E4 — Propagated & Audited**：E3基础上，影响传播、版本更新和独立审计完成。

只有达到E3的有效证据才能作为Owner批准依据；冻结切片应达到E4。专业审查意见应单独记录，不与Owner批准混为一谈。

## 4. 条件批准

ApprovedWithConditions必须写明条件ID、责任Owner、到期时间、验证方法、未满足时的回退/阻断动作。条件未满足前不得把该字段用于更高风险的生产场景，也不得将整个Profile计为已批准。

## 5. 关闭状态

`Closed-Approved`、`Closed-Rejected`、`Closed-Deferred`、`Open-Clarification`、`Blocked-Authority`、`Blocked-Evidence`。Closed-Deferred必须保留风险和复审触发器；Rejected不能从历史台账删除。

## 6. 本阶段审计结论

当前没有新增Owner批准证据可供E3/E4审计；因此本阶段仅定义关闭门槛，不关闭任何新议题，不更新任何OT为Approved。
