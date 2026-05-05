#!/usr/bin/env python3
"""Remove Summary lines that duplicate See Also link bullets (- [Title](ref): ...).

PHYS130B: fixes plain-markdown link bullets missed by the earlier **- **[** heuristic.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LINK_BULLET = re.compile(
    r"^\s*-\s+\[[^\]]+\]\([^)]+\)\s*:\s*"
)
BOLD_LINK_BULLET = re.compile(
    r"^\s*-\s+\*\*\[[^\]]+\]\([^)]+\)\*\*\s*:\s*"
)
SEE_ALSO_START = re.compile(r"(?m)^:::\{admonition\}\s+See Also\s*$")
# Do not use \s* before $ — \s matches newlines and would consume blank lines after the heading.
SUMMARY_HDR = re.compile(r"(?m)^###\s+Summary$")


def _repo_root() -> Path:
    for d in Path(__file__).resolve().parents:
        if (d / "notes_src").is_dir():
            return d
    raise RuntimeError("Could not locate repo root (notes_src/)")


def text_to_source(text: str) -> list[str]:
    lines = text.split("\n")
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + "\n")
        else:
            if line:
                source.append(line)
    return source


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def lecture_cell_index(nb: dict) -> int | None:
    for i, c in enumerate(nb.get("cells", [])):
        if c.get("cell_type") != "markdown":
            continue
        src = c.get("source", [])
        if not isinstance(src, list):
            continue
        t = "".join(src)
        if "## Lecture Notes" in t and "### Summary" in t:
            return i
    return None


def extract_seealso_block(text: str, block_start: int) -> str | None:
    """Return full See Also admonition from byte offset of opening `:::`."""
    if not SEE_ALSO_START.match(text, block_start):
        return None
    chunk = text[block_start:]
    lines = chunk.split("\n")
    for j in range(1, len(lines)):
        if lines[j].strip() == ":::":
            return "\n".join(lines[: j + 1])
    return None


def link_bullets_in_block(block: str) -> set[str]:
    out: set[str] = set()
    for ln in block.split("\n"):
        if LINK_BULLET.match(ln) and not BOLD_LINK_BULLET.match(ln):
            out.add(norm(ln))
    return out


def strip_duplicate_summary_links(text: str) -> tuple[str, int]:
    """Return (new_text, num_removed)."""
    sm = SUMMARY_HDR.search(text)
    if not sm:
        return text, 0
    msee = SEE_ALSO_START.search(text, sm.end())
    if not msee:
        return text, 0
    see_block = extract_seealso_block(text, msee.start())
    if not see_block:
        return text, 0
    see_set = link_bullets_in_block(see_block)
    if not see_set:
        return text, 0

    summary_body = text[sm.end() : msee.start()]
    removed = 0
    new_lines: list[str] = []
    for ln in summary_body.split("\n"):
        if LINK_BULLET.match(ln) and not BOLD_LINK_BULLET.match(ln):
            if norm(ln) in see_set:
                removed += 1
                continue
        new_lines.append(ln)
    while new_lines and new_lines[-1].strip() == "":
        new_lines.pop()
    while new_lines and new_lines[0].strip() == "":
        new_lines.pop(0)
    new_body = "\n".join(new_lines)
    if new_body:
        # Match corpus: blank line after `### Summary` heading (head ends before that line's `\n`).
        new_body = "\n\n" + new_body + "\n"
    else:
        new_body = "\n"

    new_text = text[: sm.end()] + new_body + text[msee.start() :]
    if new_text == text:
        return text, 0
    return new_text, removed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "paths",
        nargs="*",
        help="Notebook paths (default: known affected set)",
    )
    args = ap.parse_args()
    default = [
        "notes_src/ch5_perturbation-theory/5-1-1-toy-model.ipynb",
        "notes_src/ch5_perturbation-theory/5-1-2-non-degenerate-perturbation-theory.ipynb",
        "notes_src/ch5_perturbation-theory/5-1-3-degenerate-perturbation-theory.ipynb",
        "notes_src/ch5_perturbation-theory/5-2-2-fermis-golden-rule.ipynb",
        "notes_src/ch6_quantum-foundations/6-2-3-bell-inequality.ipynb",
    ]
    paths = [Path(p) for p in (args.paths or default)]
    root = _repo_root()
    total_removed = 0
    for rel in paths:
        p = rel if rel.is_absolute() else root / rel
        nb = json.loads(p.read_text(encoding="utf-8"))
        li = lecture_cell_index(nb)
        if li is None:
            print("skip no lecture", p)
            continue
        text = "".join(nb["cells"][li]["source"])
        new_text, n = strip_duplicate_summary_links(text)
        if new_text != text:
            nb["cells"][li]["source"] = text_to_source(new_text)
            p.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
            print(f"{p.relative_to(root)} removed_links={n}")
            total_removed += n
        else:
            print(f"{p.relative_to(root)} no change")
    print("total_removed", total_removed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
