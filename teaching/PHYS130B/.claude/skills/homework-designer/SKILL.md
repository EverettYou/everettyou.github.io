---
name: phys130b-homework-designer
description: Design, audit, and rewrite homework problems for PHYS130B lecture notes. Enforces formatting rules, quality principles, and AI-era pedagogy. Use when creating new problems, reviewing existing homework, or fixing formatting issues.
---

# Skill: Homework Designer (PHYS130B)

Unified reference for **designing**, **auditing**, and **formatting** homework problems in PHYS130B quantum mechanics lecture notes. Consolidates rules from `content-style.md`, `teaching-philosophy.md`, `prompt-templates.md`, and `physics-conventions.md`.

## Activation (auto)

- Writing new homework problems for a subsection notebook.
- Reviewing or auditing existing homework for quality, formatting, or alignment with lecture content.
- Fixing homework formatting issues (bold markers, sub-parts, display math spacing, etc.).
- Responding to feedback items about homework quality or style.

## Non-goals

- Physics correctness of "show that" targets or derivation endpoints — hand off to **`science-reviewer`**.
- JSON / cell-level notebook editing mechanics — hand off to **`notebook-writer`**.
- Lecture content changes — hand off to **`lecture-content`**.

---

## 1. Teaching Context

### Why homework matters in 2026

LLMs solve undergraduate physics homework at or above student level. Students work with AI on homework and are graded on submission, not correctness. **The same problems appear on the final exam (in-person, no AI).** Homework must therefore build *internalized understanding* — worldview (世界观) and method (方法论) — not just procedural skill.

### What homework must achieve

- **Build worldview**: problems that force the student to hold a mental model, not just follow steps.
- **Prepare for the exam**: a student who truly understood the homework (not just copied AI output) can solve exam variants.
- **Be AI-resistant in spirit**: even though students use AI, the problem should require *understanding* to solve variants on the exam.

### Difficulty distribution and lecture-connectedness

Homework must have a **gradient from easy to hard** and from **close to the lecture to far from the lecture**. Not every problem should be creative or challenging — some should directly exercise the skills and knowledge taught in class.

**Required distribution for a typical 7–8 problem set:**

- **2–3 near-lecture problems (easy–medium):** Directly apply a definition, method, or result from the lecture to a concrete case. These are NOT "lecture duplication" (anti-pattern §3.1) because they ask the student to *use* the result, not re-derive it. Examples: plug a specific system into a formula derived in lecture; verify a property for a given state; compute a quantity using a method taught in class. These problems build fluency and confidence.
- **2–3 medium problems:** Transfer, comparison, or guided multi-step problems. Require adapting lecture material to a new context or combining two ideas.
- **1–2 hard/far problems:** Connection to other areas of physics, misconception testing, inversion, or edge-case exploration. These stretch understanding and prepare students for exam variations.

**The first 2–3 problems should be approachable by any student who attended the lecture.** The last 1–2 problems can be challenging. Never make all problems hard or all problems far from the lecture — students need to practice the basics before stretching.

**New anti-pattern (§3.6): All problems too far from lecture.** If every problem requires knowledge or context beyond what the lecture teaches, students cannot practice the core material. At least 2–3 problems must be solvable using only the lecture content and standard techniques.

---

## 2. Quality Principles — What Makes Homework Meaningful

Every problem should satisfy at least one of these six design principles. Problems that satisfy none are likely trivial or duplicative.

### 2.1 Transfer

> Apply a concept or method to a new context not shown in lecture.

The lecture proves a theorem for spin-1/2; the homework asks the student to work it out for spin-1. The lecture derives the density matrix for a thermal state; the homework asks for a different ensemble. **The student must adapt, not copy.**

### 2.2 Inversion

> Reverse the logical direction of a lecture derivation.

The lecture derives the output from the input; the homework gives the output and asks "what input produces this?" Example: lecture shows how to compute expectation values given a state; homework gives expectation values and asks to reconstruct the state.

### 2.3 Edge Cases and Limits

> Explore what happens at boundaries, special values, or limiting regimes.

What happens when the coupling goes to zero? When two energy levels become degenerate? When the system size goes to infinity? Edge cases reveal whether the student truly understands the structure or just memorized the generic formula.

### 2.4 Comparison

> Compare two methods, representations, or approximations on the same problem.

Solve the same problem in the Schrödinger and Heisenberg pictures. Compare exact and perturbative results. Use both position and momentum representations. This builds judgment about when to use which tool.

### 2.5 Connection

> Link the current topic to a different part of the course or to a different area of physics.

Show that a quantum result reduces to the classical limit. Connect an entanglement measure to a thermodynamic quantity. These problems build the knowledge graph and reinforce worldview.

### 2.6 Misconception Testing

> Design a problem where a common wrong approach gives a specific wrong answer.

The student must recognize why the naive method fails and apply the correct one. Example: using non-degenerate perturbation theory on a degenerate level gives a divergent answer — the student must recognize and switch to degenerate perturbation theory.

---

## 3. Anti-Patterns — Problems to Avoid

### 3.1 Lecture duplication

A problem that asks the student to "show that [exact result from lecture]" using the same method taught in lecture. The student (or AI) can copy the derivation verbatim. **Fix:** change the system, the method, or the direction (inversion).

### 3.2 Trivial table-copy

"Fill in the analogy table" or "list the properties of X" when the answer is a direct copy of a table or list already in the lecture notes. **Fix:** ask the student to *use* the table to solve a problem, or to extend it to a case not covered.

### 3.3 "Explain in N sentences"

Open-ended prompts with no concrete physics task. "Explain the significance of entanglement in 3 sentences." These are trivially answered by AI and test nothing on the exam. **Fix:** replace with a concrete conceptual question with a definite answer.

### 3.4 Tedious computation

Long algebra or numerical calculations that test patience, not understanding. If the main challenge is bookkeeping rather than physics, the problem is not exam-worthy. **Fix:** simplify the system or break into guided sub-parts.

### 3.5 Trick combinations

Problems requiring an unmotivated clever trick that students cannot be expected to discover. **Fix:** provide the trick as a hint, or restructure as guided sub-parts.

### 3.6 All problems too far from lecture

Every problem requires context, techniques, or physical systems not discussed in the lecture. Students who understood the lecture perfectly still cannot start the homework without external research. **Fix:** ensure the first 2–3 problems directly exercise lecture content — apply a formula, verify a property, compute a specific case.

---

## 4. Formatting Rules

### 4.1 Problem format

Every problem starts with a **bold number and short title** (1–5 words), followed by the task on the same line:

```
**N. Title.** Task sentence describing what to do...
```

**Problem voice:** Never use “a student” / “the student” in problem wording. Use imperative or impersonal tasks, or **one** for generic framing (“One might claim…,” “Suppose one measures…”). See `content-style.md` § Homework Design.

Rules:
- Number, period, title, and closing period are **all inside one bold span**: `**N. Title.**`
- The task continues on the same line after the closing `**` (inline, not standalone).
- Every problem **must** have a title — no bare `**N.** Show that...`.
- **ASCII words only inside the bold title** — no `$...$`, `\(...\)`, or LaTeX inside `**...**`. All math goes in the task text after the closing `**`.
- Do **not** use `**Problem.**`, `###` headings, or parenthetical titles like `(Topic)`.
- Capitalize the first word of every title.

### 4.2 Sub-parts

- Each sub-part `(a)`, `(b)`, ... starts on its **own line** with a blank line before it.
- **No subtitles** on sub-parts — `(a)` states the task directly, never `**(a) Title.**`.
- **Every sub-part must ask a question or assign a task** ("show that," "compute," "find," "explain why"). Never use a sub-part just to provide context.
- Part (a) should start simple; subsequent parts escalate.

### 4.3 Problem preamble

- If a problem needs extended context (more than ~2 sentences of setup), place it in a **preamble paragraph** between the title line and `(a)`.
- Do not bury context inside a sub-part.
- Use sub-parts to **guide step by step** through complexity.

### 4.4 Display math in homework

- `$$...$$` blocks MUST have **blank lines above and below**.
- Do NOT put blank lines inside a `$$...$$` block.
- For multiline equations, use `\begin{split}...\end{split}` inside `$$...$$`.
- Do NOT use `align` or `aligned` environments.

### 4.5 Cross-referencing

- Reference problems as `HW x.y.z.k` (e.g., `HW 6.1.2.3`).
- 5–10 problems per subsection.

---

## 5. Common Formatting Errors

These are frequently introduced during automated editing. Check for all of them after any homework edit.

| Error | Wrong | Right |
|-------|-------|-------|
| Trailing `**` | `**3. Title.** text **` | `**3. Title.** text` |
| Missing `$$` blank lines | `text\n$$\nE=mc^2\n$$\ntext` | `text\n\n$$\nE=mc^2\n$$\n\ntext` |
| Inline sub-parts | `text. (a) Find X. (b) Find Y.` | `text.\n\n(a) Find X.\n\n(b) Find Y.` |
| Lowercase title | `**2. spin precession.**` | `**2. Spin precession.**` |
| LaTeX in bold title | `**5. Limit ($\lambda$).**` | `**5. Short-wavelength limit.**` |
| Mixed bullets | `- X\n* Y\n- Z` | `- X\n- Y\n- Z` |
| “A student” in task text | `A student claims that…` | `One might claim that…` (or impersonal setup) |

---

## 6. Design Process

When creating or revising homework for a subsection notebook:

1. **Read the lecture cell** (cell 2). List the key concepts, results, and methods taught.
2. **Map one problem per major concept.** Ensure each problem satisfies at least one quality principle from §2.
3. **Check against anti-patterns** (§3). If a drafted problem matches an anti-pattern, redesign it.
4. **Format** according to §4. Use the problem format template.
5. **Verify physics** of "show that" targets — if unsure, flag for `science-reviewer` or note in `feedback.md`.
6. **Validate** after editing: run `python3 .claude/scripts/validate_project.py --scope <stem>` and `python3 .claude/scripts/audit_homework_format.py`.

### Problem mix guidance

For a typical subsection with 7–8 problems, arrange from easy/near to hard/far:

| Position | Difficulty | Distance from lecture | Type |
|----------|-----------|----------------------|------|
| P1–P2 | Easy | Near (direct application) | Apply a definition or formula from lecture to a concrete case; verify a property; compute a specific quantity |
| P3–P4 | Medium | Moderate (same topic, new angle) | Transfer to a new system; comparison of two methods; guided "show that" with sub-parts |
| P5–P6 | Medium–Hard | Moderate–Far | Inversion; edge case / limit; misconception testing |
| P7–P8 | Hard | Far (connection / extension) | Connection to other areas of physics; advanced application; open-ended conceptual challenge |

**Key constraint:** The first 2–3 problems must be solvable using only the lecture content. Not every subsection needs all types — match the problems to what the lecture actually teaches. If a lecture is computation-heavy, more "apply the method" problems are appropriate; if a lecture is conceptual, more "explain why" problems fit.

---

## 7. Audit Checklist

When reviewing existing homework:

- [ ] 5–10 problems?
- [ ] No “a student” / “the student” in problem wording (use imperatives or “one”)?
- [ ] Each problem has `**N. Title.** Task...` format?
- [ ] Titles are ASCII-only, capitalized?
- [ ] Sub-parts on separate lines with blank lines before each?
- [ ] Every sub-part has a concrete task (not just context)?
- [ ] No anti-patterns (§3)?
- [ ] Each problem satisfies at least one quality principle (§2)?
- [ ] Problems track the lecture content (not testing material from other sections)?
- [ ] Difficulty gradient: first 2–3 problems are easy/near-lecture, last 1–2 are hard/far?
- [ ] At least 2–3 problems are solvable using only lecture content (no external knowledge needed)?
- [ ] Display math has blank lines above and below `$$`?
- [ ] No trailing `**` or other formatting errors (§5)?
- [ ] Physics of "show that" targets verified?

---

## 8. Validation

After editing homework cells, run:

```bash
# Single notebook
python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate <path.ipynb>

# Full homework format audit
python3 .claude/scripts/audit_homework_format.py

# Scoped validation
python3 .claude/scripts/validate_project.py --scope <stem>
```

The validators check: homework line format (bold titles, sub-parts), `$$` spacing, banned patterns, notation consistency, and control character corruption.

---

## 9. LaTeX Conventions in Homework

Follow `rules/physics-conventions.md`:
- Vectors: `\boldsymbol{v}` (not `\vec{v}`)
- Operators: `\hat{H}`, `\hat{p}`
- Imaginary unit: `\mathrm{i}`; Euler: `\mathrm{e}`; differential: `\mathrm{d}`
- Kets: `\vert\psi\rangle` (use `\vert`, not `|`)
- Dot product `\cdot` only between vectors, never between scalars
- In homework JSON: beware Python escape sequences corrupting `\rho`, `\alpha`, `\beta`, `\frac` — always use raw strings or double backslashes

---

## References

- `rules/content-style.md` § Homework Design (canonical formatting rules)
- `rules/teaching-philosophy.md` (course strategy, role of homework)
- `rules/physics-conventions.md` (LaTeX notation)
- `rules/prompt-templates.md` (checklist for new notebooks)
- `rules/validation.md` (which validators to run)
- `rules/notebook-editing.md` (safe JSON editing)
- `skills/lecture-content/SKILL.md` (content review context)
- `skills/science-reviewer/SKILL.md` (physics verification)
- **`_refs/`** (project root): Professor's original lecture notes and `HOMEWORK.md` (original homework problems). Read the relevant `_refs/` file before designing problems to ensure alignment with the professor's presentation and notation. See `CLAUDE.md` § "Reference materials" for the chapter-to-file mapping.
