# G2-03｜ADS / SCO 全量 API 契约映射与六域权威治理报告

**日期：** 2026-11-10  
**基线：** V2.3 ADS API v1 RC0 / SCO API v1 RC0（OpenAPI 3.2.1 候选）  
**状态：** G2-03.1～G2-03.4 映射候选完成；G2-03.5～G2-03.6 待评审与验证  
**范围：** 纯架构研究与契约治理，不包含工程实现代码

## 0. 执行结论

从两份原始机器可读OpenAPI逐项提取并映射：
- ADS：40个operation，38个path。
- SCO：35个operation，35个path。
- 合计：75个operation；ADS 27个OAuth2 scopes，SCO 21个scopes。
- 两份OpenAPI均声明OpenAPI 3.2.1、版本1.0.0-rc0，且均标注尚未实现。
- ADS/SCO都定义RequestEnvelope，但Path引用次数为0；ADS 24个Path、SCO 22个Path引用GenericCommand。
- 两者GenericCommand均要求request_id、correlation_id、issued_at、api_version、schema_version；payload可选，additionalProperties=true。
- 两份OpenAPI没有声明任何HTTP Header参数；但SCO完整接口规范要求写操作带Idempotency-Key、X-Request-ID、X-Correlation-ID，并支持If-Match/ETag。

## 1. 六域统一责任模型

### D1 联邦治理与参与方
接口：ADS Participants / Trust；SCO ListCandidates。  
权威：Participant Owner、TrustDomain Owner、双方 Federation Governance Owner。  
ADS负责登记、目录、信任协商和撤销传播；SCO只消费候选站点。登记不等于法律核验，互认不等于所有资源开放，治理暂停不直接关停本地设备。

### D2 身份、信任与策略授权
接口：ADS Identity / Policy；并作为全部ADS/SCO操作的横切门禁。  
权威：Credential Issuer、Workload Identity Issuer、目标资源/数据Owner PDP、Site PEP。  
ADS可以验证和协调，但最终Permit必须由目标资源Owner的权威PDP签发，本地PEP执行；Indeterminate不等于Permit。

### D3 Ontology与能力生态
接口：ADS Ontology / Capabilities。  
权威：Ontology Governance Committee、Domain Profile Owner、Capability Owner、独立Validator。  
ADS维护共同语义目录和能力发现；领域端负责专业验证、适配和采用。Registered、Verified、Published、Adopted、Available必须分开。

### D4 数据空间与用途治理
接口：ADS DataSpace。  
权威：Data Owner、Data Product Owner、Grant Issuer、Lineage Owner、目标Site PEP。  
ADS负责目录发现、用途合同协商和撤销协调；DataUseGrant由Data Owner授权主体签发；每次数据访问由目标站点重新授权。Discoverable不等于Readable，Readable不等于Trainable。

### D5 任务合同与算力资源
接口：SCO Contracts / Plans / Runs / Resources / Operations。  
权威：合同签署方、Task Owner、Site Task Owner、Compute Resource Owner、Site LCP Lease Authority。  
SCO负责全局计划和跨站点协调；本地LCP执行Prepare/Commit并由本地Lease Authority签发Lease/FencingToken。SCO不得签发本地租约，也不得绕过本地PDP/PEP。

### D6 结果、证据、验收与结算
接口：SCO Results / Acceptance / Settlement / Evidence；ADS VerifyObligations。  
权威：Result Producer、Artifact Owner、Evidence Owner、Independent Acceptance Owner、Metering Owner、Settlement Owner。  
SCO负责关联和编排；结果提交不等于验收，验收不等于结算；Acceptance必须由合同指定的独立验收方签发。

## 2. ADS 40个操作映射

| API分组 | 数量 | 权威边界 |
|---|---:|---|
| Participants | 4 | Participant Registry Owner；暂停仅影响联邦治理状态 |
| Trust | 4 | TrustDomain Owner；双边签署、可撤销 |
| Identity | 5 | Credential/Workload/Attestation Issuer与Verifier |
| Policy | 8 | 目标Resource/Data Owner PDP；本地PEP执行 |
| Ontology | 4 | Core Governance Committee与Domain Profile Owner |
| Capabilities | 6 | Capability Owner + 独立Validator + Domain Adoption |
| DataSpace | 9 | Data Owner/Grant Issuer/Lineage Owner |

逐项方法、路径、Scope、Schema、Owner、权威对象、风险和整改动作见 `ADS_API_40接口逐项权威映射.csv`。

## 3. SCO 35个操作映射

| API分组 | 数量 | 权威边界 |
|---|---:|---|
| Contracts | 6 | 合同参与方签署；SCO维护流程/版本 |
| Plans | 4 | SCO产生候选计划；Task Owner选择；不等于资源预留 |
| Federation | 1 | 候选发现；Participant/Capability Owner是源权威 |
| Runs | 7 | Site Task Owner / Local Task Coordinator最终控制执行 |
| Resources | 6 | SCO协调；各Site LCP/Lease Authority持有租约权威 |
| Results | 1 | Result Owner/Artifact Owner |
| Acceptance | 2 | Independent Acceptance Owner |
| Settlement | 3 | Metering Owner与Settlement Owner |
| Evidence | 1 | Evidence Owner |
| Operations | 4 | SCO只对Operation自身负责，不代表业务对象状态 |

逐项映射见 `SCO_API_35接口逐项权威映射.csv`。

## 4. 关键契约问题

1. RequestEnvelope孤立：ADS/SCO都定义组件，但Path引用0次；实际使用GenericCommand。
2. GenericCommand过宽：payload可选、additionalProperties=true，不能完成逐操作业务载荷验证。
3. Response过度抽象：大量接口返回ResourceReference，不能表达PolicyDecision、TaskRun、Acceptance、Settlement等强类型对象。
4. EvaluatePolicy返回202 Operation，但策略规范要求明确Decision、Owner、Obligations、valid_until、signature_ref。
5. Operation.status是命令/编排状态，不是业务对象权威状态。
6. SCO DOCX列有GET `/runs/{run_id}/operations` / ListRunOperations，但OpenAPI文件缺少该操作。
7. SCO规范要求Idempotency-Key、X-Request-ID、X-Correlation-ID、If-Match/ETag，但OpenAPI中Header参数计数为0。
8. RenewLease/ReleaseLease/ReconcileLease必须明确为向Site LCP/Lease Authority转发/对账，SCO不得拥有本地Lease写权。
9. Start/Suspend/Resume/Cancel/Retry只可请求本地动作，最终由Site Task Coordinator、PDP/PEP、Lease Authority判定。
10. SubmitResult、RequestAcceptance、CalculateSettlement必须严格区分结果、验收、计量和结算权威。
11. 列表接口需定义Page<T>、cursor、source_ref、freshness，不能用单一ResourceReference替代。
12. OpenAPI 3.2.1、DM04参考REST Binding 3.1.1的共同工具链尚未验证。
13. `example.invalid`与`{controlled-domain}`是占位命名空间，不可作为生产URI。

## 5. REST Header / Envelope 建议

- request_id与X-Request-ID一致；correlation_id与X-Correlation-ID一致。
- 写操作Idempotency-Key必需；Header与body同时出现时必须相等。
- 更新已有对象必须If-Match/ETag；缺失建议428，版本冲突412。
- caller_principal、workload_identity、audience从已验证OAuth2/mTLS上下文绑定，不信任body自报值。
- purpose从显式操作目的与TaskContract/DataSpaceContract/DataUseGrant解析；reason不等于purpose。
- protocol_profile由双方协商并登记；不从api_version/schema_version推断。
- IFC0.2仍只增加可选profile_extensions，不改IFC0.1必需字段。

## 6. ResponseContext建议

对异步写操作，Operation只表达操作进度。业务结果应通过result_ref指向强类型对象，并提供：
- request_id、responder_site_id；
- object_ref、object_version；
- command_status；
- authoritative_state（authority_ref、state_value、state_version、as_of、freshness）；
- event_cursor、evidence_refs。

Accepted不等于Succeeded；Succeeded不等于业务对象已被独立验收；Unknown必须对账。

## 7. 关键状态机

Participant、TrustAgreement、Credential、PolicyDecision、Capability、DataUseGrant、TaskContract、TaskPlan、TaskRun、ResourceReservation、ResourceLease、Operation、Result、Acceptance、Settlement分别维护独立状态机和权威Owner。禁止用一个`active=true`替代Registered/Verified/Published/Adopted/Authorized/Enforced/Available。

## 8. G2-03 交付与验证状态

已完成候选映射：
- 75个操作逐项Owner、Coordinator、Authority、Risk、Precondition、Ontology refs映射；
- 六域责任矩阵；
- 16项API契约缺口和整改矩阵；
- 15类关键对象状态机/权威矩阵；
- Header/Envelope绑定矩阵；
- Excel多工作表和CSV；
- SVG/8K架构图。

未完成：Owner签署、OpenAPI工具链验证、REST Binding RC1正式改版、两套独立实现互操作、真实双站点故障注入。

**准确状态：G2-03逐接口映射候选完成；不等于接口已实现或正式冻结。**
