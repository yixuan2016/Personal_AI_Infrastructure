# 算力底座架构研究资料总目录

本目录集中沉淀“算力底座”项目的架构研究、协议契约、治理矩阵、双站点联邦验证与版本发布资料。研究范围为架构设计和技术决策，不包含未经批准的工程实现代码。

## 目录原则

- `00-Source-Baselines/`：源基线、术语、范围与设计输入。
- `01-G0-Architecture-Governance/`：架构治理、责任边界、决策与签署机制。
- `02-G1-Ontology-Protocol-Consistency/`：Ontology V3.1、DM04/IFC0.2、语义与协议一致性。
- `03-G2-OntologyV3.1-IFC0.2-Contract-Governance/`：ADS/SCO API、75个操作映射、六域权威矩阵与契约缺口。
- `06-G2-04-REST-Binding-RC1-Dual-Site-Transaction/`：REST Binding RC1、双站点交易状态机、Prepare/Commit、回执、故障注入与互操作验收。
- `archives/`：各阶段完整归档包。
- `manifests/`：文件清单与SHA-256校验记录。

## 当前已确认的架构原则

1. 本地与云端混合运行、混合式数据架构、渐进式微服务拆分是既定方向；部署位置、数据架构和服务拆分是三个独立决策维度。
2. ADS承担跨域治理、共同语义、能力发现与协同，不取代领域Owner的最终授权和专业责任。
3. SCO负责跨站点任务/资源协调，不取代站点本地Task Owner、PDP/PEP和Lease Authority。
4. Operation只表达命令/编排状态；业务对象状态必须由其权威Owner提供。
5. Prepare不等于Commit；Plan选择不等于资源预留；SCO不签发本地Lease/FencingToken。
6. 结果提交、独立验收、计量和结算必须保持责任主体分离。
7. UNKNOWN状态必须触发权威对账，不得推定成功或失败；撤销水位过期时高风险操作Fail-closed。

## G2-03 盘点摘要

- ADS：40 operations / 38 paths。
- SCO：35 operations / 35 paths。
- 合计：75 operations。
- 已形成六域Owner/Coordinator/Authority映射、16项契约缺口、关键对象状态机与REST Header/Envelope绑定矩阵。
- 关键待整改项：RequestEnvelope未被Path引用、GenericCommand过宽、强类型响应不足、EvaluatePolicy结果类型、Operation与业务状态分离、Idempotency/Request-ID/Correlation-ID/If-Match Header声明、ListRunOperations文档与OpenAPI差异。

## 发布状态说明

当前研究归档分支：`docs/compute-base-g2-20261110`。本目录内容以阶段性提交方式进入仓库；必须以分支HEAD、文件清单和SHA-256核验结果判断完整性。未完成的批次不得标记为“全部推送完成”，未经评审不得合并到main或标记正式冻结。
