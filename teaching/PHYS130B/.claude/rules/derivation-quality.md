# Rule: Derivation Quality and Reference-Note Alignment

This rule codifies lessons learned from recurring quality gaps between the lecture notes and the professor's original reference notes (`_refs/`). It applies to every derivation, worked example, and physics argument in the notebooks.

## Scope of `_refs/` alignment

Two layers — keep them separate:

- **Math derivation and physics argument** (the *content* of each step): follow `_refs/` closely. Notation, sign conventions, intermediate algebraic steps, the chain of building-block identities, the physical interpretation of each move — these track the professor's reference. Step counts and granularity match `_refs/` line for line (see § Mandatory detail level).
- **Lecture flow and narrative storyline** (the *order* in which concepts are introduced): the new lecture is **free** to design its own sequence. Section ordering, which concept motivates which, when each object enters, what bridges connect sections — these are pedagogical choices the new note makes; they are **not** required to mirror `_refs/`.

A derivation that is technically correct against `_refs/` but **pulls concepts in from later sections** of the new lecture (objects the body has not yet introduced at the point the dropdown appears) is a rule violation, even if those concepts appear earlier in the reference. See § Scope and pedagogical fit and the corresponding anti-pattern below.

## Scope and pedagogical fit

Two scope rules — both required:

1. **One focus per derivation.** Every derivation must isolate **a single point**: one identity, one chain-rule application, one commutator evaluation, one limiting argument. Combining unrelated steps into a single dropdown ("derive X *and* show Y *and also* establish Z") dilutes pedagogical purpose and almost always pulls the derivation out of context.

2. **Stay in context with the surrounding lecture.** A derivation may **only** invoke concepts, definitions, and notation that the surrounding lecture body has *already* introduced by the point at which the dropdown appears. If a notion (e.g. covariant derivative, gauge potential, connection field) is introduced in a later section, do not name or use it inside an earlier derivation. The derivation can *motivate* the next section without preempting it — for example, by closing with "absorbing this requires a structure built next" rather than by writing down the structure itself.

These rules separate the *flow of the lecture* (which the new note designs freely) from the *math and physics of each step* (which follows `_refs/`). "Adding detail" to a derivation always means slicing existing steps finer for student readability — never expanding the derivation's topical scope (see § Mandatory detail level).

## Root causes of quality gaps

Five failure modes have been identified. Every one has occurred multiple times in this project; none is hypothetical.

1. **Skipped intermediate steps.** The derivation jumps from premises to conclusions without showing the evaluations that connect them. The reference note includes those steps because they are where students learn; the lecture note omits them because the AI author "already knows" the answer. *Example:* 4-1-2 stated $[\hat{\pi}_i, f(\boldsymbol{x})] = -\mathrm{i}\hbar\,\partial_i f$ without explaining why $\hat{\pi}$ inherits this from $[\hat{p}, f(\boldsymbol{x})]$.

2. **Misleading notation choices.** The note uses a mathematically correct but pedagogically confusing form when a clearer equivalent exists. *Example:* writing $[\hat{\pi}/m, \hat{H}]$ instead of $[\hat{v}, \hat{H}]$ — students read $\hat{\pi}/m$ as a possible typo for $\hat{p}/m$ and cannot tell which operator is meant.

3. **Wrong notation (index errors, unit-system errors).** Tensor indices, metric signatures, or unit conventions are silently wrong. *Example:* a table listing $A_\mu = (\phi, \boldsymbol{A})$ when the metric convention requires $A^\mu = (\phi, \boldsymbol{A})$ and $A_\mu = (\phi, -\boldsymbol{A})$.

4. **Missing motivation for "why this form."** The note presents a result without explaining what question it answers or why the chosen form is natural. The student memorizes an expression without understanding its origin. *Example:* the Heisenberg equation $\mathrm{d}\hat{v}/\mathrm{d}t = [\hat{v}, \hat{H}]/(\mathrm{i}\hbar) + \partial_t \hat{v}$ appears without explaining that $\hat{v}$ has explicit time dependence through $\boldsymbol{A}(\hat{\boldsymbol{x}}, t)$, so the partial-derivative term is essential.

5. **Reverse-engineering from the answer.** The derivation is written by starting from the known final result and working backward, pulling in prefactors and symbol switches that have no forward motivation. *Example:* a $1/A$ factor appears in a formula because the target result uses current density $\hat{J} = (1/A)\sum_n \hat{j}^{(n)}$, but the derivation never defines $\hat{J}$ or explains the symbol change from $\hat{j}$ to $\hat{J}$.

## Mandatory procedure: derivation authoring

### Before writing

1. **Read the corresponding `_refs/` file.** Locate the matching section. Note its **logical structure**: what identities does it state first? What building-block results does it derive before the main result? What intermediate steps does it show? This sets the math content (chain of identities) and physics argument the new derivation must reproduce. **Do not** copy the reference's *narrative position* — section ordering, which idea motivates which, when each object enters — into the new note. The new lecture is free to sequence sections differently, and the derivation must respect the new lecture's flow (see § Scope and pedagogical fit). If `_refs/` derives the same identity *after* introducing an object that the new lecture introduces *later*, drop that object from the derivation rather than dragging it forward.

2. **Outline the logical chain.** Before writing any LaTeX, write a numbered list (for yourself, not in the notebook) of the key steps: "Step 1: state commutator identity. Step 2: evaluate $[\hat{\pi}, \hat{x}]$ from $[\hat{p}, \hat{x}]$. Step 3: …" Each step must follow from the previous one without hidden algebra.

3. **Choose notation deliberately.** For every operator, index, or symbol, ask: "Will a student reading this for the first time confuse it with something else?" If yes, pick the unambiguous form and add an explicit note distinguishing the two. Refer to `physics-conventions.md` for mandatory conventions.

### While writing

4. **Show every commutator / identity evaluation.** When a derivation uses a commutator $[A, B]$, either (a) the result is a well-known identity already stated or derived in the same notebook, or (b) the evaluation is shown explicitly in the dropdown. "It can be shown that" is banned in derivation dropdowns.

5. **State building-block results first.** Structure the dropdown as: (i) building-block identities (with evaluation), (ii) assembly into the main result, (iii) final simplification. This matches the reference-note structure and gives the reader a roadmap.

6. **Explain where each term comes from.** When a term appears in an intermediate expression, the reader must be able to trace it to a specific step. Add parenthetical citations like "(from Eq. above)" or "(using $[\hat{\pi}_i, x_j] = -\mathrm{i}\hbar\delta_{ij}$)."

7. **Flag explicit vs implicit time dependence.** When an operator $\hat{O}$ depends on time both through the Heisenberg evolution and through explicit parameters (e.g., external fields $\boldsymbol{A}(\boldsymbol{x}, t)$), state this clearly before invoking the Heisenberg equation. Never let a $\partial_t \hat{O}$ term appear without prior explanation of why $\hat{O}$ has explicit time dependence.

### After writing

8. **Structural diff against `_refs/`.** Re-read the reference derivation and compare the logical chain step by step. Check:
   - Does the lecture note include every identity the reference note derives?
   - Does the lecture note show every intermediate evaluation the reference shows?
   - Are there steps the reference note takes that the lecture note skips?
   If any step is missing, add it — or justify its omission (e.g., it duplicates a result derived in an earlier subsection, cited by equation label).

9. **Student-confusion test.** For every expression in the derivation, ask: "Could a student misread this as a different expression?" Check for:
   - Operators that look like typos for other operators ($\hat{\pi}/m$ vs $\hat{p}/m$).
   - Index positions that could be flipped ($A_\mu$ vs $A^\mu$).
   - Symbols that collide with other uses in the same notebook ($\phi$ for both flux and potential).

10. **Notation-convention sweep.** After any edit involving operator algebra, tensor indices, or electromagnetic quantities, re-read `physics-conventions.md` and verify compliance. Run `validate_project.py --scope <stem>` to catch automated checks.

## Minimum derivation depth

A derivation dropdown in these notes serves as the **reference-grade proof** that a student (or AI) can follow step by step. The bar is:

- **Every claimed identity must be either (a) proved in-place, (b) derived in an earlier notebook and cited by equation label, or (c) a standard textbook result stated with a citation.**
- **No "it follows that" gaps.** If two consecutive displayed equations differ by more than simple algebra (distributing, collecting terms), the intermediate step must be shown.
- **Commutator evaluations are shown, not quoted**, unless the same commutator was evaluated earlier in the same cell and can be cited.

Short derivations (< 10 lines) are fine when the result genuinely follows in 2–3 steps. But if a derivation is short because steps were skipped, it fails this rule.

### Mandatory detail level: match `_refs/`

The professor's original lecture notes (`_refs/`) set the **binding standard** for how many intermediate algebraic steps a derivation must show. The lecture notes must match that level of detail line for line — not compress it, summarize it, or "streamline" it.

**What "match `_refs/`" means — and what it does not.** The line counts below set the *depth* of intermediate algebra each derivation must expose: how many product-rule applications, commutator expansions, or substitutions are visible, written for a student who needs every step. They do **not** set the *scope* of the derivation. *Adding detail* means making each step of the same focused calculation more student-friendly — slicing a 2-line jump into its 4 underlying lines — never importing additional building-block results, downstream conclusions, or material from later sections of the new lecture (see § Scope and pedagogical fit). A derivation that grows past its single focus, or that names objects the surrounding body has not yet introduced, is too long even if it nominally matches a `_refs/` line count.

**Concrete calibration from `_refs/PhaseAndGauge.md`:**

- **Canonical commutation relation** $[\hat{x}_i, \hat{p}_j] = \mathrm{i}\hbar\delta_{ij}$: 4 displayed lines (act on test function $\psi$, expand product rule, cancel, conclude).
- **$[\hat{\boldsymbol{x}}, (\hat{\boldsymbol{p}} - \hat{\boldsymbol{A}})^2]$**: 6 displayed lines (expand with product rule for commutators, use $[\hat{x}_i, \hat{p}_j - qA_j] = [\hat{x}_i, \hat{p}_j]$, substitute $\mathrm{i}\hbar\delta_{ij}$, collect symmetric pair, simplify, write in vector form).
- **$[\hat{\pi}_i, \hat{\pi}_j]$**: 7 displayed lines (expand $[\hat{p}_i - A_i, \hat{p}_j - A_j]$, keep only $[p,A]$ cross terms, rewrite using $[\hat{p}_i, \hat{x}_k]\partial_k A_j$, substitute $\mathrm{i}\hbar\delta_{ik}$, simplify to $\partial_i A_j - \partial_j A_i$, use Levi-Civita identity, arrive at $\mathrm{i}\hbar\epsilon^{ijk}B_k$).
- **$[\hat{\pi}, \hat{\pi}^2]$**: 4 displayed lines (product rule, substitute $[\hat{\pi}_i, \hat{\pi}_j]$, symmetrize, write as cross products).
- **$[\hat{\pi}, \phi]$**: 4 displayed lines (drop $A$ term, apply $[p,f]$ identity, substitute $-\mathrm{i}\hbar\delta_{ij}$, simplify to $-\mathrm{i}\hbar\nabla\phi$).
- **Velocity operator** $\partial_t\hat{\boldsymbol{x}}$: 5 displayed lines (Heisenberg equation, expand $H$, drop $\phi$ commutator, substitute building-block result, simplify).
- **Acceleration operator** $\partial_t^2\hat{\boldsymbol{x}}$: 7 displayed lines (split into explicit + Heisenberg parts, expand commutator with $H$, separate kinetic and potential pieces, substitute building blocks, factor out $1/m$, identify $\hat{\boldsymbol{E}}$, write final Lorentz form).

**Rule:** Each commutator evaluation or algebraic derivation in a dropdown must contain **at least as many displayed intermediate lines as the corresponding passage in `_refs/`**. Typically this means **4–7 lines per commutator evaluation**. A 2-line commutator that skips from the definition to the answer is a rule violation unless the result genuinely follows in one step of trivial algebra (e.g., substituting a single known identity with no further simplification).

**How to check compliance:** After writing a derivation, open the matching `_refs/` file, locate the same derivation, and count the displayed equation lines. If the lecture note has fewer lines, it is almost certainly skipping steps that the professor considered important. Add the missing lines.

**Why this level of detail matters:** The reference notes were written by the professor for students to follow step by step. Every intermediate line exists because the professor judged that a student needs to see that step to understand the derivation. AI authors consistently underestimate how many steps students need — they compress 5-step evaluations into 2-line results because the AI "already knows" the answer. This compression is the single most common quality gap in the project.

## Anti-patterns

| Anti-pattern | What to do instead |
|---|---|
| "It can be shown that $[A,B] = C$" | Show the evaluation, or cite the equation where it was shown. |
| Using an operator form that looks like a typo for a simpler one | Use the clearest name ($\hat{v}$ not $\hat{\pi}/m$) and define it. |
| Index placement copied from a different metric convention | Check `physics-conventions.md` § Electromagnetic Units before writing any $A_\mu$ or $A^\mu$. |
| A prefactor ($1/A$, $1/V$, $\sum_n$) appears without a definition step | Define both the per-particle and collective symbols before the derivation. |
| Writing the final result first, then backfilling a "derivation" | Write forward: premises → building blocks → assembly → result. |
| "By the Heisenberg equation, $\dot{O} = [O,H]/(i\hbar)$" for an operator with explicit $t$-dependence | State the full Heisenberg equation including $\partial_t O$, and explain why that term is present. |
| **Importing concepts the lecture body has not yet introduced** (e.g. naming covariant derivatives, gauge potentials, or other later-section objects in an earlier dropdown) | Rewrite using only what the surrounding body has already established at this point. Close with a forward-pointer ("absorbing this requires a structure built next") if a tease is helpful, but **do not** name or use the not-yet-introduced object. If the derivation genuinely needs the later object, move the dropdown to that section. |
| **Expanding scope under the banner of "more detail"** (turning a focused single-point derivation into a multi-topic chain that imports follow-on results) | Slice each existing step into finer student-friendly steps, but keep the derivation's topical focus unchanged. New topics → separate dropdowns (or no dropdown). |

## Relation to other rules

- **Notation and conventions:** `physics-conventions.md` (mandatory).
- **Cell structure and admonitions:** `content-style.md`, `notebook-architecture.md`.
- **Symbol audits (case/sub/super collisions):** `notebook-editing.md` § Related-symbol audit.
- **Maintenance scope:** `maintenance-scope.md` — this rule does not license wholesale rewrites; apply it when editing or auditing a specific derivation.
- **Skill workflow:** **`skills/derivation-designer/SKILL.md`** must run this file’s **full** mandatory procedure (**read `_refs/` first** → **outline chain** → **every intermediate** → **structural diff afterward**) for **any** derivation touch, scoped to the specific derivation—**`skills/notebook-writer/SKILL.md`** applies proposals **and** runs **`validation.md`** after each save.
