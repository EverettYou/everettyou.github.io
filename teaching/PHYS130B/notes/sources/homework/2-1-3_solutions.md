# 2.1.3 Second Quantization
Worked solutions for the homework problems in the [2.1.3 Second Quantization](../ch2_identical-particles/2-1-3-second-quantization) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Fock states from the vacuum.** Use the bosonic action rules $\hat{b}^\dagger\vert n\rangle = \sqrt{n+1}\vert n+1\rangle$, $\hat{b}\vert n\rangle = \sqrt n\vert n-1\rangle$, and the vacuum condition $\hat{b}\vert 0\rangle = 0$.

(a) Apply $\hat{b}^\dagger$ to $\vert 0\rangle$ once, twice, and three times, tracking the $\sqrt{n+1}$ prefactor at each step. Use induction to show that

$$
\vert n\rangle = \frac{(\hat{b}^\dagger)^n}{\sqrt{n!}}\,\vert 0\rangle.
$$

(b) Compute the matrix elements $\langle m\vert\hat{b}^\dagger\vert n\rangle$ and $\langle m\vert\hat{b}\vert n\rangle$ in the Fock basis. Conclude that $\hat{b}^\dagger$ is super-diagonal and $\hat{b}$ is sub-diagonal — they connect only Fock states differing by one quantum.

(c) Verify directly from the action rules that $\hat{b}^\dagger\hat{b}\vert n\rangle = n\vert n\rangle$ and $\hat{b}\hat{b}^\dagger\vert n\rangle = (n+1)\vert n\rangle$. Subtract to recover $[\hat{b},\hat{b}^\dagger]\vert n\rangle = \vert n\rangle$ on every Fock state — the algebra emerges from the state action, not the other way around.

(d) The harmonic-oscillator position operator is $\hat{x} = x_0(\hat{b} + \hat{b}^\dagger)$ with $x_0 = \sqrt{\hbar/(2m\omega)}$. Compute $\langle m\vert\hat{x}\vert n\rangle$ and identify the **dipole selection rule**: $\hat{x}$ connects only Fock states with $\vert m - n\vert = 1$.

**Solution.**

Work in a single mode; drop the subscript on $\hat b$.

(a) Apply $\hat{b}^\dagger$ step by step starting from $\vert 0\rangle$:

$$
\hat{b}^\dagger\vert 0\rangle = \sqrt 1\,\vert 1\rangle = \vert 1\rangle,
$$

$$
(\hat{b}^\dagger)^2\vert 0\rangle = \hat{b}^\dagger\vert 1\rangle = \sqrt 2\,\vert 2\rangle,
$$

$$
(\hat{b}^\dagger)^3\vert 0\rangle = \sqrt 2\,\hat{b}^\dagger\vert 2\rangle = \sqrt 2\sqrt 3\,\vert 3\rangle = \sqrt{3!}\,\vert 3\rangle.
$$

Each $\hat{b}^\dagger$ pulls out one $\sqrt{n+1}$ factor as it raises the occupation. *Induction:* assume $(\hat{b}^\dagger)^n\vert 0\rangle = \sqrt{n!}\,\vert n\rangle$. Then

$$
(\hat{b}^\dagger)^{n+1}\vert 0\rangle = \hat{b}^\dagger\sqrt{n!}\,\vert n\rangle = \sqrt{n!}\,\sqrt{n+1}\,\vert n+1\rangle = \sqrt{(n+1)!}\,\vert n+1\rangle,
$$

closing the induction. Hence $\vert n\rangle = (\hat{b}^\dagger)^n/\sqrt{n!}\,\vert 0\rangle$. The $\sqrt{n!}$ normalisation is the cumulative product $\sqrt 1\cdot\sqrt 2\cdots\sqrt n$ — boson enhancement compounded across $n$ insertions.

(b) From the action rules and orthonormality $\langle m\vert k\rangle = \delta_{mk}$:

$$
\langle m\vert\hat{b}^\dagger\vert n\rangle = \sqrt{n+1}\,\langle m\vert n+1\rangle = \sqrt{n+1}\,\delta_{m,n+1},
$$

$$
\langle m\vert\hat{b}\vert n\rangle = \sqrt n\,\langle m\vert n-1\rangle = \sqrt n\,\delta_{m,n-1}.
$$

As infinite matrices in the basis $\{\vert 0\rangle,\vert 1\rangle,\vert 2\rangle,\ldots\}$,

$$
\hat{b} = \begin{pmatrix} 0 & \sqrt 1 & 0 & 0 & \cdots\\ 0 & 0 & \sqrt 2 & 0 & \cdots\\ 0 & 0 & 0 & \sqrt 3 & \cdots\\ \vdots & & & & \ddots\end{pmatrix}, \qquad \hat{b}^\dagger = \begin{pmatrix} 0 & 0 & 0 & \cdots\\ \sqrt 1 & 0 & 0 & \cdots\\ 0 & \sqrt 2 & 0 & \cdots\\ 0 & 0 & \sqrt 3 & \cdots\\ \vdots & & & \ddots\end{pmatrix}.
$$

These are Hermitian conjugates of each other: annihilation is the transpose of creation, as the dagger advertises.

(c) Apply $\hat{b}$ then $\hat{b}^\dagger$:

$$
\hat{b}^\dagger\hat{b}\vert n\rangle = \hat{b}^\dagger\sqrt n\,\vert n-1\rangle = \sqrt n\sqrt n\,\vert n\rangle = n\,\vert n\rangle.
$$

Reverse the order:

$$
\hat{b}\hat{b}^\dagger\vert n\rangle = \hat{b}\sqrt{n+1}\,\vert n+1\rangle = \sqrt{n+1}\sqrt{n+1}\,\vert n\rangle = (n+1)\vert n\rangle.
$$

Subtract:

$$
[\hat{b},\hat{b}^\dagger]\vert n\rangle = (\hat{b}\hat{b}^\dagger - \hat{b}^\dagger\hat{b})\vert n\rangle = \bigl((n+1) - n\bigr)\vert n\rangle = \vert n\rangle.
$$

Valid on every Fock basis state; by completeness, $[\hat{b},\hat{b}^\dagger] = 1$ as an operator identity. The lecture introduced the action rules and the algebra as equivalent definitions — this calculation **derives the algebra from the action rules**, confirming that equivalence directly.

(d) Combine (b) with $\hat{x} = x_0(\hat{b}+\hat{b}^\dagger)$:

$$
\langle m\vert\hat{x}\vert n\rangle = x_0\bigl(\sqrt n\,\delta_{m,n-1} + \sqrt{n+1}\,\delta_{m,n+1}\bigr).
$$

Non-zero only when $m = n-1$ (lowered by one) or $m = n+1$ (raised by one): the position operator connects **adjacent** Fock states only. Any electric-dipole coupling $-q\hat{x}E(t)$ between an oscillator and an external field therefore drives transitions $\vert n\rangle\to\vert n\pm 1\rangle$, with rates governed by $\sqrt n$ for absorption and $\sqrt{n+1}$ for emission — the harmonic-oscillator **selection rule** $\Delta n = \pm 1$ and a first glimpse of the stimulated-emission enhancement explored in Problem 4.

<!-- ─── -->

**2. Number-ladder commutators.** Compute the commutators $[\hat{n}_\alpha, \hat{b}^\dagger_\beta]$ and $[\hat{n}_\alpha, \hat{b}_\beta]$ from $[\hat{b}_\alpha, \hat{b}^\dagger_\beta] = \delta_{\alpha\beta}$. Interpret: how does $\hat{b}^\dagger_\beta$ change the eigenvalue of $\hat{n}_\alpha$, and what is the role of $\delta_{\alpha\beta}$?

**Solution.**

Apply the Leibniz rule $[\hat A\hat B, \hat C] = \hat A[\hat B,\hat C] + [\hat A,\hat C]\hat B$ to $\hat n_\alpha = \hat b^\dagger_\alpha\hat b_\alpha$, using $[\hat b_\alpha,\hat b^\dagger_\beta] = \delta_{\alpha\beta}$ and the trivial $[\hat b_\alpha,\hat b_\beta] = [\hat b^\dagger_\alpha,\hat b^\dagger_\beta] = 0$.

*Commutator with $\hat b^\dagger_\beta$.*

$$
\begin{split}
[\hat n_\alpha,\hat b^\dagger_\beta] &= [\hat b^\dagger_\alpha\hat b_\alpha,\hat b^\dagger_\beta] = \hat b^\dagger_\alpha[\hat b_\alpha,\hat b^\dagger_\beta] + [\hat b^\dagger_\alpha,\hat b^\dagger_\beta]\hat b_\alpha\\
&= \hat b^\dagger_\alpha\delta_{\alpha\beta} + 0 = \delta_{\alpha\beta}\hat b^\dagger_\beta.
\end{split}
$$

*Commutator with $\hat b_\beta$.*

$$
\begin{split}
[\hat n_\alpha,\hat b_\beta] &= [\hat b^\dagger_\alpha\hat b_\alpha,\hat b_\beta] = \hat b^\dagger_\alpha[\hat b_\alpha,\hat b_\beta] + [\hat b^\dagger_\alpha,\hat b_\beta]\hat b_\alpha\\
&= 0 + (-\delta_{\alpha\beta})\hat b_\alpha = -\delta_{\alpha\beta}\hat b_\beta.
\end{split}
$$

So $[\hat n_\alpha,\hat b^\dagger_\beta] = \delta_{\alpha\beta}\hat b^\dagger_\beta$ and $[\hat n_\alpha,\hat b_\beta] = -\delta_{\alpha\beta}\hat b_\beta$.

*Interpretation.* When $\beta = \alpha$, the rearrangement $\hat n_\alpha\hat b^\dagger_\alpha = \hat b^\dagger_\alpha(\hat n_\alpha + 1)$ acting on a Fock state with $\hat n_\alpha\vert n_\alpha\rangle = n_\alpha\vert n_\alpha\rangle$ gives

$$
\hat n_\alpha(\hat b^\dagger_\alpha\vert n_\alpha\rangle) = (n_\alpha + 1)\,\hat b^\dagger_\alpha\vert n_\alpha\rangle,
$$

so $\hat b^\dagger_\alpha$ produces a new eigenstate with occupation **raised by one**. Likewise $\hat b_\alpha$ lowers by one. The $\delta_{\alpha\beta}$ factor encodes mode-localisation: when $\beta \neq \alpha$, the commutator vanishes, meaning $\hat b^\dagger_\beta$ and $\hat b_\beta$ act on a different mode and leave the occupation of mode $\alpha$ untouched. **Each ladder operator acts only on its own mode**; modes are independent, and that independence is the algebraic foundation of the occupation-number representation.

<!-- ─── -->

**3. Coherent states.** Define the **coherent state** with complex amplitude $\alpha$ by

$$
\vert\alpha\rangle = \mathrm{e}^{-\vert\alpha\vert^2/2}\sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}}\,\vert n\rangle.
$$

(a) Verify that $\vert\alpha\rangle$ is normalised: $\langle\alpha\vert\alpha\rangle = 1$.

(b) Show that $\vert\alpha\rangle$ is an **eigenstate** of the annihilation operator $\hat b$ with eigenvalue $\alpha$: $\hat b\vert\alpha\rangle = \alpha\vert\alpha\rangle$.

(c) Compute the mean and variance of the particle number, $\langle\hat n\rangle$ and $(\Delta\hat n)^2$. Show that the relative fluctuation $\Delta\hat n / \langle\hat n\rangle = 1/\vert\alpha\vert$ — Poisson statistics — and that fluctuations become negligible in the classical limit $\vert\alpha\vert\to\infty$.

(d) Compute the overlap $\vert\langle\alpha\vert\beta\rangle\vert^2$ between two coherent states. Show that it equals $\mathrm{e}^{-\vert\alpha-\beta\vert^2}$. Are coherent states orthogonal?

**Solution.**

(a) The Fock basis is orthonormal, so

$$
\langle\alpha\vert\alpha\rangle = \mathrm{e}^{-\vert\alpha\vert^2}\sum_n \frac{\vert\alpha\vert^{2n}}{n!} = \mathrm{e}^{-\vert\alpha\vert^2}\,\mathrm{e}^{\vert\alpha\vert^2} = 1. \quad\checkmark
$$

(b) Use $\hat b\vert n\rangle = \sqrt n\vert n-1\rangle$ (with $\hat b\vert 0\rangle = 0$):

$$
\hat b\vert\alpha\rangle = \mathrm{e}^{-\vert\alpha\vert^2/2}\sum_{n=1}^\infty \frac{\alpha^n}{\sqrt{n!}}\sqrt n\,\vert n-1\rangle = \mathrm{e}^{-\vert\alpha\vert^2/2}\sum_{n=1}^\infty \frac{\alpha^n}{\sqrt{(n-1)!}}\vert n-1\rangle.
$$

Re-index with $m = n - 1$:

$$
\hat b\vert\alpha\rangle = \alpha\,\mathrm{e}^{-\vert\alpha\vert^2/2}\sum_{m=0}^\infty \frac{\alpha^m}{\sqrt{m!}}\vert m\rangle = \alpha\,\vert\alpha\rangle. \quad\checkmark
$$

So coherent states are exactly the eigenstates of the **annihilation** operator (not Hermitian, so complex eigenvalues are allowed). This is unique to the bosonic algebra — the corresponding fermionic eigenstate equation has no non-trivial solution beyond the vacuum.

(c) Using $\hat b\vert\alpha\rangle = \alpha\vert\alpha\rangle$ and its dual $\langle\alpha\vert\hat b^\dagger = \alpha^*\langle\alpha\vert$:

$$
\langle\hat n\rangle = \langle\alpha\vert\hat b^\dagger\hat b\vert\alpha\rangle = \alpha^*\alpha = \vert\alpha\vert^2.
$$

For the variance, compute $\langle\hat n^2\rangle = \langle\alpha\vert\hat b^\dagger\hat b\hat b^\dagger\hat b\vert\alpha\rangle$. Reorder the middle pair using $\hat b\hat b^\dagger = \hat b^\dagger\hat b + 1$:

$$
\langle\hat n^2\rangle = \langle\alpha\vert\hat b^\dagger(\hat b^\dagger\hat b + 1)\hat b\vert\alpha\rangle = \langle\alpha\vert\hat b^\dagger\hat b^\dagger\hat b\hat b\vert\alpha\rangle + \langle\alpha\vert\hat b^\dagger\hat b\vert\alpha\rangle = \vert\alpha\vert^4 + \vert\alpha\vert^2.
$$

So $(\Delta\hat n)^2 = \langle\hat n^2\rangle - \langle\hat n\rangle^2 = \vert\alpha\vert^2$, i.e. $\Delta\hat n = \vert\alpha\vert = \sqrt{\langle\hat n\rangle}$. This is the signature of a **Poisson distribution**: variance equals mean. The relative fluctuation is

$$
\frac{\Delta\hat n}{\langle\hat n\rangle} = \frac{\vert\alpha\vert}{\vert\alpha\vert^2} = \frac{1}{\vert\alpha\vert}.
$$

As $\vert\alpha\vert\to\infty$ (intense classical field), relative fluctuations vanish — quantum noise is undetectable, and the coherent state behaves like a classical wave of amplitude $\alpha$.

(d) Compute the inner product:

$$
\langle\alpha\vert\beta\rangle = \mathrm{e}^{-\vert\alpha\vert^2/2}\mathrm{e}^{-\vert\beta\vert^2/2}\sum_n\frac{(\alpha^*)^n\beta^n}{n!} = \mathrm{e}^{-\vert\alpha\vert^2/2 - \vert\beta\vert^2/2 + \alpha^*\beta}.
$$

Squared modulus, using $\vert\mathrm{e}^z\vert^2 = \mathrm{e}^{2\mathrm{Re}(z)}$:

$$
\vert\langle\alpha\vert\beta\rangle\vert^2 = \mathrm{e}^{-\vert\alpha\vert^2 - \vert\beta\vert^2 + 2\mathrm{Re}(\alpha^*\beta)} = \mathrm{e}^{-\vert\alpha-\beta\vert^2}.
$$

Coherent states are **not orthogonal** — they overlap exponentially in the distance $\vert\alpha-\beta\vert$ in the complex plane. Distant coherent states ($\vert\alpha-\beta\vert\gtrsim 1$) are nearly orthogonal; nearby ones overlap strongly. The set $\{\vert\alpha\rangle : \alpha\in\mathbb{C}\}$ is **overcomplete**: it spans the Fock space but its members are not linearly independent. This redundancy is the basis of the phase-space description of bosonic systems (Wigner / Husimi functions).

<!-- ─── -->

**4. Stimulated emission and the boson enhancement factor.** A single bosonic mode contains $n$ existing quanta. Consider a coupling that drives transitions in or out of the mode through the ladder operators.

(a) Compute the transition amplitude $\langle n+1\vert\hat b^\dagger\vert n\rangle$ (emission) and the absorption amplitude $\langle n-1\vert\hat b\vert n\rangle$. Square each to obtain the corresponding transition *rate* per unit coupling.

(b) Decompose the emission rate as $(n+1) = 1 + n$. Identify the "$1$" as the **spontaneous** rate and the "$n$" as the **stimulated** rate proportional to the existing field.

(c) Compute the **net emission rate** (emission minus absorption) and show it equals $1$, independent of $n$. Interpret physically: stimulated emission and absorption have the same matrix element, so their difference picks out only the spontaneous "vacuum" contribution.

(d) Identify the laser regime: when does stimulated dominate spontaneous, and what does this regime predict about the field amplitude inside an active laser cavity?

**Solution.**

(a) From the action $\hat b^\dagger\vert n\rangle = \sqrt{n+1}\vert n+1\rangle$ (lecture):

$$
\langle n+1\vert\hat b^\dagger\vert n\rangle = \sqrt{n+1}, \qquad \vert\langle n+1\vert\hat b^\dagger\vert n\rangle\vert^2 = n+1.
$$

Likewise from $\hat b\vert n\rangle = \sqrt n\vert n-1\rangle$:

$$
\langle n-1\vert\hat b\vert n\rangle = \sqrt n, \qquad \vert\langle n-1\vert\hat b\vert n\rangle\vert^2 = n.
$$

The emission rate scales as $n+1$, the absorption rate as $n$.

(b) Write the emission rate $n+1 = 1 + n$:

- The constant "$1$" is the **spontaneous emission** rate — present even when the mode is empty ($n=0$ gives rate $1$, not $0$). This is the quantum vacuum producing a transition.
- The $n$-proportional part is **stimulated emission** — proportional to the number of quanta already present in the mode. More photons "stimulate" more photons.

The $\sqrt{n+1}$ amplitude is the bosonic enhancement that distinguishes quantum from classical statistics: in a classical field there is no spontaneous emission, only stimulated.

(c) Net emission rate:

$$
R_{\mathrm{net}}(n) = (n+1) - n = 1.
$$

Independent of $n$. **Interpretation:** stimulated emission and absorption share the same matrix element ($\hat b^\dagger$ and $\hat b$ are Hermitian conjugates, with squared moduli $n+1$ and $n$ respectively); their *difference* picks out only the spontaneous contribution. In thermal equilibrium, where emission and absorption balance, this is the algebraic origin of the Planck spectrum — the difference $(n+1) - n = 1$ is what forces the photon Bose-Einstein distribution $n_{\mathrm{th}} = (\mathrm{e}^{\hbar\omega/k_B T} - 1)^{-1}$.

(d) Stimulated dominates spontaneous when $n \gg 1$, i.e. when the cavity already contains many photons. In an active laser cavity, population inversion ensures that the upper level is more populated than the lower, so emission outweighs absorption; combined with positive feedback (mirrors that send emitted photons back into the cavity), this builds $n$ to macroscopic values. The threshold condition for lasing is precisely $n_{\mathrm{stim}} = n \gtrsim 1$ — beyond that, emission self-amplifies exponentially. This is why a laser produces coherent light at extremely high intensity from a single mode (part (c)'s amplitude $\alpha\sim\sqrt n$ at the macroscopic regime is, in a deep sense, a coherent state of the field).

<!-- ─── -->

**5. Slater determinant from creation operators.** For two fermions in orthonormal single-particle modes $\vert\alpha\rangle$ and $\vert\beta\rangle$ ($\alpha\neq\beta$), define the second-quantized two-particle state

$$
\vert\alpha,\beta\rangle_F \equiv \hat c^\dagger_\alpha \hat c^\dagger_\beta \vert 0\rangle.
$$

(a) Show $\vert\beta,\alpha\rangle_F = -\vert\alpha,\beta\rangle_F$, i.e. exchange flips the sign. Identify which anticommutation relation is responsible.

(b) Show $\hat c^\dagger_\alpha \hat c^\dagger_\alpha \vert 0\rangle = 0$ — Pauli exclusion in operator form. Identify the responsible relation.

(c) Use the anticommutator $\{\hat c_\alpha, \hat c^\dagger_\beta\} = \delta_{\alpha\beta}$ together with $\hat c_\alpha\vert 0\rangle = 0$ to compute the inner product $\langle\alpha',\beta'\vert\alpha,\beta\rangle_F$. Show it equals the $2\times 2$ Slater determinant $\det\!\begin{pmatrix}\langle\alpha'\vert\alpha\rangle & \langle\alpha'\vert\beta\rangle \\ \langle\beta'\vert\alpha\rangle & \langle\beta'\vert\beta\rangle\end{pmatrix}$, recovering 2.1.2 Problem 6.

(d) Argue in one sentence why the second-quantized formalism makes the manual antisymmetrisation of 2.1.2 automatic: the algebra encodes Pauli exclusion structurally.

**Solution.**

(a) Exchange the two creation operators using $\{\hat c^\dagger_\alpha,\hat c^\dagger_\beta\} = 0$, which gives $\hat c^\dagger_\alpha\hat c^\dagger_\beta = -\hat c^\dagger_\beta\hat c^\dagger_\alpha$:

$$
\vert\beta,\alpha\rangle_F = \hat c^\dagger_\beta\hat c^\dagger_\alpha\vert 0\rangle = -\hat c^\dagger_\alpha\hat c^\dagger_\beta\vert 0\rangle = -\vert\alpha,\beta\rangle_F. \quad\checkmark
$$

The responsible relation is **$\{\hat c^\dagger_\alpha,\hat c^\dagger_\beta\} = 0$**: anticommutation of creation operators on different modes.

(b) Specialise to $\beta = \alpha$: $\{\hat c^\dagger_\alpha,\hat c^\dagger_\alpha\} = 0$ gives $2(\hat c^\dagger_\alpha)^2 = 0$, hence $(\hat c^\dagger_\alpha)^2 = 0$:

$$
\hat c^\dagger_\alpha\hat c^\dagger_\alpha\vert 0\rangle = 0. \quad\checkmark
$$

The responsible relation is $(\hat c^\dagger_\alpha)^2 = 0$, the operator-level statement of Pauli exclusion.

(c) Compute the inner product by moving the bra's annihilation operators to the right using $\{\hat c_\mu,\hat c^\dagger_\nu\} = \delta_{\mu\nu}$. Take $\langle\alpha',\beta'\vert = \langle 0\vert\hat c_{\beta'}\hat c_{\alpha'}$ (the bra of $\hat c^\dagger_{\alpha'}\hat c^\dagger_{\beta'}\vert 0\rangle$). Then

$$
\langle\alpha',\beta'\vert\alpha,\beta\rangle_F = \langle 0\vert\hat c_{\beta'}\hat c_{\alpha'}\hat c^\dagger_\alpha\hat c^\dagger_\beta\vert 0\rangle.
$$

Anticommute $\hat c_{\alpha'}$ past $\hat c^\dagger_\alpha$ using $\hat c_{\alpha'}\hat c^\dagger_\alpha = \delta_{\alpha'\alpha} - \hat c^\dagger_\alpha\hat c_{\alpha'}$:

$$
= \langle 0\vert\hat c_{\beta'}(\delta_{\alpha'\alpha} - \hat c^\dagger_\alpha\hat c_{\alpha'})\hat c^\dagger_\beta\vert 0\rangle = \delta_{\alpha'\alpha}\langle 0\vert\hat c_{\beta'}\hat c^\dagger_\beta\vert 0\rangle - \langle 0\vert\hat c_{\beta'}\hat c^\dagger_\alpha\hat c_{\alpha'}\hat c^\dagger_\beta\vert 0\rangle.
$$

The first term: $\langle 0\vert\hat c_{\beta'}\hat c^\dagger_\beta\vert 0\rangle = \langle 0\vert(\delta_{\beta'\beta} - \hat c^\dagger_\beta\hat c_{\beta'})\vert 0\rangle = \delta_{\beta'\beta}$ (the second piece kills the vacuum). The second term: anticommute $\hat c_{\alpha'}\hat c^\dagger_\beta = \delta_{\alpha'\beta} - \hat c^\dagger_\beta\hat c_{\alpha'}$, then the residual term kills the vacuum, leaving

$$
-\delta_{\alpha'\beta}\langle 0\vert\hat c_{\beta'}\hat c^\dagger_\alpha\vert 0\rangle = -\delta_{\alpha'\beta}\delta_{\beta'\alpha}.
$$

Combining:

$$
\langle\alpha',\beta'\vert\alpha,\beta\rangle_F = \delta_{\alpha'\alpha}\delta_{\beta'\beta} - \delta_{\alpha'\beta}\delta_{\beta'\alpha} = \det\begin{pmatrix}\langle\alpha'\vert\alpha\rangle & \langle\alpha'\vert\beta\rangle\\ \langle\beta'\vert\alpha\rangle & \langle\beta'\vert\beta\rangle\end{pmatrix},
$$

the Slater determinant of single-particle overlaps — matching 2.1.2 Problem 6 exactly. (Using $\langle\alpha'\vert\alpha\rangle = \delta_{\alpha'\alpha}$ for orthonormal modes makes this trivial; for non-orthonormal modes the same algebra works with $\langle\mu\vert\nu\rangle$ replacing $\delta_{\mu\nu}$ throughout.)

(d) In second quantization, antisymmetrisation is **built into the operator algebra** via the anticommutation relations $\{\hat c^\dagger_\alpha,\hat c^\dagger_\beta\} = 0$ — exchanging two creation operators automatically flips the sign — so $\hat c^\dagger_\alpha\hat c^\dagger_\beta\vert 0\rangle$ is *already* the Slater-determinant state $\vert\alpha,\beta\rangle_-/\sqrt 2$ (up to a phase), with no explicit sum over permutations. This is the central efficiency gain over first quantization: the $N!$ symmetrisation sums collapse into a single product of $N$ creation operators.

<!-- ─── -->

**6. Particle-hole conjugation.** In a fermionic Fock space, define the **hole operator** $\hat d_\alpha \equiv \hat c^\dagger_\alpha$ (and its conjugate $\hat d^\dagger_\alpha = \hat c_\alpha$).

(a) Compute the four anticommutators $\{\hat d_\alpha,\hat d^\dagger_\beta\}$, $\{\hat d_\alpha,\hat d_\beta\}$, $\{\hat d^\dagger_\alpha,\hat d^\dagger_\beta\}$ from the fermionic algebra of $\hat c$. Show that the hole operators satisfy the **same** fermionic anticommutation algebra.

(b) For a finite set of modes $\alpha = 1,\ldots,D$, define the **filled state** $\vert F\rangle = \hat c^\dagger_1\hat c^\dagger_2\cdots\hat c^\dagger_D\vert 0\rangle$. Show that $\vert F\rangle$ is the **hole vacuum**: $\hat d_\alpha\vert F\rangle = 0$ for every $\alpha$.

(c) The hole number operator is $\hat n^h_\alpha = \hat d^\dagger_\alpha\hat d_\alpha$. Show that $\hat n^h_\alpha = 1 - \hat n_\alpha$ (a hole exists in mode $\alpha$ exactly when the mode is empty of fermions).

(d) Interpret physically: in solid-state physics, removing an electron from a filled valence band creates a "hole" that behaves as a positive-charge fermion. Argue that this physical picture is exactly the algebraic statement that **the hole operators obey the same fermionic algebra as the particle operators**, just relative to a different vacuum ($\vert F\rangle$ instead of $\vert 0\rangle$).

**Solution.**

(a) Compute each anticommutator. Using $\hat d_\alpha = \hat c^\dagger_\alpha$ and $\hat d^\dagger_\alpha = \hat c_\alpha$:

$$
\{\hat d_\alpha,\hat d^\dagger_\beta\} = \{\hat c^\dagger_\alpha,\hat c_\beta\} = \{\hat c_\beta,\hat c^\dagger_\alpha\} = \delta_{\alpha\beta},
$$

$$
\{\hat d_\alpha,\hat d_\beta\} = \{\hat c^\dagger_\alpha,\hat c^\dagger_\beta\} = 0,
$$

$$
\{\hat d^\dagger_\alpha,\hat d^\dagger_\beta\} = \{\hat c_\alpha,\hat c_\beta\} = 0.
$$

Identical to the $\hat c$ algebra: hole creation and annihilation **obey the same fermionic anticommutation relations** as particle creation and annihilation.

(b) Compute $\hat d_\alpha\vert F\rangle = \hat c^\dagger_\alpha\vert F\rangle$. The filled state $\vert F\rangle$ already has every mode occupied, so creating another fermion in mode $\alpha$ would put two in mode $\alpha$:

$$
\hat c^\dagger_\alpha\vert F\rangle = \hat c^\dagger_\alpha\,\hat c^\dagger_1\cdots\hat c^\dagger_\alpha\cdots\hat c^\dagger_D\vert 0\rangle.
$$

Anticommute $\hat c^\dagger_\alpha$ to its position (introducing signs but preserving the structure), arriving at a product containing $(\hat c^\dagger_\alpha)^2$, which vanishes (Problem 5b / lecture):

$$
\hat d_\alpha\vert F\rangle = 0 \quad\text{for every } \alpha.
$$

So $\vert F\rangle$ is annihilated by every $\hat d_\alpha$ — exactly the defining property of a vacuum, but now for the hole algebra.

(c) Compute $\hat n^h_\alpha = \hat d^\dagger_\alpha\hat d_\alpha = \hat c_\alpha\hat c^\dagger_\alpha$. Use $\hat c_\alpha\hat c^\dagger_\alpha = \{\hat c_\alpha,\hat c^\dagger_\alpha\} - \hat c^\dagger_\alpha\hat c_\alpha = 1 - \hat n_\alpha$:

$$
\hat n^h_\alpha = 1 - \hat n_\alpha.
$$

So if $\hat n_\alpha = 1$ (electron present) then $\hat n^h_\alpha = 0$; if $\hat n_\alpha = 0$ (electron absent) then $\hat n^h_\alpha = 1$. The hole number operator counts unoccupied modes exactly.

(d) **The particle-hole transformation is an algebraic equivalence:** the hole operators $\hat d_\alpha = \hat c^\dagger_\alpha$ obey the same fermionic anticommutation relations as the original $\hat c_\alpha$, just relative to the filled state $\vert F\rangle$ instead of the empty vacuum $\vert 0\rangle$. Any physics expressed in terms of the $\hat c$ algebra has an exact mirror expressed in the $\hat d$ algebra — including conserved quantities, currents, and dynamics. In solid-state physics this is the formal statement that "missing an electron in a filled band" can be treated identically to "having an electron in an empty band," just with charge sign flipped and effective mass inverted (since the dispersion near a band edge changes sign). This **particle-hole duality** is one of the most important structural symmetries of fermionic systems: it explains why semiconductors carry "two species" of carriers (electrons and holes) even though only one species of particle (the electron) exists, and it underlies the analogous duality in superconducting mean-field theory (developed in later chapters).

<!-- ─── -->

**7. Two-mode boson tunnelling.** Consider two bosonic modes labelled L (left) and R (right), with Hamiltonian

$$
\hat H = -t\bigl(\hat b_L^\dagger\hat b_R + \hat b_R^\dagger\hat b_L\bigr), \qquad t > 0.
$$

This is the simplest tunnelling model — particles "hop" between two sites with amplitude $t$.

(a) **Single particle ($N = 1$).** The Hilbert space at fixed $N=1$ is spanned by $\vert 1,0\rangle = \hat b_L^\dagger\vert 0\rangle$ and $\vert 0,1\rangle = \hat b_R^\dagger\vert 0\rangle$. Compute the action of $\hat H$ on each basis state, and write $\hat H$ as a $2\times 2$ matrix in this basis.

(b) Diagonalise $\hat H$. Show that the eigenstates are the **bonding** state $\vert +\rangle = (\vert 1,0\rangle + \vert 0,1\rangle)/\sqrt 2$ with energy $-t$ and the **antibonding** state $\vert -\rangle = (\vert 1,0\rangle - \vert 0,1\rangle)/\sqrt 2$ with energy $+t$.

(c) Starting from $\vert\psi(0)\rangle = \vert 1,0\rangle$, compute the probability $P_R(t)$ of finding the particle in the right well at time $t$. Identify the tunnelling angular frequency.

(d) **Two particles ($N = 2$).** The Hilbert space at $N=2$ has dimension $3$ (states $\vert 2,0\rangle$, $\vert 1,1\rangle$, $\vert 0,2\rangle$). Compute the action of $\hat H$ on each — paying attention to the boson enhancement factors $\sqrt{n+1}$ — and write $\hat H$ as a $3\times 3$ matrix.

**Solution.**

(a) Apply the ladder rules $\hat b\vert n\rangle = \sqrt n\vert n-1\rangle$, $\hat b^\dagger\vert n\rangle = \sqrt{n+1}\vert n+1\rangle$ on the two-mode state $\vert n_L,n_R\rangle$:

$$
\hat H\vert 1,0\rangle = -t\bigl(\hat b_L^\dagger\hat b_R\vert 1,0\rangle + \hat b_R^\dagger\hat b_L\vert 1,0\rangle\bigr) = -t\bigl(0 + \vert 0,1\rangle\bigr) = -t\vert 0,1\rangle.
$$

$$
\hat H\vert 0,1\rangle = -t\bigl(\hat b_L^\dagger\hat b_R\vert 0,1\rangle + \hat b_R^\dagger\hat b_L\vert 0,1\rangle\bigr) = -t\bigl(\vert 1,0\rangle + 0\bigr) = -t\vert 1,0\rangle.
$$

Matrix in basis $\{\vert 1,0\rangle, \vert 0,1\rangle\}$:

$$
\hat H = \begin{pmatrix} 0 & -t \\ -t & 0\end{pmatrix} = -t\hat X.
$$

(b) The matrix $-t\hat X$ has eigenvalues $\mp t$ with eigenstates $\vert\pm\rangle = (\vert 1,0\rangle \pm \vert 0,1\rangle)/\sqrt 2$ (1.1.3 P5/P7 territory). Explicitly:

- Bonding state $\vert+\rangle = \tfrac{1}{\sqrt 2}(\vert 1,0\rangle + \vert 0,1\rangle)$, energy $E_+ = -t$ (the lower energy).
- Antibonding state $\vert-\rangle = \tfrac{1}{\sqrt 2}(\vert 1,0\rangle - \vert 0,1\rangle)$, energy $E_- = +t$ (the higher energy).

These are the chemical-bonding analogues for a single particle in a double-well — the bonding state has lower energy because the wavefunction is symmetric (constructive interference between the two wells), while the antibonding has destructive interference at the centre.

(c) Decompose the initial state: $\vert 1,0\rangle = \tfrac{1}{\sqrt 2}(\vert+\rangle + \vert-\rangle)$. Evolve each component by its own phase:

$$
\vert\psi(t)\rangle = \tfrac{1}{\sqrt 2}\bigl(\mathrm{e}^{+\mathrm{i}t t/\hbar}\vert+\rangle + \mathrm{e}^{-\mathrm{i}t t/\hbar}\vert-\rangle\bigr).
$$

(Note the signs: $E_+ = -t$ gives evolution $\mathrm{e}^{+\mathrm{i}tt/\hbar}$.) The amplitude of $\vert 0,1\rangle$ component is

$$
\langle 0,1\vert\psi(t)\rangle = \tfrac{1}{2}\bigl(\mathrm{e}^{+\mathrm{i}tt/\hbar} - \mathrm{e}^{-\mathrm{i}tt/\hbar}\bigr) = \mathrm{i}\sin(tt/\hbar),
$$

so

$$
P_R(t) = \vert\langle 0,1\vert\psi(t)\rangle\vert^2 = \sin^2(tt/\hbar).
$$

The probability oscillates between $0$ and $1$ at angular frequency $\omega_{\mathrm{tunn}} = 2t/\hbar$, with the particle fully transferring to the right well at $t_\star = \pi\hbar/(2t)$. This is the **Rabi-like oscillation** of a single particle between two wells — formally identical to the Pauli two-level dynamics of 1.3.2.

(d) For $N=2$, use $\hat b^\dagger_L\hat b_R\vert n_L,n_R\rangle = \sqrt{(n_L+1)n_R}\vert n_L+1,n_R-1\rangle$ and the conjugate. On the three basis states:

$$
\hat H\vert 2,0\rangle = -t\bigl(0 + \sqrt 2\sqrt 1\vert 1,1\rangle\bigr) = -t\sqrt 2\vert 1,1\rangle,
$$

$$
\hat H\vert 1,1\rangle = -t\bigl(\sqrt 2\sqrt 1\vert 2,0\rangle + \sqrt 2\sqrt 1\vert 0,2\rangle\bigr) = -t\sqrt 2(\vert 2,0\rangle + \vert 0,2\rangle),
$$

$$
\hat H\vert 0,2\rangle = -t\bigl(\sqrt 2\sqrt 1\vert 1,1\rangle + 0\bigr) = -t\sqrt 2\vert 1,1\rangle.
$$

Matrix in basis $\{\vert 2,0\rangle, \vert 1,1\rangle, \vert 0,2\rangle\}$:

$$
\hat H = -t\sqrt 2\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix}.
$$

The factor $\sqrt 2$ comes from the bosonic enhancement $\sqrt{n+1}$ when hopping into an already-occupied mode — the same $\sqrt 2$ as in 1.3.3 Problem 4. The matrix is $-t\sqrt 2\,(\hat X_{(2,0)\to(1,1)} + \hat X_{(1,1)\to(0,2)})$, a tridiagonal structure familiar from tight-binding chains. Its three eigenvalues are $-2t,\,0,\,+2t$ (you can verify by checking $\det(\hat H - \lambda\hat I) = -\lambda(\lambda^2 - 8t^2)$); the bosonic enhancement has doubled the level spacing relative to the single-particle case (b), an explicit example of the "rich get richer" stimulated-emission effect of Problem 4.

<!-- ─── -->

**8. Fock space dimensions.** From 2.1.2 Problems 7 and 8, the number of $N$-particle states in $D$ modes is $\binom{D}{N}$ for fermions and $\binom{N+D-1}{N}$ for bosons. Recover these counts from the operator formalism, then assemble the full Fock space.

(a) The most general fermion Fock state in $D$ modes is $\prod_\alpha (\hat c^\dagger_\alpha)^{n_\alpha}\vert 0\rangle$ with each $n_\alpha\in\{0,1\}$ (by $(\hat c^\dagger_\alpha)^2 = 0$). Count the choices of $\{n_\alpha\}$ with $\sum_\alpha n_\alpha = N$ to recover $\binom{D}{N}$.

(b) The general boson Fock state is $\prod_\alpha\frac{(\hat b^\dagger_\alpha)^{n_\alpha}}{\sqrt{n_\alpha!}}\vert 0\rangle$ with each $n_\alpha\in\{0,1,2,\ldots\}$. Count the choices with $\sum_\alpha n_\alpha = N$ to recover $\binom{N+D-1}{N}$.

(c) Sum over $N$ to find the total dimension of the Fock space $\mathcal F_D = \bigoplus_{N=0}^\infty \mathcal H_N$. Show that for fermions $\dim\mathcal F_D = 2^D$ (finite!), while for bosons $\dim\mathcal F_D = \infty$.

(d) Interpret physically: the same algebraic distinction (anticommutator vs commutator) that gives the Pauli exclusion principle also constrains the **size** of the fermionic Hilbert space. Why is a finite-dimensional Fock space the natural setting for "lattice fermion" problems (electrons on a crystal), and why does the infinite boson Fock space correspond to the more delicate analytical issues of bosonic theories (BEC, photon counting)?

**Solution.**

(a) Each of the $D$ modes contributes either $\hat c^\dagger_\alpha$ (occupation $n_\alpha = 1$) or nothing (occupation $n_\alpha = 0$). With total $\sum_\alpha n_\alpha = N$, we are choosing **which $N$ of the $D$ modes are occupied** — a size-$N$ subset of the $D$-element mode set. The count is the binomial coefficient

$$
\#\{\text{fermion N-states}\} = \binom{D}{N}.
$$

Matches 2.1.2 Problem 7 exactly. The constraint $n_\alpha\le 1$ is the algebraic Pauli exclusion $(\hat c^\dagger_\alpha)^2 = 0$.

(b) Each $n_\alpha$ can be $0, 1, 2, \ldots$, with $\sum_\alpha n_\alpha = N$. This is the "distribute $N$ indistinguishable balls into $D$ distinguishable boxes" problem, solved by stars-and-bars:

$$
\#\{\text{boson N-states}\} = \binom{N + D - 1}{N},
$$

matching 2.1.2 Problem 8.

(c) **Fermion Fock space total dimension.** Sum the binomial coefficients:

$$
\dim\mathcal F^{(F)}_D = \sum_{N=0}^D \binom{D}{N} = 2^D,
$$

a finite total. (The sum truncates at $N = D$ — beyond that there are no states, since each mode is at most singly occupied. This is the algebraic finiteness from Pauli exclusion.)

**Boson Fock space total dimension.** Sum to infinity:

$$
\dim\mathcal F^{(B)}_D = \sum_{N=0}^\infty \binom{N + D - 1}{N} = \infty,
$$

since each term in the sum is positive and the series diverges (in fact it grows polynomially with $N$, so the sum is infinite). The bosonic Fock space is **infinite-dimensional** for any $D\ge 1$.

(d) The finite versus infinite Fock-space dimension is the **same** algebraic distinction as Pauli exclusion versus bosonic stimulated enhancement: at the per-mode level, fermions are capped at $n_\alpha\le 1$ while bosons can pile up to $n_\alpha = \infty$. Multiplying across $D$ modes gives total dimension $2^D$ for fermions and $\infty$ for bosons.

**Lattice fermions.** A system of electrons on a crystal lattice with $D$ orbitals fits naturally in a $2^D$-dimensional Hilbert space — exactly the dimension of $D$ classical bits. This is why fermionic lattice problems (Hubbard, tight-binding) map cleanly onto quantum-computational problems and admit finite-matrix diagonalisation up to moderate $D$.

**Bosonic theories.** The infinite-dimensional boson Fock space is the natural home for photon counting, BEC, and quantum optics. Many bosonic computations require truncating the per-mode Hilbert space at some finite occupation, with the truncation justified by physical arguments (low photon number, ground-state-dominated dynamics, etc.). The analytic subtleties of bosonic theories — divergences, normal ordering, regularisation — all trace back to this infinite-dimensional structure.

The **commutator-vs-anticommutator** distinction at the algebraic level is therefore responsible for the *Hilbert-space-dimension* difference, the *statistics* difference (Bose-Einstein vs Fermi-Dirac), and the *computational complexity* difference between bosonic and fermionic many-body physics.

<!-- ─── -->

**9. Equal partition theorem.** Consider the harmonic oscillator $\hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \tfrac{1}{2})$ with position $\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger)$ and momentum $\hat{p} = \mathrm{i}\sqrt{\frac{m\hbar\omega}{2}}(\hat{a}^\dagger - \hat{a})$.

(a) Show that in the energy eigenstate $\vert n\rangle$, $\langle n\vert\hat{x}^2\vert n\rangle = \frac{\hbar}{2m\omega}(2n+1)$ and $\langle n\vert\hat{p}^2\vert n\rangle = \frac{m\hbar\omega}{2}(2n+1)$.

(b) Verify that $\frac{1}{2m}\langle\hat{p}^2\rangle = \frac{1}{2}m\omega^2\langle\hat{x}^2\rangle = \frac{1}{2}E_n$ in each eigenstate $\vert n\rangle$. This is the quantum equal partition of energy between kinetic and potential.

(c) For a superposition $\vert\psi(0)\rangle = c_0\vert 0\rangle + c_1\vert 1\rangle$, compute $\langle\hat{x}^2\rangle(t)$ and $\langle\hat{p}^2/(m^2\omega^2)\rangle(t)$. Show that the time-averaged values over one period still satisfy equal partition.

**Solution.**

(a) Square the expressions for $\hat{x}$ and $\hat p$ in terms of ladder operators:

$$
\hat{x}^2 = \frac{\hbar}{2m\omega}(\hat a + \hat a^\dagger)^2 = \frac{\hbar}{2m\omega}(\hat a^2 + (\hat a^\dagger)^2 + \hat a\hat a^\dagger + \hat a^\dagger\hat a) = \frac{\hbar}{2m\omega}(\hat a^2 + (\hat a^\dagger)^2 + 2\hat n + 1),
$$

using $\hat a\hat a^\dagger = \hat n + 1$. On $\vert n\rangle$, the $\hat a^2$ and $(\hat a^\dagger)^2$ pieces have vanishing expectation value (they shift the state by $\pm 2$ quanta, orthogonal to $\vert n\rangle$):

$$
\langle n\vert\hat{x}^2\vert n\rangle = \frac{\hbar}{2m\omega}(2n + 1).
$$

Likewise

$$
\hat p^2 = -\frac{m\hbar\omega}{2}(\hat a^\dagger - \hat a)^2 = -\frac{m\hbar\omega}{2}(\hat a^2 + (\hat a^\dagger)^2 - 2\hat n - 1) = \frac{m\hbar\omega}{2}(2\hat n + 1 - \hat a^2 - (\hat a^\dagger)^2),
$$

so $\langle n\vert\hat p^2\vert n\rangle = \frac{m\hbar\omega}{2}(2n + 1)$.

(b) Substitute:

$$
\frac{1}{2m}\langle\hat p^2\rangle = \frac{1}{2m}\cdot\frac{m\hbar\omega}{2}(2n+1) = \frac{\hbar\omega}{4}(2n+1) = \frac{1}{2}\cdot\hbar\omega(n + \tfrac{1}{2}) = \tfrac{1}{2}E_n,
$$

$$
\frac{1}{2}m\omega^2\langle\hat{x}^2\rangle = \frac{1}{2}m\omega^2\cdot\frac{\hbar}{2m\omega}(2n+1) = \frac{\hbar\omega}{4}(2n+1) = \tfrac{1}{2}E_n.
$$

Both kinetic and potential energies are exactly half the total — quantum **equipartition** between the two quadratic forms. (This is the operator analogue of the classical statement that, time-averaged, a harmonic oscillator stores half its energy as kinetic and half as potential. Here it holds *instantaneously* in any energy eigenstate.)

(c) On a superposition $\vert\psi(0)\rangle = c_0\vert 0\rangle + c_1\vert 1\rangle$, time evolution gives $\vert\psi(t)\rangle = c_0\mathrm{e}^{-\mathrm{i}\hbar\omega t/2\hbar}\vert 0\rangle + c_1\mathrm{e}^{-3\mathrm{i}\hbar\omega t/2\hbar}\vert 1\rangle = \mathrm{e}^{-\mathrm{i}\omega t/2}\bigl(c_0\vert 0\rangle + c_1\mathrm{e}^{-\mathrm{i}\omega t}\vert 1\rangle\bigr)$. The relative phase $\mathrm{e}^{-\mathrm{i}\omega t}$ between $\vert 0\rangle$ and $\vert 1\rangle$ produces $t$-dependence in cross-matrix-elements but not in diagonal ones.

Compute $\langle\hat{x}^2\rangle(t)$. The $\hat{x}^2$ matrix has diagonal entries $\langle 0\vert\hat{x}^2\vert 0\rangle = \hbar/(2m\omega)$ and $\langle 1\vert\hat{x}^2\vert 1\rangle = 3\hbar/(2m\omega)$, and off-diagonal $\langle 0\vert\hat{x}^2\vert 1\rangle = 0$ (since $\hat{x}^2$ shifts particle number by even amounts). So

$$
\langle\hat{x}^2\rangle(t) = \vert c_0\vert^2\cdot\frac{\hbar}{2m\omega} + \vert c_1\vert^2\cdot\frac{3\hbar}{2m\omega} = \frac{\hbar}{2m\omega}(1 + 2\vert c_1\vert^2),
$$

**independent of $t$**. By the same argument $\langle\hat p^2\rangle(t)$ is also $t$-independent, and equipartition $\frac{1}{2m}\langle\hat p^2\rangle = \frac{1}{2}m\omega^2\langle\hat{x}^2\rangle$ holds at every $t$ (not just time-averaged). The relative-phase rotation between $\vert 0\rangle$ and $\vert 1\rangle$ shows up in *linear* observables like $\langle\hat{x}\rangle(t) \propto \cos\omega t$, but its quadratic counterparts $\langle\hat{x}^2\rangle$ and $\langle\hat p^2\rangle$ are insensitive.

If one mixes $\vert 0\rangle$ and $\vert 2\rangle$ instead (states differing by two quanta), then $\langle\hat{x}^2\rangle(t)$ does depend on $t$ through $\hat a^2, (\hat a^\dagger)^2$ matrix elements — and the time-averaged equipartition relation still holds, since $\langle\cos 2\omega t\rangle_t = 0$. Equipartition is exact instantaneously for $\vert 0\rangle$/$\vert 1\rangle$ superpositions and exact only after time-averaging for superpositions involving states with $\Delta n = 2$.

<!-- ─── -->

**10. Schwinger boson.** Define two independent bosonic modes with operators $(\hat{a}, \hat{a}^\dagger)$ and $(\hat{b}, \hat{b}^\dagger)$, and construct

$$
\hat{S}_+ = \hat{a}^\dagger\hat{b}, \quad \hat{S}_- = \hat{b}^\dagger\hat{a}, \quad \hat{S}_z = \tfrac{1}{2}(\hat{a}^\dagger\hat{a} - \hat{b}^\dagger\hat{b}).
$$

(a) Verify that these satisfy the angular momentum commutation relations $[\hat{S}_z, \hat{S}_\pm] = \pm\hat{S}_\pm$ and $[\hat{S}_+, \hat{S}_-] = 2\hat{S}_z$.

(b) Show that $\hat{\boldsymbol{S}}^2 = \hat{S}_z^2 + \frac{1}{2}(\hat{S}_+\hat{S}_- + \hat{S}_-\hat{S}_+) = \frac{\hat{N}}{2}\bigl(\frac{\hat{N}}{2} + 1\bigr)$, where $\hat{N} = \hat{a}^\dagger\hat{a} + \hat{b}^\dagger\hat{b}$ is the total boson number.

(c) In the subspace with $\hat{N} = 2$ (three Fock states $\vert 2,0\rangle$, $\vert 1,1\rangle$, $\vert 0,2\rangle$), write $\hat{S}_z$ and $\hat{S}_+$ as $3\times 3$ matrices. Verify these are the spin-1 representation.

(d) Identify the general correspondence: each Fock state $\vert n_a, n_b\rangle$ with $n_a + n_b = 2s$ maps to $\vert s, m\rangle$ with $m = (n_a - n_b)/2$. What value of $s$ does the $N$-boson subspace carry?

**Solution.**

(a) Use $[\hat a, \hat a^\dagger] = [\hat b, \hat b^\dagger] = 1$, and the fact that operators on different modes commute.

*$[\hat S_z, \hat S_+]$:* $\hat S_z = \tfrac{1}{2}(\hat a^\dagger\hat a - \hat b^\dagger\hat b)$, $\hat S_+ = \hat a^\dagger\hat b$. Using the Leibniz rule and the per-mode commutators,

$$
[\hat S_z, \hat S_+] = \tfrac{1}{2}([\hat a^\dagger\hat a, \hat a^\dagger]\hat b + \hat a^\dagger[-\hat b^\dagger\hat b,\hat b]) = \tfrac{1}{2}(\hat a^\dagger\hat b + \hat a^\dagger\hat b) = \hat a^\dagger\hat b = \hat S_+. \quad\checkmark
$$

(Used $[\hat a^\dagger\hat a, \hat a^\dagger] = \hat a^\dagger$ and $[\hat b^\dagger\hat b, \hat b] = -\hat b$.) Conjugating gives $[\hat S_z, \hat S_-] = -\hat S_-$.

*$[\hat S_+, \hat S_-]$:*

$$
\hat S_+\hat S_- = \hat a^\dagger\hat b\hat b^\dagger\hat a = \hat a^\dagger\hat a(\hat b^\dagger\hat b + 1) = \hat n_a(\hat n_b + 1),
$$

$$
\hat S_-\hat S_+ = \hat b^\dagger\hat a\hat a^\dagger\hat b = \hat b^\dagger\hat b(\hat a^\dagger\hat a + 1) = \hat n_b(\hat n_a + 1).
$$

Subtracting: $[\hat S_+, \hat S_-] = \hat n_a - \hat n_b = 2\hat S_z$. $\checkmark$

(b) Compute $\hat{\boldsymbol S}^2 = \hat S_z^2 + \tfrac{1}{2}(\hat S_+\hat S_- + \hat S_-\hat S_+)$. From (a),

$$
\hat S_+\hat S_- + \hat S_-\hat S_+ = \hat n_a(\hat n_b + 1) + \hat n_b(\hat n_a + 1) = 2\hat n_a\hat n_b + \hat n_a + \hat n_b = 2\hat n_a\hat n_b + \hat N.
$$

And $\hat S_z^2 = \tfrac{1}{4}(\hat n_a - \hat n_b)^2$. Combining:

$$
\begin{split}
\hat{\boldsymbol S}^2 &= \tfrac{1}{4}(\hat n_a - \hat n_b)^2 + \hat n_a\hat n_b + \tfrac{1}{2}\hat N \\
&= \tfrac{1}{4}(\hat n_a^2 - 2\hat n_a\hat n_b + \hat n_b^2 + 4\hat n_a\hat n_b) + \tfrac{1}{2}\hat N \\
&= \tfrac{1}{4}(\hat n_a + \hat n_b)^2 + \tfrac{1}{2}\hat N \\
&= \tfrac{1}{4}\hat N^2 + \tfrac{1}{2}\hat N.
\end{split}
$$

Factor: $\tfrac{1}{4}\hat N^2 + \tfrac{1}{2}\hat N = \tfrac{\hat N}{2}\bigl(\tfrac{\hat N}{2} + 1\bigr)$, which is the standard form $s(s+1)$ with $s = \hat N/2$. ✓

(c) On the $N=2$ subspace, basis $\{\vert 2,0\rangle,\vert 1,1\rangle,\vert 0,2\rangle\}$.

*$\hat S_z = \tfrac{1}{2}(\hat n_a - \hat n_b)$:*
$\hat S_z\vert 2,0\rangle = +\vert 2,0\rangle$, $\hat S_z\vert 1,1\rangle = 0$, $\hat S_z\vert 0,2\rangle = -\vert 0,2\rangle$. Matrix: $\mathrm{diag}(1, 0, -1)$.

*$\hat S_+ = \hat a^\dagger\hat b$:* Acts as $\sqrt{(n_a+1)n_b}\vert n_a+1, n_b - 1\rangle$. So $\hat S_+\vert 2,0\rangle = 0$, $\hat S_+\vert 1,1\rangle = \sqrt 2\vert 2,0\rangle$, $\hat S_+\vert 0,2\rangle = \sqrt 2\vert 1,1\rangle$. Matrix:

$$
\hat S_+ = \begin{pmatrix} 0 & \sqrt 2 & 0 \\ 0 & 0 & \sqrt 2 \\ 0 & 0 & 0\end{pmatrix}.
$$

These match the **spin-1 angular momentum matrices** in the standard $\{\vert 1,+1\rangle, \vert 1,0\rangle, \vert 1,-1\rangle\}$ basis (where $\hat S_+\vert s,m\rangle = \sqrt{s(s+1) - m(m+1)}\vert s,m+1\rangle = \sqrt{1\cdot 2 - m(m+1)}\vert s,m+1\rangle$ gives the same $\sqrt 2$ factors). The identification:

$$
\vert 2,0\rangle \leftrightarrow \vert 1,+1\rangle, \quad \vert 1,1\rangle \leftrightarrow \vert 1,0\rangle, \quad \vert 0,2\rangle \leftrightarrow \vert 1,-1\rangle.
$$

(d) From part (b), $\hat{\boldsymbol S}^2 = \tfrac{\hat N}{2}\bigl(\tfrac{\hat N}{2} + 1\bigr)$ on every Fock state. Setting $\hat N = N$ gives $\hat{\boldsymbol S}^2 = s(s+1)$ with $s = N/2$. So the $N$-boson subspace carries spin $s = N/2$. The state $\vert n_a, n_b\rangle$ with $n_a + n_b = N$ has $\hat S_z$ eigenvalue $m = (n_a - n_b)/2$, so

$$
\vert n_a, n_b\rangle \leftrightarrow \vert s = N/2,\ m = (n_a - n_b)/2\rangle.
$$

This is the **Schwinger boson representation** of angular momentum: **two independent harmonic oscillators reproduce every irreducible spin representation** ($s = 0, 1/2, 1, 3/2, \ldots$) by restricting to the $N$-boson subspace. The construction was Schwinger's tool for deriving rotation operators and Clebsch–Gordan coefficients, and it remains central to nuclear physics, strongly correlated electrons, and the spin-coherent-state formalism. Cross-link forward: in §2.2 this construction provides the cleanest derivation of the angular-momentum spectrum and the matrix representations of $\hat S_x, \hat S_y, \hat S_z$ for any spin $s$.
