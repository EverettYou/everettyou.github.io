# PHYS130B rules index (`.claude/rules/`)

Paths in the table below are **relative to this folder** (`.claude/rules/`).

## Rules vs skills (functional split)

| Layer | **Single source of truth for…** | **Must not** |
|--------|----------------------------------|----------------|
| **`rules/*.md` (law)** | Norms: what is allowed/required/forbidden; LaTeX/MyST requirements; mandatory procedures; validator policy. | Refer to a skill file as the authority for those norms; do **not** treat `TEMPLATES.md` as law. |
| **`skills/*/SKILL.md` (roles)** | *When* to act, *which* rule files to load, handoffs to **`notebook-writer`**, audit **sequence**; per-designer copy-paste shells in **`../skills/*-designer/TEMPLATES.md`** (see § Design templates). | Copy long normative tables from `rules/`—**link + section** instead. |

If a skill and a rule say the same thing, **the rule wins**; trim the skill.

## Design templates (skills)

Paths below are relative to **`.claude/skills/`**. These files are **not** law: they collect MyST snippets aligned to **live** subsection notebooks (e.g. `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb`). When updating a template, reconcile with the cited **`rules/`** files so agents do not drift from norms.

| `TEMPLATES.md` | Covers |
|----------------|--------|
| **`prompt-designer/TEMPLATES.md`** | Cell 1 `:::{admonition} Prompts` |
| **`lecture-designer/TEMPLATES.md`** | Subsection lecture arc + new-notebook integration checklist |
| **`homework-designer/TEMPLATES.md`** | `## Homework` problem layout |
| **`summary-designer/TEMPLATES.md`** | `### Summary` + `See Also` |
| **`derivation-designer/TEMPLATES.md`** | `:::{admonition} Derivation: …` + `:class: dropdown information` |

## Reading order (pick one path)

| Situation | What to read |
|-----------|----------------|
| **New session / first touch this repo** | **`../CLAUDE.md`** (constitution) → **`.claude/README.md`** (maintenance + mechanics) → then the **one** rule you need from this index. You do **not** need `CLAUDE.md` open to *use* this file as a lookup table. |
| **Quick rule check** (e.g. “what is the `$$` rule?”) | Open **only** the relevant row below—**no** requirement to re-read `CLAUDE.md` first. |
| **After you already ingested** `CLAUDE.md` / session README | Use this file as **navigation only**; jump straight to the rule. |

**Canonical “start of agent work” order** for the whole project lives in **`.claude/README.md` § 6** (and `CLAUDE.md` for policy). This README is an **index**, not a second front door—avoid duplicating full-stack read order here.

| File | Use when |
|------|-----------|
| **`teaching-philosophy.md`** | Course strategy, AI-era pedagogy, role of notes |
| **`maintenance-scope.md`** | Editorial stance, when to stop, escalation |
| **`notebook-architecture.md`** | File names, cells, section vs subsection layout, widgets |
| **`content-style.md`** | Admonitions, polls, homework/project norms, **Summary / See Also**, banned *content* patterns |
| **`myst-references.md`** | MyST/Sphinx pitfalls, cross-refs, figures, footnotes |
| **`physics-conventions.md`** | LaTeX, bras/kets, ch4 EM SI, **display math layout** (canonical) |
| **`prompt-preview.md`** | Cell-1 prompt preview **law** (LLM criteria + anti-patterns); MyST shell → **`../skills/prompt-designer/TEMPLATES.md`** |
| **`derivation-quality.md`** | Derivation depth, `_refs/` alignment |
| **`notebook-editing.md`** | Required `.ipynb` edit method, `text_to_source`, post-edit sweeps |
| **`tooling-security.md`** | Why Bash + Python I/O; redirects; `_build/` glob exclusion |
| **`validation.md`** | Agent validator commands (sole list) |
| **`troubleshooting-ipynb.md`** | Corruption recovery recipes; homework cell *mechanical* repairs |

**Overlaps intentionally split:** MyST *document* issues → `myst-references.md`; equation/spacing *and* notation → `physics-conventions.md`; homework *authoring rules* → `content-style.md`; homework *repair code* → `troubleshooting-ipynb.md`.
