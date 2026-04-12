# Rule: Content Style and Structure

All notebooks must follow **`notebook-architecture.md`**, **`teaching-philosophy.md`** (course context), **`myst-references.md`**, **`prompt-templates.md`**, and this file.

## Cell Structure

### Subsection Notebooks (x.y.z) — 4 cells

| Cell | Content |
|------|---------|
| 0 | `# x.y.z Title` (dots in title) |
| 1 | Prompts admonition (`:class: tip`) with 4–5 guiding questions |
| 2 | `## Lecture Notes` → `### Overview` → body sections → `### Summary` |
| 3 | `## Homework` with 5–10 numbered problems |

### Section Parent Notebooks (x.y) — 3 cells

| Cell | Content |
|------|---------|
| 0 | `# x.y Section Title` |
| 1 | `## Overview` → motivating paragraph → `### Topics` table → `### Key Concepts` → `### Learning Objectives` |
| 2 | `## Project` → one research-level project |

## Admonition Usage

Full table of admonition classes and their designated roles. Every admonition in the notes must use one of these classes.

### Student-Facing Interactive Boxes

| Class | Role | Collapsed? | Placement |
|-------|------|------------|-----------|
| `tip` | **Prompts** — guiding questions for AI-assisted preview | No | Cell 1, x.y.z only |
| `tip` | **Discussion** — broad, deep questions for TA-led discussion sessions | Yes (`dropdown`) | Inline in cell 2 |
| `poll` | **Poll** — quick in-class multiple-choice conceptual checks | Yes (`dropdown`) | Inline in cell 2 |

- **Prompts** and **Discussion** both use `tip` (green, inviting). Differentiate by title: `Prompts` for preview questions, `Discussion` for TA-led sessions on broad, high-level topics.
- **Discussion** boxes are always collapsed (`dropdown tip`) so they don't interrupt lecture flow. They target open-ended, extended questions — not quick in-class exercises.
- **Poll** boxes use `poll dropdown` (collapsed by default). They are designed for live in-class use: the professor displays the question, students vote, then the class discusses. See **§ Poll Design** below for full rules.

### Content Boxes

| Class | Role | When to Use |
|-------|------|-------------|
| `important` | Core definitions, theorems, fundamental equations | Key results students must memorize and retain. Prominently visible, never collapsed. |
| `example` | Worked examples with detailed calculations | State the problem visibly; hide the full solution behind a `dropdown`. |
| `note` | Background, clarifications, physical intuition, paradox setup | Supplementary context that enriches understanding but isn't essential to the main argument. |
| `information` | Derivations and proofs | Extended mathematical derivations or formal proofs. Always collapsed (`dropdown information`). |
| `hint` | Nudge toward a solution; "think about...", "recall that..." | Brief pointers that guide reasoning without giving away the answer. |
| `seealso` | Cross-references, further reading, animations, external links | Pointers to related sections, textbook chapters, or online resources. |

### Warning Hierarchy (increasing severity)

| Class | Role | When to Use |
|-------|------|-------------|
| `attention` | Easy-to-miss subtleties and important distinctions | Surprising facts, non-obvious scope limitations, "this looks like X but is actually Y". |
| `caution` | Sign conventions, common pitfalls, easy algebraic mistakes | Mechanical errors students frequently make; wrong-sign traps, index confusion, etc. |
| `warning` | Serious conceptual traps | Deeper misunderstandings that lead to fundamentally wrong physics (e.g., confusing entanglement with correlation). |
| `danger` | Wrong approaches or formulas that do NOT apply | Explicitly flag methods that seem applicable but fail (e.g., using non-degenerate perturbation theory on a degenerate level). |
| `error` | Explicit misconceptions, wrong statements, frequent exam mistakes | "Students often claim X. This is wrong because..." — direct myth-busting. |

### Special

| Class | Role | When to Use |
|-------|------|-------------|
| `dropdown` | Collapsible container for derivations and extended content | Long derivations, proofs, or supplementary material that would interrupt flow. Combine with another class (e.g., `dropdown information` for derivations/proofs, `dropdown example` for worked examples, `dropdown note` for supplementary context). |
| `poll dropdown` | In-class poll / clicker prompts | Quick multiple-choice conceptual checks for live in-class voting. See **§ Poll Design**. |

### Usage Examples

**Prompts (cell 1):**
```
:::{admonition} Prompts
:class: tip

- Explain [main idea]. How does it differ from [related concept]?
- Walk me through [derivation]. What changes if [variation]?
:::
```

**Discussion (inline in cell 2, collapsed):**
```
:::{admonition} Discussion
:class: dropdown tip

[Debatable physics question grounded in specific content...]
:::
```

**Core result (always visible):**
```
:::{admonition} Spectral Theorem
:class: important

Every Hermitian operator $\hat{A}$ admits a spectral decomposition...
:::
```

**Worked example (problem visible, solution collapsed):**
```
:::{admonition} Example: Spin-1/2 Precession
:class: dropdown example

**Problem.** A spin-1/2 particle is prepared in $|+\rangle$ and placed in a field $\boldsymbol{B} = B\hat{z}$. Find $\langle \hat{\sigma}^x \rangle(t)$.

**Solution.** ...
:::
```


**Derivation / Proof (always collapsed):**
```
:::{admonition} Derivation: Schrödinger Equation from Path Integral
:class: dropdown information

[Step-by-step derivation...]
:::
```
**Misconception (myth-busting):**
```
:::{admonition} Misconception: "Entanglement = Correlation"
:class: error

Entanglement is NOT the same as classical correlation...
:::
```

## Poll Design

Polls are quick in-class multiple-choice questions for live voting. They test whether students absorbed the lecture content and help the professor diagnose misconceptions in real time.

### Purpose and philosophy

In the AI era, the key skills are **asking good questions** (to prompt AI efficiently) and **having good taste/intuition** (to critically evaluate AI answers and spot hallucinations). Polls should cultivate these skills, not just test rote problem-solving.

### Rules

- **At most 2 polls per lecture.** Some lectures may have zero — only add a poll where it fits naturally. Do not force polls into every notebook; do not be aggressive in adding them.
- **Closely tied to lecture content.** The poll must test understanding of material covered in the same lecture note. Do not introduce new concepts or diverge from the lesson's topic.
- **One definite correct answer.** Every poll has exactly one correct choice. The question must not be open-ended or ambiguous.
- **All distractors plausible.** Every wrong choice should be wrong for a specific, instructive reason — a particular misconception, reasoning error, or conceptual trap. No obviously absurd options.
- **Quick to answer.** A student with solid understanding should reach the correct answer in under a minute. The difficulty comes from needing the right *concept*, not from lengthy calculation.
- **Collapsed by default.** Use `dropdown poll` so polls don't interrupt the reading flow.

### What polls should test

- **Misconceptions and conceptual barriers** — expose common wrong intuitions.
- **Simple applications** — apply a definition or result to a concrete scenario.
- **Quick calculations or estimations** — a few lines at most, with a clear physical picture. No tedious number-crunching.
- **Physical modeling and framing** — "which of these is the right way to set up this problem?"
- **AI-era judgment** — "which of these AI-generated responses best answers the question?" or "how would you prompt an AI to solve this?" (grounded in physics content, not prompt engineering per se).

### Format

Title: `Poll: [short topic phrase]`. Choices labeled `(A)`, `(B)`, `(C)`, `(D)` — typically 3–4 choices. Answer indicated at the end inside a nested collapsed block.

```
:::{admonition} Poll: Phase factor observability
:class: dropdown poll

A qubit state $\vert\psi\rangle = \mathrm{e}^{\mathrm{i}\phi}\vert 0\rangle$ differs from $\vert 0\rangle$ by a global phase. Which statement is correct?

(A) The two states give different measurement probabilities in the $Z$ basis.

(B) The two states give different measurement probabilities in the $X$ basis.

(C) The two states are physically indistinguishable by any measurement.

(D) The global phase becomes observable when the qubit is part of a two-qubit system.

:::
```

### Post-vote pedagogy (instructor guidance)

After the vote, do not immediately reveal the answer. If the class is split, ask one student from each side to give a one-sentence justification. Each wrong choice maps to a specific misconception that the professor can address based on the vote distribution.

## Banned Patterns

- `---` horizontal rules (causes docutils crash)
- Nested `:::` admonitions (breaks rendering)
- `plt.show()` in widgets (use `display(fig)` + `plt.close(fig)`)
- Bare `### Application:` headings (wrap in `example` admonition instead)

## Content Philosophy

- Keep content minimal and concise — teach essential ideas, cut the rest
- Lead with **why** before **how**
- Key results stay visible; extended derivations go in `:::{dropdown}`
- Each `###` section is a self-contained conceptual unit
- End subsections with `### Summary` (3–5 bullets)
- Connect new material to prior topics (build the knowledge graph)

## Ongoing maintenance (narrative and bloat)

- **One thread per lesson**—each section advances the same main question; cut tangents that do not serve it.
- **Prefer tightening** over adding: merge redundant paragraphs; do not duplicate derivations already standard elsewhere unless this lesson truly needs a self-contained version (then keep it short or in a dropdown).
- **Worked examples** are welcome when they are **short, single-purpose, and on-topic** (e.g. one explicit calculation, or one “how to apply this definition” walkthrough). Skip examples that introduce new topics or long side stories.
- **Prompts and homework** should track the lecture actually present—revise them when the lecture is trimmed or refocused (`skills/lecture-content/SKILL.md`).

## Homework Design

- 5–10 problems per subsection
- Each problem targets one concept or skill
- Mix: conceptual questions, short derivations, "show that" proofs, physical reasoning
- Avoid tedious computation or trick combinations
- Problems appear on the final exam — they must test understanding, not procedure
- Cross-ref problems as `HW x.y.z.k`
- **Difficulty gradient:** first 2–3 problems should directly exercise lecture content (easy, near-lecture); middle problems transfer or compare; last 1–2 can be hard/far-reaching. See `skills/homework-designer/SKILL.md` § Difficulty distribution.

### Problem format

Every problem starts with a **bold number and short title** (1–5 words), followed by the task:

```
**N. Title.** Task sentence describing what to do...
```

- **Homework voice:** Do **not** address the reader as “a student” or “the student.” Phrase tasks impersonally (“Show that…,” “Compute…,” “Explain why…”) or use **one** for a generic agent (“One might claim…,” “Suppose one measures…”). Same convention for quoted misconceptions: prefer “One might argue: …” over “A student says: ….”
- A **single-word title** is allowed (e.g. standard acronyms such as WKB, or names such as SU(2)).
- The number, period, title, and closing period are **all inside one bold span**: `**N. Title.**`
- The task continues on the same line after the bold span (inline title, not standalone).
- Do **not** use `**Problem.**`, `###` headings, or parenthetical titles like `(Topic)` for individual problems.
- Every problem **must** have a title — no bare `**N.** Show that...` without a topic phrase.
- **ASCII words only inside the bold title** — the span `**N. Title.**` must contain plain words (letters, digits, apostrophe, hyphen, period); do **not** put `$...$`, `\(...\)`, display math, or other LaTeX inside it. Put **all mathematics in the task text** that follows the closing `**` (immediately after `**N. Title.**` on the same line). Math inside the bold span can place a literal `**` next to punctuation and **break Markdown bold parsing** (e.g. a truncated `$\lambda.**` closes bold early and corrupts the line).

**Examples:**

```
**3. Spin precession.** A spin-1/2 particle is placed in a magnetic field $\boldsymbol{B} = B\hat{z}$. Show that $\langle \hat{\sigma}^x 
angle(t)$ oscillates at the Larmor frequency.

**5. Landau-Zener transition.** Consider a two-level system with Hamiltonian $\hat{H}(t) = \alpha t\,\hat{\sigma}^z + \Delta\,\hat{\sigma}^x$.

(a) Find the instantaneous eigenvalues $E_\pm(t)$ and the minimum gap.

(b) In the adiabatic limit $\alpha \to 0$, argue that the system stays in the ground state.

(c) Show that the transition probability is $P = \mathrm{e}^{-\pi\Delta^2/\hbar\alpha}$.
```

### Sub-parts

- Each sub-part `(a)`, `(b)`, ... starts on its **own line** (blank line before each for MyST paragraph separation).
- **No subtitles** on sub-parts — `(a)` states the task directly, never `**(a) Title.**`
- **Every sub-part must ask a question or assign a task** ("show that," "compute," "find," "explain why"). Never use a sub-part just to provide context or reading without a clear action.
- Part (a) should start simple; subsequent parts escalate.

### Problem preamble and complexity

- If a problem needs extended context or motivation (more than ~2 sentences of setup), place it in a **preamble paragraph** between the title line and `(a)`. Do not bury context inside a sub-part.
- Use sub-parts to **guide step by step** through a complex problem, rather than front-loading a wall of text with a single open-ended question.
- Keep problems focused: each problem tests one concept or skill. If a problem sprawls into many unrelated sub-parts, consider splitting it.

### Common formatting errors to avoid

These errors are frequently introduced during automated reformatting or editing. **Preventive checklist** for all homework cells:

1. **Mismatched bold markers** — Extra closing `**` at end of problem line.
   - Wrong: `**3. Spin precession.** Setup text **`
   - Right: `**3. Spin precession.** Setup text` (no trailing `**`)
   - Prevention: Verify each problem line has exactly one `**` pair wrapping number + title + period.

2. **Missing blank lines around `$$` blocks** — Display math fused to surrounding text.
   - Wrong: `Some text
$$
E=mc^2
$$
More text` (no blank lines)
   - Right: `Some text

$$
E=mc^2
$$

More text` (blank lines above and below)
   - Prevention: Every `$$` block in homework must have a blank line before and after (see **`myst-references.md`**).

3. **Inline sub-parts** — Sub-part labels `(a)`, `(b)` run on the same line as preceding text.
   - Wrong: `**1. Title.** Setup text. (a) Find X. (b) Find Y.`
   - Right: `**1. Title.** Setup text.

(a) Find X.

(b) Find Y.`
   - Prevention: Each sub-part starts on its own line with a blank line before it (see **§ Sub-parts** above).

4. **Lowercase problem titles** — First word of title not capitalized.
   - Wrong: `**2. spin precession.** A particle...`
   - Right: `**2. Spin precession.** A particle...`
   - Prevention: Always capitalize the first word of every problem title; use title case for multi-word titles.

5. **Mixed list syntax** — Inconsistent bullet markers (`-` vs `*`) within a single problem's sub-parts or preamble.
   - Wrong: `- Point 1
* Point 2
- Point 3`
   - Right: `- Point 1
- Point 2
- Point 3` (or all `*`; be consistent)
   - Prevention: Pick one bullet style per problem and use it consistently throughout sub-parts and preambles.

6. **LaTeX inside the bold homework title** — Math or backslash commands between `**` and `**`.
   - Wrong: `**5. Limit ($\lambda \to 0$).** In the short-wavelength limit...` (risk of `**`/`$` interaction and duplicated text)
   - Right: `**5. Stationary Phase and Fermat.** In the short-wavelength limit ($\lambda \to 0$, so $k_0 \to \infty$), argue...`
   - Prevention: Keep `**N. Title.**` to ASCII words only; put every formula in the task after the closing `**` (see **§ Problem format** above).

**Validation:** After editing a homework cell, inspect the raw markdown by comparing rendered output against these rules. `validate_project.py` enforces homework line format (see `scripts/homework_format.py`); run `audit_homework_format.py` for a homework-only listing (`rules/validation.md`).

**Comprehensive homework guide:** For quality principles (Transfer, Inversion, Edge cases, Comparison, Connection, Misconception testing), anti-patterns, and the full design process, see **`skills/homework-designer/SKILL.md`**.


## Project Design (x.y level)

- One research-level project per section
- Must be at the frontier of physics research
- Requires literature survey, computation, and scientific writing
- Achievable in ~2 weeks with AI assistance
- NOT a big homework problem — genuine scientific inquiry
