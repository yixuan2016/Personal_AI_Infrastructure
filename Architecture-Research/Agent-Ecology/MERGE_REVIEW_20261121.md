# Agent Ecology V1.2–V1.7 归档合并复核（2026-11-21）

- 对应 PR：#11
- 来源分支：docs/agent-ecology-v1.2-v1.7-20261110
- 目标分支：main
- 复核时 head：dca2773d28f9d8955750fbe1717a1019542a1cb2
- 复核时 compare：22 ahead / 0 behind；100 个变更路径
- 复核性质：研究资料归档审查，不是领域 Owner 批准、工程验收或生产准入

## 1. 资产完整性复核

- PR 变更路径共 100 项。
- MANIFEST_SHA256.json 包含 96 个唯一文件条目；路径均唯一，bytes 为整数，SHA-256 均为 64 位十六进制。
- 96/96 Manifest 路径均存在于 PR 文件清单。
- 其余 4 个路径为 ARCHIVE_AUDIT.md、BINARY_ASSET_STATUS_V1.2-V1.7.md、MANIFEST_SHA256.json 自身和 UPLOAD_STATUS.md；这些文件不纳入自身递归哈希清单。
- 变更资产由 Markdown、CSV、JSON、YAML 和 SVG 组成；未包含 DOCX、PDF、PNG 或 ZIP 原始二进制。

## 2. 二进制与图像边界

- V1.2—V1.7 的 SVG 架构图源文件纳入 Git，适合继续编辑和无损渲染。
- Word、PDF、8K PNG 与 ZIP 原件仍按 BINARY_ASSET_STATUS 登记为未上传；超出 GitHub 单文件限制的 PDF/ZIP 需要 Git LFS 或 Release。
- 不将 SVG 冒充 PNG，不将提取文本冒充 DOCX/PDF，不将本地 SHA 清单解释为二进制已上传。

## 3. 研究与验证状态

- 该 PR 是 V1.2—V1.7 的研究归档，不是 V1.9 或生产运行时实现。
- Schema、协议、Ontology、威胁矩阵和验收矩阵保留各自 Candidate/NotRun 状态。
- 未执行完整 JSON Schema Draft 2020-12 验证、密码学验证、跨生态互操作、真实 Runtime、双站点测试或生产测试。
- 资料入库不等于实验复现，不等于 Owner 签认，不改变 productionAllowed=false。

## 4. 合并裁决

本次按用户持续推进研究归档与主线整合的指示，对 PR #11 进行维护者侧内容复核。复核范围仅覆盖文件清单、Manifest 结构、二进制披露和验证状态标记；没有外部领域 Owner 或独立安全审查签认。

**裁决：可作为 V1.2—V1.7 研究源资产归档合入 main；不得标记为完整二进制交付、工程验证通过或生产批准。**

## 5. 后续依赖

- PR #12（V1.8）依赖本 PR 的归档分支；PR #11 合并后，应将 PR #12 base 重定向到 main，再复核差异。
- PR #14（V1.9）依赖 V1.8；须在 PR #12 合并后再重定向到 main。
- V1.9 的 321 项验收、Schema 完整验证、TLC、Runtime 和双生态实测继续保持各自状态，不因本归档合并而改变。
