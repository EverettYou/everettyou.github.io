# Rule: Content Style and Structure

All notebooks must follow the structure and style defined in design.md.

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
| `tip` | **Discussion** — physics questions for in-class debate | Yes (`dropdown`) | Inline in cell 2 |

Both Prompts and Discussion use `tip` (green, inviting). Differentiate by title: `Prompts` for preview questions, `Discussion` for in-class debate. Discussion boxes are always collapsed (`dropdown tip`) so they don't interrupt lecture flow.

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
| `poll dropdown` | In-class poll / clicker prompts | Optional quick-poll questions, collapsed by default. |

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

## Homework Design

- 5–10 problems per subsection
- Each problem targets one concept or skill
- Mix: conceptual questions, short derivations, "show that" proofs, physical reasoning
- Avoid tedious computation or trick combinations
- Problems appear on the final exam — they must test understanding, not procedure
- Number format: `**1.** [statement]`, cross-ref as `HW x.y.z.k`

## Project Design (x.y level)

- One research-level project per section
- Must be at the frontier of physics research
- Requires literature survey, computation, and scientific writing
- Achievable in ~2 weeks with AI assistance
- NOT a big homework problem — genuine scientific inquiry
