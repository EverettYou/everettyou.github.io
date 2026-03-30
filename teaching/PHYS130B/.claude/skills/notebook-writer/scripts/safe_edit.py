#!/usr/bin/env python3
"""Safe notebook editing utilities for PHYS130B.

Usage:
    python safe_edit.py read <notebook_path> [--cell N]
    python safe_edit.py write <notebook_path> --cell N --content-file <path>
    python safe_edit.py insert <notebook_path> --at N --content-file <path>
    python safe_edit.py validate <notebook_path>
"""

import json
import sys
import argparse
import glob


def text_to_source(text):
    """Convert a markdown string to a proper ipynb source array."""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:
                source.append(line)
    return source


def load_notebook(path):
    with open(path) as f:
        return json.load(f)


def save_notebook(nb, path):
    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)


def print_cell_summary(nb, cell_idx=None):
    """Print a summary of notebook cells."""
    cells = nb['cells']
    if cell_idx is not None:
        cells = [cells[cell_idx]]
        indices = [cell_idx]
    else:
        indices = range(len(cells))

    for i, cell in zip(indices, cells):
        src = ''.join(cell['source'])
        preview = src[:120].replace('\n', '\\n')
        print(f"[{i}] {cell['cell_type']} ({len(cell['source'])} lines): {preview}")
        if cell_idx is not None:
            print("--- Full content ---")
            print(src)


def validate_cell(src, cell_idx, filename=""):
    """Validate a single cell's source array. Returns list of issues."""
    issues = []
    if not src or len(src) < 5:
        return issues

    # Char-by-char corruption
    short = sum(1 for s in src if len(s) <= 2)
    if short > len(src) * 0.7 and len(src) > 20:
        issues.append(f"CHAR-BY-CHAR: {filename} cell {cell_idx}")

    # Collapsed lines
    max_len = max(len(s) for s in src)
    if max_len > 1000:
        issues.append(f"LONG LINE: {filename} cell {cell_idx} (max {max_len})")

    # Missing newlines
    missing = sum(1 for i, s in enumerate(src[:-1]) if not s.endswith('\n'))
    if missing > 0:
        issues.append(f"MISSING \\n: {filename} cell {cell_idx} ({missing} lines)")

    return issues


def validate_notebook(path):
    """Validate all cells in a notebook."""
    nb = load_notebook(path)
    all_issues = []
    for ci, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'markdown':
            continue
        issues = validate_cell(cell['source'], ci, path)
        all_issues.extend(issues)
    return all_issues


def cmd_read(args):
    nb = load_notebook(args.path)
    print_cell_summary(nb, args.cell)


def cmd_write(args):
    nb = load_notebook(args.path)
    with open(args.content_file) as f:
        content = f.read()
    nb['cells'][args.cell]['source'] = text_to_source(content)
    save_notebook(nb, args.path)
    # Validate
    issues = validate_cell(nb['cells'][args.cell]['source'], args.cell, args.path)
    if issues:
        print("VALIDATION ISSUES:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print(f"OK: Cell {args.cell} written and validated.")


def cmd_insert(args):
    nb = load_notebook(args.path)
    with open(args.content_file) as f:
        content = f.read()
    new_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": text_to_source(content)
    }
    nb['cells'].insert(args.at, new_cell)
    save_notebook(nb, args.path)
    print(f"OK: New cell inserted at index {args.at}. Total cells: {len(nb['cells'])}")


def cmd_validate(args):
    if '*' in args.path or '?' in args.path:
        paths = sorted(glob.glob(args.path, recursive=True))
    else:
        paths = [args.path]

    total_issues = 0
    for path in paths:
        if '/_build/' in path:
            continue
        issues = validate_notebook(path)
        total_issues += len(issues)
        for issue in issues:
            print(issue)

    if total_issues == 0:
        print(f"OK: {len(paths)} notebook(s) validated, no issues found.")
    else:
        print(f"\nFOUND {total_issues} issue(s) across {len(paths)} notebook(s).")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Safe notebook editor')
    sub = parser.add_subparsers(dest='command')

    p_read = sub.add_parser('read')
    p_read.add_argument('path')
    p_read.add_argument('--cell', type=int, default=None)

    p_write = sub.add_parser('write')
    p_write.add_argument('path')
    p_write.add_argument('--cell', type=int, required=True)
    p_write.add_argument('--content-file', required=True)

    p_insert = sub.add_parser('insert')
    p_insert.add_argument('path')
    p_insert.add_argument('--at', type=int, required=True)
    p_insert.add_argument('--content-file', required=True)

    p_validate = sub.add_parser('validate')
    p_validate.add_argument('path')

    args = parser.parse_args()
    if args.command == 'read':
        cmd_read(args)
    elif args.command == 'write':
        cmd_write(args)
    elif args.command == 'insert':
        cmd_insert(args)
    elif args.command == 'validate':
        cmd_validate(args)
    else:
        parser.print_help()
