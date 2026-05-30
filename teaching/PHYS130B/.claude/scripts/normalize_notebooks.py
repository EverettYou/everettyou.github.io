#!/usr/bin/env python3
"""Normalize PHYS130B notebooks to the canonical on-disk form.

Fixes the "editor shows notebook as modified the instant it opens" problem.
Cursor / VS Code / Jupyter parse a notebook into an in-memory model and then
re-serialize it; if the bytes on disk are not already in that canonical shape,
the editor immediately flags the file as dirty (even though `git status` shows
no change, because nothing was actually edited). This script rewrites the JSON
so disk == editor model.

It enforces three things:

  1. **No trailing newline on the last line of any cell's `source`.**
     nbformat convention: every line *except the last* carries a trailing
     "\\n"; the last line carries none. A stray final "\\n" (e.g. a cell ending
     in ":::\\n") is what the editor silently strips on open.
  2. **`nbformat_minor >= 5` whenever cells carry `id` fields.** Cell `id`s were
     introduced in nbformat 4.5; declaring minor 2/4 while cells have ids is
     invalid and forces an in-memory format upgrade (= dirty on open).
  3. **Every cell has a stable `id`** (required by nbformat 4.5).

Idempotent and safe to re-run. Only `source`, `id`, and `nbformat_minor` are
touched; cell outputs, execution counts, and metadata are left untouched.

Run from teaching/PHYS130B/:
    python3 .claude/scripts/normalize_notebooks.py            # fix in place
    python3 .claude/scripts/normalize_notebooks.py --check    # report only (exit 1 if any need fixing)
    python3 .claude/scripts/normalize_notebooks.py --scope ch2
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")

MIN_NBFORMAT_MINOR = 5


def is_build_path(path: str) -> bool:
    return "/_build/" in path.replace("\\", "/")


def iter_notebooks(scope: str | None):
    paths = sorted(glob.glob(NOTEBOOK_GLOB, recursive=True))
    paths = [p for p in paths if not is_build_path(p)]
    if not scope:
        return paths
    scope = scope.strip()
    if scope.startswith("ch"):
        return [p for p in paths if f"/{scope}_" in p.replace("\\", "/")]
    return [p for p in paths if scope in os.path.basename(p)]


def normalize_source(source) -> list[str]:
    """Return a canonical source array: only non-final lines keep their "\\n".

    Splits on "\\n" only (never on \\r/\\v/\\f etc.) so that mis-escaped LaTeX
    control characters are preserved verbatim for the corruption validators to
    catch, rather than being silently turned into line breaks here.
    """
    text = source if isinstance(source, str) else "".join(source)
    text = text.rstrip("\n")
    if not text:
        return []
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + [parts[-1]]


def gen_cell_id() -> str:
    return uuid.uuid4().hex[:8]


def normalize_notebook(nb: dict) -> bool:
    """Mutate `nb` in place toward canonical form. Return True if anything changed."""
    changed = False

    cells = nb.get("cells", [])
    has_ids = False
    for cell in cells:
        src = cell.get("source", [])
        new_src = normalize_source(src)
        if new_src != src:
            cell["source"] = new_src
            changed = True
        if "id" not in cell:
            cell["id"] = gen_cell_id()
            changed = True
        has_ids = True

    if has_ids and nb.get("nbformat_minor", 0) < MIN_NBFORMAT_MINOR:
        nb["nbformat_minor"] = MIN_NBFORMAT_MINOR
        changed = True

    return changed


def needs_fix(nb: dict) -> list[str]:
    """Return human-readable reasons the notebook is not canonical (empty = clean)."""
    reasons: list[str] = []
    cells = nb.get("cells", [])
    for ci, cell in enumerate(cells):
        src = cell.get("source", [])
        text = src if isinstance(src, str) else "".join(src)
        if isinstance(src, list) and src and src[-1].endswith("\n"):
            reasons.append(f"cell {ci}: last source line ends with newline")
        elif isinstance(src, str) and text.endswith("\n"):
            reasons.append(f"cell {ci}: source string ends with newline")
        if "id" not in cell:
            reasons.append(f"cell {ci}: missing cell id")
    if cells and any("id" in c for c in cells) and nb.get("nbformat_minor", 0) < MIN_NBFORMAT_MINOR:
        reasons.append(
            f"nbformat_minor={nb.get('nbformat_minor')} but cells have ids "
            f"(requires >= {MIN_NBFORMAT_MINOR})"
        )
    return reasons


def write_notebook(nb: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize PHYS130B notebooks")
    parser.add_argument("--scope", default=None, help="ch2 or a filename stem")
    parser.add_argument("--check", action="store_true", help="report only; do not write")
    args = parser.parse_args()

    paths = list(iter_notebooks(args.scope))
    fixed: list[str] = []
    flagged: dict[str, list[str]] = {}

    for path in paths:
        with open(path, encoding="utf-8") as f:
            nb = json.load(f)
        if args.check:
            reasons = needs_fix(nb)
            if reasons:
                flagged[os.path.relpath(path, ROOT)] = reasons
        else:
            if normalize_notebook(nb):
                write_notebook(nb, path)
                fixed.append(os.path.relpath(path, ROOT))

    print("=" * 60)
    print(f"Notebooks scanned: {len(paths)}")
    if args.check:
        if flagged:
            print(f"Notebooks needing normalization: {len(flagged)}")
            for loc in sorted(flagged):
                print(f"\n{loc}")
                for r in flagged[loc]:
                    print(f"  - {r}")
            return 1
        print("All notebooks already canonical.")
        return 0

    if fixed:
        print(f"Notebooks normalized: {len(fixed)}")
        for loc in fixed:
            print(f"  - {loc}")
    else:
        print("No changes needed; all notebooks already canonical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
