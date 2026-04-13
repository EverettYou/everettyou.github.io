# PHYS130B — Lecture notes (constitution)

## Session workflow

**Each run:** follow **`.claude/README.md`** — read **`feedback.md`** and **`progress.md`**, do assigned work (or propose and execute scoped work / queue large items in **`progress.md`**).

## What this project is

Jupyter Book lecture notes for UCSD PHYS 130B (Quantum Mechanics), Prof. Yi-Zhuang You. Textbook: David Tong, *Quantum Mechanics* (CUP). Source: `notes_src/**/*.ipynb` and MyST markdown; published at `https://everettyou.github.io/teaching/PHYS130B/notes/`.

**Notebook inventory:** about **84** `.ipynb` files under `notes_src/` (60 subsection lessons + 20 section parents + extras; canonical counts in `.claude/settings.json` → `structure`).

## Mission (agents)

**Maintain and incrementally improve** the notes: clarity, alignment with **`rules/`**, consistent style, and correct physics. The corpus is mature—prefer **small, conservative** edits over rewrites.

## Out of scope (don't)

- Course-wide re-outline, mass renames, or TOC surgery without explicit human direction.
- Rewriting many notebooks in one pass “for consistency.”
- Editing generated output under `notes/` (build products only).
- Introducing new languages/toolchains for authoring without explicit ask.
- Claiming work is complete based on **`./build.sh` or `jupyter-book build`** (see Validation below).

## Why the non-negotiables exist

- **`NotebookEdit` / careless JSON edits** → char-by-char corruption in cell `source` arrays.
- **`Edit` / `Write` on the repo (Cowork)** → permission prompts every time; blocks unattended runs. **Use Bash + Python `open` / `json.load` / `json.dump`** for writes instead.
- **Missing `\n` on non-final `source` lines** → MyST concatenates lines; rendered notes break.
- **Teaching and authoring policy** lives in **`rules/`** (start with **`teaching-philosophy.md`**, **`notebook-architecture.md`**, **`myst-references.md`**)—read before changing pedagogy, structure, or MyST.

## Anti-patterns (don’t)

- Use `NotebookEdit`, or `Edit`/`Write`, on notebooks (or any file if Cowork blocks you).
- Shell-redirect (`>`, `>>`) into the mounted project tree from Bash—use Python file I/O in the same invocation (see `rules/tooling-security.md`).
- Bury **definitions students need** inside dropdown-only walls of text; pad with tangents; duplicate the same derivation in multiple lessons.
- Change filenames, `_toc.yml`, or cross-links without a tracked reason and grep for broken refs.

## Validation (agents only)

**Do not run `./build.sh` or `jupyter-book build`** as an agent (sandbox errors / blocks). `settings.json` intentionally has **no** `build_command` for agents. Use static validators only—not a substitute for human local builds, but required for agent work.

After substantive notebook edits, run:

- `python3 .claude/scripts/validate_project.py --scope <notebook-stem-or-chN>` when possible, or full tree if appropriate; and/or  
- `python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate <path.ipynb>` for a single file.

Details: `rules/validation.md`.

**Humans** run `./build.sh` locally for HTML proofreading and MyST errors that only appear in a full build.

## Where detail lives

| Document | Role |
|----------|------|
| **`README.md`** (this folder) | Session order: feedback → progress → work → propose/queue |
| `rules/teaching-philosophy.md` | Course strategy, role of notes |
| `rules/notebook-architecture.md` | Paths, cells, figures, widgets |
| `rules/myst-references.md` | MyST, `$$`, cross-refs |
| `rules/prompt-templates.md` | Prompts box, new-notebook checklist |
| Other `rules/*.md` | Editing, security, validation, physics, style, troubleshooting |
| `skills/` | Context-triggered workflows |
| `progress.md`, `feedback.md` | Project root; tracking and professor notes |
| **`_refs/`** (project root) | Professor's original lecture notes — authoritative source for derivations and physics content |

## Reference materials (`_refs/`)

The `_refs/` directory at the project root contains the professor's **original lecture notes** (Mathematica `.nb` and exported `.md`). These are the authoritative source for physics content, derivations, notation choices, and presentation style.

| File | Covers |
|------|--------|
| `QubitsAndEntanglement.nb` | Ch 1 (qubits) |
| `SecondQuantization.nb` | Ch 2 (identical particles) |
| `PathIntegral.nb` | Ch 3 (path integral) |
| `PhaseAndGauge.nb/.md` | Ch 4 (phase and gauge) |
| `PerturbationTheory.nb/.md` | Ch 5 (perturbation theory) |
| `QuantumStatistics.nb` | Ch 6 (quantum foundations) |
| `AlgebraicMethods.nb` | Algebraic methods |
| `MatrixMechanics.nb` | Matrix mechanics |
| `PiecewisePotentials.nb` | Piecewise potentials |
| `HOMEWORK.md` | Original homework problems |

**Rule:** Before writing or rewriting any derivation, worked example, or physics argument, **read the corresponding `_refs/` file first**. The professor's presentation is the ground truth; do not reinvent derivations from scratch.

## Human loop

Professor uses **`feedback.md`** for corrections and priorities. Optional: local **`./build.sh`** + browser proofread—**not** an agent step.

## Tool-agnostic layout

Short constitution (`CLAUDE.md`), session guide (`README.md`), split `rules/`, small `skills/`, validator (`scripts/validate_project.py`). Other AI tools can mirror the same structure.
