---
name: phys130b-derivation-designer
description: Derivation QC for PHYS130B—every derivation touch follows rules/derivation-quality.md (read _refs first, outline chain, full steps, structural diff vs professor notes). Aligns with _refs/; proposes scoped fixes only; notebook-writer implements.
---

# Skill: Derivation designer (PHYS130B)

## Role in the stack

**Content designer (derivations & proofs):** read derivation dropdowns, worked chains, and **proof-style** homework (“show that”, multi-step derives). **Deliver** a structured report: gaps vs **`_refs/`**, wrong steps, notation issues, and **concrete replacement text or step outline** for **`notebook-writer`** to apply.

**Do not** edit `.ipynb` JSON. **Do not** run `validate_project.py`, `safe_edit.py validate`, or any validator CLI—that is **`notebook-writer`** after it implements changes (**`rules/validation.md`**).

## Mandatory procedure (workflow only)

**Any** derivation or proof-style chain touch: run the **entire** mandatory flow in **`rules/derivation-quality.md`** (§ *Before writing*, *While writing*, *After writing*, minimum depth, anti-patterns, student-confusion test)—**do not** substitute a shorter in-skill checklist. **`_refs/`** file map and reading order: **`CLAUDE.md`** § Reference materials only. **Scope:** same file’s § Relation + **`maintenance-scope.md`** — **no wholesale rewrites**; only the **specific** derivation/block under review unless a human widens scope.

**Dropdown MyST shell (presentation only):** **`TEMPLATES.md`** (this folder)—must still satisfy **`derivation-quality.md`** end-to-end.

**Notation inside math chains:** cite violations against **`rules/physics-conventions.md`**; do not restate convention tables here.

## What this role covers (not duplicated law)

Judge **derivations and proofs** only (not lecture prose, prompts, or homework *set* design—**`lecture-designer`** / **`homework-designer`**). The **report dimensions** are exactly those defined in **`derivation-quality.md`** + **`physics-conventions.md`** for in-chain notation.

## Activation (auto)

- Auditing or redesigning content inside **`:::{dropdown information}`** (or similar) derivation blocks.
- After edits that touch **multi-step** display math or commutator/operator chains.
- Homework or discussion items that are **proof obligations** (not just short numerical answers).
- **`feedback.md`** flags a derivation error or gap.
- Maintenance **phase D** (and **phase B** when the ambiguity lives **inside a derivation**, not in prose layout).

## Non-goals

- **Not** for cell counts, MyST fences, or mechanical JSON—**`notebook-writer`** + **`rules/troubleshooting-ipynb.md`**.
- **Not** for narrative flow without proof content—**`lecture-designer`**.
- **Not** for homework **set design** (number of problems, difficulty curve, AI-era pedagogy)—**`homework-designer`** (may **call** this skill for proof-heavy items).
- **Not** for running **validators** or **`./build.sh`** / **`jupyter-book build`**—ever.

## Output format

```markdown
## Derivation design report: [notebook / section]

### Status: PASS | NEEDS WORK | CRITICAL

### `_refs/` alignment
- [Reference section/lines consulted]
- [Missing or divergent steps vs reference]

### Chain issues (gaps / jumps)
- Step or equation: [what is missing / wrong]

### Notation / rigor
- [symbol / line]: [issue + suggested fix for notebook-writer]

### Proposed text (optional)
- [Markdown or step list for notebook-writer to paste / translate to cells]
```

## References

- **`TEMPLATES.md`** — derivation dropdown MyST shell (non-normative)
- `rules/derivation-quality.md`, `rules/physics-conventions.md`, `CLAUDE.md` (`_refs/` map)
- `skills/notebook-writer/SKILL.md` — implementation + **post-edit validation only there**
- `skills/maintenance-phases/SKILL.md`
