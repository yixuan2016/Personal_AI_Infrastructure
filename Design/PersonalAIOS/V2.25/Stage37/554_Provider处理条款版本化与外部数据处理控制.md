# 554｜Provider处理条款版本化与外部数据处理控制

**状态：** Provider Contract Control Candidate；No Provider Approved

## 1. 目的

把Provider外部处理条款转化为可审查、可版本化、可映射到Policy的控制对象，防止“已签合同”“默认不训练”或“区域可选”等模糊表述被误当作具体数据处理授权。

## 2. Provider Profile最小审查维度

| 维度 | 必须明确 |
|---|---|
| Contract Identity | 合同/条款版本、生效日期、适用主体和地区 |
| Data Role | Provider及各子处理商的处理角色和责任 |
| Input Use | 输入是否用于推理、服务改进、训练或人工审查 |
| Output Use | 输出、派生内容和反馈数据的使用范围 |
| Retention | 在线数据、缓存、日志、备份和支持工单的保留期限 |
| Deletion | 删除请求渠道、时限、例外和可核验回执 |
| Region | 计算、存储、日志、人工访问和灾备地区 |
| Subprocessors | 子处理商名单、变更通知和异议机制 |
| Security | 加密、访问控制、隔离、审计和事件通报 |
| Portability | 数据导出、格式和服务终止后的处置 |
| Human Access | 人工支持、调试、质量抽查和审批要求 |
| Incident | 泄露/故障通知、调查配合和证据保存 |

## 3. 版本化原则

Provider Profile每次变化都应有独立版本、原始条款引用、变更摘要、适用时间和审查状态。ExtractionRun必须引用调用发生时适用的Profile版本，不能在Provider条款变化后把历史运行记录自动指向新版本。

## 4. 与M15/M18分工

M15维护Processor/Provider能力目录、集成事实和实际调用记录；M18决定当前Purpose、数据范围、Actor、Provider和Region组合是否允许；Security/Privacy/Legal审查其专业范围；M08保存ExtractionRun实例和引用。任何一方都不能替代其他方。

## 5. Fail Closed场景

Provider Profile缺失或过期、实际Region无法证明、子处理商未审查、训练用途未知、数据保留条款冲突、Policy Decision缺失或不匹配时，受影响的高敏处理不得继续。允许的本地处理或低风险路径应作为单独授权的降级方案，不得自动绕过审查。

## 6. 审计要求

每次外部处理至少能够追溯请求输入范围、处理器版本、Profile版本、Policy Decision、实际Region证据、Provider Operation ID、输出引用、完成状态和后续删除义务。不得在普通日志或Digest中保存API密钥、访问令牌或其他秘密。

## 7. 当前状态

本文件只建立条款审查框架。未核验具体合同、Provider能力或区域证据前，不得将任何外部服务标记为Approved Provider。