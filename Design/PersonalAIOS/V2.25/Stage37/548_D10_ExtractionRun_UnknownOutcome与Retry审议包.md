# 548｜D-10 ExtractionRun UnknownOutcome与Retry：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

外部处理调用可能在请求已被服务端接收或执行后发生超时、连接断开或回执丢失。此时本地无法判断任务是否执行、是否产生输出或是否产生计费/外部副作用。将UnknownOutcome直接标记Failed并重试，可能重复处理、重复扣费、重复发送或产生不一致派生资产。

## 2. 关联字段与权威边界

- EXT-016 run_state
- EXT-019 error_class
- EXT-020 retry_of_ref
- EXT-021 idempotency_scope_ref
- EXT-022 correlation_id
- 联动EXT-003/004输入、EXT-017/018输出及EXT-012 Provider Profile。

主决定权威候选：M08负责运行记录和状态；M15负责外部调用与Provider对账能力；M06负责状态语义和合法迁移。

## 3. 必须回答的问题

1. UnknownOutcome的进入条件是什么，如何与Failed、Cancelled、TimedOut和PartiallyCompleted区分？
2. 是否存在Provider operation ID或可查询的执行状态接口？
3. correlation_id与idempotency_scope_ref分别承担什么责任？
4. retry_of_ref表示逻辑任务的前次尝试、直接父尝试还是整个重试链？
5. 对不支持幂等键的Provider，如何防止重复副作用？
6. 对已执行但输出丢失的任务，如何安全恢复结果或人工对账？
7. 何时允许自动重试，何时必须暂停并等待人工判断？
8. 失败补偿是否会引入新的外部副作用，谁批准补偿？

## 4. 候选方案（不构成推荐或批准）

- A：显式UnknownOutcome状态，先对账再决定重试；安全边界清楚，但可能延长任务恢复时间。
- B：以稳定Idempotency Scope和Provider Operation ID协调重试；自动化程度较高，但依赖Provider能力和严格键生命周期。
- C：不支持可靠对账的Provider禁止自动重试，转人工确认或新建明确的新任务；保守但增加人工成本。

## 5. 必须提供的证据

- M15调用生命周期、超时语义和Provider状态查询能力；
- Provider幂等键支持、保留时长和重复请求行为说明；
- correlation_id、operation ID和回执样例；
- 重复计费、重复输出、重复写入和部分完成的风险分析；
- 补偿操作及其授权和审计规则。

## 6. 下游影响与测试

影响ExtractionRun状态机、任务队列、费用核算、输出资产创建、Chunk发布和事件消费。UnknownOutcome不得被下游当作Succeeded或Failed；在对账完成前，输出必须保持不可发布或隔离。

测试覆盖请求已接收但响应丢失、请求未送达、Provider完成但输出未落库、重复提交、幂等键过期、并发重试、部分完成、回执乱序和对账服务不可用。

## 7. 阻断条件

无法区分请求是否被接收；没有可靠对账方式却允许自动重试；幂等范围不明；副作用没有唯一关联标识；UnknownOutcome被错误映射为成功或失败。

## 8. 当前状态

本文件仅形成D-10审议准备包。没有真实Owner反馈或Provider证据；EXT-016及EXT-019至EXT-022继续保持Pending。