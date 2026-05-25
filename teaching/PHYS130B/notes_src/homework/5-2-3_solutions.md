# 5.2.3 Applications
Worked solutions for the homework problems in the [5.2.3 Applications](../ch5_perturbation-theory/5-2-3-applications) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Phase cancellation.** Verify in detail the cancellation of the overall $\mathrm{e}^{-\mathrm{i}E_f t/\hbar}\mathrm{e}^{\mathrm{i}E_i t_0/\hbar}$ phase in the first-order amplitude $\langle f\vert\hat{G}(t,t_0)\vert i\rangle$, and conclude that $P_{i\to f}^{(1)}$ depends only on $V_{fi}(t_1)\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}$. Why is this cancellation expected on general grounds?

**Solution.**

Start from the first-order Dyson term sandwiched between the eigenstates
$\langle f\vert$ and $\vert i\rangle$ of $\hat{H}_0$ (with $f\neq i$, so the
zeroth-order term $\langle f\vert\hat{G}_0(t,t_0)\vert i\rangle=0$):

$$
\langle f\vert\hat{G}(t,t_0)\vert i\rangle
=-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}t_1\,
\langle f\vert\hat{G}_0(t,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,t_0)\vert i\rangle.
$$

The bare propagator is diagonal in the $\hat{H}_0$ eigenbasis,
$\hat{G}_0(t,t')=\sum_n\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}\,\langle n\vert$.
Acting to the left on $\langle f\vert$ and to the right on $\vert i\rangle$
picks out single terms:

$$
\langle f\vert\hat{G}_0(t,t_1)=\mathrm{e}^{-\mathrm{i}E_f(t-t_1)/\hbar}\,\langle f\vert,
\qquad
\hat{G}_0(t_1,t_0)\vert i\rangle=\mathrm{e}^{-\mathrm{i}E_i(t_1-t_0)/\hbar}\,\vert i\rangle.
$$

Substituting, and writing $V_{fi}(t_1)\equiv\langle f\vert\hat{V}(t_1)\vert i\rangle$,

$$
\langle f\vert\hat{G}(t,t_0)\vert i\rangle
=-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}t_1\,
\mathrm{e}^{-\mathrm{i}E_f(t-t_1)/\hbar}\,V_{fi}(t_1)\,\mathrm{e}^{-\mathrm{i}E_i(t_1-t_0)/\hbar}.
$$

Now isolate the parts of the exponents that **do not depend on the integration
variable** $t_1$. Expand both exponents:

$$
-\frac{\mathrm{i}E_f(t-t_1)}{\hbar}-\frac{\mathrm{i}E_i(t_1-t_0)}{\hbar}
=\underbrace{-\frac{\mathrm{i}E_f t}{\hbar}+\frac{\mathrm{i}E_i t_0}{\hbar}}_{t_1\text{-independent}}
+\underbrace{\frac{\mathrm{i}(E_f-E_i)t_1}{\hbar}}_{t_1\text{-dependent}}.
$$

The first group is a constant prefactor; the second is exactly
$\mathrm{i}\omega_{fi}t_1$. Pulling the constant out of the integral,

$$
\langle f\vert\hat{G}(t,t_0)\vert i\rangle
=-\frac{\mathrm{i}}{\hbar}\,
\mathrm{e}^{-\mathrm{i}E_f t/\hbar}\,\mathrm{e}^{\mathrm{i}E_i t_0/\hbar}
\int_{t_0}^{t}\mathrm{d}t_1\,V_{fi}(t_1)\,\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}.
$$

Take the squared modulus. The prefactor
$\mathrm{e}^{-\mathrm{i}E_f t/\hbar}\,\mathrm{e}^{\mathrm{i}E_i t_0/\hbar}$ is a
product of two pure phases, each of unit modulus, so it contributes a factor
$1$ to $\vert\cdot\vert^2$. Likewise $\vert-\mathrm{i}/\hbar\vert^2=1/\hbar^2$.
Hence

$$
P_{i\to f}^{(1)}(t,t_0)=\bigl\vert\langle f\vert\hat{G}(t,t_0)\vert i\rangle\bigr\vert^2
=\frac{1}{\hbar^2}\left\vert\int_{t_0}^{t}\mathrm{d}t_1\,V_{fi}(t_1)\,\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}\right\vert^{2},
$$

which depends only on the combination $V_{fi}(t_1)\,\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}$.

**Why this is expected on general grounds.** A transition *probability* is a
physical observable, while the two phases that cancelled are not. The factor
$\mathrm{e}^{-\mathrm{i}E_f t/\hbar}$ is the free evolution accrued by the final
state and $\mathrm{e}^{\mathrm{i}E_i t_0/\hbar}$ that of the initial state — the
phases of $\hat{G}_0\vert f\rangle$ and $\hat{G}_0\vert i\rangle$. Two facts
make them unobservable. First, a global phase on a state has no physical
content: $\vert i\rangle$ and $\mathrm{e}^{\mathrm{i}\theta}\vert i\rangle$
describe the same physics, so an amplitude can only enter a probability through
its modulus. Second, the *zero of energy* is a convention: shifting
$\hat{H}_0\to\hat{H}_0+c\hat{I}$ sends $E_n\to E_n+c$, multiplying the amplitude
by the extra phase $\mathrm{e}^{-\mathrm{i}c(t-t_0)/\hbar}$, which again drops
out of $\vert\cdot\vert^2$. Only the **energy difference** $E_f-E_i$, i.e. the
Bohr frequency $\omega_{fi}$, is convention-independent — and it is precisely
$\omega_{fi}$ that survives in $P^{(1)}$. The cancellation is the statement that
the answer respects both invariances.

<!-- ─── -->

**2. Sinc-squared properties.** From $P_{i\to f}^{(1)}(t)=\frac{|V_{fi}|^2}{\hbar^2}\bigl[\sin((\omega_{fi}-\omega)t/2)/((\omega_{fi}-\omega)/2)\bigr]^2$ with $\alpha=(\omega_{fi}-\omega)/2$, derive each of the following:

(a) Peak height $P^{(1)}\vert_{\alpha=0}=\vert V_{fi}\vert^{2}t^{2}/\hbar^{2}$.

(b) First zero at $\alpha t=\pi$, i.e. width $\Delta\alpha\sim\pi/t$.

(c) Integrated weight $\int_{-\infty}^{\infty}\mathrm{d}\alpha\,(\sin\alpha t/\alpha)^{2}=\pi t$.

Explain why (a)$\times$(b)$\sim$(c) is the algebraic origin of a **constant rate** in the long-time limit.

**Solution.**

With $\alpha=(\omega_{fi}-\omega)/2$, $P_{i\to f}^{(1)}(t)=\frac{|V_{fi}|^2}{\hbar^2}\bigl[\sin((\omega_{fi}-\omega)t/2)/((\omega_{fi}-\omega)/2)\bigr]^2$ reads

$$
P^{(1)}(t)=\frac{\vert V_{fi}\vert^{2}}{\hbar^{2}}\left(\frac{\sin\alpha t}{\alpha}\right)^{2}.
$$

**(a) Peak height.** The kernel $(\sin\alpha t/\alpha)^2$ is largest at the
resonance $\alpha=0$. There $\sin\alpha t\approx\alpha t-\tfrac16(\alpha t)^3+\cdots$,
so $\sin\alpha t/\alpha\to t$ as $\alpha\to0$, and

$$
\left(\frac{\sin\alpha t}{\alpha}\right)^{2}\Bigg\vert_{\alpha\to0}=t^{2},
\qquad\Longrightarrow\qquad
P^{(1)}\big\vert_{\alpha=0}=\frac{\vert V_{fi}\vert^{2}t^{2}}{\hbar^{2}}.
$$

The peak grows **quadratically** in $t$.

**(b) Width.** The kernel vanishes when $\sin\alpha t=0$ with $\alpha\neq0$,
i.e. $\alpha t=n\pi$ for integer $n\neq0$. The central resonance peak is bounded
by its first zeros at $\alpha t=\pm\pi$, so

$$
\alpha_{\text{first zero}}=\frac{\pi}{t},
\qquad
\Delta\alpha\sim\frac{\pi}{t}.
$$

The peak **narrows** as $1/t$: the longer the perturbation acts, the sharper the
resonance condition becomes.

**(c) Integrated weight.** Compute
$\displaystyle I=\int_{-\infty}^{\infty}\mathrm{d}\alpha\,\left(\frac{\sin\alpha t}{\alpha}\right)^{2}$
by the substitution $u=\alpha t$ (so $\alpha=u/t$, $\mathrm{d}\alpha=\mathrm{d}u/t$):

$$
I=\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{t}\left(\frac{\sin u}{u/t}\right)^{2}
=\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{t}\,t^{2}\left(\frac{\sin u}{u}\right)^{2}
=t\int_{-\infty}^{\infty}\mathrm{d}u\,\left(\frac{\sin u}{u}\right)^{2}.
$$

The remaining integral is the standard result
$\int_{-\infty}^{\infty}(\sin u/u)^{2}\,\mathrm{d}u=\pi$ (for instance, by
Parseval applied to the rectangle-function Fourier pair, or by contour
integration of $\int(1-\cos2u)/u^2$). Therefore

$$
I=\int_{-\infty}^{\infty}\mathrm{d}\alpha\,\left(\frac{\sin\alpha t}{\alpha}\right)^{2}=\pi t.
$$

**Why (a)×(b) ∼ (c) gives a constant rate.** The three results say the
resonance peak is a spike of **height $\propto t^2$** and **width $\propto1/t$**,
so its area scales as

$$
\text{(peak height)}\times\text{(width)}\sim t^{2}\cdot\frac{1}{t}=t,
$$

matching the exact integrated weight $\pi t$ found in (c). The transition rate
is $W_i=P/t$ summed over a *continuum* of final states. Summing replaces
$\sum_f$ by $\int\mathrm{d}E_f\,\rho(E_f)$; because the kernel is sharply peaked,
only the area under the peak contributes, and that area grows **linearly** in
$t$. Dividing the area ($\propto t$) by $t$ leaves a quantity **independent of
$t$** — a constant rate. The quadratic single-state growth $t^2$ and the
linear-in-$t$ area are not in conflict: a fixed resonant state has $P\propto t^2$
(until depletion matters), but a *band* of states each spends progressively
less time on resonance as the peak narrows, and the net effect is a steady,
$t$-independent rate. This is precisely the content of Fermi's golden rule.

<!-- ─── -->

**3. Sinc-to-delta.** Prove the distributional identity

$$
\lim_{t\to\infty}\frac{1}{t}\left(\frac{\sin\alpha t}{\alpha}\right)^{\!2}=\pi\,\delta(\alpha).
$$

Hint: act on a smooth test function $g(\alpha)$ and use the change of variable $u=\alpha t$ together with $\int_{-\infty}^{\infty}(\sin u/u)^{2}\,\mathrm{d}u=\pi$.

**Solution.**

A distributional identity is a statement about what both sides do when
integrated against an arbitrary smooth, rapidly decaying test function
$g(\alpha)$. So define

$$
L_t\equiv\int_{-\infty}^{\infty}\mathrm{d}\alpha\;\frac{1}{t}\left(\frac{\sin\alpha t}{\alpha}\right)^{2}g(\alpha),
$$

and show $\lim_{t\to\infty}L_t=\pi\,g(0)$, which is by definition the action of
$\pi\,\delta(\alpha)$.

Change variables to $u=\alpha t$, so $\alpha=u/t$ and $\mathrm{d}\alpha=\mathrm{d}u/t$.
The kernel transforms as

$$
\frac{1}{t}\left(\frac{\sin\alpha t}{\alpha}\right)^{2}
=\frac{1}{t}\left(\frac{\sin u}{u/t}\right)^{2}
=\frac{1}{t}\,t^{2}\left(\frac{\sin u}{u}\right)^{2}
=t\left(\frac{\sin u}{u}\right)^{2}.
$$

Hence

$$
L_t=\int_{-\infty}^{\infty}\frac{\mathrm{d}u}{t}\;t\left(\frac{\sin u}{u}\right)^{2}g\!\left(\frac{u}{t}\right)
=\int_{-\infty}^{\infty}\mathrm{d}u\,\left(\frac{\sin u}{u}\right)^{2}g\!\left(\frac{u}{t}\right).
$$

The $t$-dependence now sits **only** inside the slowly-varying argument $u/t$ of
the test function. As $t\to\infty$, for every fixed $u$ one has $u/t\to0$ and,
since $g$ is continuous, $g(u/t)\to g(0)$. The factor
$(\sin u/u)^{2}$ is non-negative and integrable, with
$\int(\sin u/u)^2\,\mathrm{d}u=\pi<\infty$, and $\vert g(u/t)\vert$ is bounded by
$\sup\vert g\vert$; the dominating function $(\sin u/u)^2\sup\vert g\vert$ is
integrable. The dominated convergence theorem therefore lets the limit pass
through the integral:

$$
\lim_{t\to\infty}L_t
=\int_{-\infty}^{\infty}\mathrm{d}u\,\left(\frac{\sin u}{u}\right)^{2}\,
\lim_{t\to\infty}g\!\left(\frac{u}{t}\right)
=g(0)\int_{-\infty}^{\infty}\mathrm{d}u\,\left(\frac{\sin u}{u}\right)^{2}
=\pi\,g(0).
$$

Since this holds for every test function $g$,

$$
\lim_{t\to\infty}\frac{1}{t}\left(\frac{\sin\alpha t}{\alpha}\right)^{2}=\pi\,\delta(\alpha).
$$

Two remarks. The prefactor $1/t$ is exactly what is needed: without it the
kernel would have weight $\pi t\to\infty$; with it the weight is the fixed
$\pi$, the hallmark of a properly normalised nascent delta. And the rescaling
$\alpha\to2\alpha$ gives the equivalent form quoted in the lecture,
$\lim_{t\to\infty}t^{-1}(\sin\alpha t/\alpha)^2=2\pi\,\delta(2\alpha)$, used to
turn the sinc-squared into the energy-conserving delta of Fermi's golden rule.

<!-- ─── -->

**4. Density of states.** For free particles in three dimensions in a box of volume $V$,

(a) Show that the density of states is $\rho(E)=\dfrac{V m}{2\pi^{2}\hbar^{3}}\sqrt{2mE}$.

(b) Use Fermi's golden rule with this $\rho$ to express $W_i$ in terms of $\vert V_{fi}\vert^{2}$, the drive frequency $\omega$, and the initial energy $E_i$. How does $W_i$ scale with $E_i$ at fixed $\vert V_{fi}\vert$?

**Solution.**

**(a) Counting states.** A free particle in a cubic box of volume $V=L^3$ with
periodic boundary conditions has plane-wave eigenstates labelled by wavevectors
$\boldsymbol{k}=(2\pi/L)(n_x,n_y,n_z)$, $n_i\in\mathbb{Z}$, with energy
$E=\hbar^2 k^2/(2m)$. The allowed $\boldsymbol{k}$-points form a cubic lattice
of spacing $2\pi/L$, so each occupies a $k$-space volume $(2\pi/L)^3$ and the
number of states per unit $k$-space volume is $V/(2\pi)^3$.

The number of states with energy below $E$ — equivalently with wavevector
magnitude below $k=\sqrt{2mE}/\hbar$ — is the volume of a ball of radius $k$
times that density:

$$
N(E)=\frac{V}{(2\pi)^{3}}\cdot\frac{4}{3}\pi k^{3}
=\frac{V}{6\pi^{2}}\,k^{3}
=\frac{V}{6\pi^{2}}\left(\frac{2mE}{\hbar^{2}}\right)^{3/2}
=\frac{V}{6\pi^{2}\hbar^{3}}\,(2mE)^{3/2}.
$$

The density of states is the energy derivative:

$$
\rho(E)=\frac{\mathrm{d}N}{\mathrm{d}E}
=\frac{V}{6\pi^{2}\hbar^{3}}\,(2m)^{3/2}\cdot\frac{3}{2}\,E^{1/2}
=\frac{V\,(2m)^{3/2}}{4\pi^{2}\hbar^{3}}\sqrt{E}.
$$

Rewrite $(2m)^{3/2}=2m\sqrt{2m}$ to bring the result to the requested form:

$$
\rho(E)=\frac{V\cdot 2m\sqrt{2m}}{4\pi^{2}\hbar^{3}}\sqrt{E}
=\frac{Vm}{2\pi^{2}\hbar^{3}}\sqrt{2mE}.
$$

(This counts orbital states only; a spin-$\tfrac12$ particle would carry an
extra factor of $2$, which the problem statement omits.)

**(b) Transition rate into the continuum.** Fermi's golden rule for a transition
into a continuum of final states, summed with the density of states, is

$$
W_i=\frac{2\pi}{\hbar}\,\vert V_{fi}\vert^{2}\,\rho(E_f)\Big\vert_{E_f=E_i+\hbar\omega},
$$

where the energy-conserving delta of $W_{i\to f}=\frac{2\pi}{\hbar}\,|V_{fi}|^2\,\delta(E_f-E_i-\hbar\omega)$ has pinned the final
energy to the resonance shell $E_f=E_i+\hbar\omega$. Insert the
density of states evaluated at that energy:

$$
W_i=\frac{2\pi}{\hbar}\,\vert V_{fi}\vert^{2}\,
\frac{Vm}{2\pi^{2}\hbar^{3}}\sqrt{2m(E_i+\hbar\omega)}
=\frac{Vm\,\vert V_{fi}\vert^{2}}{\pi\hbar^{4}}\sqrt{2m\,(E_i+\hbar\omega)}.
$$

**Scaling with $E_i$.** At fixed matrix element $\vert V_{fi}\vert$ the rate
depends on the initial energy only through the square root,

$$
W_i\propto\sqrt{E_i+\hbar\omega}.
$$

For an initial energy large compared with the photon energy, $E_i\gg\hbar\omega$,
this reduces to $W_i\propto\sqrt{E_i}$ — the rate **grows** with energy because
the available phase space of final states (the density of states) grows as
$\sqrt{E}$. Near threshold, $E_i+\hbar\omega\to0^{+}$, the rate is suppressed:
there are simply very few states for the particle to scatter into.

<!-- ─── -->

**5. Adiabatic ramp Lorentzian.** Derive $P_{i\to f}=\frac{|V_{fi}|^2}{(E_f-E_i)^2+(\hbar/\tau)^2}$ step by step, starting from $\hat{V}(t)=\hat{V}\mathrm{e}^{t/\tau}$ for $t<0$. State the FWHM in $\omega_{fi}$ and in $\Delta E=E_f-E_i$, and sketch the lineshape.

**Solution.**

The perturbation is switched on exponentially from the infinite past and off at
$t=0$:

$$
\hat{V}(t)=\hat{V}\,\mathrm{e}^{t/\tau}\quad(t<0),\qquad \tau>0,
$$

with the system prepared in $\vert i\rangle$ at $t_0\to-\infty$ and the
transition probability to $\vert f\rangle$ asked at $t=0$. The matrix element is
$V_{fi}(t_1)=V_{fi}\,\mathrm{e}^{t_1/\tau}$ with $V_{fi}=\langle f\vert\hat{V}\vert i\rangle$
time-independent. Substitute into the master formula $P_{i\to f}^{(1)}(t,t_0)=\frac{1}{\hbar^2}\bigl|\int_{t_0}^{t}\mathrm{d}t_1\,V_{fi}(t_1)\,\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}\bigr|^2$
with $t_0\to-\infty$, $t\to0$:

$$
P_{i\to f}=\frac{1}{\hbar^{2}}\left\vert\int_{-\infty}^{0}\mathrm{d}t_1\,
V_{fi}\,\mathrm{e}^{t_1/\tau}\,\mathrm{e}^{\mathrm{i}\omega_{fi}t_1}\right\vert^{2}.
$$

**Step 1 — combine the exponents.** The two exponentials merge into a single
exponential with complex rate $\mathrm{i}\omega_{fi}+1/\tau$:

$$
\int_{-\infty}^{0}\mathrm{d}t_1\,\mathrm{e}^{(\mathrm{i}\omega_{fi}+1/\tau)t_1}.
$$

**Step 2 — evaluate the integral.** The antiderivative is
$\mathrm{e}^{(\mathrm{i}\omega_{fi}+1/\tau)t_1}/(\mathrm{i}\omega_{fi}+1/\tau)$:

$$
\int_{-\infty}^{0}\mathrm{d}t_1\,\mathrm{e}^{(\mathrm{i}\omega_{fi}+1/\tau)t_1}
=\left[\frac{\mathrm{e}^{(\mathrm{i}\omega_{fi}+1/\tau)t_1}}{\mathrm{i}\omega_{fi}+1/\tau}\right]_{-\infty}^{0}
=\frac{1}{\mathrm{i}\omega_{fi}+1/\tau}.
$$

The lower limit contributes nothing: as $t_1\to-\infty$ the modulus
$\vert\mathrm{e}^{(\mathrm{i}\omega_{fi}+1/\tau)t_1}\vert=\mathrm{e}^{t_1/\tau}\to0$
because $\tau>0$. This is exactly the role of the adiabatic switch-on — it
regulates the integral at the infinite past.

**Step 3 — take the squared modulus.** With
$\vert\mathrm{i}\omega_{fi}+1/\tau\vert^{2}=\omega_{fi}^{2}+1/\tau^{2}$,

$$
P_{i\to f}=\frac{\vert V_{fi}\vert^{2}}{\hbar^{2}}\,
\left\vert\frac{1}{\mathrm{i}\omega_{fi}+1/\tau}\right\vert^{2}
=\frac{\vert V_{fi}\vert^{2}}{\hbar^{2}\bigl(\omega_{fi}^{2}+1/\tau^{2}\bigr)}.
$$

**Step 4 — convert to energy.** Multiply numerator and denominator by
$\hbar^{2}$ and use $\hbar\omega_{fi}=E_f-E_i$:

$$
\boxed{\;
P_{i\to f}=\frac{\vert V_{fi}\vert^{2}}{(E_f-E_i)^{2}+(\hbar/\tau)^{2}}\;}
$$

which is $P_{i\to f}=\frac{|V_{fi}|^2}{(E_f-E_i)^2+(\hbar/\tau)^2}$.

**FWHM.** The result is a Lorentzian of the generic form
$\mathcal{L}(x)=C/(x^2+\gamma^2)$, peaked at $x=0$ with maximum $C/\gamma^2$. The
half-maximum is reached where $x^2+\gamma^2=2\gamma^2$, i.e. $x=\pm\gamma$, so
the full width at half maximum is $2\gamma$.

- In terms of $\Delta E=E_f-E_i$: the half-width parameter is $\gamma=\hbar/\tau$,
  so $\mathrm{FWHM}_{\Delta E}=2\hbar/\tau$.
- In terms of the Bohr frequency $\omega_{fi}$: from
  $P\propto1/(\omega_{fi}^2+1/\tau^2)$ the half-width parameter is
  $\gamma=1/\tau$, so $\mathrm{FWHM}_{\omega_{fi}}=2/\tau$.

The two are consistent: $\mathrm{FWHM}_{\Delta E}=\hbar\,\mathrm{FWHM}_{\omega_{fi}}$.

**Lineshape sketch.** As a function of $\Delta E$, the curve is a symmetric bell
centred at $\Delta E=0$, with peak value $\vert V_{fi}\vert^{2}\tau^{2}/\hbar^{2}$
and characteristic width $2\hbar/\tau$; it falls off as $1/(\Delta E)^2$ in the
tails.

```
 P
 |          .-.            peak height = |V_fi|^2 tau^2 / hbar^2
 |         /   \
 |        /     \          FWHM = 2 hbar / tau
 |   ____/       \____
 +----------+----------- Delta E
            0
```

A faster ramp (smaller $\tau$) gives a broader, lower resonance; a slower ramp
(larger $\tau$) gives a narrower, taller one. The width $\hbar/\tau$ is the
finite-time energy resolution: the ramp lasting a time $\sim\tau$ cannot resolve
energy mismatches smaller than $\hbar/\tau$.

<!-- ─── -->

**6. Adiabatic to static perturbation.** Take the $\tau\to\infty$ limit of $P_{i\to f}=\frac{|V_{fi}|^2}{(E_f-E_i)^2+(\hbar/\tau)^2}$ for **fixed** $\Delta E\neq 0$, and compare with $\vert\langle f\vert i(V)\rangle\vert^{2}$ from non-degenerate perturbation theory ([5.1.2](../ch5_perturbation-theory/5-1-2-non-degenerate-perturbation-theory)). Explain physically why the two answers must agree.

**Solution.**

**The limit.** Start from $P_{i\to f}=\frac{|V_{fi}|^2}{(E_f-E_i)^2+(\hbar/\tau)^2}$,

$$
P_{i\to f}=\frac{\vert V_{fi}\vert^{2}}{(E_f-E_i)^{2}+(\hbar/\tau)^{2}}.
$$

Hold $\Delta E=E_f-E_i\neq0$ fixed and let $\tau\to\infty$. Then $\hbar/\tau\to0$,
the regulator term drops out of the denominator, and

$$
\lim_{\tau\to\infty}P_{i\to f}
=\frac{\vert V_{fi}\vert^{2}}{(E_f-E_i)^{2}}
\qquad(\Delta E\neq0).
$$

**Comparison with time-independent perturbation theory.** In non-degenerate
perturbation theory ([5.1.2](../ch5_perturbation-theory/5-1-2-non-degenerate-perturbation-theory)), the
exact eigenstate of $\hat{H}_0+\hat{V}$ that grows continuously out of the
unperturbed eigenstate $\vert i\rangle$ is, to first order in $\hat{V}$,

$$
\vert i(V)\rangle=\vert i\rangle+\sum_{m\neq i}\vert m\rangle\,\frac{V_{mi}}{E_i-E_m}+\cdots.
$$

Overlap with a different unperturbed eigenstate $\vert f\rangle$ ($f\neq i$)
picks out the single $m=f$ term:

$$
\langle f\vert i(V)\rangle=\frac{V_{fi}}{E_i-E_f}+\cdots
\qquad\Longrightarrow\qquad
\vert\langle f\vert i(V)\rangle\vert^{2}=\frac{\vert V_{fi}\vert^{2}}{(E_i-E_f)^{2}}.
$$

Since $(E_i-E_f)^2=(E_f-E_i)^2$, this is **identical** to the $\tau\to\infty$
limit above. Time-dependent perturbation theory, run with an infinitely slow
ramp, reproduces time-independent perturbation theory exactly.

**Why they must agree.** This is the **adiabatic theorem** at work. Switching
$\hat{V}$ on infinitely slowly means the Hamiltonian changes much more slowly
than any internal timescale $\hbar/\vert\Delta E\vert$ of the system. Under such
slow change, a system that starts in an instantaneous eigenstate stays in the
corresponding instantaneous eigenstate: the unperturbed eigenstate $\vert i\rangle$
deforms continuously, with no real (energy-non-conserving) transitions, into the
exact perturbed eigenstate $\vert i(V)\rangle$. The state at $t=0$ is therefore
just $\vert i(V)\rangle$, and the "transition probability" to $\vert f\rangle$ is
nothing but the **squared admixture coefficient** of $\vert f\rangle$ inside that
perturbed eigenstate — which is exactly what first-order time-independent
perturbation theory computes. The dynamical (golden-rule) language and the
static (energy-denominator) language are two descriptions of the same physics;
the slow-ramp limit is the bridge that forces them to coincide. The finite-$\tau$
Lorentzian width $\hbar/\tau$ also shows that the apparent divergence of the
energy denominator at $\Delta E=0$ is not physical: any real, finite ramp
smooths the resonance into a peak of finite height.

<!-- ─── -->

**7. Three-level Raman (long-time limit).** Continue the setup from HW 5.2.2.8: $\hat{H}_0=\Delta\vert 3\rangle\langle 3\vert$ with $E_1=E_2=0$, $E_3=\Delta>0$, and $\hat{V}(t)=\lambda(t)[(\vert 1\rangle+\vert 2\rangle)\langle 3\vert+\mathrm{h.c.}]$ with $\lambda(t)=\lambda_0\cos(\omega t)$.

(a) Starting from the second-order amplitude $\langle 2\vert\hat{G}(t,0)\vert 1\rangle$ obtained in HW 5.2.2.8, evaluate the double time integral in the long-time limit $\omega^{-1},\Delta^{-1}\ll t\ll\lambda_0^{-1}$. Identify which of the four oscillating terms contribute (those whose total exponent vanishes) and show

$$
\langle 2\vert\hat{G}(t,0)\vert 1\rangle\approx\frac{\mathrm{i}\,\lambda_0^{2}\,t}{2}\,\frac{\Delta}{\Delta^{2}-\omega^{2}}.
$$

(b) Compute $P_{1\to 2}(t)=\vert\langle 2\vert\hat{G}(t,0)\vert 1\rangle\vert^{2}$ and identify the time scaling and the frequency dependence on $\omega/\Delta$.

(c) Explain physically why the result is **resonantly enhanced** near $\omega/\Delta=1$ and why the time scaling is $t^{2}$ rather than $t$ (compare to Fermi's golden rule).

(d) **Near-resonance limit and the rotating wave approximation.** Set $\omega \approx \Delta$ (close to but not exactly at single-photon resonance) and re-evaluate the second-order amplitude under the **rotating wave approximation (RWA)**: of the four $(\Omega_1, \Omega_2)$ combinations identified in (a), keep only the one for which *both* exponents are slow in the limit $\omega \to \Delta$, and drop the other three as fast-oscillating. Show that the RWA amplitude is

$$
\langle 2\vert\hat G(t,0)\vert 1\rangle \approx \frac{\mathrm{i}\,\lambda_0^{2}\,t}{4(\Delta - \omega)},
$$

and verify that this agrees with the full off-resonant result of (a) in the near-resonant limit $\vert\Delta - \omega\vert \ll \Delta + \omega$.

**Solution.**

*Convention.* The level-3 energy $E_3=\Delta$ enters the Bohr phase as
$\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)/\hbar}$. The target amplitude quoted in
the problem statement compares $\Delta$ directly with the drive frequency
$\omega$, so — consistently with HW 5.2.2.8 and the reference treatment — we
adopt units with $\hbar=1$; equivalently $\Delta$ denotes the level-3 angular
frequency and the Bohr frequency of the virtual transition is $\omega_{31}=\Delta$.
With this convention the Dyson factor at order $k$ is $(-\mathrm{i})^k$.

**(a) Setting up the double integral.** From HW 5.2.2.8 the first non-vanishing
contribution to $\langle 2\vert\hat{G}(t,0)\vert 1\rangle$ is second order,
because $\langle 2\vert\hat{G}_0\vert 1\rangle=0$ and $\langle 2\vert\hat{V}\vert 1\rangle=0$;
the only path is $\vert 1\rangle\to\vert 3\rangle\to\vert 2\rangle$ through the
virtual intermediate state $\vert 3\rangle$. With matrix elements
$\langle 3\vert\hat{V}(t_1)\vert 1\rangle=\lambda(t_1)$,
$\langle 2\vert\hat{V}(t_2)\vert 3\rangle=\lambda(t_2)$, and the level-3
propagator $\langle 3\vert\hat{G}_0(t_2,t_1)\vert 3\rangle=\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}$,

$$
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
\approx-\lambda_0^{2}\int_{0}^{t}\mathrm{d}t_2\int_{0}^{t_2}\mathrm{d}t_1\,
\cos(\omega t_2)\cos(\omega t_1)\,\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}.
$$

**Expanding the cosines.** Write
$\cos(\omega t)=\tfrac12(\mathrm{e}^{\mathrm{i}\omega t}+\mathrm{e}^{-\mathrm{i}\omega t})$.
The product of the two cosines with the Bohr phase
$\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}=\mathrm{e}^{\mathrm{i}\Delta t_1}\mathrm{e}^{-\mathrm{i}\Delta t_2}$
splits into four terms, each of the form
$\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{\mathrm{i}\Omega_2 t_2}$ with

$$
\Omega_1=\Delta\pm\omega,\qquad\Omega_2=-\Delta\pm\omega .
$$

Thus

$$
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
\approx-\frac{\lambda_0^{2}}{4}\sum_{\text{4 terms}}
\int_{0}^{t}\mathrm{d}t_2\int_{0}^{t_2}\mathrm{d}t_1\,
\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{\mathrm{i}\Omega_2 t_2}.
$$

**The generic nested integral.** Doing the inner integral first,

$$
\int_{0}^{t}\mathrm{d}t_2\int_{0}^{t_2}\mathrm{d}t_1\,\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{\mathrm{i}\Omega_2 t_2}
=\int_{0}^{t}\mathrm{d}t_2\,\frac{\mathrm{e}^{\mathrm{i}\Omega_1 t_2}-1}{\mathrm{i}\Omega_1}\,\mathrm{e}^{\mathrm{i}\Omega_2 t_2}
=\frac{1}{\mathrm{i}\Omega_1}\int_{0}^{t}\mathrm{d}t_2\Bigl(\mathrm{e}^{\mathrm{i}(\Omega_1+\Omega_2)t_2}-\mathrm{e}^{\mathrm{i}\Omega_2 t_2}\Bigr).
$$

**Identifying the long-time-dominant terms — the secular discriminant.**
Define the nested integral

$$
I(\Omega_1,\Omega_2)=\int_0^t\!\mathrm{d}t_2\int_0^{t_2}\!\mathrm{d}t_1\,\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{\mathrm{i}\Omega_2 t_2}.
$$

It grows **linearly in $t$** iff at least one of $\Omega_1$, $\Omega_2$, or
$\Omega_1+\Omega_2$ vanishes; otherwise every contribution is a bounded
oscillation. (Quick check: at $\Omega_1=0$ the inner integral becomes $t_2$ and
the outer one delivers a $t/(\mathrm{i}\Omega_2)$ piece; at $\Omega_2=0$ a
$-t/(\mathrm{i}\Omega_1)$ piece; at $\Omega_1+\Omega_2=0$ a $t/(\mathrm{i}\Omega_1)$
piece. Away from these three branches, every $\mathrm{e}^{\mathrm{i}\Omega t}-1$
factor stays bounded.) In the window
$\omega^{-1},\Delta^{-1}\ll t\ll\lambda_0^{-1}$ only the linear-in-$t$ pieces
survive.

With $\Omega_1=\Delta\pm\omega$ and $\Omega_2=-\Delta\pm\omega$:

- $\Omega_1=0$ or $\Omega_2=0$ both require $\omega=\Delta$ — **single-photon
  resonance** with the intermediate state $\vert 3\rangle$, where the energy
  denominator collapses and perturbation theory itself breaks down. We exclude
  this point and treat $\omega\neq\Delta$.
- $\Omega_1+\Omega_2=\pm\omega\pm\omega$ vanishes for the two **mixed-sign**
  combinations (one $+\omega$, one $-\omega$); the two same-sign combinations
  give $\pm 2\omega\neq 0$ and contribute only bounded oscillations. The
  mixed-sign condition is the **two-photon Raman** resonance — absorption of
  one drive quantum followed by emission of one, with zero net frequency change
  matching the degeneracy $E_2=E_1$. For a resonant term, $\Omega_2=-\Omega_1$ and

$$
\int_{0}^{t}\mathrm{d}t_2\int_{0}^{t_2}\mathrm{d}t_1\,
\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{-\mathrm{i}\Omega_1 t_2}
=\frac{1}{\mathrm{i}\Omega_1}\int_{0}^{t}\mathrm{d}t_2\Bigl(1-\mathrm{e}^{-\mathrm{i}\Omega_1 t_2}\Bigr)
=\frac{t}{\mathrm{i}\Omega_1}-\frac{\mathrm{e}^{-\mathrm{i}\Omega_1 t}-1}{\Omega_1^{2}}
\;\xrightarrow{\;t\to\infty\;}\;\frac{t}{\mathrm{i}\Omega_1}.
$$

**The two contributing terms.** They are:

- $t_1$ carries $+\omega$, $t_2$ carries $-\omega$: $\Omega_1=\Delta+\omega$.
- $t_1$ carries $-\omega$, $t_2$ carries $+\omega$: $\Omega_1=\Delta-\omega$.

Each contributes $t/(\mathrm{i}\Omega_1)$, so

$$
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
\approx-\frac{\lambda_0^{2}}{4}\left(\frac{t}{\mathrm{i}(\Delta+\omega)}+\frac{t}{\mathrm{i}(\Delta-\omega)}\right).
$$

Combine the two fractions over the common denominator $\Delta^2-\omega^2$:

$$
\frac{1}{\Delta+\omega}+\frac{1}{\Delta-\omega}
=\frac{(\Delta-\omega)+(\Delta+\omega)}{\Delta^{2}-\omega^{2}}
=\frac{2\Delta}{\Delta^{2}-\omega^{2}}.
$$

Therefore

$$
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
\approx-\frac{\lambda_0^{2}}{4}\cdot\frac{t}{\mathrm{i}}\cdot\frac{2\Delta}{\Delta^{2}-\omega^{2}}
=-\frac{\lambda_0^{2}t}{2\mathrm{i}}\cdot\frac{\Delta}{\Delta^{2}-\omega^{2}}.
$$

Using $1/\mathrm{i}=-\mathrm{i}$, so $-1/(2\mathrm{i})=\mathrm{i}/2$:

$$
\boxed{\;
\langle 2\vert\hat{G}(t,0)\vert 1\rangle\approx\frac{\mathrm{i}\,\lambda_0^{2}\,t}{2}\,\frac{\Delta}{\Delta^{2}-\omega^{2}}.\;}
$$

**(b) Transition probability.** Take the squared modulus. The amplitude is
$\mathrm{i}$ times a real quantity, so

$$
P_{1\to 2}(t)=\bigl\vert\langle 2\vert\hat{G}(t,0)\vert 1\rangle\bigr\vert^{2}
=\left(\frac{\lambda_0^{2}t}{2}\right)^{2}\left(\frac{\Delta}{\Delta^{2}-\omega^{2}}\right)^{2}
=\frac{\lambda_0^{4}\,t^{2}}{4}\,\frac{\Delta^{2}}{(\Delta^{2}-\omega^{2})^{2}}.
$$

It is convenient to factor out $\Delta$ and display the dependence on the ratio
$\omega/\Delta$:

$$
P_{1\to 2}(t)=\frac{\lambda_0^{4}\,t^{2}}{4\,\Delta^{2}}\,
\frac{1}{\bigl(1-(\omega/\Delta)^{2}\bigr)^{2}}.
$$

- **Time scaling:** $P_{1\to 2}\propto t^{2}$ — coherent quadratic growth.
- **Frequency dependence:** $P_{1\to 2}\propto\bigl(1-(\omega/\Delta)^2\bigr)^{-2}$
  — it diverges as $\omega/\Delta\to1$ and is strongly suppressed for
  $\omega/\Delta\gg1$ or $\omega/\Delta\ll1$.

**(c) Physical interpretation.**

*Resonant enhancement near $\omega/\Delta=1$.* The transition
$\vert 1\rangle\to\vert 2\rangle$ proceeds through the virtual intermediate
state $\vert 3\rangle$ at energy $\Delta$. The drive supplies quanta of energy
$\omega$. When $\omega\approx\Delta$ a single drive quantum nearly matches the
energy gap to $\vert 3\rangle$: the intermediate state is nearly on-shell, the
energy denominator $\Delta\pm\omega$ for the near-resonant pathway becomes
small, and the second-order amplitude is strongly enhanced. This is exactly the
small-energy-denominator amplification familiar from time-independent
perturbation theory, now for a two-step (Raman) process — $\vert 1\rangle$
absorbs a quantum to reach $\vert 3\rangle$, then emits one to settle into
$\vert 2\rangle$. Away from resonance the virtual excursion through $\vert 3\rangle$
is energetically costly and the process is suppressed.

*Why $t^{2}$, not $t$.* Fermi's golden rule produces a linear-in-$t$ probability
(a constant rate) because it describes an **irreversible** decay into a
**continuum** of final states: the sinc-squared kernel, summed over a continuum,
yields a delta function and a steady rate. Here, by contrast, $\vert 2\rangle$
is a **single discrete level**, degenerate with the initial state
$\vert 1\rangle$ ($E_1=E_2=0$). There is no continuum, hence no density of states
to integrate over and no $\delta$-function to generate a rate. The amplitude
itself grows linearly in $t$ — it is the *coherent* accumulation of a fixed
two-photon amplitude — so the probability, its square, grows as $t^{2}$. This is
the same quadratic growth seen for a single resonant final state in HW 2(a)
before any continuum sum. The $t^2$ law signals **coherent Rabi-like
oscillation** (valid only for $t\ll\lambda_0^{-1}$, before the linearised
amplitude saturates), whereas the linear $t$ law of the golden rule signals
**incoherent decay**.

**(d) Near-resonance limit and the RWA.** Inspect the four $(\Omega_1, \Omega_2)$
combinations with $\Omega_1 = \Delta \pm \omega$ and $\Omega_2 = -\Delta \pm \omega$
near $\omega \approx \Delta$:

- $(\Delta + \omega, -\Delta + \omega)$: $\Omega_1 \approx 2\Delta$ fast, $\Omega_2 \approx 0$ slow, sum $\approx 2\omega$ fast.
- $(\Delta + \omega, -\Delta - \omega)$: both exponents fast ($\sim\pm 2\Delta$); a mixed-sign sum-frequency contribution irrelevant near resonance.
- $(\Delta - \omega, -\Delta + \omega)$: both exponents slow ($\approx \pm 0$), sum exactly zero.
- $(\Delta - \omega, -\Delta - \omega)$: $\Omega_1 \approx 0$ slow, $\Omega_2 \approx -2\Delta$ fast.

The RWA discards any term whose exponent oscillates on the fast scale
$1/(2\Delta)$ during the time window $t \gg \Delta^{-1}$ of interest — these
contributions average to zero and give only bounded $\mathcal{O}(1/\Delta)$
pieces. Of the four, only the third combination — with both exponents
$\sim(\Delta - \omega)t$ — survives. Following the generic nested-integral
identity of (a) with $\Omega_2 = -\Omega_1$ and $\Omega_1 = \Delta - \omega$,

$$
\int_{0}^{t}\!\mathrm{d}t_2\!\int_{0}^{t_2}\!\mathrm{d}t_1\,
\mathrm{e}^{\mathrm{i}(\Delta - \omega)t_1}\,\mathrm{e}^{\mathrm{i}(\omega - \Delta)t_2}
\;\approx\; \frac{t}{\mathrm{i}(\Delta - \omega)}
$$

in the regime $\vert\Delta - \omega\vert^{-1} \ll t$. Multiplying by the
$-\lambda_0^{2}/4$ prefactor of the Dyson expansion,

$$
\langle 2\vert\hat G(t,0)\vert 1\rangle
\approx -\frac{\lambda_0^{2}}{4}\cdot\frac{t}{\mathrm{i}(\Delta - \omega)}
= \frac{\mathrm{i}\,\lambda_0^{2}\,t}{4(\Delta - \omega)}.
$$

**Consistency with (a).** The full off-resonant amplitude derived in (a) is
$\langle 2\vert\hat G(t,0)\vert 1\rangle \approx \mathrm{i}\lambda_0^{2}\,t\,\Delta/[2(\Delta^{2} - \omega^{2})]$.
In the near-resonant limit $\vert\Delta - \omega\vert \ll \Delta + \omega$,

$$
\frac{\Delta}{\Delta^{2} - \omega^{2}}
= \frac{\Delta}{(\Delta - \omega)(\Delta + \omega)}
\approx \frac{\Delta}{2\Delta\,(\Delta - \omega)}
= \frac{1}{2(\Delta - \omega)},
$$

so the off-resonant formula reduces to
$\mathrm{i}\lambda_0^{2}\,t/[4(\Delta - \omega)]$, matching the RWA result exactly.

**Physical content of the RWA.** The surviving combination is the
*near-resonant Raman pathway* — a drive quantum of frequency $\omega \approx \Delta$
absorbed at the $\vert 1\rangle \to \vert 3\rangle$ leg, then re-emitted at the
$\vert 3\rangle \to \vert 2\rangle$ leg also near resonance. The discarded
counter-rotating partners — absorption-absorption and emission-emission, both
carrying $\mathrm{e}^{\pm\mathrm{i}(\Delta + \omega)t}$ — are non-zero, but their
contributions to the amplitude oscillate too rapidly to accumulate over the
relevant time scale. RWA is the natural and most commonly used approximation in
coherent-control settings (cavity QED, two-level atoms driven by near-resonant
lasers, NV centres), precisely because near-resonant drive is the regime of
interest in such systems. Away from resonance ($\omega/\Delta$ not close to $1$),
RWA must be abandoned and the full off-resonant calculation of (a) used
instead — they agree in the overlap regime but differ as $\omega/\Delta$ departs
from unity.

<!-- ─── -->

**8. Minimal Kubo exercise.** Take a two-level toy with $\hat{H}_0=-\frac{1}{2}\hbar\omega_0\hat{Z}$, occupied $\vert 0\rangle$, empty $\vert 1\rangle$, and current operators $\hat{j}_x=\hat{X}$, $\hat{j}_y=\hat{Y}$ (without charge or geometric prefactors).

(a) Compute the four matrix elements entering the Kubo numerator.

(b) Evaluate

$$
\sigma_{xy}=\mathrm{i}\hbar\,
\frac{\langle 0\vert\hat{j}_x\vert 1\rangle\langle 1\vert\hat{j}_y\vert 0\rangle-\langle 0\vert\hat{j}_y\vert 1\rangle\langle 1\vert\hat{j}_x\vert 0\rangle}{(E_1-E_0)^{2}}.
$$

(c) Replace $\hat{j}_y\to\hat{X}$ and show that $\sigma_{xy}$ vanishes — i.e. why a Hall response requires **non-commuting** current operators.

**Solution.**

**Energies.** With $\hat{H}_0=-\frac12\hbar\omega_0\hat{Z}$ and the standard
convention $\hat{Z}\vert 0\rangle=+\vert 0\rangle$, $\hat{Z}\vert 1\rangle=-\vert 1\rangle$:

$$
E_0=-\tfrac12\hbar\omega_0(+1)=-\tfrac12\hbar\omega_0,\qquad
E_1=-\tfrac12\hbar\omega_0(-1)=+\tfrac12\hbar\omega_0,
$$

so the gap is $E_1-E_0=\hbar\omega_0$ and $(E_1-E_0)^{2}=\hbar^{2}\omega_0^{2}$.
The state $\vert 0\rangle$ is the lower-energy (occupied) state and $\vert 1\rangle$
the empty one, as stated.

**(a) The four matrix elements.** Use the action of the Pauli operators,
$\hat{X}\vert 0\rangle=\vert 1\rangle$, $\hat{X}\vert 1\rangle=\vert 0\rangle$,
$\hat{Y}\vert 0\rangle=\mathrm{i}\vert 1\rangle$,
$\hat{Y}\vert 1\rangle=-\mathrm{i}\vert 0\rangle$, together with
orthonormality $\langle 0\vert 0\rangle=\langle 1\vert 1\rangle=1$,
$\langle 0\vert 1\rangle=0$:

$$
\begin{split}
\langle 0\vert\hat{j}_x\vert 1\rangle&=\langle 0\vert\hat{X}\vert 1\rangle=\langle 0\vert 0\rangle=1,\\
\langle 1\vert\hat{j}_x\vert 0\rangle&=\langle 1\vert\hat{X}\vert 0\rangle=\langle 1\vert 1\rangle=1,\\
\langle 0\vert\hat{j}_y\vert 1\rangle&=\langle 0\vert\hat{Y}\vert 1\rangle=\langle 0\vert(-\mathrm{i}\vert 0\rangle)=-\mathrm{i},\\
\langle 1\vert\hat{j}_y\vert 0\rangle&=\langle 1\vert\hat{Y}\vert 0\rangle=\langle 1\vert(\mathrm{i}\vert 1\rangle)=+\mathrm{i}.
\end{split}
$$

(As a check, $\langle 1\vert\hat{j}_y\vert 0\rangle=\langle 0\vert\hat{j}_y\vert 1\rangle^{*}$,
consistent with $\hat{Y}$ being Hermitian.)

**(b) The Hall conductivity.** Assemble the numerator of the Kubo formula:

$$
\langle 0\vert\hat{j}_x\vert 1\rangle\langle 1\vert\hat{j}_y\vert 0\rangle
-\langle 0\vert\hat{j}_y\vert 1\rangle\langle 1\vert\hat{j}_x\vert 0\rangle
=(1)(+\mathrm{i})-(-\mathrm{i})(1)=\mathrm{i}+\mathrm{i}=2\mathrm{i}.
$$

Divide by $(E_1-E_0)^{2}=\hbar^{2}\omega_0^{2}$ and multiply by $\mathrm{i}\hbar$:

$$
\sigma_{xy}=\mathrm{i}\hbar\,\frac{2\mathrm{i}}{\hbar^{2}\omega_0^{2}}
=\frac{2\mathrm{i}^{2}\hbar}{\hbar^{2}\omega_0^{2}}
=\boxed{\;-\frac{2}{\hbar\,\omega_0^{2}}\;}
$$

The result is real (as a physical conductivity must be) and non-zero. The toy
exhibits a finite Hall response: the antisymmetric current–current correlation
$\langle\hat{j}_x\hat{j}_y\rangle-\langle\hat{j}_y\hat{j}_x\rangle$ is non-zero,
fed by the virtual transition $\vert 0\rangle\to\vert 1\rangle\to\vert 0\rangle$.

**(c) Why non-commuting currents are required.** Now set $\hat{j}_y\to\hat{X}$,
so both current operators are the *same* operator, $\hat{j}_x=\hat{j}_y=\hat{X}$.
The numerator becomes

$$
\langle 0\vert\hat{X}\vert 1\rangle\langle 1\vert\hat{X}\vert 0\rangle
-\langle 0\vert\hat{X}\vert 1\rangle\langle 1\vert\hat{X}\vert 0\rangle=0,
$$

identically — the two products are term-by-term equal, so their difference
vanishes. Hence $\sigma_{xy}=0$.

The structural reason: the Kubo numerator is **antisymmetric** under exchange
$\hat{j}_x\leftrightarrow\hat{j}_y$. Any antisymmetric bilinear of two identical
(or, more generally, commuting and simultaneously diagonalisable) operators
vanishes. A non-zero Hall conductivity therefore requires the two current
operators to be genuinely **distinct and non-commuting**. In the working
example $[\hat{j}_x,\hat{j}_y]=[\hat{X},\hat{Y}]=2\mathrm{i}\hat{Z}\neq0$, and it
is exactly this commutator — a measure of the failure of $\hat{j}_x$ and
$\hat{j}_y$ to share eigenstates — that supplies the imaginary, antisymmetric
correlation responsible for the transverse response. Physically, a Hall current
flows *perpendicular* to the applied field; that transverse, chirality-carrying
response cannot be built from a single current direction, and the
non-commutativity of $\hat{j}_x$ and $\hat{j}_y$ is the operator-level
expression of the broken $x\leftrightarrow y$ symmetry (time-reversal /
chirality) that the Hall effect needs.
