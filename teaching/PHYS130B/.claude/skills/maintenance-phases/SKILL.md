---
name: phys130b-maintenance-phases
description: Ch4–6 phased notebook maintenance (validate → notation → style → derivation quality). Use when progress.md phase cursor, auditing the next notebook in the round, or user says maintenance phases / phase A–D.
---

# Skill: Maintenance phases (PHYS130B)

Operational companion to **`.claude/README.md` § 1** (phases) and **§ 2** (skills: when and how). Defines **what to do** in each phase and **which** rules/skills to load—not a second copy of validator commands (**`rules/validation.md`** only).

## Activation

- `progress.md` lists a **phase cursor** (A/B/C/D + notebook stem).
- User asks for **maintenance round**, **phase audit**, **next notebook** in ch4–6 quality pass.
- After **tickets** from an audit: fixing **one** ticket is usually **`notebook-writer`** (implement) plus the relevant **`*-designer`** spec—not this skill end-to-end.

## Non-goals

- **Professor-owned items** in **`feedback.md`** — those **override** this program; resolve first per **`CLAUDE.md`**.
- **Chapters 1–3** as maintenance targets (use as **reference** only).
- **Validator command tables** — never duplicate here; use **`rules/validation.md`**.

## Phase checklists (per notebook)

**Validators:** `*-designer` skills **never** run `validate_project.py` / `safe_edit.py validate`. **Read-only** audit passes (e.g. Phase **A** listing failures) may invoke them without editing. **Whenever a notebook file is modified**, **`notebook-writer`** must run **`rules/validation.md`** immediately after that save.

### A — Validate

- Run validators per **`rules/validation.md`** (scoped to this notebook stem) to **audit** mechanical health.
- If failures: classify mechanical vs content; mechanical fixes → **`notebook-writer`** + troubleshooting docs.
- **Rules:** `myst-references.md`, `notebook-architecture.md` (structure signals), `troubleshooting-ipynb.md`.

### B — Notation

- Compare lecture math to **`rules/physics-conventions.md`** (sole convention table); flag inconsistencies—**do not** restate the table in tickets.
- If the ambiguity is **inside a derivation / proof chain**, add **`derivation-designer`** to the ticket; otherwise stay in rule + **`notebook-writer`** for mechanical fixes.

### C — Style & structure

- Subsection vs parent layout per **`notebook-architecture.md`**.
- Narrative arc and teaching flow → **`lecture-designer`** (`TEMPLATES.md` + rules); homework design surface per **`content-style.md`** + **`homework-designer/TEMPLATES.md`**; prompts per **`rules/prompt-preview.md`** + **`prompt-designer/TEMPLATES.md`**.
- **Prompts cell:** deep pass → **`prompt-designer`**.
- **Homework cell:** formatting + pedagogy depth → **`homework-designer`** (proof-style “show that” chains → **`derivation-designer`**).
- **`### Summary` / See Also:** → **`summary-designer`**.

### D — Derivation quality

- Only if the lesson has derivations or worked chains that should match **`_refs/`**.
- Procedure: **`rules/derivation-quality.md`** + **`CLAUDE.md`** `_refs/` map.
- If the derivation chain is wrong or gappy, **`derivation-designer`**; if edits are needed, **`notebook-writer`** (then it validates).

## Audit output template

```markdown
## Phase [A|B|C|D] audit: [stem]

### Notebook
[path or stem]

### Pass | Findings
- ...

### Tickets for progress.md
1. [Single-scope ticket]
```

## Skill set (uniform naming)

| Skill | Role |
|-------|------|
| **`notebook-writer`** | **Only** skill that edits `.ipynb` JSON |
| **`lecture-designer`** | Phase C narrative / structure / arc |
| **`homework-designer`** | Homework depth & AI-era criteria |
| **`prompt-designer`** | Prompts-only |
| **`summary-designer`** | Summary / See Also specs (+ bulk script *invocation* only via notebook-writer) |
| **`derivation-designer`** | Derivation & proof QC (correctness, steps, notation in chains) |

**Overlap:** `lecture-designer` and `homework-designer` both touch homework—use **`lecture-designer`** for light alignment and **`homework-designer`** for deep problem-set audit or rewrites.

## References

- `.claude/README.md` §§ 1–2, `rules/maintenance-scope.md`, `rules/validation.md`, `CLAUDE.md`
