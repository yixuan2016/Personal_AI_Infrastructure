# DM04 IFC0.2 `profile_extensions` 增量提案

**状态：** Proposed；不是已批准的 DM04 契约。  
**基线：** V2.9-RC9.2-DM04-IFC0.1。  
**性质：** 仅增量契约提案，不是代码实现。

## 1. 变更边界
只增加可选属性 `profile_extensions`；原 IFC0.1 必需字段、状态机、幂等和响应语义保持不变。此 JSON Schema 是增量片段，不替代完整 RequestEnvelope Schema。

## 2. 候选结构
```json
{
  "profile_extensions": {
    "https://{controlled-domain}/aee-ascp/profiles/1.1": {
      "profile_version": "1.1.0-rc0",
      "schema_ref": "https://{controlled-domain}/aee-ascp/schemas/context/1.1",
      "criticality": "required",
      "payload_digest": "sha256:<64位十六进制摘要>",
      "data": {
        "environment_ref": "urn:environment:...",
        "ontology_profile_ref": "urn:ontology:...",
        "trace_refs": ["urn:trace:..."],
        "governance_context_ref": "urn:governance-context:..."
      }
    }
  }
}
```
`{controlled-domain}` 是占位符，正式发布前必须替换为已验证的项目控制域名。

## 3. 字段语义
| 字段 | 含义 | 约束 |
|---|---|---|
| map key | Profile URI | HTTPS、唯一、已注册 |
| profile_version | Profile语义版本 | SemVer/RC约定 |
| schema_ref | 数据Schema URI | 必须与双方注册表匹配 |
| criticality | required / optional | 未知 required 拒绝；未知 optional 忽略并审计 |
| payload_digest | 扩展data摘要 | 对规范化data计算SHA-256 |
| data | Profile数据 | 必须按schema_ref校验；AEE数据只允许引用 |

## 4. 禁止承载
- DataUseGrant或任何Bearer Token；
- 本地资源Lease、FencingToken；
- 原始数据、Artifact正文或超出授权字段的载荷；
- 用于覆盖RequestEnvelope的purpose、audience、caller_principal、workload_identity、expires_at、idempotency_key或expected_state_version的字段。

## 5. 接收端规则
1. 未协商IFC0.2，不得发送。
2. 未知URI + required：副作用前拒绝。
3. 未知URI + optional：忽略处理并记录审计。
4. Schema或摘要失败：拒绝。
5. 已知URI但版本不兼容：按criticality拒绝或忽略。
6. 引用解析时必须由目标站点本地PDP/PEP重新授权。
7. 高风险写请求的整体payload_digest必须覆盖profile_extensions。
8. 扩展缺失或未激活但又是安全执行前提时，暂停该操作，不得自动降级为放行。

## 6. 响应建议
可在 IFC0.2 ResponseEnvelope 增加可选 `profile_extensions_applied`，回显已处理的URI、版本、摘要和状态（applied/ignored），避免调用方误以为 optional 扩展已生效。该字段同样待双方评审。

## 7. 候选错误语义
`UNSUPPORTED_REQUIRED_EXTENSION`、`PROFILE_EXTENSION_INVALID`、`PROFILE_VERSION_MISMATCH`。尚未分配到 DM04 现有错误码目录；需 API Owner 审核编号和HTTP映射。

## 8. 兼容与放行
IFC0.2批准前，IFC0.1继续作为互操作基线。必须通过双实现Schema校验、required/optional测试、摘要篡改测试、未知扩展零副作用测试和向后兼容测试。
