#!/usr/bin/env python3
"""Append a :::{admonition} See Also block to lecture cells that lack one.

Uses notes_src/_toc.yml DFS order for prev / next / (+2) navigation targets.
Link lines: plain markdown `- [Title](target): gloss` (no **).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


def _repo_root() -> Path:
    for d in Path(__file__).resolve().parents:
        if (d / "notes_src").is_dir():
            return d
    raise RuntimeError("Could not locate repo root (notes_src/)")


ROOT = _repo_root()
NOTES = ROOT / "notes_src"
TOC_PATH = NOTES / "_toc.yml"
TITLE_RE = re.compile(r"(?m)^#\s+(.+)$")
SEE_ALSO_MARK = ":::{admonition} See Also"
SEE_ALSO_START = re.compile(r"(?m)^:::\{admonition\}\s+See Also\s*$")


def strip_all_seealso_blocks(md: str) -> str:
    out = md
    while True:
        m = SEE_ALSO_START.search(out)
        if not m:
            break
        chunk = out[m.start() :]
        lines = chunk.split("\n")
        for j in range(1, len(lines)):
            if lines[j].strip() == ":::":
                block = "\n".join(lines[: j + 1])
                out = out[: m.start()] + out[m.start() + len(block) :]
                break
        else:
            break
    return out.rstrip()


def text_to_source(text: str) -> list[str]:
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            out.append(line + "\n")
        else:
            if line:
                out.append(line)
    return out


def iter_toc_files(node) -> list[str]:
    out: list[str] = []

    def walk(x):
        if isinstance(x, dict):
            if "file" in x:
                out.append(x["file"])
            for k in ("sections", "chapters"):
                if k in x:
                    walk(x[k])
        elif isinstance(x, list):
            for item in x:
                walk(item)

    walk(node)
    return out


def split_chapter_stem(track: str) -> tuple[str, str]:
    parts = track.split("/", 1)
    if len(parts) != 2:
        return "", track
    return parts[0], parts[1]


def nb_path(track: str) -> Path:
    return NOTES / f"{track}.ipynb"


def load_title(track: str, cache: dict[str, str]) -> str:
    if track in cache:
        return cache[track]
    p = nb_path(track)
    if not p.exists():
        cache[track] = track.split("/")[-1].replace("-", " ").title()
        return cache[track]
    nb = json.loads(p.read_text(encoding="utf-8"))
    for c in nb.get("cells", []):
        if c.get("cell_type") != "markdown":
            continue
        src = c.get("source", [])
        if not isinstance(src, list):
            continue
        t = "".join(src)
        m = TITLE_RE.search(t)
        if m:
            cache[track] = m.group(1).strip()
            return cache[track]
    cache[track] = track.split("/")[-1].replace("-", " ").title()
    return cache[track]


def gloss(role: str) -> str:
    """One-line gloss; link text already states the destination title — do not repeat it."""
    if role == "prev":
        return "Prerequisite material and notation for this lesson."
    if role == "next":
        return "Natural next step along the course sequence."
    return "Neighbour in the table of contents (same chapter thread)."


def rel_target(from_ch: str, to_track: str) -> str:
    to_ch, stem = split_chapter_stem(to_track)
    if from_ch == to_ch:
        return stem
    return f"../{to_ch}/{stem}"


def link_line(from_ch: str, to_track: str, title: str, role: str) -> str:
    tgt = rel_target(from_ch, to_track)
    g = gloss(role)
    return f"- [{title}]({tgt}): {g}"


def build_block(from_track: str, tracks: list[str], idx: int, cache: dict[str, str]) -> str:
    from_ch, _ = split_chapter_stem(from_track)
    lines: list[str] = []
    seen: set[str] = set()

    def add(j: int, role: str) -> None:
        if j < 0 or j >= len(tracks):
            return
        t = tracks[j]
        if t in seen:
            return
        seen.add(t)
        title = load_title(t, cache)
        lines.append(link_line(from_ch, t, title, role))

    add(idx - 1, "prev")
    add(idx + 1, "next")
    add(idx + 2, "hub")

    while len(lines) > 4:
        lines.pop()
    if len(lines) < 2:
        add(idx - 2, "prev")

    body = "\n".join(lines)
    return "\n\n:::{admonition} See Also\n:class: seealso\n\n" + body + "\n:::\n"


def lecture_cell_index(nb: dict) -> int | None:
    for i, c in enumerate(nb.get("cells", [])):
        if c.get("cell_type") != "markdown":
            continue
        src = c.get("source", [])
        if not isinstance(src, list):
            continue
        t = "".join(src)
        if "## Lecture Notes" in t and "### Summary" in t:
            return i
    return None


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--refresh",
        action="store_true",
        help="Replace existing See Also blocks (same navigation, updated template/gloss).",
    )
    args = ap.parse_args()

    if not TOC_PATH.exists():
        print("missing", TOC_PATH, file=sys.stderr)
        return 1
    toc = yaml.safe_load(TOC_PATH.read_text(encoding="utf-8"))
    tracks = iter_toc_files(toc["chapters"])
    track_to_idx = {t: k for k, t in enumerate(tracks)}

    missing_list_path = ROOT / ".tmp_origin_master_seealso_blocks.md"
    missing: list[str] = []
    if missing_list_path.exists():
        text = missing_list_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("- `notes_src/") and line.endswith(".ipynb`"):
                rel = line[len("- `") : -len("`")]
                missing.append(rel)
    if not missing:
        missing = [
            "notes_src/ch1_qubit/1-1-2-state-and-representation.ipynb",
            "notes_src/ch1_qubit/1-1-3-hermitian-operators.ipynb",
            "notes_src/ch1_qubit/1-3-1-unitary-evolution.ipynb",
            "notes_src/ch1_qubit/1-3-3-heisenberg-picture.ipynb",
            "notes_src/ch2_identical-particles/2-1-1-tensor-product.ipynb",
            "notes_src/ch2_identical-particles/2-1-3-second-quantization.ipynb",
            "notes_src/ch2_identical-particles/2-2-1-angular-momentum-algebra.ipynb",
            "notes_src/ch2_identical-particles/2-2-2-spin-representations.ipynb",
            "notes_src/ch2_identical-particles/2-2-3-addition-of-angular-momenta.ipynb",
            "notes_src/ch2_identical-particles/2-3-1-exchange-statistics.ipynb",
            "notes_src/ch2_identical-particles/2-3-2-fractional-quantum-hall-anyons.ipynb",
            "notes_src/ch2_identical-particles/2-3-3-toric-code.ipynb",
            "notes_src/ch3_path-integral/3-1-2-physical-optics.ipynb",
            "notes_src/ch3_path-integral/3-2-1-path-integral-formulation.ipynb",
            "notes_src/ch3_path-integral/3-2-2-schrodinger-equation.ipynb",
            "notes_src/ch3_path-integral/3-2-3-free-particle-propagator.ipynb",
            "notes_src/ch3_path-integral/3-3-1-stationary-phase-approximation.ipynb",
            "notes_src/ch3_path-integral/3-3-2-wkb-approximation.ipynb",
            "notes_src/ch3_path-integral/3-3-3-bohr-sommerfeld-quantization.ipynb",
            "notes_src/ch3_path-integral/3-4-1-wick-rotation.ipynb",
            "notes_src/ch3_path-integral/3-4-2-black-hole-temperature.ipynb",
            "notes_src/ch4_phase-and-gauge/4-3-2-landau-quantization.ipynb",
            "notes_src/ch4_phase-and-gauge/4-3-3-quantum-hall-effect.ipynb",
            "notes_src/ch4_phase-and-gauge/4-4-1-classical-spin.ipynb",
            "notes_src/ch5_perturbation-theory/5-2-1-interaction-picture.ipynb",
            "notes_src/ch5_perturbation-theory/5-2-3-applications.ipynb",
            "notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb",
            "notes_src/ch6_quantum-foundations/6-1-2-entropy.ipynb",
            "notes_src/ch6_quantum-foundations/6-3-1-projective-measurement.ipynb",
            "notes_src/ch6_quantum-foundations/6-3-2-povm.ipynb",
            "notes_src/ch6_quantum-foundations/6-3-3-quantum-channels.ipynb",
            "notes_src/ch6_quantum-foundations/6-4-1-decoherence.ipynb",
            "notes_src/ch6_quantum-foundations/6-4-2-lindblad-master-equation.ipynb",
            "notes_src/ch6_quantum-foundations/6-4-3-error-correction.ipynb",
        ]

    cache: dict[str, str] = {}
    changed = 0
    for rel in missing:
        p = ROOT / rel
        if not p.exists():
            print("skip missing file", rel, file=sys.stderr)
            continue
        track = rel[len("notes_src/") : -len(".ipynb")]
        if track not in track_to_idx:
            print("skip not in toc", track, file=sys.stderr)
            continue
        nb = json.loads(p.read_text(encoding="utf-8"))
        li = lecture_cell_index(nb)
        if li is None:
            print("skip no lecture", rel, file=sys.stderr)
            continue
        cell = nb["cells"][li]
        md = "".join(cell["source"])
        if SEE_ALSO_MARK in md and not args.refresh:
            print("skip already has See Also", rel)
            continue
        idx = track_to_idx[track]
        block = build_block(track, tracks, idx, cache)
        base = strip_all_seealso_blocks(md) if args.refresh and SEE_ALSO_MARK in md else md
        new_md = base.rstrip() + block
        cell["source"] = text_to_source(new_md)
        p.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
        print("wrote", rel)
        changed += 1
    print("changed", changed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
