# 509｜M06 TDA/SA审议工作流与语义定稿边界

**状态：** TDA/SA Review Workstream Candidate；M06 Owner Feedback Pending

## 1. 审议目标

核验M06作为六个S1 OT候选Type Definition Authority/Semantic Authority时，对类型定义、字段语义、关系、基数、枚举和跨对象语义是否具有清晰权威；并防止把M06语义权威扩大为实例写入、物理保管或Policy裁决权。

## 2. 必须定稿的语义层

- OT/子记录/Projection的粒度及身份边界；
- 字段定义、数据类型、Cardinality、缺失语义和可变性；
- 对象关系、引用目标类型、方向、基数和删除语义；
- 生命周期状态、合法迁移和状态正交性；
- Source与SourceSnapshot、RawAsset与Physical Handle、KnowledgeAsset与Version、ExtractionRun与Processor、Chunk与Projection的概念边界；
- Evidence Target联合分支、Locator坐标、Digest范围和Integrity语义；
- Schema/Contract/Event版本兼容原则。

## 3. 六对象重点议题

| 对象 | M06重点审议 | 不应由M06代替 |
|---|---|---|
| Source | Source身份、来源权威、Locator和Rights引用语义 | 外部来源事实确认、M08实例写入 |
| SourceSnapshot | 不可变快照、采集封套、子记录基数 | M02字节保管、M18处理依据 |
| RawAsset | 逻辑原始资产与物理字节的类型关系 | M02 Handle/密钥/物理删除 |
| KnowledgeAsset | 逻辑知识资产、内容版本和处理状态正交性 | M08实例维护、M18 Policy |
| ExtractionRun | 有界处理记录、输入输出引用、UnknownOutcome | M15 Provider能力、M18策略 |
| Chunk/Evidence | 派生片段、集合完整性、类型化Target与完整性语义 | M07 Projection实现、Assertion核验执行的其他权威 |

## 4. Evidence边界特别审议

M06负责定义Evidence与Assertion的语义关系及其核验流程；M08维护Evidence对象的身份、TargetRef、Locator、Digest和生命周期记录。Digest匹配只能说明指定范围的内容摘要一致，不能自动说明来源可信、断言真实或Assertion Verified。Receipt原件由M17维护；Observation原件由其真实Owner维护。

## 5. 需要回答的问题

1. 六个OT是否存在字段重名但语义不同的情况？
2. SourceAuthority、Provider、CaptureActor和CreatedBy是否明确区分？
3. `Unknown/Null/Absent/Empty/Withheld`是否具有一致且可测试的含义？
4. 版本号是否区分对象版本、内容版本、Schema版本、Processor版本和Event版本？
5. 关系基数是否有现实场景和反例支持？
6. 子记录与OT的区别是否在Registry中表达清楚？
7. 是否有字段实际上属于M02/M18/M07/M15的权威对象，而不是M08 OT字段？
8. 哪些变更需要ACR或OD，而不能作为普通字段修订？

## 6. 所需证据

字段词汇表、既有OT Registry映射、类型定义原件、关系样例、状态迁移表、消费者契约、反例、负向测试映射和Owner明确决议。M06对语义的批准必须限定到精确Field ID/Relation ID/Profile Version。

## 7. 当前结论

本文件不代表M06已经审议或批准任何字段。全部Profile仍为Candidate/Proposed；M06真实反馈和批准证据待接收。