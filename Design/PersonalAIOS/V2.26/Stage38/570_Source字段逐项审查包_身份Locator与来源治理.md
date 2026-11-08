# 570｜Source字段逐项审查包：身份、Locator与来源治理

**状态：** Field-Level Design Review Candidate；Owner Feedback 15/15 Pending；No Approval

## 1. 对象边界

Source表示来源主体/来源系统及其持续身份，不等于一次采集结果，也不等于某个物理文件。Source身份变化、外部Locator变化和SourceSnapshot历史必须分离。D-01/D-02/D-04是本对象主要决策边界。

## 2. 字段逐项审查

| Field ID | 字段 | 设计审查焦点 | 主要决策 |
| SRC-001 | `source_id` | Source稳定身份是否全局唯一；ID是否与外部来源ID分离，是否允许迁移而不改变本地身份。 | D-01 |
| SRC-002 | `source_kind` | source_kind是否为受控分类；扩展枚举是否有兼容和未知值处理规则。 | D-01 |
| SRC-003 | `source_authority_ref` | source_authority_ref指向谁；权威范围、有效期、授权与冲突仲裁是否明确。 | D-01 |
| SRC-004 | `origin_identity_ref` | origin_identity_ref的命名空间、外部ID变更、碰撞和不可用场景如何表达。 | D-01 |
| SRC-005 | `locator_refs` | locator_refs是否支持多值、历史、优先级和失效；凭据是否与定位信息隔离。 | D-02 |
| SRC-006 | `availability_state` | availability_state表达当前可访问性还是来源自身可用性；状态由谁观测、何时过期。 | D-02 |
| SRC-007 | `lifecycle_state` | lifecycle_state是否与availability_state分离；归档、撤回、删除和停用是否可区分。 | D-01/D-02 |
| SRC-008 | `source_rights_refs` | source_rights_refs如何表达多重权利、地域/用途限制、有效期和撤回。 | D-04 |
| SRC-009 | `data_subject_refs` | data_subject_refs是否最小化；多主体、未知主体和身份纠错如何表达。 | D-04 |
| SRC-010 | `classification_ref` | classification_ref是否由权威分类体系提供；来源分类变化如何传播到派生物。 | D-04 |
| SRC-011 | `created_by_ref` | created_by_ref表示创建者还是实际采集Actor；服务账号和代理行为如何标记。 | D-01/D-02 |
| SRC-012 | `created_at` | created_at使用哪个时钟、时区和精度；是否代表业务发生时间还是记录创建时间。 | D-01/D-02 |
| SRC-013 | `updated_at` | updated_at由哪些变更触发；是否避免被无关读取或派生过程刷新。 | D-01/D-02 |
| SRC-014 | `object_version` | object_version如何递增、并发冲突如何处理；与Snapshot Sequence是否分离。 | D-01/D-02 |
| SRC-015 | `supersedes_source_ref` | supersedes_source_ref表达替代、合并还是纠错；循环引用和多对一如何处理。 | D-01 |

## 3. 对象内一致性约束

- source_id稳定且不携带外部系统的可变定位语义。
- source_authority_ref与origin_identity_ref不得混用：前者回答谁对来源有权威，后者回答外部身份是什么。
- locator_refs是定位集合，不是访问凭据集合；凭据必须经独立秘密/授权机制处理。
- availability_state与lifecycle_state正交：来源可访问不代表仍允许采集，来源停用也不必抹去历史Snapshot。
- source_rights_refs、data_subject_refs、classification_ref分别表达权利、主体和分类，不能压缩成一个“可用”标志。
- supersedes_source_ref必须防循环；替代关系不应删除旧Source身份或历史引用。

## 4. 关键交叉检查

D-01：本地ID稳定、外部命名空间显式、Authority冲突可升级。  
D-02：Locator多值/历史/失效可表达，凭据隔离，失效不改变Source身份。  
D-04：权利、主体、分类、Purpose和Policy分别可追踪；下游Snapshot采集必须重新检查当前依据。

## 5. Owner审议证据

需要Source Authority真实授权证明、外部身份样例、Locator历史与失效样例、凭据隔离方案、Rights/Purpose/Consent政策依据和消费者清单。没有证据时不得把来源名称或URL当作身份权威。

## 6. 当前结论

15/15字段完成设计审查问题登记；Owner状态15/15 Pending；无字段批准，无Source Profile Delta获批。

## 5. 字段审查结果状态

| 检查项 | 结果 |
|---|---|
| 字段ID/名称核对 | 15/15 与Stage35原始台账一致 |
| 语义审查问题 | 15/15 已登记 |
| Owner真实反馈 | 0 |
| Owner批准 | 0 |
| Profile/Contract变更批准 | 0 |
| 当前处置 | Candidate / Owner Review Required |

**说明：** 本文件是逐字段审查准备材料，不更新514号原始反馈台账中的Pending状态。