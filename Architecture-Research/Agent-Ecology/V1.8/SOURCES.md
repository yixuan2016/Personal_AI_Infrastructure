# V1.8 研究来源与证据边界

以下来源用于识别标准/研究方向，不代表已被 Agent Ecology 采用为规范，也不代表相关方案已经达到生产成熟度。

1. **IETF Internet-Draft: Multi-agent Collaboration Protocol Suites Architecture, draft-li-dmsc-macp-07**, published 2026-11-02.  
   https://datatracker.ietf.org/doc/html/draft-li-dmsc-macp-07  
   状态：Internet-Draft / Work in Progress，非 RFC、非正式标准。参考价值：跨域 Agent onboarding、能力发现、能力同步、身份与授权协议的结构化讨论。

2. **ETSI GS ENI 005 V4.1.1 (2026-01), ENI System Architecture**  
   https://www.etsi.org/deliver/etsi_gs/ENI/001_099/005/04.01.01_60/gs_ENI005v040101p.pdf  
   状态：ETSI Group Specification。参考价值：闭环控制、策略管理、跨域策略冲突检测与架构功能分层。注意其部分联邦冲突处理内容属于进一步研究方向，不等于已标准化的完整方案。

3. **Romandini et al., Enabling trustworthy agentic AI through blockchain technology**, AI Magazine, first published 2026-09-04.  
   DOI: https://doi.org/10.1002/aaai.70084  
   参考价值：DID、VC、能力注册与交互背书的可验证信任基础设施；局限：链上信誉不能单独证明能力正确，密钥轮换、Sybil/串谋和规模化仍有挑战。

4. **Seven security challenges in cross-domain multi-agent LLM systems**, Nature Portfolio, 2026.  
   https://www.nature.com/articles/s44387-026-00128-9  
   参考价值：跨域协作中的信任边界、串谋与跨域风险传播。页面访问受限，本版本仅引用搜索摘要可见内容；需要后续获取全文核验。

5. **Cross-Agent Governance Alignment (CAGA): Verifiable Coordination Across Private AI Governance Domains**, SSRN, revised 2026-08-28.  
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6299461  
   状态：预印本/工作论文，不是正式标准。参考价值：区分跨域策略兼容与本地动作授权，并采用 ALLOW/DENY/ABSTAIN 语义。

## 证据使用规则

- 标准、Internet-Draft、研究论文、预印本和工程实践分层标注。
- 不把作者提出的框架写成行业共识。
- 不把 PoC、仿真或数值分析写成生产验证。
- V1.8 所提出的联邦协议、信任向量和状态机均为本项目候选设计，需要独立评审与验证。
