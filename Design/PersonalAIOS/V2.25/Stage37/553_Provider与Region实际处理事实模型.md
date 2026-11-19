# 553｜Provider与Region实际处理事实模型

**状态：** Provider Execution Fact Model Candidate

## 1. 设计目标

D-09的核心不是增加一个Provider名称字段，而是建立“声明能力—请求配置—策略授权—实际执行—执行后证据”的闭环。Provider Profile描述服务能力与条款，ExtractionRun记录一次运行事实，两者不能互相替代。

## 2. Region至少区分五种语义

- Requested Region：请求或配置中指定的地区；
- Compute Region：实际执行计算的地区；
- Data-at-Rest Region：输入、输出或缓存持久化地区；
- Log/Telemetry Region：服务日志、遥测和诊断数据所在地区；
- Support/Access Region：人工支持或运维访问可能发生的地区。

单一provider_region_ref如果无法表达这些差异，应明确其定义并通过引用扩展或ACR处理，不得把一个地区名称解释为所有处理位置的证明。

## 3. Provider/Processor身份层次

Provider是外部服务主体；Processor是具体处理能力或处理器；Processor Version是具体模型/服务版本；Provider Profile是某个时点的合同、能力、区域、数据使用和安全声明集合；Provider Operation是一次调用的外部操作事实。字段引用必须明确指向哪一层。

## 4. 事实来源与证明强度

配置文件、SDK参数和请求路由只能证明预期配置；服务端回执、区域路由证明、Provider审计报告或合同约束可用于支持实际执行事实。若实际区域不可观测，必须记录Unknown，不得从配置推断Compute Region。

## 5. Policy绑定

EXT-011 Policy Decision至少应可追溯到Actor/Service、输入资源与版本、Action、Purpose、Provider Profile版本、目标Region范围、Policy版本和裁决时间。一次Policy Decision不得被复用为对所有未来调用的永久授权。

## 6. 变更触发

Provider条款、子处理商、模型版本、区域路由、日志保留或数据训练政策发生变化时，应触发Profile版本更新和重新评估。若变化影响既有授权或处理依据，应暂停受影响调用，直至M18及专业审查完成判断。

## 7. 当前状态

本模型供M15/M18及Security/Privacy/Legal审议。没有任何Provider、Region或跨境处理安排在本阶段被批准。