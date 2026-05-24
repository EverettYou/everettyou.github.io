#!/usr/bin/env python3
"""Sync homework problems from notes_src/homework/x-y-z_solutions.md into the
corresponding lecture notebook's Homework cell (cell index 3).

For each *_solutions.md file:
  - Parse the preamble hyperlink to find the lecture notebook path.
  - Extract problem statements only (skip Solutions).
  - Format as `## Homework\n\n**1. ...**\n\n**2. ...**\n\n...`
    per rules/content-style.md § Homework Design.
  - Replace cell 3 in the corresponding .ipynb via Python json (NOT NotebookEdit),
    per rules/notebook-editing.md.
  - Idempotent: skip notebooks already in sync.
"""

import json
import pathlib
import re
import sys

PROJECT_ROOT = pathlib.Path(
    "/Users/home/Documents/GitHub/everettyou.github.io/teaching/PHYS130B/notes_src"
)
HW_DIR = PROJECT_ROOT / "homework"

# Matches: [<lesson-num> <Title>](../<chapter_dir>/<slug>)
PREAMBLE_LINK_RE = re.compile(
    r'\[\d+\.\d+\.\d+ [^\]]+\]\(\.\./([\w\-]+)/([\d\-a-z]+)\)'
)


def parse_lecture_path(md_text):
    """Return (chapter_dir, slug) from the preamble hyperlink, else None."""
    m = PREAMBLE_LINK_RE.search(md_text)
    if not m:
        return None
    return m.group(1), m.group(2)


def extract_problems(md_text):
    """Extract problem statements (without solutions) as a list of strings.

    Strategy: scan for problem openers ``**N. ...**`` at column 0 and grab
    each chunk until the next opener (or EOF); strip from ``**Solution.**``
    onward. Separator-agnostic so ``_solutions.md`` files do not need to use
    ``---`` (banned by ``rules/myst-references.md``); any leftover
    horizontal-rule or HTML-comment marker at the end of a chunk is trimmed
    defensively.
    """
    openers = list(re.finditer(r'^\*\*\d+\.\s.*?\*\*', md_text, re.M))
    problems = []
    for k, m in enumerate(openers):
        s = m.start()
        e = openers[k + 1].start() if k + 1 < len(openers) else len(md_text)
        chunk = md_text[s:e]
        sol = re.search(r'\n\*\*Solution\.\*\*', chunk)
        if sol:
            chunk = chunk[:sol.start()]
        chunk = re.sub(r'\n+(?:---|<!--[^>]*-->)\s*$', '', chunk).rstrip()
        problems.append(chunk)
    return problems

def text_to_source(text):
    """Convert plain text to ipynb source-array format.
    Every line except the last must end with '\\n' (per rules/notebook-editing.md)."""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:
                source.append(line)
    return source


def build_homework_cell(problems):
    return "## Homework\n\n" + "\n\n".join(problems)


def sync_one(md_path):
    """Sync one solutions file to its lecture notebook. Returns a status string."""
    md_text = md_path.read_text()
    parsed = parse_lecture_path(md_text)
    if parsed is None:
        return f"SKIP {md_path.name}: no preamble lecture link found"
    chapter_dir, slug = parsed
    nb_path = PROJECT_ROOT / chapter_dir / f"{slug}.ipynb"
    if not nb_path.exists():
        return f"SKIP {md_path.name}: notebook {nb_path} not found"

    problems = extract_problems(md_text)
    if not problems:
        return f"SKIP {md_path.name}: no problems extracted"

    new_source_text = build_homework_cell(problems)

    with nb_path.open() as f:
        nb = json.load(f)
    if len(nb['cells']) < 4:
        return f"SKIP {md_path.name}: notebook has only {len(nb['cells'])} cells"

    current_source_text = ''.join(nb['cells'][3]['source'])
    if current_source_text == new_source_text:
        return f"ok   {md_path.name}: already in sync ({len(problems)} problems)"

    nb['cells'][3]['source'] = text_to_source(new_source_text)
    with nb_path.open('w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write('\n')

    return f"UPD  {md_path.name}: synced {len(problems)} problems -> {chapter_dir}/{slug}.ipynb"


def main():
    md_files = sorted(HW_DIR.glob('*_solutions.md'))
    if not md_files:
        print("No solution files found.")
        return 1
    n_updated = 0
    n_ok = 0
    n_skip = 0
    for md_path in md_files:
        status = sync_one(md_path)
        print(status)
        if status.startswith('UPD'):
            n_updated += 1
        elif status.startswith('ok'):
            n_ok += 1
        else:
            n_skip += 1
    print(f"\nSummary: {n_updated} updated, {n_ok} already in sync, {n_skip} skipped (of {len(md_files)} files)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
