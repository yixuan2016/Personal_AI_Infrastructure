# 478｜S1字段级治理、分类、Purpose与权限绑定矩阵

**状态：** Governance Mapping Candidate；Legal/Security/Privacy Review Pending

## 1. 字段级治理原则

对象级Classification只是默认下限，字段/片段/派生内容可以提高敏感度。读取、处理、导出、模型外发、Embedding、Memory准入和删除均需要按当前Purpose和Policy重新评估。字段存在于对象中不代表每个Actor都可以读取。

## 2. 字段组分类建议

| 字段组 | 典型字段 | 风险关注 | 控制要求 |
|---|---|---|---|
| 稳定身份 | source_id、asset_id、evidence_id | 跨系统关联 | 稳定Ref最小暴露 |
| 外部身份 | origin_identity_ref、external_resource_id | Provider账号/资源枚举 | 按Purpose隐藏 |
| Locator | URL、文件位置、MessageRef、DOM路径 | 暴露账户、个人和内容 | 受控读取、日志脱敏 |
| 正文/片段 | content_ref、excerpt_ref、Chunk内容 | 个人/第三方敏感信息 | 字段/片段级PEP |
| Digest | byte_digest、text_digest | 跨租户内容存在性侧信道 | 不默认公开，不作为身份 |
| Actor/DataSubject | actor_ref、data_subject_refs | 主体识别 | 最小化和访问审计 |
| Rights/Consent | rights_refs、basis_refs | 权利和授权范围 | 治理模块受控读写 |
| Purpose/Policy | purpose_ref、policy_decision_ref | 使用场景与策略 | 不得由调用者伪造Decision |
| Processor/Provider | processor_version、provider_ref、region_ref | 外发、保留、区域 | 每次外发重新检查 |
| Error/Logs | error_class、resource_usage_summary | 可能泄露输入或账户信息 | 结构化最小日志 |
| Projection | Embedding、Index、Summary | 继承源敏感度 | 权限不低于源资产 |

## 3. Purpose绑定矩阵

| 操作 | 必需Purpose | 需重新执行Policy | 可能需要Consent/其他依据 | 其他守卫 |
|---|---|---|---|---|
| RegisterSource | 是 | 是 | 按来源/主体判断 | 来源身份核验 |
| CaptureSnapshot | 是 | 是 | 按数据主体和来源权利 | Rights Snapshot、最小化 |
| ReadRawAsset | 是 | 是 | 按当前处理依据 | M02 Host Permission |
| CreateKnowledgeAssetVersion | 是 | 是 | 按内容来源/编辑方式 | 精确输入版本 |
| RunExtraction | 是 | 是 | 外部Provider/敏感内容时重点评估 | 沙箱、Processor Version |
| PublishChunkSet | 是 | 是 | 按派生数据适用范围 | 源权限继承 |
| ReadChunk/Embedding | 是 | 是 | 按源内容和当前用途 | 不能绕过源Policy |
| RegisterEvidence | 是 | 是 | 按证据内容和数据主体 | Target Version/Locator |
| Export/Provider Egress | 是 | 每次调用 | 视适用依据/Consent | Provider/Region/Retention/Approval |
| Delete/Withdraw | 是 | 是 | 撤销/删除请求主体验证 | Tombstone/传播闭包 |

## 4. Rights/Consent/Other Basis/Policy/Approval分离

Source Rights是来源许可证、Provider条款或合同限制；Processing Basis是当前场景适用的处理依据；ConsentGrant是数据主体在适用场景中作出的授权行为记录；Purpose说明本次处理为何发生；PolicyDecision判断当前Actor/Resource/Purpose/Operation是否允许；Approval是有权主体对具体高风险操作的批准；Owner Confirmation是本人对个人表达、意图或记忆采纳的确认。任何一项不能自动替代其他项。

## 5. Provider外发检查

每次ModelInvocation检查字段最小化、Purpose、数据主体、Source Rights、适用Consent/其他依据、Provider身份、Region、Retention、训练/再利用条款、删除能力、Policy版本、Approval和Owner Confirmation。Provider、模型、区域、账号、条款变化都应重新评估。Unknown条件下高敏数据Fail Closed。

## 6. 删除与派生继承

Chunk、Embedding、Summary、Context、Cache、Export和日志继承源数据分类或更严格分类。源数据撤销/删除时，Projection Owner按血缘执行Restriction/Invalidation/Purge；重建时应用最新Tombstone和Policy状态。

## 7. 未决专业问题

具体法律处理依据、第三方邮件/语音处理、跨境传输、Provider训练使用、Retention和法定保留例外不在本阶段决定，必须由Privacy/Legal/Security及真实Owner审查。
