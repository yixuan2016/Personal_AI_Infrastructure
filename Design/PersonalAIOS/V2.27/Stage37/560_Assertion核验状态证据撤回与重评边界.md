# 560｜Assertion核验状态、Evidence撤回与重评边界

**状态：** Assertion Verification Governance Candidate

## 1. 核心区分

- Evidence：可定位的材料引用及其来源、版本和完整性信息；
- Assertion：主体提出的事实主张；
- Verification：对Assertion在特定范围、时间和证据集合下进行的核验活动；
- Confidence：在明确方法和范围下形成的评估，不等同于事实真值；
- Source Trust：对来源身份、权限和可靠性的评价。

上述概念不能由一个Evidence integrity_state或单一置信度字段替代。

## 2. 核验责任

M06定义Assertion与Evidence关系、核验语义和状态规则；M08维护Evidence实例及引用；M17维护Receipt原件和Connector来源事实；目标对象Owner确认目标内容的业务权威；适用的专业领域Owner对其专业范围内的结论负责。Evidence创建者不得自动成为Assertion最终核验者。

## 3. 核验状态候选

Proposed、Supported、Contested、Verified、Rejected、Withdrawn、Stale、ReverificationRequired。它们是状态语义候选，不是现有Assertion Profile的批准枚举。每次核验必须记录核验主体、时间、方法、证据集合、适用范围、反证和有效期/复核触发器。

## 4. Evidence撤回与下游影响

Evidence撤回可能源于来源授权撤销、目标版本错误、内容被证明伪造、定位失效、个人撤回或Retention要求。撤回理由必须记录，且要区分“内容不再可访问”“来源不再授权”“证据被反证”和“证据对象被删除”。

若某Evidence被撤回，所有依赖该Evidence的Assertion、Knowledge摘要、决策依据和长期记忆必须进入影响评估；不能自动全部判假，也不能继续显示为无条件Verified。应根据剩余证据决定维持、降级、重新核验或撤回。

## 5. 历史与纠错

历史核验记录不得原位覆盖。新的核验结果应追加并指向被复核的旧结果；当前状态可更新，但历史决议和当时证据集合必须保留可审计引用。撤回不会抹去曾经作出该主张或核验的历史事实。

## 6. 当前状态

本文件仅定义核验与撤回边界，不对任何个人Assertion作事实判断，也不创建或批准新的Assertion状态枚举。