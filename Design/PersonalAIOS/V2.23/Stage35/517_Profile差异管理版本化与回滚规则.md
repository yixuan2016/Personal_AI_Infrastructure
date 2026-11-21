# 517｜Profile差异管理、版本化与回滚规则

**状态：** Profile Delta Governance Candidate

## 1. 目标

确保每次Owner反馈导致的Profile变化都能精确表达“改了什么、为什么改、谁批准、影响谁、何时生效”，同时保留V2.22原始定义和被否决方案。

## 2. 差异分类

| Delta Type | 定义 | 示例 |
|---|---|---|
| Editorial | 只改善表达，不改变语义 | 定义文字更清楚 |
| Semantic | 改变字段/关系的业务含义 | Source Authority语义重定 |
| Structural | 改变类型、基数、父子关系或字段形态 | 单值改为多值 |
| Governance | 改变Owner、权限、Policy或分类 | 写入权威变更 |
| Lifecycle | 改变状态或迁移守卫 | 增加撤销路径 |
| Contract | 改变API/Command/Query/Event | 新增必填载荷 |
| Compatibility | 影响旧消费者/旧事件 | Schema升级 |
| Deletion/Retention | 改变保留、撤销、删除或备份传播 | 派生闭包扩大 |

## 3. 版本规则

- V2.22是本阶段父基线，不覆盖、不改写。
- V2.23-Draft只收录有明确来源和审议状态的候选差异。
- 未获批准的变化标记`Proposed`，不能当作新基线生效定义。
- 每项变化保存`old_definition_ref`、`new_definition_ref`、`decision_id`、`approval_evidence_ref`、`supersedes_ref`。
- 语义变更不得复用旧字段ID表达完全不同的含义；是否新增Field ID需由M06决定并检查OT准入。
- 旧字段弃用必须定义读取兼容、写入停止、迁移窗口和删除批准。

## 4. Diff Record字段

`profile_delta_id`、`baseline_from`、`baseline_to`、`object_type_id`、`field_id`、`delta_type`、`before_text`、`after_text`、`reason`、`feedback_refs`、`decision_id`、`owner`、`approval_evidence_ref`、`consumer_impact_ref`、`test_refs`、`status`、`supersedes_ref`。

## 5. 回滚规则

回滚不是覆盖历史版本，而是发布新的受控修订，将字段/契约恢复到经批准的语义。对已产生Event、外部副作用或数据变更的情况，必须考虑补偿、对账和审计，不能仅将Profile文件回退。

## 6. 差异准入

- Editorial可在确认不改变语义后作为文档修订；
- Semantic/Structural/Governance/Lifecycle必须有Owner决议；
- Contract/Compatibility必须有消费者影响分析；
- Deletion/Retention/Provider变更必须有M02/M18/M15及专业审查；
- ACR/OD相关变化必须完成对应决策；
- 无批准证据的变化只进入候选区，不覆盖正式定义。

## 7. 当前状态

尚无真实反馈触发的Profile差异；六个Profile仍保持V2.22候选定义。V2.23只建立差异管理框架，不宣称已完成字段修订。