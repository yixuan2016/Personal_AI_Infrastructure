# 596｜M02 Physical Custodian专项审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M02 Physical Custodian（候选）

## 1. 审议目标与权限边界

确认M02对物理字节、Opaque Handle、宿主访问、加密/密钥、备份副本、物理删除和Custody Receipt的真实权威。M08维护逻辑资产和血缘；M02维护物理保管事实。两者不能以一个Storage状态合并。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围。RAW-004是D-05核心字段；RAW-005/006/007仅作为物理大小和媒体格式事实的横切会审输入，不扩大D-05正式批准范围。此处不表示M02对所有列出字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| SNP-010 | raw_asset_refs | raw_asset_refs是否只引用已登记RawAsset；部分捕获和多文件组成如何表达。 | D-03 | Medium |
| SNP-011 | captured_bytes_digest | captured_bytes_digest摘要的字节范围、规范化、算法和校验主体是否明确。 | D-03 | Medium |
| SNP-012 | digest_scope | digest_scope是否版本化、可枚举；压缩、封装、分段和多文件场景如何定义。 | D-03 | Medium |
| SNP-022 | snapshot_manifest_digest | snapshot_manifest_digest覆盖哪些Snapshot组成项；清单本身如何防篡改和验证。 | D-03 | Medium |
| RAW-004 | physical_handle_ref | physical_handle_ref是否为Opaque Handle；避免暴露Bucket、路径、凭据或可绕过授权的URL。 | D-05 | High |
| RAW-005 | byte_size | byte_size按原始字节还是封装后字节计算；分段/流式资产如何定义。 | 横切关联D-05 | Medium |
| RAW-006 | media_type_declared | media_type_declared来源、可信度和缺失值如何记录；不能当作实际格式证明。 | 横切关联D-05 | Medium |
| RAW-007 | media_type_detected | media_type_detected由何种检测器产生、版本和置信依据；与声明不一致如何处理。 | 横切关联D-05 | Medium |
| RAW-008 | byte_digest | byte_digest的算法、字节范围和规范化规则是否明确；是否支持多摘要。 | D-06 | High |
| RAW-009 | digest_algorithm | digest_algorithm是否允许算法迁移和多算法并存；弱算法何时退役。 | D-06 | High |
| RAW-010 | digest_scope | digest_scope能否准确区分原始字节、封装字节、分块和逻辑内容。 | D-06 | Medium |
| RAW-011 | integrity_state | integrity_state区分未验证、已验证、失效、未知和不可验证；不等于来源可信。 | D-06 | Medium |
| RAW-012 | custody_state | custody_state由谁维护；逻辑保管、物理持有、备份和外部托管是否分离。 | D-07 | Medium |
| RAW-013 | encryption_profile_ref | encryption_profile_ref指向策略还是实际密钥实例；密钥轮换和销毁如何留证。 | D-07 | Medium |
| RAW-019 | deletion_state_ref | deletion_state_ref是否能表达逻辑隐藏、物理删除、备份到期和阻断。 | — | Medium |
| RAW-020 | custody_receipt_refs | custody_receipt_refs由哪个物理权威签发；回执覆盖范围、时间和验证方式。 | D-07 | Medium |
| KAS-005 | raw_asset_refs | raw_asset_refs指向逻辑RawAsset还是物理Handle；删除和保留责任如何继承。 | — | Medium |
| KAS-016 | deletion_dependency_refs | deletion_dependency_refs是否枚举Chunk、Projection、缓存、Provider、导出、日志和备份。 | D-08 | Medium |
| EVD-007 | target_content_digest | target_content_digest摘要哪个目标版本及内容范围；算法与Scope必须明确。 | D-06/D-12 | High |
| EVD-010 | excerpt_digest | excerpt_digest覆盖摘录原始还是规范化文本；不能替代Target Digest。 | D-12 | High |
| EVD-021 | deletion_state_ref | deletion_state_ref区分内容删除、Projection撤除、引用失效和保留例外。 | — | Medium |

## 3. 必须回答的问题

1. 谁签发和撤销physical_handle_ref，Handle是否不可被当作公开URL？
2. 物理字节、备份、归档、缓存和副本的范围如何枚举？
3. Digest的算法、字节范围和规范化如何固定？
4. 完整性验证失败、未知或不可验证时如何表达？
5. 主存删除、备份轮换、密钥销毁和Legal Hold分别如何留证？
6. M08能否在没有M02回执时把对象标记为物理删除完成？
7. 哪些EVD/CHK引用只有在其内容确实由M02托管时才触发M02审议？

## 4. 必须提交的证据

1. RAW-004与RAW-008—011的Handle/Digest算法/范围/完整性证据；
2. RAW-012/013/019/020的Custody、Encryption、Deletion和Receipt Schema；
3. Snapshot捕获的RawAsset字节、摘要、封装范围和副本清单；
4. 物理访问PEP、密钥轮换/撤销、备份恢复和副本删除能力；
5. 物理删除/密钥销毁回执的签发者、覆盖范围、版本和可独立验证方法；
6. M08逻辑删除与M02物理处置状态的对账样例。

## 5. 必须记录的边界与反例

- 说明该模块实际能决定的事项，以及明确不能决定的事项；
- 以合成数据给出允许、拒绝、Unknown、部分失败和撤销案例；
- 对外部能力声明与实际运行事实进行区分；
- 对历史版本、当前版本和派生副本分别给出证据；
- 不得将“系统暂时支持”写成“Owner已批准”。

## 6. 输出要求

提交材料至少包括：逐字段/逐议题意见、原始证据引用、事实假设、建议处置、反方风险、权限边界、会审需求、未决问题、条件和复审触发器。若无权批准，明确标记为专业意见或会审意见，不写OwnerApproved。

## 7. 当前结论

本包为审议执行材料；尚无真实Owner反馈、正式会议结论或批准证据。未审议字段保持Pending；不产生Profile Delta，不授权工程实现。