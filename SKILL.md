---
name: xiaowei-goal
description: >
  Convert app, website, SaaS, landing page, content, SEO, growth, competitor,
  product, or vague business tasks into Xiaowei-style executable `/goal`
  commands. Use when the user wants to search first, learn from the internet,
  use Agent Reach, do competitor research, build an app/site after research,
  turn a rough idea into an agent task, or define evidence-based success
  criteria. Triggers include 小伟 goal, xiaowei-goal, 联网调研, 先搜索再做,
  Agent Research, Agent Reach, 竞品分析, 网站方案, App MVP, 增长方案, SEO 方案,
  and 把需求写成可执行 goal.
---

# Xiaowei Goal

把一句模糊的业务想法，改写成可以交给 agent 持续执行、能联网研究、能落到业务动作、能验收结果的 `/goal`。

核心风格：

- 先看外部世界，再决定怎么做。
- 先分清事实和判断，再给执行动作。
- 先做一个能跑通的小闭环，再扩展功能。
- 重要结论必须有来源；没有证据就标成假设。
- 不复制竞品，只提炼可迁移的结构、路径和判断。

## Default Mode

Use Chinese output by default for Chinese users. Keep the slash command as `/goal`.

Choose one of two modes:

1. **研究优先模式**：default for app, website, landing page, SaaS, SEO, growth, competitor, content, market, and product direction tasks.
2. **直接执行模式**：use for narrow local coding/doc tasks where external information is unnecessary.

If the user mentions Agent Reach, search, research, competitor analysis, app/site planning, SEO, growth, or "先学习再应用", choose 研究优先模式.

## Workflow

1. Restate the user's real outcome in business terms.
2. Decide whether the task needs external research.
3. If research is needed, read `references/research-workflow.md`.
4. If the user names an app/site/business channel, read `references/source-map.md`.
5. If the task is ready for execution, read `references/goal-contract.md`.
6. Produce the best copy-ready `/goal` first.
7. Add a short reason for the defaults.
8. Add compact options only when a choice changes cost, risk, or direction.
9. If writing an output file, run `python3 scripts/validate_xiaowei_goal.py <file>`.

## Research-First Output

Use this shape when the task should search first:

```text
推荐执行版（中文，可直接复制）
/goal 先围绕[业务任务]做一轮[轻量/标准/深度]联网研究，再把可迁移的信息整理成业务判断、执行动作和下一阶段实现目标。
研究要求：优先使用 Agent Reach 或当前环境可用的搜索、浏览、平台读取工具；检索并阅读[数量]个高相关来源，覆盖直接竞品、官方资料、用户评价或社区讨论、内容平台、技术/实现参考；每条关键结论记录标题、URL、来源类型和检索日期。
输出物：产出一份研究简报，包含来源清单、关键事实、用户痛点、竞品做法、可迁移动作、不能复制的内容、风险和下一阶段 `/goal`。
验证方式：关键结论必须能追溯到来源；事实、推断、建议分开写；最终动作要能对应到产品、页面、文案、SEO、增长、技术实现或验证实验。
限制：不复制竞品品牌、文案、图片、视频、代码、课程、版权素材或未经证实的市场结论；不把单一来源当成事实；不使用登录账号、付费平台、生产数据或隐私数据，除非用户明确授权。
工作边界：研究阶段只创建研究文档和下一阶段执行目标；实现阶段只改与当前业务目标直接相关的文件。
推进规则：先列研究问题和搜索词，再分渠道检索；优先一手来源和高相关来源；遇到矛盾信息时标注不确定；研究完成后再进入实现。
停止标准：研究简报达到所选深度，包含可追溯来源、业务启发、可执行动作和下一阶段目标。
暂停条件：需要 Cookie、付费数据库、绕过平台限制、法律/医疗/金融判断、版权授权、生产数据或重大业务定位选择时暂停。
```

Default source counts:

- 轻量：6-8 个来源
- 标准：15-25 个来源
- 深度：40+ 个来源

## Direct Execution Output

Use this shape when research is unnecessary:

```text
推荐执行版（中文，可直接复制）
/goal 基于当前项目上下文完成[具体结果]，先读取已有文档、脚本和约定，再做最小必要改动。
验证方式：运行项目中最小相关检查；如果是前端或交互任务，启动本地服务并走通核心流程；用命令输出、日志、截图或产物路径证明完成。
限制：不改无关功能、公开接口、数据结构、生产配置、凭证或用户数据；不加入用户没有要求的账号、支付、部署或复杂功能。
工作边界：只修改与本次目标直接相关的文件、测试和文档。
推进规则：一次只做一个聚焦改动；每次有意义改动后重跑检查；失败时先读错误、日志或文档，再调整方案。
停止标准：核心结果被运行证据证明可用，相关检查通过，或缺少配置时明确说明无法继续的原因。
暂停条件：需要凭证、付费服务、生产数据、破坏性操作、法律/医疗/金融判断、版权素材或产品方向决策时暂停。
```

## Response Contract

For Chinese users, output:

1. `推荐执行版（中文，可直接复制）`
2. `默认选择理由`
3. `可选调整`
4. `Goal Draft (English-compatible)` only when useful for cross-tool compatibility or when the user asks for it

Do not lead with a blank template. Do not leave placeholders. Do not start implementation unless the user explicitly asks to execute the generated goal.

## Quality Rules

Good goals:

- describe an outcome, not activity
- name source count or verification commands
- protect unrelated files, secrets, production data, and copyrighted material
- separate facts, inferences, and actions
- define where work may happen
- define how to retry after failures
- define when to stop and when to pause

Bad goals:

- "帮我做得更好"
- "随便搜一下"
- "一直试直到满意"
- "看起来可以就行"
- "全网资料都整理一下" without depth or source rules
- "照着竞品做一个一样的"

## References

- `references/research-workflow.md`: research-first method, source depth, evidence table, and business application rules.
- `references/source-map.md`: platform routing and query patterns for app, website, SEO, growth, and technical tasks.
- `references/goal-contract.md`: compact templates for executable goals and validation rules.
- `scripts/validate_xiaowei_goal.py`: local validator for generated goal examples.
