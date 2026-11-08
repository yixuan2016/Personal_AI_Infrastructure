# 594｜M06 TDA/SA语义审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M06 Type Definition Authority / Semantic Authority（候选）

## 1. 审议目标与权限边界

核验M06是否对六个OT及SourceSnapshot子记录的类型定义、字段语义、关系、基数、枚举、状态机和Evidence语义具有明确权威。M06对语义作决定，不因此获得实例写入、物理保管、Provider事实或Policy裁决权。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围，不表示该角色对所有字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| SRC-001 | source_id | Source稳定身份是否全局唯一；ID是否与外部来源ID分离，是否允许迁移而不改变本地身份。 | D-01 | High |
| SRC-002 | source_kind | source_kind是否为受控分类；扩展枚举是否有兼容和未知值处理规则。 | — | Medium |
| SRC-003 | source_authority_ref | source_authority_ref指向谁；权威范围、有效期、授权与冲突仲裁是否明确。 | D-01 | High |
| SRC-004 | origin_identity_ref | origin_identity_ref的命名空间、外部ID变更、碰撞和不可用场景如何表达。 | D-01 | High |
| SRC-005 | locator_refs | locator_refs是否支持多值、历史、优先级和失效；凭据是否与定位信息隔离。 | D-02 | Medium |
| SRC-006 | availability_state | availability_state表达当前可访问性还是来源自身可用性；状态由谁观测、何时过期。 | — | Medium |
| SRC-007 | lifecycle_state | lifecycle_state是否与availability_state分离；归档、撤回、删除和停用是否可区分。 | — | Medium |
| SRC-008 | source_rights_refs | source_rights_refs如何表达多重权利、地域/用途限制、有效期和撤回。 | D-04 | Medium |
| SRC-009 | data_subject_refs | data_subject_refs是否最小化；多主体、未知主体和身份纠错如何表达。 | — | Medium |
| SRC-010 | classification_ref | classification_ref是否由权威分类体系提供；来源分类变化如何传播到派生物。 | — | Medium |
| SRC-011 | created_by_ref | created_by_ref表示创建者还是实际采集Actor；服务账号和代理行为如何标记。 | — | Medium |
| SRC-012 | created_at | created_at使用哪个时钟、时区和精度；是否代表业务发生时间还是记录创建时间。 | — | Medium |
| SRC-013 | updated_at | updated_at由哪些变更触发；是否避免被无关读取或派生过程刷新。 | — | Medium |
| SRC-014 | object_version | object_version如何递增、并发冲突如何处理；与Snapshot Sequence是否分离。 | — | Medium |
| SRC-015 | supersedes_source_ref | supersedes_source_ref表达替代、合并还是纠错；循环引用和多对一如何处理。 | — | Medium |
| SNP-001 | snapshot_id | snapshot_id是否不可变且唯一；内容相同的重复采集如何表达。 | D-03 | Medium |
| SNP-002 | source_ref | source_ref是否固定Source身份；来源后续更名或合并是否影响历史Snapshot。 | D-03 | Medium |
| SNP-003 | snapshot_sequence | snapshot_sequence作用域、递增规则、并发采集和缺号语义是否明确。 | D-03 | Medium |
| SNP-004 | capture_state | capture_state区分计划、进行中、部分、成功、失败和校验失败；失败快照能否被消费。 | D-03 | Medium |
| SNP-005 | captured_at | captured_at记录采集动作发生时间；时间来源、精度和可信度如何表达。 | D-03 | Medium |
| SNP-006 | acquired_at | acquired_at记录内容获取时间还是外部时间；与captured_at为何不同。 | D-03 | Medium |
| SNP-007 | capture_method | capture_method是否受控；人工、Connector、API、文件导入和批量同步如何区分。 | D-03 | Medium |
| SNP-008 | captured_locator_ref | captured_locator_ref是否固定采集时Locator；失效或凭据过期不应改写历史。 | D-02/D-03 | Medium |
| SNP-009 | external_version_token | external_version_token由外部系统提供还是本地推断；不稳定Token如何标注。 | D-03 | Medium |
| SNP-010 | raw_asset_refs | raw_asset_refs是否只引用已登记RawAsset；部分捕获和多文件组成如何表达。 | D-03 | Medium |
| SNP-011 | captured_bytes_digest | captured_bytes_digest摘要的字节范围、规范化、算法和校验主体是否明确。 | D-03 | Medium |
| SNP-012 | digest_scope | digest_scope是否版本化、可枚举；压缩、封装、分段和多文件场景如何定义。 | D-03 | Medium |
| SNP-013 | rights_snapshot_ref | rights_snapshot_ref是否保存采集时权利状态及来源；不能被当前权利覆盖。 | D-03/D-04 | High |
| SNP-014 | purpose_ref | purpose_ref是否对应本次采集目的；目的变更是否触发重新授权。 | D-03/D-04 | High |
| SNP-015 | policy_decision_ref | policy_decision_ref是否绑定Actor、Source、Action、Purpose和采集时Policy版本。 | D-03/D-04 | High |
| SNP-016 | applicable_basis_refs | applicable_basis_refs区分Consent、合同、法定义务等依据；多依据冲突如何处理。 | D-03/D-04 | High |
| SNP-017 | data_subject_refs | data_subject_refs是否继承并可修正；主体不明时是否限制后续处理。 | D-03 | Medium |
| SNP-018 | classification_ref | classification_ref是否记录采集时分类；分类升级如何触发派生数据重评。 | D-03 | Medium |
| SNP-019 | retention_profile_ref | retention_profile_ref是否固定采集时适用的保留规则版本和触发起点。 | D-03 | Medium |
| SNP-020 | capture_actor_ref | capture_actor_ref记录实际执行人或服务；委托、代理和自动化身份如何审计。 | D-03 | Medium |
| SNP-021 | recorded_at | recorded_at与captured_at分离的目的、时钟来源和不可回填规则。 | D-03 | Medium |
| SNP-022 | snapshot_manifest_digest | snapshot_manifest_digest覆盖哪些Snapshot组成项；清单本身如何防篡改和验证。 | D-03 | Medium |
| RAW-001 | raw_asset_id | RawAsset稳定身份是否与物理对象/存储Key分离；迁移是否保持逻辑ID。 | — | Medium |
| RAW-002 | raw_asset_kind | raw_asset_kind受控类型如何覆盖文件、媒体、附件、流和复合封装。 | — | Medium |
| RAW-003 | source_snapshot_refs | source_snapshot_refs支持一对多/多对多时如何表达主来源及完整性。 | — | Medium |
| RAW-004 | physical_handle_ref | physical_handle_ref是否为Opaque Handle；避免暴露Bucket、路径、凭据或可绕过授权的URL。 | D-05 | High |
| RAW-005 | byte_size | byte_size按原始字节还是封装后字节计算；分段/流式资产如何定义。 | — | Medium |
| RAW-006 | media_type_declared | media_type_declared来源、可信度和缺失值如何记录；不能当作实际格式证明。 | — | Medium |
| RAW-007 | media_type_detected | media_type_detected由何种检测器产生、版本和置信依据；与声明不一致如何处理。 | — | Medium |
| RAW-008 | byte_digest | byte_digest的算法、字节范围和规范化规则是否明确；是否支持多摘要。 | D-06 | High |
| RAW-009 | digest_algorithm | digest_algorithm是否允许算法迁移和多算法并存；弱算法何时退役。 | D-06 | High |
| RAW-010 | digest_scope | digest_scope能否准确区分原始字节、封装字节、分块和逻辑内容。 | D-06 | Medium |
| RAW-011 | integrity_state | integrity_state区分未验证、已验证、失效、未知和不可验证；不等于来源可信。 | D-06 | Medium |
| RAW-012 | custody_state | custody_state由谁维护；逻辑保管、物理持有、备份和外部托管是否分离。 | D-07 | Medium |
| RAW-013 | encryption_profile_ref | encryption_profile_ref指向策略还是实际密钥实例；密钥轮换和销毁如何留证。 | D-07 | Medium |
| RAW-014 | classification_ref | classification_ref是否与源Snapshot分类保持可解释的继承/提升关系。 | — | Medium |
| RAW-015 | retention_profile_ref | retention_profile_ref绑定哪一版本；Legal Hold、例外和保留起点如何确定。 | — | Medium |
| RAW-016 | created_by_ref | created_by_ref区分导入者、采集服务和实际生成者。 | — | Medium |
| RAW-017 | created_at | created_at与acquired_at、captured_at的差异和时钟可信度。 | — | Medium |
| RAW-018 | object_version | object_version是否仅表示元数据修订；不能被误用为内容版本。 | — | Medium |
| RAW-019 | deletion_state_ref | deletion_state_ref是否能表达逻辑隐藏、物理删除、备份到期和阻断。 | — | Medium |
| RAW-020 | custody_receipt_refs | custody_receipt_refs由哪个物理权威签发；回执覆盖范围、时间和验证方式。 | D-07 | Medium |
| KAS-001 | knowledge_asset_id | KnowledgeAsset逻辑身份是否稳定；与内容版本、展示名称和外部ID分离。 | — | Medium |
| KAS-002 | asset_kind | asset_kind的分类边界、扩展规则和复合资产语义。 | — | Medium |
| KAS-003 | display_name | display_name是否仅为展示元数据；改名不应改变身份或版本。 | — | Medium |
| KAS-004 | source_snapshot_refs | source_snapshot_refs是否固定原始来源版本；合并资产如何保留多来源血缘。 | — | Medium |
| KAS-005 | raw_asset_refs | raw_asset_refs指向逻辑RawAsset还是物理Handle；删除和保留责任如何继承。 | — | Medium |
| KAS-006 | current_asset_version_ref | current_asset_version_ref是可变指针；并发更新、回滚和历史引用如何保证。 | D-08 | High |
| KAS-007 | asset_versions | asset_versions是否引用不可变内容版本；版本元数据、摘要和supersedes关系是否齐全。 | D-08 | High |
| KAS-008 | lifecycle_state | lifecycle_state与Current Version状态、Retention和Deletion状态是否正交。 | — | Medium |
| KAS-009 | classification_ref | classification_ref如何从来源和处理结果继承；冲突时采用何种提升规则。 | — | Medium |
| KAS-010 | retention_profile_ref | retention_profile_ref适用范围是逻辑资产还是每个版本；更严格规则如何传播。 | — | Medium |
| KAS-011 | created_by_ref | created_by_ref记录资产创建者还是内容贡献者；多方贡献如何表达。 | — | Medium |
| KAS-012 | created_at | created_at是逻辑资产创建时间还是首个内容版本时间。 | — | Medium |
| KAS-013 | updated_at | updated_at是否只随对象元数据变化；内容更新应由Version表达。 | — | Medium |
| KAS-014 | object_version | object_version与Content Version分离；并发修订和审计如何实现。 | — | Medium |
| KAS-015 | processing_purpose_refs | processing_purpose_refs如何保留各派生用途的来源链；是否允许用途扩展。 | — | Medium |
| KAS-016 | deletion_dependency_refs | deletion_dependency_refs是否枚举Chunk、Projection、缓存、Provider、导出、日志和备份。 | D-08 | Medium |
| EXT-001 | extraction_run_id | extraction_run_id是否为单次尝试ID；逻辑任务ID和Provider Operation ID是否另设。 | — | Medium |
| EXT-002 | run_kind | run_kind如何区分采集、抽取、转换、摘要、嵌入等处理意图。 | — | Medium |
| EXT-003 | input_refs | input_refs是否固定对象及版本；多输入顺序和缺失输入如何表达。 | — | Medium |
| EXT-004 | input_digest_refs | input_digest_refs是否覆盖全部输入及规范化Scope；防止输入漂移。 | — | Medium |
| EXT-005 | processor_kind | processor_kind是否为受控类别；本地/外部/人工混合流水线如何表达。 | — | Medium |
| EXT-006 | processor_ref | processor_ref指向逻辑处理器、部署还是服务实例；身份层级必须明确。 | D-09 | High |
| EXT-007 | processor_version_ref | processor_version_ref如何固定模型/服务版本；静默升级和灰度路由如何留证。 | D-09 | High |
| EXT-008 | configuration_digest | configuration_digest覆盖哪些参数；秘密、令牌和个人数据不得进入普通摘要明文。 | D-09 | High |
| EXT-009 | purpose_ref | purpose_ref绑定本次运行的具体目的；不能继承成永久通用授权。 | D-09 | Medium |
| EXT-010 | actor_or_service_ref | actor_or_service_ref区分发起主体、执行主体和Provider；委托关系如何追踪。 | D-09 | Medium |
| EXT-011 | policy_decision_ref | policy_decision_ref是否绑定输入、Action、Purpose、Provider、Region和Policy版本。 | D-09 | High |
| EXT-012 | provider_profile_ref | provider_profile_ref固定合同/能力/子处理商条款版本；Profile更新不得改写历史。 | D-09 | High |
| EXT-013 | provider_region_ref | provider_region_ref区分请求地区、计算地区、存储/日志/人工访问地区。 | D-09 | High |
| EXT-014 | started_at | started_at由本地还是Provider记录；时钟偏差和重试尝试如何处理。 | — | Medium |
| EXT-015 | completed_at | completed_at表示外部执行结束还是本地落库完成；未知结果不得伪造完成时间。 | — | Medium |
| EXT-016 | run_state | run_state是否把调度、外部执行、结果持久化和业务发布分离。 | D-10 | High |
| EXT-017 | output_refs | output_refs是否仅包含已登记且可验证的输出；部分输出如何隔离。 | — | Medium |
| EXT-018 | output_manifest_digest | output_manifest_digest覆盖哪些输出及顺序；如何证明输出集合完整。 | — | Medium |
| EXT-019 | error_class | error_class是否区分可重试、不可重试、未知结果和部分副作用。 | D-10 | Medium |
| EXT-020 | retry_of_ref | retry_of_ref表示直接前序尝试还是逻辑重试链；循环和分叉如何处理。 | D-10 | High |
| EXT-021 | idempotency_scope_ref | idempotency_scope_ref绑定任务、输入版本、配置和Provider；键有效期如何管理。 | D-10 | High |
| EXT-022 | correlation_id | correlation_id跨模块与Provider串联是否稳定且避免碰撞/敏感信息泄露。 | D-10 | Medium |
| EXT-023 | resource_usage_summary | resource_usage_summary区分单次尝试、逻辑任务和Provider账单；估算与实耗分离。 | — | Medium |
| EXT-024 | retention_profile_ref | retention_profile_ref覆盖输入副本、输出、日志、临时文件和Provider缓存的哪一范围。 | — | Medium |
| EXT-025 | object_version | object_version只表示Run记录修订；不能代替状态迁移历史。 | — | Medium |
| CHK-001 | chunk_id | chunk_id是否全局唯一且不可复用；重新分块产生新身份还是更新旧对象。 | — | Medium |
| CHK-002 | knowledge_asset_ref | knowledge_asset_ref是否指向稳定资产身份；读取时是否必须同时固定版本。 | — | Medium |
| CHK-003 | asset_version_ref | asset_version_ref必须绑定Chunk实际来源内容版本，禁止指向动态Current。 | — | Medium |
| CHK-004 | extraction_run_ref | extraction_run_ref是否指向已核验终态Run；UnknownOutcome输出不得发布。 | — | Medium |
| CHK-005 | chunk_set_id | chunk_set_id集合身份作用域、资产绑定和重建语义。 | D-11 | High |
| CHK-006 | chunk_set_version | chunk_set_version是否不可变；与Asset Content Version和Strategy Version关系。 | D-11 | High |
| CHK-007 | chunk_sequence | chunk_sequence是否从固定起点连续；重复、缺口和局部重排如何处理。 | D-11 | High |
| CHK-008 | content_ref | content_ref引用内容存储还是文本片段；权限与物理Handle如何隔离。 | D-11 | Medium |
| CHK-009 | text_digest | text_digest算法、规范化和Scope是否明确；摘要匹配不证明语义相同。 | D-11 | Medium |
| CHK-010 | locator_in_parent | locator_in_parent如何定位父内容版本；偏移单位和版本上下文是否明确。 | D-11 | Medium |
| CHK-011 | token_range | token_range依赖哪个Tokenizer及版本；跨模型Token范围是否可复现。 | D-11 | Medium |
| CHK-012 | character_range | character_range的字符编码、索引单位和Unicode规范化规则。 | D-11 | Medium |
| CHK-013 | chunk_strategy_ref | chunk_strategy_ref固定分块策略及版本；策略变化如何产生新Set。 | D-11 | Medium |
| CHK-014 | language_refs | language_refs支持多语言、混合语言和检测不确定性。 | D-11 | Medium |
| CHK-015 | classification_ref | classification_ref如何继承源资产分类；分块不得降低敏感级别。 | D-11 | High |
| CHK-016 | purpose_lineage_refs | purpose_lineage_refs保留处理目的和允许用途；检索用途是否重新授权。 | D-11 | High |
| CHK-017 | projection_state | projection_state区分生成、可见、过期、撤销、移除；不能代表权限批准。 | D-11 | High |
| CHK-018 | supersedes_chunk_ref | supersedes_chunk_ref表达替代/修订而非覆盖；跨Set引用是否允许。 | — | Medium |
| CHK-019 | created_at | created_at记录Chunk生成时间而非父内容时间。 | — | Medium |
| CHK-020 | retention_profile_ref | retention_profile_ref是否继承更严格规则；Chunk保留不能超过源依据。 | — | Medium |
| CHK-021 | object_version | object_version与Chunk内容版本/ChunkSet版本分离。 | — | Medium |
| CHK-022 | deletion_state_ref | deletion_state_ref覆盖索引、向量、缓存、Context和外部Projection清除状态。 | D-11 | Medium |
| EVD-001 | evidence_id | evidence_id稳定且不可复用；撤回后是否保留审计身份。 | — | Medium |
| EVD-002 | evidence_kind | evidence_kind受控分类能否区分原始材料、Receipt、摘录、观察记录和外部证明。 | — | Medium |
| EVD-003 | evidence_target_ref | evidence_target_ref采用类型化目标；仅允许Registry批准的对象和子记录。 | D-12 | High |
| EVD-004 | target_version_ref | target_version_ref是否固定目标版本；动态目标如何保存核验时解析快照。 | D-12 | High |
| EVD-005 | locator_schema_ref | locator_schema_ref是否版本化；页码、段落、表格、消息和媒体坐标如何统一。 | D-12 | High |
| EVD-006 | locator_payload | locator_payload只保存定位坐标；不得包含Token、Cookie、签名URL秘密或绕过授权凭据。 | D-12 | High |
| EVD-007 | target_content_digest | target_content_digest摘要哪个目标版本及内容范围；算法与Scope必须明确。 | D-06/D-12 | High |
| EVD-008 | locator_fragment_digest | locator_fragment_digest摘要哪一片段；片段规范化和定位漂移如何处理。 | D-06/D-12 | High |
| EVD-009 | excerpt_ref | excerpt_ref指向可控摘录副本；访问权限、来源版本和保留规则如何继承。 | D-12 | High |
| EVD-010 | excerpt_digest | excerpt_digest覆盖摘录原始还是规范化文本；不能替代Target Digest。 | D-12 | High |
| EVD-011 | integrity_state | integrity_state只表达技术完整性/可验证性；不得映射为来源可信或Assertion Verified。 | D-12 | High |
| EVD-012 | lifecycle_state | lifecycle_state区分有效、过期、撤回、受限和删除；与integrity_state分离。 | — | Medium |
| EVD-013 | created_by_ref | created_by_ref表示Evidence创建主体；不自动赋予Assertion核验权。 | — | Medium |
| EVD-014 | created_at | created_at是Evidence创建时间；来源事件时间应另行定位。 | — | Medium |
| EVD-015 | recorded_at | recorded_at记录进入系统时间；迟到证据和回填时间如何审计。 | — | Medium |
| EVD-016 | classification_ref | classification_ref按目标和摘录中更严格级别继承；不得降级。 | — | Medium |
| EVD-017 | purpose_lineage_refs | purpose_lineage_refs记录证据采集/使用目的；下游主张使用需独立Policy检查。 | — | Medium |
| EVD-018 | retention_profile_ref | retention_profile_ref处理原件、摘录、摘要和审计引用的不同保留要求。 | — | Medium |
| EVD-019 | object_version | object_version表示Evidence元数据修订；Target Version不能随之漂移。 | — | Medium |
| EVD-020 | withdrawal_reason_ref | withdrawal_reason_ref区分来源撤权、目标错误、反证、定位失效和主体撤回。 | D-12 | High |
| EVD-021 | deletion_state_ref | deletion_state_ref区分内容删除、Projection撤除、引用失效和保留例外。 | — | Medium |
| EVD-022 | captured_at | captured_at记录证据材料被捕获的时间；与创建和入库时间分离。 | — | Medium |

## 3. 必须回答的问题

1. 哪些字段语义尚存在多义解释，是否有真实反例？
2. 同名字段是否在不同OT中承担不同语义？
3. 是否把物理Handle、Provider事实或PolicyDecision错误建模为M08 OT字段？
4. 多值引用是否有序、可重复、可为空，Unknown与空集合如何区分？
5. SourceSnapshot和ChunkSet是否清楚保持子记录/集合边界而未被提升为新OT？
6. 哪些字段/关系变更属于普通语义修订，哪些触发ACR/OD？
7. Evidence完整性是否被严格限制在目标/片段范围，避免推导Assertion真实？

## 4. 必须提交的证据

1. 六个OT及Snapshot子记录的现行Type/Profile/Relation Registry原件和版本；
2. 每个字段的类型、基数、必填/可空、Unknown/Absent/Null/Empty/Withheld、可变性和校验约束；
3. 关系的Domain/Range、方向、基数、引用版本、循环限制和删除语义；
4. 状态枚举、合法迁移、并发冲突和历史不可变规则；
5. Evidence Target、Locator、Digest、Integrity与Assertion Verification的语义分界；
6. 字段到Command/Query/Event、Producer/Consumer和负向测试的追踪证据。

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