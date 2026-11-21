# 497｜S1 Security / Privacy / Legal 独立审查议题册

**状态：** Independent Review Docket Prepared；Professional Review Pending

## 1. 审查定位

本议题册将S1六个Profile中需要专业审查的风险集中登记。它不提供法律意见，不确定适用司法辖区、具体处理依据或保留期限，也不把Security/Privacy/Legal审查等同于业务Owner批准。

## 2. 审查议题

| Docket ID | 主题 | 关键问题 | 相关对象 | 必须形成的输出 |
|---|---|---|---|---|
| SPL-001 | 多主体与第三方数据 | Source/邮件/附件中多主体如何识别、最小化和隔离 | Source/Snapshot/KnowledgeAsset | 主体识别不确定性与访问边界 |
| SPL-002 | Source Rights | 来源许可、合同、Provider条款和Consent如何区分 | Source/Snapshot | Rights映射与未知状态处理 |
| SPL-003 | Processing Basis | 当前处理依据由谁确认，如何与Purpose/Consent分离 | Snapshot/ExtractionRun | M18登记和专业审查路径 |
| SPL-004 | Data Classification | 字段/片段/摘要/Digest/Embedding是否继承或提高分类 | 全部 | 分类继承规则 |
| SPL-005 | Retention | 期限、例外、法律保留和删除请求如何处理 | RawAsset/KnowledgeAsset/Run/Chunk/Evidence | 保留目录和例外流程 |
| SPL-006 | Provider Egress | 每次外发如何核验字段最小化、Purpose、Provider和Region | ExtractionRun | Egress审查清单 |
| SPL-007 | Provider Training/Re-use | 训练、再利用、人工访问和日志使用条款如何识别 | ExtractionRun | 条款版本与允许范围 |
| SPL-008 | Region/Transfer | 实际处理区域和跨境传输如何记录 | ExtractionRun | Region证据及适用审查 |
| SPL-009 | Sandbox | OCR/ASR/Parser是否隔离恶意文件、脚本和网络 | ExtractionRun | 隔离控制清单 |
| SPL-010 | Locator/Credentials | URL、MessageRef、凭据和路径是否泄露 | Source/Evidence | Locator脱敏和秘密隔离 |
| SPL-011 | Digest Side Channel | Digest是否泄露跨主体内容存在性 | RawAsset/Evidence/Chunk | 访问控制和去重约束 |
| SPL-012 | Derived Data | Chunk/Embedding/Summary/Context如何继承权限 | KnowledgeAsset/Chunk | 派生权限闭包 |
| SPL-013 | Deletion/Backup | 主存、副本、缓存、Provider和备份的删除证明如何形成 | RawAsset/KnowledgeAsset/Chunk/Evidence | 删除范围和回执 |
| SPL-014 | Evidence Excerpt | 摘录是否必要、范围是否最小、是否涉及第三方 | Evidence | Excerpt准入与审计 |
| SPL-015 | Audit/Logs | 错误、资源用量、Correlation ID是否泄露内容或身份 | ExtractionRun/全局 | 日志字段最小化 |

## 3. 审查方法

每项议题应记录数据类别、主体、处理目的、操作、数据流向、接收方、区域、保留、访问主体、派生数据、删除能力、剩余风险和专业意见。未知项不得通过假设补齐；高敏或外发风险未厘清时Fail Closed。

## 4. 审查意见状态

`NotStarted`、`InReview`、`ClarificationRequired`、`Approved`、`ApprovedWithConditions`、`Rejected`、`Deferred`。`Approved`必须附专业审查人身份、审查范围、依据版本、意见日期和证据引用。业务Owner仍须独立作出其权限内的批准。

## 5. 禁止事项

不得将通用安全检查表当作渗透测试报告；不得声称已符合某一法律或认证；不得凭模型判断替代律师/隐私专业人员意见；不得将Provider宣传页当作合同条款证据；不得将删除API响应当作备份不可恢复的充分证明。

## 6. 当前状态

SPL-001—015均为待审查议题。当前未形成新的Security/Privacy/Legal批准证据，具体法律依据、Retention期限、Provider和Region安排仍保持未决。
