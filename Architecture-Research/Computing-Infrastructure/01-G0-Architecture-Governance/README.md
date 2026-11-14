# 算力底座 G0 架构评审与签署治理包

状态：候选治理方案，待双方 Owner
与架构委员会评审和签署。纯架构研究，不含工程实现代码。

## 关键决策

-   六个接口域保持不变，AEE/ASCP横切六域。
-   SCO负责全局TaskContract/ContractGraph/Plan/Saga/Barrier汇总。
-   Site A/B Local Task Coordinator分别签发本地TaskClaim。
-   Resource Lease/FencingToken由资源所在地Lease Authority独立签发。
-   正式URI尚未注册；所有URI均为模板。
-   DM04 IFC0.2
    profile_extensions仅为增量提案，批准前不得在IFC0.1请求中发送。

## 主要文件

-   G0_架构评审与签署治理备忘录.docx / .md
-   matrices/G0_六域与横切能力_RACI.csv（23项）
-   matrices/G0_签署权威与证据责任矩阵.csv（20项）
-   matrices/G0_URI命名空间注册台账.csv
-   matrices/G0_架构评审签署检查清单.csv（12项）
-   schemas/DM04_IFC0.2_profile_extensions_增量提案.schema.json
-   G0_DM04_IFC0.2_profile_extensions增量提案.md
-   G0_URI命名空间与注册规范.md
-   decisions/ADR-11 / ADR-12 / ADR-13
-   diagrams/G0_权威责任与双站点签署边界.svg / 8K.png
-   MANIFEST_SHA256.txt

## 未完成事项

实际Owner名单、Site
A/B主体、受控域名、双方签署、IFC0.2批准、双实现互操作和真实双站点故障验证。
