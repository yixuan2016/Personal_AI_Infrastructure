# AEE / ASCP V1.0.0-RC0 评审包

本包是架构研究与机器可读契约候选稿，不是生产实现或互操作测试报告。

## 文件

-   `AEE_ASCP_V1.0_RC0_接口与数据契约评审稿.md`：中文评审稿
-   `schemas/AEE_ASCP_V1.0_RC0.schema.json`：JSON Schema Draft 2020-12
-   `mappings/Ontology_V3_AEE映射矩阵.csv`：六类对象与 Ontology V3.0
    映射
-   `mappings/AEE事件扩展目录.csv`：新增事件与既有事件复用清单
-   `examples/A2A_AEE_Extension_示例.json`：A2A 扩展示例

## 状态

RC0，待架构评审。正式冻结前仍需确认治理域
URI、签名配置、租期参数、订阅投递和保留策略。

- `examples/AEE_ASCP_六类对象样例.json`：六类对象最小合法样例，已通过 Draft 2020-12 Schema 校验。


## 版本关系与权威修订说明

- V1.0.0-RC0 保留为初始历史候选稿；当前设计应以同目录的 V1.1.0-RC0 双站点互操作设计为准。
- V1.0 中将 `TaskClaimLease` 认领权归于 SCO 的表述已被 V1.1 修订，不得作为当前权威规则使用。
- V1.1 将规范对象调整为站点本地 `TaskClaim`：由站点本地任务协调器对本地 TaskStage 原子认领；它不等同于资源所在地 Lease Authority 签发的 `LocalResourceLease` 或 `FencingToken`。
- V1.1 仍为 RC0 候选，待双方 Owner/架构委员会评审；18 项增量互操作验收及总计 66 项候选检查仍待执行。
