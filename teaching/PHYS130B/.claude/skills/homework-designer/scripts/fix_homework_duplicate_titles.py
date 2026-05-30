#!/usr/bin/env python3
"""Remove exact `Title.** Title.**` duplicates and known broken lines in homework cells."""

from __future__ import annotations

import json
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

DUP = re.compile(r"\*\*(\d+)\.\s+(.+?)\.\*\*\s+\2\s*\.\*\*\s*")


def infer_subsection(path: str) -> bool:
    stem = os.path.basename(path).replace(".ipynb", "")
    parts = stem.split("-")
    return (
        len(parts) >= 3
        and parts[0].isdigit()
        and parts[1].isdigit()
        and parts[2].isdigit()
    )


def text_to_source_lines(text: str) -> list[str]:
    if not text:
        return []
    lines = text.split("\n")
    out: list[str] = []
    for i, ln in enumerate(lines):
        if i < len(lines) - 1:
            out.append(ln + "\n")
        else:
            if ln:
                out.append(ln)
    return out


def fix_text(text: str) -> str:
    prev = None
    while prev != text:
        prev = text
        text = DUP.sub(r"**\1. \2.** ", text)
    text = text.replace(
        "**2. Pure vs. Mixed States.** Pure vs.** Mixed States.",
        "**2. Pure vs. Mixed States.**",
    )
    return text


def main() -> int:
    changed = 0
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "notes_src")):
        if "_build" in dirpath:
            continue
        for fn in files:
            if not fn.endswith(".ipynb"):
                continue
            path = os.path.join(dirpath, fn)
            if not infer_subsection(path):
                continue
            with open(path, encoding="utf-8") as f:
                nb = json.load(f)
            cells = nb.get("cells", [])
            if len(cells) != 4:
                continue
            c3 = cells[3]
            if c3.get("cell_type") != "markdown":
                continue
            old = "".join(c3.get("source", []))
            if "## Homework" not in old:
                continue
            new = fix_text(old)
            if new != old:
                c3["source"] = text_to_source_lines(new)
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(nb, f, ensure_ascii=False, indent=1)
                changed += 1
                print("updated", os.path.relpath(path, ROOT))
    print(f"done, {changed} notebooks modified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
