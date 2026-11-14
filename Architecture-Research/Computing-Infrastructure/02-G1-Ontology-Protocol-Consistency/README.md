# 算力底座 G1 Ontology 与协议契约一致性包

状态：候选设计，待Owner评审签署；不含工程实现代码。

## 本轮发现
1. DM04 IFC0.1与ADS/SCO OpenAPI RC0 Request/Response Envelope存在字段语义和必需性差异。
2. Ontology V3.0存在ParticipantBinding、TrustAgreement、DataSpaceContract、DelegationGrant、HumanApproval、OutputArtifact、Result等语义缺口。
3. AEE/ASCP六对象应采用直接映射、关联投影、Profile/Runtime扩展三类方式，不能另建平行权威。
4. A2A、CloudEvents、FWSX、DM04分层，不互相替代。

## 文件
- G1_Ontology与协议契约一致性报告.docx / .md
- G1_IFC0.2_Request_Response_Envelope对齐增量.md
- G1_A2A_CloudEvents_FWSX分层互操作规范.md
- matrices/G1_六对象逐字段Ontology_DM04映射.csv（69行）
- matrices/G1_Ontology缺口与修订建议.csv（14项）
- matrices/G1_IFC0.1与ADS_SCO_OpenAPI字段兼容矩阵.csv（24项）
- matrices/G1_ResponseEnvelope状态语义交叉表.csv
- matrices/G1_A2A_CloudEvents_FWSX协议兼容矩阵.csv（25项）
- matrices/G1_66项双站点互操作验收总矩阵.csv（66项）
- decisions/ADR-G1-01至03
- diagrams/G1_Ontology_DM04_AEE协议分层全景图.svg / 8K.png
- MANIFEST_SHA256.txt

## 验收状态
DM04 48项 + AEE/ASCP 18项 = 66项。当前全部待执行；不代表真实双站点互操作通过。
