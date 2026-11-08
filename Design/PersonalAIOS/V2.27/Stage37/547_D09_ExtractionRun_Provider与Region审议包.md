# 547｜D-09 ExtractionRun Provider/Region：Owner审议包

**状态：** Decision Dossier Candidate；Owner Feedback Pending；No Approval Recorded

## 1. 议题定义

ExtractionRun可能由本地处理器、云端模型、第三方服务或组合式流水线执行。配置中的Provider和Region不一定等于实际执行的Provider和处理区域；服务端日志、人工审查、子处理商、临时缓存和模型训练再利用也可能构成额外处理。必须区分能力声明、调用配置、实际运行事实和Policy授权。

## 2. 关联字段与权威边界

- EXT-006 processor_ref
- EXT-007 processor_version_ref
- EXT-008 configuration_digest
- EXT-009 purpose_ref
- EXT-010 actor_or_service_ref
- EXT-011 policy_decision_ref
- EXT-012 provider_profile_ref
- EXT-013 provider_region_ref

主决定权威候选：M15负责Processor/Provider能力与集成事实；M18负责Purpose、Policy、Consent和外部处理授权；M08记录ExtractionRun实例事实；Security/Privacy/Legal独立审查。

## 3. 必须回答的问题

1. processor_ref指向逻辑处理器、具体模型部署还是实际服务实例？
2. processor_version_ref如何固定模型/服务版本，服务端静默升级如何记录？
3. configuration_digest覆盖哪些配置，是否排除密钥和敏感参数？
4. provider_profile_ref是合同能力配置、服务档案还是一次调用的Provider身份？
5. provider_region_ref记录配置地区、实际计算地区、数据存储地区还是全部？是否需分开？
6. Provider是否使用子处理商、人工审查、服务日志、缓存或数据训练？
7. EXT-011 Policy Decision是否绑定当前Actor、输入资源、Purpose、Provider和Region？
8. 实际Region未知、Provider条款变化或路由故障时，是否阻断处理或进入受控降级？

## 4. 候选方案（不构成推荐或批准）

- A：运行记录分别固定Processor版本、Provider Profile版本和实际Region证据；M18逐次授权，M15提供能力事实。
- B：使用版本化Provider Execution Profile封装服务商、区域、子处理商、数据使用和删除条款，运行记录引用该Profile并保存实际执行回执。
- C：仅记录Provider与Region名称；字段简单，但无法证明实际处理地点和条款状态，不足以支持高敏数据外发审查。

## 5. 必须提供的证据

- M15 Processor Registry、Provider Profile和实际调用路由说明；
- Provider合同、DPA/数据处理条款、子处理商清单及变更通知机制；
- 计算、存储、日志、备份和人工访问的实际地区说明；
- 训练再利用、保留期限、删除、导出和审计条款；
- M18 Policy输入输出和授权决策记录；
- Security/Privacy/Legal对具体数据类型、用途和地区的审查意见。

## 6. 下游影响与测试

影响ExtractionRun、KnowledgeAsset派生、Chunk、Embedding、Context、日志、Provider缓存和删除流程。不得以“模型服务可用”推断数据处理已获授权；不得以Region配置值冒充实际Region证明。

测试覆盖Provider Profile过期、处理区域未知、服务端版本漂移、子处理商变化、Purpose不匹配、Policy拒绝、条款禁止训练但服务配置不明、Provider删除回执缺失和跨区域故障切换。

## 7. 阻断条件

Provider身份或合同条款不明；实际处理区域不可证明；Purpose/Policy未通过；训练/人工审查/日志用途不清；子处理商和删除责任不明；把配置值当作运行事实。

## 8. 当前状态

本文件仅形成D-09审议准备包。没有真实Owner意见或专业审查结论；EXT-006至EXT-013继续保持Pending。