# Rule: Maintenance scope and editorial judgment

Lecture notes are **mature**. Default stance: **preserve structure and physics**; improve **clarity, flow, and alignment** with `rules/` (especially `teaching-philosophy.md`, `notebook-architecture.md`, `content-style.md`).

## Prefer

- **One clear thread per lesson**—reader always knows what question the section answers.
- **Tighter prose**—cut redundancy; merge duplicate explanations across paragraphs.
- **Visible essentials**—definitions and key results easy to find; long derivations in `dropdown` per `content-style.md` / `notebook-architecture.md`.
- **Targeted mini-examples** when they teach **one** idea: a short calculation, or “how to use this object / this step”—**simple, explicit, on-topic**. No digressions framed as examples.

## Avoid

- Scope creep (new topics not needed for the lesson’s goal).
- “While we’re here” sections that break narrative.
- Large-scale reorganization without human sign-off.
- Replacing correct, stable content with speculative rewrites.

## When to stop and escalate

- Ambiguous physics or conflicting sources → note in `feedback.md` or ask the instructor; do not guess.
- Filename / TOC / cross-chapter moves → confirm before executing; grep for backlinks.

## Coordination

If multiple editors could touch the same notebook, serialize writes; always **read before write** and **validate after** (`rules/validation.md`).
