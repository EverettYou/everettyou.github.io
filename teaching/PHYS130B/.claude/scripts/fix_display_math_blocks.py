#!/usr/bin/env python3
"""
Normalize $$ display math in markdown cells: no blank lines inside blocks;
blank lines immediately above and below each block. Uses the same fence
rules as validate_project.py.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")

# Import fence helpers from validator (single source of truth)
sys.path.insert(0, os.path.dirname(__file__))
from validate_project import _is_display_math_close, _is_display_math_open  # noqa: E402


def fix_display_math_lines(lines: list[str]) -> tuple[list[str], bool]:
    changed = False
    out = list(lines)
    i = 0
    while i < len(out):
        if not _is_display_math_open(out[i]):
            i += 1
            continue
        start = i
        end = None
        for j in range(start + 1, len(out)):
            if _is_display_math_close(out[j]):
                end = j
                break
        if end is None:
            i += 1
            continue

        # Drop internal empty lines
        k = start + 1
        while k < end:
            if out[k].strip() == "":
                del out[k]
                end -= 1
                changed = True
            else:
                k += 1

        # Blank line above opening $$
        if start > 0 and out[start - 1].strip() != "":
            out.insert(start, "")
            end += 1
            start += 1
            changed = True

        # Blank line below closing $$ / $$ (label)
        if end < len(out) - 1 and out[end + 1].strip() != "":
            out.insert(end + 1, "")
            changed = True

        i = end + 2

    return out, changed


def text_to_source_lines(text: str) -> list[str]:
    """Split cell text into Jupyter `source` lines (each ends with ``\\n``)."""
    if not text:
        return []
    parts = text.splitlines(keepends=True)
    out: list[str] = []
    for p in parts:
        if not p.endswith("\n"):
            p = p + "\n"
        out.append(p)
    return out


def process_notebook(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)

    file_changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", [])
        if not source:
            continue
        text = "".join(source)
        ends_nl = text.endswith("\n")
        lines = text.splitlines()
        new_lines, changed = fix_display_math_lines(lines)
        if not changed:
            continue
        new_text = "\n".join(new_lines)
        if ends_nl and not new_text.endswith("\n"):
            new_text += "\n"
        elif not ends_nl and new_text.endswith("\n"):
            new_text = new_text.rstrip("\n")
        cell["source"] = text_to_source_lines(new_text)
        file_changed = True

    if file_changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
            f.write("\n")
    return file_changed


def main() -> int:
    import glob

    paths = sorted(glob.glob(NOTEBOOK_GLOB, recursive=True))
    paths = [p for p in paths if "/_build/" not in p.replace("\\", "/")]
    n = 0
    for p in paths:
        if process_notebook(p):
            print("updated", os.path.relpath(p, ROOT))
            n += 1
    print(f"Done. {n} notebook(s) modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
