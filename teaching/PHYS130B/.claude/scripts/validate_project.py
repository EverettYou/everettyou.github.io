#!/usr/bin/env python3
"""
Unified validation for PHYS130B notebooks and rule docs.

Examples:
  python3 .claude/scripts/validate_project.py
  python3 .claude/scripts/validate_project.py --scope ch2
  python3 .claude/scripts/validate_project.py --scope 2-1-1-tensor-product
  python3 .claude/scripts/validate_project.py --docs-only
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")
RULES_PATH = os.path.join(ROOT, ".claude", "rules", "physics-conventions.md")
DESIGN_PATH = os.path.join(ROOT, ".claude", "design.md")


@dataclass
class Issue:
    location: str
    message: str


def is_build_path(path: str) -> bool:
    return "/_build/" in path.replace("\\", "/")


def iter_notebooks(scope: str | None) -> Iterable[str]:
    paths = sorted(glob.glob(NOTEBOOK_GLOB, recursive=True))
    paths = [p for p in paths if not is_build_path(p)]
    if not scope:
        return paths

    scope = scope.strip()
    if scope.startswith("ch"):
        return [p for p in paths if f"/{scope}_" in p.replace("\\", "/")]
    return [p for p in paths if scope in os.path.basename(p)]


def check_source_health(src: list[str], label: str) -> list[Issue]:
    issues: list[Issue] = []
    if not src:
        return issues

    short = sum(1 for s in src if len(s) <= 2)
    if len(src) > 20 and short > len(src) * 0.7:
        issues.append(Issue(label, f"char-by-char corruption suspected ({short}/{len(src)} short lines)"))

    max_len = max(len(s) for s in src)
    if max_len > 1000:
        issues.append(Issue(label, f"collapsed content suspected (max line length {max_len})"))

    missing_newline = sum(1 for s in src[:-1] if not s.endswith("\n"))
    if missing_newline:
        issues.append(Issue(label, f"missing newline terminators ({missing_newline} non-final lines)"))

    return issues


def _check_display_math_lines(lines: list[str], label: str) -> list[Issue]:
    """Check $$ blocks: blank lines outside, no blank lines inside."""
    issues: list[Issue] = []
    idx = 0
    while idx < len(lines):
        if lines[idx].strip() != "$$":
            idx += 1
            continue

        start = idx
        end = None
        for j in range(start + 1, len(lines)):
            if lines[j].strip() == "$$":
                end = j
                break

        if end is None:
            issues.append(Issue(label, "unclosed $$ display block"))
            break

        if start > 0 and lines[start - 1].strip() != "":
            issues.append(Issue(label, "$$ block missing blank line above"))
        if end < len(lines) - 1 and lines[end + 1].strip() != "":
            issues.append(Issue(label, "$$ block missing blank line below"))

        for k in range(start + 1, end):
            if lines[k].strip() == "":
                issues.append(Issue(label, "$$ block contains internal blank line"))
                break

        idx = end + 1
    return issues


def infer_notebook_kind(path: str) -> str:
    """
    subsection: x-y-z-...
    parent:     x-y-...
    other:      fallback
    """
    stem = os.path.basename(path).replace(".ipynb", "")
    parts = stem.split("-")
    if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        return "subsection"
    if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and not parts[2].isdigit():
        return "parent"
    return "other"


def validate_notebook(path: str) -> list[Issue]:
    issues: list[Issue] = []
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    kind = infer_notebook_kind(path)
    base = os.path.basename(path)

    expected_cells = {"subsection": 4, "parent": 3}.get(kind)
    if expected_cells is not None and len(cells) != expected_cells:
        issues.append(Issue(base, f"unexpected cell count: {len(cells)} (expected {expected_cells})"))

    if cells and cells[0].get("cell_type") == "markdown":
        title_text = "".join(cells[0].get("source", [])).strip().splitlines()
        first_line = title_text[0] if title_text else ""
        if kind == "subsection" and not re.match(r"^#\s+\d+\.\d+\.\d+\s+\S+", first_line):
            issues.append(Issue(base, "title format mismatch for x.y.z notebook"))
        if kind == "parent" and not re.match(r"^#\s+\d+\.\d+\s+\S+", first_line):
            issues.append(Issue(base, "title format mismatch for x.y notebook"))

    for ci, cell in enumerate(cells):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", [])
        label = f"{base}:cell{ci}"
        issues.extend(check_source_health(source, label))
        text = "".join(source)
        lines = text.splitlines()
        issues.extend(_check_display_math_lines(lines, label))

        if re.search(r"(?m)^---\s*$", text):
            issues.append(Issue(label, "contains banned horizontal rule '---'"))
        if "plt.show()" in text:
            issues.append(Issue(label, "contains plt.show(); use display(fig) + plt.close(fig)"))

    return issues


def detect_rule_flags(text: str) -> dict[str, bool]:
    t = text.lower()
    return {
        "blank_lines_outside": ("blank lines above and below" in t) or ("blank lines outside" in t),
        "no_blank_inside": ("no blank lines *within* `$$...$$`" in t)
        or ("do not put blank lines inside a `$$...$$` block" in t)
        or ("no blank lines within" in t),
        "split_required": ("always use `\\begin{split}" in t) or ("always use \\begin{split}" in t),
        "align_forbidden": ("do not use `align` or `aligned`" in t)
        or ("do not use align or aligned" in t),
    }


def validate_rule_docs() -> list[Issue]:
    issues: list[Issue] = []
    for p in (RULES_PATH, DESIGN_PATH):
        if not os.path.exists(p):
            issues.append(Issue(".claude docs", f"missing required file: {os.path.relpath(p, ROOT)}"))
            return issues

    with open(RULES_PATH, encoding="utf-8") as f:
        rules_text = f.read()
    with open(DESIGN_PATH, encoding="utf-8") as f:
        design_text = f.read()

    rules_flags = detect_rule_flags(rules_text)
    design_flags = detect_rule_flags(design_text)

    for key in ("blank_lines_outside", "no_blank_inside", "split_required", "align_forbidden"):
        if not rules_flags[key]:
            issues.append(Issue("rules/physics-conventions.md", f"missing rule signal: {key}"))
        if not design_flags[key]:
            issues.append(Issue("design.md", f"missing rule signal: {key}"))
        if rules_flags[key] != design_flags[key]:
            issues.append(Issue(".claude docs", f"rule mismatch between docs: {key}"))

    return issues


def print_issues(issues: list[Issue]) -> None:
    if not issues:
        return
    grouped: dict[str, list[str]] = {}
    for issue in issues:
        grouped.setdefault(issue.location, []).append(issue.message)

    for loc in sorted(grouped.keys()):
        print(f"\n{loc}")
        for msg in grouped[loc]:
            print(f"  - {msg}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Unified PHYS130B validator")
    parser.add_argument("--scope", default=None, help="Notebook scope: e.g. ch2 or 2-1-1-tensor-product")
    parser.add_argument("--docs-only", action="store_true", help="Validate only .claude rule/design docs")
    parser.add_argument("--notebooks-only", action="store_true", help="Validate only notebooks")
    args = parser.parse_args()

    if args.docs_only and args.notebooks_only:
        print("ERROR: --docs-only and --notebooks-only are mutually exclusive.")
        return 2

    all_issues: list[Issue] = []
    notebook_count = 0

    if not args.docs_only:
        notebooks = list(iter_notebooks(args.scope))
        notebook_count = len(notebooks)
        for path in notebooks:
            all_issues.extend(validate_notebook(path))

    if not args.notebooks_only:
        all_issues.extend(validate_rule_docs())

    print("=" * 60)
    if not args.docs_only:
        print(f"Notebooks checked: {notebook_count}")
    if not args.notebooks_only:
        print("Rule docs checked: .claude/rules/physics-conventions.md, .claude/design.md")

    if all_issues:
        print(f"Total issues: {len(all_issues)}")
        print_issues(all_issues)
        return 1

    print("All validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
