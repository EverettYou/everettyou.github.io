# PHYS130B `.claude` — ch4–6 maintenance program

Read after **`CLAUDE.md`** when doing agent work on this course.

**Professor input:** **`feedback.md`** (project root) is **professor-owned**. Open items there **outrank** the maintenance program below. Procedure: **`CLAUDE.md`** § Human loop.

**Division of labor:** **`CLAUDE.md`** = constitution and doc map. **This file** = **definition** of the phased maintenance loop for chapters **4–6**, plus **which skill to use when**, and minimal session mechanics. **Norms (law)** = **`rules/*.md`** (see **`rules/README.md`**). **Validator commands** = **only** **`rules/validation.md`**.

Paths like `rules/…` mean **`.claude/rules/…`**. Paths like `skills/…` mean **`.claude/skills/…`**.

---

## 1. Multi-phase maintenance

### 1.1 Goal

- **Scope:** subsection notebooks in **chapters 4, 5, 6** (and section parents when the ticket says so). Chapters **1–3** are the **gold standard** for notation, structure, and tone.
- **Pace:** **one** focused action per session—either **one phase audit** on **one** notebook, or **one fix ticket** from `progress.md` (see § 4). No full-chapter sweeps in one session.

### 1.2 Phases (in order per notebook)

Progress the **same** notebook through **A → B → C → D** before moving the phase cursor to the next notebook (unless a ticket narrows scope). Skip **D** when the notebook has no derivation-heavy / `_refs`-aligned content (note skip in `progress.md`).

| Phase | Intent | Primary rules | Skills (typical) |
|-------|--------|---------------|------------------|
| **A — Validate** | Mechanical health: JSON/cells, MyST, banned patterns | `validation.md`, `myst-references.md`, `troubleshooting-ipynb.md` | Fixes: **`notebook-writer`** |
| **B — Notation** | QM / LaTeX conventions (operators, units in ch4, kets, `\mathrm{i}` …) | `physics-conventions.md` | Derivation/proof notation issues: **`derivation-designer`** |
| **C — Style & structure** | Cell arc, Overview → Summary, prompts, homework format, See Also | `content-style.md`, `notebook-architecture.md`, `prompt-preview.md`; templates in **`skills/*-designer/TEMPLATES.md`** | **`lecture-designer`**; prompts: **`prompt-designer`**; homework depth: **`homework-designer`**; **`### Summary` / See Also:** **`summary-designer`** |
| **D — Derivation quality** | Logical chain vs professor reference | `derivation-quality.md`, **`_refs/`** (see `CLAUDE.md`) | Chain QC: **`derivation-designer`**; edits + **validation**: **`notebook-writer`** |

**Audit vs fix**

- **Audit:** run checks, record findings as **tickets** in `progress.md`; do **not** bundle unrelated fixes into the same session.
- **Fix:** take **one** ticket; implement with the right skill stack; run validators per **`rules/validation.md`**.

**Skill map detail:** **`skills/maintenance-phases/SKILL.md`** (phase checklists—operational companion to § 1.2).

### 1.3 Cursor and rounds

- Record **current phase**, **notebook stem** (or explicit path), and **round** in **`progress.md`** (phase cursor section—keep it scannable).
- When **D** is done (or skipped with reason), advance to the **next** ch4/5/6 notebook at **phase A**.
- When every target notebook has completed **A–D** for the round, **increment the round** and restart from **A** on the first notebook of the pass.

### 1.4 When the ticket queue has work

Items in **`progress.md`** that are **not** phase-audit findings (e.g. one-off fixes) still use **one ticket, one session**. Phase cursor advances only when you are explicitly doing a **phase audit** pass, not when executing an ad hoc ticket (unless the ticket says otherwise).

---

## 2. Skills: when and how

### 2.1 Two roles (do not blur)

| Skill | **Edits** `notes_src/**/*.ipynb`? | **Runs** validator CLIs in `rules/validation.md`? |
|-------|-----------------------------------|---------------------------------------------------|
| **`notebook-writer`** | **Yes** — sole implementation layer | **Yes** — after **every** save that touches a notebook |
| **Every `*-designer`** (`lecture`, `prompt`, `homework`, `summary`, `derivation`) | **No** — audit, plan, markdown specs, reports | **No** — hand off to **`notebook-writer`** |

**`maintenance-phases`** is not a designer: it is a **routing checklist** for phased work—read it when executing **§ 1** on ch4–6.

### 2.2 Which skill for which work

Use **one** primary designer per ticket unless the ticket explicitly spans cells. Load that skill’s **`SKILL.md`**, then the **`rules/`** files it cites. Use **`TEMPLATES.md`** only when you need a **copy-paste MyST shell** (must still satisfy `rules/`).

| You are doing… | Open first | Law / templates (typical) | Who implements |
|----------------|--------------|-----------------------------|----------------|
| JSON repair, cell surgery, ad hoc notebook patch, running bulk `scripts/*.py` | **`skills/notebook-writer/SKILL.md`** | `notebook-editing.md`, `validation.md`, `troubleshooting-ipynb.md` | Same (**`notebook-writer`**) |
| Whole-lecture arc, Overview→body→Summary flow, bloat, cross-cell pedagogy | **`skills/lecture-designer/SKILL.md`** | `notebook-architecture.md`, `content-style.md`, `lecture-designer/TEMPLATES.md` | **`notebook-writer`** |
| Cell **1** Prompts only (LLM preview strings) | **`skills/prompt-designer/SKILL.md`** | `prompt-preview.md`, `prompt-designer/TEMPLATES.md` | **`notebook-writer`** |
| Homework **set** design, difficulty curve, problem wording (not proof chain QC) | **`skills/homework-designer/SKILL.md`** | `content-style.md` § Homework, `homework-designer/TEMPLATES.md`; audits: **`homework-designer/scripts/README.md`** | **`notebook-writer`** |
| `### Summary` + `See Also` bullets/links, TOC bootstrap, curated See Also | **`skills/summary-designer/SKILL.md`** | `content-style.md` § Summary and See Also, `myst-references.md`, `summary-designer/TEMPLATES.md`; bulk: **`summary-designer/scripts/README.md`** | **`notebook-writer`** (runs those scripts) |
| Derivation / proof **chains** (dropdowns, long “show that”) vs **`_refs/`** | **`skills/derivation-designer/SKILL.md`** | `derivation-quality.md`, `physics-conventions.md`, `derivation-designer/TEMPLATES.md` | **`notebook-writer`** (after designer report) |

**Overlap:** homework *proof* text → **`derivation-designer`** first when the chain is non-trivial; homework *set* shape and pedagogy stay with **`homework-designer`**. Lecture notebook *structure* audit can start with **`lecture-designer`**; deep Prompts-only pass → **`prompt-designer`**.

### 2.3 Designer → `notebook-writer` handoff (how)

1. **Designer** reads **`SKILL.md`** + cited **`rules/`** (+ **`TEMPLATES.md`** if producing MyST).
2. **Designer** outputs a **concrete spec**: e.g. `progress.md` ticket, or “cell *k*, replace with this markdown block,” or “run `python3 .claude/skills/…/scripts/foo.py` then validate.”
3. **`notebook-writer`** applies edits (Bash + Python / `safe_edit.py` per `notebook-editing.md`).
4. **`notebook-writer`** runs **`rules/validation.md`** before claiming done. **Designers never run** `validate_project.py` / `safe_edit.py validate`.

**Bulk mutating scripts** live under **`skills/homework-designer/scripts/`** and **`skills/summary-designer/scripts/`**—see each folder’s **`scripts/README.md`**. Run them **only** in a **`notebook-writer`** session.

### 2.4 Repo-wide scripts (not in a designer folder)

**`.claude/scripts/README.md`** indexes **`validate_project.py`** and **`fix_display_math_blocks.py`**. Same handoff rule: **`notebook-writer`** executes when the change touches notebooks.

---

## 3. `progress.md` (agent queue + cursor)

Tickets, session log, and **phase cursor** live here. This file is for **agents**; it does not replace **`feedback.md`**.

### Keeping `progress.md` usable

- **Completed tickets** older than ~2 rounds: compress to one-line entries under a **History** section (date + notebook + action).
- Keep **active** queue + cursor **short** (aim **≤ ~100 lines** of live content); archive older narrative to a separate file if needed.
- The file should be scannable in ~30 seconds.

---

## 4. Session mechanics (minimal)

1. **`CLAUDE.md`** — constraints and doc map.
2. **`feedback.md`** — if any **open** professor item exists, work **one** of those first; then mark **DONE** with date per **`CLAUDE.md`**.
3. **`progress.md`** — otherwise next ticket **or** next phase audit per § 1.
4. **`designer` → `notebook-writer`:** choose the designer with **§ 2.2** (or phase **§ 1.2**); `*-designer` skills **only** propose; **`notebook-writer`** applies edits **and** runs validators per **`rules/validation.md`** after **every** save (`*-designer` skills do **not** run validator CLI).
5. Close: update **`progress.md`**; if the job was from **`feedback.md`**, mark it **DONE** there; new issues → **new tickets**, not same-session scope creep.

---

## 5. Nothing assigned and queue empty

Propose small work consistent with **`rules/maintenance-scope.md`**, or advance **§ 1** with a phase audit on the next notebook. **Large / risky** items → ticket only, do not start immediately.

---

## 6. Read order (reference)

| Order | Doc |
|-------|-----|
| 1 | `CLAUDE.md` |
| 2 | This `README.md` — at least **§ 2** (skills) when the task is not a raw mechanical fix; **§ 1** when doing ch4–6 phase maintenance |
| 3 | `feedback.md` (professor) if present; else `progress.md` |
| 4 | **`skills/maintenance-phases/SKILL.md`** when running phased maintenance (else skip) |
| 5 | Pick **one** row from **§ 2.2** → that skill’s **`SKILL.md`** → cited **`rules/`** → **`TEMPLATES.md` / `scripts/README.md`** only if needed |
| 6 | After **`notebook-writer`** saves `.ipynb`: **`rules/validation.md`** (writers only—not designers) |
