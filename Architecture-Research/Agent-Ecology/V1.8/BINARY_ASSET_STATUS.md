# Agent Ecology V1.8｜二进制资产状态

核验日期：2026-11-10

## 已推送

- V1.8 的 Markdown 架构说明、协议/治理边界与 SVG 源图已进入 `docs/agent-ecology-v1.8-20261110`。
- 当前 PR #12 为 Draft，base 为 PR #11 的工作分支；尚未合并。

## 尚未进入 GitHub 的原始二进制

| 原始资产 | 大小（字节） | 状态 |
|---|---:|---|
| Agent_Ecology_V1.8_跨生态联邦进化与多生态协同治理架构.docx | 51,581 | 待二进制上传 |
| Agent_Ecology_V1.8_跨生态联邦进化与多生态协同治理架构.pdf | 41,457 | 待二进制上传 |
| Agent_Ecology_V1.8_跨生态联邦进化与多生态协同治理_完整资料包.zip | 1,581,949 | 不上传 ZIP，保留独立源文件 |
| Agent_Ecology_V1.8_8K架构图集_PNG_SVG.zip | 1,549,939 | 不上传 ZIP，SVG 源图已入库 |

## 限制

当前会话的 GitHub 写入通道无法从 Library 直接传输原始 DOCX/PDF/PNG 字节。文本和 SVG 源文件已推送，但原始 Word/PDF/PNG 不标记为已上传。后续应通过本地 Git、Git LFS 或 GitHub Release 上传原件，并复核文件大小与 SHA-256。


## 2026-11-21 重基复核

- V1.2—V1.7 已通过 PR #11 合入 main；V1.8 不再以旧 PR #11 工作分支作为 base。
- V1.8 源文件已复制到独立 mainline 分支 integration/agent-ecology-v1.8-mainline-20261121，基于 main；当前 PR #17 Draft/Open。
- 原 stacked PR #12 因重复历史文件已关闭，V1.8 由 PR #17 继续审查。
- 3 张 SVG 源图已纳入 Git；3 张 8K PNG 原始渲染文件仍未上传，仍按本表登记。
- Word/PDF/ZIP 原件仍未上传；不以 SVG、提取文本或本地 SHA 清单冒充原始二进制。
- 7 份 JSON Schema 仅完成 JSON 语法解析；Draft 2020-12 完整验证、语义验证、密码学验证仍 NOT_RUN。
- F0 Gate 12 项全部 NotRun；无真实成员登记、Owner 签署、密钥演练或双生态互操作测试。
