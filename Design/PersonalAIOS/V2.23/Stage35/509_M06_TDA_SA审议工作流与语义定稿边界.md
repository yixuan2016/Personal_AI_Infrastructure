# 509｜M06 TDA/SA审议工作流与语义定稿边界

**父基线：** V2.22-Draft / 00—503  
**目标基线：** V2.23-Draft / 00—523  
**状态：** Candidate / Pending；不推断Owner批准，不授权工程实现

## 1. 目的
核验M06对类型、字段、关系、基数、枚举和跨对象语义的决定权，不扩大为实例写入、物理保管或Policy裁决权。

## 2. 审议范围
- OT/子记录/Projection粒度；字段类型、Cardinality、缺失语义和可变性。
- 关系方向、基数、引用目标、生命周期和合法迁移。
- 对象版本、内容版本、Schema版本、Processor版本和Event版本分离。
- Evidence Target联合分支、Locator坐标、Digest范围和Integrity语义。

## 3. 权威边界与控制要求
- M06定义Evidence—Assertion语义关系和核验流程；M08维护Evidence身份、TargetRef、Locator和Digest。
- Digest匹配不能推导来源可信或Assertion Verified。
- Receipt原件由M17维护，Observation由真实Owner维护。

## 4. 所需证据与验收
- 词汇表、OT Registry映射、关系样例、状态迁移、消费者契约、反例和负向测试。
- 批准范围必须精确到Field ID/Relation ID/Profile Version；当前仍Candidate/Proposed。

**统一状态声明：** 本文件为审议准备材料；未取得真实Owner原始反馈和有效批准证据前，相关事项保持Pending/Proposed，不得升级为Approved或Freeze。
