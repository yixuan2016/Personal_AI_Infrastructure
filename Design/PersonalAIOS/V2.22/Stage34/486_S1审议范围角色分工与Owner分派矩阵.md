# 486｜S1审议范围、角色分工与Owner分派矩阵

**状态：** Responsibility Assignment Candidate；Owner Confirmation Pending

## 1. 权威角色不得混同

| 角色 | 决定/负责的内容 | 不代表拥有的权力 |
|---|---|---|
| Instance Authority（IA） | 实例创建、更新、状态与生命周期写入 | 不自动拥有类型语义或来源事实权威 |
| Type Definition Authority（TDA） | 对象类型、字段、类型约束和Profile定义 | 不替代Source Authority或法定授权 |
| Semantic Authority（SA） | Ontology、Assertion关系及语义解释 | 不自动拥有物理字节和策略决策 |
| Physical Custodian | 物理字节、密钥、宿主访问、备份和物理删除 | 不拥有知识资产/Assertion语义 |
| Projection Owner | Chunk、Embedding、Index、Context等派生投影 | 不得降低源数据权限或改变源权威 |
| Policy Authority | Purpose/Policy/Approval登记及策略裁决规则 | 不替代个人对价值/目标的最终确认 |
| Source Authority | 原始来源内容或外部资源的事实/发布权威 | 不等同于采集平台或本地存储者 |
| Personal Owner | 本人数据主权、个人意图和需要本人确认的决定 | 不替第三方主体授权 |

## 2. 既有OF-006角色分配

本阶段严格沿用312号OF-006既有角色分配：六个OT的候选IA=M08；候选TDA/SA=M06；Physical Custodian=M02；Policy Authority=M18。该分配在本阶段作为审议输入，不因矩阵复述而升级为新的批准。

## 3. 对象级审议矩阵

| 对象 | 主审议方 | 必须会审 | 专项审查 | 决策边界 |
|---|---|---|---|---|
| OT-SOURCE | M08（IA候选）、M06（TDA/SA候选） | M02、M18、M17 | Privacy/Legal | 身份、来源权威、Locator、Rights和Snapshot关系 |
| SourceSnapshot | M08、M06 | M02、M18、M17 | Privacy/Legal | 不可变性、采集封套、字节保管和历史Rights |
| OT-RAW-ASSET | M08、M06 | M02、M18 | Security/Privacy | 逻辑资产与物理字节/密钥/删除边界 |
| OT-KNOWLEDGE-ASSET | M08、M06 | M02、M18、M07 | Privacy/Security | 内容版本、处理版本、分类和派生闭包 |
| OT-EXTRACTION-RUN | M08、M06 | M15、M18、M02 | Security/Privacy/Legal | Processor、Provider、Region、Purpose、UnknownOutcome |
| OT-CHUNK | M08、M06 | M07、M18 | Security/Privacy | 父版本、ChunkSet发布、Projection和权限继承 |
| OT-EVIDENCE | M08、M06 | M17、M18、目标对象Owner | Privacy/Legal | TargetRef、Locator、Digest和Assertion核验边界 |

## 4. 议题分派规则

- 字段定义、Cardinality、对象状态、引用约束：M06作为TDA/SA候选主审，M08提供实例维护事实。
- 对象实例、写入、版本、生命周期和血缘：M08作为IA候选主审。
- 物理Handle、加密、备份、宿主权限和物理删除：M02主审；M08不得代为批准。
- Purpose、Consent、Policy、Approval、Retention和分类规则：M18主审；Privacy/Legal提供独立专业意见。
- Processor、Provider、Region、模型条款和外发：M15与M18会审，Security/Privacy/Legal独立审查。
- Chunk/Embedding/Context投影：M07与M08会审，M18审查权限继承。
- ConnectorReceipt原件：M17保有原件权威；Evidence只引用，不复制权威。
- Observation目标：由Observation实际Owner确认，不能由M08或M06替代。

## 5. 冲突时的原则

一个字段可以有多个会审方，但只能有一个适用的决定权威或明确的联合决策规则。会审方的沉默不视为批准；IA不应因“负责写入”而获得TDA/SA或Policy Authority；Security/Privacy/Legal意见不能被产品或工程便利性覆盖。

## 6. 未决项

各模块具体授权代表、替补代表、批准方式、审批时限和升级路径尚待真实Owner确认。未确认前，本矩阵仅是候选分派方案。
