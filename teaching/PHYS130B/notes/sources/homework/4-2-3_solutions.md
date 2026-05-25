# 4.2.3 Flux Ring
Worked solutions for the homework problems in the [4.2.3 Flux Ring](../ch4_phase-and-gauge/4-2-3-flux-ring) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Persistent current at finite temperature.** At temperature $T$, the flux ring is described by the Boltzmann ensemble over angular-momentum levels $\{\vert n\rangle\}$ with energies $E_n(\Phi)$ from {eq}`eq-ring-spectrum`. Working in the canonical ensemble for a single particle, the thermal persistent current is

$$
I(T,\Phi)=-\partial_\Phi F=-\frac{1}{Z}\sum_{n\in\mathbb{Z}}\mathrm{e}^{-\beta E_n(\Phi)}\,\partial_\Phi E_n(\Phi),
$$

with $Z=\sum_n\mathrm{e}^{-\beta E_n(\Phi)}$, $\beta=1/(k_BT)$, and natural energy unit $E_0=\hbar^2/(2mR^2)$. Define the dimensionless temperature $t=k_BT/E_0$ and the dimensionless flux $\varphi=\Phi/\Phi_0$.

(a) Write $I(T,\Phi)$ as an explicit sum over $n$ in dimensionless variables $(t,\varphi)$, with $I_0=E_0/\Phi_0$ as the unit of current.

(b) In the low-$T$ limit ($t\ll 1$), keep only the lowest-energy term on each branch and recover the zero-temperature sawtooth $I/I_0=2(n_*-\varphi)$ derived in lecture, where $n_*$ is the integer closest to $\varphi$.

(c) In the high-$T$ limit ($t\gg 1$), the Gaussian width $\sqrt{t}$ exceeds the integer spacing, so the sum $Z(t,\varphi)$ is well approximated by its integral. Compute this leading integral approximation and show that the persistent current vanishes at this order. Conclude that the flux-dependent current at high $T$ is the small *discrete correction* to the integral approximation, exponentially suppressed in $t$. Identify the activation temperature scale at which thermal smearing destroys the sawtooth.

(d) Sketch (or compute numerically) $I(T,\Phi)/I_0$ on one period $\varphi\in[0,1]$ for $t=0.1,\,1,\,10$, and describe how the sawtooth rounds off into a sinusoid as $T$ grows. What is the practical temperature scale below which the sharp discontinuities at half-integer flux remain visible?

**Solution.**

**(a)** With $E_n(\Phi)=E_0(n-\varphi)^2$, the flux derivative is
$\partial_\Phi E_n = -(2E_0/\Phi_0)(n-\varphi)$. Substituting into the
canonical average,

$$
I(T,\Phi) = \frac{2E_0}{\Phi_0\,Z}\sum_{n\in\mathbb{Z}}(n-\varphi)\,\mathrm{e}^{-(n-\varphi)^2/t},
\qquad
Z(t,\varphi) = \sum_{n\in\mathbb{Z}}\mathrm{e}^{-(n-\varphi)^2/t}.
$$

In units of $I_0 = E_0/\Phi_0$,

$$
\boxed{\,\frac{I(T,\Phi)}{I_0} = \frac{2}{Z(t,\varphi)}\sum_{n\in\mathbb{Z}}(n-\varphi)\,\mathrm{e}^{-(n-\varphi)^2/t}.\,}
$$

This exact sum reduces to the two analytically tractable limits below.

**(b)** *Low temperature, $t\ll 1$.* The Boltzmann factor
$\mathrm{e}^{-(n-\varphi)^2/t}$ is sharply peaked on the integer $n_*$ closest
to $\varphi$. For generic $\varphi\in(n_*-1/2,n_*+1/2)$ with
$|n_*-\varphi|<1/2$, the next-closest term has $|n-\varphi|\ge 1-|n_*-\varphi|$
and its relative weight is exponentially small,
$\mathrm{e}^{-[(1-|n_*-\varphi|)^2 - (n_*-\varphi)^2]/t}$. Keeping only the
dominant term in both numerator and denominator,

$$
\frac{I}{I_0} \approx \frac{2(n_*-\varphi)\,\mathrm{e}^{-(n_*-\varphi)^2/t}}{\mathrm{e}^{-(n_*-\varphi)^2/t}}
= 2(n_*-\varphi),
$$

the zero-temperature sawtooth derived in lecture. The approximation breaks
down only in a window of width $\sim t^{1/2}$ around each half-integer flux,
where two levels become comparable — and this is exactly where thermal
rounding sets in.

**(c)** *High temperature, $t\gg 1$.* The Gaussian $\mathrm{e}^{-(n-\varphi)^2/t}$ has width $\sqrt{t} \gg 1$ on the integer lattice — many integers fit under one peak — so the discrete sum is well approximated by its integral. Use the change of variables $u = n - \varphi$:

$$
Z(t,\varphi) = \sum_{n\in\mathbb{Z}}\mathrm{e}^{-(n-\varphi)^2/t}
\;\approx\;\int_{-\infty}^{\infty}\mathrm{e}^{-u^{2}/t}\,\mathrm{d}u
= \sqrt{\pi t}.
$$

The integral is **independent of $\varphi$** — the shift absorbs the flux entirely. Recasting the current using $\sum_n(n-\varphi)\mathrm{e}^{-(n-\varphi)^2/t} = (t/2)\,\partial_\varphi Z$ (from $\partial_\varphi\mathrm{e}^{-(n-\varphi)^2/t} = (2/t)(n-\varphi)\mathrm{e}^{-(n-\varphi)^2/t}$),

$$
\frac{I}{I_0} = \frac{2}{Z}\cdot\frac{t}{2}\,\partial_\varphi Z = t\,\partial_\varphi\ln Z.
$$

To the integral-approximation order $Z \approx \sqrt{\pi t}$ is $\varphi$-independent, so $\partial_\varphi\ln Z = 0$ and the persistent current **vanishes**. The actual flux-dependent current at high $T$ is therefore the small *discrete correction* by which the sum departs from the integral — equivalently, the residual flux-periodicity in $Z(t,\varphi)$ that the integral approximation washes out.

This correction is **exponentially small in $t$**: as $\sqrt{t}$ grows, the Gaussian becomes increasingly "flat" on the lattice scale, and the difference between the sum and the integral shrinks exponentially in the ratio $\sqrt{t}/1$ of widths. (Explicit evaluation of the leading correction shows it decays as $\mathrm{e}^{-\pi^{2}t}$, but the central point is the exponential suppression itself.) The high-$T$ persistent current is therefore washed out exponentially.

The activation scale is set by $t \sim 1$, i.e. $k_BT \sim E_0 = \hbar^{2}/(2mR^{2})$: below this temperature the sum is dominated by one or two integers and the sawtooth survives; above it the sum collapses to its integral and the flux response dies.

**(d)** Evaluating the exact sum of part (a) numerically:

- $t = 0.1$ (cold): a sharp sawtooth indistinguishable from the
  zero-temperature curve, with a vertical jump at $\varphi=1/2$ from
  $+1$ to $-1$ in units of $I_0$.
- $t = 1$ (warm): the discontinuity rounds into a steep but finite-slope crossover through zero; the linear ramps on either side still dominate the envelope. The discrete correction to the integral approximation is already exponentially small at this temperature, so the visible structure is essentially the thermally rounded sawtooth.
- $t = 10$ (hot): the sawtooth is destroyed; $Z$ has collapsed to its integral approximation $\sqrt{\pi t}$ to very high accuracy, and the residual flux-dependent current is effectively zero — what little remains is the exponentially small smooth modulation around $\varphi$.

The practical visibility threshold is $t\lesssim 1$, i.e.
$k_BT \lesssim E_0 = \hbar^2/(2mR^2)$. For a ring of $R=1\,\mu\mathrm{m}$ this
places the experimental window in the sub-millikelvin regime (cf. the
estimate of $T^*$ in Problem 8b).

<!-- ─── -->

**2. Many fermions on the ring.** $N$ non-interacting spinless fermions occupy the ring and fill the $N$ lowest single-particle levels $E_n(\Phi)$ from {eq}`eq-ring-spectrum`. The many-body ground-state energy is $E_{\mathrm{tot}}(N,\Phi)=\sum_{n\in F}E_n(\Phi)$ over the filled set $F$, and the total persistent current is $I_{\mathrm{tot}}(N,\Phi)=-\partial_\Phi E_{\mathrm{tot}}$.

(a) For $N=2$ and $\varphi=\Phi/\Phi_0\in(0,1)$, identify the filled set, derive

$$
E_{\mathrm{tot}}(2,\Phi)=\frac{\hbar^2}{2mR^2}\bigl[1-2\varphi+2\varphi^2\bigr],
$$

and find $I_{\mathrm{tot}}(2,\Phi)$. State how its shape and sign behaviour differ from the $N=1$ result, and what happens at $\varphi=1/2$.

(b) For odd $N=2M+1$ and $\varphi\in(-1/2,1/2)$, show that the filled set is the symmetric window $\{-M,\ldots,M\}$ and derive

$$
I_{\mathrm{tot}}(2M+1,\Phi)=-(2M+1)\frac{\hbar^2}{mR^2\Phi_0}\,\varphi.
$$

Confirm the period in $\Phi$ is $\Phi_0$, and that the slope is $N$ times the single-particle slope.

(c) Large-$N$ limit. Define the Fermi momentum $k_F=N/(2R)$, the Fermi velocity $v_F=\hbar k_F/m$, and the ring circumference $L=2\pi R$. Show that the maximum total persistent current approaches

$$
I_{\mathrm{tot}}^{\max}\to\frac{q\,v_F}{L}
$$

up to a sign set by charge convention. Interpret this as "one carrier per traversal time $L/v_F$" and explain how the $N$-level sum collapses to a universal Fermi-scale amplitude.

**Solution.**

**(a)** For $\varphi\in(0,1)$ the four lowest candidate levels are
$E_0=E_0\varphi^2$, $E_1=E_0(1-\varphi)^2$, $E_{-1}=E_0(1+\varphi)^2$, and
$E_2=E_0(2-\varphi)^2$. On the whole branch
$E_0\le E_1 < \min(E_{-1},E_2)$, so the filled set is $\{0,1\}$ throughout
(it changes only at $\varphi=1$, where $E_2=E_0(1)^2=E_1(0)$). Hence

$$
E_{\mathrm{tot}}(2,\Phi) = E_0[\varphi^2 + (1-\varphi)^2]
= \frac{\hbar^2}{2mR^2}\bigl[1 - 2\varphi + 2\varphi^2\bigr],
$$

and

$$
I_{\mathrm{tot}}(2,\Phi) = -\partial_\Phi E_{\mathrm{tot}}
= \frac{2E_0}{\Phi_0}\,(1-2\varphi).
$$

*Comparison with $N=1$.* The single-particle current on branch $n=0$ is
$I_1 = -(2E_0/\Phi_0)\varphi$, valid only on $\varphi\in(-1/2,1/2)$, with
discontinuities at every *half*-integer flux. The $N=2$ current
$I_{\mathrm{tot}}=(2E_0/\Phi_0)(1-2\varphi)$ is linear on the entire interval
$\varphi\in(0,1)$, takes its maximum value $+2E_0/\Phi_0$ at $\varphi=0^+$ and
its negative extremum $-2E_0/\Phi_0$ at $\varphi=1^-$, and passes
**smoothly through zero at $\varphi=1/2$** — no discontinuity there. The
filled-set jump for $N=2$ happens at *integer* flux instead, where the set
$\{0,1\}\to\{1,2\}$.

This is the well-known **parity effect**: odd $N$ has persistent-current
discontinuities at half-integer flux, while even $N$ has them at integer
flux. The two parities are out of phase by half a flux quantum.

**(b)** For odd $N=2M+1$ and $\varphi\in(-1/2,1/2)$, the levels closest to
$\varphi=0$ are symmetric about zero. Comparing $E_n=E_0(n-\varphi)^2$ for
small $|\varphi|$: the $N$ smallest values are $|n|\le M$. (For
$\varphi\to 1/2^-$, $E_M=E_0(M-1/2)^2$ approaches $E_{M+1}=E_0(M+1/2)^2$ only
if $\varphi$ exits the branch; this happens exactly at $\varphi=1/2$, the
edge of the interval.) So the filled set is $F=\{-M,\ldots,M\}$ throughout
the branch.

Compute the total energy:

$$
\begin{split}
E_{\mathrm{tot}}(N,\Phi)
&= E_0\!\sum_{n=-M}^{M}(n-\varphi)^2
= E_0\!\sum_{n=-M}^{M}\bigl[n^2 - 2n\varphi + \varphi^2\bigr]\\
&= E_0\!\left[\sum_{n=-M}^{M}n^2 \;-\; 2\varphi\!\sum_{n=-M}^{M}n \;+\; N\varphi^2\right]\\
&= E_0\!\left[\tfrac{M(M+1)(2M+1)}{3} + N\varphi^2\right],
\end{split}
$$

where the cross term vanishes by symmetry ($\sum_{n=-M}^M n = 0$) and the
$\varphi$-independent piece $\sum_{n=-M}^M n^2$ is the standard
$M(M+1)(2M+1)/3$. Differentiating,

$$
I_{\mathrm{tot}}(N,\Phi) = -\partial_\Phi E_{\mathrm{tot}}
= -\frac{2NE_0}{\Phi_0}\,\varphi
= -N\,\frac{\hbar^2}{mR^2\Phi_0}\,\varphi.
$$

The slope $-2NE_0/\Phi_0$ is exactly $N$ times the single-particle slope:
each filled level contributes one copy of the same linear response. (The
pair contributions at $\pm n$ cancel in the *constant* piece but reinforce
in the $\varphi$-piece — see (c) below.) At $\varphi=1/2$ the filled set
shifts to $\{-M+1,\ldots,M+1\}$ and the same calculation gives
$I_{\mathrm{tot}} = -(2NE_0/\Phi_0)(\varphi-1)$ on the next branch; the
current jumps from $-NE_0/\Phi_0$ to $+NE_0/\Phi_0$ at $\varphi=1/2$, then
repeats with period $\Phi_0$.

**(c)** With $k_F=N/(2R)$ (one-dimensional density $N/L=N/(2\pi R)$, so
$k_F=\pi\cdot N/L = N/(2R)$ for spinless fermions in a box of length $L$),
$v_F=\hbar k_F/m=\hbar N/(2mR)$, and $L=2\pi R$, compute the universal
combination:

$$
\frac{q\,v_F}{L} = \frac{q\,\hbar N}{4\pi mR^2}.
$$

From part (b) the maximum current on the branch is
$|I_{\mathrm{tot}}^{\max}| = NE_0/\Phi_0$, evaluated at $\varphi=1/2^-$.
Substituting $E_0=\hbar^2/(2mR^2)$ and $\Phi_0=h/q=2\pi\hbar/q$:

$$
\frac{NE_0}{\Phi_0}
= \frac{N\hbar^2/(2mR^2)}{2\pi\hbar/q}
= \frac{Nq\hbar}{4\pi mR^2} = \frac{qv_F}{L}.
$$

So $I_{\mathrm{tot}}^{\max}=qv_F/L$ in the large-$N$ limit (up to a sign set
by the charge convention).

*Interpretation.* All $N$ levels contribute to $\partial_\Phi E_{\mathrm{tot}}$:
the per-level slope $-2E_0\varphi/\Phi_0$ adds $N$ times because every level
shifts in the same direction with flux (the level-$n$ kinetic momentum is
$\hbar(n-\varphi)/R$, and $\partial_\Phi$ acts on the $-\varphi$ piece
identically for all $n$). The factor $N$ is absorbed into the Fermi velocity
$v_F\propto N$, leaving a result $qv_F/L$ that depends only on Fermi-surface
data. Physically, the answer equals the current a single classical carrier
of charge $q$ would deposit if it traversed the loop once per period
$L/v_F$ — the universal mesoscopic persistent-current amplitude, derived
here from the canonical many-body ground state.

<!-- ─── -->

**3. Half-flux doublet under perturbation.** At $\Phi=\Phi_0/2$ the doublet $\{\vert 0\rangle,\vert 1\rangle\}$ is protected by the anticommuting pair $\hat T_\pi$ (translation by $\pi$) and $\hat S=\hat R\hat U_{LG}$ (reflection plus large gauge) derived in lecture. Add a static potential $V(\theta)$ to the ring and study which symmetries survive, and when a gap opens.

(a) Show that $\hat T_\pi V(\theta)\hat T_\pi^{-1}=V(\theta+\pi)$ and $\hat S V(\theta)\hat S^{-1}=V(-\theta)$. (Hint: $\hat U_{LG}$ is a rephasing by $\mathrm{e}^{-\mathrm{i}\theta}$, which commutes with any function of $\theta$.)

(b) Complete the symmetry-and-gap table. Mark $\hat T_\pi$ and $\hat S$ as preserved (P) or broken (B), then say whether the doublet gap is forbidden by symmetry, allowed at first order in $V_0$, or allowed only at higher order.

| $V(\theta)$        | $\hat T_\pi$ | $\hat S$ | Gap status |
|--------------------|--------------|----------|------------|
| $V_0\cos\theta$    |              |          |            |
| $V_0\sin\theta$    |              |          |            |
| $V_0\cos 2\theta$  |              |          |            |
| $V_0\cos 3\theta$  |              |          |            |

(c) For each row, compute the doublet matrix $V_{ab}=\langle a\vert V\vert b\rangle$ with $a,b\in\{0,1\}$ and confirm consistency: a nonzero off-diagonal at first order requires at least one of $\hat T_\pi,\hat S$ to be broken, and the off-diagonal must vanish whenever both are preserved.

(d) Two perturbations with the same symmetry status can still differ. Show that $\cos\theta$ opens a first-order gap of size $V_0$, while $\cos 3\theta$ also breaks $\hat T_\pi$ but has a vanishing doublet matrix element at first order. Identify the angular-momentum selection rule that distinguishes them, and argue whether $\cos 3\theta$ ever opens a gap at higher order.

(e) Connect to the anomaly. In one or two sentences, explain why $\cos 2\theta$ at arbitrary strength leaves the doublet exactly degenerate, while an infinitesimal $\cos\theta$ already gaps it. What does this say about how anomaly-protected degeneracies differ from accidental level crossings?

**Solution.**

**(a)** The operators $\hat T_\pi$, $\hat R$, $\hat U_{LG}$ all act on the
$\theta$-basis as either translations, reflections, or diagonal-phase
rephasings.

*Translation.* $\hat T_\pi$ shifts $\theta\to\theta+\pi$, so any
multiplication operator transforms as
$\hat T_\pi V(\hat\theta)\hat T_\pi^{-1} = V(\hat\theta+\pi)$.

*Reflection-with-large-gauge.* $\hat S = \hat R\hat U_{LG}$. The large gauge
$\hat U_{LG}$ multiplies wavefunctions by the phase
$\mathrm{e}^{-\mathrm{i}\theta}$; in the position basis it is diagonal, so it
commutes with any other diagonal operator $V(\hat\theta)$:
$\hat U_{LG}V(\hat\theta)\hat U_{LG}^{-1} = V(\hat\theta)$. The reflection
sends $\theta\to-\theta$:
$\hat R V(\hat\theta)\hat R^{-1} = V(-\hat\theta)$. Composing,

$$
\hat S\,V(\hat\theta)\,\hat S^{-1}
= \hat R\,[\hat U_{LG}V(\hat\theta)\hat U_{LG}^{-1}]\,\hat R^{-1}
= \hat R\,V(\hat\theta)\,\hat R^{-1} = V(-\hat\theta).
$$

The two rules $V(\theta)\to V(\theta+\pi)$ (for $\hat T_\pi$) and
$V(\theta)\to V(-\theta)$ (for $\hat S$) are all that is needed to classify
any explicit potential.

**(b)** Apply the rules to each row.

- $V_0\cos\theta$: $\cos(\theta+\pi)=-\cos\theta$, so $\hat T_\pi$ takes
  $V\to-V$ — **broken**. $\cos(-\theta)=\cos\theta$, so $\hat S$ is
  **preserved**.
- $V_0\sin\theta$: $\sin(\theta+\pi)=-\sin\theta$ — $\hat T_\pi$ **broken**.
  $\sin(-\theta)=-\sin\theta$ — $\hat S$ **broken**.
- $V_0\cos 2\theta$: $\cos(2\theta+2\pi)=\cos 2\theta$ — $\hat T_\pi$
  **preserved**. $\cos(-2\theta)=\cos 2\theta$ — $\hat S$ **preserved**.
- $V_0\cos 3\theta$: $\cos(3\theta+3\pi)=-\cos 3\theta$ — $\hat T_\pi$
  **broken**. $\cos(-3\theta)=\cos 3\theta$ — $\hat S$ **preserved**.

*Gap status*: the doublet is the smallest faithful representation of the
anticommuting pair, so it cannot be split as long as **both** symmetries
survive. Whenever at least one is broken, splitting is *allowed*, but
whether it appears at first order in $V_0$ requires a nonzero matrix element
on the doublet (treated in (c) and (d)).

| $V(\theta)$        | $\hat T_\pi$ | $\hat S$ | Gap status |
|--------------------|--------------|----------|------------|
| $V_0\cos\theta$    | B            | P        | allowed; appears at first order |
| $V_0\sin\theta$    | B            | B        | allowed; appears at first order |
| $V_0\cos 2\theta$  | P            | P        | forbidden to all orders |
| $V_0\cos 3\theta$  | B            | P        | allowed; first-order matrix vanishes, higher orders possible |

**(c)** With $\vert n\rangle = (1/\sqrt{2\pi})\int_0^{2\pi}\mathrm{e}^{\mathrm{i}n\theta}\vert\theta\rangle\,\mathrm{d}\theta$,

$$
\langle m\vert\mathrm{e}^{\mathrm{i}k\theta}\vert n\rangle = \delta_{m,n+k},
\qquad
\langle m\vert\cos k\theta\vert n\rangle = \tfrac12(\delta_{m,n+k}+\delta_{m,n-k}).
$$

On the doublet $\{\vert 0\rangle,\vert 1\rangle\}$:

- $V_0\cos\theta$:
  $\langle 0\vert V\vert 1\rangle = (V_0/2)(\delta_{0,2}+\delta_{0,0}) = V_0/2$;
  $\langle 0\vert V\vert 0\rangle = (V_0/2)(\delta_{0,1}+\delta_{0,-1}) = 0$;
  $\langle 1\vert V\vert 1\rangle = 0$ likewise. Matrix
  $V\vert_{\rm doublet} = (V_0/2)\hat X$. Nonzero; consistent with
  $\hat T_\pi$ broken.
- $V_0\sin\theta = (V_0/2\mathrm{i})(\mathrm{e}^{\mathrm{i}\theta}-\mathrm{e}^{-\mathrm{i}\theta})$:
  $\langle 0\vert V\vert 1\rangle = (V_0/2\mathrm{i})(\delta_{0,2}-\delta_{0,0}) = \mathrm{i}V_0/2$;
  diagonals zero. Matrix $V\vert_{\rm doublet} = (V_0/2)\hat Y$. Nonzero;
  consistent with both symmetries broken.
- $V_0\cos 2\theta$:
  $\langle 0\vert V\vert 1\rangle = (V_0/2)(\delta_{0,3}+\delta_{0,-1}) = 0$;
  diagonals $\langle 0\vert V\vert 0\rangle = (V_0/2)(\delta_{0,2}+\delta_{0,-2}) = 0$,
  $\langle 1\vert V\vert 1\rangle = (V_0/2)(\delta_{1,3}+\delta_{1,-1}) = 0$.
  Matrix $V\vert_{\rm doublet} = 0$. Consistent with both symmetries
  preserved.
- $V_0\cos 3\theta$:
  $\langle 0\vert V\vert 1\rangle = (V_0/2)(\delta_{0,4}+\delta_{0,-2}) = 0$;
  diagonals zero similarly. Matrix $V\vert_{\rm doublet} = 0$ at first
  order, even though $\hat T_\pi$ is broken — the breaking is not "felt"
  inside the doublet at $O(V_0)$.

The pattern matches the symmetry argument: $V\vert_{\rm doublet}$ can be
nonzero (and gap the doublet) only when at least one anticommuting symmetry
is broken; it must vanish on the doublet whenever both are preserved.

**(d)** The selection rule: $\langle 0\vert\cos k\theta\vert 1\rangle\ne 0$
requires $\delta_{0,1+k}=1$ or $\delta_{0,1-k}=1$, i.e.
$k=\pm 1$. Only the $k=1$ Fourier component of $V(\theta)$ couples the two
doublet states at first order — the doublet has angular-momentum content
$\Delta n = 1$, and a potential whose Fourier harmonic matches this
selection rule "fits" inside it; harmonics with $|k|\ne 1$ couple $\vert 0\rangle$
and $\vert 1\rangle$ only via virtual transitions to states outside the doublet
($\vert\pm 3\rangle$ for $\cos 3\theta$, $\vert\pm 2\rangle$ for $\cos 2\theta$,
etc.). For $\cos\theta$ this gives an explicit first-order gap

$$
\Delta E\bigl[\cos\theta\bigr] = \lambda_+ - \lambda_-
= \tfrac{V_0}{2} - (-\tfrac{V_0}{2}) = V_0
$$

(eigenvalues of $(V_0/2)\hat X$). For $\cos 3\theta$, the first-order matrix
on the doublet is zero, so degenerate perturbation theory at first order
leaves the doublet degenerate. *At higher order*, $\cos 3\theta$ couples
$\vert 0\rangle\to\vert\pm 3\rangle\to\ldots\to\vert 1\rangle$. The path
$\vert 0\rangle\to\vert 3\rangle\to\vert 0\rangle$ shifts $\vert 0\rangle$ but
does not couple it to $\vert 1\rangle$; reaching $\vert 1\rangle$ requires a
chain like $\vert 0\rangle\to\vert 3\rangle\to\vert 6\rangle\to\ldots$ that never
closes back onto $\vert 1\rangle$ at any finite order — because every step
changes $n$ by $\pm 3$, while $\vert 0\rangle\to\vert 1\rangle$ would need
$\Delta n=\pm 1\pmod 0$. So $\cos 3\theta$ alone does **not** open a gap at
any order. (It can, however, combine with another perturbation that supplies
the missing $\Delta n$; symmetry only guarantees protection when *all*
admissible perturbations preserve $\hat T_\pi$ and $\hat S$.)

**(e)** $\cos 2\theta$ commutes with both $\hat T_\pi$ and $\hat S$, so the
two anticommuting symmetries remain exact symmetries of the full
$\hat H_0+\hat V$ at *every* strength of $V_0$. Their smallest faithful
representation is two-dimensional, so the doublet cannot be lifted — the
degeneracy is **anomaly-protected** and survives non-perturbatively. By
contrast, $\cos\theta$ breaks $\hat T_\pi$ even infinitesimally: the
protection mechanism is gone, the anomaly no longer applies, and there is no
*topological* obstruction to lifting the doublet — a gap opens
immediately at first order. The distinction is qualitative: anomaly
protection enforces degeneracy by symmetry (zero-measure perturbation
breaking it removes the protection), while accidental degeneracies (two
parabolas crossing at half-integer flux) are lifted by *any* generic
perturbation that has the right Fourier content.

<!-- ─── -->

**4. Cooper pair versus electron.** Compare the flux response of a ring carrying a single electron ($q = -e$) with a superconducting ring carrying Cooper pairs ($q = -2e$).

(a) What is the flux quantum for each case? Compute both numerically.

(b) A normal ring shows AB oscillations in resistance with period $h/e$. A superconducting ring quantizes flux in units of $h/(2e)$. Explain the physical origin of the factor-of-two difference.

(c) In a mesoscopic normal ring at low temperature, both $h/e$ and $h/(2e)$ periodicities are observed. The $h/(2e)$ component arises from time-reversed path pairs. Explain this using the concept of weak localization.

**Solution.**

**(a)** The flux quantum is $\Phi_0 = h/q$, set by the magnitude of the charge
of the coherent object. With $h = 6.626\times10^{-34}\,\mathrm{J\cdot s}$ and
$e = 1.602\times10^{-19}\,\text{C}$:

- *Single electron*, $\vert q\vert = e$:

$$
\vert\Phi_0\vert = \frac{h}{e}
= \frac{6.626\times10^{-34}}{1.602\times10^{-19}}
\approx 4.14\times10^{-15}\ \text{Wb}.
$$

- *Cooper pair*, $\vert q\vert = 2e$:

$$
\vert\Phi_0\vert = \frac{h}{2e}
\approx 2.07\times10^{-15}\ \text{Wb}.
$$

The superconducting flux quantum is exactly half the normal-metal one.

**(b)** The period is fixed by the charge of whatever quantum object carries
the coherent phase around the loop. In a **normal-metal** ring the interfering
object is a single electron of charge $e$; the Aharonov-Bohm phase it picks up
around the loop is $\Delta\Phi_{\mathrm{AB}} = e\Phi/\hbar$, which is
$2\pi$-periodic in $\Phi$ with period $h/e$ — hence resistance oscillations of
period $h/e$. In a **superconductor** the coherent object is not a lone
electron but the **Cooper pair**: the macroscopic condensate wavefunction has
charge $q = 2e$, and single-valuedness of that wavefunction around the loop
quantizes the enclosed flux as $\Phi = n\,h/(2e)$. The charge that couples to
the flux has doubled, so the flux unit is halved: $h/(2e)$ versus $h/e$. The
factor of two is a direct count of the pairing — historically it was the
decisive experimental evidence that the superconducting charge carriers are
*pairs* of electrons (Deaver–Fairbank and Doll–Näbauer, 1961).

**(c)** A disordered normal ring shows two superimposed oscillations, with
different physical origins.

The $h/e$ component (Aharonov–Bohm) comes from an electron traversing the ring
through its two arms — clockwise versus counterclockwise — a single net
encirclement of the flux. The two amplitudes pick up a relative phase
$e\Phi/\hbar$, giving period $h/e$. But the *offset* of this oscillation
depends on the detailed, essentially random impurity configuration of the
particular ring, so averaging over an ensemble of rings (or over many flux
periods) washes the $h/e$ term out.

The $h/(2e)$ component (Al'tshuler–Aronov–Spivak oscillations) comes from
**pairs of time-reversed paths**. Consider an electron that is backscattered
around a closed loop and returns to its starting point, and the *same* loop
traversed in the opposite sense. These two paths are related by time reversal;
they enclose the flux with **opposite sign**, so their relative AB phase is
$2e\Phi/\hbar$ — period $h/(2e)$. At $\Phi = 0$, time-reversal symmetry makes
the two amplitudes *exactly equal and in phase*: they interfere
constructively, enhancing the probability for the electron to return to its
origin. Enhanced backscattering means reduced conductance — this is **weak
localization**. Threading flux spoils the constructive interference, so the
conductance oscillates, with period $h/(2e)$. Crucially, the constructive
condition at $\Phi=0$ is pinned by time-reversal symmetry, *not* by the
impurity configuration; it is the same for every ring. The $h/(2e)$ component
therefore **survives ensemble and disorder averaging**, while the
configuration-dependent $h/e$ component does not. That is why the $h/(2e)$
periodicity shows up robustly in disordered normal rings.

<!-- ─── -->

**5. Flux-dependent tunneling.** A barrier at $\theta = 0$ allows tunneling across the ring. The tunneling amplitude is $\mathcal{T}(\Phi) \propto \cos(\pi\Phi/\Phi_0)$.

(a) At what flux values is tunneling maximized? Minimized? Interpret physically.

(b) The tunneling rate $\Gamma \propto \vert\mathcal{T}\vert^2$ oscillates with flux. Sketch $\Gamma(\Phi/\Phi_0)$ for two full periods. What is the contrast ratio $\Gamma_\text{max}/\Gamma_\text{min}$?

(c) A flux qubit exploits this flux-dependent tunneling at $\Phi \approx \Phi_0/2$. Near this operating point, expand $\mathcal{T}$ to first order in $\delta\Phi = \Phi - \Phi_0/2$ and show the qubit is maximally sensitive to small flux changes.

**Solution.**

**(a)** Write $\mathcal{T}(\Phi) = \mathcal{T}_0\cos(\pi\Phi/\Phi_0)$.

- *Maximized* (in magnitude) when $\cos(\pi\Phi/\Phi_0) = \pm1$, i.e.
  $\pi\Phi/\Phi_0 = m\pi$, so $\Phi = m\Phi_0$ — **integer flux**.
- *Minimized* (zero) when $\cos(\pi\Phi/\Phi_0) = 0$, i.e.
  $\pi\Phi/\Phi_0 = (m+\tfrac12)\pi$, so $\Phi = (m+\tfrac12)\Phi_0$ —
  **half-integer flux**.

A particle tunnelling from one side of the ring to the other can go around
either semicircle. The two semicircular paths enclose half the ring each and
acquire opposite AB phases $\pm\pi\Phi/\Phi_0$, so their **relative** phase is
$2\pi\Phi/\Phi_0$. At integer flux this relative phase is a multiple of
$2\pi$: the two path amplitudes add **constructively** and tunnelling is
maximal. At half-integer flux the relative phase is an odd multiple of $\pi$:
the two amplitudes are exactly out of phase, interfere **destructively**, and
cancel — tunnelling is switched off completely. The barrier transmission is
gated by the enclosed flux even though the particle never touches the field
region.

**(b)** The rate is $\Gamma(\Phi) = \Gamma_0\cos^2(\pi\Phi/\Phi_0)$, a
raised-cosine ($\cos^2$) oscillation of period $\Phi_0$. Over two periods,
$\Phi/\Phi_0\in[0,2]$:

```
 Γ/Γ0
  1 ┤●            ●            ●
    │ ╲          ╱ ╲          ╱
    │  ╲        ╱   ╲        ╱
    │   ╲      ╱     ╲      ╱
  0 ┤    ●────●       ●────●
    └──┬────┬────┬────┬────┬──  Φ/Φ0
       0   0.5   1   1.5   2
```

It peaks at $\Gamma_0$ at every integer flux and drops to $0$ at every
half-integer flux. The contrast ratio is

$$
\frac{\Gamma_{\max}}{\Gamma_{\min}} = \frac{\Gamma_0}{0} \to \infty.
$$

Ideally the modulation is total: perfect destructive interference at
half-integer flux extinguishes the rate completely. In a real device a small
path asymmetry or decoherence lifts the minimum slightly above zero, giving a
large but finite contrast ratio rather than a true infinity.

**(c)** Set $\delta\Phi = \Phi - \Phi_0/2$ and expand about the half-flux
point:

$$
\mathcal{T} = \mathcal{T}_0\cos\!\left(\frac{\pi\Phi}{\Phi_0}\right)
= \mathcal{T}_0\cos\!\left(\frac{\pi}{2} + \frac{\pi\,\delta\Phi}{\Phi_0}\right)
= -\,\mathcal{T}_0\sin\!\left(\frac{\pi\,\delta\Phi}{\Phi_0}\right)
\approx -\,\mathcal{T}_0\,\frac{\pi\,\delta\Phi}{\Phi_0}.
$$

So near $\Phi_0/2$ the tunnelling amplitude is **linear** in $\delta\Phi$: it
passes through zero with finite slope. The slope of the full curve is
$\mathrm{d}\mathcal{T}/\mathrm{d}\Phi = -\mathcal{T}_0(\pi/\Phi_0)\sin(\pi\Phi/\Phi_0)$,
whose magnitude is largest exactly where $\sin(\pi\Phi/\Phi_0) = \pm1$ — at
**half-integer flux**:

$$
\left.\frac{\mathrm{d}\mathcal{T}}{\mathrm{d}\Phi}\right|_{\Phi_0/2}
= -\,\frac{\pi\,\mathcal{T}_0}{\Phi_0}
\qquad(\text{maximal magnitude}).
$$

By contrast, at integer flux $\mathcal{T}$ sits at an extremum and
$\mathrm{d}\mathcal{T}/\mathrm{d}\Phi = 0$ — there it is first-order
*insensitive* to flux. Operating a flux qubit at $\Phi\approx\Phi_0/2$ thus
places it where the tunnelling amplitude — and hence the qubit gap that the
tunnelling controls — responds linearly and most steeply to a small flux
change: maximal flux sensitivity, the working principle of the device as a
flux transducer. (The same steep slope that makes $\Phi_0/2$ the most
sensitive detection point also makes it the most exposed to flux noise; a
qubit operated as a quiet memory is instead parked where
$\mathrm{d}\mathcal{T}/\mathrm{d}\Phi$ is small.)

<!-- ─── -->

**6. SQUID magnetometry.** A dc SQUID has two Josephson junctions, each with critical current $I_c$. As derived in the lecture, the time-averaged voltage is $\langle V \rangle = R\sqrt{I_{\text{bias}}^2 - 4I_c^2\cos^2(\pi\Phi/\Phi_0)}$.

(a) When $I_\text{max}$ is exceeded, the SQUID switches to a resistive state. Explain why measuring this switching current reveals the enclosed flux $\Phi$.

(b) Compute the flux sensitivity $\mathrm{d}I_\text{max}/\mathrm{d}\Phi$ near $\Phi = \Phi_0/4$. For $I_c = 10\,\mu$A, express this in amperes per flux quantum.

(c) SQUIDs can detect flux changes as small as $10^{-6}\Phi_0$. Convert this to a magnetic field sensitivity for a SQUID loop of area $1\,\text{mm}^2$, and compare to the Earth's magnetic field ($\sim 50\,\mu$T).

**Solution.**

**(a)** The two junctions in parallel can carry a dissipationless
supercurrent up to a maximum set by their interference,

$$
I_{\max}(\Phi) = 2I_c\left\vert\cos\!\left(\frac{\pi\Phi}{\Phi_0}\right)\right\vert.
$$

This is the largest current the superconducting channel can absorb. As long as
the bias current obeys $I_{\text{bias}} < I_{\max}$, the average phase $\delta$
locks to a fixed value, the supercurrent carries everything, and the voltage
is zero. The moment $I_{\text{bias}}$ exceeds $I_{\max}$, the supercurrent can
no longer absorb the full bias: the phase $\delta$ starts to wind, the ac
Josephson effect generates a finite time-averaged voltage, and the device
**switches** to the resistive state. The bias current at which this happens is
precisely $I_{\max}(\Phi)$. Because $I_{\max}$ is a *known* function of the
enclosed flux, $2I_c\vert\cos(\pi\Phi/\Phi_0)\vert$, measuring the switching
current measures $\cos(\pi\Phi/\Phi_0)$ and hence determines $\Phi$ (modulo a
flux quantum and the cosine's symmetry). The SQUID converts an enclosed
magnetic flux into an electrically measurable critical current — that is what
makes it a magnetometer.

**(b)** Near $\Phi = \Phi_0/4$ the argument is $\pi\Phi/\Phi_0 = \pi/4$, where
$\cos(\pi/4) = 1/\sqrt2 > 0$; the modulus can be dropped, so
$I_{\max} = 2I_c\cos(\pi\Phi/\Phi_0)$. Differentiating,

$$
\frac{\mathrm{d}I_{\max}}{\mathrm{d}\Phi}
= -\,\frac{2\pi I_c}{\Phi_0}\sin\!\left(\frac{\pi\Phi}{\Phi_0}\right).
$$

At $\Phi = \Phi_0/4$, $\sin(\pi/4) = 1/\sqrt2$, so

$$
\left.\frac{\mathrm{d}I_{\max}}{\mathrm{d}\Phi}\right|_{\Phi_0/4}
= -\,\frac{2\pi I_c}{\Phi_0}\cdot\frac{1}{\sqrt2}
= -\,\frac{\sqrt2\,\pi I_c}{\Phi_0}.
$$

Expressed in amperes per flux quantum (multiplying the magnitude by $\Phi_0$),

$$
\left\vert\frac{\mathrm{d}I_{\max}}{\mathrm{d}\Phi}\right\vert
= \sqrt2\,\pi I_c \quad\text{per }\Phi_0.
$$

For $I_c = 10\,\mu\text{A}$,

$$
\sqrt2\,\pi\,(10\,\mu\text{A}) \approx 44.4\,\mu\text{A per }\Phi_0.
$$

The negative sign means $I_{\max}$ falls as the flux increases on this branch;
$\Phi_0/4$ sits on the steep flank of the $I_{\max}(\Phi)$ curve, a
representative SQUID operating point where flux is transduced into a sizeable
current change.

**(c)** A SQUID is a superconducting device, so the relevant flux quantum is
$\Phi_0 = h/(2e) \approx 2.07\times10^{-15}\,\text{Wb}$. A detectable flux
change $\delta\Phi = 10^{-6}\,\Phi_0$ is

$$
\delta\Phi = 10^{-6}\times 2.07\times10^{-15}\,\text{Wb}
\approx 2.07\times10^{-21}\,\text{Wb}.
$$

For a loop of area $A = 1\,\text{mm}^2 = 10^{-6}\,\text{m}^2$, the corresponding
magnetic-field sensitivity is

$$
\delta B = \frac{\delta\Phi}{A}
= \frac{2.07\times10^{-21}\,\text{Wb}}{10^{-6}\,\text{m}^2}
\approx 2.1\times10^{-15}\,\text{T} = 2.1\ \text{fT}.
$$

Compared with the Earth's field $B_\oplus \sim 50\,\mu\text{T} = 5\times10^{-5}\,\text{T}$,

$$
\frac{B_\oplus}{\delta B} \approx \frac{5\times10^{-5}}{2.1\times10^{-15}}
\approx 2.4\times10^{10}.
$$

The SQUID resolves magnetic fields about $2\times10^{10}$ times weaker than
the Earth's — femtotesla sensitivity. This is fine enough to detect the
magnetic fields produced by currents in the human brain and heart
(magnetoencephalography and magnetocardiography), which is exactly what
SQUID magnetometers are used for.

<!-- ─── -->

**7. Ground state phase transition.** As flux increases from $0$ to $\Phi_0$, the ground state quantum number changes from $n = 0$ to $n = 1$. This is a quantum phase transition.

(a) At what flux value does the transition occur? Is it first-order or continuous? (Hint: does the ground state energy have a cusp or a smooth crossover?)

(b) The persistent current $I(\Phi)$ is discontinuous at the transition point. Relate the magnitude of the jump to the ring parameters $m$, $R$, and $q$.

(c) In a realistic system with disorder or finite temperature, the sharp transition is smoothed. Explain qualitatively why, and sketch the smoothed $I(\Phi)$.

**Solution.**

**(a)** The ground state is the branch with $n$ nearest $\Phi/\Phi_0$. As the
flux rises from $0$ to $\Phi_0$, branches $n=0$ and $n=1$ exchange roles
exactly where their parabolas cross,

$$
E_0(\Phi) = E_1(\Phi)
\;\Longrightarrow\;
\left(\frac{\Phi}{\Phi_0}\right)^2 = \left(1-\frac{\Phi}{\Phi_0}\right)^2
\;\Longrightarrow\;
\Phi = \frac{\Phi_0}{2}.
$$

The transition is at **$\Phi = \Phi_0/2$**, the half-integer flux. The
ground-state energy $E_{\mathrm{gs}}(\Phi) = \min_n E_n(\Phi)$ is continuous
there, but it is built from two *different* parabolas on the two sides, meeting
with *different* slopes — so $E_{\mathrm{gs}}$ has a **cusp** (a kink), and its
first derivative $\partial E_{\mathrm{gs}}/\partial\Phi$ jumps. A discontinuity
in the first derivative of the ground-state energy, produced by a genuine
crossing of two levels, is the defining signature of a **first-order** quantum
phase transition. The ground-state wavefunction changes abruptly from
$\vert 0\rangle$ to $\vert 1\rangle$ — there is no smooth interpolation. So the
transition is first-order, at $\Phi = \Phi_0/2$.

**(b)** The persistent current $I = -\partial E_{\mathrm{gs}}/\partial\Phi$
inherits the discontinuity. Using the
lecture's persistent-current formula $I = (\hbar^2/(mR^2\Phi_0))(n_* - \Phi/\Phi_0)$ on the
branch with quantum number $n_*$, evaluate it on each side of $\Phi = \Phi_0/2$:

$$
\begin{split}
I(\Phi_0/2^-) &= \frac{q\hbar}{2\pi mR^2}\left(0 - \tfrac12\right)
= -\,\frac{q\hbar}{4\pi mR^2} \qquad (\text{branch }n_*=0),\\
I(\Phi_0/2^+) &= \frac{q\hbar}{2\pi mR^2}\left(1 - \tfrac12\right)
= +\,\frac{q\hbar}{4\pi mR^2} \qquad (\text{branch }n_*=1).
\end{split}
$$

The jump across the transition is

$$
\Delta I = I(\Phi_0/2^+) - I(\Phi_0/2^-) = \frac{q\hbar}{2\pi mR^2},
\qquad
\vert\Delta I\vert = \frac{\vert q\vert\,\hbar}{2\pi mR^2}.
$$

The magnitude depends only on the ring parameters $m$, $R$ and the charge $q$;
for an electron $\vert\Delta I\vert = e\hbar/(2\pi mR^2)$. It equals
$2I_{\max}$, twice the lecture sawtooth amplitude $I_{\max} = q\hbar/(4\pi mR^2)$ — the current swings
the full distance between the two branch extrema as the ground state switches.

**(c)** A real ring is never perfectly clean. Any disorder potential — for
instance a $V_0\cos\theta$ term as in Problem 3 — has matrix elements coupling
$\vert 0\rangle$ and $\vert 1\rangle$, and that coupling opens a gap at the
crossing. The true level crossing becomes an **avoided crossing**: the two
branches no longer touch, and the ground state evolves *smoothly and
adiabatically* from $\vert 0\rangle$-like to $\vert 1\rangle$-like as the flux
is swept. Consequently $E_{\mathrm{gs}}(\Phi)$ becomes analytic — the cusp is
rounded — and its derivative $I(\Phi) = -\partial E_{\mathrm{gs}}/\partial\Phi$
becomes **continuous**: the vertical sawtooth jump is replaced by a steep but
finite-slope segment passing smoothly through zero. Finite temperature smooths
it further, by thermally populating both branches near the crossing (Problem
2c). The smoothed current looks like a rounded sawtooth:

```
  I
 +Imax ┤╲       ╭╴╲       ╭╴╲
       │ ╲     ╱    ╲     ╱
   0   ┤──╲───╱──────╲───╱────  Φ/Φ0
       │   ╲ ╱        ╲ ╱
 -Imax ┤    ╰╴         ╰╴
       └──┬────┬────┬────┬──
         0.5  1.5  2.5
```

— straight linear ramps joined by smooth, steep S-shaped crossovers at each
half-integer flux, instead of the idealised vertical discontinuities.

<!-- ─── -->

**8. Dimensional analysis.** The ring Hamiltonian has a single energy scale $E_0 = \hbar^2/(2mR^2)$.

(a) Express the persistent current $I$, the flux quantum $\Phi_0$, and the ground state energy gap at $\Phi = 0$ in terms of $E_0$ and fundamental constants.

(b) For an electron on a ring of radius $R = 1\,\mu$m, estimate $E_0$ in meV. At what temperature $T^*$ does thermal energy $k_BT^*$ equal $E_0$?

(c) The AB effect in mesoscopic rings was first observed at temperatures below $\sim 1$ K. Is this consistent with your estimate of $T^*$ for micrometer-scale rings?

**Solution.**

*(In this problem $E_0$ denotes the ring's energy scale $\hbar^2/(2mR^2)$, as
defined in the problem statement — not the $n=0$ branch energy of the earlier
problems.)*

**(a)** *Persistent current.* The current carried by branch $n$ is
$I_n = (q\hbar/2\pi mR^2)(n - \Phi/\Phi_0)$. Since
$E_0 = \hbar^2/(2mR^2)$ gives $\hbar/(2mR^2) = E_0/\hbar$,

$$
\frac{q\hbar}{2\pi mR^2} = \frac{q}{\pi}\cdot\frac{\hbar}{2mR^2}
= \frac{q E_0}{\pi\hbar} = \frac{2qE_0}{h},
$$

so $I_n = (2qE_0/h)\,(n - \Phi/\Phi_0)$, and the sawtooth amplitude is

$$
I_{\max} = \frac{2qE_0}{h}\cdot\frac12 = \frac{qE_0}{h}.
$$

The persistent-current scale is charge $\times$ energy scale $/$ Planck's
constant.

*Flux quantum.* $\Phi_0 = h/q$ — fixed entirely by the charge and Planck's
constant. It is **independent of $E_0$**: the flux quantum knows nothing about
the ring's size or mass, which is why the same $\Phi_0$ governs any ring of a
given charge.

*Energy gap at $\Phi = 0$.* At zero flux the spectrum is
$E_n(0) = E_0\,n^2$. The ground state is $n=0$ at energy $0$; the first
excited states are $n = \pm1$, degenerate, at energy $E_0$. The gap above the
ground state is

$$
\Delta = E_0\cdot 1^2 - 0 = E_0,
$$

exactly the energy scale itself — and the first excited level is two-fold
degenerate.

**(b)** For an electron ($m = m_e = 9.11\times10^{-31}\,\text{kg}$) on a ring
of radius $R = 1\,\mu\text{m} = 10^{-6}\,\text{m}$, with
$\hbar = 1.055\times10^{-34}\,\mathrm{J\cdot s}$:

$$
E_0 = \frac{\hbar^2}{2m_eR^2}
= \frac{(1.055\times10^{-34})^2}{2\,(9.11\times10^{-31})(10^{-6})^2}
\approx \frac{1.11\times10^{-68}}{1.82\times10^{-42}}
\approx 6.1\times10^{-27}\,\text{J}.
$$

Converting to electronvolts ($1\,\text{eV} = 1.602\times10^{-19}\,\text{J}$),

$$
E_0 \approx \frac{6.1\times10^{-27}}{1.602\times10^{-19}}\,\text{eV}
\approx 3.8\times10^{-8}\,\text{eV}
= 3.8\times10^{-5}\,\text{meV}
\quad(\approx 38\ \text{neV}).
$$

The temperature at which $k_BT^* = E_0$
($k_B = 1.38\times10^{-23}\,\text{J/K}$) is

$$
T^* = \frac{E_0}{k_B}
= \frac{6.1\times10^{-27}}{1.38\times10^{-23}}\,\text{K}
\approx 4.4\times10^{-4}\,\text{K} \approx 0.44\ \text{mK}.
$$

**(c)** The estimate $T^* \approx 0.44\,\text{mK}$ is far below the $\sim1\,$K
at which AB oscillations in mesoscopic rings are observed — yet the two
temperatures are *consistent*, because they measure different things.

$T^* = E_0/k_B$ is the scale for thermally **resolving the discrete
single-particle levels** of the ring (and for seeing a sharp persistent-current
sawtooth — the thermal-rounding scale of Problem 1). For a micron-scale ring that requires sub-millikelvin
temperatures, and indeed equilibrium persistent currents are measured only in
that range.

The AB **oscillation of the resistance/conductance**, by contrast, does not
require resolving individual levels. It only requires that the electron keep
**quantum phase coherence** all the way around the ring — that the phase
coherence length $L_\varphi$ exceed the ring circumference. $L_\varphi$ is
limited by inelastic (phase-breaking) scattering, which freezes out as the
temperature drops; below $\sim1\,$K it becomes long enough in a micron-scale
ring. So $\sim1\,$K is a **dephasing** scale, a far milder condition than
$k_BT\sim E_0$.

Observing AB oscillations below $\sim1\,$K is therefore entirely consistent
with $T^*\approx0.4\,$mK: the interference pattern survives at $1\,$K because
phase coherence does, even though the individual energy levels are not
thermally resolved until the temperature falls another three orders of
magnitude, into the millikelvin range.
