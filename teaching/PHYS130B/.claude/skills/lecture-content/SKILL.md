---
name: phys130b-lecture-content
description: Narrative, pedagogy, structure, prompts, homework, projects, and discussion boxes for PHYS130B notes—align with rules/teaching-philosophy.md, content-style.md, notebook-architecture.md without bulk rewrites.
---

# Skill: Lecture content (PHYS130B)

Improve **teaching clarity**, **structure**, and **alignment** with `rules/teaching-philosophy.md`, `rules/notebook-architecture.md`, `rules/content-style.md`, `rules/maintenance-scope.md`, `rules/prompt-templates.md`. Read-heavy; implementation of edits goes through **`notebook-writer`**.

## Activation (auto)

- Editing **markdown** in lecture cells (Prompts, `## Lecture Notes`, Summary, Discussion, Homework, Project).
- Reviewing a notebook for **flow**, **bloat**, **missing or misaligned** prompts/homework after lecture changes.
- Designing or revising **homework**, **discussion** questions, or **section project** text (pedagogy and wording—not LaTeX physics verification alone).

## Non-goals

- Large-scale **TOC / rename / cross-chapter moves** without explicit human approval (`maintenance-scope.md`).
- **Physics correctness** as sole reviewer—use **`science-reviewer`** for equations and “show that” targets.
- **Not** the primary owner of JSON corruption repair (see `notebook-writer` + `troubleshooting-ipynb`).
- **`./build.sh`** or **`jupyter-book build`**—blocked or failing in sandboxes; use **`rules/validation.md`** only.

## Fallback / de-escalation

- If structure is broken or cells are wrong, **stop** content polish—hand off structure fixes to `notebook-writer` / human.
- If physics of homework statements is uncertain, **flag** for `science-reviewer` or `feedback.md`—do not ship guessed problem statements.

## Structural review (subsection x.y.z)

- [ ] Cell 0: `# x.y.z Title`; cell 1: Prompts `tip`; cell 2: `## Lecture Notes` → `### Overview` → body → `### Summary`; cell 3: `## Homework`; **4 cells** total.
- [ ] No `---`; no nested `:::`; display math blank lines per `physics-conventions.md`.

## Structural review (section parent x.y)

- [ ] Cell 0: `# x.y Title`; cell 1: `## Overview` → Topics → Key Concepts → Learning Objectives; cell 2: `## Project`; **3 cells**; no Prompts at x.y.

## Content review

- **Narrative:** one main thread; cut tangents; optional **short** worked examples (one idea each).
- **Prompts:** natural, specific, map to what cell 2 actually teaches.
- **Homework:** 5–10 problems, one focus each; mix conceptual / derive / apply / reason; exam-ready, not tedious (`content-style.md`).
- **Discussion:** genuinely debatable, physics-grounded, `dropdown tip` inline.
- **Project (x.y):** research-level, feasible ~2 weeks with AI; literature + computation + writing.

## Homework / project design process

1. Read lecture cell(s); list concepts and results.
2. Map **one problem per major concept**; verify “show that” statements (send to science review if needed).
3. Output markdown ready for `notebook-writer` to paste into the right cell.

## Review report template (read-only pass)

```markdown
## Review: [notebook]

### Status: PASS | NEEDS WORK | CRITICAL
### Structural issues
### Content issues
### Proposed changes
1. [Concrete edit for notebook-writer]
```

## References

- `rules/teaching-philosophy.md`, `rules/notebook-architecture.md`, `rules/content-style.md`, `rules/maintenance-scope.md`, `rules/prompt-templates.md`, `rules/physics-conventions.md`, `.claude/README.md`
- `skills/homework-designer/SKILL.md` (homework design, quality, formatting)
