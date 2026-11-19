# 559｜Evidence Target类型化引用与版本定位规范

**状态：** Evidence Target Model Candidate

## 1. 目标

Evidence Target必须能稳定定位到一个受控目标对象及其版本，而不是仅保存一个可能重定向、失效或被替换的URL。引用目标和访问权限分离：能定位不代表有权访问。

## 2. 目标引用结构候选

目标引用至少包含目标类型、目标稳定ID、目标版本或快照身份、目标Owner/权威来源和引用时间。允许目标类型必须来自经批准的OT/OF/子记录/受控外部目标注册表；不允许自由文本冒充类型化引用。

## 3. 固定版本与动态解析

- 历史事实、审计、决策和已核验Assertion原则上固定目标版本；
- 对持续更新的外部资源，可以保留动态引用，但核验时必须保存实际解析到的目标版本/内容摘要；
- 目标当前版本发生变化时，不得静默改写旧Evidence的Target Version；
- 目标删除或不可访问时，Evidence应进入相应失效/受限状态，不得伪造可用性。

## 4. Locator Schema

locator_schema_ref标识定位规则版本；locator_payload只表达定位坐标，例如文档页码/段落、表格行列、消息ID、媒体时间戳、网页片段或记录主键。坐标必须带目标版本语境，避免同一页码在不同版本指向不同内容。

## 5. Digest与Excerpt

target_content_digest摘要明确目标内容范围；locator_fragment_digest摘要定位片段；excerpt_digest摘要被保存的摘录。三者必须分别记录算法、Scope和规范化规则。摘要匹配不证明目标来源可信或Assertion真实。

## 6. 隐私与安全

locator_payload不得包含访问令牌、Cookie、签名URL秘密参数或可绕过PEP的直达凭据。敏感目标的定位信息应受控保存；对外展示时按Policy进行脱敏或拒绝。

## 7. 当前状态

本文件深化EVD-003至EVD-010的语义，不批准新增字段或Target类型；需要扩展时走ACR/OD和Owner审议。