# GitHub 同步状态

## 仓库与目录
- 仓库：`yixuan2016/Personal_AI_Infrastructure`
- 独立目录：`Architecture-Research/Agent-Ecology/`
- V1.2—V1.7：PR #11，Draft/Open，目标 main。
- V1.8：PR #12，Draft/Open，目标为 V1.2—V1.7 归档分支（stacked review）。
- V1.9：PR #14，Draft/Open，目标为 V1.8 分支 `docs/agent-ecology-v1.8-20261110`。

## 当前云端资料
- V1.2—V1.7：历史研究报告、机器可读契约、SVG 架构源图、证据和验收矩阵。
- V1.8 子目录：31 个版本资料源文件，另有 `BINARY_ASSET_STATUS.md` 与 `GITHUB_BLOB_MANIFEST.md`。
- F0：治理章程、RACI、跨域授权矩阵、决策登记册、12 项 Gate。
- V1.8：7 类候选 Schema、23 项验证矩阵、16 项威胁矩阵，全部 NotRun。
- V1.9：主报告、7 项研究证据、22 项合成实验/验收设计、8 项候选 ADR、12 项威胁项、STATUS 和 Git Blob Manifest。
- 8K PNG、Word、PDF 和 ZIP 作为独立交付附件；未上传的二进制文件不标记为 GitHub 已同步。

## 审查状态
- V1.3—V1.7 六份主报告的 41 个图片引用均已核验为有效 SVG 路径。
- PR #11 有 100 个变更路径；Draft/Open，目标 main。
- PR #12 有 36 个变更路径；Draft/Open，目标 V1.2—V1.7 分支。
- PR #14 有 11 个变更路径；Draft/Open，目标 V1.8 分支。GitHub 当前返回 mergeable=false；独立 Compare 显示 V1.8 基线是 V1.9 分支祖先且 behind_by=0。仍保持 Draft，不自动合并，须完成正式审查并复核可合并状态。
- V1.9 的 22 项实验全部 NOT_RUN；8 项 ADR 均 Candidate；未取得 Owner 签署。
- F0 Gate 未通过；无真实成员登记、密钥演练或双生态互操作测试。
- 未执行 Runtime、红队、生产或现场验收。
- 所有 PR 均未合并；main 未修改。

## 校验说明
- V1.9 Git Blob Manifest 记录 Git Blob SHA，不等于 SHA-256 文件摘要。
- 远端文件回读和 PR 变更统计不等于本地资料包 SHA-256、ZIP 完整性或实验验收。
