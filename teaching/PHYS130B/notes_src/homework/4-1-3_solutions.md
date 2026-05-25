# 4.1.3 Gauge Invariance
Worked solutions for the homework problems in the [4.1.3 Gauge Invariance](../ch4_phase-and-gauge/4-1-3-gauge-invariance) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Gauge-transforming an observable.** Consider the expectation value $\langle\hat{O}\rangle = \langle\psi\vert\hat{O}\vert\psi\rangle$.

(a) Under the gauge transformation $\vert\psi\rangle \to \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\vert\psi\rangle$, show that $\langle\hat{O}\rangle$ is invariant if and only if $[\hat{O}, \mathrm{e}^{\mathrm{i}q\alpha/\hbar}] = 0$. Which familiar operators satisfy this, and which do not?

(b) One claims that $\langle\hat{\boldsymbol{p}}\rangle$ is gauge-invariant because "momentum is physical." Find the flaw by computing $\langle\hat{\boldsymbol{p}}\rangle$ in two gauges for a particle in a uniform field $\boldsymbol{B} = B\boldsymbol{e}_z$ (with $\boldsymbol{e}_z$ the unit vector along the $z$-axis).

(c) Construct a gauge-invariant momentum operator from $\hat{\boldsymbol{p}}$ and $\boldsymbol{A}$.

**Solution.**

**(a)** Write the rephased state as $\vert\psi'\rangle = \hat{U}\vert\psi\rangle$ with the
unitary multiplication operator $\hat{U} = \mathrm{e}^{\mathrm{i}q\alpha(\hat{\boldsymbol{x}})/\hbar}$.
Holding the operator $\hat{O}$ fixed, its expectation in the new state is

$$
\langle\hat{O}\rangle' = \langle\psi'\vert\hat{O}\vert\psi'\rangle
= \langle\psi\vert\hat{U}^\dagger\hat{O}\hat{U}\vert\psi\rangle .
$$

If $[\hat{O},\hat{U}] = 0$ then $\hat{U}^\dagger\hat{O}\hat{U} = \hat{U}^\dagger\hat{U}\hat{O} = \hat{O}$,
so $\langle\hat{O}\rangle' = \langle\hat{O}\rangle$ for every state — invariance holds.
Conversely, suppose $\langle\hat{O}\rangle' = \langle\hat{O}\rangle$ for *all* $\vert\psi\rangle$.
Then the Hermitian operator $\hat{U}^\dagger\hat{O}\hat{U} - \hat{O}$ has vanishing
expectation in every state, and an operator with zero expectation in every state
is the zero operator. Hence $\hat{U}^\dagger\hat{O}\hat{U} = \hat{O}$, i.e.
$\hat{O}\hat{U} = \hat{U}\hat{O}$, which is $[\hat{O},\hat{U}] = 0$. This proves the
"if and only if."

Since $\hat{U} = \mathrm{e}^{\mathrm{i}q\alpha(\hat{\boldsymbol{x}})/\hbar}$ is a function of
position, the operators that commute with it are exactly the functions of
position: $\hat{\boldsymbol{x}}$ itself, any potential $V(\hat{\boldsymbol{x}})$, the
projector $\vert\boldsymbol{r}\rangle\langle\boldsymbol{r}\vert$ onto a position
eigenstate (hence the probability density $\rho = \vert\psi\vert^2$). Operators
built from $\hat{\boldsymbol{p}} = -\mathrm{i}\hbar\nabla$ do **not** commute with
$\hat{U}$: the canonical momentum $\hat{\boldsymbol{p}}$, the kinetic energy, the
canonical Hamiltonian. The lesson is that "gauge invariance of an observable"
cannot mean "its expectation in the rephased state is unchanged while the
operator stays fixed" — for almost every interesting operator that fails. The
operator must itself be re-expressed in the new gauge (see part (c)).

**(b)** Take the two standard gauges for $\boldsymbol{B} = B\boldsymbol{e}_z$: the symmetric
gauge $\boldsymbol{A}_{\mathrm{S}} = \tfrac{B}{2}(-y,x,0)$ and the Landau gauge
$\boldsymbol{A}_{\mathrm{L}} = (0,Bx,0)$. They are related by $\boldsymbol{A}_{\mathrm{L}} = \boldsymbol{A}_{\mathrm{S}} + \nabla\alpha$ with

$$
\alpha = \tfrac{B}{2}xy,
\qquad
\nabla\alpha = \tfrac{B}{2}(y,x,0),
$$

since $\boldsymbol{A}_{\mathrm{S}} + \nabla\alpha = \tfrac{B}{2}(-y,x,0) + \tfrac{B}{2}(y,x,0) = (0,Bx,0)$.
The *same physical state* is described by $\psi_{\mathrm{S}}$ in gauge S and by
$\psi_{\mathrm{L}} = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_{\mathrm{S}}$ in gauge L.
Using the conjugation identity from the preamble,

$$
\begin{split}
\langle\hat{\boldsymbol{p}}\rangle_{\mathrm{L}}
&= \langle\psi_{\mathrm{L}}\vert\hat{\boldsymbol{p}}\vert\psi_{\mathrm{L}}\rangle
 = \langle\psi_{\mathrm{S}}\vert\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}\hat{\boldsymbol{p}}\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\vert\psi_{\mathrm{S}}\rangle \\
&= \langle\psi_{\mathrm{S}}\vert\,(\hat{\boldsymbol{p}} + q\nabla\alpha)\,\vert\psi_{\mathrm{S}}\rangle
 = \langle\hat{\boldsymbol{p}}\rangle_{\mathrm{S}} + q\langle\nabla\alpha\rangle .
\end{split}
$$

With $\nabla\alpha = \tfrac{B}{2}(y,x,0)$ this gives $\langle\hat{\boldsymbol{p}}\rangle_{\mathrm{L}} = \langle\hat{\boldsymbol{p}}\rangle_{\mathrm{S}} + \tfrac{qB}{2}(\langle y\rangle,\langle x\rangle,0)$,
which differs from $\langle\hat{\boldsymbol{p}}\rangle_{\mathrm{S}}$ whenever
$\langle x\rangle$ or $\langle y\rangle$ is nonzero (the shift vanishes only for states
centred at the origin, with $\langle x\rangle = \langle y\rangle = 0$). So
$\langle\hat{\boldsymbol{p}}\rangle$ is **gauge-dependent**.
The flaw in the claim is the identification of $\hat{\boldsymbol{p}} = -\mathrm{i}\hbar\nabla$
with "physical momentum." The canonical momentum measures the *phase gradient* of
the wavefunction, and the gauge phase $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$ changes
that gradient. The physical (mechanical) momentum is $m\hat{\boldsymbol{v}} = \hat{\boldsymbol{\pi}}$.

**(c)** The gauge-invariant momentum is the **kinetic momentum**

$$
\hat{\boldsymbol{\pi}} = \hat{\boldsymbol{p}} - q\boldsymbol{A} = m\hat{\boldsymbol{v}} .
$$

Under the gauge transformation the operator must be rebuilt with the new
potential, $\hat{\boldsymbol{\pi}}' = \hat{\boldsymbol{p}} - q\boldsymbol{A}' = \hat{\boldsymbol{p}} - q\boldsymbol{A} - q\nabla\alpha$. Conjugating by the phase,

$$
\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}\,\hat{\boldsymbol{\pi}}'\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}
= (\hat{\boldsymbol{p}} + q\nabla\alpha) - q\boldsymbol{A} - q\nabla\alpha
= \hat{\boldsymbol{p}} - q\boldsymbol{A} = \hat{\boldsymbol{\pi}} ,
$$

because $q\boldsymbol{A}$ and $q\nabla\alpha$ are functions of position and pass
through the phase untouched. Therefore

$$
\langle\hat{\boldsymbol{\pi}}'\rangle' = \langle\psi'\vert\hat{\boldsymbol{\pi}}'\vert\psi'\rangle
= \langle\psi\vert\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}\hat{\boldsymbol{\pi}}'\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\vert\psi\rangle
= \langle\hat{\boldsymbol{\pi}}\rangle .
$$

This is the precise sense of gauge invariance for an operator: $\hat{\boldsymbol{\pi}}$
transforms by conjugation, $\hat{\boldsymbol{\pi}}' = \hat{U}\hat{\boldsymbol{\pi}}\hat{U}^\dagger$,
so that its expectation value is the same number in every gauge.

<!-- ─── -->

**2. Probability current.** The probability current is $\boldsymbol{j} = \frac{1}{m}\mathrm{Re}(\psi^*\hat{\boldsymbol{\pi}}\psi)$ with $\hat{\boldsymbol{\pi}} = \hat{\boldsymbol{p}} - q\boldsymbol{A}$.

(a) Show that $\boldsymbol{j}$ is gauge-invariant.

(b) Show that the continuity equation $\partial_t\vert\psi\vert^2 + \nabla \cdot \boldsymbol{j} = 0$ holds in every gauge.

**Solution.**

**(a)** Expanding $\hat{\boldsymbol{\pi}} = -\mathrm{i}\hbar\nabla - q\boldsymbol{A}$, the
current is

$$
\boldsymbol{j} = \frac{1}{m}\mathrm{Re}\bigl(\psi^*(-\mathrm{i}\hbar\nabla - q\boldsymbol{A})\psi\bigr)
= \frac{\hbar}{m}\mathrm{Im}(\psi^*\nabla\psi) - \frac{q}{m}\boldsymbol{A}\,\vert\psi\vert^2 ,
$$

using $\mathrm{Re}(-\mathrm{i}\hbar\,\psi^*\nabla\psi) = \hbar\,\mathrm{Im}(\psi^*\nabla\psi)$
and that $-q\boldsymbol{A}\vert\psi\vert^2$ is already real. The fastest invariance
proof uses the **homogeneous transformation of $\hat{\boldsymbol{\pi}}\psi$**
established for the covariant derivative in §4.1.1: under the gauge transformation

$$
\hat{\boldsymbol{\pi}}'\psi' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\hat{\boldsymbol{\pi}}\psi .
$$

Then $\psi'^*\,\hat{\boldsymbol{\pi}}'\psi' = \bigl(\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\bigr)^*\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{\boldsymbol{\pi}}\psi = \psi^*\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\hat{\boldsymbol{\pi}}\psi = \psi^*\,\hat{\boldsymbol{\pi}}\psi$, so $\boldsymbol{j}' = \boldsymbol{j}$ immediately.

It is instructive to see the cancellation term by term as well. Under
$\psi \to \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi$,

$$
\nabla\psi' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\Bigl(\nabla\psi + \tfrac{\mathrm{i}q}{\hbar}(\nabla\alpha)\psi\Bigr),
\qquad
\psi'^*\nabla\psi' = \psi^*\nabla\psi + \tfrac{\mathrm{i}q}{\hbar}(\nabla\alpha)\vert\psi\vert^2 ,
$$

so $\mathrm{Im}(\psi'^*\nabla\psi') = \mathrm{Im}(\psi^*\nabla\psi) + \tfrac{q}{\hbar}(\nabla\alpha)\vert\psi\vert^2$.
The first term of $\boldsymbol{j}$ therefore gains $\tfrac{q}{m}(\nabla\alpha)\vert\psi\vert^2$,
while the second term, with $\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha$ and
$\vert\psi'\vert^2 = \vert\psi\vert^2$, gains $-\tfrac{q}{m}(\nabla\alpha)\vert\psi\vert^2$.
The two changes cancel exactly:

$$
\boldsymbol{j}' = \frac{\hbar}{m}\mathrm{Im}(\psi^*\nabla\psi) + \frac{q}{m}(\nabla\alpha)\vert\psi\vert^2
- \frac{q}{m}(\boldsymbol{A} + \nabla\alpha)\vert\psi\vert^2 = \boldsymbol{j} .
$$

The current is gauge-invariant because the $\nabla\alpha$ injected by the rephased
wavefunction is precisely the $\nabla\alpha$ absorbed into $\boldsymbol{A}$.

**(b)** Write the current with the covariant derivative $\boldsymbol{D} = \nabla - \tfrac{\mathrm{i}q}{\hbar}\boldsymbol{A}$,
so that $\hat{\boldsymbol{\pi}}\psi = -\mathrm{i}\hbar\,\boldsymbol{D}\psi$ and

$$
\boldsymbol{j} = \frac{\hbar}{m}\mathrm{Im}(\psi^*\boldsymbol{D}\psi)
= \frac{\hbar}{2\mathrm{i}m}\bigl(\psi^*\boldsymbol{D}\psi - \psi\,\boldsymbol{D}^*\psi^*\bigr),
\qquad \boldsymbol{D}^* = \nabla + \tfrac{\mathrm{i}q}{\hbar}\boldsymbol{A} .
$$

Differentiate the density using the Schrödinger equation $\mathrm{i}\hbar\partial_t\psi = \hat{H}\psi$
with $\hat{H} = \hat{\boldsymbol{\pi}}^2/2m + q\phi$:

$$
\partial_t\vert\psi\vert^2 = \psi^*\partial_t\psi + \psi\,\partial_t\psi^*
= \frac{1}{\mathrm{i}\hbar}\bigl[\psi^*(\hat{H}\psi) - \psi(\hat{H}\psi)^*\bigr]
= \frac{2}{\hbar}\,\mathrm{Im}\bigl(\psi^*\hat{H}\psi\bigr) .
$$

The scalar-potential term contributes nothing: $\psi^*(q\phi)\psi = q\phi\vert\psi\vert^2$
is real, so $\mathrm{Im}$ kills it. Only the kinetic term survives, and with
$\hat{\boldsymbol{\pi}}^2 = -\hbar^2\boldsymbol{D}^2$,

$$
\partial_t\vert\psi\vert^2
= \frac{1}{\hbar m}\,\mathrm{Im}\bigl(\psi^*\hat{\boldsymbol{\pi}}^2\psi\bigr)
= -\frac{\hbar}{m}\,\mathrm{Im}\bigl(\psi^*\boldsymbol{D}^2\psi\bigr)
= -\frac{\hbar}{2\mathrm{i}m}\bigl(\psi^*\boldsymbol{D}^2\psi - \psi\,(\boldsymbol{D}^*)^2\psi^*\bigr).
$$

The covariant derivative obeys a Leibniz identity in which $\boldsymbol{D}$ on a ket
pairs with $\boldsymbol{D}^*$ on a bra, the $\boldsymbol{A}$ terms cancelling:
$\nabla\cdot(\psi^*\boldsymbol{V}) = (\boldsymbol{D}^*\psi^*)\cdot\boldsymbol{V} + \psi^*(\boldsymbol{D}\cdot\boldsymbol{V})$.
Applying it with $\boldsymbol{V} = \boldsymbol{D}\psi$ and with $\boldsymbol{V} = \boldsymbol{D}^*\psi^*$,

$$
\begin{split}
\nabla\cdot(\psi^*\boldsymbol{D}\psi) &= (\boldsymbol{D}^*\psi^*)\cdot(\boldsymbol{D}\psi) + \psi^*\boldsymbol{D}^2\psi , \\
\nabla\cdot(\psi\,\boldsymbol{D}^*\psi^*) &= (\boldsymbol{D}\psi)\cdot(\boldsymbol{D}^*\psi^*) + \psi\,(\boldsymbol{D}^*)^2\psi^* .
\end{split}
$$

Subtracting, the symmetric cross terms cancel and

$$
\nabla\cdot\bigl(\psi^*\boldsymbol{D}\psi - \psi\,\boldsymbol{D}^*\psi^*\bigr)
= \psi^*\boldsymbol{D}^2\psi - \psi\,(\boldsymbol{D}^*)^2\psi^* .
$$

Multiplying by $\hbar/(2\mathrm{i}m)$, the right side is the negative of the
expression for $\partial_t\vert\psi\vert^2$, while the left side is $\nabla\cdot\boldsymbol{j}$.
Hence

$$
\partial_t\vert\psi\vert^2 + \nabla\cdot\boldsymbol{j} = 0 .
$$

This holds **in every gauge** for two independent reasons. First, the derivation
above never selected a gauge — it used only the Schrödinger equation with
arbitrary $(\boldsymbol{A},\phi)$, so it is valid for any choice. Second, by part (a)
both $\rho = \vert\psi\vert^2$ and $\boldsymbol{j}$ are gauge-invariant; the continuity
equation is therefore literally the *same* equation, relating the *same* two
gauge-invariant fields, no matter which gauge one computes in.

<!-- ─── -->

**3. Canonical momentum shifts.** Two physicists compute $\langle\hat{\boldsymbol{p}}\rangle$ for the same electron in a uniform magnetic field $\boldsymbol{B} = B\boldsymbol{e}_z$. Physicist A uses the symmetric gauge $\boldsymbol{A} = \frac{B}{2}(-y, x, 0)$; physicist B uses the Landau gauge $\boldsymbol{A} = (0, Bx, 0)$.

(a) Explain why they get different values of $\langle\hat{\boldsymbol{p}}\rangle$.

(b) Show that both agree on $\langle\hat{\boldsymbol{\pi}}\rangle$.

(c) Which quantity would be measured in an experiment?

**Solution.**

**(a)** The two gauges describe the *same* magnetic field — both have
$\nabla\times\boldsymbol{A} = B\boldsymbol{e}_z$ — and therefore the *same* physical electron.
They are connected by the gauge transformation found in Problem 1(b),

$$
\boldsymbol{A}_{\mathrm{B}} = \boldsymbol{A}_{\mathrm{A}} + \nabla\alpha,
\qquad \alpha = \tfrac{B}{2}xy,
\qquad \nabla\alpha = \tfrac{B}{2}(y,x,0),
$$

so the electron's wavefunction is $\psi_{\mathrm{A}}$ for physicist A and
$\psi_{\mathrm{B}} = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_{\mathrm{A}}$ for
physicist B. Their canonical-momentum expectations differ by

$$
\langle\hat{\boldsymbol{p}}\rangle_{\mathrm{B}} - \langle\hat{\boldsymbol{p}}\rangle_{\mathrm{A}}
= q\langle\nabla\alpha\rangle
= \frac{qB}{2}\bigl(\langle y\rangle,\,\langle x\rangle,\,0\bigr),
$$

which is nonzero whenever $\langle x\rangle$ or $\langle y\rangle$ is nonzero (only
states with $\langle x\rangle = \langle y\rangle = 0$ give the same canonical-momentum
expectation in both gauges).

The reason is structural: $\hat{\boldsymbol{p}} = -\mathrm{i}\hbar\nabla$ reads off the
*phase gradient* of the wavefunction, and the two physicists' wavefunctions differ
by the position-dependent phase $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$. A different
gauge is a different bookkeeping convention for splitting the phase between $\psi$
and $\boldsymbol{A}$; the canonical momentum is sensitive to that split. It is a
gauge-dependent label, not a physical quantity.

**(b)** The kinetic momentum is $\hat{\boldsymbol{\pi}} = \hat{\boldsymbol{p}} - q\boldsymbol{A}$,
built with each physicist's own potential. For physicist B,

$$
\begin{split}
\langle\hat{\boldsymbol{\pi}}\rangle_{\mathrm{B}}
&= \langle\hat{\boldsymbol{p}}\rangle_{\mathrm{B}} - q\langle\boldsymbol{A}_{\mathrm{B}}\rangle
 = \bigl(\langle\hat{\boldsymbol{p}}\rangle_{\mathrm{A}} + q\langle\nabla\alpha\rangle\bigr)
   - q\langle\boldsymbol{A}_{\mathrm{A}} + \nabla\alpha\rangle \\
&= \langle\hat{\boldsymbol{p}}\rangle_{\mathrm{A}} - q\langle\boldsymbol{A}_{\mathrm{A}}\rangle
 = \langle\hat{\boldsymbol{\pi}}\rangle_{\mathrm{A}} .
\end{split}
$$

The $q\langle\nabla\alpha\rangle$ picked up by the canonical momentum is exactly the
$q\langle\nabla\alpha\rangle$ added to $q\boldsymbol{A}$; they cancel. Both physicists
agree on $\langle\hat{\boldsymbol{\pi}}\rangle = m\langle\hat{\boldsymbol{v}}\rangle$.

**(c)** An experiment measures the **kinetic momentum** $\langle\hat{\boldsymbol{\pi}}\rangle = m\langle\hat{\boldsymbol{v}}\rangle$ — the quantity tied to the electron's actual
motion (its velocity, its cyclotron radius $r_c = m v_\perp/qB$, the current it
carries, its time-of-flight). This is gauge-invariant, so both physicists predict
the same measurable result. The canonical momentum $\langle\hat{\boldsymbol{p}}\rangle$
is never measured directly: it is not even well-defined until a gauge is chosen,
and different legitimate choices give different numbers.

<!-- ─── -->

**4. Energy under gauge transformation.** One might argue: "The eigenvalue equation $\hat{H}\psi_n = E_n\psi_n$ contains $\hat{H}$, which depends on $\boldsymbol{A}$ and $\phi$. So changing gauge must change the energy eigenvalues."

(a) Refute this by showing explicitly that if $\hat{H}\psi_n = E_n\psi_n$, then $\hat{H}'\psi_n' = E_n\psi_n'$ with the transformed $\hat{H}'$ and $\psi_n' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_n$.

(b) The kinetic energy $\frac{1}{2m}\langle\hat{\boldsymbol{\pi}}^2\rangle$ is gauge-invariant, but $q\langle\phi\rangle$ is not. How can $E_n$ be gauge-invariant if one of its terms is not? Resolve the apparent paradox.

(c) An experimentalist measures the hydrogen atom spectrum. In what sense is the result "gauge-invariant" even though the calculation was done in a specific gauge?

**Solution.**

**(a)** Stationary states exist for *static* fields, so take a time-independent
gauge function $\alpha(\boldsymbol{r})$. Then $\phi' = \phi - \partial_t\alpha = \phi$ is
unchanged and only $\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha$ shifts. The claim is
that the new Hamiltonian is a *unitary similarity transform* of the old one,

$$
\hat{H}' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\hat{H}\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar} .
$$

To see this, conjugate the kinetic momentum. Using the preamble identity
$\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{\boldsymbol{p}}\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar} = \hat{\boldsymbol{p}} - q\nabla\alpha$, and that $q\boldsymbol{A}$ commutes with the phase,

$$
\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\hat{\boldsymbol{\pi}}\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}
= (\hat{\boldsymbol{p}} - q\nabla\alpha) - q\boldsymbol{A}
= \hat{\boldsymbol{p}} - q\boldsymbol{A}' = \hat{\boldsymbol{\pi}}' .
$$

Squaring, $\hat{\boldsymbol{\pi}}'^2 = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{\boldsymbol{\pi}}^2\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}$
(the phase factors between the two $\hat{\boldsymbol{\pi}}$'s cancel), and $q\phi' = q\phi$
commutes with the phase, so indeed $\hat{H}' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{H}\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}$.
Now act on the rephased eigenstate $\psi_n' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_n$:

$$
\hat{H}'\psi_n'
= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{H}\,\mathrm{e}^{-\mathrm{i}q\alpha/\hbar}\,\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_n
= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\hat{H}\psi_n
= \mathrm{e}^{\mathrm{i}q\alpha/\hbar}E_n\psi_n
= E_n\psi_n' .
$$

The transformed state is an eigenstate of the transformed Hamiltonian with the
**same eigenvalue** $E_n$. This is inevitable: a unitary similarity transformation
never changes a spectrum. The argument in quotation marks confuses "$\hat{H}$ looks
different" with "$\hat{H}$ has different eigenvalues" — but $\hat{H}' = \hat{U}\hat{H}\hat{U}^\dagger$
is **unitarily equivalent** to $\hat{H}$, so the two Hamiltonians have the same
spectrum even though their matrix elements in a fixed basis differ.

**(b)** The decomposition $E_n = \tfrac{1}{2m}\langle\hat{\boldsymbol{\pi}}^2\rangle + q\langle\phi\rangle$
is a split into expectation values, and it is *not* a gauge-covariant split. Two
points resolve the paradox.

First, restrict to gauge transformations that preserve the static structure of the
problem (time-independent $\alpha$, as in part (a)). For these, $\phi$ does not
change at all, so $q\langle\phi\rangle$ is in fact invariant — *and* $\langle\hat{\boldsymbol{\pi}}^2\rangle$
is invariant, *and* so is their sum $E_n$. There is no paradox within the class of
transformations that keep "stationary state" meaningful.

Second, the statement "$q\langle\phi\rangle$ is not gauge-invariant" refers to the
*full* gauge group, which includes time-dependent $\alpha$. The simplest such
transformation, a purely time-dependent $\alpha(t)$ with $\partial_t\alpha = -c$,
leaves $\boldsymbol{A}$ untouched ($\nabla\alpha = 0$) but shifts $\phi \to \phi + c$,
hence $q\langle\phi\rangle \to q\langle\phi\rangle + qc$ and $E_n \to E_n + qc$.
This shifts *every* level by the *same* constant — it is nothing but the freedom to
choose the zero of the potential energy. The kinetic part $\tfrac{1}{2m}\langle\hat{\boldsymbol{\pi}}^2\rangle$
is untouched. So the resolution is: $E_n$ is gauge-invariant up to a global,
$n$-independent additive constant fixed by the energy-zero convention. The
genuinely physical, fully gauge-invariant quantities are the **energy differences**
$E_n - E_m$, in which the constant cancels. The "non-invariant term" $q\langle\phi\rangle$
encodes exactly the unphysical freedom of where to put the energy origin — the
familiar statement that absolute potential energy has no meaning.

**(c)** Spectroscopy of hydrogen measures *spectral line frequencies*, which are
energy differences: $\omega_{nm} = (E_n - E_m)/\hbar$. The calculation is typically
done in the Coulomb gauge ($\boldsymbol{A} = 0$, $\phi = -e/4\pi\epsilon_0 r$), but
any other gauge yields wavefunctions $\psi_n' = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi_n$
related by a unitary transformation, hence the same spectrum up to the global
constant of part (b). Since the measured frequencies are *differences*, the
constant drops out and every gauge predicts identical line positions. More
broadly, every genuine observable — transition frequencies, transition rates,
cross-sections, the probability density — comes out gauge-invariant. "The result
is gauge-invariant" means precisely that the physics extracted from the
calculation does not depend on the gauge chosen to perform it, even though
intermediate objects like $\boldsymbol{A}$, $\hat{\boldsymbol{p}}$, or the absolute $E_n$ do.

<!-- ─── -->

**5. Coulomb gauge residual freedom.** In the Coulomb gauge $\nabla \cdot \boldsymbol{A} = 0$, show that the gauge is not fully fixed: $\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha$ still satisfies $\nabla \cdot \boldsymbol{A}' = 0$ provided $\nabla^2\alpha = 0$. Give an explicit example of such a residual transformation.

**Solution.**

A gauge condition is meant to single out one representative from each class of
physically equivalent potentials. The Coulomb (transverse) condition imposes
$\nabla\cdot\boldsymbol{A} = 0$. Take a potential $\boldsymbol{A}$ already satisfying it and
apply a further gauge transformation $\boldsymbol{A}' = \boldsymbol{A} + \nabla\alpha$. Its
divergence is

$$
\nabla\cdot\boldsymbol{A}' = \nabla\cdot\boldsymbol{A} + \nabla\cdot(\nabla\alpha)
= 0 + \nabla^2\alpha .
$$

Hence $\boldsymbol{A}'$ is *still* in the Coulomb gauge if and only if

$$
\nabla^2\alpha = 0 ,
$$

i.e. $\alpha$ is a **harmonic function**. The Coulomb condition therefore does not
fix the gauge completely: the whole space of harmonic functions $\alpha$ generates
**residual gauge transformations** that move $\boldsymbol{A}$ around within the Coulomb
gauge. The condition $\nabla\cdot\boldsymbol{A} = 0$ removes the *longitudinal* part of
the gauge freedom but leaves the *harmonic* part.

Explicit examples of residual transformations (each has $\nabla^2\alpha = 0$):

- $\alpha = \boldsymbol{c}\cdot\boldsymbol{r}$ with $\boldsymbol{c}$ a constant vector.
  Then $\nabla\alpha = \boldsymbol{c}$, so $\boldsymbol{A}' = \boldsymbol{A} + \boldsymbol{c}$ —
  adding a uniform constant to the vector potential keeps it transverse.
- $\alpha = xy$, giving $\nabla\alpha = (y,x,0)$; or $\alpha = x^2 - y^2$, giving
  $\nabla\alpha = (2x,-2y,0)$. Both satisfy $\nabla^2\alpha = 0$, as does any real
  or imaginary part of an analytic function of $x+\mathrm{i}y$.
- A spatially uniform but time-dependent $\alpha = f(t)$: trivially harmonic,
  leaves $\boldsymbol{A}$ unchanged, and shifts $\phi \to \phi - \dot f$ — the
  energy-zero freedom of Problem 4(b).

A remark on boundary conditions: which residual transformations are *admissible*
depends on the domain. For fields that must vanish at infinity, the only harmonic
$\alpha$ bounded everywhere is a constant ($\nabla\alpha = 0$), so the Coulomb gauge
is then effectively fixed up to that triviality. On bounded domains, or in
multiply connected regions, nontrivial harmonic $\alpha$ survive and the residual
freedom is genuine.

<!-- ─── -->

**6. Gauge-invariant classification.** For each quantity below, check the box indicating whether it is **gauge-invariant** or **gauge-dependent** under $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$, $\phi\to\phi-\partial_t\alpha$, $\psi\to\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi$. For each gauge-dependent entry, identify a related gauge-invariant quantity.

| Quantity | Gauge invariant | Gauge-dependent |
|---|:---:|:---:|
| $\vert\psi(\boldsymbol{r})\vert^2$ | ☐ | ☐ |
| $\arg\psi(\boldsymbol{r})$ | ☐ | ☐ |
| $\langle\hat{\boldsymbol{p}}\rangle$ | ☐ | ☐ |
| $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ | ☐ | ☐ |
| $\boldsymbol{A}(\boldsymbol{r})$ | ☐ | ☐ |
| $\oint\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$ (closed loop) | ☐ | ☐ |
| Energy eigenvalue $E_n$ | ☐ | ☐ |
| Canonical momentum eigenvalue $\hbar k$ | ☐ | ☐ |
| Electric field $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ | ☐ | ☐ |

**Solution.**

| Quantity | Gauge invariant | Gauge-dependent |
|---|:---:|:---:|
| $\vert\psi(\boldsymbol{r})\vert^2$ | ☑ |  |
| $\arg\psi(\boldsymbol{r})$ |  | ☑ |
| $\langle\hat{\boldsymbol{p}}\rangle$ |  | ☑ |
| $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ | ☑ |  |
| $\boldsymbol{A}(\boldsymbol{r})$ |  | ☑ |
| $\oint\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$ (closed loop) | ☑ |  |
| Energy eigenvalue $E_n$ | ☑ |  |
| Canonical momentum eigenvalue $\hbar k$ |  | ☑ |
| Electric field $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ | ☑ |  |

*Reasoning, entry by entry.*

- $\vert\psi(\boldsymbol{r})\vert^2$ — invariant: $\vert\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi\vert^2 = \vert\psi\vert^2$ (probability density is physical).
- $\arg\psi(\boldsymbol{r})$ — shifts by $q\alpha(\boldsymbol{r})/\hbar$. **Repair:** the covariant phase gradient $\hbar\nabla\arg\psi - q\boldsymbol{A}$ is invariant (both terms pick up $q\nabla\alpha$ and cancel). It equals the local kinetic momentum, with $\boldsymbol{j} = (\rho/m)(\hbar\nabla\arg\psi - q\boldsymbol{A})$.
- $\langle\hat{\boldsymbol{p}}\rangle$ — shifts under the rephasing (Problems 1b, 3). **Repair:** the kinetic-momentum expectation $\langle\hat{\boldsymbol{\pi}}\rangle = \langle\hat{\boldsymbol{p}}-q\boldsymbol{A}\rangle = m\langle\hat{\boldsymbol{v}}\rangle$.
- $\boldsymbol{B} = \nabla\times\boldsymbol{A}$ — invariant: $\nabla\times(\boldsymbol{A}+\nabla\alpha) = \nabla\times\boldsymbol{A}$ since $\nabla\times\nabla\alpha = 0$.
- $\boldsymbol{A}(\boldsymbol{r})$ — shifts by $\nabla\alpha$. **Repair:** its curl $\boldsymbol{B}$ (local) or its closed-loop integral (nonlocal).
- $\oint\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$ — invariant: under $\boldsymbol{A}\to\boldsymbol{A}+\nabla\alpha$ the change is $\oint\nabla\alpha\cdot\mathrm{d}\boldsymbol{l} = \alpha(\boldsymbol{r}_\text{end}) - \alpha(\boldsymbol{r}_\text{start}) = 0$ for single-valued $\alpha$ on a closed loop. By Stokes it equals the enclosed magnetic flux $\Phi$.
- $E_n$ — invariant under transformations preserving the static structure (Problem 4a); fully physical content is the set of differences $E_n - E_m$ (Problem 4b).
- Canonical momentum eigenvalue $\hbar k$ — shifts under rephasing of a plane-wave eigenstate of $\hat{\boldsymbol{p}}$: $\hbar k \to \hbar k + q\,\partial_x\alpha$. The same gauge shift afflicts any canonical-momentum matrix element. **Repair:** the kinetic-momentum eigenvalue $\hbar k - qA$ (eigenvalue of $\hat{\boldsymbol{\pi}}$), equivalently $mv$.
- $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ — invariant: the $\partial_t\alpha$ from $\phi$ and the $\nabla\alpha$ from $\boldsymbol{A}$ cancel, $-\nabla(-\partial_t\alpha) - \partial_t(\nabla\alpha) = 0$, using $\partial_t\nabla\alpha = \nabla\partial_t\alpha$.

*Pattern.* Moduli, curls, and closed-loop integrals are gauge-invariant; phases, potentials, canonical labels, and open-path integrals are gauge-dependent. Each gauge-dependent quantity is repaired either by subtracting the matching potential ($\hat{\boldsymbol{p}}\to\hat{\boldsymbol{\pi}}$) or by closing the loop.
