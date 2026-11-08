# 577｜字段类型、基数、空值与Unknown语义统一规范

**状态：** Cross-Object Type Semantics Candidate；No Schema/Profile Change Approved

## 1. 目标

避免不同对象对同一概念使用不一致的类型和空值解释。142个字段逐项定稿前，必须先统一引用、集合、时间、状态、摘要、范围、分类和策略引用的表达规则。

## 2. 类型类别

| 类型类别 | 适用示例 | 统一要求 |
|---|---|---|
| Stable Identifier | *_id | 命名空间、唯一性、不可复用规则明确 |
| Typed Reference | *_ref | 目标类型、目标ID、版本要求和权限检查明确 |
| Reference Collection | *_refs | 基数、顺序、重复、空集合和部分有效语义明确 |
| Controlled Vocabulary | *_kind、*_state | Registry/Schema版本、未知值和废弃值策略明确 |
| Timestamp | *_at | 时区、精度、时钟来源、事件语义和可回填性明确 |
| Digest | *_digest | 算法、Scope、规范化和目标版本必须共同定义 |
| Opaque Handle | physical_handle_ref | 不泄露物理路径、凭据或绕过授权能力 |
| Structured Payload | locator_payload | Schema版本、校验规则、敏感字段和大小限制明确 |
| Version Reference | *_version_ref | 版本身份、不可变性、父版本和解析规则明确 |
| State Reference | *_state_ref | 状态域、状态机、迁移守卫和权威来源明确 |

## 3. 空值语义必须拆分

- **Absent / Not Provided：** 生产者未提供，不能推断为“不存在”。
- **Unknown：** 已知该事实需要，但目前无法确认；必须保留未知原因/证据缺口。
- **Not Applicable：** 经规则确认该字段对当前对象/场景不适用。
- **Empty Collection：** 已确认集合为空，不等于字段缺失。
- **Null：** 只有Schema明确允许时使用；必须定义与Absent/Unknown的差别。
- **Redacted / Withheld：** 因权限或隐私限制不向当前消费者披露，不代表底层值不存在。
- **Invalid：** 已提供但无法通过类型/约束校验，不能静默丢弃。

禁止用空字符串、零值、空数组或默认枚举值同时代表Unknown、Not Applicable和Empty。

## 4. 基数规则

单值引用必须说明是否允许空值及唯一性；多值引用必须说明是否有序、是否去重、是否允许跨对象类型、部分失败如何表达。多值不自动代表多权威；如多个来源冲突，必须保留冲突并交由权威规则解决。

## 5. 状态字段与状态引用

状态必须绑定明确的状态机和Owner；不能仅凭字段名推断迁移规则。运行状态、生命周期、权限状态、完整性状态、物理保管状态和删除状态必须分域表达。

## 6. 时间语义

所有时间字段必须说明事件时间、记录时间、采集时间、处理时间、完成时间或观察时间；统一使用带时区的时间表示，保留原始时区/来源信息。时钟不确定时应标注Unknown或精度边界，不得伪造精确顺序。

## 7. 摘要语义

Digest必须绑定算法、规范化规则、字节/逻辑内容Scope、目标版本和生成主体。Digest匹配仅能支持指定内容范围的完整性判断，不证明来源真实性、授权状态或Assertion成立。

## 8. 当前结论

本规范为142字段统一审查的类型语义候选，不修改任何已批准Schema或Profile。所有不满足项进入Schema Gap Register。