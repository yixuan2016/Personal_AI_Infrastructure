# 558｜Chunk Projection权限继承、撤销与失效治理

**状态：** Projection Governance Candidate

## 1. Projection边界

Embedding、向量索引、关键词索引、摘要、Context Cache和其他派生视图均属于Projection或派生副本。它们为查询和使用提供便利，但不构成新的事实权威，也不能因为不可直接阅读原文就自动降低敏感级别。

## 2. 权限继承

Projection必须能够追溯到Chunk、ChunkSet Version、KnowledgeAsset Content Version和源Purpose/Classification。访问控制至少检查当前主体、用途、动作、资源、策略版本和Projection状态。创建Projection时的许可不能替代每次读取时所需的当前Policy判断。

## 3. 撤销与失效传播

发生Consent撤回、Purpose不再适用、Classification提升、源资产删除、ChunkSet被撤销或Provider授权变化时，必须触发受影响Projection重新评估。传播链应覆盖索引、向量、缓存、预计算摘要、Context Bundle和外部检索副本。

## 4. 失效状态候选

Active、RefreshPending、Stale、AccessRestricted、RevocationPending、RemovalPending、Removed、RemovalBlocked。不得把“已从主索引移除”解释为所有缓存和备份均已清除。Projection状态与源Chunk生命周期分开管理。

## 5. 读取时保护

任何检索路径不得绕过M18 Policy和M07访问编排，直接凭向量库或缓存命中返回受限内容。过滤必须在结果进入模型上下文前完成；若无法证明过滤完整，应拒绝返回或降级到安全路径。

## 6. 删除回执

M07负责Projection层移除和刷新证据；M02负责其管理的物理存储副本；M15/Provider负责外部处理副本；M18决定策略和保留例外。跨模块协调器可以编排流程，但不能替代各权威签发回执。

## 7. 当前状态

本文件为M07/M18审议候选，不代表已有Projection权限继承或删除传播能力。