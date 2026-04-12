#!/usr/bin/env python3
"""
Homework audit CLI (subsection notebooks, cell 3). Same rules as validate_project homework checks.

  python3 .claude/scripts/audit_homework_format.py
"""

from __future__ import annotations

import glob
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from homework_format import check_homework_cell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")


def infer_subsection(path: str) -> bool:
    stem = os.path.basename(path).replace(".ipynb", "")
    parts = stem.split("-")
    return (
        len(parts) >= 3
        and parts[0].isdigit()
        and parts[1].isdigit()
        and parts[2].isdigit()
    )


def main() -> int:
    paths = sorted(glob.glob(NOTEBOOK_GLOB, recursive=True))
    paths = [p for p in paths if "/_build/" not in p.replace("\\", "/") and infer_subsection(p)]

    all_rows: list[tuple[str, str, str]] = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            nb = json.load(f)
        cells = nb.get("cells", [])
        if len(cells) != 4:
            continue
        c3 = cells[3]
        if c3.get("cell_type") != "markdown":
            all_rows.append((p, "hw_cell", "cell 3 is not markdown"))
            continue
        text = "".join(c3.get("source", []))
        base = os.path.relpath(p, ROOT)
        for fnd in check_homework_cell(text):
            all_rows.append((p, fnd.code, fnd.message))

    if not all_rows:
        print(f"Homework format audit: {len(paths)} subsection notebooks — no issues found.")
        return 0

    print(f"Homework format audit: {len(paths)} subsection notebooks, {len(all_rows)} issue(s)\n")
    by_code: dict[str, int] = {}
    for _p, code, _msg in all_rows:
        by_code[code] = by_code.get(code, 0) + 1
    print("By code:", dict(sorted(by_code.items(), key=lambda x: -x[1])))
    print()
    for p, code, msg in all_rows:
        print(f"{os.path.relpath(p, ROOT)} [{code}] {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
