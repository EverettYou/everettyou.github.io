# Rule: Cell-1 prompt preview (law)

**MyST shells, skeleton bullets, and style-matched examples** live in **`skills/prompt-designer/TEMPLATES.md`**. Those templates must satisfy this file and match **current** subsection notebooks (e.g. `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` cell 1).

Student-facing prompt frameworks (pedagogical vocabulary only): **COSTAR** (Context, Objective, Style, Tone, Audience, Response), **RACE** (Role, Action, Context, Expectation), **CREATE** (Character, Request, Examples, Additions, Type, Extras).

## LLM preview prompt criteria (normative)

Cell-1 **Prompts** are **LLM input strings** for pre-class preview—not homework or exam items. Each bullet **must**:

1. **Be specific** — Name the concept/object and the angle (level, comparison, or mechanism). Avoid bare one-liners (“What is X?”) unless expanded so a general LLM can answer in a **lecture-aligned** way.
2. **Use math as naming, not as task** — Short inline math is fine to identify objects (e.g. propagator, purity). Do **not** lead with long Hamiltonians; do **not** turn the prompt into computation homework (“Compute …”, “Starting from $\hat H=\ldots$ derive …”).
3. **Keep one main topic per bullet** — A two-part question on the *same* thread is OK; unrelated multi-step chains in one bullet are not.
4. **Track cell 2** — After lecture edits, every prompt must still map to content actually in the lecture cell.
5. **Cover the lecture’s key ideas** — No topics that exist only in later sections/homework/textbook; no two bullets duplicating the same idea.
6. **Vary prompt types** — Mix conceptual, derive+why, connection, application, contrast as fits; **4–5** bullets typical for a subsection lesson.
7. **Stay respectful and impersonal** — No “students find this hard”; no deficit framing.
8. **Respect notebook level** — Prompts admonition appears **only** in subsection **x.y.z** notebooks; section parents use Overview per **`notebook-architecture.md`**.
9. **Be self-contained** — No `§…` refs, “previous lecture”, or unit numbering the LLM cannot resolve; use standard physics names instead.

## Prompt anti-patterns (normative)

| Anti-pattern | Required response |
|--------------|-------------------|
| Bare concept only | Add scope and “why it matters” (criterion 1). |
| Full Hamiltonian / long expression as setup | Name the object in words; keep math to short identifiers. |
| Unrelated compound chain in one bullet | Split into separate bullets. |
| Topic not in cell 2 | Remove or replace. |
| “Students / you may not know …” | Ask the physics directly. |
| Homework-style “Show that …” preview | Rephrase as mechanism / intuition / “why,” not graded computation. |
| More than ~6 prompts | Trim to 4–5 essentials. |
| Internal course cross-refs (`§`, “last time”) | Rewrite with self-contained naming (criterion 9). |
| Umbrella prompt with no anchor | Add distinguishing context (criterion 1). |

**Workflow** (audit order, handoff to `notebook-writer`): **`skills/prompt-designer/SKILL.md`**.
