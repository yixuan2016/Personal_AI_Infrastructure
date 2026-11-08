# 555｜ExtractionRun UnknownOutcome状态机与对账流程

**状态：** Run State Machine Candidate；No Runtime Implementation

## 1. 设计原则

UnknownOutcome描述“执行是否发生或结果是否完整，当前无法确定”的认知状态，不是普通失败码。网络超时、连接断开或回执丢失，只能证明本地没有及时获得结果，不能证明Provider没有执行。

## 2. 状态维度分离

至少区分：
- 本地调度状态：是否创建、准备、提交和等待；
- 外部执行状态：Provider是否接收、执行、完成或拒绝；
- 结果持久化状态：输出是否已完整接收、校验和登记；
- 业务发布状态：输出是否允许成为KnowledgeAsset版本或ChunkSet。

上述状态可能不同步，不能压缩为一个“成功/失败”布尔值。

## 3. 状态机候选

Created → Dispatching → Submitted → Running → Succeeded / Failed / Cancelled。

当请求可能已被接收但无法取得权威终态时，进入UnknownOutcome。随后进入ReconciliationPending，并根据可核验事实分流为：
- ReconciledSucceeded：确认外部处理已完成，继续核验输出和回执；
- ConfirmedNotExecuted：有证据确认请求未执行，允许按策略决定重试；
- PartialSideEffectDetected：发现部分外部副作用，先执行对账/补偿审查；
- ManualResolutionRequired：无法自动确认，等待授权人员处理。

以上为状态语义候选，最终枚举和迁移守卫由M06审议，实例状态由M08维护，外部事实由M15提供。

## 4. 对账优先级

1. 使用Provider Operation ID查询权威状态；
2. 使用稳定Correlation ID查询请求与回执；
3. 对照Provider账单、任务记录或服务端审计证据；
4. 对照本地输出清单、Manifest和写入记录；
5. 仍无法确定时进入ManualResolutionRequired，不得推断成功或失败。

## 5. 输出隔离

UnknownOutcome期间，未确认的输出不得被标记为可用KnowledgeAsset版本，不得发布ChunkSet，不得进入正式检索和Context。若外部已产生输出但本地尚未取得，必须通过对账和完整性核验后再登记。

## 6. 时间与升级

每个UnknownOutcome应记录进入时间、最后查询时间、对账责任角色、Provider响应期限、下一次复核时间和超时升级路径。期限到达只触发升级，不自动把状态改成Failed。

## 7. 当前状态

本文件是状态机设计候选，不改变EXT-016字段定义，不执行真实Provider调用，也不代表M08/M15已批准状态枚举。