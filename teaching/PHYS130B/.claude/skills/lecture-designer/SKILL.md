---
name: phys130b-lecture-designer
description: Design and audit lecture narrative, pedagogy, structure, prompts, homework, projects, and discussion boxes for PHYS130B—align with rules without implementing .ipynb edits. Pair with notebook-writer for implementation.
---

# Skill: Lecture designer (PHYS130B)

## Role in the stack

**Content designer:** audit notebooks and **specify** changes (reports, proposed markdown, cell targets). **Do not** edit `.ipynb` JSON. **Do not** run validator CLIs. **Implementation** is only **`notebook-writer`** (`rules/notebook-editing.md`); **`notebook-writer`** runs **`rules/validation.md`** after every save.

Improve **teaching clarity**, **structure**, and **alignment** with `rules/teaching-philosophy.md`, `rules/notebook-architecture.md`, `rules/content-style.md`, `rules/maintenance-scope.md`, `rules/prompt-preview.md`. **Copy-paste subsection shells:** **`TEMPLATES.md`** (this folder).

## Activation (auto)

- Reviewing or reshaping **markdown** in lecture cells (Prompts, `## Lecture Notes`, Summary, Discussion, Homework, Project)—**specify** edits for `notebook-writer`.
- Reviewing a notebook for **flow**, **bloat**, **missing or misaligned** prompts/homework after lecture changes.
- Designing **homework**, **discussion** questions, or **section project** text (pedagogy and wording—not LaTeX physics verification alone).

## Non-goals

- Large-scale **TOC / rename / cross-chapter moves** without explicit human approval (`maintenance-scope.md`).
- **Proof / derivation correctness** (chains, “show that” math)—use **`derivation-designer`**; hand narrative-only physics judgment to **`feedback.md`** when unsure.
- **Not** the primary owner of JSON corruption repair (see `notebook-writer` + `troubleshooting-ipynb`).
- **`./build.sh`** or **`jupyter-book build`**—agents must not run full book builds.
- **Running** `validate_project.py` / `safe_edit.py validate`—**`notebook-writer`** only, after it edits files.

## Fallback / de-escalation

- If structure is broken or cells are wrong, **stop** content polish—hand off structure fixes to `notebook-writer` / human.
- If a homework “show that” or derivation chain is uncertain, **flag** for **`derivation-designer`** or `feedback.md`—do not ship guessed proof statements.

## Structural review (law lives in rules)

Do **not** re-encode cell layouts here. Use **`TEMPLATES.md`** (new-notebook integration checklist) plus **`rules/notebook-architecture.md`** (subsection vs parent), **`rules/myst-references.md`**, and **`rules/physics-conventions.md`** (display math). Record PASS/FAIL and cite **rule §** in your report.

## Content review (role-only)

- **Narrative arc:** one thread, cut tangents—criteria in **`rules/content-style.md`** + **`rules/maintenance-scope.md`**.
- **Prompts:** delegate deep pass to **`skills/prompt-designer/SKILL.md`** (law: **`rules/prompt-preview.md`**; shell: **`skills/prompt-designer/TEMPLATES.md`**).
- **Homework / Discussion / Project:** norms in **`rules/content-style.md`** and **`rules/teaching-philosophy.md`**; homework depth workflow in **`skills/homework-designer/SKILL.md`**.

## Homework / project design process

1. Read lecture cell(s); list concepts and results.
2. Map **one problem per major concept**; for proof-heavy “show that” targets, request **`derivation-designer`** review before **`notebook-writer`** implements.
3. Output markdown and cell index for **`notebook-writer`** to apply.

## Review report template (read-only pass)

```markdown
## Lecture design: [notebook]

### Status: PASS | NEEDS WORK | CRITICAL
### Structural issues
### Content issues
### Proposed changes (for notebook-writer)
1. [Cell N: concrete markdown or instruction]
```

## Reference materials (`_refs/`)

**Single source for file map and reading order:** **`CLAUDE.md`** § Reference materials. Before specifying any derivation or worked physics argument, read the matching `_refs/` entry there; for proof-chain QC, **`skills/derivation-designer/SKILL.md`**.

## References

- `rules/teaching-philosophy.md`, `rules/notebook-architecture.md`, `rules/content-style.md`, `rules/maintenance-scope.md`, `rules/prompt-preview.md`, `rules/physics-conventions.md`, **`TEMPLATES.md`** (this folder), `.claude/README.md`, `skills/maintenance-phases/SKILL.md` (Phase **C** style pass)
- `skills/homework-designer/SKILL.md` (homework depth, quality, formatting specs)
- `skills/prompt-designer/SKILL.md` (prompt quality, LLM-friendliness)
- `skills/derivation-designer/SKILL.md` (derivation & proof chain QC)
- `_refs/` (via **`CLAUDE.md`** map — read before specifying derivations)
