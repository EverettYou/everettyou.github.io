# 4.1.1 Gauge Principle
Worked solutions for the homework problems in the [4.1.1 Gauge Principle](../ch4_phase-and-gauge/4-1-1-gauge-principle) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Diagnosing redundancy.** For each pair $(\psi, \psi')$ below, compute $\vert\psi\vert^2$, $\arg\psi$, and $\langle\hat{p}_x\rangle$, and decide whether the two states represent the same physical system or different ones.

(a) $\psi(x) = \mathrm{e}^{\mathrm{i}kx}$ and $\psi'(x) = \mathrm{e}^{\mathrm{i}kx+\mathrm{i}\theta_0}$ (constant overall phase).

(b) $\psi(x) = \mathrm{e}^{\mathrm{i}kx}$ and $\psi'(x) = \mathrm{e}^{\mathrm{i}(k+k_0)x}$ (different wavevector).

(c) $\psi(\boldsymbol{r}) = f(\boldsymbol{r})$ and $\psi'(\boldsymbol{r}) = \mathrm{e}^{\mathrm{i}q\alpha(\boldsymbol{r})/\hbar}f(\boldsymbol{r})$, *together with the simultaneous gauge transformation* $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$.

State which transformation is a symmetry and which is a redundancy, and identify the operational diagnostic.

**Solution.**

With $\hat{p}_x = -\mathrm{i}\hbar\,\partial_x$, a plane wave $\mathrm{e}^{\mathrm{i}\kappa x}$ is a momentum eigenstate: $\hat{p}_x\,\mathrm{e}^{\mathrm{i}\kappa x} = \hbar\kappa\,\mathrm{e}^{\mathrm{i}\kappa x}$, so $\langle\hat{p}_x\rangle = \hbar\kappa$ (the constant $\vert\psi\vert^2$ makes this the natural per-particle value).

**(a)** $\vert\psi\vert^2 = \vert\psi'\vert^2 = 1$. The arguments are $\arg\psi = kx$ and $\arg\psi' = kx + \theta_0$, differing by the constant $\theta_0$. For the momentum,

$$
\hat{p}_x\psi' = -\mathrm{i}\hbar(\mathrm{i}k)\mathrm{e}^{\mathrm{i}kx+\mathrm{i}\theta_0} = \hbar k\,\psi',
$$

so $\langle\hat{p}_x\rangle = \hbar k$ for both — the constant phase cancels between $\psi'^{*}$ and $\psi'$. Every observable agrees: the two describe the **same physical system**. A constant phase is the **global-phase redundancy** of §1.1.1.

**(b)** Again $\vert\psi\vert^2 = \vert\psi'\vert^2 = 1$ — the probability densities are identical. But $\arg\psi = kx$ and $\arg\psi' = (k+k_0)x$ differ by the *position-dependent* phase $k_0 x$. The momenta differ:

$$
\hat{p}_x\psi = \hbar k\,\psi,
\qquad
\hat{p}_x\psi' = \hbar(k+k_0)\,\psi',
$$

so $\langle\hat{p}_x\rangle = \hbar k$ versus $\hbar(k+k_0)$, and the kinetic energies $\hbar^2 k^2/2m$ versus $\hbar^2(k+k_0)^2/2m$ differ as well. Equal $\vert\psi\vert^2$ is *not* enough to identify two states: these are **physically different plane-wave states** (different wavevector $k\to k+k_0$). The map $\psi \to \mathrm{e}^{\mathrm{i}k_0 x}\psi$ is a position-dependent phase with *no* compensating change of $\boldsymbol{A}$; it relabels canonical momentum but is **not** a gauge redundancy of the charged-particle Hamiltonian.

**(c)** $\vert\psi'\vert^2 = \vert\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\vert^2\vert f\vert^2 = \vert f\vert^2 = \vert\psi\vert^2$ — same density. The argument shifts by the position-dependent $q\alpha(\boldsymbol{r})/\hbar$: $\arg\psi' = \arg f + q\alpha/\hbar$. The *canonical* momentum does change, $\langle\hat{p}_x\rangle \to \langle\hat{p}_x\rangle + q\langle\partial_x\alpha\rangle$, but it is accompanied by $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$, so the gauge-invariant **kinetic momentum** is unchanged:

$$
\langle\hat{\pi}_x'\rangle = \langle\hat{p}_x\rangle + q\langle\partial_x\alpha\rangle - q\langle A_x + \partial_x\alpha\rangle = \langle\hat{p}_x - qA_x\rangle = \langle\hat{\pi}_x\rangle.
$$

Every gauge-invariant quantity — density, kinetic momentum (hence velocity), and the fields $\boldsymbol{E},\boldsymbol{B}$ — agrees. The two describe the **same physical system** in two different descriptions.

**Symmetry versus redundancy.** Cases (a) and (c) are **redundancies**: (a) is the global-phase redundancy, and (c) is the **local gauge redundancy** in which the wavefunction *and* the connection transform together. Case (b) is **not** a redundancy — it changes a physical observable (canonical momentum and kinetic energy) without the compensating connection shift that defines a gauge transformation.

**Operational diagnostic.** A transformation is a redundancy if and only if *every* gauge-invariant observable is unchanged — in particular $\vert\psi\vert^2$ **and** the kinetic momentum $\langle\hat{\boldsymbol{p}} - q\boldsymbol{A}\rangle$ (equivalently the velocity) **and** the fields $\boldsymbol{E},\boldsymbol{B}$. Equality of $\vert\psi\vert^2$ alone is insufficient — case (b) passes that test yet is a physical change. The decisive check is the kinetic momentum: in (a) it is unchanged (no $\boldsymbol{A}$, and $\langle\hat{p}_x\rangle$ fixed); in (c) $\langle\hat{p}_x\rangle$ moves but $\langle\hat{p}_x - qA_x\rangle$ does not; in (b) $\langle\hat{p}_x\rangle$ moves with no compensating $\boldsymbol{A}$, so $\langle\hat{p}_x - qA_x\rangle$ moves — the signature of a physical change.

<!-- ─── -->

**2. Plane-wave gauge transform.** Let $\psi(\boldsymbol r,t)$ be an arbitrary state (not necessarily a plane wave). Use the single gauge function

$$
\alpha(\boldsymbol{r},t)=\boldsymbol{k}\cdot\boldsymbol{r}-\omega t,
$$

with constant $\boldsymbol{k}$ and $\omega$, and apply

$$
\begin{split}
\psi' &= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi,\\
\boldsymbol A' &= \boldsymbol A + \nabla\alpha,\\
\phi' &= \phi - \partial_t\alpha.
\end{split}
$$

(a) Compute the shifts $\boldsymbol{A}'-\boldsymbol{A}$ and $\phi'-\phi$.

(b) Show directly that the fields are unchanged:

$$
\begin{split}
\boldsymbol E' &= -\nabla\phi' - \partial_t\boldsymbol A' = \boldsymbol E,\\
\boldsymbol B' &= \nabla\times\boldsymbol A' = \boldsymbol B.
\end{split}
$$

(c) Explain why this statement is independent of the specific choice of state $\psi$.

(d) Give a short physical interpretation: what changes under this transformation (description/kinematic labels), and what does not (gauge-invariant fields and force law)?

**Solution.**

**(a)** The gauge function $\alpha = \boldsymbol{k}\cdot\boldsymbol{r} - \omega t$ has

$$
\nabla\alpha = \boldsymbol{k},
\qquad
\partial_t\alpha = -\omega,
$$

both *constant* in spacetime. Hence

$$
\boldsymbol{A}' - \boldsymbol{A} = \nabla\alpha = \boldsymbol{k},
\qquad
\phi' - \phi = -\partial_t\alpha = \omega.
$$

The vector potential is shifted by the constant vector $\boldsymbol{k}$ and the scalar potential by the constant $\omega$.

**(b)** Using that $\boldsymbol{k}$ and $\omega$ are constants ($\nabla\omega = 0$, $\partial_t\boldsymbol{k} = 0$, $\nabla\times\boldsymbol{k} = 0$),

$$
\begin{split}
\boldsymbol{E}' &= -\nabla\phi' - \partial_t\boldsymbol{A}' = -\nabla(\phi+\omega) - \partial_t(\boldsymbol{A}+\boldsymbol{k}) = -\nabla\phi - \partial_t\boldsymbol{A} = \boldsymbol{E},\\
\boldsymbol{B}' &= \nabla\times\boldsymbol{A}' = \nabla\times(\boldsymbol{A}+\boldsymbol{k}) = \nabla\times\boldsymbol{A} = \boldsymbol{B}.
\end{split}
$$

The result is in fact general, for *any* gauge function $\alpha$: since $\nabla\times\nabla\alpha = 0$ and mixed partials commute, $\partial_t\nabla\alpha = \nabla\partial_t\alpha$,

$$
\begin{split}
\boldsymbol{B}' &= \nabla\times(\boldsymbol{A}+\nabla\alpha) = \boldsymbol{B} + \nabla\times\nabla\alpha = \boldsymbol{B},\\
\boldsymbol{E}' &= -\nabla(\phi-\partial_t\alpha) - \partial_t(\boldsymbol{A}+\nabla\alpha) = \boldsymbol{E} + \nabla\partial_t\alpha - \partial_t\nabla\alpha = \boldsymbol{E}.
\end{split}
$$

For the present linear $\alpha$ the shifts happen to be constants, which is the simplest possible illustration of the cancellation.

**(c)** The fields $\boldsymbol{E} = -\nabla\phi-\partial_t\boldsymbol{A}$ and $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ are functionals of the potentials $(\phi,\boldsymbol{A})$ **only** — the wavefunction $\psi$ never appears in them. The potential shifts $\nabla\alpha$ and $-\partial_t\alpha$ are fixed by $\alpha$ alone, and the cancellations in (b) rely solely on the identities $\nabla\times\nabla\alpha = 0$ and $\partial_t\nabla\alpha = \nabla\partial_t\alpha$, which are properties of $\alpha$. The state $\psi$ only *receives* the phase factor $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$; that factor does not feed back into $\boldsymbol{E}$ or $\boldsymbol{B}$. So the field-invariance statement holds whatever $\psi$ is carried along.

**(d)** What **changes** is the *description*: the local phase convention of the wavefunction ($\psi\to\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi$) and the kinematic labels built from the potentials — the canonical-momentum origin shifts by $q\boldsymbol{k}$ and the zero of the electrostatic energy $q\phi$ shifts by $q\omega$. What does **not** change is anything physical: the gauge-invariant fields $\boldsymbol{E},\boldsymbol{B}$, hence the Lorentz force $\boldsymbol{F} = q(\boldsymbol{E}+\boldsymbol{v}\times\boldsymbol{B})$, the probability density $\vert\psi\vert^2$, and the kinetic momentum / velocity. With $\alpha = \boldsymbol{k}\cdot\boldsymbol{r}-\omega t$ the transformation is a pure relabeling — a uniform shift of the canonical-momentum and energy origins — with no dynamical consequence.

<!-- ─── -->

**3. Covariance of derivatives.** Verify by direct computation that under $\psi\to\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi,\;\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha,\;\phi\to\phi-\partial_t\alpha$,

$$
\begin{split}
D'_{i}\psi' &= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}D_{i}\psi,\\
D'_{t}\psi' &= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}D_{t}\psi.
\end{split}
$$

(a) Carry out the spatial calculation explicitly in 1D, showing which $\partial_{x}\alpha$ terms cancel.

(b) Repeat for the time derivative, showing how the shift $\phi\to\phi-\partial_{t}\alpha$ cancels the $\partial_{t}\alpha$ term from differentiating $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$.

(c) Note that the spatial gauge shift uses $+\nabla\alpha$ while the temporal one uses $-\partial_{t}\alpha$. Explain in one sentence why these signs are opposite — what does that have to do with the opposite signs in $D_{i}$ vs $D_{t}$?

**Solution.**

**(a)** In 1D the spatial covariant derivative is $D_x = \partial_x - \mathrm{i}(q/\hbar)A_x$. Under the gauge transformation $A_x \to A_x + \partial_x\alpha$ and $\psi \to \psi' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi$,

$$
D'_x\psi' = \left(\partial_x - \mathrm{i}\frac{q}{\hbar}(A_x+\partial_x\alpha)\right)\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi.
$$

The product rule gives $\partial_x\bigl(\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\bigr) = \mathrm{i}(q/\hbar)(\partial_x\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi + \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\partial_x\psi$, so

$$
\begin{split}
D'_x\psi' &= \mathrm{i}\frac{q}{\hbar}(\partial_x\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi
+ \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\partial_x\psi
- \mathrm{i}\frac{q}{\hbar}A_x\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi
- \mathrm{i}\frac{q}{\hbar}(\partial_x\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\\
&= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\left(\partial_x - \mathrm{i}\frac{q}{\hbar}A_x\right)\psi
= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}D_x\psi.
\end{split}
$$

The first term ($+\mathrm{i}(q/\hbar)\partial_x\alpha$, from $\partial_x$ acting on the phase factor) cancels the last term ($-\mathrm{i}(q/\hbar)\partial_x\alpha$, from the shift of $A_x$). The two $\partial_x\alpha$ pieces are equal and opposite — that is the whole point of the construction.

**(b)** The temporal covariant derivative is $D_t = \partial_t + \mathrm{i}(q/\hbar)\phi$. Under $\phi \to \phi - \partial_t\alpha$,

$$
D'_t\psi' = \left(\partial_t + \mathrm{i}\frac{q}{\hbar}(\phi-\partial_t\alpha)\right)\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi.
$$

Using $\partial_t\bigl(\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\bigr) = \mathrm{i}(q/\hbar)(\partial_t\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi + \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\partial_t\psi$,

$$
\begin{split}
D'_t\psi' &= \mathrm{i}\frac{q}{\hbar}(\partial_t\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi
+ \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\partial_t\psi
+ \mathrm{i}\frac{q}{\hbar}\phi\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi
- \mathrm{i}\frac{q}{\hbar}(\partial_t\alpha)\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\\
&= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\left(\partial_t + \mathrm{i}\frac{q}{\hbar}\phi\right)\psi
= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}D_t\psi.
\end{split}
$$

The $+\mathrm{i}(q/\hbar)\partial_t\alpha$ generated by differentiating $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$ is cancelled by the $-\mathrm{i}(q/\hbar)\partial_t\alpha$ carried in by the shift $\phi \to \phi - \partial_t\alpha$ inside the term $+\mathrm{i}(q/\hbar)\phi$.

**(c)** In each covariant derivative the connection term must generate a piece $-\mathrm{i}(q/\hbar)(\partial\alpha)$ that cancels the $+\mathrm{i}(q/\hbar)(\partial\alpha)$ produced when the derivative hits the phase factor; since the spatial connection sits in $D_i = \partial_i - \mathrm{i}(q/\hbar)A_i$ with a **minus** sign while the temporal connection sits in $D_t = \partial_t + \mathrm{i}(q/\hbar)\phi$ with a **plus** sign (opposite signs mirroring the Lorentzian signature of spacetime), the potential shifts must carry opposite signs too — $+\nabla\alpha$ for $\boldsymbol{A}$ and $-\partial_t\alpha$ for $\phi$ — so that $(-)\times(+)$ and $(+)\times(-)$ both deliver the same cancelling term.

<!-- ─── -->

**4. Gauge on punctured plane.** Consider a particle restricted to the punctured plane $\mathbb{R}^{2}\setminus\{0\}$ (the origin removed). Let the gauge function be

$$
\alpha(\rho,\varphi)=\kappa\,\varphi,
$$

where $\varphi$ is the azimuthal angle and $\kappa$ is a constant.

(a) Compute $\nabla\alpha$ in polar coordinates and write the transformed vector-potential shift $\Delta\boldsymbol{A}=\nabla\alpha$.

(b) Show that $\nabla\times\nabla\alpha=0$ only away from the origin, so $\boldsymbol{B}$ is unchanged on the punctured plane. Then evaluate $\oint \nabla\alpha\cdot \mathrm{d}\boldsymbol{\ell}$ around a loop enclosing the hole and use Stokes/distribution language to explain why a singular magnetic flux $\Phi_{\mathrm{hole}}$ at the hole is required.

(c) Explain why this gauge function is not globally single-valued when $\varphi\to\varphi+2\pi$. What condition on $\kappa$ (in terms of $q$ and $\hbar$) makes the wavefunction phase factor $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$ single-valued after one full loop?

(d) Summarize the physical picture: outside the hole, local fields are unchanged; at the hole, a singular flux $\Phi_{\mathrm{hole}}$ carries the nontrivial holonomy. Explain why both statements are needed for a consistent global description.

**Solution.**

**(a)** In polar coordinates $\nabla = \boldsymbol{e}_\rho\,\partial_\rho + \boldsymbol{e}_\varphi\,\rho^{-1}\partial_\varphi$ (with $\boldsymbol{e}_\rho, \boldsymbol{e}_\varphi$ the polar basis unit vectors). Since $\alpha = \kappa\varphi$ depends only on $\varphi$, $\partial_\rho\alpha = 0$ and $\partial_\varphi\alpha = \kappa$, so

$$
\nabla\alpha = \frac{\kappa}{\rho}\,\boldsymbol{e}_\varphi,
\qquad
\Delta\boldsymbol{A} = \nabla\alpha = \frac{\kappa}{\rho}\,\boldsymbol{e}_\varphi.
$$

The shift is purely azimuthal and falls off as $1/\rho$.

**(b)** The $z$-component of the curl of a vector field $\boldsymbol{V} = V_\rho\boldsymbol{e}_\rho + V_\varphi\boldsymbol{e}_\varphi$ is $(\nabla\times\boldsymbol{V})_z = \rho^{-1}\bigl[\partial_\rho(\rho V_\varphi) - \partial_\varphi V_\rho\bigr]$. Here $V_\varphi = \kappa/\rho$ and $V_\rho = 0$, so $\rho V_\varphi = \kappa$ is constant and

$$
(\nabla\times\nabla\alpha)_z = \frac{1}{\rho}\,\partial_\rho(\kappa) = 0
\qquad (\rho > 0).
$$

Thus $\nabla\times\nabla\alpha = 0$ everywhere on the punctured plane, and $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ is unchanged there. Yet the circulation around a loop *enclosing* the hole does not vanish. On a circle of radius $\rho$, $\mathrm{d}\boldsymbol{\ell} = \boldsymbol{e}_\varphi\,\rho\,\mathrm{d}\varphi$, so

$$
\oint \nabla\alpha\cdot\mathrm{d}\boldsymbol{\ell}
= \int_0^{2\pi}\frac{\kappa}{\rho}\,(\rho\,\mathrm{d}\varphi)
= 2\pi\kappa \neq 0.
$$

By Stokes' theorem this circulation equals $\int(\nabla\times\nabla\alpha)\cdot\mathrm{d}\boldsymbol{S}$ over any surface spanning the loop. The integrand vanishes everywhere the surface stays on the punctured plane, yet the integral is $2\pi\kappa$ — a contradiction that is resolved only if $\nabla\times\nabla\alpha$ carries a singular contribution at the excluded origin,

$$
\nabla\times\nabla\alpha = 2\pi\kappa\,\delta^2(\boldsymbol{r})\,\boldsymbol{e}_z.
$$

The curl of the gradient is not globally zero — it is a point source. In field language, $\Delta\boldsymbol{A} = \nabla\alpha$ is the vector potential of a **singular magnetic flux line** $\Phi_{\mathrm{hole}} = \oint\Delta\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{\ell} = 2\pi\kappa$ threading the hole. A would-be "pure gauge" $\nabla\alpha$ built from a *multivalued* $\alpha$ is really a flux-carrying configuration: a consistent global description must place that flux somewhere, and the only location available is the excluded origin.

**(c)** The function $\alpha = \kappa\varphi$ jumps by $2\pi\kappa$ under $\varphi\to\varphi+2\pi$, so it is multivalued for any $\kappa\neq0$. The object that must be well defined is the wavefunction phase factor $\mathrm{e}^{\mathrm{i}q\alpha/\hbar} = \mathrm{e}^{\mathrm{i}q\kappa\varphi/\hbar}$; after one full loop it is multiplied by $\mathrm{e}^{2\pi\mathrm{i}q\kappa/\hbar}$. Single-valuedness of the wavefunction requires

$$
\mathrm{e}^{2\pi\mathrm{i}q\kappa/\hbar} = 1,
$$

equivalent to $q\kappa/\hbar = n$, i.e. $\kappa = n\hbar/q$ for $n\in\mathbb{Z}$.

Equivalently the inserted flux $\Phi_{\mathrm{hole}} = 2\pi\kappa = 2\pi n\hbar/q = n\,\Phi_0$ is an integer multiple of the **flux quantum for charge $q$**,

$$
\Phi_0 = \frac{2\pi\hbar}{q} = \frac{h}{q}
$$

(for an electron with $q=-e$ this is $h/e$; in a superconductor the Cooper-pair charge $2e$ gives the familiar $h/2e$). Only for $\kappa = n\hbar/q$ is the multivalued gauge function an admissible (genuinely redundant) transformation; for other $\kappa$ it shifts the physical Aharonov–Bohm phase and is not a redundancy.

**(d)** Outside the hole the transformation is locally indistinguishable from a trivial gauge change: $\nabla\times\nabla\alpha = 0$, so $\boldsymbol{B}$ and every *local* field measurement are untouched. At the hole, the multivaluedness is concentrated as a singular flux $\Phi_{\mathrm{hole}} = 2\pi\kappa$ carrying the nontrivial holonomy $\oint\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{\ell}$. Both statements are needed. The local statement says that no local probe can detect the change. The global statement says that a *non-local* probe — an interference experiment on a loop encircling the hole — does register it, through the Aharonov-Bohm phase $q\Phi_{\mathrm{hole}}/\hbar = 2\pi q\kappa/\hbar$. Reporting only the local fact would falsely conclude "nothing happened"; reporting only the flux would miss that the particle's accessible region is field-free. A topologically nontrivial domain — the puncture — is precisely where "gauge-equivalent" stops meaning "physically identical," unless the flux is quantized to $n\Phi_0$, in which case even the holonomy is trivial and the transformation is a true redundancy.

<!-- ─── -->

**5. What gauge transformations cannot do.** A particle moves in a *static* gravitational potential $V(\boldsymbol{r}) = mgz$, where $\boldsymbol{r}=(x,y,z)$ and $z$ is the vertical (height) coordinate. One might claim: "A spatial gauge transformation $\psi \to \mathrm{e}^{\mathrm{i}q\alpha(\boldsymbol{r})/\hbar}\psi$ should remove $V$ from the Schrödinger equation, just as it removes a static $\boldsymbol{A}$."

(a) Try to find $\alpha(\boldsymbol{r})$ that eliminates $V$. Where does the attempt fail?

(b) Allow $\alpha$ to depend on $t$. The only way to cancel $V$ in the $q\phi$ slot of the Hamiltonian is $-\partial_{t}\alpha = -V/q$, which forces $\alpha(\boldsymbol{r}, t) = (V(\boldsymbol{r})/q)\,t + g(\boldsymbol{r})$ for some $g$. Compute the resulting $\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha$ and show it is now *time-dependent*. Conclude that $V$ has not been removed — it has been shuffled into a time-dependent vector potential.

(c) Conclude: gauge transformations can shuffle physical content between $\phi$ and $\boldsymbol{A}$ but cannot erase it. The energy landscape of an external $V(\boldsymbol{r})$ is gauge-invariant — gravity does not arise from a $U(1)$ gauge redundancy.

**Solution.**

**(a)** A *static* gauge function $\alpha(\boldsymbol{r})$ has $\partial_t\alpha = 0$, so it shifts only the vector potential, $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$, and leaves the scalar potential entirely untouched, $\phi\to\phi-\partial_t\alpha = \phi$. In the Hamiltonian

$$
\hat{H} = \frac{(\hat{\boldsymbol{p}}-q\boldsymbol{A})^2}{2m} + q\phi,
$$

the gravitational potential sits in the $q\phi$ slot, $\phi = V/q = mgz/q$ — and a static $\alpha$ cannot reach that slot. One might instead hope to bury $V$ inside the kinetic term by a clever $\boldsymbol{A}$: but $(\hat{\boldsymbol{p}}-q\boldsymbol{A})^2/2m$ is *quadratic* in momentum, and no choice of $\boldsymbol{A}(\boldsymbol{r})$ produces a momentum-independent term $-V(\boldsymbol{r})$ — completing the square always leaves a residual term linear in $\hat{\boldsymbol{p}}$. The attempt fails because the redundancy generated by a static $\alpha$ is confined to $\boldsymbol{A}$, whereas $V$ lives in $\phi$.

**(b)** Allowing $\alpha(\boldsymbol{r},t)$, cancelling $V$ in the $q\phi$ slot requires $\phi' = \phi - \partial_t\alpha = 0$ with $q\phi = V$, i.e. $\partial_t\alpha = V/q$. Integrating,

$$
\alpha(\boldsymbol{r},t) = \frac{V(\boldsymbol{r})}{q}\,t + g(\boldsymbol{r}),
$$

for an arbitrary static $g(\boldsymbol{r})$. Starting from $\boldsymbol{A} = 0$, the resulting vector potential is

$$
\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha = \frac{t}{q}\,\nabla V + \nabla g = \frac{mg\,t}{q}\,\boldsymbol{e}_z + \nabla g,
$$

using $\nabla V = \nabla(mgz) = mg\,\boldsymbol{e}_z$. The $\boldsymbol{e}_z$-term (with $\boldsymbol{e}_z$ the unit vector along the $z$-axis) grows linearly in $t$: $\boldsymbol{A}'$ is explicitly **time-dependent**. The potential energy has not been removed — it has reappeared as a time-dependent vector potential. Consistently, the gauge-invariant field is unchanged: before, $\boldsymbol{E} = -\nabla\phi = -(mg/q)\boldsymbol{e}_z$; after,

$$
\boldsymbol{E}' = -\nabla\phi' - \partial_t\boldsymbol{A}' = 0 - \frac{mg}{q}\,\boldsymbol{e}_z = \boldsymbol{E}.
$$

The transformation moved the physics out of $\phi$ and into $\boldsymbol{A}$ without erasing it.

**(c)** A gauge transformation can **shuffle** physical content between $\phi$ and $\boldsymbol{A}$ but cannot **erase** it: the invariant combination $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ — here the uniform $-(mg/q)\boldsymbol{e}_z$ — is fixed under every gauge choice. The energy landscape of an external $V(\boldsymbol{r})$ is gauge-invariant physical input. Unlike the *phase of $\psi$*, which is local internal data and therefore a redundancy, the gravitational potential is not a redundancy of the $U(1)$ description and cannot be gauged away. Gravity does not arise from a $U(1)$ phase redundancy. (Gravity is governed by a different local invariance — general covariance / diffeomorphisms — which lies outside the $U(1)$ gauge principle of this section.)

<!-- ─── -->

★ **6. Second-order bilinear covariance.** Consider the same local phase redundancy

$$
\psi' = \mathrm{e}^{\mathrm{i}q\alpha(\boldsymbol r)/\hbar}\psi.
$$

For second spatial derivatives, study the bilinear combination

$$
\partial_{ij}[\psi]\equiv \psi\,\partial_i\partial_j\psi-(\partial_i\psi)(\partial_j\psi).
$$

(a) Expand $\partial_{ij}[\psi']$ explicitly and show that the non-covariant remainder equals $(\mathrm{i}q/\hbar)(\partial_i\partial_j\alpha)\psi^2 \cdot \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}$.

(b) Introduce a symmetric rank-2 gauge field $A_{ij}=A_{ji}$ and define

$$
\mathcal{D}_{ij}[\psi]\equiv \psi\,\partial_i\partial_j\psi-(\partial_i\psi)(\partial_j\psi)-\mathrm{i}\frac{q}{\hbar}A_{ij}\psi^2.
$$

Find the transformation law for $A_{ij}$ such that

$$
\mathcal{D}'_{ij}[\psi'] = \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\,\mathcal{D}_{ij}[\psi].
$$

(c) Explain why the first two terms must appear together (not separately) to make this construction work.

(d) Build one gauge-invariant scalar density from $\mathcal{D}_{ij}[\psi]$ and $\psi$ (for example using index contraction and complex conjugation), and state in one sentence what physical type of constrained motion this kind of second-derivative gauge structure is designed to capture.

**Solution.**

Write $\Lambda \equiv q\alpha/\hbar$, so $\psi' = \mathrm{e}^{\mathrm{i}\Lambda}\psi$ and $\partial_i\psi' = \mathrm{e}^{\mathrm{i}\Lambda}\bigl(\partial_i\psi + \mathrm{i}(\partial_i\Lambda)\psi\bigr)$.

**(a)** Differentiating once more,

$$
\partial_i\partial_j\psi' = \mathrm{e}^{\mathrm{i}\Lambda}\Bigl[\partial_i\partial_j\psi + \mathrm{i}(\partial_i\Lambda)\partial_j\psi + \mathrm{i}(\partial_j\Lambda)\partial_i\psi + \mathrm{i}(\partial_i\partial_j\Lambda)\psi - (\partial_i\Lambda)(\partial_j\Lambda)\psi\Bigr].
$$

The two terms of $\partial_{ij}[\psi']$ are therefore

$$
\psi'\,\partial_i\partial_j\psi' = \mathrm{e}^{2\mathrm{i}\Lambda}\,\psi\Bigl[\partial_i\partial_j\psi + \mathrm{i}(\partial_i\Lambda)\partial_j\psi + \mathrm{i}(\partial_j\Lambda)\partial_i\psi + \mathrm{i}(\partial_i\partial_j\Lambda)\psi - (\partial_i\Lambda)(\partial_j\Lambda)\psi\Bigr],
$$

$$
(\partial_i\psi')(\partial_j\psi') = \mathrm{e}^{2\mathrm{i}\Lambda}\Bigl[(\partial_i\psi)(\partial_j\psi) + \mathrm{i}(\partial_j\Lambda)\psi\,\partial_i\psi + \mathrm{i}(\partial_i\Lambda)\psi\,\partial_j\psi - (\partial_i\Lambda)(\partial_j\Lambda)\psi^2\Bigr].
$$

Subtracting, the three pieces $\mathrm{i}(\partial_i\Lambda)\psi\,\partial_j\psi$, $\mathrm{i}(\partial_j\Lambda)\psi\,\partial_i\psi$, and $-(\partial_i\Lambda)(\partial_j\Lambda)\psi^2$ are common to both lines and cancel, leaving

$$
\partial_{ij}[\psi'] = \mathrm{e}^{2\mathrm{i}\Lambda}\Bigl[\psi\,\partial_i\partial_j\psi - (\partial_i\psi)(\partial_j\psi) + \mathrm{i}(\partial_i\partial_j\Lambda)\psi^2\Bigr]
= \mathrm{e}^{2\mathrm{i}\Lambda}\Bigl[\partial_{ij}[\psi] + \mathrm{i}(\partial_i\partial_j\Lambda)\psi^2\Bigr].
$$

With $\Lambda = q\alpha/\hbar$, so $\partial_i\partial_j\Lambda = (q/\hbar)\partial_i\partial_j\alpha$,

$$
\partial_{ij}[\psi'] = \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\,\partial_{ij}[\psi] + \frac{\mathrm{i}q}{\hbar}(\partial_i\partial_j\alpha)\,\psi^2\,\mathrm{e}^{2\mathrm{i}q\alpha/\hbar}.
$$

Every term containing a *first* derivative of $\alpha$ has cancelled; the non-covariant remainder is exactly $(\mathrm{i}q/\hbar)(\partial_i\partial_j\alpha)\psi^2\cdot\mathrm{e}^{2\mathrm{i}q\alpha/\hbar}$, as claimed.

**(b)** Using $\psi'^2 = \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\psi^2$ together with the result of (a),

$$
\mathcal{D}'_{ij}[\psi'] = \partial_{ij}[\psi'] - \frac{\mathrm{i}q}{\hbar}A'_{ij}\psi'^2
= \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\Bigl[\partial_{ij}[\psi] + \frac{\mathrm{i}q}{\hbar}(\partial_i\partial_j\alpha)\psi^2 - \frac{\mathrm{i}q}{\hbar}A'_{ij}\psi^2\Bigr].
$$

This equals $\mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\,\mathcal{D}_{ij}[\psi] = \mathrm{e}^{2\mathrm{i}q\alpha/\hbar}\bigl[\partial_{ij}[\psi] - \mathrm{i}(q/\hbar)A_{ij}\psi^2\bigr]$ if and only if $(\partial_i\partial_j\alpha) - A'_{ij} = -A_{ij}$, i.e.

$$
A_{ij} \to A'_{ij} = A_{ij} + \partial_i\partial_j\alpha.
$$

The inhomogeneous shift $\partial_i\partial_j\alpha$ is automatically symmetric in $i,j$, consistent with $A_{ij} = A_{ji}$; it is the rank-2 analogue of $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$, carrying one extra derivative.

**(c)** Neither term transforms cleanly on its own. From the expansion in (a), $\psi\,\partial_i\partial_j\psi$ alone picks up $\mathrm{i}(\partial_i\Lambda)\psi\,\partial_j\psi + \mathrm{i}(\partial_j\Lambda)\psi\,\partial_i\psi - (\partial_i\Lambda)(\partial_j\Lambda)\psi^2 + \mathrm{i}(\partial_i\partial_j\Lambda)\psi^2$, and $(\partial_i\psi)(\partial_j\psi)$ alone picks up the *same* first three pieces. Each separately carries artifacts proportional to $\partial\Lambda$ and $(\partial\Lambda)^2$ that no single linear shift of one field could absorb. Only their **difference** cancels all of those, leaving the lone inhomogeneous piece $\mathrm{i}(\partial_i\partial_j\Lambda)\psi^2$ — and an inhomogeneous shift linear in $\partial_i\partial_j\alpha$ is precisely what a connection field $A_{ij}$ can soak up. Pairing the second-derivative term with the product-of-first-derivatives term is the rank-2 echo of why $D_i = \partial_i - \mathrm{i}(q/\hbar)A_i$ pairs a derivative with a connection: the combination is engineered so that the redundancy artifact collapses to a pure connection shift.

**(d)** The object $\mathcal{D}_{ij}[\psi]$ carries phase weight $\mathrm{e}^{2\mathrm{i}q\alpha/\hbar}$ (the same weight as $\psi^2$), and its complex conjugate carries $\mathrm{e}^{-2\mathrm{i}q\alpha/\hbar}$. Contracting the symmetric index pair with $\delta^{ij}$ to form a scalar and taking the modulus squared,

$$
\mathcal{S}[\psi] \equiv \sum_{i,j}\bigl\vert\mathcal{D}_{ij}[\psi]\bigr\vert^2 = \sum_{i,j}\overline{\mathcal{D}_{ij}[\psi]}\;\mathcal{D}_{ij}[\psi],
$$

transforms by $\mathrm{e}^{-2\mathrm{i}q\alpha/\hbar}\,\mathrm{e}^{+2\mathrm{i}q\alpha/\hbar} = 1$ — a **gauge-invariant scalar density**. (Equivalently, $\delta^{ij}\,\bar{\psi}^2\,\mathcal{D}_{ij}[\psi]$ is invariant, the factor $\bar{\psi}^2$ supplying the cancelling $\mathrm{e}^{-2\mathrm{i}q\alpha/\hbar}$.) This rank-2 connection pattern is the same algebraic idea used in more advanced models with restricted-mobility matter, where second-derivative couplings enforce *restricted mobility* — matter that carries charge and dipole quantum numbers and cannot move as freely as in ordinary electromagnetism. That application lies beyond the minimal $U(1)$ gauge principle of §4.1.1, but the bilinear pairing in (c) is exactly what makes the construction work here.

<!-- ─── -->

**7. Gauge connection on links.** Consider a one-dimensional tight-binding model with hopping between neighboring sites $n$ and $n+1$:

$$
\hat{H}_{\text{hop}}=-t\sum_n \left(U_{n,n+1}\,\hat{c}_{n+1}^{\dagger}\hat{c}_n+\text{h.c.}\right),
$$

where $U_{n,n+1}=\mathrm{e}^{\mathrm{i}q a A_n/\hbar}$ is a link variable and $a$ is the lattice spacing. Under a local phase redefinition,

$$
\hat{c}_n\to \mathrm{e}^{\mathrm{i}q\alpha_n/\hbar}\hat{c}_n.
$$

(a) Find how $U_{n,n+1}$ must transform so that each hopping term remains invariant.

(b) Translate your answer into a transformation law for $A_n$. Show that, in the continuum limit, it becomes $A\to A+\partial_x\alpha$.

(c) Explain why the link variable is the lattice version of a connection: what does it compare between neighboring sites, and why is it forced by local phase redundancy?

**Solution.**

**(a)** Under $\hat{c}_n \to \mathrm{e}^{\mathrm{i}q\alpha_n/\hbar}\hat{c}_n$ the creation operator transforms as $\hat{c}_n^\dagger \to \mathrm{e}^{-\mathrm{i}q\alpha_n/\hbar}\hat{c}_n^\dagger$, so the bare neighbour bilinear becomes

$$
\hat{c}_{n+1}^\dagger\hat{c}_n \to \mathrm{e}^{-\mathrm{i}q\alpha_{n+1}/\hbar}\,\mathrm{e}^{\mathrm{i}q\alpha_n/\hbar}\,\hat{c}_{n+1}^\dagger\hat{c}_n = \mathrm{e}^{-\mathrm{i}q(\alpha_{n+1}-\alpha_n)/\hbar}\,\hat{c}_{n+1}^\dagger\hat{c}_n.
$$

For the hopping term $U_{n,n+1}\,\hat{c}_{n+1}^\dagger\hat{c}_n$ to stay invariant, the link variable must absorb the inverse factor:

$$
U_{n,n+1} \to U'_{n,n+1} = \mathrm{e}^{\mathrm{i}q\alpha_{n+1}/\hbar}\,U_{n,n+1}\,\mathrm{e}^{-\mathrm{i}q\alpha_n/\hbar}.
$$

Check: $U'_{n,n+1}\,\hat{c}_{n+1}^{\prime\dagger}\hat{c}'_n = \mathrm{e}^{\mathrm{i}q\alpha_{n+1}/\hbar}U_{n,n+1}\mathrm{e}^{-\mathrm{i}q\alpha_n/\hbar}\cdot\mathrm{e}^{-\mathrm{i}q\alpha_{n+1}/\hbar}\mathrm{e}^{\mathrm{i}q\alpha_n/\hbar}\,\hat{c}_{n+1}^\dagger\hat{c}_n = U_{n,n+1}\,\hat{c}_{n+1}^\dagger\hat{c}_n$, and the Hermitian conjugate term is then invariant automatically. The link variable picks up the phase of the site it points *to* and the inverse phase of the site it points *from* — a parallel-transport law.

**(b)** Writing $U_{n,n+1} = \mathrm{e}^{\mathrm{i}qaA_n/\hbar}$ and $U'_{n,n+1} = \mathrm{e}^{\mathrm{i}qaA'_n/\hbar}$, all factors are c-numbers, so exponents add:

$$
\frac{qa}{\hbar}A'_n = \frac{qa}{\hbar}A_n + \frac{q}{\hbar}(\alpha_{n+1}-\alpha_n),
$$

so $A'_n = A_n + (\alpha_{n+1}-\alpha_n)/a$.

In the continuum limit $a\to0$, label sites by position $x$ with $\alpha_n = \alpha(x)$ and $\alpha_{n+1} = \alpha(x+a)$:

$$
\frac{\alpha_{n+1}-\alpha_n}{a} = \frac{\alpha(x+a)-\alpha(x)}{a} \xrightarrow[a\to0]{} \partial_x\alpha,
$$

which is the definition of the derivative. Hence $A \to A + \partial_x\alpha$ — exactly the continuum gauge transformation $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$ restricted to one dimension.

**(c)** The link variable $U_{n,n+1}$ lives on the *bond* between sites $n$ and $n+1$, not on a site. It is a **parallel transporter**: it specifies how to carry the phase convention of site $n$ over to site $n+1$ so that the two can be compared. The phase of $\hat{c}_n$ at each site is local internal data with an independently choosable convention, so the bare neighbour comparison $\hat{c}_{n+1}^\dagger\hat{c}_n$ has no convention-independent meaning — under a local rephasing it changes by $\mathrm{e}^{-\mathrm{i}q(\alpha_{n+1}-\alpha_n)/\hbar}$. The link variable is *forced* to exist precisely because only a quantity transforming by exactly the endpoint phases can soak up that relative phase and render the hopping term gauge-invariant. That is the defining property of a connection: it compares internal data at neighbouring points. Thus $U_{n,n+1}$ is the lattice connection, $A_n$ is its potential, the Peierls phase $\mathrm{e}^{\mathrm{i}qaA_n/\hbar}$ is the lattice realization of minimal coupling, and $\partial_x\alpha$ emerges as the continuum gauge-transformation law.
