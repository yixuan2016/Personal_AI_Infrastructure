# 506｜S1 Feedback Record字段Schema与填写模板

**父基线：** V2.22-Draft / 00—503  
**目标基线：** V2.23-Draft / 00—523  
**状态：** Candidate / Pending；不推断Owner批准，不授权工程实现

## 1. 目的
将原始反馈、原子问题和正式决策拆成三个独立记录，避免一段自由文本同时承担意见、批准和版本变更。

## 2. 审议范围
- Feedback Record：ID、基线、原始来源、来源类型、接收时间、提交者、角色、身份核验、权限范围、原始意见、整理摘要、受影响对象/字段、证据、隐私分类和状态。
- Atomic Issue：Issue ID、反馈引用、问题类型、单一问题、当前定义、请求变化、理由、证据、决定权威、会审方、风险、依赖和测试引用。
- Decision Record继续沿用495号Schema。

## 3. 权威边界与控制要求
- Feedback Record不拥有selected_option或approval_evidence_ref。
- 身份/权限未核验的输入不能升级为OwnerApproved。
- AIAnalysis来源不得标记为批准证据。

## 4. 所需证据与验收
- 原始引用、整理摘要、身份核验、授权范围、受影响对象和证据引用。
- 每个Atomic Issue只问一个可判定问题。

**统一状态声明：** 本文件为审议准备材料；未取得真实Owner原始反馈和有效批准证据前，相关事项保持Pending/Proposed，不得升级为Approved或Freeze。
