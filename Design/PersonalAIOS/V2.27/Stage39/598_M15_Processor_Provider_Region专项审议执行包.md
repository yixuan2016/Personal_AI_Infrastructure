# 598｜M15 Processor/Provider/Region专项审议执行包

**状态：** Specialist Review Package Candidate；Actual Owner Response Pending；No Approval Recorded  
**候选角色：** M15 Processor/Provider Authority（候选）

## 1. 审议目标与权限边界

确认M15对Processor/Provider能力、版本、实际调用、Region、Operation ID、幂等、对账、资源用量和外部副作用的事实权威。M15提供事实和集成能力，不授予个人数据外发许可；处理授权仍由M18及适用的Personal Owner决定。

## 2. 关联字段与审议范围

本包中的字段是需要该权威角色参与的审议范围，不表示该角色对所有字段拥有单独批准权。字段的语义仍由M06 TDA/SA候选审议，实例写入和生命周期事实由M08 IA候选审议；最终权限以真实授权证据为准。

| Field ID | 字段 | 需要回答的问题 | 原始核心决策 | 风险 |
|---|---|---|---|---|
| EXT-005 | processor_kind | processor_kind是否为受控类别；本地/外部/人工混合流水线如何表达。 | — | Medium |
| EXT-006 | processor_ref | processor_ref指向逻辑处理器、部署还是服务实例；身份层级必须明确。 | D-09 | High |
| EXT-007 | processor_version_ref | processor_version_ref如何固定模型/服务版本；静默升级和灰度路由如何留证。 | D-09 | High |
| EXT-008 | configuration_digest | configuration_digest覆盖哪些参数；秘密、令牌和个人数据不得进入普通摘要明文。 | D-09 | High |
| EXT-010 | actor_or_service_ref | actor_or_service_ref区分发起主体、执行主体和Provider；委托关系如何追踪。 | D-09 | Medium |
| EXT-012 | provider_profile_ref | provider_profile_ref固定合同/能力/子处理商条款版本；Profile更新不得改写历史。 | D-09 | High |
| EXT-013 | provider_region_ref | provider_region_ref区分请求地区、计算地区、存储/日志/人工访问地区。 | D-09 | High |
| EXT-014 | started_at | started_at由本地还是Provider记录；时钟偏差和重试尝试如何处理。 | — | Medium |
| EXT-015 | completed_at | completed_at表示外部执行结束还是本地落库完成；未知结果不得伪造完成时间。 | — | Medium |
| EXT-016 | run_state | run_state是否把调度、外部执行、结果持久化和业务发布分离。 | D-10 | High |
| EXT-019 | error_class | error_class是否区分可重试、不可重试、未知结果和部分副作用。 | D-10 | Medium |
| EXT-020 | retry_of_ref | retry_of_ref表示直接前序尝试还是逻辑重试链；循环和分叉如何处理。 | D-10 | High |
| EXT-021 | idempotency_scope_ref | idempotency_scope_ref绑定任务、输入版本、配置和Provider；键有效期如何管理。 | D-10 | High |
| EXT-022 | correlation_id | correlation_id跨模块与Provider串联是否稳定且避免碰撞/敏感信息泄露。 | D-10 | Medium |
| EXT-023 | resource_usage_summary | resource_usage_summary区分单次尝试、逻辑任务和Provider账单；估算与实耗分离。 | — | Medium |

## 3. 必须回答的问题

1. processor_ref指向逻辑处理器、部署还是服务实例？
2. 服务端静默升级或动态路由如何记录？
3. 配置Region和实际计算/存储/日志Region如何区分？
4. Provider子处理商、人工访问、日志、缓存和训练再利用如何披露？
5. Provider已接收请求但回执丢失时如何查证是否执行？
6. 哪些Provider支持幂等，幂等键的作用域和有效期是什么？
7. M15如何证明外部处理事实但不代替M18批准Purpose/Consent？

## 4. 必须提交的证据

1. EXT-005—008、EXT-010、EXT-012—016、EXT-019—023相关Processor/Provider Profile及版本；
2. 实际计算、存储、日志、备份、人工访问和子处理商区域证据；
3. Provider合同/DPA、训练再利用、保留、删除和审计条款版本；
4. 调用Operation ID、回执、幂等键作用域、超时和UnknownOutcome对账证据；
5. 部分完成、重复计费、重复输出和补偿操作的合成案例；
6. M18 Policy Decision与M15实际执行事实的关联证据。

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