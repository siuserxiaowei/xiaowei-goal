#!/usr/bin/env python3
"""Validate Xiaowei-style goal drafts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_DIRECT = {
    "command": [r"^/goal\s+.+"],
    "verification": [r"^验证方式[:：]\s*"],
    "limits": [r"^限制[:：]\s*"],
    "boundary": [r"^工作边界[:：]\s*"],
    "progress": [r"^推进规则[:：]\s*"],
    "stop": [r"^停止标准[:：]\s*"],
    "pause": [r"^暂停条件[:：]\s*"],
}

RESEARCH_FIELDS = {
    "stage 1 broad research": [r"^阶段\s*1\s*-\s*广域调研[:：]\s*"],
    "stage 2 deep research": [r"^阶段\s*2\s*-\s*Deep Research[:：]\s*"],
    "stage 3 business application": [r"^阶段\s*3\s*-\s*业务应用[:：]\s*"],
    "deliverable": [r"^输出物[:：]\s*"],
}

PLACEHOLDERS = [
    r"\[[^\]]+\]",
    r"\bTODO\b",
    r"\bTBD\b",
    r"待定",
    r"待补充",
    r"<[^>]+>",
]

BAD_PHRASES = [
    r"随便搜",
    r"随便改",
    r"全网都搜",
    r"一直试",
    r"直到满意",
    r"看起来可以",
    r"感觉可以",
    r"照抄",
    r"扒下来",
    r"做一个一样的",
    r"make sure it works",
    r"keep trying",
    r"edit anything",
]

EVIDENCE_HINTS = [
    r"来源",
    r"URL",
    r"检索日期",
    r"命令",
    r"日志",
    r"截图",
    r"产物",
    r"运行",
    r"测试",
    r"检查",
    r"证据",
    r"\b(test|build|lint|log|screenshot|source|url|evidence)\b",
]


def _line_starts(text: str, patterns: list[str]) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for pattern in patterns:
        matches.extend(re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE))
    return sorted(matches, key=lambda match: match.start())


def _field_content(text: str, patterns: list[str], all_markers: list[re.Match[str]]) -> str | None:
    starts = _line_starts(text, patterns)
    if not starts:
        return None

    start = starts[0]
    next_markers = [marker for marker in all_markers if marker.start() > start.start()]
    end = next_markers[0].start() if next_markers else len(text)
    line = text[start.start() : end]
    return re.sub(patterns[0], "", line, count=1, flags=re.IGNORECASE | re.MULTILINE).strip()


def lint_text(text: str, source: str) -> list[str]:
    errors: list[str] = []
    marker_patterns = [pattern for patterns in (list(REQUIRED_DIRECT.values()) + list(RESEARCH_FIELDS.values())) for pattern in patterns]
    all_markers = _line_starts(text, marker_patterns)

    if re.search(r"^\s*/目标\b", text, flags=re.MULTILINE):
        errors.append(f"{source}: use `/goal`, not `/目标`")

    for name, patterns in REQUIRED_DIRECT.items():
        if not _line_starts(text, patterns):
            errors.append(f"{source}: missing required field `{name}`")

    is_research_goal = bool(re.search(r"联网研究|广域调研|Deep Research|业务应用|Agent Reach|竞品|来源|检索", text, flags=re.IGNORECASE))
    if is_research_goal:
        for name, patterns in RESEARCH_FIELDS.items():
            if not _line_starts(text, patterns):
                errors.append(f"{source}: research goal missing `{name}`")

    for pattern in PLACEHOLDERS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"{source}: unresolved placeholder matched `{pattern}`")

    for pattern in BAD_PHRASES:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"{source}: unsafe vague phrase matched `{pattern}`")

    goal_line = next((line.strip() for line in text.splitlines() if line.strip().startswith("/goal")), "")
    if goal_line and len(goal_line.removeprefix("/goal").strip()) < 20:
        errors.append(f"{source}: /goal outcome is too short")

    verification = _field_content(text, REQUIRED_DIRECT["verification"], all_markers)
    if verification is not None and len(verification) < 16:
        errors.append(f"{source}: verification is too thin")
    if verification and not any(re.search(pattern, verification, flags=re.IGNORECASE) for pattern in EVIDENCE_HINTS):
        errors.append(f"{source}: verification should name concrete evidence")

    for name, patterns in REQUIRED_DIRECT.items():
        if name == "command":
            continue
        content = _field_content(text, patterns, all_markers)
        if content is not None and len(content) < 10:
            errors.append(f"{source}: `{name}` content is too thin")

    if is_research_goal:
        for name, patterns in RESEARCH_FIELDS.items():
            content = _field_content(text, patterns, all_markers)
            if content is not None and len(content) < 16:
                errors.append(f"{source}: `{name}` content is too thin")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: validate_xiaowei_goal.py <file> [<file> ...]", file=sys.stderr)
        return 2

    errors: list[str] = []
    for raw_path in argv[1:]:
        path = Path(raw_path)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path}: cannot read file: {exc}")
            continue
        errors.extend(lint_text(text, str(path)))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Xiaowei goal validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
