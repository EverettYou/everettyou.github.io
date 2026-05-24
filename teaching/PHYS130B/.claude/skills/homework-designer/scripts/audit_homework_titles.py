#!/usr/bin/env python3
"""
Audit consistency between problem titles in `homework.md` (index) and the
matching `*_solutions.md` files. Exits non-zero on drift.

  python3 .claude/skills/homework-designer/scripts/audit_homework_titles.py
"""

from __future__ import annotations

import glob
import os
import re
import sys


def _repo_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(d, "notes_src")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    raise RuntimeError("Could not locate repo root (notes_src/)")


ROOT = _repo_root()
HW = os.path.join(ROOT, "notes_src", "homework")

SECTION_RE = re.compile(
    r"\*\*\[(\d+\.\d+\.\d+)[^\]]*\]\(([\d\-_a-z]+\.md)\)\*\*\s*\n"
    r"((?:.*\n)*?)(?=\n\*\*\[|\Z)"
)
INDEX_PROBLEM_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$", re.M)
SOLN_TITLE_RE = re.compile(r"^\*\*(\d+)\.\s+([^*\n]+?)\.\*\*", re.M)


def parse_index() -> dict[str, dict[int, str]]:
    with open(os.path.join(HW, "homework.md")) as f:
        text = f.read()
    out: dict[str, dict[int, str]] = {}
    for m in SECTION_RE.finditer(text):
        stem = m.group(2).replace(".md", "")
        block = m.group(3)
        probs: dict[int, str] = {}
        for pm in INDEX_PROBLEM_RE.finditer(block):
            title = pm.group(2).strip().replace("**", "").strip()
            probs[int(pm.group(1))] = title
        out[stem] = probs
    return out


def parse_solutions() -> dict[str, dict[int, str]]:
    out: dict[str, dict[int, str]] = {}
    for path in sorted(glob.glob(os.path.join(HW, "*_solutions.md"))):
        stem = os.path.basename(path).replace(".md", "")
        with open(path) as f:
            text = f.read()
        probs: dict[int, str] = {}
        for m in SOLN_TITLE_RE.finditer(text):
            probs[int(m.group(1))] = m.group(2).strip()
        out[stem] = probs
    return out


def main() -> int:
    idx = parse_index()
    sols = parse_solutions()
    issues: list[str] = []
    stems = sorted(set(idx) | set(sols))
    for stem in stems:
        ip = idx.get(stem, {})
        sp = sols.get(stem, {})
        if stem not in idx:
            issues.append(f"{stem}: section block missing from homework.md")
            continue
        if stem not in sols:
            issues.append(f"{stem}: solutions file missing")
            continue
        for n in sorted(set(ip) | set(sp)):
            a, b = ip.get(n), sp.get(n)
            if a is None:
                issues.append(f"{stem} #{n}: missing from homework.md index (solns={b!r})")
            elif b is None:
                issues.append(f"{stem} #{n}: missing from solutions (index={a!r})")
            elif a.lower() != b.lower():
                issues.append(f"{stem} #{n}: index={a!r} solns={b!r}")
    if issues:
        print("Title-consistency issues between homework.md and *_solutions.md:")
        for line in issues:
            print(f"  - {line}")
        print(f"\nTotal: {len(issues)} issue(s)")
        return 1
    print(f"OK: {sum(len(v) for v in idx.values())} problems consistent across {len(idx)} subsections.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
