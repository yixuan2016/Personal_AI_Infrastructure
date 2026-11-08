# 572｜RawAsset字段逐项审查包：物理Handle、完整性与保管

**状态：** Field-Level Design Review Candidate；Owner Feedback 20/20 Pending；No Approval

## 1. 对象边界

RawAsset表达原始数字资产的逻辑身份、类型、来源、物理Handle引用和保管状态。M08负责逻辑资产记录，M02负责物理字节、Opaque Handle、加密、备份和物理删除；两者不得互相代替。D-05/D-06/D-07是主决策。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| RAW-001 | `raw_asset_id` | RawAsset稳定身份是否与物理对象/存储Key分离；迁移是否保持逻辑ID。 | D-05/D-07 |
| RAW-002 | `raw_asset_kind` | raw_asset_kind受控类型如何覆盖文件、媒体、附件、流和复合封装。 | D-05/D-07 |
| RAW-003 | `source_snapshot_refs` | source_snapshot_refs支持一对多/多对多时如何表达主来源及完整性。 | D-05/D-07 |
| RAW-004 | `physical_handle_ref` | physical_handle_ref是否为Opaque Handle；避免暴露Bucket、路径、凭据或可绕过授权的URL。 | D-05 |
| RAW-005 | `byte_size` | byte_size按原始字节还是封装后字节计算；分段/流式资产如何定义。 | D-05 |
| RAW-006 | `media_type_declared` | media_type_declared来源、可信度和缺失值如何记录；不能当作实际格式证明。 | D-05 |
| RAW-007 | `media_type_detected` | media_type_detected由何种检测器产生、版本和置信依据；与声明不一致如何处理。 | D-05 |
| RAW-008 | `byte_digest` | byte_digest的算法、字节范围和规范化规则是否明确；是否支持多摘要。 | D-06 |
| RAW-009 | `digest_algorithm` | digest_algorithm是否允许算法迁移和多算法并存；弱算法何时退役。 | D-06 |
| RAW-010 | `digest_scope` | digest_scope能否准确区分原始字节、封装字节、分块和逻辑内容。 | D-06 |
| RAW-011 | `integrity_state` | integrity_state区分未验证、已验证、失效、未知和不可验证；不等于来源可信。 | D-06 |
| RAW-012 | `custody_state` | custody_state由谁维护；逻辑保管、物理持有、备份和外部托管是否分离。 | D-07 |
| RAW-013 | `encryption_profile_ref` | encryption_profile_ref指向策略还是实际密钥实例；密钥轮换和销毁如何留证。 | D-07 |
| RAW-014 | `classification_ref` | classification_ref是否与源Snapshot分类保持可解释的继承/提升关系。 | D-04 |
| RAW-015 | `retention_profile_ref` | retention_profile_ref绑定哪一版本；Legal Hold、例外和保留起点如何确定。 | D-04 |
| RAW-016 | `created_by_ref` | created_by_ref区分导入者、采集服务和实际生成者。 | D-05/D-07 |
| RAW-017 | `created_at` | created_at与acquired_at、captured_at的差异和时钟可信度。 | D-05/D-07 |
| RAW-018 | `object_version` | object_version是否仅表示元数据修订；不能被误用为内容版本。 | D-05/D-07 |
| RAW-019 | `deletion_state_ref` | deletion_state_ref是否能表达逻辑隐藏、物理删除、备份到期和阻断。 | D-05/D-07 |
| RAW-020 | `custody_receipt_refs` | custody_receipt_refs由哪个物理权威签发；回执覆盖范围、时间和验证方式。 | D-07 |

## 3. 对象内一致性约束

- raw_asset_id不等于physical_handle_ref；存储迁移不得改变逻辑身份。
- byte_size、media_type_declared、media_type_detected分别表达大小、声明格式和检测事实。
- byte_digest必须与digest_algorithm和digest_scope一起解释；integrity_state只表达字节完整性验证。
- custody_state、encryption_profile_ref、retention_profile_ref和deletion_state_ref不可合并为一个存储状态。
- custody_receipt_refs必须来自有权物理保管方，且回执覆盖对象/副本/时间/操作范围。
- classification和Retention不能因RawAsset复制或重新封装而降级。

## 4. 删除与物理证明

M08的逻辑删除标记不等于M02物理字节删除。备份、复制、归档、密钥销毁、Provider副本和Legal Hold均需分别追踪；未取得物理回执时只能报告逻辑状态或待确认状态。

## 5. 当前结论

20/20字段完成设计审查问题登记；Owner状态20/20 Pending；没有M02物理删除批准或RawAsset Profile Delta获批。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 20/20 与Stage35原始台账一致 |
| 语义审查问题 | 20/20 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。