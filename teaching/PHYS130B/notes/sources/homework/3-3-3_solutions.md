# 3.3.3 Bohr-Sommerfeld Quantization
Worked solutions for the homework problems in the [3.3.3 Bohr-Sommerfeld Quantization](../ch3_path-integral/3-3-3-bohr-sommerfeld-quantization) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Harmonic oscillator.** For the harmonic oscillator $V(x) = \frac{1}{2}m\omega^{2}x^{2}$, the classical turning points at energy $E$ are $x = \pm a$ with $a = \sqrt{2E/(m\omega^{2})}$.

(a) Compute the orbit integral $\oint p\,\mathrm{d}x = 2\int_{-a}^{a}\sqrt{2m(E - \tfrac{1}{2}m\omega^{2}x^{2})}\,\mathrm{d}x$ and show that it equals $2\pi E/\omega$.

(b) Apply the Bohr-Sommerfeld rule $\oint p(x)\,\mathrm{d}x = 2\pi\hbar(n + \tfrac{1}{2})$ to derive $E_{n} = \hbar\omega(n + 1/2)$. Note that this is the exact quantum result.

**Solution.**

**(a)** At the turning points $E = \tfrac{1}{2}m\omega^{2}a^{2}$, so $E$ and $a$
are related by $2E = m\omega^{2}a^{2}$. Use this to rewrite the momentum:

$$
p(x) = \sqrt{2m\left(E - \tfrac{1}{2}m\omega^{2}x^{2}\right)}
= \sqrt{m^{2}\omega^{2}\left(a^{2} - x^{2}\right)}
= m\omega\sqrt{a^{2} - x^{2}},
$$

where the middle step used $2mE = m^{2}\omega^{2}a^{2}$. The orbit integral runs
once around the closed phase-space loop — out from $-a$ to $+a$ and back — which
is twice the line integral between the turning points:

$$
\oint p\,\mathrm{d}x = 2\int_{-a}^{a} m\omega\sqrt{a^{2}-x^{2}}\,\mathrm{d}x.
$$

The remaining integral is the area under a semicircle of radius $a$,
$\int_{-a}^{a}\sqrt{a^{2}-x^{2}}\,\mathrm{d}x = \tfrac{1}{2}\pi a^{2}$. Hence

$$
\oint p\,\mathrm{d}x = 2\,m\omega\cdot\frac{\pi a^{2}}{2} = \pi m\omega a^{2}.
$$

Finally substitute $a^{2} = 2E/(m\omega^{2})$:

$$
\oint p\,\mathrm{d}x = \pi m\omega\cdot\frac{2E}{m\omega^{2}} = \frac{2\pi E}{\omega}.
$$

**(b)** Apply the Bohr-Sommerfeld rule $\oint p\,\mathrm{d}x = 2\pi\hbar(n + \tfrac{1}{2})$ at $E = E_{n}$:

$$
\frac{2\pi E_{n}}{\omega} = 2\pi\hbar\left(n + \tfrac{1}{2}\right),
$$

so $E_{n} = \hbar\omega(n + \tfrac{1}{2})$ for $n = 0, 1, 2, \ldots$

This coincides with the **exact** quantum spectrum, zero-point energy included.
The agreement is not luck: for a quadratic potential the higher-order
($\hbar^{2}$ and beyond) corrections to the WKB phase vanish identically, so the
leading semiclassical result is already exact. The Maslov $\tfrac{1}{2}$ is
precisely what supplies the ground-state energy $\tfrac{1}{2}\hbar\omega$; without
it one would predict a vanishing zero-point energy.

<!-- ─── -->

**2. Particle in a box.** A particle of mass $m$ is confined between hard walls at $x = 0$ and $x = a$. Inside the box $V = 0$, so $p = \sqrt{2mE}$.

(a) For hard walls, the Maslov index is $\mu = 1$ per wall (versus $\mu = 1/2$ at a soft turning point), so use the generalized rule $\oint p\,\mathrm{d}x = 2\pi\hbar\bigl(n + (\mu_a+\mu_b)/2\bigr)$ with $\mu_{a} = \mu_{b} = 1$.

(b) Show that this gives $E_{n} = (n+1)^{2}\pi^{2}\hbar^{2}/(2ma^{2})$ for $n = 0, 1, 2,\ldots$, which is the exact spectrum (with the conventional relabeling $n\to n-1$).

(c) Explain physically why the hard-wall Maslov index differs from the soft case: what does the wave do at a rigid boundary versus at a smooth turning point?

**Solution.**

**(a)** Inside the box the potential is flat, so the momentum
$p = \sqrt{2mE}$ is a constant. The classical orbit is a particle bouncing wall
to wall: it travels from $x = 0$ to $x = a$ and back, so

$$
\oint p\,\mathrm{d}x = 2\int_{0}^{a} p\,\mathrm{d}x = 2\,p\,a = 2a\sqrt{2mE}.
$$

Both boundaries are hard walls, $\mu_{a} = \mu_{b} = 1$, so
$(\mu_{a}+\mu_{b})/2 = 1$ and the generalized rule $\oint p\,\mathrm{d}x = 2\pi\hbar\bigl(n + (\mu_a+\mu_b)/2\bigr)$ reads

$$
\oint p\,\mathrm{d}x = 2\pi\hbar\left(n + 1\right).
$$

**(b)** Equate the two expressions for the orbit integral:

$$
2a\sqrt{2mE_{n}} = 2\pi\hbar\,(n+1),
$$

so $\sqrt{2mE_{n}} = \pi\hbar(n+1)/a$.

Square both sides and solve for the energy:

$$
2mE_{n} = \frac{\pi^{2}\hbar^{2}(n+1)^{2}}{a^{2}},
$$

so $E_{n} = (n+1)^{2}\pi^{2}\hbar^{2}/(2ma^{2})$ for $n = 0, 1, 2, \ldots$

This is the **exact** infinite-square-well spectrum. With the conventional
relabeling $n \to n-1$ (so the ground state carries the label $1$ rather than
$0$), it takes the familiar form $E_{n} = n^{2}\pi^{2}\hbar^{2}/(2ma^{2})$ for
$n = 1, 2, 3, \ldots$ The semiclassical rule is exact here because the only
non-trivial physics is the boundary phase, which the Maslov bookkeeping captures
exactly — the interior wavefunction is a pure plane wave with no curvature
correction.

**(c)** At a **rigid wall** the potential jumps to infinity, so the wavefunction
must vanish there, $\psi = 0$. An incident wave reflects with a sign flip — a
hard node is pinned at the boundary, exactly as for a wave on a string with a
fixed end. The reflected wave is phase-shifted by a full $\pi$, which is the
content of $\mu = 1$.

At a **soft turning point** the potential is finite and smooth; $E = V$ there but
$\psi$ does **not** vanish. The wave does not reflect abruptly — it bends over
and leaks into the classically forbidden region, decaying exponentially beyond
the turning point (the Airy-function behaviour of §3.3.2). This gentle turnover
costs only half the phase: a $\pi/2$ shift, i.e. $\mu = \tfrac{1}{2}$. The
difference is precisely the difference between a wave slamming into an
impenetrable barrier and a wave easing through a smooth classical boundary.

<!-- ─── -->

**3. Linear potential.** A particle in a half-line gravitational-like potential $V(x) = Fx$ for $x \geq 0$, with a hard wall at $x = 0$.

(a) At energy $E$, find the soft turning point $x_{a} = E/F$ and compute $\int_{0}^{x_{a}}\sqrt{2m(E - Fx)}\,\mathrm{d}x = \tfrac{(2mE)^{3/2}}{3mF}$.

(b) Write the Bohr-Sommerfeld rule with the correct Maslov indices ($\mu = 1$ at the hard wall, $\mu = 1/2$ at the soft turning point) and solve for $E_{n}$.

(c) Show that the energy spacing $\Delta E_{n}$ decreases with $n$, unlike the harmonic oscillator. Why does a linear potential produce non-uniform level spacing?

**Solution.**

**(a)** At the soft turning point the particle is momentarily at rest, so all of
its energy is potential: $E = V(x_{a}) = F x_{a}$, hence

$$
x_{a} = \frac{E}{F}.
$$

For the integral, substitute $u = E - Fx$, so $\mathrm{d}u = -F\,\mathrm{d}x$;
the limits map $x = 0 \to u = E$ and $x = x_{a} \to u = 0$:

$$
\int_{0}^{x_{a}}\sqrt{2m(E - Fx)}\,\mathrm{d}x
= \frac{1}{F}\int_{0}^{E}\sqrt{2m\,u}\;\mathrm{d}u
= \frac{\sqrt{2m}}{F}\left[\frac{2}{3}u^{3/2}\right]_{0}^{E}
= \frac{2\sqrt{2m}}{3F}\,E^{3/2}.
$$

Written compactly, this is

$$
\int_{0}^{x_{a}}\sqrt{2m(E - Fx)}\,\mathrm{d}x = \frac{(2mE)^{3/2}}{3mF}.
$$

(The two forms are identical: $(2mE)^{3/2} = 2m\sqrt{2m}\,E^{3/2}$, so dividing
by $3mF$ leaves $\tfrac{2\sqrt{2m}}{3F}E^{3/2}$. The compact form
$\tfrac{(2mE)^{3/2}}{3mF}$ is the one quoted in the problem statement, and is
the value used in parts (b) and (c).)

**(b)** The classical orbit is a particle launched up the ramp, decelerating to
rest at $x_{a}$, and falling back to bounce off the hard wall at $x = 0$. The
orbit integral covers the up-and-back trip:

$$
\oint p\,\mathrm{d}x = 2\int_{0}^{x_{a}}\sqrt{2m(E - Fx)}\,\mathrm{d}x
= \frac{4\sqrt{2m}}{3F}\,E^{3/2}.
$$

The two boundaries are different: a hard wall at $x = 0$ ($\mu_{a} = 1$) and a
soft turning point at $x_{a}$ ($\mu_{b} = \tfrac{1}{2}$). The Maslov term is
$(\mu_{a}+\mu_{b})/2 = (1 + \tfrac{1}{2})/2 = \tfrac{3}{4}$, so the generalized
rule $\oint p\,\mathrm{d}x = 2\pi\hbar\bigl(n + (\mu_a+\mu_b)/2\bigr)$ is

$$
\frac{4\sqrt{2m}}{3F}\,E_{n}^{3/2} = 2\pi\hbar\left(n + \tfrac{3}{4}\right).
$$

Solve for $E_{n}$:

$$
E_{n}^{3/2} = \frac{3\pi\hbar F}{2\sqrt{2m}}\left(n + \tfrac{3}{4}\right),
$$

so $E_{n} = (9\pi^{2}\hbar^{2}F^{2}/(8m))^{1/3}(n + \tfrac{3}{4})^{2/3}$ for $n = 0, 1, 2, \ldots$

The energy levels scale as $E_{n} \propto (n + 3/4)^{2/3}$ — the characteristic
$n^{2/3}$ growth of a linear potential.

**(c)** Because $E_{n} \propto (n + 3/4)^{2/3}$ with exponent $2/3 < 1$, the
spectrum is **concave** in $n$. The spacing is the discrete derivative; for large
$n$,

$$
\Delta E_{n} = E_{n+1} - E_{n}
\approx \frac{\mathrm{d}E_{n}}{\mathrm{d}n}
= \frac{2}{3}\left(\frac{9\pi^{2}\hbar^{2}F^{2}}{8m}\right)^{1/3}
\left(n + \tfrac{3}{4}\right)^{-1/3},
$$

which **decreases** as $n^{-1/3}$. The harmonic oscillator, by contrast, has
$E_{n} \propto n$ exactly, so its spacing $\hbar\omega$ is constant.

The physical reason is the classical orbital period. In the semiclassical regime
the level spacing equals $\hbar$ times the classical orbital frequency,
$\Delta E_{n} \approx \hbar\,\omega_\text{cl}(E_{n})$ — indeed
$\mathrm{d}(\oint p\,\mathrm{d}x)/\mathrm{d}E$ is exactly the orbital period. For
the harmonic oscillator the period is independent of amplitude (isochronism), so
$\omega_\text{cl}$ and hence $\Delta E$ are energy-independent. For the linear
ramp the turning point $x_{a} = E/F$ recedes as the energy grows, the orbit gets
longer, and the period lengthens (one finds $\omega_\text{cl} \propto E^{-1/2}$).
A slower orbit means a smaller energy quantum, so the levels crowd together at
high $n$.

<!-- ─── -->

**4. Anharmonic oscillator.** Consider $V(x) = \tfrac{1}{2}m\omega^{2}x^{2} + \lambda x^{4}$ with $\lambda > 0$ small.

(a) Explain qualitatively why the quartic term steepens the potential at large $\vert x\vert$, shrinking the classical turning points compared to the pure harmonic case at the same energy.

(b) Argue that the orbit integral $\oint p\,\mathrm{d}x$ is therefore smaller than for the harmonic oscillator at the same energy, so Bohr-Sommerfeld predicts higher energy levels. Are the energy spacings larger or smaller than $\hbar\omega$?

(c) For which regime (low $n$ or high $n$) is the quartic correction most important? Use the ratio $\lambda x^{4}/(\tfrac{1}{2}m\omega^{2}x^{2})$ at the turning point.

**Solution.**

**(a)** The added term $\lambda x^{4}$ is strictly positive for $x \neq 0$ (since
$\lambda > 0$), and it grows faster than the quadratic part: the ratio
$\lambda x^{4}/(\tfrac{1}{2}m\omega^{2}x^{2}) = 2\lambda x^{2}/(m\omega^{2})$
increases without bound as $\vert x\vert$ grows. So at large displacement the
quartic well sits **above** the pure harmonic well. The classical turning point
is where $V(x_{t}) = E$; since the anharmonic potential reaches the value $E$
sooner — at a smaller $\vert x\vert$ — its turning points $\pm x_{t}$ lie inside
the harmonic turning points $\pm a$ for the same energy $E$. The quartic wall
"catches" the particle earlier.

**(b)** The orbit integral
$\oint p\,\mathrm{d}x = 2\int_{-x_{t}}^{x_{t}}\sqrt{2m(E - V)}\,\mathrm{d}x$
is reduced by the quartic term in two reinforcing ways: the integration range
$[-x_{t}, x_{t}]$ is narrower (part (a)), and at every interior point the
potential is higher, so $E - V$ is smaller and the integrand $\sqrt{2m(E-V)}$ is
smaller. Both effects shrink the integral, so at a fixed energy $E$

$$
\oint p\,\mathrm{d}x\,\Big\vert_\text{anharmonic} < \oint p\,\mathrm{d}x\,\Big\vert_\text{harmonic}
= \frac{2\pi E}{\omega}.
$$

Now read the Bohr-Sommerfeld rule the other way around. The right-hand side
$2\pi\hbar(n+\tfrac{1}{2})$ is fixed by the quantum number $n$. Since the
anharmonic orbit integral accumulates more slowly with energy, a **larger** $E$
is needed to reach the same value $2\pi\hbar(n+\tfrac{1}{2})$. Hence
$E_{n}^\text{anh} > \hbar\omega(n+\tfrac{1}{2})$ — every level is pushed up.

For the spacing, recall $\mathrm{d}(\oint p\,\mathrm{d}x)/\mathrm{d}E$ is the
classical period $T(E)$, so $\Delta E_{n} \approx 2\pi\hbar/T(E_{n})$. The quartic
term stiffens the restoring force ($-V' = -m\omega^{2}x - 4\lambda x^{3}$ is
stronger than harmonic), so the oscillation is faster: $T < 2\pi/\omega$ and
shrinks further as the amplitude grows. Therefore the spacings are **larger than
$\hbar\omega$**, and they increase with $n$. A harder-than-quadratic well always
has a widening spectrum (the extreme case being the box, $E_{n}\propto n^{2}$).

**(c)** The relative size of the quartic correction is measured at the turning
point, where the displacement is largest:

$$
\frac{\lambda x_{t}^{4}}{\tfrac{1}{2}m\omega^{2}x_{t}^{2}}
= \frac{2\lambda x_{t}^{2}}{m\omega^{2}}.
$$

To leading order the turning point satisfies
$\tfrac{1}{2}m\omega^{2}x_{t}^{2} \approx E$, i.e.
$x_{t}^{2} \approx 2E/(m\omega^{2})$, so the ratio becomes

$$
\frac{2\lambda x_{t}^{2}}{m\omega^{2}} \approx \frac{4\lambda E}{m^{2}\omega^{4}}
\;\propto\; E \;\propto\; n.
$$

The ratio grows with the energy and hence with the quantum number. The quartic
correction is therefore **negligible at low $n$** — near the bottom of the well
the amplitude is tiny and the potential is effectively harmonic — and **most
important at high $n$**, where the large-amplitude orbit explores the steep
quartic walls. This is why anharmonic corrections to molecular vibrational
spectra show up as a progressive widening (or, for softer wells, narrowing) of
the level spacing at higher excitation.

<!-- ─── -->

**5. Two-dimensional anisotropic oscillator.** A particle moves in $V(x,y) = \tfrac{1}{2}m\omega_{x}^{2}x^{2} + \tfrac{1}{2}m\omega_{y}^{2}y^{2}$ with $\omega_{x} \neq \omega_{y}$.

(a) The motion separates: $x$ and $y$ each oscillate independently. Apply Bohr-Sommerfeld to each direction to derive $E_{n_{x},n_{y}} = \hbar\omega_{x}(n_{x} + \tfrac{1}{2}) + \hbar\omega_{y}(n_{y} + \tfrac{1}{2})$.

(b) For $\omega_{x} = 2\omega_{y} = 2\omega$, list the first five distinct energy levels in units of $\hbar\omega$ and identify any degeneracies.

(c) The same construction fails for *non-separable* (in particular *chaotic*) potentials. In one sentence, explain why the rule "quantize each closed action variable independently" requires the system to be integrable (as many conserved quantities as degrees of freedom).

**Solution.**

**(a)** The potential is a sum of an $x$-part and a $y$-part, and the kinetic
energy splits the same way, $H = H_{x} + H_{y}$ with
$H_{x} = p_{x}^{2}/2m + \tfrac{1}{2}m\omega_{x}^{2}x^{2}$ and likewise for $y$.
The two coordinates do not couple, so the total energy partitions as
$E = E_{x} + E_{y}$, and each coordinate executes an independent 1D harmonic
oscillation with its own conserved energy. Bohr-Sommerfeld applies separately to
each closed loop in the $(x,p_{x})$ and $(y,p_{y})$ planes. Each is a 1D harmonic
oscillator with two soft turning points, so by Problem 1,

$$
E_{x} = \hbar\omega_{x}\left(n_{x} + \tfrac{1}{2}\right), \qquad
E_{y} = \hbar\omega_{y}\left(n_{y} + \tfrac{1}{2}\right).
$$

Adding the two independently quantized pieces,

$$
E_{n_{x},n_{y}} = \hbar\omega_{x}\left(n_{x} + \tfrac{1}{2}\right)
+ \hbar\omega_{y}\left(n_{y} + \tfrac{1}{2}\right),
\qquad n_{x}, n_{y} = 0, 1, 2, \ldots
$$

**(b)** With $\omega_{x} = 2\omega$ and $\omega_{y} = \omega$,

$$
E_{n_{x},n_{y}} = 2\hbar\omega\left(n_{x}+\tfrac{1}{2}\right)
+ \hbar\omega\left(n_{y}+\tfrac{1}{2}\right)
= \hbar\omega\left(2n_{x} + n_{y} + \tfrac{3}{2}\right).
$$

So the energy in units of $\hbar\omega$ is $2n_{x} + n_{y} + \tfrac{3}{2}$.
Enumerating $(n_{x}, n_{y})$:

| $E/\hbar\omega$ | states $(n_{x},n_{y})$ | degeneracy |
|---|---|---|
| $3/2$  | $(0,0)$ | 1 |
| $5/2$  | $(0,1)$ | 1 |
| $7/2$  | $(1,0),\ (0,2)$ | 2 |
| $9/2$  | $(1,1),\ (0,3)$ | 2 |
| $11/2$ | $(2,0),\ (1,2),\ (0,4)$ | 3 |

The first five distinct levels are
$\tfrac{3}{2}, \tfrac{5}{2}, \tfrac{7}{2}, \tfrac{9}{2}, \tfrac{11}{2}$
(in units of $\hbar\omega$). Degeneracies appear
from the third level upward: distinct $(n_{x},n_{y})$ pairs give the same energy
because $2n_{x} + n_{y}$ can be reached in several ways once it is $\geq 2$. This
is a consequence of the **commensurate** (rational-ratio) frequencies
$\omega_{x}:\omega_{y} = 2:1$; for an irrational ratio every level would be
non-degenerate.

**(c)** Quantizing "each closed action variable independently" presupposes that
the phase-space motion winds around invariant tori on which each action
$\oint p_{i}\,\mathrm{d}q_{i}$ is separately well-defined and conserved — and that
requires the system to be **integrable**, i.e. to possess as many independent
conserved quantities as degrees of freedom; a chaotic (non-integrable) system
has too few constants of motion, its trajectories fill phase-space regions
ergodically rather than lying on tori, and no global action variables exist to
quantize.

<!-- ─── -->

**6. Hydrogen atom (circular orbits).** For the Coulomb potential $V(r) = -q_{e}^{2}/(4\pi\epsilon_{0}r)$, consider circular orbits with angular momentum $L = n_{\varphi}\hbar$.

(a) From the force balance $mv^{2}/r = q_{e}^{2}/(4\pi\epsilon_{0}r^{2})$ and $L = mvr = n_{\varphi}\hbar$, show that $r_{n_{\varphi}} = n_{\varphi}^{2}a_{0}$ where $a_{0} = 4\pi\epsilon_{0}\hbar^{2}/(m q_{e}^{2})$ is the Bohr radius.

(b) Use the virial theorem ($E = -T = V/2$ for the Coulomb potential) to derive $E_{n_{\varphi}} = -13.6\,\text{eV}/n_{\varphi}^{2}$.

(c) Adding the radial Bohr-Sommerfeld quantization with a radial quantum number $n_{r}$ promotes $n_{\varphi}$ to $n = n_{r} + n_{\varphi}$. Explain why this reproduces the same formula $E_{n} = -13.6\,\text{eV}/n^{2}$ with additional degeneracy.

**Solution.**

**(a)** The angular-momentum quantization $L = mvr = n_{\varphi}\hbar$ fixes the
speed in terms of the radius, $v = n_{\varphi}\hbar/(mr)$. The force balance for a
circular orbit (Coulomb attraction supplies the centripetal force) is

$$
\frac{mv^{2}}{r} = \frac{q_{e}^{2}}{4\pi\epsilon_{0}r^{2}},
$$

so $mv^{2} = q_{e}^{2}/(4\pi\epsilon_{0}r)$.

Substitute $v = n_{\varphi}\hbar/(mr)$ into the left-hand side:

$$
m\cdot\frac{n_{\varphi}^{2}\hbar^{2}}{m^{2}r^{2}} = \frac{q_{e}^{2}}{4\pi\epsilon_{0}r},
$$

so $n_{\varphi}^{2}\hbar^{2}/(m\,r) = q_{e}^{2}/(4\pi\epsilon_{0})$.

Solving for $r$,

$$
r_{n_{\varphi}} = \frac{4\pi\epsilon_{0}\,n_{\varphi}^{2}\hbar^{2}}{m\,q_{e}^{2}}
= n_{\varphi}^{2}\,a_{0},
\qquad
a_{0} \equiv \frac{4\pi\epsilon_{0}\hbar^{2}}{m\,q_{e}^{2}}.
$$

The allowed circular radii grow as $n_{\varphi}^{2}$, in units of the Bohr radius
$a_{0}$.

**(b)** For a circular orbit the kinetic energy is
$T = \tfrac{1}{2}mv^{2}$, and the force balance of part (a) gives
$mv^{2} = q_{e}^{2}/(4\pi\epsilon_{0}r)$, so

$$
T = \frac{1}{2}mv^{2} = \frac{q_{e}^{2}}{8\pi\epsilon_{0}r}
= -\frac{1}{2}V(r),
$$

which is the virial relation for the Coulomb ($\propto 1/r$) potential. The total
energy is then

$$
E = T + V = -\tfrac{1}{2}V + V = \tfrac{1}{2}V(r_{n_{\varphi}})
= -\frac{q_{e}^{2}}{8\pi\epsilon_{0}\,r_{n_{\varphi}}}
= -\frac{q_{e}^{2}}{8\pi\epsilon_{0}\,a_{0}}\cdot\frac{1}{n_{\varphi}^{2}}.
$$

The prefactor is the Rydberg energy. Substituting
$a_{0} = 4\pi\epsilon_{0}\hbar^{2}/(m q_{e}^{2})$,

$$
\frac{q_{e}^{2}}{8\pi\epsilon_{0}\,a_{0}}
= \frac{m\,q_{e}^{4}}{2(4\pi\epsilon_{0})^{2}\hbar^{2}}
\approx 13.6\,\text{eV},
$$

so that

$$
E_{n_{\varphi}} = -\frac{13.6\,\text{eV}}{n_{\varphi}^{2}},
\qquad n_{\varphi} = 1, 2, 3, \ldots
$$

**(c)** Circular orbits are only the special case of zero radial motion. A general bound orbit is an ellipse on which $r$ also oscillates between a perihelion $r_{-}$ and an aphelion $r_{+}$ — two soft turning points. The radial libration carries its own action, which must be separately quantized. To carry this out, use the conserved angular momentum $L = n_{\varphi}\hbar$ to eliminate the angular degree of freedom from the energy. With $k \equiv q_{e}^{2}/(4\pi\epsilon_{0})$,

$$
E = \frac{p_{r}^{2}}{2m} + \frac{L^{2}}{2mr^{2}} - \frac{k}{r},
\qquad
p_{r}(r) = \sqrt{\,2m\!\left(E + \frac{k}{r}\right) - \frac{L^{2}}{r^{2}}\,}.
$$

For bound motion $E < 0$; write $\vert E\vert = -E > 0$. The turning points are the roots of $p_{r} = 0$, equivalently $-2m\vert E\vert r^{2} + 2mk\,r - L^{2} = 0$:

$$
r_{\pm} = \frac{k \pm \sqrt{k^{2} - 2\vert E\vert L^{2}/m}}{2\vert E\vert},
\qquad
r_{+} + r_{-} = \frac{k}{\vert E\vert},
\qquad
r_{+}\,r_{-} = \frac{L^{2}}{2m\vert E\vert}.
$$

Factor the radicand using these roots,

$$
-2m\vert E\vert + \frac{2mk}{r} - \frac{L^{2}}{r^{2}} = \frac{2m\vert E\vert\,(r_{+} - r)(r - r_{-})}{r^{2}},
$$

so

$$
p_{r}(r) = \frac{\sqrt{2m\vert E\vert}}{r}\,\sqrt{(r_{+} - r)(r - r_{-})}.
$$

The radial action is then

$$
\oint p_{r}\,\mathrm{d}r = 2\int_{r_{-}}^{r_{+}} p_{r}\,\mathrm{d}r = 2\sqrt{2m\vert E\vert}\,\int_{r_{-}}^{r_{+}} \frac{\sqrt{(r_{+} - r)(r - r_{-})}}{r}\,\mathrm{d}r.
$$

The remaining integral has the closed-form value (Sommerfeld 1916; verifiable by the substitution $r = \tfrac{1}{2}(r_{+}+r_{-}) - \tfrac{1}{2}(r_{+}-r_{-})\cos\theta$, or by contour methods),

$$
\int_{r_{-}}^{r_{+}} \frac{\sqrt{(r_{+} - r)(r - r_{-})}}{r}\,\mathrm{d}r = \pi\!\left(\frac{r_{+} + r_{-}}{2} - \sqrt{r_{+}\,r_{-}}\right).
$$

Substituting the values of $r_{+} + r_{-}$ and $r_{+}r_{-}$,

$$
\begin{split}
\oint p_{r}\,\mathrm{d}r &= 2\sqrt{2m\vert E\vert}\cdot \pi\!\left(\frac{k}{2\vert E\vert} - \frac{L}{\sqrt{2m\vert E\vert}}\right)\\
&= 2\pi\!\left(k\sqrt{\frac{m}{2\vert E\vert}} - L\right).
\end{split}
$$

Now apply Bohr-Sommerfeld separately to the two periodic motions. The angular motion is a *ring* (no turning points, $\mu_{\varphi} = 0$), so $\oint p_{\varphi}\,\mathrm{d}\varphi = 2\pi L = 2\pi n_{\varphi}\hbar$ — already used. The radial motion has two soft turning points; we take its quantization in the old-Sommerfeld form $\oint p_{r}\,\mathrm{d}r = 2\pi n_{r}\hbar$ with $n_{r} = 0,1,2,\ldots$ (see remark below on Maslov bookkeeping). Then

$$
2\pi\!\left(k\sqrt{\frac{m}{2\vert E\vert}} - n_{\varphi}\hbar\right) = 2\pi n_{r}\hbar,
$$

so $k\sqrt{m/(2\vert E\vert)} = (n_{r} + n_{\varphi})\,\hbar \equiv n\,\hbar$.

The radial and angular quantum numbers enter the energy *only through their sum* $n$. Squaring and solving,

$$
\vert E\vert = \frac{m k^{2}}{2 n^{2}\hbar^{2}} = \frac{1}{n^{2}}\cdot\frac{m q_{e}^{4}}{2(4\pi\epsilon_{0})^{2}\hbar^{2}} \approx \frac{13.6\,\text{eV}}{n^{2}},
\qquad
E_{n} = -\frac{13.6\,\text{eV}}{n^{2}}.
$$

This is the same prefactor as in part (b), but now $n = n_{r} + n_{\varphi}$ plays the role of the principal quantum number.

**Why energy depends only on the sum.** The Coulomb $1/r$ potential is the unique attractive central potential (together with the isotropic harmonic oscillator) whose bound orbits *close* — every classical orbit retraces itself after one period. The radial and angular motions therefore share a common period, and the energy is fixed by the **semi-major axis** of the Kepler ellipse alone, independent of eccentricity. Different splittings $(n_{r},n_{\varphi})$ at fixed $n$ correspond to orbits of different eccentricities (nearly circular: $n_{\varphi}\approx n$, $n_{r}\approx 0$; thin elongated ellipse: $n_{\varphi}$ small, $n_{r}$ large), but they share the same semi-major axis and hence the same energy. Each level $n$ therefore acquires a **degeneracy** $n_{\varphi} = 1, 2, \ldots, n$ (with $n_{r} = n - n_{\varphi} \ge 0$). This semiclassical degeneracy is the shadow of the exact $n^{2}$-fold hydrogen degeneracy, ultimately traced to the hidden $\mathrm{SO}(4)$ symmetry of the $1/r$ potential.

**Remark on Maslov bookkeeping.** Two soft radial turning points would naively contribute a $+\tfrac{1}{2}$ Maslov correction, giving $\oint p_{r}\,\mathrm{d}r = 2\pi\hbar(n_{r} + \tfrac{1}{2})$. For 3D radial WKB, however, an additional **Langer correction** shifts the effective angular momentum entering $p_{r}$ from $L = n_{\varphi}\hbar$ to $L_\text{eff} = (n_{\varphi} + \tfrac{1}{2})\hbar$. The two half-integer shifts cancel in the combination $k\sqrt{m/(2\vert E\vert)} = (n_{r}+\tfrac{1}{2}) + (n_{\varphi}+\tfrac{1}{2})\hbar = (n_{r}+n_{\varphi}+1)\hbar$, restoring the integer principal quantum number $n = n_{r}+n_{\varphi}+1 \ge 1$ and the same $E_{n}$. The old-Sommerfeld bookkeeping used above is the cleanest route; either accounting reproduces the exact hydrogen spectrum, a coincidence special to the $1/r$ potential.

<!-- ─── -->

**7. Correspondence principle.** In the classical limit ($n \gg 1$), the energy spacing $\Delta E = E_{n+1} - E_{n}$ should equal $\hbar\omega_\text{cl}$, where $\omega_\text{cl}$ is the classical orbital frequency.

(a) For the harmonic oscillator, verify $\Delta E = \hbar\omega$ for all $n$.

(b) For a power-law potential $V(x) = C\vert x\vert^{\alpha}$, Bohr-Sommerfeld gives $E_{n} \propto n^{2\alpha/(\alpha+2)}$. Show that $\Delta E/E_{n}\to 0$ as $n\to\infty$, so the spectrum becomes quasi-continuous in the classical limit.

(c) For hydrogen ($E_{n}\propto -1/n^{2}$), compute the classical orbital frequency $\omega_\text{cl} = \Delta E/\hbar$ at large $n$ and show it scales as $n^{-3}$. This is the radiation frequency in transitions between adjacent high-$n$ Rydberg levels.

**Solution.**

**(a)** From Problem 1, $E_{n} = \hbar\omega(n + \tfrac{1}{2})$, so

$$
\Delta E = E_{n+1} - E_{n}
= \hbar\omega\left(n + \tfrac{3}{2}\right) - \hbar\omega\left(n + \tfrac{1}{2}\right)
= \hbar\omega.
$$

The spacing is exactly $\hbar\omega$ for every $n$, not merely asymptotically.
This matches the classical orbital frequency: a harmonic oscillator is
isochronous, oscillating at $\omega$ regardless of amplitude, so
$\omega_\text{cl} = \omega$ at all energies and $\Delta E = \hbar\omega_\text{cl}$
holds for the harmonic oscillator down to the ground state.

**(b)** Write $E_{n} = A\,n^{\beta}$ with $\beta = 2\alpha/(\alpha+2)$. Since
$\alpha > 0$, the exponent satisfies $0 < \beta < 2$; in particular $\beta < 2$,
and for any potential softer than the box $\beta$ is finite. (Sketch of the
scaling: the turning point obeys $C x_{t}^{\alpha} = E$, so
$x_{t}\propto E^{1/\alpha}$; rescaling $x = x_{t}u$ in
$\oint p\,\mathrm{d}x = 4\int_{0}^{x_{t}}\sqrt{2m(E - Cx^{\alpha})}\,\mathrm{d}x$
factors out $\sqrt{E}\,x_{t}\propto E^{1/2+1/\alpha}$, and Bohr-Sommerfeld sets
this $\propto n$, giving $E\propto n^{2\alpha/(\alpha+2)}$.)

For large $n$ the spacing is the discrete derivative,

$$
\Delta E = E_{n+1} - E_{n} \approx \frac{\mathrm{d}E_{n}}{\mathrm{d}n}
= A\beta\,n^{\beta-1}.
$$

The relative spacing is therefore

$$
\frac{\Delta E}{E_{n}} \approx \frac{A\beta\,n^{\beta-1}}{A\,n^{\beta}}
= \frac{\beta}{n} \;\xrightarrow[n\to\infty]{}\; 0.
$$

So although the absolute spacing $\Delta E$ may grow ($\beta > 1$), constant
($\beta = 1$), or shrink ($\beta < 1$), the **fractional** spacing always
vanishes as $1/n$. At high quantum numbers neighbouring levels are
indistinguishable on the scale of the energy itself: the spectrum becomes
**quasi-continuous**, exactly as a classical particle with continuously variable
energy would have. This is the correspondence principle — quantum discreteness
fades into the classical continuum as $n\to\infty$.

**(c)** For hydrogen, $E_{n} = -\text{Ry}/n^{2}$ with $\text{Ry} = 13.6\,\text{eV}$.
The spacing at large $n$ is

$$
\Delta E = E_{n+1} - E_{n} \approx \frac{\mathrm{d}E_{n}}{\mathrm{d}n}
= \frac{\mathrm{d}}{\mathrm{d}n}\left(-\frac{\text{Ry}}{n^{2}}\right)
= \frac{2\,\text{Ry}}{n^{3}}.
$$

The classical orbital frequency predicted by the correspondence principle is then

$$
\omega_\text{cl} = \frac{\Delta E}{\hbar} = \frac{2\,\text{Ry}}{\hbar\,n^{3}}
\;\propto\; n^{-3}.
$$

This $n^{-3}$ scaling is exactly the Kepler result: the orbital radius grows as
$r_{n}\propto n^{2}$ (Problem 6a), and Kepler's third law for a $1/r$ potential
gives a period $T\propto r^{3/2}\propto n^{3}$, hence
$\omega_\text{cl} = 2\pi/T\propto n^{-3}$. A Rydberg electron in a high-$n$ state
orbits slowly, and when it drops to the adjacent level $n \to n-1$ it radiates a
photon of frequency $\omega \approx \omega_\text{cl}$ — the quantum transition
frequency between adjacent high-$n$ levels coincides with the classical orbital
frequency. This agreement between the quantum emission spectrum and classical
electrodynamics is the original setting in which Bohr stated the correspondence
principle.
