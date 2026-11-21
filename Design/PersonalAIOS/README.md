# Personal AI Life OS｜研究设计版本导航

本目录维护个人数智底座 / Personal AI Life OS 的独立研究设计版本。版本目录按阶段增量保存，历史版本保留；研究文档入库不代表工程实现、Owner批准或产品发布。

## 版本入口

- [V2.21｜Stage33 S1 六个 OT 字段级 Profile 与 Owner 审议准备](./V2.21/README.md)
- [V2.22｜Stage34 S1 Owner 审议操作化与定稿准备](./V2.22/README.md)

## 当前状态

- V2.21 已通过 PAI PR #1 合入 main。
- V2.22 本轮从历史 stacked PR #2 选择性迁移到以当前 main 为基线的清洁候选分支。
- V2.22 Stage34 新增 20 份编号文档（484—503）；累计编号 00—503，共 504 份。
- 六个 S1 OT 仍为 Candidate；142 个字段定义待真实 Owner 逐项审议；新增 Owner Feedback/Approval 证据为 0。
- 56 项负向测试已设计、0 项执行；Security/Privacy/Legal 审查 Pending。
- S1 Freeze Not Ready；Design Freeze Not Ready；Engineering Not Authorized；Implementation Not Started。

## 使用规则

1. 个人数据、个人事实、个人授权和个人记忆仍由 Personal Owner 控制。
2. 候选字段、Schema、对象关系和决策记录不得被解释为已批准生产契约。
3. 任何 Owner 决策必须有真实身份、授权范围、精确版本、批准证据和审计记录。
4. 测试设计、桌面推演、静态检查与真实执行/独立验收分开记录。
5. 本目录只维护研究设计资产，不替代 `palos` 产品工程仓库，也不自动授权工程实现。


## V2.23｜Stage35 S1 Owner 反馈与原子决策闭环
- [V2.23 研究入口](./V2.23/README.md)：接收真实 Owner 反馈、来源核验、字段处置、ACR/OD 路由、Profile 差异与回滚、56 项负向测试追踪。
- 本阶段新增编号文档 504—523，共 20 份；S1 仍以六个既有 OT 为范围，不自动新增 OT/OF。
- Owner Feedback、批准、ACR 与负向测试的状态以 V2.23 Manifest 的可核验证据为准；无真实来源的意见不得伪装成 Owner 决策。
- V2.23 为候选研究包，不代表 S1 Freeze、Design Freeze 或工程授权。


## V2.24｜Stage36 首批高风险决策审议包
- [V2.24 研究入口](./V2.24/README.md)：D-01—D-07 高风险决策、Owner 审议规程、证据来源链、DecisionRecord、消费者测试追踪、专业审查和 ProfileDelta。
- 本阶段新增编号文档 524—543，共 20 份；不新增 OT/OF。
- 142 个字段进入首批高风险审议范围；真实 Owner Feedback、Owner Approvals、ACR Approvals 均为 0。
- 56 项负向测试仍为 Designed / 0 Executed；Security/Privacy/Legal 专业审查 Pending。
- S1 Freeze Not Ready；Design Freeze Not Ready；Engineering Not Authorized；Implementation Not Started。
