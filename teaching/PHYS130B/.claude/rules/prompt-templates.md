# Rule: Prompt templates and new-notebook checklist

## Prompt box template (x.y.z, cell 1)

```
:::{admonition} Prompts
:class: tip

- What is [concept], and why does [key property] follow? How does it differ from [related concept]?
- Derive [result]. Why does [notable feature] emerge from the derivation?
- How does [object A] relate to [object B]? What does this connection reveal about [physics]?
- For [specific setup], [compute/show] [quantity]. What does the result tell us about [interpretation]?
- Why does [surprising fact] hold? What would go wrong if [alternative]?
:::
```

Each prompt should be **specific enough** for an LLM to give a focused, lecture-relevant answer — name the concept or object precisely (short inline math like `$\hat{\rho}$` or `$K(x,t;x',t')$` is fine to identify objects). Avoid pasting full Hamiltonians or long expressions; refer to them by name instead.

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

**Comprehensive prompt guide:** For audit workflow, quality principles, and LLM-friendliness rules, see **`skills/prompt-auditor/SKILL.md`**.
