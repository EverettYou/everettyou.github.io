#!/usr/bin/env python3
"""
Validate all .ipynb notebooks for common corruption patterns.

Run from PHYS130B/ directory:
    python3 .claude/scripts/validate_notebooks.py

Checks:
  1. Char-by-char corruption (most source lines are 1-2 chars)
  2. Collapsed content (any line > 1000 chars, headings fused to body)
  3. Missing \\n terminators on non-final source lines
  4. Section parent structure (Topics → Overview → Key Concepts)
"""

import json, glob, os, re, sys


def check_source_health(src):
    """Return list of issue strings for a cell source array."""
    issues = []
    if not src or len(src) < 5:
        return issues

    # 1. Char-by-char
    short = sum(1 for s in src if len(s) <= 2)
    if short > len(src) * 0.7 and len(src) > 20:
        issues.append(f"CHAR-BY-CHAR ({len(src)} elements, {short} short)")

    # 2. Collapsed content
    max_len = max(len(s) for s in src)
    if max_len > 1000:
        issues.append(f"LONG LINE (max {max_len} chars)")

    # 3. Missing newlines
    missing = sum(1 for i, s in enumerate(src[:-1]) if not s.endswith('\n'))
    if missing > 0:
        issues.append(f"MISSING \\n ({missing}/{len(src)} lines)")

    return issues


def check_section_parent(src_text, fname):
    """Check section parent has correct heading structure."""
    issues = []
    headings = re.findall(r'###\s+([^\n]+)', src_text)
    heading_names = [h.strip() for h in headings]

    if 'Topics' not in heading_names:
        issues.append("MISSING ### Topics")
    if 'Overview' not in heading_names:
        issues.append("MISSING ### Overview")
    if 'Key Concepts' not in heading_names:
        issues.append("MISSING ### Key Concepts")

    # Check ordering
    idxs = {}
    for name in ['Topics', 'Overview', 'Key Concepts']:
        if name in heading_names:
            idxs[name] = heading_names.index(name)

    if 'Topics' in idxs and 'Overview' in idxs and idxs['Topics'] > idxs['Overview']:
        issues.append("WRONG ORDER: Overview before Topics")
    if 'Overview' in idxs and 'Key Concepts' in idxs and idxs['Overview'] > idxs['Key Concepts']:
        issues.append("WRONG ORDER: Key Concepts before Overview")

    # Check for banned content
    if 'Prompts' in src_text and ':::{admonition}' in src_text:
        issues.append("HAS Prompts box (should only be at x.x.x level)")

    return issues


def main():
    base = "notes_src"
    if not os.path.isdir(base):
        base = "."  # maybe already in notes_src/

    total_issues = 0
    files_checked = 0

    for f in sorted(glob.glob(f'{base}/**/*.ipynb', recursive=True)):
        if '/_build/' in f:
            continue

        with open(f) as fh:
            nb = json.load(fh)

        fname = os.path.basename(f)
        files_checked += 1
        file_issues = []

        for ci, cell in enumerate(nb['cells']):
            if cell['cell_type'] != 'markdown':
                continue
            src = cell['source']
            issues = check_source_health(src)
            for iss in issues:
                file_issues.append(f"  cell {ci}: {iss}")

        # Check section parent structure
        parts = fname.replace('.ipynb', '').split('-')
        is_parent = (len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit()
                     and not parts[2][0].isdigit())
        if is_parent and len(nb['cells']) > 1:
            src_text = ''.join(nb['cells'][1].get('source', []))
            parent_issues = check_section_parent(src_text, fname)
            for iss in parent_issues:
                file_issues.append(f"  structure: {iss}")

        if file_issues:
            print(f"\n{fname}:")
            for iss in file_issues:
                print(iss)
            total_issues += len(file_issues)

    print(f"\n{'='*50}")
    print(f"Checked {files_checked} notebooks")
    if total_issues == 0:
        print("All notebooks PASS ✓")
    else:
        print(f"Found {total_issues} issues")
        sys.exit(1)


if __name__ == '__main__':
    main()
