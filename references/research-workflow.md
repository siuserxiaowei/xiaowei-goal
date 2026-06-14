# Research Workflow

Use this reference when the user wants an app, website, landing page, SaaS,
content plan, SEO plan, growth idea, competitor scan, or product strategy that
should learn from external sources before implementation.

The default business workflow has three required stages:

1. Broad Research: build the source pool and map the landscape.
2. Deep Research: read, compare, and cross-check the highest-value sources.
3. Business Application: convert evidence into actions for the user's business.

## Research Depth

Choose the smallest broad-research depth that can support the decision.

| Depth | Sources | Use case |
|---|---:|---|
| 轻量 | 6-8 | fast MVP direction, early idea, low-risk page change |
| 标准 | 15-25 | app/site planning, landing page, competitor scan, product scope |
| 深度 | 40+ | strategic market map, pricing, SEO cluster, investment of serious build time |

Default to 标准 for app/site/business tasks.

## Stage 1: Broad Research

Goal: gather enough external context to avoid working from guesses.

Require the agent to:

- list research questions before searching
- generate search terms in Chinese and English when useful
- collect a source pool at the selected depth
- cover direct competitors, adjacent products, official sources, user discussions, content platforms, technical references, and risk references when relevant
- record title, URL, source type, retrieval date, short note, and initial relevance

Stage 1 output:

```text
来源池：标题 | URL | 来源类型 | 检索日期 | 初步价值 | 是否进入 Deep Research
```

## Stage 2: Deep Research

Goal: go beyond "collected links" and produce evidence-backed judgment.

Deep Research should focus on the highest-value sources from Stage 1. It should:

- read the selected sources closely
- compare competitors and adjacent products
- cross-check claims across multiple sources
- extract user pain, purchase triggers, objections, product patterns, page patterns, growth channels, SEO topics, technical patterns, and risks
- mark contradictions and weak evidence
- avoid copying language, designs, media, code, or protected material

Stage 2 output:

```text
深度研究证据表：主题 | 关键事实 | 支撑来源 | 反例/矛盾 | 推断 | 证据强度 | 对本业务的意义
```

## Stage 3: Business Application

Goal: apply all relevant, deduplicated, source-backed information to the user's current business.

Do not merely summarize research. Convert it into:

- product scope
- MVP feature list
- page structure
- copy direction
- SEO content topics
- growth actions
- technical implementation suggestions
- validation experiments
- risk controls
- next-stage executable `/goal`

Stage 3 output:

```text
业务应用表：业务模块 | 可用资料/证据 | 业务判断 | 具体动作 | 优先级 | 验证方式 | 是否需要人工确认
```

## Evidence Table

Require this table in the final research application brief:

```text
来源标题 | URL | 来源类型 | 日期/检索日期 | 事实 | 推断 | 可执行动作 | 置信度 | 需要人工确认？
```

Rules:

- `事实` must be directly visible in the source.
- `推断` explains what the fact may mean for the user's business.
- `可执行动作` must map to a product, page, copy, SEO, growth, technical, or validation action.
- `置信度` should be high, medium, or low.
- Mark contradictions instead of smoothing them over.

## Business Translation

Convert Deep Research into decisions:

1. What pattern can be borrowed safely?
2. What should not be copied?
3. What should be built first?
4. What should wait?
5. What claim needs stronger proof?
6. What metric or user behavior should validate the next step?
7. What should the next `/goal` be?

All relevant material collected in the current run should be used or explicitly discarded. If a source is discarded, give a short reason such as duplicate, low relevance, weak evidence, inaccessible, promotional, or outdated.

## App Checklist

For app tasks, map findings to:

- first-run experience
- core workflow
- activation moment
- habit or retention loop
- pricing or monetization
- app store listing, screenshots, and review themes
- support, privacy, or trust risks

## Website Checklist

For website tasks, map findings to:

- first viewport message
- navigation
- page sections
- CTA path
- proof points
- pricing or lead capture
- SEO topics
- analytics or experiment plan

## Guardrails

Do not allow research goals to:

- copy competitor content, brand, visual assets, code, or paid material
- use one source as market truth
- hide weak evidence behind confident language
- request cookies, paid access, scraping bypasses, or private data without explicit permission
- start implementation before a research brief exists, unless the user explicitly asks for direct execution
- skip Deep Research and jump from search results directly to recommendations
- claim "all internet information" was covered; use "all collected, deduplicated, relevant, source-backed material from this run"
