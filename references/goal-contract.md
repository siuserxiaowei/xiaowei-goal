# Goal Contract

Use this reference for final goal wording.

## Required Fields

A Xiaowei goal should include:

- `/goal` line with one clear outcome
- `研究要求` when external research is needed
- `输出物` when a document or brief is expected
- `验证方式`
- `限制`
- `工作边界`
- `推进规则`
- `停止标准`
- `暂停条件`

For direct execution goals, `研究要求` and `输出物` may be omitted if not relevant.

## Research-First Template

```text
/goal 先围绕[业务任务]做一轮[轻量/标准/深度]联网研究，再把可迁移的信息整理成业务判断、执行动作和下一阶段实现目标。
研究要求：[工具优先级、来源数量、来源类型、记录字段]。
输出物：[研究简报、证据表、业务动作、下一阶段目标]。
验证方式：[来源可追溯、事实/推断/建议分开、动作可执行]。
限制：[不复制、不编造、不碰隐私/付费/生产]。
工作边界：[研究阶段和实现阶段各自允许写什么]。
推进规则：[先问题和搜索词，再分渠道搜索，再整理，再生成下一目标]。
停止标准：[达到深度、证据完整、下一目标清楚]。
暂停条件：[账号、付费、绕过限制、合规、版权、生产数据、方向决策]。
```

## Direct Execution Template

```text
/goal 基于当前项目上下文完成[具体结果]，先读取已有文档、脚本和约定，再做最小必要改动。
验证方式：[命令、日志、截图、产物、核心流程]。
限制：[不能改变的行为、接口、数据、配置、凭证、范围]。
工作边界：[允许修改的目录/文件和禁止触碰的部分]。
推进规则：[小步修改、重跑检查、基于证据调整]。
停止标准：[什么证据证明完成]。
暂停条件：[需要人工、账号、付费、生产、破坏性操作、合规或方向选择]。
```

## Default Choices

Use these defaults unless the user says otherwise:

- New app/site: research-first, standard depth, no backend/auth/payment in first goal.
- Existing repo: inspect local scripts and docs before changes.
- No deployment request: local verification only.
- No source preference: web + competitors + user communities + implementation references.
- No language preference from a Chinese user: Chinese recommended goal first.
- No authorization: do not use login-only or paid channels.

## Red Flags

Revise the goal if it contains:

- placeholders such as `[xxx]`, `TODO`, `TBD`, `待定`
- "随便搜", "全网都搜", or "一直试"
- "照抄", "扒下来", or "做一个一样的"
- no source count for research
- no verification evidence
- no pause condition
