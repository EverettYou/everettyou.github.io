#!/usr/bin/env python3
"""
Detect duplicate homework problems across subsection notebooks.

Catches the failure mode where a problem was copied (not moved) between chapters
and the original was never removed. Compares normalized problem bodies across
every subsection `.ipynb` (cell 3) and reports high-similarity pairs.

Usage:
    python3 .claude/scripts/check_duplicate_homework.py
    python3 .claude/scripts/check_duplicate_homework.py --threshold 0.75

Recommended as part of post-refactor validation when a problem was intentionally
moved between notebooks, and as a periodic audit.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")


def is_build_path(p: str) -> bool:
    return "/_build/" in p.replace("\\", "/")


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower().strip())


def split_problems(hw: str):
    """Yield (num, title, body) for each **N. Title.** ... block."""
    parts = re.split(r"(\*\*\d+\.\s+[^*\n]+\*\*)", hw)
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        m = re.match(r"\*\*(\d+)\.\s+([^*]+)\*\*", header)
        if not m:
            continue
        yield m.group(1), m.group(2).strip().rstrip("."), body


def collect() -> list[tuple[str, str, str, str]]:
    """Return [(stem, num, title, normalized_body)]."""
    out: list[tuple[str, str, str, str]] = []
    for p in sorted(glob.glob(NOTEBOOK_GLOB, recursive=True)):
        if is_build_path(p):
            continue
        stem = os.path.basename(p).replace(".ipynb", "")
        if not re.match(r"\d+-\d+-\d+-", stem):
            continue
        try:
            with open(p) as f:
                nb = json.load(f)
        except Exception:
            continue
        if len(nb["cells"]) < 4:
            continue
        hw = "".join(nb["cells"][3].get("source", []))
        for num, title, body in split_problems(hw):
            norm = normalize(body)
            if len(norm) < 120:  # skip trivial problems
                continue
            out.append((stem, num, title, norm))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--threshold", type=float, default=0.80,
                    help="similarity threshold (0..1) for reporting (default 0.80)")
    ap.add_argument("--snippet", type=int, default=300,
                    help="prefix length used as coarse fingerprint (default 300)")
    args = ap.parse_args()

    problems = collect()
    # First pass: cheap prefix fingerprint to bucket candidates.
    buckets: dict[str, list[int]] = defaultdict(list)
    for idx, (_, _, _, body) in enumerate(problems):
        fp = hashlib.md5(body[: args.snippet].encode()).hexdigest()[:10]
        buckets[fp].append(idx)

    reported_pairs: set[tuple[int, int]] = set()
    flagged = []

    # Exact-prefix collisions: always report.
    for idxs in buckets.values():
        if len(idxs) > 1:
            for i in range(len(idxs)):
                for j in range(i + 1, len(idxs)):
                    reported_pairs.add((idxs[i], idxs[j]))
                    flagged.append((1.0, idxs[i], idxs[j]))

    # Second pass: SequenceMatcher on all pairs from different files with overlapping
    # 20-char shingles (keeps cost bounded while catching near-duplicates).
    shingles: dict[str, list[int]] = defaultdict(list)
    SHINGLE = 40
    for idx, (_, _, _, body) in enumerate(problems):
        seen = set()
        for k in range(0, len(body) - SHINGLE, 20):
            seen.add(body[k : k + SHINGLE])
        for sh in seen:
            shingles[sh].append(idx)

    candidate_pairs: set[tuple[int, int]] = set()
    for idxs in shingles.values():
        if len(idxs) < 2:
            continue
        # Limit expansion on very common shingles
        if len(idxs) > 50:
            continue
        for i in range(len(idxs)):
            for j in range(i + 1, len(idxs)):
                a, b = sorted((idxs[i], idxs[j]))
                candidate_pairs.add((a, b))

    for a, b in sorted(candidate_pairs):
        if (a, b) in reported_pairs:
            continue
        if problems[a][0] == problems[b][0]:
            continue  # same file
        ratio = SequenceMatcher(None, problems[a][3], problems[b][3]).ratio()
        if ratio >= args.threshold:
            flagged.append((ratio, a, b))
            reported_pairs.add((a, b))

    flagged.sort(key=lambda t: -t[0])
    if not flagged:
        print("No duplicate homework problems detected.")
        return 0

    print(f"Potential duplicate homework problems (threshold={args.threshold:.2f}):\n")
    for ratio, a, b in flagged:
        sa, na, ta, _ = problems[a]
        sb, nb, tb, _ = problems[b]
        print(f"  [{ratio:.2f}]  {sa} #{na} '{ta}'")
        print(f"           {sb} #{nb} '{tb}'")
    print(f"\n{len(flagged)} pair(s) flagged. Review each and confirm whether the duplicate is intentional.")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
