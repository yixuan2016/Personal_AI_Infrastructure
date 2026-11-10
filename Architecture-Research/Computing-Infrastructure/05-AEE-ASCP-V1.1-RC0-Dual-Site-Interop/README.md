# AEE/ASCP V1.1.0-RC0 双站点联邦互操作设计包

**状态：** 架构候选，待双方 Owner
与架构委员会评审；非工程实现、非真实部署、非生产验收。

## 本版关键结论

-   AEE/ASCP 是横切 DM04 六域的 Profile，不是第七接口域。
-   六对象映射到既有权威；不新建全局授权、Lease、事件事实库或 Artifact
    Registry。
-   TaskClaim 是站点本地任务阶段认领；与 LocalResourceLease 分离。
-   TraceRecord 映射 CloudEvents；FWSX 只负责事件交付。
-   A2A 1.0 扩展声明、请求级激活和 Task metadata 按官方扩展机制处理。
-   复用 DM04 48项，新增 AEE/ASCP 18项；总计66项候选检查，均待执行。

## 文件清单

-   Word / Markdown 架构设计稿
-   JSON Schema：AEE Profile Context 与
    TaskClaim（增量Schema，不替代DM04基础Schema）
-   六域权威映射矩阵、对象迁移矩阵、事件映射矩阵
-   18项双站点专项验收矩阵
-   A2A 1.0 扩展示例
-   SVG 矢量架构图、7680×4320 PNG、Mermaid流程源
-   SHA-256 清单

## 重要限制

本包不代表双站点真实互操作测试已通过，不代表DM04
IFC0.2已批准，不代表AEE扩展URI已正式注册。
