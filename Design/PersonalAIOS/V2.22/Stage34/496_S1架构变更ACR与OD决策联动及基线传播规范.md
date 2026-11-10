# 496｜S1架构变更ACR与OD决策联动及基线传播规范

**状态：** Change Control Candidate；No New ACR Approved

## 1. 目的

Owner审议可能只澄清字段，也可能改变既有类型、模块权责、对象粒度或个人主权边界。必须区分普通澄清、Profile修订、架构变更和OD级决策，避免把高影响变化藏在字段表更新中。

## 2. 变更分类与路由

| 变更类型 | 示例 | 路由 | 最低证据 |
|---|---|---|---|
| Clarification | 补充不改变语义的定义/示例 | Owner审议台账 | 澄清依据与版本差异 |
| Field Refinement | 调整字段缺失、校验、可变性 | 字段Owner + TDA/SA | 字段影响分析和测试映射 |
| Contract Change | Command/Query/Event载荷或错误变化 | 契约Owner + 消费者 | 消费者清单、兼容策略 |
| Object Boundary Change | OT/子记录/Projection边界变化 | M06 + M08 + OD治理 | 类型粒度分析 |
| Authority Change | IA/TDA/SA/Custodian/Policy Authority变化 | 相关模块Owner + Personal Owner | 权威RACI、历史影响 |
| Module Boundary Change | M01—M18职责调整或新增模块 | OD决策流程 | 顶层架构比较与反方审查 |
| Personal Sovereignty Change | 本人确认、授权、目标或边界变化 | Personal Owner | 明确本人决策证据 |

## 3. OD状态保护

| 决策 | 当前已知状态 | 本阶段规则 |
|---|---|---|
| OD-01 | Approved A | 不因S1字段审议改写M01—M18稳定ID |
| OD-02 | Approved A | 196仍为全局对象权威注册表唯一入口；逐类型批准仍需证据 |
| OD-03 | Pending | 不推定批准；涉及个人意图权威的议题必须保留Pending |
| OD-04 | Approved B | 保留M01—M18顶层责任单元和既有模块准入边界 |

## 4. ACR最低内容

`acr_id`、提出原因、当前基线、目标基线、变更分类、原始证据、问题定义、选项、推荐方案、反方审查、影响闭包、风险分级、兼容迁移、回滚、Owner列表、Security/Privacy/Legal意见、批准证据和生效条件。

## 5. 影响传播闭包

任何获批变更必须检查并更新：Object Type Registry、Type Profile、Field Profile、关系矩阵、状态机、Command/Query/Event、Policy/PEP、数据血缘、Projection、删除闭包、测试、文档索引、决策台账和版本Manifest。只改一张字段表而不更新消费者与测试，视为变更传播不完整。

## 6. 版本和历史

变更以新版本追加，旧版本保留；明确`supersedes_ref`和生效范围。语义变化不能复用旧字段名表达新含义。迁移前必须定义旧读者、旧写者、双读/双写窗口、数据映射、验证、回滚和旧字段弃用条件。

## 7. 冻结规则

涉及已批准OD的变化未完成相应Owner决策前，相关Profile和契约保持Blocked/Proposed。任何ACR批准都不自动等于工程授权；任何字段批准也不自动意味着S1 Freeze Ready。
