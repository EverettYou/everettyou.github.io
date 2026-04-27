#!/usr/bin/env python3
"""Strip **...** around markdown links in :::{admonition} See Also ... ::: blocks only."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SEE_ALSO_START = re.compile(r"(?m)^:::\{admonition\}\s+See Also\s*$")
# List item: optional indent, - , space, **[link](url)**: rest
BOLD_LINK_ITEM = re.compile(
    r"^(\s*-\s+)\*\*(\[[^\]]+\]\([^)]+\))\*\*:(.*)$"
)


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


def dembold_seealso_block(block: str) -> tuple[str, int]:
    n = 0
    out_lines: list[str] = []
    for ln in block.split("\n"):
        m = BOLD_LINK_ITEM.match(ln)
        if m:
            ln = f"{m.group(1)}{m.group(2)}:{m.group(3)}"
            n += 1
        out_lines.append(ln)
    return "\n".join(out_lines), n


def extract_seealso_block(text: str, block_start: int) -> str | None:
    if not SEE_ALSO_START.match(text, block_start):
        return None
    chunk = text[block_start:]
    lines = chunk.split("\n")
    for j in range(1, len(lines)):
        if lines[j].strip() == ":::":
            return "\n".join(lines[: j + 1])
    return None


def process_cell_markdown(text: str) -> tuple[str, int]:
    total = 0
    pos = 0
    parts: list[str] = []
    while True:
        m = SEE_ALSO_START.search(text, pos)
        if not m:
            parts.append(text[pos:])
            break
        parts.append(text[pos : m.start()])
        block = extract_seealso_block(text, m.start())
        if not block:
            parts.append(text[m.start() : m.end()])
            pos = m.end()
            continue
        new_block, n = dembold_seealso_block(block)
        total += n
        parts.append(new_block)
        pos = m.start() + len(block)
    return "".join(parts), total


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Notebooks (default: all under notes_src)")
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[2]
    if args.paths:
        paths = [Path(p) if Path(p).is_absolute() else root / p for p in args.paths]
    else:
        paths = sorted(
            p for p in (root / "notes_src").rglob("*.ipynb") if "/_build/" not in str(p)
        )
    changed_files = 0
    total_lines = 0
    for p in paths:
        nb = json.loads(p.read_text(encoding="utf-8"))
        file_n = 0
        for c in nb.get("cells", []):
            if c.get("cell_type") != "markdown":
                continue
            src = c.get("source", [])
            if not isinstance(src, list):
                continue
            text = "".join(src)
            if "See Also" not in text or ":::{" not in text:
                continue
            new_text, n = process_cell_markdown(text)
            if n:
                c["source"] = text_to_source(new_text)
                file_n += n
        if file_n:
            p.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
            rel = p.relative_to(root) if p.is_relative_to(root) else p
            print(f"{rel} dembolded {file_n}")
            changed_files += 1
            total_lines += file_n
    print("files_changed", changed_files, "bullets_changed", total_lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
