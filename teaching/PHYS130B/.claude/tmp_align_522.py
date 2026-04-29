#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path("/Users/home/Documents/GitHub/everettyou.github.io/teaching/PHYS130B")
path = ROOT / "notes_src/ch5_perturbation-theory/5-2-2-fermis-golden-rule.ipynb"


def text_to_source(text: str) -> list:
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            out.append(line + "\n")
        elif line:
            out.append(line)
    return out


PROMPTS = r""":::{admonition} Prompts
:class: tip

- Starting from Eq.~{eq}`eq-5-2-1-bridge-prob`, what does the phase $\mathrm{e}^{\mathrm{i}\omega_{fi}t'}$ encode, and why does time integration turn into a resonance condition?
- For $\hat{V}(t)=\hat{V}\mathrm{e}^{-\mathrm{i}\omega t}$ switched on at $t=0$, trace the integral $\int_0^t\mathrm{e}^{\mathrm{i}(\omega_{fi}-\omega)t'}\mathrm{d}t'$ to the sinc-squared probability; what is the $\omega=0$ limit?
- Why does a **continuum** of final energies turn the same sinc peak into a **constant rate** $\Gamma$ with a factor $\rho(E_f)$?
- When can one speak of a rate $\Gamma$ even though $P(t)$ grows without bound in perturbation theory at strict $t\to\infty$?
- (Optional) For an exponential ramp $\mathrm{e}^{t/\tau}$, why does a Lorentzian in $\Delta E$ connect slow switching to the $1/(E_i-E_f)^2$ language of [5.1.2](5-1-2-non-degenerate-perturbation-theory)?
:::
"""

CELL2 = r"""## Lecture Notes

### Overview

**One thread through 5.2.1 and 5.2.2.** Section~5.2.1 built the interaction picture and showed how $\hat{V}_{\mathcal{I}}(t)$ acquires Bohr phases $\mathrm{e}^{\mathrm{i}\omega_{mn}t}$ (Eq.~{eq}`eq-5-2-1-VI-matrix`). Section~5.2.2 asks the **same** question in probability language: *starting from $\vert i\rangle$, how much weight appears in $\vert f\rangle$ after time $t$, to first order in the disturbance?*  The entire answer is the **single** time integral in Eq.~{eq}`eq-5-2-1-bridge-prob`; what follows is only how different time dependences of $\hat{V}(t)$ shape that integral.

**Notation (fixed for all of Sec.~5.2).** Initial time $t_0=0$. Bare energies $\hat{H}_0\vert n\rangle=E_n\vert n\rangle$. Couplings $V_{mn}(t)=\langle m\vert\hat{V}(t)\vert n\rangle$ in the Schrödinger picture. Bohr frequencies $\omega_{mn}=(E_m-E_n)/\hbar$. We write $V_{fi}(t)=\langle f\vert\hat{V}(t)\vert i\rangle$ and $\omega_{fi}=(E_f-E_i)/\hbar$.

:::{admonition} Starting point (from Sec.~5.2.1)
:class: important

To first order, the transition probability is (same equation as Eq.~{eq}`eq-5-2-1-bridge-prob`)

$$
P_{i\to f}^{(1)}(t)=\frac{1}{\hbar^2}\left\vert\int_0^t\mathrm{d}t'\,
V_{fi}(t')\,\mathrm{e}^{\mathrm{i}\omega_{fi}t'}\right\vert^2.
$$

Sec.~5.2.1 also relates $\vert\langle f\vert\hat{U}(t)\vert i\rangle\vert$ to this integral when $f\neq i$.
:::

### Harmonic drive: sinc-squared resonance

Take a monochromatic perturbation switched on at $t=0$,

$$
\hat{V}(t)=\begin{cases}
\hat{V}\,\mathrm{e}^{-\mathrm{i}\omega t}, & t>0,\\[4pt]
0, & t\le 0,
\end{cases}
$$

so $V_{fi}(t')=V_{fi}\,\mathrm{e}^{-\mathrm{i}\omega t'}$ with $V_{fi}\equiv\langle f\vert\hat{V}\vert i\rangle$ time-independent. Then

$$
\int_0^t\mathrm{d}t'\,\mathrm{e}^{\mathrm{i}(\omega_{fi}-\omega)t'}
=\frac{\mathrm{e}^{\mathrm{i}(\omega_{fi}-\omega)t}-1}{\mathrm{i}(\omega_{fi}-\omega)},
$$

and

$$
P_{i\to f}^{(1)}(t)=\frac{\vert V_{fi}\vert^2}{\hbar^2}\left[\frac{\sin\bigl((\omega_{fi}-\omega)t/2\bigr)}{(\omega_{fi}-\omega)/2}\right]^2.
$$ (eq-5b-sinc-driven)

:::{admonition} Derivation: exponential $\to$ sinc-squared
:class: dropdown information

Let $x=(\omega_{fi}-\omega)/2$. Then $\bigl(\mathrm{e}^{\mathrm{i}2xt}-1\bigr)/(2\mathrm{i}x)=\mathrm{e}^{\mathrm{i}xt}\sin(xt)/x$, so the squared modulus is $\sin^2(xt)/x^2$.
:::

:::{admonition} Finite-time resolution
:class: attention

Near resonance, $P\sim \vert V_{fi}\vert^2 t^2/\hbar^2$ (quadratic short-time growth). Far off resonance, the kernel is suppressed $\propto (\omega_{fi}-\omega)^{-2}$ after local averaging. The main lobe width $\Delta\omega\sim 2\pi/t$ is the **finite-time** energy resolution — strict $\delta$-function conservation only emerges in a long-time limit.
:::

**Static perturbation** ($\omega=0$): replace $\omega_{fi}-\omega\to\omega_{fi}$,

$$
P_{i\to f}^{(1)}(t)=\frac{\vert V_{fi}\vert^2}{\hbar^2}\,\frac{\sin^2(\omega_{fi}t/2)}{(\omega_{fi}/2)^2}.
$$ (eq-5b-P-sinc-formula)

### Long-time limit and Fermi's golden rule

For one isolated final level, $P_{i\to f}^{(1)}(t)$ does **not** stay $\ll 1$ forever; first-order theory must break down when the initial state depletes. The **rate** picture applies when probability **spreads** into many unresolved final channels — a **continuum** with density of states $\rho(E)$ (states per energy, fixed convention as in applications).

Use

$$
\lim_{t\to\infty}\frac{1}{t}\left[\frac{\sin(xt/2)}{x/2}\right]^2=2\pi\,\delta(x),
$$

and define the **transition rate** $\Gamma_{i\to f}\equiv\lim_{t\to\infty}P_{i\to f}^{(1)}(t)/t$. Then

$$
\Gamma_{i\to f}
=\frac{2\pi}{\hbar}\,\vert V_{fi}\vert^2\,\delta\!\bigl(E_f-E_i-\hbar\omega\bigr),
$$ (eq-5b-fgr-delta)

and integrating over final energies,

:::{admonition} Fermi's golden rule (continuum)
:class: important

$$
\boxed{\
\Gamma_{i\to f}=\frac{2\pi}{\hbar}\,\vert\langle f\vert\hat{V}\vert i\rangle\vert^2\,\rho(E_f)\Big\vert_{E_f=E_i+\hbar\omega}\
}.
$$ (eq-5b-fgr-standard)

For static $\hat{V}$ ($\omega=0$), evaluate at $E_f=E_i$.
:::

:::{admonition} Derivation: sinc kernel $\to\delta(\omega)$ (distribution sketch)
:class: dropdown information

Let $K_t(\omega)=\sin^2(\omega t/2)/(\omega/2)^2$. For smooth test $g(\omega)$, $\int\mathrm{d}\omega\,K_t(\omega)g(\omega)\to 2\pi t\,g(0)$ as $t\to\infty$, while $\int K_t\,\mathrm{d}\omega/(2\pi t)\to 1$ under the peak. Hence $K_t/t\to 2\pi\delta(\omega)$.
:::

:::{admonition} When is $\Gamma_{i\to f}=P/t$ still consistent with first order?
:class: caution

For **detuned** transitions, "long time" means $t\gg 1/\vert\omega_{fi}-\omega\vert$, which can still be **short** compared with the depletion time $\sim\hbar/\vert V_{fi}\vert$. Then the rate extracted from $P/t$ is meaningful in perturbation theory. If $P$ is no longer small, use a non-perturbative or open-system description.
:::

### Optional bridge: slow turn-on and Sec.~5.1

If instead the perturbation is ramped from the past as $\hat{V}(t)=\hat{V}\mathrm{e}^{t/\tau}$ for $t<0$ (and $0$ for $t\ge 0$), the same linear amplitude gives a **Lorentzian**

$$
P_{i\to f}\propto \frac{\vert V_{fi}\vert^2}{(E_f-E_i)^2+(\hbar/\tau)^2},
$$

regularizing the $E_f\to E_i$ pole. As $\tau\to\infty$ this matches the **energy-denominator** language of time-independent mixing ([5.1.2](5-1-2-non-degenerate-perturbation-theory)); finite $\tau$ sets an energy width $\sim\hbar/\tau$.

:::{admonition} Selection rules and linewidth (same matrix element)
:class: note

If $\langle f\vert\hat{V}\vert i\rangle=0$ by symmetry, the channel is absent at leading order (dipole rules, parity, etc.). A decay rate $\Gamma$ implies a natural linewidth $\Delta E\sim\hbar\Gamma$ — the same $\vert V\vert^2$ factor that controls dynamics also controls spectral broadening.
:::

:::{admonition} Poll: what suppresses a rate most?
:class: dropdown poll

At resonance, $\Gamma_{i\to f}\propto \vert\langle f\vert\hat{V}\vert i\rangle\vert^2\,\rho(E_f)$. If $\vert\langle f\vert\hat{V}\vert i\rangle\vert$ is very small, which dominates how *slow* the transition is?

(A) $\vert\langle f\vert\hat{V}\vert i\rangle\vert^2$

(B) $\rho(E_f)$ alone, independent of the matrix element

(C) Only the drive frequency $\omega$

(D) Only the initial energy $E_i$
:::

:::{admonition} Discussion: same integral, two regimes
:class: dropdown tip

The **same** Eq.~{eq}`eq-5-2-1-bridge-prob` gives $P\propto t^2$ at very short times and $P\approx\Gamma t$ into a broad continuum at longer times. Where is the crossover for a transition you care about?
:::

### Summary

- **One input:** Eq.~{eq}`eq-5-2-1-bridge-prob` from Sec.~5.2.1.
- **Harmonic drive:** sinc-squared in $\omega_{fi}-\omega$; static case $\omega=0$.
- **Continuum:** $\sin^2$ kernel $\to\delta$ $\Rightarrow$ Fermi's golden rule with $\rho(E_f)$.
- **Optional:** exponential ramp $\leftrightarrow$ Lorentzian $\leftrightarrow$ [5.1.2](5-1-2-non-degenerate-perturbation-theory) denominators.

:::{admonition} See Also
:class: seealso

- [5.2.1 Interaction Picture](5-2-1-interaction-picture): $\hat{U}_{\mathcal{I}}$, $\hat{V}_{\mathcal{I}}$, Bohr phases, bridge to Eq.~{eq}`eq-5-2-1-bridge-prob`
- [5.1.2 Non-Degenerate Perturbation Theory](5-1-2-non-degenerate-perturbation-theory): $1/(E_i-E_m)$ mixing and slow-switching contact
- [5.2.3 Applications](5-2-3-applications): dipole transitions, scattering, response
:::
"""

HOMEWORK = r"""## Homework

**1. Finite-time window.** From Eq.~(eq-5b-sinc-driven), show peak height $\propto t^2$, width $\propto 1/t$, and lobe weight $\propto t$.

**2. Short times.** For $\vert(\omega_{fi}-\omega)t\vert\ll 1$, show $P\approx \vert V_{fi}\vert^2 t^2/\hbar^2$.

**3. Sinc-to-delta.** Prove $\lim_{t\to\infty}t^{-1}[\sin(xt/2)/(x/2)]^2=2\pi\delta(x)$ distributionally.

**4. From δ(E) to Γ.** Use Eq.~(eq-5b-fgr-delta) and $\int\rho(E_f)\mathrm{d}E_f$ to obtain Eq.~(eq-5b-fgr-standard).

**5. DOS in 3D.** Derive $\rho(E)=\dfrac{Vm}{2\pi^2\hbar^3}\sqrt{2mE}$ and state how $\Gamma$ scales with $E$ at fixed $\vert V\vert$.

**6. Dipole rules.** Allowed or forbidden: (a) $2s\to 1s$, (b) $2p,m=0\to 1s,m=0$ ($z$ light), (c) $2p,m=1\to 1s,m=0$ ($\sigma^-$).

**7. Width vs lifetime.** From $\mathrm{e}^{-\Gamma t}$, show linewidth $\sim\hbar\Gamma$.

**8. Which fails first?** (i) weak + continuum, (ii) strong two-level drive, (iii) one final level, (iv) pulse shorter than $2\pi/\vert\omega_{fi}-\omega\vert$.

**9. Ramp width.** For $P\propto \vert V_{fi}\vert^2/(\omega_{fi}^2+1/\tau^2)$, give FWHM in $\omega_{fi}$ and in $\Delta E$, and the $\tau\to\infty$ limit vs [5.1.2](5-1-2-non-degenerate-perturbation-theory).
"""


def main():
    with path.open() as f:
        nb = json.load(f)
    nb["cells"][1]["source"] = text_to_source(PROMPTS)
    nb["cells"][2]["source"] = text_to_source(CELL2)
    nb["cells"][3]["source"] = text_to_source(HOMEWORK)
    with path.open("w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("wrote", path)


if __name__ == "__main__":
    main()
