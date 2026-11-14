# CHANGELOG

## 2026-11-10｜V1.2—V1.7 研究归档
- 归档协议契约、Ontology、Environment Runtime、生态自治、世界模型/数字孪生和生态级 RSI 研究资料。
- 纳入 Markdown、CSV、JSON、YAML、SVG、威胁矩阵、验收矩阵与研究证据。
- 修复 V1.3—V1.7 主报告的 SVG 图片引用，并新增归档审查和二进制资产状态记录。

## 2026-11-10｜V1.8 跨生态联邦与 F0 治理
- 新增跨生态联邦拓扑、本地主权职责边界、多生态协同与跨域策略兼容设计。
- 新增身份、能力声明、信任向量、改进提案、证据包和本地采用回执契约。
- 新增 F0 治理章程、不可委托权限清单、成员生命周期、密钥与跨域授权模型。
- 新增 R0-R4 风险/审批矩阵、RACI、决策登记册、12 项 F0 Gate。
- 新增成员声明与 DataUseGrant Schema；验证矩阵 23 项、威胁矩阵 16 项，全部 NotRun。
- 新增 3 张 SVG 架构源图和 V1.8 二进制资产状态清单。
- V1.8 为架构研究和候选契约，不代表工程实现或双生态互操作验收。

## 2026-11-14｜V1.9-A 痕迹协作实证与架构增量（Candidate）
- 新增近期共享记忆、Substrate-centric、Waggle 局部规则、SwarmWorld 持久工件、协作收益边界和环境/意图消息分离研究。
- 新增 V1.9 主报告、7 项研究证据登记、22 项 Stigmergy 合成实验与验收设计、8 项基础候选 ADR、12 项基础威胁与治理边界。
- 补充共享状态通信通道、有界发现、来源感知排序、持久工件谱系、局部反应、选择性 A2A 和单 Agent 基线要求。

## 2026-11-14｜V1.9-B 跨生态能力发现与联邦目录（Candidate）
- 新增本地权威能力目录与联邦摘要目录双层架构，明确发现视图可最终一致、执行前授权必须由目标生态本地 PDP/PEP 决定。
- 新增能力广告与能力解析候选 JSON Schema、20 项 F1 验收矩阵及跨生态能力发现架构备忘录。
- 新增 Observation Runtime 设计：事件订阅、状态唤醒、游标续读、周期对账、命名空间隔离和审计。
- 补充 A2A、MCP、CloudEvents、Ontology、SPIFFE 的职责边界，以及 MACP Internet-Draft 的证据等级与本地自治适配原则。
- 新增 7680×4320 SVG 架构源图和独立证据登记；威胁矩阵扩展至 18 项，ADR 扩展至 10 项。
- 新增能力发现候选契约静态审查，登记 10 项 Schema/语义/授权缺口；两份 JSON 文件仅完成语法解析检查，未完成完整 Schema、密码学或互操作验证。
- 合成实验与验收共 42 项全部 NOT_RUN；10 项 ADR 全部 Candidate；F0 12 项 Gate 仍未通过；productionAllowed=false。

## 2026-11-14｜V1.9 能力发现契约静态审查与候选修复
- 对 CapabilityAdvertisement、CapabilityResolution 和生命周期事件 Schema 完成 JSON 语法静态回读。
- 新增机器可读 notAuthorization=true、VERIFIED 验证上下文、NAMED_DOMAINS 可见域约束、成本单位和证据等级约束。
- 增加候选资格与 attestation/revocation/freshness 状态组合约束；增加每个候选的来源水位、撤销 Epoch 和观察有效期。
- 增加分页请求字段和能力生命周期 CloudEvents 候选 Schema。
- 静态审查 10 项缺口：7 项已形成候选修复、1 项部分修复、2 项仍开放；签名密码学、时间单调性、完整 Draft 2020-12 Validator 与互操作测试仍未执行。
- F1 验收扩展至 30 项，V1.9 合成实验与验收共 52 项全部 NOT_RUN；productionAllowed=false。

- F1 能力发现/契约矩阵增加冲突状态优先级测试；INELIGIBLE 优先于 HOLD，F1 测试增至 31 项，V1.9 验收总数增至 53 项，全部 NOT_RUN。


## 2026-11-14｜V1.9-C WP-020 跨生态信任协议与能力授权链（Candidate）
- 新增 WP-020 架构决策备忘录、研究证据登记、静态审查与 10 项未决事项。
- 新增 Peer Trust Binding、Owner Delegation Grant、Capability Owner Attestation 三份候选 JSON Schema。
- 新增 27 项跨生态信任、Owner 签名、委托衰减、Token Exchange、DPoP、撤销与审计验收设计，全部 NOT_RUN。
- 新增 7680×4320 SVG 信任与授权链架构源图。
- 新增 ADR-111—ADR-116；威胁矩阵扩展至 26 项；总候选 ADR 为 16 项。
- 默认双边显式信任、关闭传递信任；SPIFFE/OIDF 为可选适配；目标域本地 Authorization Server/PDP 保留最终授权权威。
- 六份候选 Schema 仅完成 JSON 语法解析检查；未完成完整 Draft 2020-12 Validator、密码学、父子委托语义和协议互操作测试。
- V1.9 合成实验与验收共 80 项全部 NOT_RUN；F0 未通过；productionAllowed=false；Runner 未启用。

- Peer Trust Binding 进一步要求 Trust Anchor 与 Trust Domain 显式绑定、双方对同一 agreementDigest 签署接受收据；R4 不进入 Agent 委托；WP-020 验收增至 27 项，V1.9 总验收增至 80 项，全部 NOT_RUN。
