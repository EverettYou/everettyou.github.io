# 3.3.1 Stationary Phase Approximation
Worked solutions for the homework problems in the [3.3.1 Stationary Phase Approximation](../ch3_path-integral/3-3-1-stationary-phase-approximation) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Gaussian check.** Apply the stationary-phase approximation to the pure Gaussian integral $I = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}\alpha x^{2}/\hbar}\,\mathrm{d}x$ with $\alpha > 0$ real.

(a) Find the stationary point $x_{0}$ where $S'(x_{0}) = 0$ for $S(x) = \alpha x^{2}$.

(b) Evaluate the SPA formula $I \approx A(x_0)\sqrt{2\pi\mathrm{i}\hbar/S''(x_0)}\,\mathrm{e}^{\mathrm{i}S(x_0)/\hbar}$ and compare with the exact Fresnel result $\sqrt{\pi\hbar/(-\mathrm{i}\alpha)} = \sqrt{\pi\hbar/\alpha}\,\mathrm{e}^{\mathrm{i}\pi/4}$. Show that SPA is **exact** here. Why?

**Solution.**

**(a)** With $S(x) = \alpha x^{2}$ the derivative is $S'(x) = 2\alpha x$. Setting $S'(x_{0}) = 2\alpha x_{0} = 0$ and using $\alpha \neq 0$ gives the single stationary point

$$
x_{0} = 0.
$$

**(b)** Here the amplitude is $A(x) = 1$ (constant), $S(x_{0}) = S(0) = 0$, and $S''(x) = 2\alpha$, so $S''(x_{0}) = 2\alpha > 0$. The SPA formula gives

$$
I_{\mathrm{SPA}} = A(x_{0})\,\sqrt{\frac{2\pi\mathrm{i}\hbar}{S''(x_{0})}}\,\mathrm{e}^{\mathrm{i}S(x_{0})/\hbar} = \sqrt{\frac{2\pi\mathrm{i}\hbar}{2\alpha}} = \sqrt{\frac{\pi\mathrm{i}\hbar}{\alpha}}.
$$

To compare with the exact result, note that $1/(-\mathrm{i}) = \mathrm{i}$, so

$$
\sqrt{\frac{\pi\hbar}{-\mathrm{i}\alpha}} = \sqrt{\frac{\pi\hbar}{\alpha}\cdot\frac{1}{-\mathrm{i}}} = \sqrt{\frac{\pi\hbar}{\alpha}\cdot\mathrm{i}} = \sqrt{\frac{\pi\mathrm{i}\hbar}{\alpha}} = I_{\mathrm{SPA}}.
$$

With the principal branch $\sqrt{\mathrm{i}} = \mathrm{e}^{\mathrm{i}\pi/4}$, both equal $\sqrt{\pi\hbar/\alpha}\,\mathrm{e}^{\mathrm{i}\pi/4}$. SPA reproduces the exact integral with **no error**.

*Why exact?* The SPA is built on two approximations: (i) Taylor-expanding the phase to quadratic order, $S(x) \approx S(x_{0}) + \tfrac{1}{2}S''(x_{0})(x-x_{0})^{2}$, and (ii) replacing the amplitude $A(x)$ by its value $A(x_{0})$ at the saddle. Here the phase $S(x) = \alpha x^{2}$ *is* exactly quadratic — its Taylor series terminates at the quadratic term, with no cubic or higher corrections — and the amplitude $A(x) = 1$ is exactly constant. Both "approximations" are therefore exact identities, and the remaining Fresnel integral is evaluated with no further error. SPA is exact precisely when the phase is quadratic and the amplitude constant — the same reason the free-particle path integral (a quadratic action) is solved exactly by SPA (Problem 7).

<!-- ─── -->

**2. Cubic phase.** Consider $I = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}(x^{2} + \epsilon x^{3})/\hbar}\,\mathrm{d}x$ with $\epsilon$ small and positive.

(a) Find all stationary points of $S(x) = x^{2} + \epsilon x^{3}$.

(b) For the stationary point near $x = 0$, apply the SPA formula and write the leading approximation to $I$.

(c) The naive SPA assigns both saddles a contribution of magnitude $\sqrt{\pi\hbar}$. Explain why the far saddle at $x = -2/(3\epsilon)$ is nevertheless **nonperturbative** in $\epsilon$, while the $x \approx 0$ saddle supplies the **perturbative** expansion in powers of $\epsilon$. (This is a question about how $I(\epsilon)$ is organized as a series in $\epsilon$, not about which saddle has a larger prefactor.)

**Solution.**

**(a)** $S'(x) = 2x + 3\epsilon x^{2} = x\,(2 + 3\epsilon x)$. The product vanishes when $x = 0$ or $2 + 3\epsilon x = 0$, giving two stationary points

$$
x_{0} = 0, \qquad x_{1} = -\frac{2}{3\epsilon}.
$$

**(b)** $S''(x) = 2 + 6\epsilon x$. At the saddle near the origin, $S(0) = 0$, $S''(0) = 2$, and $A = 1$:

$$
I \approx \sqrt{\frac{2\pi\mathrm{i}\hbar}{S''(0)}}\,\mathrm{e}^{\mathrm{i}S(0)/\hbar} = \sqrt{\frac{2\pi\mathrm{i}\hbar}{2}} = \sqrt{\pi\mathrm{i}\hbar} = \sqrt{\pi\hbar}\,\mathrm{e}^{\mathrm{i}\pi/4}.
$$

As $\epsilon \to 0$ this reduces continuously to the pure-Gaussian result of Problem 1 with $\alpha = 1$: it is the leading term of the **perturbative** sector in $\epsilon$.

**(c)** At the far saddle $x_{1} = -2/(3\epsilon)$,

$$
S(x_{1}) = x_{1}^{2} + \epsilon x_{1}^{3} = \frac{4}{9\epsilon^{2}} - \frac{8}{27\epsilon^{2}} = \frac{4}{27\epsilon^{2}}, \qquad S''(x_{1}) = 2 + 6\epsilon\left(-\frac{2}{3\epsilon}\right) = 2 - 4 = -2.
$$

Its naive SPA contribution is

$$
I_{1} \approx \sqrt{\frac{2\pi\mathrm{i}\hbar}{-2}}\,\mathrm{e}^{\mathrm{i}\,4/(27\epsilon^{2}\hbar)} = \sqrt{\pi\hbar}\,\mathrm{e}^{-\mathrm{i}\pi/4}\,\mathrm{e}^{\mathrm{i}\,4/(27\epsilon^{2}\hbar)}.
$$

**Comparable SPA magnitudes — not the issue.** $|I_{0}|$ and $|I_{1}|$ are both $\sqrt{\pi\hbar}$ because $|S''|=2$ at each saddle. Part (c) is *not* asking which saddle is smaller or “wins.” Naive saddle sum would add $I \approx I_{0} + I_{1}$ with two terms of the same order of magnitude but wildly different $\epsilon$-dependence.

**Perturbative sector ($x \approx 0$).** Factor the cubic perturbation and expand in $\epsilon$:

$$
I(\epsilon) = \int \mathrm{e}^{\mathrm{i}x^{2}/\hbar}\,\mathrm{e}^{\mathrm{i}\epsilon x^{3}/\hbar}\,\mathrm{d}x = \sum_{n=0}^{\infty}\frac{1}{n!}\left(\frac{\mathrm{i}}{\hbar}\right)^{n}\epsilon^{n}\int_{-\infty}^{\infty}x^{3n}\,\mathrm{e}^{\mathrm{i}x^{2}/\hbar}\,\mathrm{d}x.
$$

Every term is an **integer power of $\epsilon$** times a Fresnel integral localized at the origin (Gaussian weight $\mathrm{e}^{\mathrm{i}x^{2}/\hbar}$). The $n=0$ term is Problem 1; higher $n$ are analytic corrections. This is the standard **perturbation theory in $\epsilon$**: $I(\epsilon) = c_{0} + c_{1}\epsilon + c_{2}\epsilon^{2} + \cdots$, all built from the $x \approx 0$ saddle and its neighborhood (with $c_{0} = \sqrt{\pi\hbar}\,\mathrm{e}^{\mathrm{i}\pi/4}$).

**Nonperturbative sector (far saddle).** The second stationary point sits at $x_{1} = -2/(3\epsilon) \to -\infty$ as $\epsilon \to 0$. Its SPA piece carries phase $S(x_{1})/\hbar = 4/(27\epsilon^{2}\hbar)$: a pole in $\epsilon^{-2}$, not a power of $\epsilon$. So $I_{1} \propto \mathrm{e}^{\mathrm{i}\,4/(27\epsilon^{2}\hbar)}$ is **nonperturbative** — it cannot be generated by any finite order of the Taylor expansion above (it is “beyond all orders” in $\epsilon$). At each fixed small $\epsilon$ it is a legitimate saddle contribution of the same *prefactor* size as $I_{0}$, but it belongs to a different asymptotic *class*: not part of the $\epsilon$-series.

**What this means.** If the question is “expand $I(\epsilon)$ in powers of $\epsilon$,” only the $x \approx 0$ sector answers it; the far saddle is invisible to that expansion. If the question is “evaluate $I$ at a given small $\epsilon$ by summing all saddles,” both $I_{0}$ and $I_{1}$ can matter (with comparable magnitude but wildly oscillating relative phase as $\epsilon \to 0$). The cubic perturbation of the Gaussian is **perturbative** near the origin; the far saddle is an extra, **nonperturbative** stationary-phase channel — not a smaller one.

<!-- ─── -->

**3. Stationary-region width.** The SPA integral receives its dominant contribution from a region of width $\Delta x$ around each stationary point.

(a) Using $\vert S''(x_{0})\vert(x - x_{0})^{2}/(2\hbar)\sim 1$ as the criterion for significant phase variation, show $\Delta x \sim \sqrt{\hbar/\vert S''(x_{0})\vert}$.

(b) For the free-particle classical action $S_\text{cl} = m(\Delta x)^{2}/(2t)$, identify $S'' = m/t$ and estimate $\Delta x$ in position space. How does it scale with $m$ and $t$?

(c) Evaluate this width for an electron ($m \approx 9\times 10^{-31}\,\text{kg}$, $t = 10^{-15}\,\text{s}$) and state whether the result is comparable to atomic scales. Using the $m^{-1/2}$ scaling from part (b), explain why laboratory masses ($m \gg m_e$) have a negligible stationary-region width without repeating a second numerical example here.

**Solution.**

**(a)** Near $x_{0}$ the phase difference is $[S(x) - S(x_{0})]/\hbar \approx \vert S''(x_{0})\vert(x - x_{0})^{2}/(2\hbar)$. Contributions add coherently while this is small and start to cancel once it reaches order unity. Setting the criterion $\vert S''(x_{0})\vert(\Delta x)^{2}/(2\hbar) \sim 1$ and solving,

$$
(\Delta x)^{2} \sim \frac{2\hbar}{\vert S''(x_{0})\vert},
$$

so $\Delta x \sim \sqrt{\hbar/\vert S''(x_{0})\vert}$,

dropping the order-unity factor of $2$. Inside this band the phase is nearly stationary; outside it the integrand oscillates and cancels.

**(b)** Treat the classical action as a function of the endpoint displacement — write the displacement as $x$, so $S_\text{cl}(x) = m x^{2}/(2t)$. Then $S'' = \mathrm{d}^{2}S_\text{cl}/\mathrm{d}x^{2} = m/t$, and the position-space width is

$$
\Delta x \sim \sqrt{\frac{\hbar}{S''}} = \sqrt{\frac{\hbar t}{m}}.
$$

It grows as $\sqrt{t}$ (longer travel times widen the spread of contributing paths) and shrinks as $1/\sqrt{m}$ (heavier particles follow sharper trajectories). This is the same $\sqrt{\hbar t/m}$ scale that controls free-wavepacket spreading.

**(c)** With $m \approx 9\times 10^{-31}\,\text{kg}$ and $t = 10^{-15}\,\text{s}$,

$$
\Delta x \sim \sqrt{\frac{(1.05\times10^{-34})(10^{-15})}{9\times 10^{-31}}} \approx 3.4\times10^{-10}\,\text{m},
$$

about an Ångström — comparable to atomic dimensions, so the electron's quantum positional spread is physically significant at picosecond timescales.

For a laboratory mass $m \sim 10^{-1}\,\text{kg}$ at $t \sim 1\,\text{s}$, the same formula gives $\Delta x \sim 10^{-17}\,\text{m}$ if one plugs in numbers — roughly $10^{7}$ times smaller than a nucleus. It is cleaner to use the scaling: increasing $m$ by a factor $\sim 10^{30}$ at fixed $t$ shrinks $\Delta x$ by $\sqrt{10^{30}} \sim 10^{15}$. Macroscopic objects therefore have stationary regions far below any measurable scale; Problem 8 makes the same point via $S_\text{cl}/\hbar$ rather than $\Delta x$.

<!-- ─── -->

**4. Second variation.** For a particle in a potential $V(x)$, the second variation of the action around the classical path is $\delta^{2}S = \int_{0}^{T}\delta x(t)\,\hat{D}\,\delta x(t)\,\mathrm{d}t$ with $\hat{D} = -m\,\mathrm{d}^{2}/\mathrm{d}t^{2} - V''(x_\mathrm{cl})$.

(a) For the harmonic oscillator $V = \tfrac{1}{2}m\omega^{2}x^{2}$, show that $\hat{D} = -m(\mathrm{d}^{2}/\mathrm{d}t^{2} + \omega^{2})$.

(b) Fluctuations $\delta x(t)$ vanish at the endpoints (paths have fixed boundary conditions), so $\hat{D}\,\delta x = \lambda\,\delta x$ has Dirichlet boundary conditions $\delta x(0) = \delta x(T) = 0$, with eigenfunctions $\sin(n\pi t/T)$ for $n = 1, 2, \ldots$. Find the eigenvalues, identify the values of $T$ at which a zero eigenvalue appears, and explain what goes wrong with the semiclassical propagator at those special times.

**Solution.**

**(a)** For $V(x) = \tfrac{1}{2}m\omega^{2}x^{2}$ the derivatives are $V'(x) = m\omega^{2}x$ and $V''(x) = m\omega^{2}$, a constant. Since $V''$ does not depend on $x$, it is the same on the classical path: $V''(x_\mathrm{cl}) = m\omega^{2}$. Substituting into $\hat{D} = -m\,\mathrm{d}^{2}/\mathrm{d}t^{2} - V''(x_\mathrm{cl})$,

$$
\hat{D} = -m\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}} - m\omega^{2} = -m\left(\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}} + \omega^{2}\right).
$$

**(b)** The trial functions $\delta x_{n}(t) = \sin(n\pi t/T)$ satisfy the Dirichlet conditions $\delta x_{n}(0) = \delta x_{n}(T) = 0$ automatically. Acting with $\hat{D}$, and using $\mathrm{d}^{2}/\mathrm{d}t^{2}\,\sin(n\pi t/T) = -(n\pi/T)^{2}\sin(n\pi t/T)$,

$$
\hat{D}\,\delta x_{n} = -m\left[-\left(\frac{n\pi}{T}\right)^{2} + \omega^{2}\right]\sin\frac{n\pi t}{T} = m\left[\left(\frac{n\pi}{T}\right)^{2} - \omega^{2}\right]\delta x_{n}.
$$

So the eigenfunctions are indeed $\sin(n\pi t/T)$ with eigenvalues

$$
\lambda_{n} = m\left[\left(\frac{n\pi}{T}\right)^{2} - \omega^{2}\right], \qquad n = 1, 2, 3, \ldots
$$

A zero eigenvalue $\lambda_{n} = 0$ occurs when $(n\pi/T)^{2} = \omega^{2}$, i.e. $n\pi/T = \omega$, at the special times

$$
T = \frac{n\pi}{\omega} = n\cdot\frac{T_\text{osc}}{2}, \qquad T_\text{osc} = \frac{2\pi}{\omega},
$$

integer multiples of *half* the oscillator period.

At those times the semiclassical propagator $K \approx \mathrm{e}^{\mathrm{i}S_\mathrm{cl}/\hbar}/\sqrt{\det\hat{D}}$ breaks down. The determinant is the product of eigenvalues, $\det\hat{D} = \prod_{n}\lambda_{n}$; when any $\lambda_{n} = 0$, the determinant vanishes and the prefactor $1/\sqrt{\det\hat{D}}$ **diverges**. Physically, the times $T = n\pi/\omega$ are **focal times** of the harmonic oscillator: every classical trajectory launched from a given point reconverges there regardless of its initial velocity — for the oscillator $x_\mathrm{cl}(t) = x_{0}\cos\omega t + (v_{0}/\omega)\sin\omega t$ returns to $\pm x_{0}$ at $t = n\pi/\omega$ for *every* $v_{0}$. The vanishing eigenvalue is a **zero mode**: a nontrivial fluctuation $\delta x_{n}$ that costs no action ($\delta^{2}S = 0$ along it). The Gaussian integral over that direction is undamped, so the quadratic approximation fails and one must keep higher-order terms in the fluctuation expansion. Handled properly, the propagator stays finite, but the amplitude acquires an extra phase of $-\pi/2$ each time a focal point is crossed.

<!-- ─── -->

**5. Validity breakdown.** Apply the SPA naively to $I = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}x^{4}/\hbar}\,\mathrm{d}x$.

(a) Find the stationary points of $S(x) = x^{4}$ and compute $S''$ at each.

(b) Why does the SPA formula $I \approx A(x_0)\sqrt{2\pi\mathrm{i}\hbar/S''(x_0)}\,\mathrm{e}^{\mathrm{i}S(x_0)/\hbar}$ fail here? Which condition of the standard SPA is violated?

(c) The correct leading behaviour is $I \sim \hbar^{1/4}$, not $\hbar^{1/2}$. Argue on dimensional grounds why a *degenerate* stationary point ($S'' = 0$ but $S^{(4)}\neq 0$) changes the $\hbar$-scaling.

**Solution.**

**(a)** $S(x) = x^{4}$ gives $S'(x) = 4x^{3}$. The only root of $4x_{0}^{3} = 0$ is $x_{0} = 0$ — a single stationary point (a triple root of $S'$). The second derivative is $S''(x) = 12x^{2}$, so

$$
S''(x_{0}) = S''(0) = 0.
$$

**(b)** The SPA formula contains the factor $\sqrt{2\pi\mathrm{i}\hbar/S''(x_{0})}$. With $S''(x_{0}) = 0$ this is $\sqrt{2\pi\mathrm{i}\hbar/0}$ — divergent and meaningless. The stationary point is **degenerate**, and the explicit validity condition $\vert S''(x_{0})\vert \neq 0$ is violated. Equivalently, the SPA derivation assumes the quadratic term dominates the local expansion of the phase, $S \approx S(x_{0}) + \tfrac{1}{2}S''(x - x_{0})^{2}$; here that term is identically zero and the leading nonvanishing term is quartic, $S = \tfrac{1}{24}S^{(4)}(0)\,x^{4} = x^{4}$ (with $S^{(4)}(0) = 24$). The Gaussian (Fresnel) integral that produced the SPA prefactor simply does not apply — the local integral is a *quartic* Fresnel integral, not a quadratic one.

**(c)** Rescale the integration variable to absorb $\hbar$. Set $x = \hbar^{1/4}u$, so that $x^{4}/\hbar = \hbar u^{4}/\hbar = u^{4}$ and $\mathrm{d}x = \hbar^{1/4}\,\mathrm{d}u$. Then

$$
I = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}x^{4}/\hbar}\,\mathrm{d}x = \hbar^{1/4}\int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}u^{4}}\,\mathrm{d}u = \hbar^{1/4}\,C,
$$

where $C = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}u^{4}}\,\mathrm{d}u = \tfrac{1}{2}\Gamma(\tfrac{1}{4})\,\mathrm{e}^{\mathrm{i}\pi/8}$ is a *pure number*, independent of $\hbar$. Hence $I \propto \hbar^{1/4}$ exactly. Contrast the nondegenerate case: for $S = \alpha x^{2}$ the rescaling that removes $\hbar$ is $x = \hbar^{1/2}u$, giving $I \propto \hbar^{1/2}$. The power of $\hbar$ is fixed by the rescaling exponent needed to make the phase $\hbar$-independent: a phase $\sim x^{p}$ near the saddle requires $x \sim \hbar^{1/p}$, so $I \sim \hbar^{1/p}$. A quadratic saddle ($p = 2$) gives $\hbar^{1/2}$; a quartic degenerate saddle ($p = 4$) gives $\hbar^{1/4}$. Equivalently, the contributing width follows from $S \sim \hbar$: $x^{4} \sim \hbar \Rightarrow \Delta x \sim \hbar^{1/4}$, which is *wider* than the nondegenerate $\hbar^{1/2}$ for small $\hbar$, and $I \sim A(x_{0})\,\Delta x \sim \hbar^{1/4}$. The flatter the phase at the saddle, the broader the stationary region and the slower $I$ vanishes as $\hbar \to 0$.

<!-- ─── -->

**6. Mexican-hat saddles.** For the example with $S(x) = (x^{2}-1)^{2}$ and $A(x) = \mathrm{e}^{\mathrm{i}kx}$:

(a) Verify that $S'(x_{0}) = 0$ has the three solutions $x_{0} = -1, 0, +1$ and compute $S(x_{0})$ and $S''(x_{0})$ at each.

(b) Apply $I \approx A(x_0)\sqrt{2\pi\mathrm{i}\hbar/S''(x_0)}\,\mathrm{e}^{\mathrm{i}S(x_0)/\hbar}$ to write down $I_{\mathrm{SPA}}(k)$ as a sum of three plane waves in $k$.

(c) Compute the inverse Fourier transform $\tilde{I}(x) = (1/2\pi)\int I_{\mathrm{SPA}}(k)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d}k$. Show that it is a sum of three delta peaks at the saddle positions, with relative weights set by $1/\sqrt{\vert S''(x_{0})\vert}$.

(d) From the criterion $\sqrt{\hbar/\vert S''\vert}\ll$ saddle separation, estimate the value of $\hbar$ at which adjacent saddles begin to overlap and SPA breaks down. Compare with {numref}`fig-saddle-point`.

**Solution.**

**(a)** Expand $S(x) = (x^{2}-1)^{2} = x^{4} - 2x^{2} + 1$, so $S'(x) = 4x^{3} - 4x = 4x(x^{2}-1)$. The equation $4x(x^{2}-1) = 0$ has exactly the three roots $x_{0} = -1, 0, +1$. With $S''(x) = 12x^{2} - 4$:

| $x_{0}$ | $S(x_{0})$ | $S''(x_{0})$ |
|---|---|---|
| $-1$ | $0$ | $8$ |
| $0$ | $1$ | $-4$ |
| $+1$ | $0$ | $8$ |

**(b)** With $A(x) = \mathrm{e}^{\mathrm{i}kx}$, each saddle contributes $A(x_{0})\sqrt{2\pi\mathrm{i}\hbar/S''(x_{0})}\,\mathrm{e}^{\mathrm{i}S(x_{0})/\hbar}$. Summing the three,

$$
I_{\mathrm{SPA}}(k) = \mathrm{e}^{-\mathrm{i}k}\sqrt{\frac{2\pi\mathrm{i}\hbar}{8}} + \sqrt{\frac{2\pi\mathrm{i}\hbar}{-4}}\,\mathrm{e}^{\mathrm{i}/\hbar} + \mathrm{e}^{+\mathrm{i}k}\sqrt{\frac{2\pi\mathrm{i}\hbar}{8}}.
$$

Using the principal branch $\sqrt{2\pi\mathrm{i}\hbar/S''} = \sqrt{2\pi\hbar/\vert S''\vert}\,\mathrm{e}^{\mathrm{i}\pi/4\,\mathrm{sgn}(S'')}$ — so $\sqrt{2\pi\mathrm{i}\hbar/8} = \tfrac{1}{2}\sqrt{\pi\hbar}\,\mathrm{e}^{\mathrm{i}\pi/4}$ and $\sqrt{2\pi\mathrm{i}\hbar/(-4)} = \sqrt{\pi\hbar/2}\,\mathrm{e}^{-\mathrm{i}\pi/4}$ —

$$
I_{\mathrm{SPA}}(k) = \tfrac{1}{2}\sqrt{\pi\hbar}\;\mathrm{e}^{\mathrm{i}\pi/4}\left(\mathrm{e}^{\mathrm{i}k} + \mathrm{e}^{-\mathrm{i}k}\right) + \sqrt{\tfrac{\pi\hbar}{2}}\;\mathrm{e}^{-\mathrm{i}\pi/4}\,\mathrm{e}^{\mathrm{i}/\hbar}.
$$

This is a sum of three plane waves $\mathrm{e}^{\mathrm{i}kx_{0}}$ — one per saddle; the $x_{0} = 0$ term carries $\mathrm{e}^{\mathrm{i}k\cdot0} = 1$ and is $k$-independent. Compactly, $I_{\mathrm{SPA}}(k) = \sqrt{\pi\hbar}\,\mathrm{e}^{\mathrm{i}\pi/4}\cos k + \sqrt{\pi\hbar/2}\,\mathrm{e}^{-\mathrm{i}\pi/4}\,\mathrm{e}^{\mathrm{i}/\hbar}$.

**(c)** Write $I_{\mathrm{SPA}}(k) = \sum_{x_{0}}c_{x_{0}}\,\mathrm{e}^{\mathrm{i}kx_{0}}$ with coefficients $c_{x_{0}} = \sqrt{2\pi\mathrm{i}\hbar/S''(x_{0})}\,\mathrm{e}^{\mathrm{i}S(x_{0})/\hbar}$. The inverse Fourier transform uses the standard representation $\tfrac{1}{2\pi}\int\mathrm{e}^{\mathrm{i}kx_{0}}\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d}k = \delta(x - x_{0})$:

$$
\tilde{I}(x) = \frac{1}{2\pi}\int I_{\mathrm{SPA}}(k)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d}k = \sum_{x_{0}}c_{x_{0}}\,\delta(x - x_{0}) = c_{-1}\,\delta(x+1) + c_{0}\,\delta(x) + c_{+1}\,\delta(x-1).
$$

It is a sum of three delta peaks located exactly at the saddle positions $x = -1, 0, +1$. Their weights satisfy $\vert c_{x_{0}}\vert = \sqrt{2\pi\hbar/\vert S''(x_{0})\vert} \propto 1/\sqrt{\vert S''(x_{0})\vert}$, so

$$
\frac{\vert c_{\pm1}\vert}{\vert c_{0}\vert} = \sqrt{\frac{\vert S''(0)\vert}{\vert S''(\pm1)\vert}} = \sqrt{\frac{4}{8}} = \frac{1}{\sqrt{2}}.
$$

The central peak at $x = 0$ is heavier than each outer peak by a factor $\sqrt{2}$, because the phase is flatter there ($\vert S''\vert = 4 < 8$) and the stationary region correspondingly wider. SPA literally reads the saddle locations — and their curvatures — off the $k$-space oscillation pattern.

**(d)** The contributing half-width around a saddle is $\sqrt{\hbar/\vert S''\vert}$, and the saddle separation here is $1$ (from $x = 0$ to $x = \pm1$). The widest saddle is the central one, $\vert S''(0)\vert = 4$, with width $\sqrt{\hbar/4}$. Adjacent saddles cease to be isolated once this width grows to the separation:

$$
\sqrt{\frac{\hbar}{4}} \sim 1,
$$

i.e. $\hbar \sim 4$.

A slightly more careful estimate adds the two half-widths, $\sqrt{\hbar/4} + \sqrt{\hbar/8} \sim 1$, giving $\hbar \sim 1.4$. Either way the breakdown scale is $\hbar \sim$ order unity (a few). This matches {numref}`fig-saddle-point`: at $\hbar = 0.05$ the widths $\sqrt{\hbar/4} \approx 0.11$ lie far below the unit separation and SPA is indistinguishable from exact, whereas at $\hbar = 0.5$ the width $\sqrt{0.5/4} \approx 0.35$ is a sizeable fraction of the separation — the strict inequality "$\ll$" is no longer comfortably satisfied — and SPA visibly degrades.

<!-- ─── -->

**7. Harmonic oscillator from SPA.** The harmonic-oscillator Lagrangian $L = \tfrac{1}{2}m\dot x^{2} - \tfrac{1}{2}m\omega^{2}x^{2}$ is quadratic in the path, so — as for the free particle — SPA applied to the path integral is **exact**.

(a) The classical path from $(x_{0}, 0)$ to $(x, T)$ is $x_\text{cl}(\tau) = A\cos\omega\tau + B\sin\omega\tau$ with constants fixed by the endpoints. Show $A = x_{0}$ and $B = (x - x_{0}\cos\omega T)/\sin\omega T$, and derive the classical action

$$
S_\text{cl}(x, T; x_{0}, 0) = \frac{m\omega}{2\sin\omega T}\Bigl[(x^{2} + x_{0}^{2})\cos\omega T - 2x x_{0}\Bigr].
$$

(b) Compute the mixed second derivative

$$
-\frac{\partial^{2}S_\text{cl}}{\partial x\,\partial x_{0}} = \frac{m\omega}{\sin\omega T}.
$$

This is the harmonic-oscillator analogue of the free-particle $m/T$ from Problem 4 of 3.2.3 — and reduces to it in the small-$\omega T$ limit (verify).

(c) Apply the SPA prefactor formula for a quadratic action — $K \approx \sqrt{(-\partial^{2}S_\text{cl}/(\partial x\,\partial x_{0}))/(2\pi\mathrm{i}\hbar)}\,\exp(\mathrm{i}S_\text{cl}/\hbar)$ — to write the **harmonic-oscillator propagator** explicitly:

$$
K_{\text{HO}}(x, T; x_{0}, 0) = \sqrt{\frac{m\omega}{2\pi\mathrm{i}\hbar\sin\omega T}}\,\exp\!\left[\frac{\mathrm{i}m\omega}{2\hbar\sin\omega T}\bigl((x^{2}+x_{0}^{2})\cos\omega T - 2x x_{0}\bigr)\right].
$$

(d) Identify the times $T = n\pi/\omega$ ($n = 1, 2, \ldots$) where $\sin\omega T = 0$ and the prefactor diverges. Connect this to the zero-mode (focal-point) breakdown of Problem 4 — the same special times appear in both analyses.

**Solution.**

(a) The Euler-Lagrange equation $m\ddot x_\text{cl} = -m\omega^{2}x_\text{cl}$ has the general solution $x_\text{cl}(\tau) = A\cos\omega\tau + B\sin\omega\tau$. Boundary conditions:

- $x_\text{cl}(0) = A = x_{0}$,
- $x_\text{cl}(T) = x_{0}\cos\omega T + B\sin\omega T = x$, giving $B = (x - x_{0}\cos\omega T)/\sin\omega T$.

Compute the velocity: $\dot x_\text{cl}(\tau) = -A\omega\sin\omega\tau + B\omega\cos\omega\tau$. The classical action is

$$
S_\text{cl} = \int_{0}^{T}\Bigl[\tfrac{1}{2}m\dot x_\text{cl}^{2} - \tfrac{1}{2}m\omega^{2}x_\text{cl}^{2}\Bigr]\,\mathrm{d}\tau.
$$

A standard manipulation simplifies this on the classical trajectory: integrate the kinetic term by parts,

$$
\int_{0}^{T}\tfrac{1}{2}m\dot x_\text{cl}^{2}\,\mathrm{d}\tau = \tfrac{1}{2}m\bigl[x_\text{cl}\,\dot x_\text{cl}\bigr]_{0}^{T} - \int_{0}^{T}\tfrac{1}{2}m x_\text{cl}\,\ddot x_\text{cl}\,\mathrm{d}\tau,
$$

and substitute $\ddot x_\text{cl} = -\omega^{2}x_\text{cl}$ (equation of motion) to make the integral cancel against the potential term:

$$
S_\text{cl} = \tfrac{1}{2}m\bigl[x_\text{cl}\,\dot x_\text{cl}\bigr]_{0}^{T} = \tfrac{1}{2}m\bigl[x\,\dot x_\text{cl}(T) - x_{0}\,\dot x_\text{cl}(0)\bigr].
$$

The boundary velocities are

$$
\dot x_\text{cl}(0) = B\omega = \omega\,\frac{x - x_{0}\cos\omega T}{\sin\omega T}, \qquad \dot x_\text{cl}(T) = -A\omega\sin\omega T + B\omega\cos\omega T = \omega\,\frac{x\cos\omega T - x_{0}}{\sin\omega T},
$$

using $-x_{0}\sin^{2}\omega T + (x - x_{0}\cos\omega T)\cos\omega T = x\cos\omega T - x_{0}(\sin^{2}\omega T + \cos^{2}\omega T) = x\cos\omega T - x_{0}$. Substituting,

$$
S_\text{cl} = \frac{m\omega}{2\sin\omega T}\Bigl[x(x\cos\omega T - x_{0}) - x_{0}(x - x_{0}\cos\omega T)\Bigr] = \frac{m\omega}{2\sin\omega T}\Bigl[(x^{2} + x_{0}^{2})\cos\omega T - 2x x_{0}\Bigr]. \quad\checkmark
$$

(b) Differentiate $S_\text{cl}$ with respect to $x$, holding $x_{0}$ and $T$ fixed:

$$
\frac{\partial S_\text{cl}}{\partial x} = \frac{m\omega}{2\sin\omega T}\bigl[2x\cos\omega T - 2x_{0}\bigr] = \frac{m\omega}{\sin\omega T}\bigl[x\cos\omega T - x_{0}\bigr].
$$

(Sanity check: this equals $m\dot x_\text{cl}(T) = p_\text{cl}(T)$ — the final momentum — by part (a). The classical-mechanics identity $\partial S_\text{cl}/\partial x = p_\text{cl}$ holds for any quadratic action.) Now differentiate with respect to $x_{0}$:

$$
\frac{\partial^{2}S_\text{cl}}{\partial x_{0}\,\partial x} = \frac{m\omega}{\sin\omega T}\,\frac{\partial}{\partial x_{0}}\bigl[x\cos\omega T - x_{0}\bigr] = -\frac{m\omega}{\sin\omega T}.
$$

Therefore $-\partial^{2}S_\text{cl}/(\partial x\,\partial x_{0}) = m\omega/\sin\omega T$, as claimed. $\checkmark$

**Free-particle limit.** For small $\omega T$, $\sin\omega T \approx \omega T$, so $m\omega/\sin\omega T \to m\omega/(\omega T) = m/T$ — exactly the free-particle prefactor (3-2-3 P5). The harmonic oscillator reduces to the free particle when the period $2\pi/\omega$ is much longer than the elapsed time $T$: the restoring force has no time to act.

(c) Substituting into the SPA prefactor formula gives the harmonic-oscillator propagator as quoted. The prefactor is $\sqrt{m\omega/(2\pi\mathrm{i}\hbar\sin\omega T)}$; the exponent carries the classical action $S_\text{cl}/\hbar$. This propagator is **exact**, not merely an approximation, because the harmonic action is purely quadratic: SPA's two underlying truncations (quadratic fluctuations, constant amplitude) are exact identities — same logic as Problem 1's pure-Gaussian case.

(d) The prefactor $1/\sqrt{\sin\omega T}$ diverges whenever $\sin\omega T = 0$, i.e. at

$$
T = \frac{n\pi}{\omega}, \qquad n = 1, 2, 3, \ldots
$$

These are exactly the special times Problem 4(b) identified as zero-mode times of the second-variation operator $\hat D = -m(\mathrm{d}^{2}/\mathrm{d}t^{2} + \omega^{2})$: at $T = n\pi/\omega$ the eigenvalue $\lambda_{n} = m[(n\pi/T)^{2} - \omega^{2}]$ vanishes, $\det\hat D \to 0$, and $1/\sqrt{\det\hat D} \to \infty$ — the same divergence, viewed from the path-integral side. Physically these are **focal points** of the harmonic motion: at $T = n\pi/\omega$ every trajectory leaving $x_{0}$ reconverges to $\pm x_{0}$ regardless of initial velocity, so the propagator amplitude pile-up at the focal endpoint is infinite (in the strict semiclassical limit). The breakdown is real but mild — keeping higher-order fluctuation terms restores a finite, well-defined amplitude that carries a phase jump of $-\pi/2$ each time a focal point is crossed.

**The bigger picture.** SPA reproduces the *exact* harmonic-oscillator propagator from the SPA prefactor formula. Comparing the harmonic-oscillator prefactor $m\omega/\sin\omega T$ to the free-particle $m/T$ shows that the dimensionless combination $\omega T$ is what controls the deviation: small $\omega T \ll 1$ recovers the free case (Problem 4 of 3-2-3); $\omega T \sim 1$ shows the new structure (focal points); $\omega T \gg 1$ is the deep adiabatic regime. The two propagators are tightly linked: same SPA machinery, two different quadratic actions, one chapter of physics.

<!-- ─── -->

**8. Correspondence principle.** The ratio $S_\text{cl}/\hbar$ controls whether a system is quantum or classical.

(a) For a free particle of mass $m$ traversing distance $d$ in time $t$, $S_\text{cl} = md^{2}/(2t)$. Compute $S_\text{cl}/\hbar$ for an electron ($m\approx 9\times 10^{-31}\,\text{kg}$) moving $1\,\text{nm}$ in $1\,\text{ns}$, and for a macroscopic object ($m = 0.1\,\text{kg}$) moving $1\,\text{m}$ in $1\,\text{s}$.

(b) For the macroscopic case in part (a), the SPA selects one dominant path. Estimate the number of $2\pi$ phase oscillations as the endpoint $x$ varies over $1\,\text{mm}$. Why does this make the propagator effectively a delta function on macroscopic scales?

(c) Explain how this quantitative argument embodies the correspondence principle: classical mechanics emerges from quantum mechanics when $S_\text{cl}\gg\hbar$.

**Solution.**

**(a)** Use $S_\text{cl} = md^{2}/(2t)$ and $\hbar \approx 1.05\times10^{-34}\,\mathrm{J\cdot s}$.

Electron ($m \approx 9\times 10^{-31}\,\text{kg}$, $d = 1\,\text{nm} = 10^{-9}\,\text{m}$, $t = 1\,\text{ns} = 10^{-9}\,\text{s}$):

$$
S_\text{cl} = \frac{(9\times 10^{-31})(10^{-9})^{2}}{2(10^{-9})} \approx 4.5\times10^{-40}\,\mathrm{J\cdot s}, \qquad \frac{S_\text{cl}}{\hbar} \approx \frac{4.5\times10^{-40}}{1.05\times10^{-34}} \approx 4\times10^{-6}.
$$

Since $S_\text{cl}/\hbar \ll 1$, the electron is deep in the **quantum regime**: all paths contribute and full wave behaviour survives.

Macroscopic case ($m = 0.1\,\text{kg}$, $d = 1\,\text{m}$, $t = 1\,\text{s}$):

$$
S_\text{cl} = \frac{(0.1)(1)^{2}}{2(1)} = 0.05\,\mathrm{J\cdot s}, \qquad \frac{S_\text{cl}}{\hbar} = \frac{0.05}{1.05\times10^{-34}} \approx 5\times10^{32}.
$$

Since $S_\text{cl}/\hbar \gg 1$, the macroscopic object is deep in the **classical regime**: a single saddle path dominates.

**(b)** The propagator phase is $\Phi(x) = S_\text{cl}(x)/\hbar = mx^{2}/(2\hbar t)$. As the endpoint shifts by $\Delta x$ near $x = d$, the phase changes by

$$
\Delta\Phi \approx \frac{\partial\Phi}{\partial x}\,\Delta x = \frac{md}{\hbar t}\,\Delta x.
$$

For the macroscopic case ($m = 0.1\,\text{kg}$, $d = 1\,\text{m}$, $t = 1\,\text{s}$) and $\Delta x = 1\,\text{mm} = 10^{-3}\,\text{m}$,

$$
\Delta\Phi \approx \frac{(0.1)(1)}{(1.05\times10^{-34})(1)}\times10^{-3} \approx 9.5\times10^{29}\ \text{rad},
$$

so the number of full $2\pi$ oscillations is $\Delta\Phi/(2\pi) \approx 1.5\times10^{29}$.

The propagator's phase therefore winds through $\sim 10^{29}$ complete cycles over a single millimetre. Across any macroscopically resolvable displacement the phase oscillates so violently that amplitudes from neighbouring endpoints interfere destructively and cancel — stationary phase again, now in the endpoint variable. Only at the one endpoint actually reached by the classical trajectory does the contribution survive. Smeared over any realistic position resolution, the propagator is therefore effectively a delta function pinned to the classical endpoint.

**(c)** The dimensionless ratio $S_\text{cl}/\hbar$ is the precise control parameter of the quantum-to-classical crossover. When $S_\text{cl} \gg \hbar$ — as for the macroscopic case, $S_\text{cl}/\hbar \sim 10^{32}$ — the phase $S_\text{cl}/\hbar$ is enormous and varies enormously fast as the path is deformed, so stationary phase makes a single classical path overwhelmingly dominant and the propagator collapses onto the classical trajectory; interference between alternative paths is washed out and deterministic classical mechanics emerges. When $S_\text{cl} \lesssim \hbar$ — as for the electron, $S_\text{cl}/\hbar \sim 10^{-6}$ — many paths have comparable phase, contribute coherently, and genuine quantum wave behaviour persists. This is the **correspondence principle made quantitative**: classical mechanics is recovered not by the literal limit $\hbar \to 0$ ($\hbar$ is a fixed constant of nature) but by $S_\text{cl}/\hbar \to \infty$, which any macroscopic action achieves automatically. The very same ratio that the lecture used to tabulate the classical, semiclassical, and quantum regimes is what these numbers make concrete.
