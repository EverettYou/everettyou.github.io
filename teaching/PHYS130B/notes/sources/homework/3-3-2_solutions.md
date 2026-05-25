# 3.3.2 WKB Approximation
Worked solutions for the homework problems in the [3.3.2 WKB Approximation](../ch3_path-integral/3-3-2-wkb-approximation) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Hamilton-Jacobi from WKB.** Substitute the WKB ansatz $\psi(x) = A(x)\,\mathrm{e}^{\mathrm{i}W(x)/\hbar}$ into the time-independent Schrödinger equation $-\frac{\hbar^{2}}{2m}\psi'' + V(x)\psi = E\psi$.

(a) Collect terms by powers of $\hbar$ and show that at leading order ($\hbar^{0}$) the phase $W(x)$ satisfies the Hamilton-Jacobi equation $\frac{1}{2m}(W')^{2} + V(x) = E$.

(b) At next order ($\hbar^{1}$), show that $2A'W' + AW'' = 0$. Integrate this to obtain $A \propto 1/\sqrt{W'} = 1/\sqrt{p(x)}$.

**Solution.**

**(a)** Differentiate the ansatz $\psi = A\,\mathrm{e}^{\mathrm{i}W/\hbar}$ twice. The first derivative is

$$
\psi' = \left(A' + \frac{\mathrm{i}}{\hbar}A\,W'\right)\mathrm{e}^{\mathrm{i}W/\hbar},
$$

and differentiating once more,

$$
\psi'' = \left(A'' + \frac{2\mathrm{i}}{\hbar}A'\,W' + \frac{\mathrm{i}}{\hbar}A\,W'' - \frac{1}{\hbar^{2}}A\,(W')^{2}\right)\mathrm{e}^{\mathrm{i}W/\hbar}.
$$

Insert this into $-\frac{\hbar^{2}}{2m}\psi'' + (V-E)\psi = 0$ and cancel the common factor $\mathrm{e}^{\mathrm{i}W/\hbar}$:

$$
-\frac{\hbar^{2}}{2m}A'' - \frac{\mathrm{i}\hbar}{2m}\bigl(2A'W' + AW''\bigr) + \frac{1}{2m}A\,(W')^{2} + (V-E)A = 0.
$$

The three groups carry distinct powers of $\hbar$: the $(W')^{2}$ and $(V-E)$ terms are $\hbar^{0}$, the bracket multiplying $\mathrm{i}\hbar$ is $\hbar^{1}$, and the $A''$ term is $\hbar^{2}$. Treating $\hbar$ as a small expansion parameter, each power must vanish separately. At order $\hbar^{0}$,

$$
\frac{1}{2m}A\,(W')^{2} + (V-E)A = 0,
$$

so $\dfrac{1}{2m}(W')^{2} + V(x) = E$,

the **Hamilton-Jacobi equation**. Solving for the phase gradient gives the local classical momentum, $W' = p(x) = \pm\sqrt{2m(E-V)}$.

**(b)** At order $\hbar^{1}$ the bracketed term must vanish:

$$
2A'\,W' + A\,W'' = 0.
$$

Divide through by $A\,W'$ (nonzero away from turning points):

$$
\frac{2A'}{A} + \frac{W''}{W'} = 0,
$$

i.e. $\dfrac{\mathrm{d}}{\mathrm{d}x}(2\ln A + \ln W') = 0$.

Hence $2\ln A + \ln W' = \mathrm{const}$, i.e. $A^{2}W' = \mathrm{const}$. In the allowed region take $p(x) = |W'(x)| = \sqrt{2m(E-V)} > 0$ (the sign of $W'$ tracks propagation direction), so

$$
A(x) = \frac{C}{\sqrt{|W'(x)|}} = \frac{C}{\sqrt{p(x)}}.
$$

Equivalently, multiply $2A'W' + AW'' = 0$ by $A$ to get $2AA'W' + A^{2}W'' = \frac{\mathrm{d}}{\mathrm{d}x}(A^{2}W') = 0$ directly. The constant $A^{2}p$ is the probability current $j = A^{2}p/m$: the WKB amplitude law is nothing but current conservation.

<!-- ─── -->

**2. Allowed and forbidden regions.** A particle of energy $E$ moves in a slowly varying potential $V(x)$.

(a) In the classically allowed region ($E > V$), write the WKB wavefunction $\psi \sim p^{-1/2}\,\exp(\pm\frac{\mathrm{i}}{\hbar}\int^{x}p\,\mathrm{d}x')$ and explain physically why the amplitude $1/\sqrt{p}$ means the particle is more likely found where it moves slowly.

(b) In the classically forbidden region ($E < V$), set $p \to \mathrm{i}\kappa$ with $\kappa = \sqrt{2m(V-E)}$ and show that the wavefunction decays as $\psi \sim \kappa^{-1/2}\,\exp(-\frac{1}{\hbar}\int^{x}\kappa\,\mathrm{d}x')$.

**Solution.**

**(a)** Where $E > V$, the momentum $p(x) = \sqrt{2m(E-V)}$ is real and the phase $W = \int p\,\mathrm{d}x'$ accumulates as a genuine oscillation. Combining the phase with the amplitude $A = C/\sqrt{p}$ from Problem 1,

$$
\psi(x) \sim \frac{1}{\sqrt{p(x)}}\,\exp\!\left[\pm\frac{\mathrm{i}}{\hbar}\int^{x}p(x')\,\mathrm{d}x'\right],
$$

so the probability density is $\vert\psi\vert^{2} \propto 1/p(x)$.

This is exactly the **classical dwell time**. Picture a classical particle of energy $E$ sweeping through $V(x)$: the time it spends in an interval $\mathrm{d}x$ is $\mathrm{d}t = \mathrm{d}x/v = m\,\mathrm{d}x/p$. The fraction of a long observation during which the particle is found in $\mathrm{d}x$ is therefore $\propto 1/p$. Where the potential rises and the particle slows down, $p$ is small, $\mathrm{d}t$ is large, and the particle lingers; where it speeds up, it passes through quickly. The WKB density $\vert\psi\vert^{2}\propto 1/p$ reproduces this dwell-time distribution — the quantum particle is most likely found precisely where its classical counterpart moves slowest.

**(b)** Where $E < V$, the quantity under the square root flips sign: $2m(E-V) < 0$. Write $p = \mathrm{i}\kappa$ with $\kappa = \sqrt{2m(V-E)}$ real and positive (momentum scale; the dimensionless tunneling exponent is $\gamma = \int\kappa\,\mathrm{d}x/\hbar$). Substituting into the allowed-region form, the phase integral becomes

$$
\pm\frac{\mathrm{i}}{\hbar}\int^{x}p\,\mathrm{d}x' = \pm\frac{\mathrm{i}}{\hbar}\int^{x}\mathrm{i}\kappa\,\mathrm{d}x' = \mp\frac{1}{\hbar}\int^{x}\kappa\,\mathrm{d}x',
$$

a *real* exponent — the oscillation has turned into exponential growth or decay. The prefactor likewise becomes $p^{-1/2} = (\mathrm{i}\kappa)^{-1/2} = \kappa^{-1/2}\,\mathrm{e}^{-\mathrm{i}\pi/4}$, a constant phase that can be absorbed into the overall normalization. The two signs give two independent real solutions; the physical (normalizable, decaying) branch takes the lower sign,

$$
\psi(x) \sim \frac{1}{\sqrt{\kappa(x)}}\,\exp\!\left[-\frac{1}{\hbar}\int^{x}\kappa(x')\,\mathrm{d}x'\right].
$$

The wavefunction does not vanish abruptly at the classical boundary — it leaks into the forbidden region and dies off exponentially on the scale $\hbar/\kappa$, which is the origin of quantum tunneling.

<!-- ─── -->

**3. Validity criterion.** The WKB approximation requires $\vert\mathrm{d}\lambda/\mathrm{d}x\vert \ll 2\pi$, where $\lambda(x) = 2\pi\hbar/p(x)$ is the local de Broglie wavelength.

(a) Show that this is equivalent to the dimensionful condition $\hbar\,\vert V'(x)\vert \ll 2\sqrt{2m}\,(E - V(x))^{3/2}$ in the allowed region.

(b) For a linear potential $V(x) = Fx$ (constant force), identify where the criterion fails. Relate this to the turning point $x_{0} = E/F$.

(c) For a Gaussian barrier $V(x) = V_{0}\,\mathrm{e}^{-x^{2}/a^{2}}$ with energy $E = V_{0}/4$, identify the classical turning points and discuss whether WKB is reliable away from them.

**Solution.**

**(a)** Differentiate $\lambda = 2\pi\hbar/p$:

$$
\frac{\mathrm{d}\lambda}{\mathrm{d}x} = -\frac{2\pi\hbar}{p^{2}}\,p'(x).
$$

The validity condition $\vert\mathrm{d}\lambda/\mathrm{d}x\vert \ll 2\pi$ becomes $2\pi\hbar\,\vert p'\vert/p^{2} \ll 2\pi$, i.e.

$$
\hbar\,\vert p'(x)\vert \ll p(x)^{2}.
$$

Now express $p'$ through the potential. With $p = \sqrt{2m(E-V)}$,

$$
p' = \frac{\mathrm{d}}{\mathrm{d}x}\sqrt{2m(E-V)} = \frac{-2m\,V'}{2\sqrt{2m(E-V)}} = -\frac{m\,V'}{p},
$$

so $\vert p'\vert = m\,\vert V'\vert/p$. Substituting,

$$
\hbar\,\frac{m\,\vert V'\vert}{p} \ll p^{2},
$$

so $\hbar\,m\,\vert V'\vert \ll p^{3} = (2m(E-V))^{3/2}$.

Divide both sides by $m$ and use $(2m)^{3/2}/m = 2^{3/2}m^{1/2} = 2\sqrt{2m}$:

$$
\hbar\,\vert V'(x)\vert \ll 2\sqrt{2m}\,\bigl(E - V(x)\bigr)^{3/2}.
$$

The condition says the potential energy must change by little over one wavelength compared with the kinetic energy scale — the semiclassical "slowly varying potential" assumption.

**(b)** For $V(x) = Fx$ the force is constant, $V'(x) = F$, so the left side $\hbar F$ is fixed while the right side is $2\sqrt{2m}\,(E - Fx)^{3/2}$. The criterion reads

$$
\hbar F \ll 2\sqrt{2m}\,(E - Fx)^{3/2}.
$$

It holds comfortably deep in the allowed region where $E - Fx$ is large, but **fails as $x \to x_{0} = E/F$**, the classical turning point, because $(E-Fx)^{3/2} \to 0$ there and the right side cannot dominate $\hbar F$. Setting the two sides comparable locates the edge of the WKB-trustworthy zone: with $E - Fx = F(x_{0} - x)$,

$$
(x_{0} - x)^{3/2} \sim \frac{\hbar}{2\sqrt{2m}\,F^{1/2}},
$$

so $x_{0} - x \sim (\hbar^{2}/2mF)^{1/3} \equiv \ell$.

So WKB breaks down within a layer of thickness of order the Airy length $\ell = (\hbar^{2}/2mF)^{1/3}$ around the turning point. Outside that thin layer the linear potential is varying slowly enough and WKB is fine; inside it one must use the Airy-function matching of Problem 6.

**(c)** The turning points are where $V(x) = E$:

$$
V_{0}\,\mathrm{e}^{-x^{2}/a^{2}} = \frac{V_{0}}{4},
$$

giving $\mathrm{e}^{-x^{2}/a^{2}} = 1/4$, so $x^{2} = a^{2}\ln 4$,

giving two symmetric turning points

$$
x_{\pm} = \pm a\sqrt{\ln 4} = \pm a\sqrt{2\ln 2} \approx \pm 1.18\,a.
$$

Since the barrier peaks at $V(0) = V_{0} > E$, the region $\vert x\vert < x_{+}$ is classically **forbidden** and $\vert x\vert > x_{+}$ is **allowed**. WKB is unreliable in the Airy layers around $x_{\pm}$, where $E - V \to 0$. Away from those points, the test of reliability is the criterion of part (a). The barrier varies on the length scale $a$, so $\vert V'\vert \sim V_{0}/a$, and away from the turning points $\vert E - V\vert$ is of order $V_{0}$. The criterion then reads, in order of magnitude,

$$
\hbar\,\frac{V_{0}}{a} \ll 2\sqrt{2m}\,V_{0}^{3/2},
$$

i.e. $\hbar/(a\sqrt{2mV_{0}}) \ll 1$,

i.e. the barrier width $a$ must greatly exceed the penetration/decay length $\hbar/\sqrt{2mV_{0}}$. **If the barrier is wide and tall** ($a\sqrt{2mV_{0}}/\hbar \gg 1$), WKB is accurate everywhere except in the two narrow Airy zones, and the tunneling exponent $\gamma$ can be trusted. **If the barrier is thin** (width comparable to a de Broglie wavelength), the turning-point zones overlap, there is no genuine semiclassical interior, and WKB fails throughout.

<!-- ─── -->

**4. Square-barrier tunneling (heuristic).** A particle of mass $m$ and energy $E < V_{0}$ encounters a rectangular barrier $V(x) = V_{0}$ for $0 < x < a$ and $V = 0$ elsewhere. The discontinuous walls **violate** the WKB validity criterion $\hbar|V'(x)| \ll 2\sqrt{2m}\,(E-V(x))^{3/2}$, so the formula below captures only the dominant exponential factor — the true transmission coefficient has an additional reflection-coefficient prefactor of order unity.

(a) Apply $T \approx \mathrm{e}^{-2\gamma}$ with $\gamma = \frac{1}{\hbar}\int_{0}^{a}\kappa\,\mathrm{d}x$ to obtain $T \approx \exp\!\left(-\frac{2a}{\hbar}\sqrt{2m(V_{0} - E)}\right)$.

(b) Evaluate $T$ for an electron ($m \approx 9.1\times 10^{-31}\,\text{kg}$) with $V_{0} - E = 2\,\text{eV}$ and $a = 0.2\,\text{nm}$. Is tunneling significant?

(c) Show that doubling the barrier width $a\to 2a$ replaces $T$ by $T^{2}$ (much smaller). Explain why tunneling is exponentially sensitive to barrier width.

**Solution.**

**(a)** Inside the barrier the potential is constant, $V = V_{0}$, so the decay rate $\kappa = \sqrt{2m(V_{0}-E)}$ is constant. The tunneling exponent is then a trivial integral,

$$
\gamma = \frac{1}{\hbar}\int_{0}^{a}\kappa\,\mathrm{d}x = \frac{\kappa\,a}{\hbar} = \frac{a}{\hbar}\sqrt{2m(V_{0}-E)}.
$$

The transmission probability is

$$
T \approx \mathrm{e}^{-2\gamma} = \exp\!\left(-\frac{2a}{\hbar}\sqrt{2m(V_{0}-E)}\right).
$$

**(b)** With $V_{0} - E = 2\,\text{eV} = 3.20\times 10^{-19}\,\text{J}$, $m = 9.1\times 10^{-31}\,\text{kg}$, $a = 0.2\,\text{nm} = 2.0\times 10^{-10}\,\text{m}$, and $\hbar = 1.055\times 10^{-34}\,\mathrm{J\cdot s}$:

$$
\kappa = \sqrt{2m(V_{0}-E)} = \sqrt{2(9.1\times 10^{-31})(3.20\times 10^{-19})} \approx 7.64\times 10^{-25}\,\mathrm{kg\cdot m/s},
$$

$$
\gamma = \frac{\kappa a}{\hbar} = \frac{(7.64\times 10^{-25})(2.0\times 10^{-10})}{1.055\times 10^{-34}} \approx 1.45.
$$

Therefore

$$
T \approx \mathrm{e}^{-2\gamma} = \mathrm{e}^{-2.90} \approx 5.5\times 10^{-2}.
$$

About **5%** of incident electrons tunnel through — small but absolutely significant. A sub-nanometre barrier of a few eV is no obstacle to electrons, which is exactly why electron tunneling is observed routinely (field emission, tunnel diodes, STM). The order-unity prefactor omitted by the heuristic formula does not change this conclusion.

**(c)** Since $\gamma = \kappa a/\hbar$ is **linear in $a$**, doubling the width sends $\gamma \to 2\gamma$, and

$$
T(2a) \approx \mathrm{e}^{-2(2\gamma)} = \bigl(\mathrm{e}^{-2\gamma}\bigr)^{2} = \bigl[T(a)\bigr]^{2}.
$$

Because $T < 1$, squaring makes it dramatically smaller — for the electron above, $T \approx 0.055$ would drop to $T^{2} \approx 0.003$. The deep reason is that the transmission depends on width through an **exponential**, $T \sim \mathrm{e}^{-2\kappa a/\hbar}$: the wavefunction decays by a fixed factor per unit length inside the barrier, so equal increments of width multiply $T$ by equal factors. A linear change in $a$ produces a geometric (exponential) change in $T$. This exponential sensitivity is what makes scanning tunneling microscopy possible — a tip-height change of a fraction of an ångström produces a measurable change in tunneling current.

<!-- ─── -->

**5. Penetration depth.** The characteristic decay length of the wavefunction in a forbidden region is $\lambda_\text{decay} = \hbar/\kappa$ with $\kappa = \sqrt{2m(V - E)}$.

(a) Compute $\lambda_\text{decay}$ for an electron at a metal surface with work function $V - E = 5\,\text{eV}$. Express the answer in angstroms.

(b) Explain why this length scale makes scanning tunneling microscopy (STM) work: the tunneling current depends exponentially on the tip-surface distance.

**Solution.**

**(a)** With $V - E = 5\,\text{eV} = 8.01\times 10^{-19}\,\text{J}$ and $m = 9.1\times 10^{-31}\,\text{kg}$, the decay rate is

$$
\kappa = \sqrt{2m(V-E)} = \sqrt{2(9.1\times 10^{-31})(8.01\times 10^{-19})} \approx 1.21\times 10^{-24}\,\mathrm{kg\cdot m/s},
$$

so the penetration depth is

$$
\lambda_\text{decay} = \frac{\hbar}{\kappa} = \frac{1.055\times 10^{-34}}{1.21\times 10^{-24}} \approx 8.7\times 10^{-11}\,\text{m} \approx 0.87\,\text{Å}.
$$

The electron wavefunction outside the metal decays on a scale of roughly one ångström — an atomic length.

**(b)** The tunneling current in STM is $I \propto T \approx \mathrm{e}^{-2\gamma}$, and for a gap $d$ between tip and surface $\gamma = \kappa d/\hbar = d/\lambda_\text{decay}$, so

$$
I \propto \exp\!\left(-\frac{2d}{\lambda_\text{decay}}\right).
$$

With $\lambda_\text{decay} \approx 0.87\,\text{Å}$, increasing the gap by a single ångström multiplies the current by $\mathrm{e}^{-2/0.87} \approx \mathrm{e}^{-2.3} \approx 0.1$ — a tenfold drop. The current is so steeply dependent on $d$ that essentially all of it flows through the **single closest atom** of the tip, and height variations of a few hundredths of an ångström are detectable. That extreme sensitivity is what gives the STM its atomic-scale spatial resolution: a small geometric corrugation of the surface translates into a large, measurable current modulation.

<!-- ─── -->

**6. Airy connection formula.** At a soft turning point $x_{0}$ with $V'(x_{0}) > 0$, linearize the potential as $V(x) \approx E + V'(x_{0})(x - x_{0})$.

(a) Show that the Schrödinger equation reduces to the Airy equation $\psi'' = z\psi$ with $z = (x - x_{0})/\ell$, and identify the length scale $\ell = \bigl(\hbar^{2}/(2m\,V'(x_{0}))\bigr)^{1/3}$.

(b) The Airy function $\mathrm{Ai}(z)$ decays exponentially for $z\to+\infty$ (forbidden side) and oscillates for $z\to-\infty$ (allowed side). Use its asymptotic forms to recover the connection formula $\frac{1}{\sqrt{\kappa}}\mathrm{e}^{-\int_x^{x_0}\kappa\,\mathrm{d}x'/\hbar} \longleftrightarrow \frac{2}{\sqrt{p}}\sin\!\bigl[\int_{x_0}^{x}p\,\mathrm{d}x'/\hbar + \pi/4\bigr]$ with the $\pi/4$ phase shift.

(c) Explain in one sentence why omitting the $\pi/4$ shift in the bound-state quantization rule of §3.3.3 would mis-predict the harmonic-oscillator zero-point energy.

**Solution.**

**(a)** Insert the linearized potential $V(x) \approx E + V'(x_{0})(x-x_{0})$ into the time-independent Schrödinger equation. The constant $E$ cancels against the $E\psi$ on the right:

$$
-\frac{\hbar^{2}}{2m}\psi'' + \bigl[E + V'(x_{0})(x-x_{0})\bigr]\psi = E\psi,
$$

so $\psi'' = \dfrac{2m\,V'(x_{0})}{\hbar^{2}}\,(x-x_{0})\,\psi$.

Introduce the dimensionless coordinate $z = (x-x_{0})/\ell$. Then $\mathrm{d}/\mathrm{d}x = \ell^{-1}\mathrm{d}/\mathrm{d}z$, so $\psi'' = \ell^{-2}\,\mathrm{d}^{2}\psi/\mathrm{d}z^{2}$, and $x - x_{0} = \ell z$:

$$
\frac{1}{\ell^{2}}\frac{\mathrm{d}^{2}\psi}{\mathrm{d}z^{2}} = \frac{2m\,V'(x_{0})}{\hbar^{2}}\,\ell\,z\,\psi,
$$

i.e. $\dfrac{\mathrm{d}^{2}\psi}{\mathrm{d}z^{2}} = \dfrac{2m\,V'(x_{0})\,\ell^{3}}{\hbar^{2}}\,z\,\psi$.

This is the Airy equation $\psi'' = z\psi$ provided the coefficient equals one,

$$
\frac{2m\,V'(x_{0})\,\ell^{3}}{\hbar^{2}} = 1,
$$

so $\ell = (\hbar^{2}/2m\,V'(x_{0}))^{1/3}$.

This $\ell$ is the width of the turning-point zone where neither the oscillatory nor the exponential WKB form is valid — the region the Airy function bridges.

**(b)** The Airy function has the asymptotic forms (standard results)

$$
\mathrm{Ai}(z) \;\xrightarrow{z\to+\infty}\; \frac{1}{2\sqrt{\pi}}\,z^{-1/4}\,\exp\!\left[-\tfrac{2}{3}z^{3/2}\right],
$$

$$
\mathrm{Ai}(z) \;\xrightarrow{z\to-\infty}\; \frac{1}{\sqrt{\pi}}\,(-z)^{-1/4}\,\sin\!\left[\tfrac{2}{3}(-z)^{3/2} + \tfrac{\pi}{4}\right].
$$

Now match these to the WKB forms. On the **forbidden side** ($x > x_{0}$, $z > 0$), $\kappa = \sqrt{2m(V-E)} = \sqrt{2m\,V'(x_{0})(x-x_{0})}$. Using $2m\,V'(x_{0}) = \hbar^{2}/\ell^{3}$ and $x - x_{0} = \ell z$,

$$
\kappa = \sqrt{\frac{\hbar^{2}}{\ell^{3}}\,\ell z} = \frac{\hbar}{\ell}\,z^{1/2},
$$

so $\dfrac{1}{\hbar}\int_{x_{0}}^{x}\kappa\,\mathrm{d}x' = \int_{0}^{z}z'^{1/2}\,\mathrm{d}z' = \tfrac{2}{3}z^{3/2}$.

So the decaying WKB solution $\kappa^{-1/2}\exp[-\frac1\hbar\int\kappa]$ behaves as $z^{-1/4}\,\mathrm{e}^{-\frac23 z^{3/2}}$ — exactly the $z\to+\infty$ form of $\mathrm{Ai}$. On the **allowed side** ($x < x_{0}$, $z < 0$), $p = \sqrt{2m\,V'(x_{0})(x_{0}-x)} = (\hbar/\ell)(-z)^{1/2}$, and

$$
\frac{1}{\hbar}\int_{x}^{x_{0}}p\,\mathrm{d}x' = \tfrac{2}{3}(-z)^{3/2},
$$

so the oscillatory WKB solution $p^{-1/2}\sin[\frac1\hbar\int_{x}^{x_{0}}p + \tfrac{\pi}{4}]$ matches the $z\to-\infty$ form of $\mathrm{Ai}$, **including the $+\pi/4$** that appears in the Airy asymptotics. Comparing the amplitudes of the two limits, the oscillatory side carries prefactor $1/\sqrt{\pi}$ and the exponential side $1/(2\sqrt{\pi})$ — a ratio of $2$. Restoring the WKB amplitudes $1/\sqrt{p}$, $1/\sqrt{\kappa}$, this is the connection formula

$$
\frac{1}{\sqrt{\kappa}}\,\exp\!\left[-\frac1\hbar\int_{x}^{x_{0}}\kappa\,\mathrm{d}x'\right]
\;\longleftrightarrow\;
\frac{2}{\sqrt{p}}\,\sin\!\left[\frac1\hbar\int_{x_{0}}^{x}p\,\mathrm{d}x' + \frac{\pi}{4}\right].
$$

The $\pi/4$ is not an extra assumption: it is forced by the asymptotic phase of the exact Airy function that interpolates between the two regions.

**(c)** Each soft turning point contributes a $\pi/4$ phase, so a well bounded by two soft turning points carries an extra $\pi/2$; dropping it changes the Bohr-Sommerfeld rule from $\oint p\,\mathrm{d}x = 2\pi\hbar\,(n + \tfrac12)$ to $\oint p\,\mathrm{d}x = 2\pi\hbar\,n$, which for the harmonic oscillator gives $E_{n} = n\hbar\omega$ — a vanishing ground-state energy instead of the correct zero-point energy $\tfrac12\hbar\omega$.

<!-- ─── -->

★ **7. Double-well tunnel splitting.** Consider a symmetric double-well potential with two minima separated by a barrier of width $\sim a$. Let $\omega$ be the small-oscillation frequency in either well and $\gamma = \frac{1}{\hbar}\int_\text{barrier}\kappa\,\mathrm{d}x$.

(a) Estimate the tunneling amplitude $\Delta \sim \tfrac{1}{2}\hbar\omega\,\mathrm{e}^{-\gamma}$ from the WKB tunneling formula (the same energy scale as the uncoupled ground state in part (b)).

(b) Explain why $\Delta$ lifts the degeneracy of the two single-well ground states, splitting them by $\Delta E \approx 2\Delta$.

(c) For the ammonia molecule $\mathrm{NH}_{3}$, the nitrogen tunnels with $\gamma \approx 5$. Estimate $\Delta E/(\hbar\omega)$. Is the splitting large or small compared to a single-well excitation?

**Solution.**

**(a)** Confined to one well, the particle is a harmonic oscillator with ground-state energy $\tfrac{1}{2}\hbar\omega$. It bounces against the barrier with period $2\pi/\omega$, so each cycle makes of order one tunneling "attempt." The leaked amplitude is suppressed by $\mathrm{e}^{-\gamma}$, where $\gamma = \frac1\hbar\int_\text{barrier}\kappa\,\mathrm{d}x$ (transmission *probability* would be $\mathrm{e}^{-2\gamma}$, but the splitting is set by the tunneling *amplitude*, not its square). Multiplying the in-well energy scale $\tfrac{1}{2}\hbar\omega$ by this factor,

$$
\Delta \sim \tfrac{1}{2}\hbar\omega\,\mathrm{e}^{-\gamma}.
$$

This is the order of magnitude of the coherent coupling between the wells.

**(b)** With an impenetrable barrier the two wells are independent; each has a ground state, $\vert L\rangle$ localized in the left well and $\vert R\rangle$ in the right, **degenerate** at energy $E_{0} = \tfrac12\hbar\omega$. Tunneling provides a small matrix element coupling them. In the two-state basis $\{\vert L\rangle, \vert R\rangle\}$ the effective Hamiltonian is

$$
\hat{H} = \begin{pmatrix} E_{0} & -\Delta \\ -\Delta & E_{0} \end{pmatrix}.
$$

Diagonalizing, the eigenstates are the symmetric and antisymmetric combinations $\vert\pm\rangle = (\vert L\rangle \pm \vert R\rangle)/\sqrt{2}$ with eigenvalues

$$
E_{\pm} = E_{0} \mp \Delta.
$$

The degeneracy is lifted: the symmetric (nodeless) state is pushed **down** to $E_{0}-\Delta$, the antisymmetric (one-node) state **up** to $E_{0}+\Delta$. The energy gap between the true stationary states is

$$
\Delta E = E_{+} - E_{-} = (E_{0}+\Delta) - (E_{0}-\Delta) = 2\Delta.
$$

The localized states $\vert L\rangle, \vert R\rangle$ are not energy eigenstates once tunneling is allowed; a particle started in one well oscillates to the other and back at the angular frequency $\Delta E/\hbar = 2\Delta/\hbar$.

**(c)** With $\gamma \approx 5$ and $\Delta E \approx 2\Delta \approx \hbar\omega\,\mathrm{e}^{-\gamma}$,

$$
\frac{\Delta E}{\hbar\omega} \approx \mathrm{e}^{-\gamma} = \mathrm{e}^{-5} \approx 6.7\times 10^{-3}.
$$

The tunnel splitting is only about **$7\times 10^{-3}$ times $\hbar\omega$** — far smaller than the energy of a single-well vibrational excitation, which costs a full $\hbar\omega$. The two inversion-doublet levels of $\mathrm{NH}_{3}$ therefore sit very close together at the bottom of the double well, well separated from the next vibrational levels. (Experimentally the ammonia inversion splitting is about $24\,\text{GHz}$ against a vibrational quantum of order $30\,\text{THz}$, a ratio $\sim 10^{-3}$ — the same small order of magnitude the crude $\gamma\approx 5$ estimate produces.) The exponential factor $\mathrm{e}^{-\gamma}$ is what makes tunnel splittings tiny: even a modest barrier ($\gamma$ of a few) buries the splitting orders of magnitude below the natural oscillator scale.
