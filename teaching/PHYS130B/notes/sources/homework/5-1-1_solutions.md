# 5.1.1 Toy Model
Worked solutions for the homework problems in the [5.1.1 Toy Model](../ch5_perturbation-theory/5-1-1-toy-model) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Accuracy window.** Use the approximation $E_+^{\text{(2nd)}}(\lambda)=1+\lambda^2/2$ as a model prediction for the upper level. Find the largest real $\lambda>0$ such that the relative error

$$
\frac{\left|E_+^{\text{exact}}-E_+^{\text{(2nd)}}\right|}{\left|E_+^{\text{exact}}\right|}
$$

is below $5\%$. Interpret the result as a practical criterion for when second-order perturbation theory is trustworthy.

**Solution.**

The exact upper level is $E_+^{\text{exact}} = \sqrt{1+\lambda^2}$ and the
second-order truncation is $E_+^{\text{(2nd)}} = 1 + \lambda^2/2$. Since

$$
\sqrt{1+\lambda^2} = 1 + \frac{\lambda^2}{2} - \frac{\lambda^4}{8} + O(\lambda^6),
$$

the truncation **overshoots** the exact value for every real $\lambda \ne 0$
(the first omitted term, $-\lambda^4/8$, is negative). The relative error is
therefore

$$
r(\lambda) = \frac{\left(1+\lambda^2/2\right) - \sqrt{1+\lambda^2}}{\sqrt{1+\lambda^2}} = \frac{1+\lambda^2/2}{\sqrt{1+\lambda^2}} - 1.
$$

Set $r(\lambda) = 0.05$ and write $u = \lambda^2$:

$$
\frac{1+u/2}{\sqrt{1+u}} = 1.05.
$$

Square both sides and use the identity $(1+u/2)^2 = (1+u) + u^2/4$:

$$
\frac{(1+u/2)^2}{1+u} = 1 + \frac{u^2/4}{1+u} = 1.1025
\quad\Longrightarrow\quad
\frac{u^2}{4(1+u)} = 0.1025.
$$

This is the quadratic $u^2 - 0.41\,u - 0.41 = 0$, with positive root

$$
u = \frac{0.41 + \sqrt{0.41^2 + 4(0.41)}}{2} = \frac{0.41 + \sqrt{1.8081}}{2} = 0.8773,
$$

so

$$
\lambda_{\max} = \sqrt{u} = 0.937.
$$

(Direct check: at $\lambda = 0.937$, $\sqrt{1+\lambda^2} = 1.3702$ and
$1+\lambda^2/2 = 1.4387$, giving $r = 0.0500$.)

**Interpretation.** Second-order perturbation theory holds the upper level to
within $5\%$ all the way up to $\lambda \approx 0.94$ — coupling of order
unity, even though $\lambda$ was nominally assumed "small." The window is this
generous because the **leading error is $O(\lambda^4)$**: the $\lambda^1$ and
$\lambda^3$ terms vanish in this model, so the first uncorrected term is
$\lambda^4/8$ and the error stays tiny over a long range of $\lambda$ before
turning on sharply. The practical criterion is not "is $\lambda$ small?" in the
abstract, but "is the relative error below tolerance?" — and the only reliable
way to know is to compare the truncation against the exact (or a higher-order)
value and watch the error grow as $\lambda$ increases.

<!-- ─── -->

**2. Inverse design.** Suppose spectroscopy reports an upper-level energy $E_+=1.18$ for the toy model. Estimate $\lambda$ using second-order perturbation theory, then compute the exact $\lambda$ from $E_+=\sqrt{1+\lambda^2}$. Compare the two inferred couplings and discuss why the inverse problem can amplify approximation error.

**Solution.**

**Second-order estimate.** Invert $E_+^{\text{(2nd)}} = 1 + \lambda^2/2 = 1.18$:

$$
\frac{\lambda^2}{2} = 0.18 \quad\Longrightarrow\quad \lambda_{\text{2nd}} = \sqrt{0.36} = 0.600.
$$

**Exact value.** Invert $E_+ = \sqrt{1+\lambda^2} = 1.18$:

$$
\lambda^2 = 1.18^2 - 1 = 0.3924 \quad\Longrightarrow\quad \lambda_{\text{exact}} = \sqrt{0.3924} = 0.626.
$$

The two inferred couplings differ by $\lambda_{\text{exact}} -
\lambda_{\text{2nd}} = 0.026$, a relative discrepancy of about $4.2\%$.

**Why the inverse problem amplifies error.** Two effects compound.

First, the **informative signal lives in $E_+ - 1$, not in $E_+$.** The
unperturbed energy is $1$; all the coupling information sits in the deviation
$E_+ - 1 = 0.18$. The forward model error of the second-order truncation at
$\lambda \approx 0.6$ is $\lambda^4/8 \approx 0.016$. That is only $\sim 1.4\%$
of $E_+$, but it is $\sim 9\%$ of the signal $E_+ - 1 = 0.18$. Measuring the
energy relative to an offset turns a small absolute error into a large
fractional error of the quantity that actually carries the answer.

Second, the **forward map is locally quadratic**, so the inverse map is locally
a square root. Near the origin $E_+ - 1 \approx \lambda^2/2$, hence $\lambda
\approx \sqrt{2(E_+-1)}$ and $\delta\lambda/\lambda = \tfrac12\,\delta(E_+-1)/(E_+-1)$.
Equivalently, the forward slope $\mathrm{d}E_+/\mathrm{d}\lambda =
\lambda/\sqrt{1+\lambda^2}$ is **less than one** (it vanishes as $\lambda\to0$),
so a given energy error is *divided* by a small slope when mapped back to
$\lambda$. The $9\%$ signal error is roughly halved by the square root to the
observed $\sim 4\%$ in $\lambda$, but it is still several times larger than the
$1.4\%$ error one would naively quote from $E_+$. The lesson: a model accurate
in the forward direction can still be a poor instrument for inversion,
especially when the response is weak (small slope) and the signal sits on a
large baseline.

<!-- ─── -->

**3. Basis rotation: energies vs states.** Consider

$$
\hat{H}(\lambda,\phi)=\hat{Z}+\lambda\big(\cos\phi\,\hat{X}+\sin\phi\,\hat{Y}\big).
$$

(a) Find a unitary $\hat U(\phi)$ that rotates about $\hat Z$ and satisfies $\hat U(\phi)^\dagger\,\hat H(\lambda,\phi)\,\hat U(\phi)=\hat H(\lambda,0)$.

(b) Use this unitary equivalence to argue that the eigenvalues $E_\pm(\lambda,\phi)$ are *independent of $\phi$* — the spectrum depends on $\lambda$ alone.

(c) Show that the eigenstates *do* depend on $\phi$: $\vert\psi_\pm(\lambda,\phi)\rangle=\hat U(\phi)\,\vert\psi_\pm(\lambda,0)\rangle$.

(d) **Implication for a perturbative series in $\phi$.** Expand $E_+(\lambda,\phi)$ as a Taylor series in $\phi$ about $\phi=0$. What must every coefficient be? Now expand $\vert\psi_+(\lambda,\phi)\rangle$ in $\phi$ — is the first-order $\phi$-correction zero? If not, compute it explicitly.

(e) State the general principle illustrated here: when a parameter enters $\hat H$ only through a unitary similarity transformation, energies are invariant but eigenstates rotate.

**Solution.**

**(a)** Take the $\hat Z$-rotation

$$
\hat U(\phi) = \mathrm{e}^{-\mathrm{i}\phi\hat Z/2}.
$$

Its conjugation action on the Pauli operators follows from $[\hat Z,\hat X] =
2\mathrm{i}\hat Y$ and $[\hat Z,\hat Y] = -2\mathrm{i}\hat X$. Writing $f(\phi)
= \mathrm{e}^{\mathrm{i}\phi\hat Z/2}\hat X\,\mathrm{e}^{-\mathrm{i}\phi\hat Z/2}$,
differentiation gives $f'(\phi) = \tfrac{\mathrm{i}}{2}\,
\mathrm{e}^{\mathrm{i}\phi\hat Z/2}[\hat Z,\hat X]\,\mathrm{e}^{-\mathrm{i}\phi\hat Z/2}
= -\,\mathrm{e}^{\mathrm{i}\phi\hat Z/2}\hat Y\,\mathrm{e}^{-\mathrm{i}\phi\hat Z/2}$,
and likewise for $\hat Y$; solving the coupled pair with $f(0)=\hat X$,
$g(0)=\hat Y$ yields

$$
\hat U^\dagger \hat X\,\hat U = \hat X\cos\phi - \hat Y\sin\phi,
\qquad
\hat U^\dagger \hat Y\,\hat U = \hat X\sin\phi + \hat Y\cos\phi,
\qquad
\hat U^\dagger \hat Z\,\hat U = \hat Z.
$$

Therefore

$$
\begin{split}
\hat U^\dagger \hat H(\lambda,\phi)\,\hat U
&= \hat Z + \lambda\Big[\cos\phi\,(\hat X\cos\phi - \hat Y\sin\phi) + \sin\phi\,(\hat X\sin\phi + \hat Y\cos\phi)\Big]\\
&= \hat Z + \lambda\big[\hat X(\cos^2\phi+\sin^2\phi) + \hat Y(-\cos\phi\sin\phi+\sin\phi\cos\phi)\big]\\
&= \hat Z + \lambda\hat X = \hat H(\lambda,0).
\end{split}
$$

So $\hat U(\phi) = \mathrm{e}^{-\mathrm{i}\phi\hat Z/2}$ does the job:
geometrically it rotates the in-plane field direction $(\cos\phi,\sin\phi)$
back onto the $x$-axis.

**(b)** Rearranging part (a), $\hat H(\lambda,\phi) = \hat U(\phi)\,\hat
H(\lambda,0)\,\hat U(\phi)^\dagger$. This is a **unitary similarity
transformation**, and similar matrices have identical characteristic
polynomials, hence identical eigenvalues. Therefore

$$
E_\pm(\lambda,\phi) = E_\pm(\lambda,0) = \pm\sqrt{1+\lambda^2},
$$

independent of $\phi$ — the spectrum depends on the coupling strength
$\lambda$ alone, not on the in-plane direction $\phi$.

**(c)** Let $\hat H(\lambda,0)\,\vert\psi_\pm(\lambda,0)\rangle = E_\pm\,
\vert\psi_\pm(\lambda,0)\rangle$. Apply $\hat U(\phi)$ and insert $\hat
U^\dagger\hat U = \hat 1$:

$$
\hat H(\lambda,\phi)\,\hat U(\phi)\vert\psi_\pm(\lambda,0)\rangle
= \hat U\hat H(\lambda,0)\hat U^\dagger\,\hat U\vert\psi_\pm(\lambda,0)\rangle
= E_\pm\,\hat U(\phi)\vert\psi_\pm(\lambda,0)\rangle.
$$

So $\hat U(\phi)\vert\psi_\pm(\lambda,0)\rangle$ is an eigenstate of $\hat
H(\lambda,\phi)$ with the same eigenvalue, i.e.

$$
\vert\psi_\pm(\lambda,\phi)\rangle = \hat U(\phi)\,\vert\psi_\pm(\lambda,0)\rangle
$$

(up to an irrelevant overall phase). The eigenstates **do** depend on $\phi$:
they are carried around the $z$-axis by $\hat U(\phi)$.

**(d)** Since $E_+(\lambda,\phi) = \sqrt{1+\lambda^2}$ is exactly constant in
$\phi$, its Taylor series about $\phi=0$ is just that constant: **every
coefficient of $\phi^k$ with $k\ge 1$ vanishes.** A perturbative expansion of
the *energy* in $\phi$ is trivial at all orders.

The *state* is a different story. Expand the rotation:

$$
\vert\psi_+(\lambda,\phi)\rangle = \mathrm{e}^{-\mathrm{i}\phi\hat Z/2}\vert\psi_+(\lambda,0)\rangle
= \Big[\hat 1 - \frac{\mathrm{i}\phi}{2}\hat Z + O(\phi^2)\Big]\vert\psi_+(\lambda,0)\rangle.
$$

The first-order $\phi$-correction is

$$
\vert\psi_+^{(1)}\rangle = -\frac{\mathrm{i}}{2}\,\hat Z\,\vert\psi_+(\lambda,0)\rangle,
$$

which is **not zero** (it vanishes only if $\vert\psi_+(\lambda,0)\rangle$ is a
$\hat Z$-eigenstate, i.e. only at $\lambda=0$). Explicitly, write the
unperturbed-direction eigenstate as $\vert\psi_+(\lambda,0)\rangle =
\cos\tfrac\theta2\,\vert 0\rangle + \sin\tfrac\theta2\,\vert 1\rangle$ with
$\tan\theta = \lambda$ (the field $(\lambda,0,1)$ tilts by $\theta$ from the
$z$-axis). Then

$$
\vert\psi_+^{(1)}\rangle = -\frac{\mathrm{i}}{2}\Big(\cos\tfrac\theta2\,\vert 0\rangle - \sin\tfrac\theta2\,\vert 1\rangle\Big).
$$

So a perturbative series in $\phi$ has all-zero energy coefficients but a
genuine, computable first-order state correction.

**(e)** **Principle.** When a parameter enters the Hamiltonian only through a
unitary similarity transformation, $\hat H(\xi) = \hat W(\xi)\,\hat H_0\,\hat
W(\xi)^\dagger$, the spectrum is invariant under $\xi$ (eigenvalues are
similarity invariants) while the eigenstates are simply transported by $\hat
W$: $\vert\psi_n(\xi)\rangle = \hat W(\xi)\vert\psi_n(0)\rangle$. Such a
parameter is **geometric, not spectral** — it rotates the states without
deforming the energies. Perturbation theory in that parameter is "trivial" for
energies and entirely about the state rotation.

<!-- ─── -->

**4. Controlled asymmetry.** Add a diagonal perturbation and study

$$
\hat{H}(\lambda,\mu)=\hat{Z}+\lambda\hat{X}+\mu\hat{Z}.
$$

Treat $\lambda$ and $\mu$ as small independent parameters and expand $E_+(\lambda,\mu)$ to second order in both. Which terms are linear in $\mu$? Which terms are linear in $\lambda$? Use symmetry arguments to justify the pattern.

**Solution.**

Collecting the diagonal terms, $\hat H(\lambda,\mu) = (1+\mu)\hat Z +
\lambda\hat X$, i.e. in the $\{\vert 0\rangle,\vert 1\rangle\}$ basis

$$
\hat H(\lambda,\mu) = \begin{pmatrix} 1+\mu & \lambda \\ \lambda & -(1+\mu) \end{pmatrix},
\qquad
E_+(\lambda,\mu) = \sqrt{(1+\mu)^2 + \lambda^2}.
$$

Write the radicand as $1 + s$ with $s = 2\mu + \mu^2 + \lambda^2$ and use
$\sqrt{1+s} = 1 + s/2 - s^2/8 + \cdots$. Keeping all terms of total degree
$\le 2$ in $(\lambda,\mu)$:

$$
\frac{s}{2} = \mu + \frac{\mu^2}{2} + \frac{\lambda^2}{2},
\qquad
\frac{s^2}{8} = \frac{(2\mu)^2}{8} + (\text{degree}\ge 3) = \frac{\mu^2}{2} + \cdots.
$$

The two $\mu^2/2$ pieces cancel, leaving

$$
E_+(\lambda,\mu) = 1 + \mu + \frac{\lambda^2}{2} + O\big(\text{degree }3\big).
$$

**Which terms are linear in $\mu$?** The single term $+\mu$. **Which terms are
linear in $\lambda$?** None — there is no $\lambda^1$ term at all; the leading
$\lambda$-dependence is the quadratic $\lambda^2/2$. (The first
$\lambda$-$\mu$ cross term is $-\lambda^2\mu/2$, which appears only at third
order.)

**Symmetry justification.** The two perturbations play structurally different
roles:

- $\mu\hat Z$ is **diagonal** in the unperturbed basis — it commutes with
  $\hat H_0 = \hat Z$. Its first-order correction to the upper level is
  $\langle 0\vert\,\mu\hat Z\,\vert 0\rangle = \mu \ne 0$, so $\mu$ enters
  **linearly**: a diagonal perturbation shifts the bare energy directly.

- $\lambda\hat X$ is **purely off-diagonal**: $\langle 0\vert\hat X\vert 0\rangle = 0$,
  so its first-order correction vanishes and the leading effect is second
  order, $\lambda^2/2$.

The absence of *every* odd power of $\lambda$ (not just the linear one)
follows from an exact symmetry. Conjugating by $\hat Z$ flips the sign of
$\hat X$ while leaving $\hat Z$ alone ($\hat Z\hat X\hat Z = -\hat X$):

$$
\hat Z\,\hat H(\lambda,\mu)\,\hat Z = (1+\mu)\hat Z - \lambda\hat X = \hat H(-\lambda,\mu).
$$

This unitary equivalence forces $E_\pm(\lambda,\mu) = E_\pm(-\lambda,\mu)$ —
$E_+$ is an **even function of $\lambda$**, so all odd powers of $\lambda$ are
forbidden. No analogous symmetry sends $\mu\to-\mu$, so nothing forbids the
linear-in-$\mu$ term, and indeed it is present. This is the general pattern: a
perturbation that commutes with $\hat H_0$ contributes at first order, while a
perturbation that anticommutes with (or is purely off-diagonal in) $\hat H_0$
is parity-protected and contributes only at even orders.

<!-- ─── -->

**5. Avoided crossing width.** For

$$
\hat{H}=\begin{pmatrix}
\delta & v \\
v & -\delta
\end{pmatrix},
$$

show that the minimum gap over all $\delta$ is $2|v|$. Then solve the inverse question: if an experiment measures a minimum gap of $0.12\,\mathrm{eV}$, what is $|v|$? Explain why this is a direct operational meaning of level repulsion.

**Solution.**

The matrix $\hat H = \delta\,\hat Z + v\,\hat X$ has eigenvalues

$$
E_\pm = \pm\sqrt{\delta^2 + v^2},
$$

so the level gap is

$$
\Delta(\delta) = E_+ - E_- = 2\sqrt{\delta^2 + v^2}.
$$

As a function of the diagonal detuning $\delta$, $\Delta(\delta)$ is minimized
where the radicand is smallest. Since $\delta^2 \ge 0$ with equality only at
$\delta = 0$,

$$
\Delta_{\min} = \Delta(0) = 2\sqrt{v^2} = 2|v|.
$$

The bare diagonal energies $\pm\delta$ cross at $\delta = 0$, but the true
eigenvalues never meet: their closest approach is exactly $2|v|$.

**Inverse question.** A measured minimum gap of $0.12\,\mathrm{eV}$ gives

$$
2|v| = 0.12\,\mathrm{eV} \quad\Longrightarrow\quad |v| = 0.06\,\mathrm{eV}.
$$

**Operational meaning.** $v$ is the off-diagonal coupling between the two bare
states. Without it ($v=0$) the levels would simply cross at $\delta=0$; with it
they "repel" and stay split. Crucially, the *size* of that splitting at the
crossing point is not some complicated function of the coupling — it is
**precisely $2|v|$**. So sweeping $\delta$ through the avoided crossing and
reading off the closest approach is a direct measurement of the coupling
strength: $|v| = \Delta_{\min}/2$. This is the concrete, operational content of
"level repulsion" — the minimum gap *is* (twice) the coupling, and a nonzero
$v$ guarantees the two levels can never be exactly degenerate.

<!-- ─── -->

**6. Misconception test.** One might claim: "If the unperturbed gap is nonzero, non-degenerate perturbation theory should remain valid even when $\lambda$ is large." Test this claim quantitatively by comparing exact and second-order energies at $\lambda=0.2,0.8,1.5$. Identify where the claim fails and explain the failure using error growth as $\lambda$ increases.

**Solution.**

For the toy model the unperturbed gap is fixed at $E_+^{(0)} - E_-^{(0)} = 2$
for all $\lambda$. Compare the exact upper level $E_+ = \sqrt{1+\lambda^2}$
with the second-order truncation $E_+^{\text{(2nd)}} = 1+\lambda^2/2$:

| $\lambda$ | $E_+^{\text{exact}}$ | $E_+^{\text{(2nd)}}$ | absolute error | relative error |
|-----------|----------------------|----------------------|----------------|----------------|
| $0.2$ | $1.019804$ | $1.020000$ | $0.000196$ | $0.019\%$ |
| $0.8$ | $1.280625$ | $1.320000$ | $0.039375$ | $3.08\%$ |
| $1.5$ | $1.802776$ | $2.125000$ | $0.322224$ | $17.9\%$ |

At $\lambda = 0.2$ the truncation is essentially exact ($0.02\%$). By $\lambda
= 0.8$ it is marginal ($\sim 3\%$). At $\lambda = 1.5$ it is wrong by nearly
$18\%$ — and adding more terms does not rescue it.

**Where the claim fails and why.** The claim fails for any $\lambda$ of order
one or larger, despite the unperturbed gap being nonzero and *constant* (equal
to $2$) throughout. A nonzero gap is therefore **necessary but not
sufficient**. The reason is that the perturbative series is the Taylor
expansion of $\sqrt{1+\lambda^2}$, and that function has branch points at
$\lambda = \pm\mathrm{i}$. The radius of convergence is fixed by the nearest
singularity:

$$
R = |\pm\mathrm{i}| = 1.
$$

For $|\lambda| < 1$ the series converges and successive truncations approach
the exact answer; for $|\lambda| > 1$ the series **diverges** — the terms
eventually grow, and no order of truncation is reliable. That is exactly why
$\lambda = 1.5$ (outside the disk of convergence) is hopeless while $\lambda =
0.2$ (well inside) is excellent. Even inside the disk the truncation error
grows steeply, the leading relative error scaling as $\sim\lambda^4/8$.

The misconception conflates two distinct requirements. A nonzero gap ensures
non-degenerate perturbation theory is **well-defined** — no energy denominator
$E_n^{(0)} - E_m^{(0)}$ vanishes, so the order-by-order coefficients exist. But
for the truncated series to be **accurate**, $\lambda$ must additionally be
small compared to the scale set by the gap (here $|\lambda| < R = 1$). "Defined"
and "accurate" are not the same statement; the claim assumes the first implies
the second.

<!-- ─── -->

**7. Near-degeneracy diagnosis.** Consider

$$
\hat{H}(\lambda,\epsilon)=\begin{pmatrix}
\epsilon & \lambda \\
\lambda & -\epsilon
\end{pmatrix}, \qquad \epsilon>0.
$$

(a) Compute the exact eigenvalues and expand for small $\lambda$ at fixed $\epsilon$.

(b) Determine the condition on $\lambda, \epsilon$ under which the second-order term is a controlled correction.

(c) Use your condition to explain why the limits $\epsilon\to 0$ and $\lambda\to 0$ do not commute in practice for perturbation theory.

**Solution.**

**(a)** The matrix $\hat H = \epsilon\hat Z + \lambda\hat X$ has exact
eigenvalues

$$
E_\pm(\lambda,\epsilon) = \pm\sqrt{\epsilon^2 + \lambda^2}.
$$

The unperturbed Hamiltonian ($\lambda=0$) is $\epsilon\hat Z$ with levels
$\pm\epsilon$ and gap $2\epsilon$. Expanding the upper level for small
$\lambda$ at **fixed** $\epsilon$:

$$
E_+ = \epsilon\sqrt{1 + \frac{\lambda^2}{\epsilon^2}}
= \epsilon\left(1 + \frac{\lambda^2}{2\epsilon^2} - \frac{\lambda^4}{8\epsilon^4} + \cdots\right)
= \epsilon + \frac{\lambda^2}{2\epsilon} - \frac{\lambda^4}{8\epsilon^3} + \cdots.
$$

The second-order term is $E_+^{(2)} = \lambda^2/(2\epsilon)$. This agrees with the
non-degenerate perturbation-theory formula, $E_+^{(2)} = \vert\langle -\vert
\hat V\vert +\rangle\vert^2 / (E_+^{(0)} - E_-^{(0)})$ with off-diagonal matrix
element $\lambda$ and energy denominator equal to the unperturbed gap $2\epsilon$.

**(b)** The second-order term is a controlled (small) correction when it is
much smaller than the zeroth-order structure it corrects — here the half-gap
$\epsilon$:

$$
\frac{\lambda^2}{2\epsilon} \ll \epsilon
\quad\Longleftrightarrow\quad
\lambda^2 \ll 2\epsilon^2
\quad\Longleftrightarrow\quad
|\lambda| \ll \epsilon.
$$

Equivalently, the dimensionless expansion parameter is $\lambda/\epsilon$
(it appears as $\sqrt{1 + (\lambda/\epsilon)^2}$); the series in $\lambda$
converges for $|\lambda|/\epsilon < 1$, i.e. $|\lambda| < \epsilon$, and the
correction is a *small* controlled one when $|\lambda| \ll \epsilon$ — the
perturbation matrix element must be much smaller than the **half-gap**
$\epsilon$. (Consistently, $E_+$ has branch points at $\lambda =
\pm\mathrm{i}\,\epsilon$, so the radius of convergence is exactly $R =
\epsilon$.)

**(c)** The validity condition involves only the **ratio** $\lambda/\epsilon$,
not either parameter alone — and that is precisely why the two limits do not
commute:

- **$\lambda\to 0$ first, at fixed $\epsilon>0$:** the ratio $\lambda/\epsilon
  \to 0$, perturbation theory is valid, $E_+ \to \epsilon$, and the
  eigenstates approach the unperturbed $\vert 0\rangle, \vert 1\rangle$.
  Then taking $\epsilon\to 0$ smoothly closes the gap with the system always
  in the perturbative regime.

- **$\epsilon\to 0$ first, at fixed $\lambda$:** the ratio $\lambda/\epsilon
  \to \infty$, the energy denominator in $E_+^{(2)} = \lambda^2/\epsilon$ blows
  up, and perturbation theory **breaks down**. At $\epsilon = 0$ exactly,
  $E_\pm = \pm|\lambda|$ and the eigenstates are the *fully rotated* states
  $\vert\pm\rangle$ — nothing like $\vert 0\rangle, \vert 1\rangle$. Taking
  $\lambda\to 0$ afterward cannot undo a rotation that already happened.

Hence

$$
\lim_{\epsilon\to 0}\ \lim_{\lambda\to 0}\ \vert\psi_+(\lambda,\epsilon)\rangle
\;\ne\;
\lim_{\lambda\to 0}\ \lim_{\epsilon\to 0}\ \vert\psi_+(\lambda,\epsilon)\rangle :
$$

the double limit $(\lambda,\epsilon)\to(0,0)$ depends on the **path**, i.e. on
the value of $\lambda/\epsilon$ along the way. This is the near-degenerate
regime. When $\lambda \gtrsim \epsilon$, the two levels are too close for
$\lambda$ to count as a small correction, non-degenerate perturbation theory
fails, and one must diagonalize the $2\times 2$ block exactly (degenerate
perturbation theory). The non-commuting limits are the sharp mathematical
signature of the lesson in Problem 6: "the gap is nonzero" is not enough — what
governs perturbation theory is the size of the perturbation *relative to* the
gap.
