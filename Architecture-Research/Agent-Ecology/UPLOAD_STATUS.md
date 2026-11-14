# GitHub 同步状态

## 仓库与目录
- 仓库：`yixuan2016/Personal_AI_Infrastructure`
- 独立目录：`Architecture-Research/Agent-Ecology/`
- V1.2—V1.7：PR #11，Draft/Open，目标 main。
- V1.8：PR #12，Draft/Open，目标为 V1.2—V1.7 归档分支（stacked review）。
- V1.9：PR #14，Draft/Open，目标为 V1.8 分支 `docs/agent-ecology-v1.8-20261110`。

## 当前云端资料
- V1.2—V1.7：历史研究报告、机器可读契约、SVG 架构源图、证据和验收矩阵。
- V1.8：跨生态联邦架构、F0 治理章程、RACI、跨域授权矩阵、12 项 F0 Gate、7 类候选 Schema、23 项验证矩阵和 16 项威胁矩阵。
- V1.9-A：主研究报告、7 项研究证据、22 项 Stigmergy 合成实验、8 项基础 ADR 和 12 项基础威胁。
- V1.9-B：跨生态能力发现备忘录、研究证据边界、2 份候选 JSON Schema、20 项 F1 验收矩阵、Observation Runtime SVG、ADR-109/110 和能力发现契约静态审查。
- V1.9 汇总：42 项实验/验收全部 NOT_RUN；10 项 ADR 全部 Candidate；18 项威胁全部 Candidate。
- 8K PNG、Word、PDF 和 ZIP 作为独立交付附件；未上传的二进制文件不标记为 GitHub 已同步。

## 审查状态
- V1.3—V1.7 六份主报告的 41 个图片引用均已核验为有效 SVG 路径。
- PR #11 有 100 个变更路径；Draft/Open，目标 main。
- PR #12 有 36 个变更路径；Draft/Open，目标 V1.2—V1.7 分支。
- PR #14 有 18 个变更路径；Draft/Open，目标 V1.8 分支。GitHub 的 mergeable 字段在连续读取中出现 true/false 不一致；保持 Draft，不自动合并，合并前需重新核验并完成正式审查。
- V1.9 CSV 已完成静态列数复核：研究证据 7 行/11 列、Stigmergy 矩阵 22 行/6 列、F1 矩阵 20 行/7 列、威胁矩阵 18 行/7 列。
- 两份候选 JSON Schema 已通过 JSON 语法解析检查；尚未完成完整 Draft 2020-12 Validator、签名验证、跨字段语义验证或协议互操作。
- 能力发现契约静态审查列出 10 项缺口，候选 Schema 未据此自动修改。
- V1.8 F0 的 12 项 Gate 全部 NotRun；F0 未通过，真实双生态试点仍被阻断。
- 未执行 Runtime、红队、生产或现场验收；Runner 未启用；生产凭证未接入。
- 所有 PR 均未合并；main 未修改。

## 校验说明
- V1.9 Git Blob Manifest 记录 Git Blob SHA，不等于 SHA-256 文件摘要。
- 远端文件回读、JSON 语法解析和 CSV 静态列数复核不等于完整 Schema 验证、密码学验证、实验执行或生产验收。
