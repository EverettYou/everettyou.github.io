#!/usr/bin/env python3
"""
Unified validation for PHYS130B notebooks and rule docs.

Examples:
  python3 .claude/scripts/validate_project.py
  python3 .claude/scripts/validate_project.py --scope ch2
  python3 .claude/scripts/validate_project.py --scope 2-1-1-tensor-product
  python3 .claude/scripts/validate_project.py --docs-only
  python3 .claude/scripts/audit_homework_format.py   # homework-only report
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
from homework_format import check_homework_cell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NOTEBOOK_GLOB = os.path.join(ROOT, "notes_src", "**", "*.ipynb")
RULES_PATH = os.path.join(ROOT, ".claude", "rules", "physics-conventions.md")
MYST_RULES_PATH = os.path.join(ROOT, ".claude", "rules", "myst-references.md")


@dataclass
class Issue:
    location: str
    message: str


def is_build_path(path: str) -> bool:
    return "/_build/" in path.replace("\\", "/")


def iter_notebooks(scope: str | None) -> Iterable[str]:
    paths = sorted(glob.glob(NOTEBOOK_GLOB, recursive=True))
    paths = [p for p in paths if not is_build_path(p)]
    if not scope:
        return paths

    scope = scope.strip()
    if scope.startswith("ch"):
        return [p for p in paths if f"/{scope}_" in p.replace("\\", "/")]
    return [p for p in paths if scope in os.path.basename(p)]


def check_source_health(src: list[str], label: str) -> list[Issue]:
    issues: list[Issue] = []
    if not src:
        return issues

    # Detect control characters from mis-escaped LaTeX (e.g. \rho -> CR+ho).
    control_map = {
        "\r": ("0x0D CR", "\\rho, \\rangle, \\rightarrow"),
        "\a": ("0x07 BEL", "\\alpha, \\approx"),
        "\b": ("0x08 BS", "\\beta, \\boldsymbol, \\begin"),
        "\f": ("0x0C FF", "\\frac, \\forall"),
        "\v": ("0x0B VT", "\\varepsilon, \\vert"),
        "\t": ("0x09 TAB", "\\text, \\theta, \\tau, \\tanh"),
    }
    full = "".join(src)
    for char, (name, examples) in control_map.items():
        if char in full:
            issues.append(Issue(label, f"contains literal {name} control character (likely mis-escaped LaTeX: {examples})"))

    short = sum(1 for s in src if len(s) <= 2)
    if len(src) > 20 and short > len(src) * 0.7:
        issues.append(Issue(label, f"char-by-char corruption suspected ({short}/{len(src)} short lines)"))

    # Detect missing-backslash corruption: LaTeX commands with backslash stripped.
    # E.g. agent wrote "$rho$" instead of "$\rho$", or "ext{Tr}" instead of "\text{Tr}".
    # Match the FULL command name without a preceding backslash.
    import re as _re
    _mbs_pats = [
        (_re.compile(r'(?<!\\)(?<![a-zA-Z])rho[_\s}]'), r"\rho"),
        (_re.compile(r'(?<!\\)(?<![a-zA-Z])text\{'), r"\text{"),
        (_re.compile(r'(?<!\\)(?<![a-zA-Z])frac\{'), r"\frac{"),
        (_re.compile(r'(?<!\\)(?<![a-zA-Z])nabla[\s\\]'), r"\nabla"),
    ]
    for pat, intended in _mbs_pats:
        if pat.search(full):
            issues.append(Issue(label, f"possible missing-backslash corruption: pattern suggests {intended}"))

    max_len = max(len(s) for s in src)
    if max_len > 1000:
        issues.append(Issue(label, f"collapsed content suspected (max line length {max_len})"))

    missing_newline = sum(1 for s in src[:-1] if not s.endswith("\n"))
    if missing_newline:
        issues.append(Issue(label, f"missing newline terminators ({missing_newline} non-final lines)"))

    # Heuristic: detect \n corruption (\nabla, \nu, \neq, etc. split by newline).
    # After json.load, \n becomes the line separator, so we check source array
    # boundaries: a line ending with $ or \ followed by a line starting with a
    # LaTeX-command tail fragment.
    n_cmd_tails = {"abla", "u ", "u\\", "eq ", "eq\\", "eq}", "ot ",
                   "ot\\", "rightarrow", "ewcommand", "onumber"}
    for i in range(len(src) - 1):
        cur = src[i].rstrip("\n")
        nxt = src[i + 1]
        if cur.endswith("$") or cur.endswith("\\"):
            for tail in n_cmd_tails:
                if nxt.startswith(tail):
                    issues.append(Issue(label,
                        f"possible \\n corruption: line ends with {repr(cur[-8:])} "
                        f"followed by {repr(nxt[:15])} (\\n + {tail[:4]}... = \\n{tail[:4]}...)"))
                    break

    return issues



def check_raw_json_escapes(filepath: str) -> list[Issue]:
    """Scan raw .ipynb bytes for single-backslash JSON escapes that corrupt LaTeX."""
    issues: list[Issue] = []
    label = os.path.basename(filepath)
    with open(filepath, "rb") as fh:
        raw = fh.read()

    # Dangerous: single backslash + t/r/b/f in JSON strings (not preceded by another backslash)
    # In bytes: 0x5C followed by t/r/b/f, NOT preceded by 0x5C
    dangerous = {
        ord("t"): "\\text, \\theta, \\tau, \\tanh, \\to",
        ord("r"): "\\rho, \\rangle, \\rightarrow",
        ord("b"): "\\beta, \\boldsymbol, \\begin, \\bar",
        ord("f"): "\\frac, \\forall",
    }
    for i in range(1, len(raw) - 1):
        if raw[i] == 0x5C and raw[i + 1] in dangerous:
            # Check it's NOT preceded by another backslash (which would make \\t = literal \t)
            if raw[i - 1] != 0x5C:
                letter = chr(raw[i + 1])
                # Skip if inside JSON key context (heuristic)
                ctx = raw[max(0, i - 30):i]
                if b'"cell_' in ctx or b'"nbformat' in ctx or b'"metadata' in ctx:
                    continue
                examples = dangerous[raw[i + 1]]
                issues.append(Issue(label,
                    f"raw JSON has single-escaped \\{letter} at byte {i} "
                    f"(likely corrupts {examples})"))
    return issues



def _is_display_math_open(line: str) -> bool:
    """Opening fence: line is exactly ``$$`` (MyST display math start)."""
    return line.strip() == "$$"


def _is_display_math_close(line: str) -> bool:
    """
    Closing fence: ``$$`` alone or ``$$ (eq-label)`` / ``$$ (my-id)`` on one line
    (see myst-references.md — label may share the closing line).
    """
    t = line.strip()
    if t == "$$":
        return True
    return bool(re.match(r"^\$\$\s+\([^)]+\)\s*$", t))


def _check_display_math_lines(lines: list[str], label: str) -> list[Issue]:
    """Check $$ blocks: blank lines outside, no blank lines inside."""
    issues: list[Issue] = []
    idx = 0
    while idx < len(lines):
        if not _is_display_math_open(lines[idx]):
            idx += 1
            continue

        start = idx
        end = None
        for j in range(start + 1, len(lines)):
            if _is_display_math_close(lines[j]):
                end = j
                break

        if end is None:
            issues.append(Issue(label, "unclosed $$ display block"))
            break

        if start > 0 and lines[start - 1].strip() != "":
            issues.append(Issue(label, "$$ block missing blank line above"))
        if end < len(lines) - 1 and lines[end + 1].strip() != "":
            issues.append(Issue(label, "$$ block missing blank line below"))

        for k in range(start + 1, end):
            if lines[k].strip() == "":
                issues.append(Issue(label, "$$ block contains internal blank line"))
                break

        idx = end + 1
    return issues



def _check_inline_math_integrity(text: str, label: str) -> list[Issue]:
    r"""Detect blank lines (paragraph breaks) inside inline $...$ math spans.

    A blank line inside inline math breaks MyST rendering — the parser
    treats it as a paragraph boundary, splitting the math expression.
    Common cause: ``$\hat{U}\n\n(t)$`` where a newline separates a
    function name from its argument.
    """
    issues: list[Issue] = []
    pos = 0
    in_display = False
    while pos < len(text):
        if text[pos:pos + 2] == "$$":
            in_display = not in_display
            pos += 2
            continue
        if text[pos] == "$" and not in_display:
            end = text.find("$", pos + 1)
            if end == -1:
                break
            # Skip if it is actually $$
            if end + 1 < len(text) and text[end + 1] == "$":
                pos = end + 2
                continue
            math_content = text[pos + 1 : end]
            if "\n\n" in math_content:
                # Extract a short snippet for the message
                snippet = math_content[:60].replace("\n", " ")
                issues.append(
                    Issue(label, f"blank line inside inline $...$ math (breaks rendering): ${snippet}...")
                )
            pos = end + 1
        else:
            pos += 1
    return issues


def _iter_math_segments(text: str) -> Iterable[str]:
    """Yield LaTeX math segments from markdown text."""
    pattern = re.compile(r"\$\$(.*?)\$\$|\$(.*?)\$", re.DOTALL)
    for m in pattern.finditer(text):
        seg = m.group(1) if m.group(1) is not None else m.group(2)
        if seg:
            yield seg


def _check_content_style(text: str, label: str) -> list[Issue]:
    """Checks from rules/content-style.md that are safe to enforce globally."""
    issues: list[Issue] = []

    if re.search(r"(?m)^###\s+Application:", text):
        issues.append(Issue(label, "contains banned heading pattern '### Application:'; use an example admonition"))

    # Nested admonitions frequently break MyST rendering.
    # We only track admonition blocks, not generic directives like margin/figure.
    admonition_depth = 0
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(":::{admonition"):
            if admonition_depth > 0:
                issues.append(Issue(label, "contains nested admonition start ':::{'"))
                break
            admonition_depth += 1
        elif s == ":::":
            if admonition_depth > 0:
                admonition_depth -= 1

    return issues


def _check_physics_conventions(text: str, label: str) -> list[Issue]:
    """Checks from rules/physics-conventions.md not covered by parser checks."""
    issues: list[Issue] = []
    math_segments = list(_iter_math_segments(text))

    if any(r"\vec{" in seg for seg in math_segments):
        issues.append(Issue(label, r"uses \vec{...}; use \boldsymbol{...} for vectors"))

    # Scalar derivative with \cdot is always wrong (should be \nabla \cdot for vectors).
    scalar_cdot = re.compile(
        r"\\frac\{\\partial\}\{\\partial\s*[a-z]\}\s*\\cdot"
        r"|\\partial_[a-z]\s*\\cdot\s*(?!\\boldsymbol)"
    )
    for seg in math_segments:
        if scalar_cdot.search(seg):
            issues.append(Issue(label, r"uses \cdot with scalar derivative; use \nabla \cdot for divergence or plain derivative for 1D"))
            break

    # Differential should be upright in standard calculus patterns (skip \mathrm{d}).
    bad_diff_integral = re.compile(
        r"\\int[^\n]*?(?<![A-Za-z\\{])d\s*(?:\\[A-Za-z]+|[A-Za-z])"
    )
    bad_diff_deriv = re.compile(r"\\frac\{d\}\{d[^}]+\}")
    # \frac{d\psi}{dt}, \frac{d\vert\psi\rangle}{dt} — numerator uses bare d (not \frac{d}{dt}).
    bad_diff_frac_operator = re.compile(r"\\frac\{d\\")
    # Inline slash form: \hbar d\vert\psi\rangle/dt (validator previously only caught \int...dx and \frac{d}{dx}).
    _diff_targets = (
        r"vert|psi|Psi|phi|Phi|theta|varphi|xi|Xi|omega|Omega|alpha|Alpha|chi|eta|zeta|Gamma"
    )
    bad_diff_inline_ket = re.compile(rf"(?<![A-Za-z])d\\(?:{_diff_targets})")
    for seg in math_segments:
        if (
            bad_diff_integral.search(seg)
            or bad_diff_deriv.search(seg)
            or bad_diff_frac_operator.search(seg)
            or bad_diff_inline_ket.search(seg)
        ):
            issues.append(Issue(label, r"uses bare differential d; use \mathrm{d}"))
            break

    # Euler's number in exponentials should be upright.
    bare_e_exp = re.compile(r"(?<![A-Za-z\\])e\^\{")
    if any(bare_e_exp.search(seg) for seg in math_segments):
        issues.append(Issue(label, r"uses bare e^{...}; use \mathrm{e}^{...}"))

    # \text{Tr} should be \mathrm{Tr} or \operatorname{Tr}
    if any(r"\text{Tr}" in seg or r"\text{tr}" in seg for seg in math_segments):
        issues.append(Issue(label, r"uses \text{Tr}; use \mathrm{Tr} or \operatorname{Tr}"))

    # Imaginary unit in exponentials should be upright. Do not treat the letter "i"
    # inside commands like \otimes as the imaginary unit.
    exp_base = re.compile(r"(?:\\mathrm\{e\}|e)\^\{")
    bare_imag_i = re.compile(r"(?<![A-Za-z\\])i(?![a-zA-Z])")

    def _extract_brace_body(s: str, open_brace_at: int) -> str | None:
        """Return contents of {...} starting at open_brace_at, or None if unbalanced."""
        if open_brace_at >= len(s) or s[open_brace_at] != "{":
            return None
        depth = 0
        for k in range(open_brace_at, len(s)):
            if s[k] == "{":
                depth += 1
            elif s[k] == "}":
                depth -= 1
                if depth == 0:
                    return s[open_brace_at + 1 : k]
        return None

    for seg in math_segments:
        for m in exp_base.finditer(seg):
            brace_at = m.end() - 1
            inner = _extract_brace_body(seg, brace_at)
            if inner is None:
                continue
            if r"\mathrm{i}" in inner:
                continue
            if bare_imag_i.search(inner):
                issues.append(Issue(label, r"uses bare i in exponential phase; use \mathrm{i}"))
                break
        else:
            continue
        break

    # In markdown tables, use \vert for ket/bra pipe symbols (column pipes make
    # ASCII | ambiguous; only enforce on table rows, not prose norms like
    # |\langle[\hat A,\hat B]\rangle|).
    for line in text.splitlines():
        if "|" not in line or "$" not in line:
            continue
        if not line.lstrip().startswith("|"):
            continue
        if r"\rangle" not in line and r"\langle" not in line:
            continue
        for seg in _iter_math_segments(line):
            raw_ket_pipe = re.search(r"\|[^$]*\\rangle", seg) or re.search(r"\\langle[^$]*\|", seg)
            if raw_ket_pipe and r"\vert" not in seg:
                issues.append(Issue(label, r"uses raw | in ket/bra inside table; use \vert"))
                return issues

    # Glued \vert + letter/digit breaks MathJax (e.g. \vertV, \vertn, \vert0\rangle).
    # Valid: \vert \psi, \vert 0\rangle, \langle 1\vert V\vert 0\rangle; norms: \|V\| or \lVert V\rVert.
    glued_vert = re.compile(r"\\vert(?=[A-Za-z0-9])")
    for seg in math_segments:
        m = glued_vert.search(seg)
        if m:
            i = m.start()
            snippet = seg[max(0, i - 8) : min(len(seg), i + 24)].replace("\n", " ")
            issues.append(
                Issue(
                    label,
                    r"glued \vert before letter/digit in math (breaks rendering); "
                    r"add space after \vert, space around operators in bras, or use \|...\| for norms — "
                    f"near: ...{snippet}...",
                )
            )
            break

    return issues


def _check_subsection_cell_layout(cells: list, base: str) -> list[Issue]:
    """
    Enforce content-style.md / notebook-architecture.md for x.y.z notebooks (4 cells).
    Cell 1: Prompts admonition; cell 2: ## Lecture Notes; cell 3: ## Homework first.
    """
    issues: list[Issue] = []
    if len(cells) != 4:
        return issues

    c1 = cells[1]
    if c1.get("cell_type") != "markdown":
        issues.append(Issue(base, "cell 1 must be markdown (Prompts)"))
    else:
        t1 = "".join(c1.get("source", []))
        if ":::{admonition} Prompts" not in t1:
            issues.append(Issue(f"{base}:cell1", "missing `:::{admonition} Prompts` (subsection cell 1)"))

    c2 = cells[2]
    if c2.get("cell_type") != "markdown":
        issues.append(Issue(base, "cell 2 must be markdown (Lecture Notes)"))
    else:
        t2 = "".join(c2.get("source", []))
        if not re.search(r"(?m)^## Lecture Notes\s*$", t2):
            issues.append(Issue(f"{base}:cell2", "missing `## Lecture Notes` heading (subsection cell 2)"))

    c3 = cells[3]
    if c3.get("cell_type") != "markdown":
        issues.append(Issue(base, "cell 3 must be markdown (Homework)"))
    else:
        t3 = "".join(c3.get("source", []))
        first_nonempty = ""
        for line in t3.splitlines():
            if line.strip():
                first_nonempty = line.strip()
                break
        if first_nonempty != "## Homework":
            issues.append(
                Issue(
                    f"{base}:cell3",
                    "homework cell must start with line `## Homework` (see content-style.md cell structure)",
                )
            )

    return issues


def _check_parent_cell_layout(cells: list, base: str) -> list[Issue]:
    """Enforce section parent x.y notebooks: cell 1 has ## Overview, cell 2 has ## Project."""
    issues: list[Issue] = []
    if len(cells) != 3:
        return issues

    c1 = cells[1]
    if c1.get("cell_type") != "markdown":
        issues.append(Issue(base, "cell 1 must be markdown (Overview)"))
    else:
        t1 = "".join(c1.get("source", []))
        if not re.search(r"(?m)^## Overview\s*$", t1):
            issues.append(Issue(f"{base}:cell1", "missing `## Overview` heading (parent cell 1)"))

    c2 = cells[2]
    if c2.get("cell_type") != "markdown":
        issues.append(Issue(base, "cell 2 must be markdown (Project)"))
    else:
        t2 = "".join(c2.get("source", []))
        if not re.search(r"(?m)^## Project\s*$", t2):
            issues.append(Issue(f"{base}:cell2", "missing `## Project` heading (parent cell 2)"))

    return issues


def infer_notebook_kind(path: str) -> str:
    """
    subsection: x-y-z-...
    parent:     x-y-...
    other:      fallback
    """
    stem = os.path.basename(path).replace(".ipynb", "")
    parts = stem.split("-")
    if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        return "subsection"
    if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and not parts[2].isdigit():
        return "parent"
    return "other"


def validate_notebook(path: str) -> list[Issue]:
    issues: list[Issue] = []
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    kind = infer_notebook_kind(path)
    base = os.path.basename(path)

    expected_cells = {"subsection": 4, "parent": 3}.get(kind)
    if expected_cells is not None and len(cells) != expected_cells:
        issues.append(Issue(base, f"unexpected cell count: {len(cells)} (expected {expected_cells})"))

    if kind == "subsection" and len(cells) == 4:
        issues.extend(_check_subsection_cell_layout(cells, base))
    if kind == "parent" and len(cells) == 3:
        issues.extend(_check_parent_cell_layout(cells, base))

    if cells and cells[0].get("cell_type") == "markdown":
        title_text = "".join(cells[0].get("source", [])).strip().splitlines()
        first_line = title_text[0] if title_text else ""
        if kind == "subsection" and not re.match(r"^#\s+\d+\.\d+\.\d+\s+\S+", first_line):
            issues.append(Issue(base, "title format mismatch for x.y.z notebook"))
        if kind == "parent" and not re.match(r"^#\s+\d+\.\d+\s+\S+", first_line):
            issues.append(Issue(base, "title format mismatch for x.y notebook"))

    issues.extend(check_raw_json_escapes(path))

    for ci, cell in enumerate(cells):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", [])
        label = f"{base}:cell{ci}"
        issues.extend(check_source_health(source, label))
        text = "".join(source)
        lines = text.splitlines()
        issues.extend(_check_display_math_lines(lines, label))
        issues.extend(_check_inline_math_integrity(text, label))

        if re.search(r"(?m)^---\s*$", text):
            issues.append(Issue(label, "contains banned horizontal rule '---'"))
        if "plt.show()" in text:
            issues.append(Issue(label, "contains plt.show(); use display(fig) + plt.close(fig)"))
        issues.extend(_check_content_style(text, label))
        issues.extend(_check_physics_conventions(text, label))

        if kind == "subsection" and len(cells) == 4 and ci == 3:
            for hf in check_homework_cell(text):
                issues.append(Issue(label, f"homework: [{hf.code}] {hf.message}"))

    return issues


def detect_rule_flags(text: str) -> dict[str, bool]:
    t = text.lower()
    return {
        "blank_lines_outside": ("blank lines above and below" in t) or ("blank lines outside" in t),
        "no_blank_inside": ("no blank lines *within* `$$...$$`" in t)
        or ("do not put blank lines inside a `$$...$$` block" in t)
        or ("no blank lines within" in t),
        "split_required": ("always use `\\begin{split}" in t) or ("always use \\begin{split}" in t),
        "align_forbidden": ("do not use `align` or `aligned`" in t)
        or ("do not use align or aligned" in t),
    }


def validate_rule_docs() -> list[Issue]:
    issues: list[Issue] = []
    for p in (RULES_PATH, MYST_RULES_PATH):
        if not os.path.exists(p):
            issues.append(Issue(".claude docs", f"missing required file: {os.path.relpath(p, ROOT)}"))
            return issues

    with open(RULES_PATH, encoding="utf-8") as f:
        rules_text = f.read()
    with open(MYST_RULES_PATH, encoding="utf-8") as f:
        myst_text = f.read()

    rules_flags = detect_rule_flags(rules_text)
    myst_flags = detect_rule_flags(myst_text)

    for key in ("blank_lines_outside", "no_blank_inside", "split_required", "align_forbidden"):
        if not rules_flags[key]:
            issues.append(Issue("rules/physics-conventions.md", f"missing rule signal: {key}"))
        if not myst_flags[key]:
            issues.append(Issue("rules/myst-references.md", f"missing rule signal: {key}"))
        if rules_flags[key] != myst_flags[key]:
            issues.append(Issue(".claude docs", f"rule mismatch between docs: {key}"))

    return issues


def print_issues(issues: list[Issue]) -> None:
    if not issues:
        return
    grouped: dict[str, list[str]] = {}
    for issue in issues:
        grouped.setdefault(issue.location, []).append(issue.message)

    for loc in sorted(grouped.keys()):
        print(f"\n{loc}")
        for msg in grouped[loc]:
            print(f"  - {msg}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Unified PHYS130B validator")
    parser.add_argument("--scope", default=None, help="Notebook scope: e.g. ch2 or 2-1-1-tensor-product")
    parser.add_argument("--docs-only", action="store_true", help="Validate only .claude rule/design docs")
    parser.add_argument("--notebooks-only", action="store_true", help="Validate only notebooks")
    args = parser.parse_args()

    if args.docs_only and args.notebooks_only:
        print("ERROR: --docs-only and --notebooks-only are mutually exclusive.")
        return 2

    all_issues: list[Issue] = []
    notebook_count = 0

    if not args.docs_only:
        notebooks = list(iter_notebooks(args.scope))
        notebook_count = len(notebooks)
        for path in notebooks:
            all_issues.extend(validate_notebook(path))

    if not args.notebooks_only:
        all_issues.extend(validate_rule_docs())

    print("=" * 60)
    if not args.docs_only:
        print(f"Notebooks checked: {notebook_count}")
    if not args.notebooks_only:
        print("Rule docs checked: .claude/rules/physics-conventions.md, .claude/rules/myst-references.md")

    if all_issues:
        print(f"Total issues: {len(all_issues)}")
        print_issues(all_issues)
        return 1

    print("All validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
