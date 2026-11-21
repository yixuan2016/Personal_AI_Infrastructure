# ADR-12：AEE/ASCP URI Namespace 治理

- 状态：Proposed（待项目域名Owner与双方治理Owner评审）
- 决策：正式扩展 URI 必须使用项目/组织控制的稳定域名或正式命名空间；当前仅定义 URI 模板，不将 example.invalid 作为生产 URI。
- 前置：确认域名控制权、Namespace Owner、稳定解析、TLS、规范文档、Schema摘要、兼容和弃用策略。
- 规则：URI 永不重新分配；Major 语义变化新建 Major URI；弃用保留历史记录和迁移窗口。
- 注册字段：URI、Owner、版本、Schema Ref、Digest、状态、生效时间、兼容范围、联系人、签署记录。
- 禁止：个人临时域名、短链、未签署 URI、将 A2A 官方命名空间用于项目自定义扩展。
- 验收：双方解析结果与 Schema Digest 一致；Owner 签署记录可验证；未知 required 扩展在副作用前拒绝。
