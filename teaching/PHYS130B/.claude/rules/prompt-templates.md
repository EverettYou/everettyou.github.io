# Rule: Prompt templates and new-notebook checklist

## Prompt box template (x.y.z, cell 1)

```
:::{admonition} Prompts
:class: tip

- Explain [main idea]. How does it differ from [related concept]?
- What is [structure]? Why does [consequence] follow?
- Walk me through [derivation]. What changes if [variation]?
- Given [scenario], use [method] to find [quantity]. Work a concrete example.
- [Conceptual question that may stress-test AI answers]
:::
```

Student-facing prompt frameworks: **COSTAR** (Context, Objective, Style, Tone, Audience, Response), **RACE** (Role, Action, Context, Expectation), **CREATE** (Character, Request, Examples, Additions, Type, Extras).

## Checklist (new or heavily edited x.y.z notebooks)

- [ ] Content: minimal, principled, connected
- [ ] Cell 0: `# x.y.z Title` (dots)
- [ ] Cell 1: Prompts, `:class: tip`, 4–5 questions
- [ ] Cell 2: `## Lecture Notes` → `### Overview` → body → `### Summary`
- [ ] No `---`; no nested `:::`
- [ ] Key equations labeled; citations via `` {eq}`...` ``
- [ ] Figures use `:name:` when cross-referenced
- [ ] Cell 3: `## Homework` — every problem has `**N. Title.** Task...` format; sub-parts on new lines with clear tasks; no “a student” / “the student” in problem wording (imperatives or “one”); see `content-style.md` § Homework Design
- [ ] Widgets: `display(fig)` / `plt.close(fig)`, `Output` before callbacks

See **`content-style.md`** for admonition classes and homework/project norms.
