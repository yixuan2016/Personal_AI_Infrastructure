# AEE/ASCP URI 命名空间与注册规范（候选）

## 当前结论
尚未收到可确认由项目主体控制的正式域名。因此本文件仅提供 URI 模板，不声称已经注册任何 URI。`example.invalid` 只能用于文档示例，不得用于跨站点请求或生产配置。

## URI 模板
- Profile：`https://{controlled-domain}/aee-ascp/profiles/1.1`
- AEE Context Schema：`https://{controlled-domain}/aee-ascp/schemas/context/1.1`
- TaskClaim Schema：`https://{controlled-domain}/aee-ascp/schemas/task-claim/1.1`
- Event Type：`https://{controlled-domain}/aee-ascp/events/{event-name}/1`
- Ontology Profile：`https://{controlled-domain}/aee-ascp/ontology/{profile-name}/3.0`
- A2A Extension：`https://{controlled-domain}/aee-ascp/a2a/extensions/1.1`

## 命名与生命周期
1. URI 必须归属项目/组织控制的稳定域名或正式命名空间。
2. URI 永不重新分配给另一语义。
3. Major 语义变化使用新 Major URI；Minor/patch 通过版本元数据、Schema Digest 和兼容矩阵管理。
4. 规范文档和 Schema 必须稳定解析；不得指向临时文件、短链或个人账号。
5. 弃用必须保留历史记录、替代 URI、迁移窗口和停止服务日期。
6. A2A 自定义扩展不得使用 A2A 官方命名空间冒充官方扩展。

## 注册记录最小字段
`uri`、`namespace_owner`、`profile_version`、`schema_ref`、`schema_digest`、`status`、`effective_at`、`compatibility`、`deprecation`、`contact`、`signature_ref`。

## 正式激活门禁
- 域名控制权和TLS证书已验证；
- Namespace Owner已指定并完成签署；
- Profile与Schema文档可稳定解析；
- Schema Digest与双方注册表一致；
- 兼容/弃用策略完成评审；
- 双方治理Owner签署；
- 双实现能验证URI、版本、摘要和未知扩展处理。

未满足全部条件，状态保持 `Candidate / Not Registered`。
