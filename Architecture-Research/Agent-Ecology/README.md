# Agent Ecology｜群体智能生态架构研究

本目录独立管理 Agent Ecology V1.2—V1.8 研究资料，不与 Personal AI Life OS 主体设计、算力底座其他专题混放。

## 版本导航
- V1.2：协议契约与机器可读协作规格
- V1.3：痕迹协作、自组织协作与 ADS 生态融合
- V1.4：Environment Runtime
- V1.5：群体智能经济与生态自治
- V1.6：生态世界模型与数字孪生
- V1.7：生态级 RSI 与递归进化治理
- V1.8：跨生态联邦进化、多生态协同治理与 F0 成员边界

## 资料形态
Markdown、CSV、JSON、YAML 和 SVG 源文件纳入 Git。8K PNG、Word、PDF 和 ZIP 交付文件另行提供；SVG 可无损渲染为 8K PNG。未上传的原始二进制不标记为远端已同步。

## 统一架构原则
1. Environment 是本生态真实状态权威；World Model/Twin 只产生预测和仿真状态。
2. ADS 负责生态内协调、执行管理和进化，但不取代领域 Owner 的数据与业务权威。
3. Agent 通过共享环境状态、任务工件和事件痕迹协作；A2A 等协议承担发现、协商与传输，不取代状态权威或授权判定。
4. 智能体内环自主执行，人类外环保留根策略、关键审批、独立验证、否决、接管和最终问责权。
5. RSI 生成和验证候选，不自行扩大根权限，不自行签发生产授权。
6. 跨生态协作采用多中心自治、本地授权、证据交换和独立采用。

## V1.8 F0 治理边界
- 每个生态保留独立根治理、身份根、数据权威和本地执行门禁；不设全局超级 ADS。
- FCP 不持有成员域生产凭证，不直接执行成员域副作用动作。
- 跨域授权采用安全交集：任一 DENY 即 DENY；关键 ABSTAIN、过期或撤销状态不可达则 HOLD。
- Agent/RSI 不得修改根策略、根身份、权限上限、审批规则或审计记录。
- F0 治理章程和 Gate 均为候选设计；12 项 Gate 未签署、未演练，全部 NotRun。

## 归档审查与二进制交付
- `ARCHIVE_AUDIT.md` 记录 V1.2—V1.7 图片引用修复、历史副本和审查边界。
- `BINARY_ASSET_STATUS_V1.2-V1.7.md` 与 `V1.8/BINARY_ASSET_STATUS.md` 记录尚未上传的 Word/PDF/PNG 原件及后续上传方式。
- 六份 V1.3—V1.7 主报告的 41 个图片引用已核验为有效 SVG 路径。
- `MERGE_REVIEW_20261121.md` 记录 V1.2—V1.7 归档合并复核及二进制/验收边界。

## 状态边界
所有尚未执行的验证均标记为 NotRun；研究资料入库不等于工程实现、互操作测试或生产验收通过。


## 2026-11-21 主线同步状态
- V1.2—V1.7 已通过 PR #11 合入 main，合并提交：dbcfb283f6f4ab54b1659668135a9359fe6d30e3。
- V1.8 已重新基于 main 建立独立整合分支，避免 PR #11 squash 合并后旧 stacked branch 重复显示历史文件。
- 当前干净整合 PR 为 [#17](https://github.com/yixuan2016/Personal_AI_Infrastructure/pull/17)；旧 stacked PR #12 已关闭，V1.8 内容由 PR #17 继续审查。
- V1.8 仍为候选架构与契约；F0 12 项 Gate 全部 NotRun，未授予生产授权。
