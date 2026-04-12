"""
Homework cell checks vs .claude/rules/content-style.md § Homework Design.
Used by validate_project.py and audit_homework_format.py.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


PROBLEM_HEAD = re.compile(
    r"^\*\*(\d+)\.\s+(.+?)\.\*\*(.*)$",
    re.DOTALL,
)

DUPLICATE_TITLE_CLOSE = re.compile(r"\*\*\d+\.\s+(.+?)\.\*\*\s+\1\s*\.\*\*")


@dataclass(frozen=True)
class HomeworkFinding:
    code: str
    message: str


def check_homework_cell(text: str) -> list[HomeworkFinding]:
    """Validate homework markdown (cell body including `## Homework`)."""
    found: list[HomeworkFinding] = []
    lines = text.splitlines()
    first_nonempty = next((ln.strip() for ln in lines if ln.strip()), "")
    if first_nonempty != "## Homework":
        found.append(
            HomeworkFinding(
                "hw_heading",
                "first non-empty line must be exactly `## Homework`",
            )
        )
        return found

    problems: list[tuple[int, str, str]] = []

    for i, line in enumerate(lines, 1):
        raw = line.strip()
        if not raw.startswith("**") or not re.match(r"^\*\*\d+\.", raw):
            continue

        dup = DUPLICATE_TITLE_CLOSE.search(raw)
        if dup:
            found.append(
                HomeworkFinding(
                    "hw_duplicate_title",
                    f"line {i}: duplicated title fragment (`Title.** Title.**` corruption)",
                )
            )

        m = PROBLEM_HEAD.match(raw)
        if not m:
            found.append(
                HomeworkFinding(
                    "hw_problem_parse",
                    f"line {i}: cannot parse `**N. Title.**` (missing `.**` or `**`/math inside title)",
                )
            )
            continue

        _num_s, title, task = m.group(1), m.group(2).strip(), m.group(3).strip()
        problems.append((i, title, raw))

        if re.search(r"\*\*\d+\.\s+", raw[2:]):
            found.append(
                HomeworkFinding(
                    "hw_duplicate_header",
                    f"line {i}: second `**N.` on same line",
                )
            )

        if "**" in title:
            found.append(
                HomeworkFinding(
                    "hw_title_bold",
                    f"line {i}: no `**` inside title; title starts: {title[:65]!r}",
                )
            )

        if "$" in title or "\\" in title:
            found.append(
                HomeworkFinding(
                    "hw_title_latex",
                    f"line {i}: ASCII-only title; move math to task; title starts: {title[:55]!r}",
                )
            )

        tw = title.split()
        if len(tw) < 1:
            found.append(
                HomeworkFinding(
                    "hw_title_short",
                    f"line {i}: missing title words after `**N.`",
                )
            )
        elif len(tw) > 5:
            found.append(
                HomeworkFinding(
                    "hw_title_long",
                    f"line {i}: title has {len(tw)} words (guideline 1–5)",
                )
            )

        if title and title[0].isalpha() and not title[0].isupper():
            found.append(
                HomeworkFinding(
                    "hw_title_case",
                    f"line {i}: capitalize first word of title",
                )
            )

        if not task.strip():
            found.append(HomeworkFinding("hw_empty_task", f"line {i}: no task after bold title"))

        if raw.count("**") % 2 != 0 and not dup:
            found.append(
                HomeworkFinding(
                    "hw_odd_bold",
                    f"line {i}: odd number of `**` (unbalanced bold)",
                )
            )

    if not problems:
        found.append(HomeworkFinding("hw_no_problems", "no lines matching `**N.` problem format"))

    nums: list[int] = []
    for i, line in enumerate(lines, 1):
        raw = line.strip()
        m0 = re.match(r"^\*\*(\d+)\.", raw)
        if m0:
            nums.append(int(m0.group(1)))
    for j, n in enumerate(nums, start=1):
        if n != j:
            found.append(
                HomeworkFinding(
                    "hw_numbering",
                    f"expected homework problem {j}, found {n}",
                )
            )
            break

    return found
