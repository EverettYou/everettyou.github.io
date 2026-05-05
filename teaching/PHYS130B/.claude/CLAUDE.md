# PHYS130B — Lecture notes (constitution)

**Split with `README.md`:** This file is **policy** (what the project is, mission, hard constraints, doc map). **Ch4–6 phased maintenance** (definitions, phase table, cursor) lives in **`README.md` § 1**; **which skill to use when, designer→writer handoff, and script discipline** in **`README.md` § 2**; **session mechanics and read order** in **`README.md` §§ 4–6**. **Phase checklists:** **`skills/maintenance-phases/SKILL.md`**. Do not duplicate long workflow tables here.

Paths like `rules/…` mean **`.claude/rules/…`**.

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
- Claiming work is complete based on **`./build.sh` or `jupyter-book build`** (see **`rules/validation.md`**).

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

## Validation (agents)

**Stance:** Agents use **static validators only**; full Jupyter Book builds are **human-only**. Rationale, exact commands, scopes, and what not to run: **single source of truth — `rules/validation.md`** (do not copy command lists into this file).

## Where detail lives

| Document | Role |
|----------|------|
| **`README.md`** (this folder) | **Ch4–6 maintenance program** (phases A–D, cursor, audit vs fix) + minimal session mechanics |
| **`skills/maintenance-phases/SKILL.md`** | Phase checklists and which skill to invoke per phase |
| `rules/teaching-philosophy.md` | Course strategy, role of notes |
| `rules/notebook-architecture.md` | Paths, cells, figures, widgets |
| `rules/myst-references.md` | MyST, `$$`, cross-refs |
| `rules/prompt-preview.md` | Cell-1 prompt preview **law** (criteria, anti-patterns) |
| Designer **`TEMPLATES.md`** | Copy-paste MyST under each **`*-designer`** skill folder—indexed in **`rules/README.md`** § Design templates; must match `rules/` + live subsection notebooks |
| `rules/derivation-quality.md` | Derivation depth, reference-note alignment, anti-patterns |
| Other `rules/*.md` | Editing, security, physics, style, troubleshooting (`validation.md` = agent validators + build policy) |
| `rules/README.md` | Rule index + **when** to read `CLAUDE.md` vs jump straight to one rule (see its § Reading order) |
| `skills/` | **`*-designer`** = audit / plan / propose only (**no** validator CLI); **`notebook-writer`** = **only** `.ipynb` edits **and** runs **`rules/validation.md`** after every save |
| **`feedback.md`** | **Professor-owned** corrections and priorities — **highest priority**; open items outrank the maintenance program. Agents: address **one** item per session when working from this file; mark **DONE** with date when resolved; do not restructure the professor’s open list. |
| **`progress.md`** | Agent ticket queue, session log, phase cursor (**`README.md`** + **`skills/maintenance-phases/SKILL.md`**) |
| **`_refs/`** (project root) | Professor's original lecture notes — authoritative source for derivations and physics content |

## Reference materials (`_refs/`)

The `_refs/` directory at the project root contains the professor's **original lecture notes** (Mathematica `.nb` and exported `.md`). These are the authoritative source for physics content, derivations, notation choices, and presentation style.

| File | Covers |
|------|--------|
| `QubitsAndEntanglement.nb` | Ch 1 (qubits) |
| `SecondQuantization.nb` | Ch 2 (identical particles) |
| `PathIntegral.nb/.md` | Ch 3 (path integral) |
| `PhaseAndGauge.nb/.md` | Ch 4 (phase and gauge) |
| `PerturbationTheory.nb/.md` | Ch 5 (perturbation theory) |
| `QuantumStatistics.nb` | Ch 6 (quantum foundations) |
| `AlgebraicMethods.nb` | Algebraic methods |
| `MatrixMechanics.nb` | Matrix mechanics |
| `PiecewisePotentials.nb` | Piecewise potentials |
| `HOMEWORK.md` | Original homework problems |

**Rule:** Before writing or rewriting any derivation, worked example, or physics argument, **read the corresponding `_refs/` file first**. The professor's presentation is the ground truth; do not reinvent derivations from scratch. **After writing**, structurally diff the result against `_refs/` — verify that every intermediate step the reference includes is present or explicitly cited. See **`rules/derivation-quality.md`** for the full procedure and known failure modes.

## Human loop

**Professor → `feedback.md`:** open items **first**; **one** focused resolution per session when working from that file; mark **DONE** with date. **Maintenance → `README.md`** and **`skills/maintenance-phases/SKILL.md`**. Local HTML proofread: **`rules/validation.md`** § Humans.

## Tool-agnostic layout

Short constitution (`CLAUDE.md`), maintenance program (`README.md` + `skills/maintenance-phases/SKILL.md`), split `rules/`, specialized `skills/`, repo-wide validators in **`.claude/scripts/`** (see **`.claude/scripts/README.md`** and **`rules/validation.md`**), and **bulk helpers next to the skill that owns them** (`skills/{homework,summary}-designer/scripts/`). Other AI tools can mirror the same structure.
