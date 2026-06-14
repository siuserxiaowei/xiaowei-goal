---
title: "AI 产品开发与获客经验分享：xiaowei-goal 拆解"
---

# AI 产品开发与获客经验分享：xiaowei-goal 拆解

资料范围：飞书智能纪要《AI产品开发与获客经验分享》，会议时间 2026-05-10 18:45-19:52。本文只发布结构化理解、外部资料补充和业务拆解，不公开原始逐字稿与私有飞书链接。

处理方式：按 `xiaowei-goal` 三阶段流程执行：先做广域联网调研，再做 Deep Research 交叉判断，最后落到业务动作，并用「道法术器势」拆解。

## 一句话结论

这份纪要的核心是 **AI 产品不是从“我想做什么”开始，而是从“哪里已经有人痛、有人搜、有人付费、有人抱怨”开始**。中小团队最适合的路径不是教育全新市场，而是在已有付费心智里做细分、做更快的交付、做更好的体验和内容分发。

## 阶段 1：广域联网调研补充

| 来源 | 关键事实 | 对本纪要的补充意义 |
|---|---|---|
| [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | SEO 的核心是让搜索引擎理解内容，并帮助用户发现与判断。 | 纪要里的内容获客要回到“用户真正要什么”，不能只堆关键词。 |
| [Google 生成式 AI 搜索优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Google 生成式搜索仍依赖核心搜索质量系统；高质量、非同质、可抓取内容更重要。 | “ChatGPT/Gemini 流量”要靠内容可信度和可抓取结构，不是单纯投机。 |
| [GEO: Generative Engine Optimization 论文](https://arxiv.org/abs/2311.09735) | 生成式搜索让网站可见性成为新问题，论文提出 GEO 框架，并显示部分策略可提升生成式答案中的可见性。 | 会议里提到的 GEO 方向有研究基础，但不能把它简化成发垃圾软文。 |
| [Adsy 官方网站](https://adsy.com/) | Adsy 定位为 Digital PR、Blog & Guest Posting 服务，提供大量站点筛选和内容投放能力。 | 软文投放可以作为分发工具，但要评估站点质量、真实性和长期 SEO 风险。 |
| [Apple App Store Product Page Optimization](https://developer.apple.com/app-store/product-page-optimization/) | App Store 支持测试图标、截图、预览视频等不同版本，观察转化表现。 | 如果以后跑 APP，获客不是只买量，要系统做商店页转化实验。 |
| [Apple Custom Product Pages](https://developer.apple.com/app-store/custom-product-pages/) | App Store 可创建最多 70 个自定义产品页，并用于不同广告/受众。 | 会议中“按场景/国家/语言细分”可以落到 App Store 的不同页面。 |
| [Apple Ads Campaign Structure](https://ads.apple.com/app-store/best-practices/campaign-structure) | Apple Ads 建议按品牌、品类、竞品、发现等关键词主题拆分广告结构。 | APP 获客要从关键词结构、否定词、发现词迭代，而不是一个广告组打天下。 |
| [Google Play Acquisition Reporting](https://play.google.com/console/about/acquisitionreporting/) | Google Play 可按国家、语言、商店页、安装状态、搜索词、UTM 分析获客。 | Android APP 出海时，必须用第一方数据拆渠道和国家表现。 |
| [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) | Agent 可通过工具、MCP、handoff、guardrails、人审和观测构建复杂流程。 | “把知识付费产品化”可以做成 Agent，而不是只卖课程或咨询。 |
| [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | LLM 应用需防提示注入、不安全输出、数据污染、供应链等风险。 | 用 AI 自动生成内容、招聘判断、客服回复时，必须有人审和输出校验。 |

## 逐句级理解

| 纪要信息点 | 我的理解 | 业务含义 |
|---|---|---|
| “宏观趋势就是跟着 AI 走。” | AI 是底层生产力趋势，但不能替代商业判断。 | 要把 AI 作为能力底座，而不是把“AI”当产品卖点本身。 |
| “从小红书、抖音、微博、Reddit、YouTube 的抱怨里找需求。” | 抱怨比灵感可靠，因为抱怨代表未满足需求和真实语言。 | 建立需求雷达：抓痛点、频次、付费线索、现有替代方案。 |
| “用 AI 分析评论。” | AI 适合把大量碎片评论聚类成痛点和机会。 | 让 AI 先做归类，人再判断商业价值和可做边界。 |
| “看付费排行榜、支付平台、流量和订单排名。” | 有付费证据的市场比纯想象更可靠。 | 需求验证要包含：有人搜、有人骂、有人买、有人复购。 |
| “中小公司不要教育全新市场。” | 教育市场成本高，适合大资本或强品牌。 | 小团队应进入已有需求池，做细分切口。 |
| “在别人教育好的市场中找机会。” | 不是抄袭，而是复用市场心智，重做体验、场景、语言、价格。 | 可迁移结构，不能复制品牌、内容、代码和素材。 |
| “按场景、语言、国家变窄。” | 越窄越容易写准文案、找到渠道、打透转化。 | 一个产品可以有多个 landing page / custom product page。 |
| “ADSY 软文推广，围绕用户担忧写很多角度。” | 这是内容分发和数字 PR 思路。 | 可以测试，但要避免低质量外链和不真实提及。 |
| “最多写 200 篇文章。” | 规模化内容只有在选题真实、结构清晰、质量可控时才有效。 | 先做 20 篇验证，不要一上来批量铺垃圾内容。 |
| “可能获得 ChatGPT/Gemini 流量。” | AI 搜索会引用可抓取、可信、结构清晰的网页。 | 文章要有事实、案例、FAQ、比较、更新日期和作者可信度。 |
| “多平台内容营销。” | 推荐系统之间不完全相同，单平台风险高。 | 小红书验证，官网承接，视频号/抖音/B 站/知乎做补充分发。 |
| “看竞品和爆款内容。” | 爆款是平台对用户兴趣的反馈。 | 拆结构和用户关注点，不照搬表达。 |
| “多账号矩阵测试。” | 这是测试不同人设、话题、角度和受众。 | 需要统一素材库、选题库、违规红线和数据表。 |
| “有钱的团队可以做 KOL 合作。” | KOL 是买信任和分发，但投放质量差异很大。 | 投前看受众匹配、历史转化、内容质量，不只看粉丝数。 |
| “支付平台客户推荐。” | 支付/结算环节可能带来生态流量。 | 如果做 SaaS，要争取 marketplace、案例页、合作推荐。 |
| “知识付费和咨询有时间限制。” | 卖时间很难规模化，续费和交付压力大。 | 把知识转成产品、Agent、模板、工具、订阅。 |
| “有了 AI，可以把一个人当产品卖出去。” | 本质是把专家的知识、判断和流程产品化。 | 不是复制人格，而是封装其方法论、资料库、案例库和判断路径。 |
| “把课程、材料、认知放进飞书知识库。” | 知识库是 Agent 的上下文资产。 | 资料要结构化：概念、案例、FAQ、流程、模板、禁区。 |
| “做 Agent、网站、小程序月费。” | 把一次性交付改成可持续服务。 | 月费产品必须持续更新、持续产生价值。 |
| “用会议纪要/方法论持续更新知识库。” | 内容生产本身变成产品迭代。 | 每次咨询、课程、交付都要沉淀为可复用资料。 |
| “AI 结合风格、热点、别人内容，人工审核，再二创。” | 人负责选题和判断，AI 扩展表达形式。 | 必须区分参考、改写、原创，避免侵权和同质化。 |
| “低价低利低复购走矩阵，高价高利高复购走精细内容。” | 获客打法取决于客单价和 LTV。 | 不同产品不能用同一套内容策略。 |
| “老师宠物产品前两个失败，第三个成功。” | 产品成功往往来自连续试错，不是一次命中。 | 保留失败数据，找真正触发购买的元素。 |
| “健身教练产品先做核心功能 MVP。” | 不要先做平台，先做最短付费路径。 | 做一个能让用户当天得到训练计划/反馈的核心功能。 |
| “再小需求在大人口基数下也可能很大。” | 这句话成立但有前提：可触达、可支付、可交付。 | 不只算总人口，要算可触达市场和转化率。 |
| “AI 招聘：简历、MBTI、面试分析。” | AI 可辅助筛选和结构化记录，但不能单独决定录用。 | 用作辅助评分和面试问题生成，保留人工判断和公平性检查。 |
| “电商 AI 自动化、老板带头。” | 自动化要从老板关心的指标切入。 | 先自动化高频、低风险、可衡量任务。 |
| “视频生成别追求完美，先看流量。” | 内容早期应追求反馈速度。 | 先跑 10 个选题和 3 种结构，再决定是否提高制作成本。 |

## 阶段 2：Deep Research 判断

### 已被外部资料强化的判断

1. **需求挖掘必须从真实语言和付费证据开始。** 搜索、社媒评论、商店页评论、竞品价格页、广告关键词都比闭门想象可靠。
2. **AI 搜索/GEO 值得做，但底层仍是 SEO 和可信内容。** Google 明确强调生成式搜索仍依赖核心搜索质量系统，所以“AI 搜索优化”不能脱离内容质量、技术可抓取性和真实性。
3. **APP 获客需要商店页实验。** Apple 和 Google Play 都提供商店页转化、国家/语言、搜索词、UTM 等数据能力，适合把“场景/国家/语言细分”落成实验。
4. **知识产品化可以成为小伟业务的一条主线。** 把个人经验、会议纪要、案例、方法论变成可调用知识库，再做 Agent/网站/订阅，符合会议方向。

### 需要修正的判断

1. **软文和外链不是越多越好。** Google 对低质量、操纵性内容和不真实提及有明确风险提示。应优先做可被用户验证的内容，而不是只为机器写。
2. **多账号矩阵不是无限开号。** 如果没有统一选题、素材、指标和合规边界，矩阵会变成低质量内容工厂。
3. **AI 招聘不能用 MBTI 之类标签做决定性筛选。** 这类信息最多作为沟通参考，不能替代岗位能力和实际任务表现。

### 仍需验证的问题

1. 小伟要做的 APP/网站具体行业是什么，已有用户在哪里抱怨。
2. 目标市场是国内、小语种国家，还是英语市场。
3. 产品适合一次性售卖、订阅，还是服务+工具混合模式。

## 阶段 3：应用到业务

| 业务环节 | 可执行动作 | 验证指标 |
|---|---|---|
| 需求池 | 每个方向抓取 100 条用户原话，按痛点、场景、替代方案、付费意愿聚类。 | 高频痛点是否集中，是否有现有购买行为。 |
| MVP | 每个方向只做一个核心承诺，如“一键生成训练计划”“一键拆解会议纪要”“一键生成老师班级激励页”。 | 24 小时内能否交付结果，用户是否愿意留资或付款。 |
| 内容获客 | 先做 20 篇高质量文章/笔记，不直接铺 200 篇。 | 点击率、收藏率、咨询率、搜索收录、自然访问。 |
| AI 搜索 | 官网每个页面包含问题、结论、步骤、案例、FAQ、更新日期、作者/团队说明。 | Google 收录、自然关键词、AI 搜索引用或 referral。 |
| APP 获客 | iOS 准备不同 custom product page；Android 用 UTM、国家、语言拆数据。 | 商店页转化率、CPI、留存、付费率。 |
| 知识产品化 | 把会议纪要、课程、案例、问答放进知识库，做成 Agent 服务。 | 月活、复用次数、用户节省时间、订阅续费。 |
| 内容矩阵 | 统一选题库、素材库、发布节奏、复盘表。 | 单账号与矩阵总体 ROI，违规率，重复内容比例。 |

## 道法术器势拆解

| 层级 | 拆解 | 对应动作 |
|---|---|---|
| 道 | 商业机会来自真实需求和付费心智，不来自脑内灵感。 | 先找用户抱怨和付费证据，再决定做什么。 |
| 法 | 用“需求雷达 - MVP - 内容验证 - 数据复盘 - 产品化订阅”的方法跑闭环。 | 每个方向最多 14 天完成第一轮验证。 |
| 术 | 评论分析、竞品拆解、排行榜观察、软文/SEO、社媒矩阵、KOL、商店页 A/B、知识库 Agent。 | 先小样本验证，跑通后再规模化。 |
| 器 | Google Search Console、App Store Connect、Google Play Console、Apple Ads、知识库、Agent、内容日历、数据表。 | 把数据统一到一张增长仪表盘。 |
| 势 | AI 搜索、内容平台电商、APP 商店实验、知识产品化、Agent 服务正在同时成熟。 | 做“可搜索、可转化、可复用、可订阅”的产品，而不只是一次性内容。 |

## 下一步 `/goal`

```text
/goal 围绕“为小伟选择一个可验证的 AI 产品方向并设计获客闭环”执行三阶段研究工作流。
阶段 1 - 广域调研：检索 25 个来源，覆盖小红书/抖音/知乎/Reddit/YouTube/Google 搜索、直接竞品、App Store/Google Play 评论、价格页、内容爆款、官方 SEO 与应用商店资料。
阶段 2 - Deep Research：筛选 10 个高价值来源深读，提取用户原话、痛点聚类、付费证据、竞品结构、内容打法、商店页策略、风险和证据强度。
阶段 3 - 业务应用：输出 3 个候选产品方向、每个方向的 MVP、首批 20 个内容选题、官网结构、APP 商店页实验、增长指标和 14 天验证计划。
验证方式：每个方向必须有真实用户原话、现有付费证据和可触达渠道；事实、推断、建议分开写。
限制：不复制竞品文案、素材、代码、课程；不做低质量外链堆砌；所有 AI 生成内容必须人工审核。
```

## 资料链接

- [Google Search Central: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central: Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)
- [Adsy: Digital PR & Blog Guest Posting Service](https://adsy.com/)
- [Apple Product Page Optimization](https://developer.apple.com/app-store/product-page-optimization/)
- [Apple Custom Product Pages](https://developer.apple.com/app-store/custom-product-pages/)
- [Apple Ads Campaign Structure](https://ads.apple.com/app-store/best-practices/campaign-structure)
- [Google Play Acquisition Reporting](https://play.google.com/console/about/acquisitionreporting/)
- [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
