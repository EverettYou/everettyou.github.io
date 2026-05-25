# 3.1.3 Wave-Particle Duality
Worked solutions for the homework problems in the [3.1.3 Wave-Particle Duality](../ch3_path-integral/3-1-3-wave-particle-duality) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Free particle action.** A free particle has action $S = \boldsymbol{p}\cdot\boldsymbol{r} - Et$ with $E = p^2/(2m)$. Write down $\psi = A\,\mathrm{e}^{\mathrm{i}S/\hbar}$ and identify the wavelength and frequency in terms of $p$ and $E$. Verify the de Broglie relations.

**Solution.**

*The wavefunction.* Substituting the free-particle action into $\psi = A\,\mathrm{e}^{\mathrm{i}S/\hbar}$,

$$
\psi(\boldsymbol{r}, t) = A\,\exp\!\left[\frac{\mathrm{i}}{\hbar}\left(\boldsymbol{p}\cdot\boldsymbol{r} - Et\right)\right].
$$

This is a plane wave: the surfaces of constant phase are the planes $\boldsymbol{p}\cdot\boldsymbol{r} = \text{const}$, perpendicular to $\boldsymbol{p}$, and they march forward along the $\boldsymbol{p}$ direction as $t$ increases.

*Reading off wave vector and angular frequency.* A plane matter wave is written in the standard form $\psi \propto \mathrm{e}^{\mathrm{i}(\boldsymbol{k}\cdot\boldsymbol{r} - \omega t)}$. Matching the exponent term by term against the expression above,

$$
\boldsymbol{k} = \frac{\boldsymbol{p}}{\hbar}, \qquad \omega = \frac{E}{\hbar}.
$$

*Wavelength and frequency.* The wavelength is fixed by the magnitude of the wave vector, and the (ordinary) frequency by the angular frequency:

$$
\lambda = \frac{2\pi}{k} = \frac{2\pi\hbar}{p} = \frac{h}{p}, \qquad f = \frac{\omega}{2\pi} = \frac{E}{2\pi\hbar} = \frac{E}{h},
$$

where $h = 2\pi\hbar$ is Planck's constant.

*Verifying de Broglie.* The de Broglie relations are $\boldsymbol{p} = \hbar\boldsymbol{k}$ and $E = \hbar\omega$. They drop straight out of the matching step above — they are not additional assumptions but exactly the statement that the *particle* labels $(\boldsymbol{p}, E)$ appearing in the action are the *wave* labels $(\boldsymbol{k}, \omega)$ once the phase is measured in units of $\hbar$. Equivalently $\lambda = h/p$ and $f = E/h$ are the de Broglie relations rewritten for wavelength and frequency. The content of "the phase of the matter wave is the classical action over $\hbar$" is precisely that these identifications hold. $\checkmark$

*Consistency check — the dispersion relation.* Using $E = p^2/(2m)$,

$$
\omega = \frac{E}{\hbar} = \frac{p^2}{2m\hbar} = \frac{\hbar k^2}{2m},
$$

the familiar non-relativistic matter-wave dispersion relation $\omega \propto k^2$. (Contrast a light wave, where $\omega \propto k$.)

<!-- ─── -->

**2. De Broglie wavelength.** An electron is accelerated through a potential difference of $V = 100$ V. Compute its de Broglie wavelength. Compare this to the lattice spacing of a typical crystal ($\sim 0.3$ nm). Why does this make electron diffraction possible?

**Solution.**

*Kinetic energy gained.* An electron of charge magnitude $e$ accelerated from rest through a potential difference $V$ gains kinetic energy

$$
E_k = eV = (1.602\times10^{-19}\,\text{C})(100\,\text{V}) = 1.602\times10^{-17}\,\text{J} = 100\,\text{eV}.
$$

*Check that the motion is non-relativistic.* Compare with the electron rest energy $m_e c^2 \approx 511\,\text{keV}$: the ratio $E_k/(m_e c^2) \approx 100/(5.11\times10^5) \approx 2\times10^{-4} \ll 1$. The electron is firmly non-relativistic, so the relation $E_k = p^2/(2m_e)$ applies and relativistic corrections to $\lambda$ are at the $0.01\%$ level.

*Momentum.*

$$
p = \sqrt{2 m_e E_k} = \sqrt{2\,(9.109\times10^{-31}\,\text{kg})(1.602\times10^{-17}\,\text{J})} = 5.40\times10^{-24}\,\mathrm{kg\cdot m/s}.
$$

*De Broglie wavelength.*

$$
\lambda = \frac{h}{p} = \frac{6.626\times10^{-34}\,\mathrm{J\cdot s}}{5.40\times10^{-24}\,\mathrm{kg\cdot m/s}} \approx 1.23\times10^{-10}\,\text{m} = 0.123\,\text{nm}.
$$

A convenient shortcut packages the constants once and for all: for a non-relativistic electron with $V$ in volts, $\lambda \approx 1.226\,\mathrm{nm}/\sqrt{V}$, which gives $1.226/\sqrt{100} = 0.123$ nm — the same answer.

*Why this enables diffraction.* Diffraction from a periodic structure is appreciable only when the probe wavelength is comparable to the period of the structure. Here $\lambda \approx 0.12$ nm is the same order of magnitude as the crystal lattice spacing $d \approx 0.3$ nm ($\lambda/d \approx 0.4$). The regularly spaced atomic planes then act as a diffraction grating for the electron's matter wave: waves scattered from successive planes interfere, and they add constructively at the Bragg angles set by $2d\sin\theta = m\lambda$, producing sharp diffraction peaks.

The comparison is what matters. If $\lambda \gg d$, the grating would be far too fine to resolve and no orders beyond the straight-through beam would appear. If $\lambda \ll d$, the wave would behave like a classical ray (the geometric-optics limit) and pass through with no interference pattern. Because a $100$ V accelerating voltage places $\lambda$ squarely in the $\sim 0.1$ nm window, comparable to atomic spacings, electron diffraction off crystals is observable. This is exactly the Davisson–Germer experiment (1927), the first direct confirmation of de Broglie's matter waves.

<!-- ─── -->

**3. Optics-mechanics translation.** In a medium with spatially varying refractive index $n(\boldsymbol{x})$, a light ray bends according to Snell's law: $n(\boldsymbol{x})\sin\theta(\boldsymbol{x}) = \text{const}$, where $\theta$ is the angle to the normal. Using the optics-mechanics analogy from the lecture, translate this into a statement about a classical particle in a potential $V(\boldsymbol{x})$. What is the mechanical analogue of the refractive index?

**Solution.**

*The optical statement, restated.* In a medium the local wave number is $k = n k_0$, so the magnitude of a light ray's "momentum" $\hbar k$ is proportional to the refractive index $n$. Snell's law $n\sin\theta = \text{const}$ is then the statement that, at an interface across which $n$ varies, the component of the ray momentum *tangent to the interface* is conserved — there is no phase gradient along the interface to deflect that component. The conserved quantity is $n\sin\theta$.

*The mechanical dictionary.* In the optics-mechanics analogy the optical path length $L = \int n\,\mathrm{d}s$ corresponds to the *abbreviated action* $W = \int p\,\mathrm{d}s$ for a particle at fixed total energy. Comparing the two integrands identifies the mechanical analogue of the refractive index as the magnitude of the particle momentum:

$$
n(\boldsymbol{x}) \;\longleftrightarrow\; p(\boldsymbol{x}) = \sqrt{2m\big(E - V(\boldsymbol{x})\big)},
$$

where the last form uses energy conservation $E = p^2/(2m) + V(\boldsymbol{x})$ for a particle of fixed total energy $E$. So a particle moving through a potential $V(\boldsymbol{x})$ behaves like a light ray in a medium of refractive index

$$
n_{\text{mech}}(\boldsymbol{x}) \propto \sqrt{E - V(\boldsymbol{x})}.
$$

A low potential means large momentum and hence a high effective index; a high potential means small momentum and a low index.

*Mechanical Snell's law.* Consider a particle crossing a region where $V$ changes only along one direction — a potential step — so that the surface of constant $V$ is a flat "interface". The force $-\nabla V$ is then normal to that interface, so it changes only the normal component of momentum; the tangential component is conserved. Writing $\theta$ for the angle between the trajectory and the interface normal,

$$
p\sin\theta = \text{const},
$$

i.e. $\sqrt{2m(E - V)}\,\sin\theta = \text{const}$.

This is the mechanical Snell's law — identical in form to $n\sin\theta = \text{const}$ with the replacement $n \to \sqrt{2m(E-V)}$. A particle "refracts" at a potential step: dropping into a region of lower $V$ it speeds up and bends *toward* the normal, exactly as a light ray entering a higher-index medium bends toward the normal.

*Historical aside.* This is precisely Newton's corpuscular picture of refraction, in which the index tracks the particle's *speed*: for a massive particle $n_{\text{mech}} \propto p \propto v$. For light the wave theory is correct and the index runs the opposite way, $n \propto 1/v_{\text{phase}}$ — which is why Newton's prediction that light speeds up in glass was eventually overturned by experiment. The optics-mechanics analogy is nonetheless exact for genuine massive particles, and it is the seed of the path-integral and WKB pictures developed later in this chapter.

<!-- ─── -->

**4. Dimensions of action.** The quantum wavefunction is $\psi = A\,\mathrm{e}^{\mathrm{i}S/\hbar}$.

(a) What are the dimensions of $S$? What are the dimensions of $S/\hbar$? Why must the exponent be dimensionless?

(b) A classical baseball ($m = 0.15$ kg) is thrown at $v = 30$ m/s across a distance $d = 10$ m. Estimate its action $S \sim mvd$ and compute $S/\hbar$. What does the enormous size of this ratio imply for whether quantum interference is observable?

(c) An electron ($m = 9.1 \times 10^{-31}$ kg) moves at $v = 10^6$ m/s across $d = 1$ nm. Compute $S/\hbar$. Why is quantum behavior now important?

**Solution.**

**(a) Dimensions.** Action is defined as $S = \int L_{\mathrm{mech}}\,\mathrm{d}t$ with the Lagrangian $L_{\mathrm{mech}}$ an energy, so

$$
[S] = \text{energy}\times\text{time} = \mathrm{J\cdot s} = \mathrm{kg\cdot m^2\cdot s^{-1}}.
$$

Equivalently, from $S = \boldsymbol{p}\cdot\boldsymbol{r} - Et$ the action is also momentum × length, which carries the same units ($\mathrm{kg\cdot m\cdot s^{-1}}\times\text{m}$). Planck's constant $\hbar$ has exactly these units — $\hbar = 1.055\times10^{-34}\,\mathrm{J\cdot s}$ is a quantum of action — so the ratio is a pure number:

$$
[S/\hbar] = \frac{\mathrm{J\cdot s}}{\mathrm{J\cdot s}} = 1 \quad(\text{dimensionless}).
$$

The exponent *must* be dimensionless. The exponential is defined by its series $\mathrm{e}^{x} = 1 + x + \tfrac{1}{2}x^2 + \cdots$, which adds $x$ to $x^2$ to the pure number $1$; this is meaningful only if every term — and therefore $x$ itself — is a pure number. Physically, the exponent of $\mathrm{e}^{\mathrm{i}S/\hbar}$ is a phase angle (measured in radians), which is inherently dimensionless. This is the very reason nature needs a constant with the dimensions of action: $\hbar$ is the conversion factor that turns the classical action into a quantum phase.

**(b) Baseball.** Estimate the action as $S \sim mvd = (0.15\,\text{kg})(30\,\text{m/s})(10\,\text{m}) = 45\,\mathrm{J\cdot s}$. Then

$$
\frac{S}{\hbar} \approx \frac{45\,\mathrm{J\cdot s}}{1.055\times10^{-34}\,\mathrm{J\cdot s}} \approx 4\times10^{35}.
$$

The phase $S/\hbar$ is about $10^{35}$ radians. An utterly negligible change in the baseball's trajectory — displacing it by an atomic diameter — alters $S$ by vastly more than $\hbar$, so neighbouring paths carry completely scrambled phases and interfere destructively. Quantum interference is unobservable; the baseball follows a single sharp classical trajectory. This is the classical limit $S \gg \hbar$.

**(c) Electron.** Estimate $S \sim mvd = (9.1\times10^{-31}\,\text{kg})(10^6\,\text{m/s})(10^{-9}\,\text{m}) = 9.1\times10^{-34}\,\mathrm{J\cdot s}$. Then

$$
\frac{S}{\hbar} \approx \frac{9.1\times10^{-34}\,\mathrm{J\cdot s}}{1.055\times10^{-34}\,\mathrm{J\cdot s}} \approx 8.6.
$$

Now the phase is only a handful of radians. Deforming the electron's path over its $1\,\text{nm}$ flight changes $S$ by an amount comparable to $\hbar$ itself, so a whole bundle of paths contributes with comparable phases and interferes coherently. The single-trajectory picture fails; diffraction, tunnelling, and interference dominate. This is the quantum regime $S \sim \hbar$.

The contrast between the two ratios — roughly $10^{35}$ versus $10^{1}$ — is the whole reason the macroscopic world looks classical while the atomic world does not. Quantum behaviour is governed not by the absolute size of $S$ but by its size *relative to* $\hbar$.

<!-- ─── -->

**5. Path cancellation.** In the path integral, we sum $\mathrm{e}^{\mathrm{i}S\lbrack\mathrm{path}\rbrack/\hbar}$ over all paths.

(a) Consider two neighboring paths whose actions differ by $\Delta S$. What is the phase difference between their contributions? Under what condition do they interfere constructively?

(b) When $S \gg \hbar$, argue that a small geometric deformation of the path changes $S$ by much more than $\hbar$, so neighboring paths have wildly different phases and cancel. Why does the classical path ($\delta S = 0$) survive?

(c) When $S \sim \hbar$, explain why many paths contribute and the particle no longer follows a single trajectory.

**Solution.**

**(a)** Each path contributes a complex amplitude $\mathrm{e}^{\mathrm{i}S/\hbar}$ — a unit vector ("phasor") whose angle is the phase $\Phi = S/\hbar$. Two paths whose actions differ by $\Delta S$ therefore have phasors differing in angle by

$$
\Delta\Phi = \frac{\Delta S}{\hbar}.
$$

Their contributions reinforce when the phasors are aligned, i.e. when $\Delta\Phi$ is a multiple of $2\pi$:

$$
\Delta S = 2\pi\hbar\,N = hN, \qquad N \in \mathbb{Z}.
$$

In practice "constructive" means the phase difference is small compared with $\pi$, i.e. $|\Delta S| \lesssim \pi\hbar$: the two amplitudes then point in nearly the same direction and add. When $\Delta\Phi$ is an odd multiple of $\pi$ (that is, $\Delta S = h(N+\tfrac{1}{2})$) the phasors are anti-aligned and the two contributions cancel.

**(b)** Write a path as the classical path plus a deformation of size $\epsilon$. For a *generic* (non-classical) path the action has a non-zero first-order variation, so the deformation changes the action linearly, $\Delta S \approx (\delta S/\delta x)\,\epsilon$. When the overall scale of $S$ is enormous compared with $\hbar$, even a tiny $\epsilon$ makes $\Delta S \gg \hbar$, hence $\Delta\Phi = \Delta S/\hbar \gg 2\pi$. Neighbouring paths thus carry phasors pointing in essentially random directions all around the unit circle; summed together they cancel in pairs and contribute nothing net.

The classical path is the exception. There $\delta S = 0$ to first order — this is Hamilton's principle, that the action is *stationary* on the classical trajectory. A deformation then changes $S$ only at second order, $\Delta S \sim (\text{curvature})\,\epsilon^2$, which stays below $\hbar$ over a finite neighbourhood of paths. That whole neighbourhood shares almost the same action — almost the same phase — so these contributions add constructively. Everything else dephases and cancels. The surviving contribution to the sum comes from the stationary-phase region, and that *is* the classical trajectory. This is how the classical law $\delta S = 0$ re-emerges as the $S \gg \hbar$ limit of the path integral.

**(c)** When $S \sim \hbar$, the actions of the physically relevant paths differ from one another only by amounts of order $\hbar$ or less. Then $\Delta\Phi = \Delta S/\hbar \sim 1$ for a broad family of paths: they do *not* dephase relative to one another. Many paths — not merely an infinitesimal sliver around the classical one — contribute with comparable, coherent phases. No single path dominates the sum, so it is no longer meaningful to speak of "the trajectory" the particle follows. The observable physics is the coherent superposition over a whole bundle of paths, and that is exactly what produces diffraction, interference fringes, and tunnelling into classically forbidden regions.

<!-- ─── -->

**6. Relativistic action limit.** For a relativistic particle, $S = -mc^2\int\mathrm{d}\tau$. Show that in the non-relativistic limit ($v \ll c$), the action reduces to $S \approx \int(\tfrac{1}{2}mv^2 - mc^2)\,\mathrm{d}t$, recovering the familiar Lagrangian up to a constant.

**Solution.**

*Proper time in terms of coordinate time.* For a particle moving with velocity $\boldsymbol{v} = \mathrm{d}\boldsymbol{x}/\mathrm{d}t$ in flat spacetime, the invariant interval along its worldline is

$$
c^2\,\mathrm{d}\tau^2 = c^2\,\mathrm{d}t^2 - \mathrm{d}\boldsymbol{x}^2 = (c^2 - v^2)\,\mathrm{d}t^2,
$$

since $\mathrm{d}\boldsymbol{x}^2 = v^2\,\mathrm{d}t^2$. Taking the square root, the proper time and the coordinate time are related by

$$
\mathrm{d}\tau = \mathrm{d}t\,\sqrt{1 - \frac{v^2}{c^2}}.
$$

*The action as a coordinate-time integral.* Insert this into $S = -mc^2\int\mathrm{d}\tau$:

$$
S = -mc^2\int \sqrt{1 - \frac{v^2}{c^2}}\;\mathrm{d}t.
$$

*Non-relativistic expansion.* For $v \ll c$ the dimensionless ratio $v^2/c^2$ is small, so expand the square root using $\sqrt{1-x} = 1 - \tfrac{1}{2}x - \tfrac{1}{8}x^2 - \cdots$:

$$
\sqrt{1 - \frac{v^2}{c^2}} = 1 - \frac{v^2}{2c^2} - \frac{v^4}{8c^4} - \cdots \approx 1 - \frac{v^2}{2c^2},
$$

keeping only the leading correction (the dropped $v^4/c^4$ term is the first relativistic kinetic correction, negligible when $v \ll c$). Then

$$
S \approx -mc^2\int\left(1 - \frac{v^2}{2c^2}\right)\mathrm{d}t = \int\left(\frac{1}{2}mv^2 - mc^2\right)\mathrm{d}t,
$$

which is the required result.

*Reading off the Lagrangian.* The integrand is the non-relativistic free-particle Lagrangian

$$
L \approx \frac{1}{2}mv^2 - mc^2,
$$

i.e. the familiar kinetic term $T = \tfrac{1}{2}mv^2$ shifted by the constant $-mc^2$ (the rest energy).

*Why the constant is harmless.* The term $-mc^2$ contributes $-mc^2(t_f - t_i)$ to the action — a fixed number determined entirely by the endpoints. Its variation vanishes, $\delta\!\int(-mc^2)\,\mathrm{d}t = 0$, so it drops out of the stationary-action condition $\delta S = 0$ and does not affect the Euler–Lagrange equations. The dynamics are governed by $T - V$; here $V = 0$ for a free particle, and the classical motion is uniform straight-line motion, as expected. Thus the relativistic action $-mc^2\int\mathrm{d}\tau$ reduces, in the limit $v \ll c$, to the standard non-relativistic Lagrangian up to the dynamically irrelevant additive constant $-mc^2$. $\checkmark$

*Remark.* Repeating the expansion in a weak static gravitational potential $\Phi_g(\boldsymbol{x})$ (rather than flat spacetime) produces an extra term and gives $L \approx \tfrac{1}{2}mv^2 - m\Phi_g - mc^2$, identifying the potential energy $V = m\Phi_g$ — this is the result derived in the lecture's dropdown. The free-particle case here is the $\Phi_g \to 0$ specialization.
