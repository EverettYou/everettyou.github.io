# 3.2.3 Free Particle Propagator
Worked solutions for the homework problems in the [3.2.3 Free Particle Propagator](../ch3_path-integral/3-2-3-free-particle-propagator) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Dispersion relation.** Substitute the 3D plane wave $\psi(\boldsymbol{x},t) = \exp[\mathrm{i}(\boldsymbol{k}\cdot\boldsymbol{x} - \omega t)]$ into the free Schrödinger equation $\mathrm{i}\hbar\,\partial_t\psi(\boldsymbol{x},t) = -(\hbar^2/2m)\,\nabla^2\psi(\boldsymbol{x},t)$ and show that a solution exists if and only if $\omega = \hbar\boldsymbol{k}^{2}/(2m)$. Identify the energy and momentum of this state via the de Broglie relations.

**Solution.**

The free 3D Schrödinger equation is $\mathrm{i}\hbar\,\partial_{t}\psi = -(\hbar^{2}/2m)\,\nabla^{2}\psi$. Insert the plane-wave ansatz and evaluate the derivatives:

$$
\partial_{t}\psi = -\mathrm{i}\omega\,\psi,\qquad
\nabla\psi = \mathrm{i}\boldsymbol{k}\,\psi,\qquad
\nabla^{2}\psi = (\mathrm{i}\boldsymbol{k})\cdot(\mathrm{i}\boldsymbol{k})\,\psi = -\boldsymbol{k}^{2}\,\psi.
$$

Substituting into the equation,

$$
\mathrm{i}\hbar(-\mathrm{i}\omega)\,\psi = -\frac{\hbar^{2}}{2m}(-\boldsymbol{k}^{2})\,\psi,
$$

i.e. $\hbar\omega\,\psi = \hbar^{2}\boldsymbol{k}^{2}\psi/(2m)$.

The plane wave never vanishes — $\vert\psi\vert = 1$ at every point — so the two sides agree everywhere if and only if their coefficients agree:

$$
\hbar\omega = \frac{\hbar^{2}\boldsymbol{k}^{2}}{2m},
$$

equivalent to $\omega = \hbar\boldsymbol{k}^{2}/(2m)$.

This condition is necessary (the equation must hold somewhere) and sufficient (if it holds, $\psi$ solves the equation everywhere); for any other $\omega$ the ansatz fails. Hence a plane-wave solution of wavevector $\boldsymbol{k}$ exists precisely when $\omega = \hbar\boldsymbol{k}^{2}/(2m)$.

The de Broglie relations identify the momentum $\boldsymbol{p} = \hbar\boldsymbol{k}$ and the energy $E = \hbar\omega$. The dispersion relation then becomes

$$
E = \hbar\omega = \frac{\hbar^{2}\boldsymbol{k}^{2}}{2m} = \frac{(\hbar\boldsymbol{k})^{2}}{2m} = \frac{\boldsymbol{p}^{2}}{2m},
$$

exactly the classical kinetic energy of a free particle of mass $m$. The plane wave is therefore a simultaneous eigenstate of momentum (eigenvalue $\boldsymbol{p} = \hbar\boldsymbol{k}$) and energy (eigenvalue $E = \boldsymbol{p}^{2}/2m$).

<!-- ─── -->

**2. Momentum-space form of the free propagator.** The position-space free propagator $K_{\mathrm{free}}(\boldsymbol{x}, t; \boldsymbol{x}', 0)$ has a remarkably simple form in momentum space.

(a) Compute the Fourier transform $\tilde K(\boldsymbol{p}, t) = \int K_{\mathrm{free}}(\boldsymbol{x}, t; 0, 0)\,\mathrm{e}^{-\mathrm{i}\boldsymbol{p}\cdot\boldsymbol{x}/\hbar}\,\mathrm{d}^{3}x$.

(b) Show the result is $\tilde K(\boldsymbol{p}, t) = \exp[-\mathrm{i}\boldsymbol{p}^{2}t/(2m\hbar)]$ — a *pure phase*, depending only on the kinetic energy $\boldsymbol{p}^{2}/(2m)$.

(c) Interpret: in momentum space, free evolution multiplies each plane-wave component by a phase. Why is the momentum-space propagator dramatically simpler than the position-space one? What does this say about $\hat{H}_{\mathrm{free}}$ and the momentum operator $\hat{\boldsymbol{p}}$?

(d) Show that the position-space propagator $K_{\mathrm{free}}$ is recovered as the inverse Fourier transform of $\tilde K$. Conclude that $K_{\mathrm{free}}$ is exactly the result of multiplying each momentum-space plane wave by its individual kinetic phase $\mathrm{e}^{-\mathrm{i}E(\boldsymbol{p})t/\hbar}$ and reassembling — the "spectral decomposition" of free evolution.

**Solution.**

(a) Substitute the closed-form propagator $K_{\mathrm{free}}(\boldsymbol{x}, t; 0, 0) = (m/(2\pi\mathrm{i}\hbar t))^{3/2}\exp[\mathrm{i}m\boldsymbol{x}^{2}/(2\hbar t)]$ into the Fourier transform:

$$
\tilde K(\boldsymbol{p}, t) = \left(\frac{m}{2\pi\mathrm{i}\hbar t}\right)^{3/2}\int \exp\!\left[\frac{\mathrm{i}m\boldsymbol{x}^{2}}{2\hbar t} - \frac{\mathrm{i}\boldsymbol{p}\cdot\boldsymbol{x}}{\hbar}\right]\mathrm{d}^{3}x.
$$

The integrand factorises Cartesian-wise. Complete the square in each Cartesian component (write $a = m/(2\hbar t)$ and $b = p/\hbar$):

$$
\mathrm{i}ax^{2} - \mathrm{i}bx = \mathrm{i}a\Bigl(x - \frac{b}{2a}\Bigr)^{2} - \frac{\mathrm{i}b^{2}}{4a}.
$$

The leftover constant uses $b^{2}/(4a) = (p^{2}/\hbar^{2})/(2m/(\hbar t)) = p^{2}t/(2m\hbar)$.

(b) Shift the integration variable to $u = x - b/(2a)$, leaving a pure Fresnel integral $\int \mathrm{e}^{\mathrm{i}au^{2}}\,\mathrm{d}u = \sqrt{\pi/(\mathrm{i}a)} = \sqrt{2\pi\mathrm{i}\hbar t/m}$ (from Problem 3 / HW 3.2.2.1). The full 3D result is the cube:

$$
\int \mathrm{e}^{\mathrm{i}a\boldsymbol{u}^{2}}\,\mathrm{d}^{3}u = \left(\frac{2\pi\mathrm{i}\hbar t}{m}\right)^{3/2}.
$$

Multiplying by the prefactor $(m/(2\pi\mathrm{i}\hbar t))^{3/2}$, the prefactors **cancel exactly** — leaving only the constant from the square completion:

$$
\tilde K(\boldsymbol{p}, t) = \exp\!\left[-\frac{\mathrm{i}\boldsymbol{p}^{2}t}{2m\hbar}\right] = \exp\!\left[-\frac{\mathrm{i}E(\boldsymbol{p})\,t}{\hbar}\right],
$$

with $E(\boldsymbol{p}) = \boldsymbol{p}^{2}/(2m)$ the kinetic energy. **Pure phase, no Gaussian envelope.** $\checkmark$

(c) **Why simpler in momentum space.** The free Hamiltonian $\hat{H}_{\mathrm{free}} = \hat{\boldsymbol{p}}^{2}/(2m)$ is a *function of $\hat{\boldsymbol{p}}$ alone*. In the momentum basis where $\hat{\boldsymbol{p}}$ is diagonal, $\hat{H}_{\mathrm{free}}$ is also diagonal — eigenvalues $E(\boldsymbol{p}) = \boldsymbol{p}^{2}/(2m)$ — and the evolution operator $\mathrm{e}^{-\mathrm{i}\hat{H}t/\hbar}$ acts as $\mathrm{e}^{-\mathrm{i}E(\boldsymbol{p})t/\hbar}$ on each momentum eigenstate independently. **Momentum is conserved**, so different momenta do not mix; their evolution is just a phase rotation. In position space, by contrast, no single position eigenstate is preserved — different positions evolve into mixtures of one another — so the propagator has a non-trivial kernel.

(d) The inverse Fourier transform reconstructs $K_{\mathrm{free}}$ from $\tilde K$:

$$
K_{\mathrm{free}}(\boldsymbol{x}, t; 0, 0) = \int \frac{\mathrm{d}^{3}p}{(2\pi\hbar)^{3}}\,\mathrm{e}^{+\mathrm{i}\boldsymbol{p}\cdot\boldsymbol{x}/\hbar}\,\tilde K(\boldsymbol{p}, t) = \int \frac{\mathrm{d}^{3}p}{(2\pi\hbar)^{3}}\,\exp\!\left[\frac{\mathrm{i}(\boldsymbol{p}\cdot\boldsymbol{x} - E(\boldsymbol{p})t)}{\hbar}\right].
$$

Setting $\boldsymbol{k} = \boldsymbol{p}/\hbar$ and using $\mathrm{d}^{3}p/(2\pi\hbar)^{3} = \mathrm{d}^{3}k/(2\pi)^{3}$ converts this to the form used in Problem 3:

$$
K_{\mathrm{free}}(\boldsymbol{x}, t; 0, 0) = \int \frac{\mathrm{d}^{3}k}{(2\pi)^{3}}\,\exp\!\bigl[\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{x} - \mathrm{i}\omega(\boldsymbol{k})t\bigr].
$$

This is the **spectral decomposition** of free evolution: write any state as a momentum-space superposition $\psi = \int \mathrm{d}^{3}p\,\tilde\psi(\boldsymbol{p})\vert\boldsymbol{p}\rangle$, evolve each component by its own kinetic phase $\mathrm{e}^{-\mathrm{i}E(\boldsymbol{p})t/\hbar}$, then transform back to position space. The position-space propagator $K_{\mathrm{free}}$ is the assembly of these phase-rotated plane waves into a single integration kernel.

The position-space picture is rich (spreading, interference, classical-quantum correspondence — Problems 6 and 8) but algebraically heavy; the momentum-space picture is trivial — just phase rotation — but loses the geometric clarity. Choosing the right basis to diagonalise the Hamiltonian transforms the dynamics from a complicated integral kernel into elementary phase rotation. **This basis-choice is one of the most powerful problem-solving moves in quantum mechanics**: it converts time evolution into an algebra problem in the momentum (or any other) Hamiltonian-eigenbasis.

<!-- ─── -->

**3. Direct Gaussian integration.** Verify the closed form $K_{\mathrm{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \bigl(m/(2\pi\mathrm{i}\hbar t)\bigr)^{3/2}\exp\!\bigl[\mathrm{i}\,m(\boldsymbol{x}-\boldsymbol{x}')^2/(2\hbar t)\bigr]$ by carrying out the $\boldsymbol{k}$ integral in $K_{\mathrm{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \int \frac{\mathrm{d}^3k}{(2\pi)^3}\,\exp\!\bigl[\mathrm{i}\boldsymbol{k}\cdot(\boldsymbol{x}-\boldsymbol{x}') - \mathrm{i}\omega(\boldsymbol{k})t\bigr]$.

(a) Complete the square in $\boldsymbol{k}$.

(b) Shift the integration variable and reduce to three Cartesian Fresnel integrals.

(c) Combine prefactors and the surviving exponent and confirm the result.

**Solution.**

Start from the plane-wave construction, $K_{\text{free}} = \int\frac{\mathrm{d}^{3}k}{(2\pi)^{3}}\exp[\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r} - \mathrm{i}\beta\boldsymbol{k}^{2}]$, with $\boldsymbol{r} = \boldsymbol{x}-\boldsymbol{x}'$ and $\beta = \hbar t/(2m)$.

**(a) Complete the square.** Factor $-\mathrm{i}\beta$ out of the quadratic and linear terms in $\boldsymbol{k}$:

$$
\begin{split}
\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r} - \mathrm{i}\beta\boldsymbol{k}^{2}
&= -\mathrm{i}\beta\Bigl(\boldsymbol{k}^{2} - \frac{\boldsymbol{k}\cdot\boldsymbol{r}}{\beta}\Bigr)\\
&= -\mathrm{i}\beta\Bigl[\Bigl(\boldsymbol{k}-\frac{\boldsymbol{r}}{2\beta}\Bigr)^{2} - \frac{\boldsymbol{r}^{2}}{4\beta^{2}}\Bigr]\\
&= -\mathrm{i}\beta\Bigl(\boldsymbol{k}-\frac{\boldsymbol{r}}{2\beta}\Bigr)^{2} + \frac{\mathrm{i}\,\boldsymbol{r}^{2}}{4\beta}.
\end{split}
$$

The final term is independent of $\boldsymbol{k}$ and factors out of the integral.

**(b) Shift and reduce to Fresnel integrals.** Substitute $\boldsymbol{q} = \boldsymbol{k} - \boldsymbol{r}/(2\beta)$, a real translation with $\mathrm{d}^{3}k = \mathrm{d}^{3}q$:

$$
K_{\text{free}} = \mathrm{e}^{\mathrm{i}\boldsymbol{r}^{2}/(4\beta)}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\,\mathrm{e}^{-\mathrm{i}\beta\boldsymbol{q}^{2}}.
$$

Since $\boldsymbol{q}^{2} = q_{1}^{2}+q_{2}^{2}+q_{3}^{2}$, the integrand is a product over the three Cartesian components, so the integral splits into three identical 1D Fresnel integrals:

$$
\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\,\mathrm{e}^{-\mathrm{i}\beta\boldsymbol{q}^{2}} = \left[\frac{1}{2\pi}\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}\beta q^{2}}\,\mathrm{d}q\right]^{3}.
$$

Each 1D integral is the Fresnel result (HW 3.2.2.1 — the analytic continuation of $\int\mathrm{e}^{-bq^{2}}\mathrm{d}q = \sqrt{\pi/b}$ to $b = \mathrm{i}\beta$, with $\beta>0$):

$$
\int_{-\infty}^{\infty}\mathrm{e}^{-\mathrm{i}\beta q^{2}}\,\mathrm{d}q = \sqrt{\frac{\pi}{\mathrm{i}\beta}}.
$$

**(c) Combine prefactors and exponent.** Cube the single-integral result:

$$
\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\,\mathrm{e}^{-\mathrm{i}\beta\boldsymbol{q}^{2}}
= \frac{1}{(2\pi)^{3}}\left(\frac{\pi}{\mathrm{i}\beta}\right)^{3/2}
= \left(\frac{1}{4\pi\mathrm{i}\beta}\right)^{3/2},
$$

using $(2\pi)^{-3}\pi^{3/2} = (4\pi)^{-3/2}$. Substituting $\beta = \hbar t/(2m)$ gives $4\pi\mathrm{i}\beta = 2\pi\mathrm{i}\hbar t/m$, so the prefactor is $(m/(2\pi\mathrm{i}\hbar t))^{3/2}$. The surviving exponent is

$$
\frac{\mathrm{i}\,\boldsymbol{r}^{2}}{4\beta} = \frac{\mathrm{i}\,\boldsymbol{r}^{2}}{4}\cdot\frac{2m}{\hbar t} = \frac{\mathrm{i}m\,\boldsymbol{r}^{2}}{2\hbar t}.
$$

Assembling the two pieces,

$$
K_{\text{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \left(\frac{m}{2\pi\mathrm{i}\hbar t}\right)^{3/2}\exp\!\left[\frac{\mathrm{i}m(\boldsymbol{x}-\boldsymbol{x}')^{2}}{2\hbar t}\right],
$$

exactly the closed form $K_{\mathrm{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \bigl(m/(2\pi\mathrm{i}\hbar t)\bigr)^{3/2}\exp\!\bigl[\mathrm{i}\,m(\boldsymbol{x}-\boldsymbol{x}')^2/(2\hbar t)\bigr]$. The plane-wave superposition and the closed-form propagator are the same object.

<!-- ─── -->

**4. Slice agreement (1D).** Specialize $K_{\mathrm{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \bigl(m/(2\pi\mathrm{i}\hbar t)\bigr)^{3/2}\exp\!\bigl[\mathrm{i}\,m(\boldsymbol{x}-\boldsymbol{x}')^2/(2\hbar t)\bigr]$ to one dimension and set $t = \delta t$. Show that the result is identical to the closed-form slice propagator $K_{\delta t}^{\mathrm{free}}(x,x') = \sqrt{m/(2\pi\mathrm{i}\hbar\,\delta t)}\,\exp\!\bigl[\mathrm{i}\,m(x-x')^2/(2\hbar\delta t)\bigr]$ from §3.2.2. Comment on what this verifies about the path integral.

**Solution.**

Specialize the closed form to one spatial dimension by suppressing two Cartesian components. The single Cartesian factor of the prefactor $(m/(2\pi\mathrm{i}\hbar t))^{3/2}$ is $(m/(2\pi\mathrm{i}\hbar t))^{1/2}$, and $(\boldsymbol{x}-\boldsymbol{x}')^{2}\to(x-x')^{2}$:

$$
K_{\text{free}}^{\text{1D}}(x,t;x',0) = \left(\frac{m}{2\pi\mathrm{i}\hbar t}\right)^{1/2}\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar t}\right].
$$

Now set $t = \delta t$:

$$
K_{\text{free}}^{\text{1D}}(x,\delta t;x',0) = \left(\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}\right)^{1/2}\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar\,\delta t}\right].
$$

The closed-form single-slice propagator derived in §3.2.2 is

$$
K_{\delta t}^{\text{free}}(x,x') = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\,\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar\,\delta t}\right].
$$

The two expressions are term-by-term identical — same prefactor, same phase.

**What this verifies.** The finite-time propagator $K_{\text{free}}$ was constructed with no reference to slicing at all: it came from superposing the exact plane-wave eigenmodes of the Schrödinger equation. The single-slice propagator $K_{\delta t}^{\text{free}}$, by contrast, was obtained in §3.2.2 from the path-integral construction — its kinetic phase set by the slice action and its prefactor $A(\delta t) = \sqrt{m/(2\pi\mathrm{i}\hbar\,\delta t)}$ fixed by the zero-duration condition. That these two independently derived objects coincide at $t = \delta t$ shows that the slice formula was *not* an approximation valid only for small $\delta t$: it is the exact free propagator at any duration. Equivalently, composing many slices reconstructs the very same closed form (HW 3.2.2.4), so refining the slicing produces no new physics for the free particle. The path integral is internally self-consistent — the discrete slice picture and the continuum eigenmode picture deliver one and the same propagator.

<!-- ─── -->

**5. Action conjugate relations.** For the free-particle classical action $S_{\text{cl}}(\boldsymbol{x},t;\boldsymbol{x}',0) = m\,(\boldsymbol{x}-\boldsymbol{x}')^{2}/(2t)$,

(a) compute $\nabla S_{\text{cl}}$ and identify it with the final momentum $\boldsymbol{p}$;

(b) compute $-\partial_{t}S_{\text{cl}}$ and identify it with the energy $E$;

(c) explain how these two relations make the propagator phase $\mathrm{e}^{\mathrm{i}S_{\text{cl}}/\hbar}$ act locally as a plane wave $\mathrm{e}^{\mathrm{i}(\boldsymbol{p}\cdot\boldsymbol{x} - Et)/\hbar}$ near the classical trajectory.

**Solution.**

Write $\boldsymbol{r} = \boldsymbol{x}-\boldsymbol{x}'$, so $S_{\text{cl}} = m\boldsymbol{r}^{2}/(2t)$, and let $\boldsymbol{v} = \boldsymbol{r}/t = (\boldsymbol{x}-\boldsymbol{x}')/t$ be the constant velocity of the straight-line classical trajectory.

**(a) Gradient = final momentum.** Differentiate with respect to the endpoint $\boldsymbol{x}$, which enters only through $\boldsymbol{r}$. Using $\nabla_{\boldsymbol{x}}\boldsymbol{r}^{2} = 2\boldsymbol{r}$,

$$
\nabla S_{\text{cl}} = \frac{m}{2t}\,\nabla_{\boldsymbol{x}}\boldsymbol{r}^{2} = \frac{m}{2t}\,(2\boldsymbol{r}) = \frac{m\boldsymbol{r}}{t} = m\boldsymbol{v}.
$$

For a free particle $\boldsymbol{p} = m\boldsymbol{v}$, so $\nabla S_{\text{cl}} = \boldsymbol{p}$ — the momentum with which the particle *arrives* at $\boldsymbol{x}$. This is the Hamilton–Jacobi relation $\boldsymbol{p} = \nabla S$.

**(b) Time derivative = energy.** Differentiate with respect to the arrival time $t$ at fixed endpoints, using $\partial_{t}(1/t) = -1/t^{2}$:

$$
\partial_{t}S_{\text{cl}} = \frac{m\boldsymbol{r}^{2}}{2}\,\partial_{t}\!\left(\frac{1}{t}\right) = -\frac{m\boldsymbol{r}^{2}}{2t^{2}}.
$$

Hence

$$
-\partial_{t}S_{\text{cl}} = \frac{m\boldsymbol{r}^{2}}{2t^{2}} = \frac{1}{2}m\Bigl(\frac{\boldsymbol{r}}{t}\Bigr)^{2} = \frac{1}{2}m\boldsymbol{v}^{2} = \frac{\boldsymbol{p}^{2}}{2m} = E,
$$

the kinetic energy carried by the particle. This is the second Hamilton–Jacobi relation, $E = -\partial_{t}S$.

**(c) Local plane wave.** Expand the action for a small change of the observation point, $\boldsymbol{x}\to\boldsymbol{x}+\delta\boldsymbol{x}$, $t\to t+\delta t$, about a point $(\boldsymbol{x},t)$ on the classical trajectory:

$$
S_{\text{cl}}(\boldsymbol{x}+\delta\boldsymbol{x},\,t+\delta t) \approx S_{\text{cl}}(\boldsymbol{x},t) + \nabla S_{\text{cl}}\cdot\delta\boldsymbol{x} + \partial_{t}S_{\text{cl}}\,\delta t = S_{\text{cl}}(\boldsymbol{x},t) + \boldsymbol{p}\cdot\delta\boldsymbol{x} - E\,\delta t,
$$

inserting the results of (a) and (b). The propagator phase factor therefore behaves, in a small neighbourhood of any point on the classical trajectory, as

$$
\mathrm{e}^{\mathrm{i}S_{\text{cl}}/\hbar} \approx \mathrm{e}^{\mathrm{i}S_{\text{cl}}(\boldsymbol{x},t)/\hbar}\;\mathrm{e}^{\mathrm{i}(\boldsymbol{p}\cdot\delta\boldsymbol{x} - E\,\delta t)/\hbar}.
$$

The second factor is precisely a plane wave $\mathrm{e}^{\mathrm{i}(\boldsymbol{p}\cdot\boldsymbol{x} - Et)/\hbar}$, with local wavevector $\boldsymbol{k} = \boldsymbol{p}/\hbar$ and frequency $\omega = E/\hbar$ — the de Broglie wave of a particle carrying momentum $\boldsymbol{p}$ and energy $E$. So although $K_{\text{free}}$ is *globally* a spreading spherical wave — its momentum $\boldsymbol{p} = m\boldsymbol{r}/t$ varies from point to point — it is *locally* indistinguishable from a plane wave whose momentum and energy are exactly the classical values at that point. The two Hamilton–Jacobi relations are what make this work: $\nabla S_{\text{cl}}$ supplies the local wavevector, and $-\partial_{t}S_{\text{cl}}$ supplies the local frequency. This is the eikonal (geometric-optics) content of "phase = action": $S_{\text{cl}}/\hbar$ is a position- and time-dependent phase whose gradients reproduce the classical momentum and energy.

<!-- ─── -->

**6. Phase velocity vs group velocity.** A plane-wave matter wave $\mathrm{e}^{\mathrm{i}(\boldsymbol{k}\cdot\boldsymbol{x} - \omega t)}$ with $\omega = \hbar\boldsymbol{k}^{2}/(2m)$ propagates with two distinct velocities, which a *single* plane wave cannot reveal.

(a) From a surface of constant phase $\boldsymbol{k}\cdot\boldsymbol{x} - \omega t = \mathrm{const}$, compute the **phase velocity** $v_{\mathrm{phase}} = \omega/k$ in terms of the particle's momentum $p = \hbar k$ and mass $m$.

(b) For a wavepacket centred on momentum $\boldsymbol{p}_{0}$, the centroid of $\vert\psi\vert^{2}$ moves at the **group velocity** $v_{\mathrm{group}} = \mathrm{d}\omega/\mathrm{d}k$ evaluated at $k_{0} = p_{0}/\hbar$. Compute it.

(c) Show that $v_{\mathrm{group}} = 2v_{\mathrm{phase}}$, and identify $v_{\mathrm{group}}$ with the *classical* particle velocity $p_{0}/m$.

(d) Explain physically: why is the "particle velocity" the group velocity, not the phase velocity? What is the analogue for an electromagnetic wave in vacuum, where $\omega = ck$ — and why do photons not exhibit this factor of $2$ ambiguity?

**Solution.**

(a) **Phase velocity.** A surface of constant phase satisfies $\boldsymbol{k}\cdot\boldsymbol{x} - \omega t = \mathrm{const}$, so under translation $\boldsymbol{x}\to\boldsymbol{x} + \delta\boldsymbol{x}$ and $t\to t + \delta t$ on the surface, $\boldsymbol{k}\cdot\delta\boldsymbol{x} = \omega\,\delta t$. Taking $\delta\boldsymbol{x}$ along $\boldsymbol{k}/k$ gives $k\,\vert\delta\boldsymbol{x}\vert = \omega\,\delta t$, i.e. $v_{\mathrm{phase}} = \vert\delta\boldsymbol{x}\vert/\delta t = \omega/k$. For the matter-wave dispersion $\omega = \hbar k^{2}/(2m)$,

$$
v_{\mathrm{phase}} = \frac{\omega}{k} = \frac{\hbar k}{2m} = \frac{p}{2m}.
$$

(b) **Group velocity.** Differentiating $\omega(k) = \hbar k^{2}/(2m)$ with respect to $k$:

$$
v_{\mathrm{group}} = \frac{\mathrm{d}\omega}{\mathrm{d}k} = \frac{2\hbar k}{2m} = \frac{\hbar k}{m} = \frac{p}{m}.
$$

(c) **The factor of 2.** Comparing,

$$
v_{\mathrm{group}} = \frac{p}{m} = 2\cdot\frac{p}{2m} = 2v_{\mathrm{phase}}.
$$

The group velocity is twice the phase velocity, and **it equals the classical particle velocity** $v_{\mathrm{cl}} = p/m$. The phase velocity $p/(2m)$ has no classical interpretation as a particle speed.

(d) **Why the classical particle velocity is the group velocity.**

A *single* plane wave has constant amplitude $\vert\psi\vert^{2} = 1$ everywhere — its phase moves at $v_{\mathrm{phase}}$, but there is no localised "particle" to track; the wave is uniformly spread. To localise the particle one builds a *wavepacket* — a superposition of plane waves with momenta clustered around $\boldsymbol{p}_{0}$. The envelope of $\vert\psi\vert^{2}$ is what one would measure as a "particle"; this envelope moves at the group velocity.

The mathematical reason: for a narrow momentum spread $\Delta p \ll p_{0}$, Taylor-expand $\omega(p) \approx \omega(p_{0}) + (\mathrm{d}\omega/\mathrm{d}p)\vert_{p_{0}}\cdot(p - p_{0})$. Substituting into the wavepacket integral,

$$
\psi(x, t) \approx \mathrm{e}^{\mathrm{i}(k_{0}x - \omega_{0}t)}\int \tilde\psi(p)\,\mathrm{e}^{\mathrm{i}(p - p_{0})(x - v_{\mathrm{group}}t)/\hbar}\,\mathrm{d}p,
$$

so $\vert\psi(x, t)\vert^{2}$ depends on $x$ only through the combination $x - v_{\mathrm{group}}t$. The envelope translates at $v_{\mathrm{group}}$ — this is *where the particle is at time $t$*, and it matches the classical $p_{0}/m$.

**Electromagnetic waves in vacuum.** For light $\omega = ck$, so $v_{\mathrm{phase}} = \omega/k = c$ and $v_{\mathrm{group}} = \mathrm{d}\omega/\mathrm{d}k = c$. **The two are equal** — there is no factor-of-$2$ discrepancy, because the dispersion is linear ($\omega \propto k$) rather than quadratic ($\omega \propto k^{2}$). A photon's "phase speed" *is* its group speed *is* the speed of light. The factor-of-$2$ ambiguity of matter waves traces directly to the *quadratic* non-relativistic dispersion $E = p^{2}/(2m)$, distinct from the relativistic linear $E = pc$ of photons.

This is the simplest possible illustration of the **dispersion principle**: in any medium where $\omega(k)$ is non-linear, signal-carrying wavepackets travel at $v_{\mathrm{group}}$, while the underlying wave crests travel at the (typically different) $v_{\mathrm{phase}}$. The factor of $2$ in $v_{\mathrm{group}}/v_{\mathrm{phase}}$ for free matter waves is the algebraic signature of $E \propto p^{2}$ — quadratic kinetic energy makes the group velocity twice the phase velocity for any monoenergetic mode.

<!-- ─── -->

**7. Magnitude and normalization.** Compute $\vert K_{\text{free}}(\boldsymbol{x},t;\boldsymbol{x}',0)\vert^{2}$ from $K_{\mathrm{free}}(\boldsymbol{x},t;\boldsymbol{x}',0) = \bigl(m/(2\pi\mathrm{i}\hbar t)\bigr)^{3/2}\exp\!\bigl[\mathrm{i}\,m(\boldsymbol{x}-\boldsymbol{x}')^2/(2\hbar t)\bigr]$ and show that it is independent of position, equal to $\bigl(m/(2\pi\hbar t)\bigr)^{3}$.

(a) Explain why this *position-independence* of the modulus is consistent with the propagator being normalized as $\int K_{\text{free}}\,\mathrm{d}^{3}x = 1$ (cf. HW 3.2.2.3) at every $t$.

(b) Why is it nevertheless inappropriate to interpret $\vert K_{\text{free}}\vert^{2}$ as a probability density of finding the particle at $\boldsymbol{x}$? (Hint: the propagator describes the response to a singular delta-function initial state; physical probability densities require a normalizable initial wavefunction.)

**Solution.**

From the closed form, $K_{\text{free}} = (m/(2\pi\mathrm{i}\hbar t))^{3/2}\exp[\mathrm{i}m\boldsymbol{r}^{2}/(2\hbar t)]$ with $\boldsymbol{r} = \boldsymbol{x}-\boldsymbol{x}'$. The exponent $\mathrm{i}m\boldsymbol{r}^{2}/(2\hbar t)$ is purely imaginary — every factor $m$, $\boldsymbol{r}^{2}$, $\hbar$, $t$ is real — so the exponential is a pure phase of unit modulus: $\vert\exp[\mathrm{i}m\boldsymbol{r}^{2}/(2\hbar t)]\vert = 1$. Only the prefactor contributes to the modulus:

$$
\vert K_{\text{free}}\vert^{2} = \left\vert\left(\frac{m}{2\pi\mathrm{i}\hbar t}\right)^{3/2}\right\vert^{2} = \left\vert\frac{m}{2\pi\mathrm{i}\hbar t}\right\vert^{3} = \left(\frac{m}{2\pi\hbar t}\right)^{3},
$$

since $\vert\mathrm{i}\vert = 1$ and (for $t>0$) $\vert 2\pi\mathrm{i}\hbar t\vert = 2\pi\hbar t$. The result depends only on $t$ — it is the same for every pair $(\boldsymbol{x},\boldsymbol{x}')$.

**(a) Consistency with $\int K_{\text{free}}\,\mathrm{d}^{3}x = 1$.** There is no contradiction, because the two statements concern different objects. The normalization $\int K_{\text{free}}\,\mathrm{d}^{3}x = 1$ integrates the *complex amplitude* $K_{\text{free}}$, not its modulus. That integral is finite (indeed equal to $1$) not because the integrand decays — it does not, $\vert K_{\text{free}}\vert$ is constant — but because the rapidly varying phase $m\boldsymbol{r}^{2}/(2\hbar t)$ produces destructive interference: it is a convergent Fresnel integral, evaluated in HW 3.2.2.3 and reused in Problem 2(b) above. A function of constant modulus but rapidly oscillating phase can perfectly well integrate to a finite number. So a position-independent $\vert K_{\text{free}}\vert$ is fully compatible with $\int K_{\text{free}}\,\mathrm{d}^{3}x = 1$: here normalization is enforced by phase cancellation, not by spatial decay of the amplitude.

**(b) Why $\vert K_{\text{free}}\vert^{2}$ is not a probability density.** A probability density must be normalizable, $\int(\text{density})\,\mathrm{d}^{3}x = 1$. But $\vert K_{\text{free}}\vert^{2} = (m/(2\pi\hbar t))^{3}$ is constant in space, so

$$
\int\vert K_{\text{free}}\vert^{2}\,\mathrm{d}^{3}x = \left(\frac{m}{2\pi\hbar t}\right)^{3}\int\mathrm{d}^{3}x = \infty
$$

— it cannot be normalized. The reason is built into what the propagator *is*: $K_{\text{free}}(\boldsymbol{x},t;\boldsymbol{x}',0)$ is the response to the singular initial state $\psi(\cdot,0) = \delta^{3}(\cdot-\boldsymbol{x}')$, a perfectly localized "particle." Such a state has infinite position certainty, hence (by the uncertainty principle) infinite momentum spread, so after any time $t>0$ its amplitude is smeared over all of space with equal magnitude — there is literally no preferred location, the opposite of a localized probability distribution. A genuine probability density requires a *normalizable* initial wavefunction $\psi(\boldsymbol{x},0)$ with $\int\vert\psi\vert^{2}\,\mathrm{d}^{3}x = 1$. Propagating that state via $\psi(\boldsymbol{x},t) = \int K_{\text{free}}\,\psi(\boldsymbol{x}',0)\,\mathrm{d}^{3}x'$ yields a wavefunction whose $\vert\psi(\boldsymbol{x},t)\vert^{2}$ *is* a legitimate, normalized, position-dependent density — for example the spreading Gaussian of Problem 6. The propagator itself is a transition amplitude (an integration kernel), not a physical state, and $\vert K\vert^{2}$ is not a probability.

<!-- ─── -->

**8. Macroscopic phase factors.** The phase of the free propagator is $\Phi = m\,(\boldsymbol{x}-\boldsymbol{x}')^{2}/(2\hbar t)$.

(a) Evaluate $\Phi$ as a multiple of $2\pi$ for a baseball with $m = 0.15\,$kg, displacement $1\,$m, time $1\,$s.

(b) Evaluate $\Phi$ as a multiple of $2\pi$ for an electron with $m\approx 9\times 10^{-31}\,$kg, displacement $1\,$nm, time $1\,$ps.

(c) Use the two numbers to explain why classical objects show no observable quantum interference, while electrons routinely do.

**Solution.**

The propagator phase is $\Phi = m\,r^{2}/(2\hbar t)$ with $r = \vert\boldsymbol{x}-\boldsymbol{x}'\vert$ the displacement. Use $\hbar = 1.05\times 10^{-34}\,\mathrm{J\cdot s}$.

**(a) Baseball.** $m = 0.15\,$kg, $r = 1\,$m, $t = 1\,$s:

$$
\Phi = \frac{(0.15)(1)^{2}}{2(1.05\times 10^{-34})(1)} \approx 7.1\times 10^{32}\ \text{rad},
$$

so $\Phi/(2\pi) \approx 1.1\times 10^{32}$.

The phase amounts to about $10^{32}$ full cycles.

**(b) Electron.** $m\approx 9\times 10^{-31}\,$kg, $r = 1\,$nm $= 10^{-9}\,$m, $t = 1\,$ps $= 10^{-12}\,$s:

$$
\Phi = \frac{(9\times 10^{-31})(10^{-9})^{2}}{2(1.05\times 10^{-34})(10^{-12})} \approx 4.3\times 10^{-3}\ \text{rad},
$$

so $\Phi/(2\pi) \approx 6.8\times 10^{-4}$.

The phase is a tiny fraction of a single cycle.

**(c) Why classical objects show no interference.** Interference is observable only when the phase varies by an amount *of order* $2\pi$ across the experimentally controllable spread of paths — enough variation to build up fringes, yet not so much that neighbouring paths average to zero. What matters is therefore the *rate of change* of $\Phi$ with the path, captured by

$$
\frac{\partial\Phi}{\partial r} = \frac{m r}{\hbar t}.
$$

*Baseball:* $\partial\Phi/\partial r = (0.15)(1)/[(1.05\times 10^{-34})(1)]\approx 1.4\times 10^{33}\,$rad/m. The phase sweeps through a full $2\pi$ over a displacement change of only $\Delta r\approx 2\pi/(1.4\times 10^{33})\approx 4\times 10^{-33}\,$m — far smaller than an atomic nucleus. Any two macroscopically indistinguishable trajectories differ in phase by an enormous, effectively random multiple of $2\pi$; summing their amplitudes gives complete destructive interference except along the single stationary-phase (classical) path. The baseball follows a sharp classical trajectory and exhibits no interference fringes, because the fringes — insofar as they exist — are spaced far below any conceivable measurement resolution. The huge count $\Phi/2\pi\sim 10^{32}$ is the quantitative signature of this regime.

*Electron:* $\partial\Phi/\partial r = (9\times 10^{-31})(10^{-9})/[(1.05\times 10^{-34})(10^{-12})]\approx 8.6\times 10^{6}\,$rad/m. A full $2\pi$ now requires $\Delta r\approx 0.7\,\mu$m — a macroscopic, readily resolved length. The phase varies smoothly and by experimentally accessible amounts over nanometre–picosecond scales (the modest total $\Phi/2\pi\sim 10^{-3}$ confirms the phase is "gentle"), so amplitudes from neighbouring paths interfere coherently and produce visible fringes. This is why electron diffraction and double-slit interference are routine while a baseball's are not: the same formula $\Phi = m r^{2}/(2\hbar t)$, evaluated with everyday versus microscopic values of $m$, $r$, and $t$, places the fringe spacing either absurdly below — or comfortably above — the scale at which measurements are made.
