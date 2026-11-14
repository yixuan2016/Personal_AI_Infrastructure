# V1.9 状态记录

- 版本：Agent Ecology V1.9｜痕迹协作实证、能力发现与联邦目录
- 日期：2026-11-14
- 状态：Candidate / Draft
- 工作分支：research/agent-ecology-v1.9-stigmergy-20261114
- 基线：PR #12 的 V1.8 分支 HEAD 4e337089470076b25058a7c47edaacab77bcaa58

## 工作流 A｜Stigmergy 与共享环境
- 主研究报告、7 项研究证据登记、22 项合成实验与验收矩阵、8 项基础候选 ADR、12 项基础威胁与治理边界已入库。
- 22 项合成实验全部 NOT_RUN。

## 工作流 B｜跨生态能力发现与联邦目录
- 能力发现与目录联邦架构决策备忘录及独立研究证据边界已入库。
- 能力广告、能力解析和能力生命周期 CloudEvents JSON Schema：3 份 Candidate；JSON 语法已通过解析检查，但未完成 Draft 2020-12 完整验证。
- F1 能力发现与契约验收矩阵：30 项，全部 NOT_RUN。
- 新增 Observation Runtime、联邦目录新鲜度、撤销水位、A2A/MCP/CloudEvents/SPIFFE 协议边界设计。
- 新增 7680×4320 SVG 架构源图。
- 新增 2 项候选 ADR：ADR-109、ADR-110。
- 新增能力发现契约静态审查：10 项缺口；7 项形成候选修复、1 项部分修复、2 项仍开放；完整 Validator 与密码学验证未执行。

## 总体边界
- 合成实验与验收：52 项，全部 NOT_RUN。
- 架构决策：10 项，全部 Candidate，未获正式批准。
- 威胁与治理边界：18 项，全部 Candidate。
- V1.8 F0 Gate：12 项全部 NotRun，F0 未通过。
- 生产实现：未开始；本轮不包含工程代码。
- 真实数据：未导入；未获得任何新增数据共享授权。
- Runtime/双生态/生产测试：未执行。
- 人类审批、独立评估、Owner 签署：未取得。
- Runner：未启用；生产凭证未接入。
- 主线：未修改；V1.9 作为 stacked review 候选增量，不直接合并 main。
- productionAllowed=false

## 验收边界
- 研究资料入库不等于研究结论已在本项目复现。
- JSON 语法解析通过不等于 JSON Schema 完整验证或密码学验证。
- 静态文件回读不等于实验执行。
- Git Blob Manifest 只记录 Git 对象标识，不代替 SHA-256 校验。
- 所有未执行项必须保持 NOT_RUN；不得将候选 ADR 解释为已批准决策。
