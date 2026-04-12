#!/usr/bin/env python3
"""
Fix common ipynb cell corruption patterns.

Run from PHYS130B/ directory:
    python3 .claude/scripts/fix_corrupted_cells.py

Fixes:
  1. Char-by-char corruption → join and re-split into proper lines
  2. Missing \\n terminators → add \\n to non-final lines
  3. Collapsed content (>1000 char lines) → insert newlines before headings, admonitions, math
"""

import json, glob, os, re, sys


def text_to_source(text):
    """Convert markdown string to proper ipynb source array."""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:
                source.append(line)
    return source


def fix_char_by_char(src):
    """Fix source where each element is a single character (possibly with spurious \\n)."""
    chars = []
    for s in src:
        if s == '\n':
            chars.append('\n')
        elif s.endswith('\n') and len(s) == 2:
            chars.append(s[0])
        else:
            chars.append(s)
    return text_to_source(''.join(chars))


def fix_missing_newlines(src):
    """Add \\n to non-final lines that are missing it."""
    new_src = []
    for i, line in enumerate(src):
        if i < len(src) - 1 and not line.endswith('\n'):
            new_src.append(line + '\n')
        else:
            new_src.append(line)
    return new_src


def fix_collapsed_content(src):
    """Insert newlines before headings, admonitions, math in long lines."""
    text = ''.join(src)
    text = re.sub(r'([^\n])(#{2,4}\s)', r'\1\n\n\2', text)
    text = re.sub(r'([^\n])(:::\{)', r'\1\n\n\2', text)
    text = re.sub(r'([^\n])(:::)\s*\n', r'\1\n\2\n', text)
    text = re.sub(r'([^\n$])\n?(\$\$)', r'\1\n\n\2', text)
    text = re.sub(r'(\(eq-[^)]+\))\s*([A-Z])', r'\1\n\n\2', text)
    text = re.sub(r'(\(eq-[^)]+\))\s*(\*\*)', r'\1\n\n\2', text)
    text = re.sub(r'(\(eq-[^)]+\))\s*(where|with|Here|This|The|For|If|In|Note|We|and|so|Thus)',
                  r'\1\n\n\2', text)
    return text_to_source(text)


def main():
    base = "notes_src"
    if not os.path.isdir(base):
        base = "."

    fixed_files = 0
    fixed_cells = 0

    for f in sorted(glob.glob(f'{base}/**/*.ipynb', recursive=True)):
        if '/_build/' in f:
            continue

        with open(f) as fh:
            nb = json.load(fh)

        file_changed = False
        for ci, cell in enumerate(nb['cells']):
            if cell['cell_type'] != 'markdown':
                continue
            src = cell['source']
            if not src or len(src) < 5:
                continue

            original_src = list(src)

            # 1. Char-by-char?
            short = sum(1 for s in src if len(s) <= 2)
            if short > len(src) * 0.7 and len(src) > 20:
                src = fix_char_by_char(src)
                cell['source'] = src
                file_changed = True
                fixed_cells += 1
                print(f"  {os.path.basename(f)} cell {ci}: fixed char-by-char ({len(original_src)} → {len(src)} lines)")
                continue

            # 2. Collapsed content?
            max_len = max(len(s) for s in src)
            if max_len > 1000:
                src = fix_collapsed_content(src)
                cell['source'] = src
                file_changed = True
                fixed_cells += 1
                new_max = max(len(s) for s in src) if src else 0
                print(f"  {os.path.basename(f)} cell {ci}: fixed collapsed (max {max_len} → {new_max})")
                continue

            # 3. Missing newlines?
            missing = sum(1 for i, s in enumerate(src[:-1]) if not s.endswith('\n'))
            if missing > 0:
                src = fix_missing_newlines(src)
                cell['source'] = src
                file_changed = True
                fixed_cells += 1
                print(f"  {os.path.basename(f)} cell {ci}: fixed {missing} missing \\n")

        if file_changed:
            with open(f, 'w') as fh:
                json.dump(nb, fh, indent=1, ensure_ascii=False)
            fixed_files += 1

    print(f"\n{'='*50}")
    print(f"Fixed {fixed_cells} cells across {fixed_files} files")


if __name__ == '__main__':
    main()
