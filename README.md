# xiaowei-goal

`xiaowei-goal` 是一个面向 App、网站、落地页、SaaS、SEO、增长和竞品分析的 Agent Skill。

它的核心目标不是让 agent 立刻动手写代码，而是先把模糊业务需求变成一个 **先调研、再 Deep Research、最后应用到业务** 的 `/goal`。

一句话：

> 先看外部世界，再深度研究证据，最后把资料变成自己的业务动作。

## 适合什么场景

适合：

- 我要做一个 App，先研究竞品和用户评价
- 我要做一个网站或落地页，先看同行页面、文案和转化路径
- 我要做 SaaS、Chrome 插件、工具站，先找产品机会和技术参考
- 我要做 SEO、增长、内容选题，先研究搜索结果和用户语言
- 我要让 agent 用 Agent Reach 或其他联网工具搜资料，再应用到我的业务
- 我要把一句模糊需求改成可执行、可验证、知道什么时候停止的 `/goal`

不适合：

- 一句话翻译
- 简单改写
- 不需要联网、不需要持续执行的小任务
- 已经有清晰步骤、只需要马上跑一个命令的任务

## 安装

从 GitHub 安装：

```bash
npx skills add siuserxiaowei/xiaowei-goal
```

只查看仓库里有哪些 skill：

```bash
npx skills add siuserxiaowei/xiaowei-goal --list
```

安装后可以检查：

```bash
test -f ~/.agents/skills/xiaowei-goal/SKILL.md
```

如果你的运行环境使用其他 skills 路径，请以对应客户端的安装位置为准。

## 怎么使用

直接对 agent 说：

```text
用 xiaowei-goal 帮我写一个 goal：
我要做一个 AI 英语口语练习 App，先联网研究竞品、用户评价、小红书/B站/YouTube/公众号内容，再把结论应用到 MVP 功能和官网页面。
```

或者：

```text
用 xiaowei-goal：
我要改一个 AI 工具官网，先研究同行首页、定价页、SEO 内容和用户痛点，再给我一个可以执行的改版 goal。
```

它会优先输出一段可以复制的三阶段 `/goal`，例如：

```text
/goal 围绕 AI 英语口语练习 App 执行三阶段研究工作流：先广域联网调研，再进行 Deep Research，最后把所有有效资料应用到当前业务，形成 MVP 功能、官网页面、增长动作和下一阶段实现目标。
阶段 1 - 广域调研：优先使用 Agent Reach 或当前环境可用的搜索、浏览、平台读取工具；检索 15-25 个候选来源，覆盖直接竞品、官方资料、App 用户评价或社区讨论、小红书/B站/YouTube/公众号等内容平台、技术或实现参考；记录标题、URL、来源类型、检索日期和初步价值判断。
阶段 2 - Deep Research：从第一阶段来源池中筛选高价值来源进行深读、对比和交叉验证；提取关键事实、用户痛点、竞品策略、页面/产品结构、增长路径、技术做法、风险和证据强度；把矛盾信息标成不确定。
阶段 3 - 业务应用：把本轮收集到、去重后、与 AI 英语口语练习 App 相关且可追溯来源的资料，映射到 MVP 功能、官网页面、文案方向、SEO 主题、增长动作、技术实现、验证实验和下一阶段 `/goal`。
输出物：产出一份研究应用简报，包含来源池、深度研究证据表、业务应用表、可迁移动作、不能复制的内容、风险和下一阶段 `/goal`。
验证方式：每条关键结论必须能追溯到来源；事实、推断、建议分开写；最终动作要能对应到产品、页面、文案、SEO、增长、技术实现或验证实验。
限制：不复制竞品品牌、文案、图片、视频、代码、课程、版权素材或未经证实的市场结论；不把单一来源当成事实；不使用登录账号、付费平台、生产数据或隐私数据，除非用户明确授权。
工作边界：三阶段研究期间只创建研究应用文档和下一阶段执行目标；实现阶段只改与 AI 英语口语练习 App、官网页面或直接相关测试有关的文件。
推进规则：先列研究问题和搜索词，再做广域检索，再筛选来源做 Deep Research，最后统一映射到业务动作；每个阶段结束前先补齐证据缺口，再进入下一阶段。
停止标准：研究应用简报覆盖三阶段，包含可追溯来源、深度研究证据、业务启发、可执行动作、风险和下一阶段目标。
暂停条件：需要 Cookie、付费数据库、绕过平台限制、法律或教育合规判断、版权授权、生产数据或重大业务定位选择时暂停。
```

## 两种工作模式

### 1. 三阶段研究模式

这是默认的业务模式。适合 App、网站、SaaS、落地页、SEO、增长、竞品和产品方向。

它会要求 agent：

- 阶段 1：先做广域调研，建立来源池
- 阶段 2：再做 Deep Research，深读、对比、交叉验证高价值来源
- 阶段 3：最后做业务应用，把资料映射到产品、页面、文案、SEO、增长、技术实现和下一阶段 `/goal`
- 全程记录标题、URL、来源类型、检索日期
- 全程区分事实、推断、建议
- 不允许从搜索结果直接跳到建议，中间必须经过 Deep Research

默认广域调研来源数量：

- 轻量：6-8 个来源
- 标准：15-25 个来源
- 深度：40+ 个来源

Deep Research 不是多搜几个链接，而是从来源池里筛出高价值资料，做深读、对比、交叉验证和业务判断。

### 2. 直接执行模式

适合不需要外部信息的小范围任务，例如：

- 修一个明确 bug
- 给已有项目加一个小功能
- 改一段文档
- 跑一个本地检查

它会强调：

- 先读项目脚本和约定
- 只改相关文件
- 用命令、日志、截图或产物证明完成
- 遇到凭证、付费、生产数据、破坏性操作时暂停

## Agent Reach 怎么配合

`xiaowei-goal` 本身不直接联网。它负责生成一个更好的 `/goal`，告诉后续 agent 应该如何使用联网能力。

如果当前环境安装了 Agent Reach，生成的 goal 会优先要求使用 Agent Reach。

如果没有 Agent Reach，也可以使用当前环境可用的：

- web search
- browser
- GitHub CLI
- 官方文档
- 搜索 API
- RSS
- 平台公开接口

如果某个渠道需要 Cookie、登录、付费、代理或绕过平台限制，goal 会要求 agent 暂停并让用户决定。

## 输出会长什么样

三阶段研究任务通常包含：

```text
推荐执行版（中文，可直接复制）
/goal ...
阶段 1 - 广域调研：...
阶段 2 - Deep Research：...
阶段 3 - 业务应用：...
输出物：...
验证方式：...
限制：...
工作边界：...
推进规则：...
停止标准：...
暂停条件：...

默认选择理由：...
可选调整：...
```

最终研究应用简报通常要求包含：

```text
来源池：标题 | URL | 来源类型 | 检索日期 | 初步价值 | 是否进入 Deep Research
深度研究证据表：主题 | 关键事实 | 支撑来源 | 反例/矛盾 | 推断 | 证据强度 | 对本业务的意义
业务应用表：业务模块 | 可用资料/证据 | 业务判断 | 具体动作 | 优先级 | 验证方式 | 是否需要人工确认
```

基础证据表仍然可以使用：

```text
来源标题 | URL | 来源类型 | 日期/检索日期 | 事实 | 推断 | 可执行动作 | 置信度 | 需要人工确认？
```

这个表是整个 Skill 的重点：搜索不是为了堆资料，而是为了把外部信息转成业务动作。

## 示例

仓库内置了三个示例：

- `examples/app-research-goal.zh.txt`
- `examples/website-research-goal.zh.txt`
- `examples/practice-run-ai-website-goal.zh.txt`

你可以用本地校验脚本检查示例：

```bash
python3 scripts/validate_xiaowei_goal.py examples/app-research-goal.zh.txt examples/website-research-goal.zh.txt examples/practice-run-ai-website-goal.zh.txt
```

通过时会输出：

```text
Xiaowei goal validation passed.
```

## 目录结构

```text
xiaowei-goal/
├── SKILL.md
├── README.md
├── manifest.json
├── agents/
│   └── interface.yaml
├── examples/
│   ├── app-research-goal.zh.txt
│   └── website-research-goal.zh.txt
├── references/
│   ├── goal-contract.md
│   ├── research-workflow.md
│   └── source-map.md
└── scripts/
    └── validate_xiaowei_goal.py
```

## 设计原则

`xiaowei-goal` 的风格是：

- 业务优先，不为了形式写提示词
- 证据优先，不把猜测写成结论
- 小闭环优先，不一上来做大而全
- 边界优先，不让 agent 随便碰生产、隐私、账号、付费和版权
- 动作优先，研究必须落到产品、页面、文案、SEO、增长或实现任务

## 和乔木老师案例的关系

这个 Skill 参考了乔木老师公开的 `qiaomu-goal-meta-skill` 这个案例：它启发了“把模糊需求改写成可执行 `/goal`”这个方向。

但 `xiaowei-goal` 不是对原 Skill 的改名或换皮。它重新围绕我的使用场景设计：

- 更强调 App、网站、SaaS、SEO、增长和竞品研究
- 更强调 Agent Reach 或其他联网能力
- 更强调“事实 -> 推断 -> 可执行动作”
- 更强调广域调研、Deep Research、业务应用和下一阶段执行目标
- 重新编写了 `SKILL.md`、reference、示例和校验脚本

保留致谢，是为了尊重启发来源；重新设计，是为了服务我自己的业务工作流。

## License

MIT

Copyright (c) 2026 Xiaowei
