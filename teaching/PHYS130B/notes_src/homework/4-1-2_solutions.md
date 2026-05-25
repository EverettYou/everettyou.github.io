# 4.1.2 Electromagnetic Coupling
Worked solutions for the homework problems in the [4.1.2 Electromagnetic Coupling](../ch4_phase-and-gauge/4-1-2-electromagnetic-coupling) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Velocity for the Pauli Hamiltonian.** Spin-1/2 motion in electromagnetic fields is governed by the Pauli Hamiltonian

$$
\hat{H}_{\mathrm{P}} = \frac{(\hat{\boldsymbol{p}} - q\boldsymbol{A}(\hat{\boldsymbol{x}}))^{2}}{2m} - \frac{q\hbar}{2m}\,\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}(\hat{\boldsymbol{x}}) + q\phi(\hat{\boldsymbol{x}}),
$$

where $\hat{\boldsymbol{\sigma}} = (\hat{\sigma}^x, \hat{\sigma}^y, \hat{\sigma}^z)$ are Pauli operators acting on the spin index and $\boldsymbol{B} = \nabla\times\boldsymbol{A}$.

(a) Compute $[\hat{x}_i, \hat{H}_{\mathrm{P}}]$ and show that the spin-magnetic term contributes nothing. Conclude that $\mathrm{d}\hat{\boldsymbol{x}}/\mathrm{d}t = \hat{\boldsymbol{\pi}}/m$, identical to the spinless result.

(b) Generalize: argue that any term built from $\hat{\boldsymbol{x}}$ and $\hat{\boldsymbol{\sigma}}$ alone (without an accompanying $\hat{\boldsymbol{p}}$) cannot contribute to the velocity operator, regardless of the spin algebra.

(c) Where does the spin then influence motion? Compute the contribution of the spin-magnetic term to $m\,\mathrm{d}\hat{\boldsymbol{v}}/\mathrm{d}t$ and show that it produces a Stern-Gerlach-type force $(q\hbar/2m)\,\nabla(\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B})$ — the spin couples to motion only through the *gradient* of $\boldsymbol{B}$, not through $\boldsymbol{B}$ itself.

**Solution.**

**(a)** Write the Pauli Hamiltonian as a sum of three pieces,

$$
\hat{H}_{\mathrm{P}} = \underbrace{\frac{\hat{\pi}_j\hat{\pi}_j}{2m}}_{\text{kinetic}}
\;\underbrace{-\;\frac{q\hbar}{2m}\,\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}(\hat{\boldsymbol{x}})}_{\text{spin-magnetic}}
\;+\;\underbrace{q\phi(\hat{\boldsymbol{x}})}_{\text{electric}},
$$

with $\hat{\pi}_j = \hat{p}_j - qA_j(\hat{\boldsymbol{x}})$ and a sum over the repeated index $j$. The position operator $\hat{x}_i$ commutes with any function of $\hat{\boldsymbol{x}}$, and it acts on a different tensor factor than the Pauli operators, so $[\hat{x}_i,\hat{\sigma}^a]=0$. Both the spin-magnetic term and the electric term are built only from $\hat{\boldsymbol{x}}$ and $\hat{\boldsymbol{\sigma}}$:

$$
\begin{split}
\left[\hat{x}_i,\; -\frac{q\hbar}{2m}\,\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}(\hat{\boldsymbol{x}})\right]
&= -\frac{q\hbar}{2m}\,\hat{\sigma}^a\,[\hat{x}_i,\, B_a(\hat{\boldsymbol{x}})] = 0, \\
[\hat{x}_i,\; q\phi(\hat{\boldsymbol{x}})] &= 0.
\end{split}
$$

Only the kinetic term survives. With $[\hat{x}_i,\hat{\pi}_j] = [\hat{x}_i,\hat{p}_j] = \mathrm{i}\hbar\delta_{ij}$ and the product rule $[A,BC]=[A,B]C+B[A,C]$,

$$
\begin{split}
[\hat{x}_i,\hat{H}_{\mathrm{P}}]
&= \frac{1}{2m}\,[\hat{x}_i,\hat{\pi}_j\hat{\pi}_j] \\
&= \frac{1}{2m}\big([\hat{x}_i,\hat{\pi}_j]\hat{\pi}_j + \hat{\pi}_j[\hat{x}_i,\hat{\pi}_j]\big) \\
&= \frac{1}{2m}\big(\mathrm{i}\hbar\delta_{ij}\hat{\pi}_j + \hat{\pi}_j\,\mathrm{i}\hbar\delta_{ij}\big) \\
&= \frac{\mathrm{i}\hbar}{m}\,\hat{\pi}_i.
\end{split}
$$

Therefore

$$
\frac{\mathrm{d}\hat{x}_i}{\mathrm{d}t} = \frac{1}{\mathrm{i}\hbar}[\hat{x}_i,\hat{H}_{\mathrm{P}}] = \frac{\hat{\pi}_i}{m},
\qquad\text{i.e.}\qquad
\frac{\mathrm{d}\hat{\boldsymbol{x}}}{\mathrm{d}t} = \frac{\hat{\boldsymbol{\pi}}}{m},
$$

exactly the spinless result. The Stern-Gerlach term changes the *dynamics* of the velocity (part c), but it leaves the *definition* of the velocity operator untouched.

**(b)** The velocity operator is $\mathrm{d}\hat{x}_i/\mathrm{d}t = [\hat{x}_i,\hat{H}]/(\mathrm{i}\hbar)$, so a Hamiltonian term contributes to the velocity only if it fails to commute with $\hat{x}_i$. Consider any term $\hat{T}(\hat{\boldsymbol{x}},\hat{\boldsymbol{\sigma}})$ assembled from position operators and Pauli operators alone. The position operators commute among themselves, $[\hat{x}_i,\hat{x}_j]=0$, and they commute with every Pauli operator, $[\hat{x}_i,\hat{\sigma}^a]=0$, because the two act on different tensor factors of the Hilbert space (orbital $\otimes$ spin). Hence $\hat{x}_i$ commutes with every monomial in $\hat{\boldsymbol{x}}$ and $\hat{\boldsymbol{\sigma}}$, and therefore with any function of them:

$$
[\hat{x}_i,\hat{T}(\hat{\boldsymbol{x}},\hat{\boldsymbol{\sigma}})] = 0.
$$

The spin algebra $\hat{\sigma}^a\hat{\sigma}^b = \delta^{ab} + \mathrm{i}\epsilon^{abc}\hat{\sigma}^c$ never enters this conclusion: it is an algebra internal to the spin factor and cannot generate an $\hat{x}_i$-noncommuting object. Position operators fail to commute only with the canonical momentum, $[\hat{x}_i,\hat{p}_j]=\mathrm{i}\hbar\delta_{ij}$, so **only Hamiltonian terms containing $\hat{\boldsymbol{p}}$ contribute to the velocity operator**. This is why the velocity is always $\hat{\boldsymbol{\pi}}/m$ for a Hamiltonian quadratic in $\hat{\boldsymbol{\pi}}$ — the precise form of any spin- or potential-energy term is irrelevant to it.

**(c)** Spin enters through the *acceleration*, i.e. through the equation of motion for $\hat{\boldsymbol{v}}$. Splitting $\hat{H}_{\mathrm{P}} = \hat{H}_{\text{orb}} + \hat{H}_{\text{spin}}$ with $\hat{H}_{\text{orb}} = \hat{\boldsymbol{\pi}}^2/2m + q\phi$ and $\hat{H}_{\text{spin}} = -(q\hbar/2m)\,\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}$, the velocity obeys

$$
m\frac{\mathrm{d}\hat{v}_i}{\mathrm{d}t}
= \frac{1}{\mathrm{i}\hbar}[\hat{\pi}_i,\hat{H}_{\text{orb}}]
+ \frac{1}{\mathrm{i}\hbar}[\hat{\pi}_i,\hat{H}_{\text{spin}}]
+ m\,\partial_t\hat{v}_i.
$$

The orbital and explicit-time pieces give the ordinary Lorentz force (lecture derivation). The new contribution is the spin commutator. Since $\hat{H}_{\text{spin}}$ is a function of $\hat{\boldsymbol{x}}$ (with Pauli operators riding along as constants for the $\hat{\boldsymbol{x}}$-commutator), apply $[\hat{\pi}_i, f(\hat{\boldsymbol{x}})] = -\mathrm{i}\hbar\,\partial_i f$ with $f = \hat{H}_{\text{spin}}$:

$$
\begin{split}
[\hat{\pi}_i,\hat{H}_{\text{spin}}]
&= \left[\hat{\pi}_i,\; -\frac{q\hbar}{2m}\,\hat{\sigma}^a B_a(\hat{\boldsymbol{x}})\right] \\
&= -\frac{q\hbar}{2m}\,\hat{\sigma}^a\,[\hat{\pi}_i, B_a(\hat{\boldsymbol{x}})] \\
&= -\frac{q\hbar}{2m}\,\hat{\sigma}^a\,(-\mathrm{i}\hbar\,\partial_i B_a) \\
&= \mathrm{i}\hbar\,\frac{q\hbar}{2m}\,\partial_i(\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}).
\end{split}
$$

Dividing by $\mathrm{i}\hbar$, the spin-magnetic term adds

$$
\left(m\frac{\mathrm{d}\hat{v}_i}{\mathrm{d}t}\right)_{\!\text{spin}}
= \frac{1}{\mathrm{i}\hbar}[\hat{\pi}_i,\hat{H}_{\text{spin}}]
= \frac{q\hbar}{2m}\,\partial_i(\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}),
\qquad\text{i.e.}\qquad
\boldsymbol{F}_{\text{spin}} = \frac{q\hbar}{2m}\,\nabla(\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}).
$$

This is a **Stern-Gerlach force**. Introducing the spin magnetic moment operator $\hat{\boldsymbol{\mu}} = (q\hbar/2m)\,\hat{\boldsymbol{\sigma}}$, the spin term in the Hamiltonian is $\hat{H}_{\text{spin}} = -\hat{\boldsymbol{\mu}}\cdot\boldsymbol{B}$ and the force is $\boldsymbol{F}_{\text{spin}} = \nabla(\hat{\boldsymbol{\mu}}\cdot\boldsymbol{B})$ — the gradient of the magnetic potential energy. Because only the *gradient* of $\boldsymbol{B}$ appears, a **uniform** field exerts no translational force on the spin (it only makes the moment precess); a force on the center of mass requires a field gradient. This is exactly the mechanism that splits an atomic beam in the Stern-Gerlach experiment.

The full equation of motion for the Pauli particle is therefore

$$
m\frac{\mathrm{d}\hat{\boldsymbol{v}}}{\mathrm{d}t}
= q\boldsymbol{E}
+ \frac{q}{2}(\hat{\boldsymbol{v}}\times\boldsymbol{B} - \boldsymbol{B}\times\hat{\boldsymbol{v}})
+ \frac{q\hbar}{2m}\,\nabla(\hat{\boldsymbol{\sigma}}\cdot\boldsymbol{B}),
$$

the orbital Lorentz force plus the spin-gradient force.

<!-- ─── -->

**2. Velocity uncertainty in B.** For an electron in a uniform magnetic field $\boldsymbol{B} = B\boldsymbol{e}_z$ (with $\boldsymbol{e}_z$ the unit vector along the $z$-axis), the velocity components $\hat{v}_i = \hat{\pi}_i/m$ obey $[\hat{v}_x, \hat{v}_y] = \mathrm{i}\hbar qB/m^2$.

(a) Use the commutator to derive a Heisenberg uncertainty relation for $\Delta v_x\,\Delta v_y$.

(b) Translate this into an uncertainty for the cyclotron orbit area $\pi r_c^2$ (with $r_c = mv_\perp/(qB)$). Show that the minimum orbit area is of order $\pi\ell_B^2$, where $\ell_B^2 = \hbar/(qB)$.

(c) Interpret physically: why can the cyclotron orbit area not be made arbitrarily small even at fixed kinetic energy?

**Solution.**

Take $q>0$ and $B>0$ for definiteness (otherwise replace $qB$ by $|qB|$ below). The commutator follows directly from the kinetic-momentum algebra: $[\hat{\pi}_x,\hat{\pi}_y] = \mathrm{i}\hbar q\,\epsilon_{xyz}B_z = \mathrm{i}\hbar qB$, so

$$
[\hat{v}_x,\hat{v}_y] = \frac{1}{m^2}[\hat{\pi}_x,\hat{\pi}_y] = \frac{\mathrm{i}\hbar qB}{m^2}.
$$

**(a)** The Robertson uncertainty relation for any two observables is $\Delta A\,\Delta B \ge \tfrac12\,|\langle[\hat{A},\hat{B}]\rangle|$. Here the commutator is a pure c-number, so its expectation value is itself, independent of the state:

$$
\Delta v_x\,\Delta v_y \;\ge\; \frac{1}{2}\,\bigl|\langle[\hat{v}_x,\hat{v}_y]\rangle\bigr|
\;=\; \frac{1}{2}\,\frac{\hbar qB}{m^2}
\;=\; \frac{\hbar qB}{2m^2}.
$$

The two velocity components are *jointly* uncertain in a magnetic field: sharpening $v_x$ necessarily blurs $v_y$. In zero field the commutator vanishes and the two are simultaneously sharp.

**(b)** Consider a stationary (cyclotron / Landau) state, for which the orbit is centered, $\langle\hat{v}_x\rangle = \langle\hat{v}_y\rangle = 0$. Then $\langle\hat{v}_x^2\rangle = (\Delta v_x)^2$ and likewise for $y$, so the mean-square transverse speed is

$$
\langle v_\perp^2\rangle = \langle\hat{v}_x^2\rangle + \langle\hat{v}_y^2\rangle = (\Delta v_x)^2 + (\Delta v_y)^2.
$$

By the arithmetic-geometric-mean inequality and then the result of (a),

$$
(\Delta v_x)^2 + (\Delta v_y)^2 \;\ge\; 2\,\Delta v_x\,\Delta v_y \;\ge\; 2\cdot\frac{\hbar qB}{2m^2} = \frac{\hbar qB}{m^2},
$$

so $\langle v_\perp^2\rangle \ge \hbar qB/m^2$. The cyclotron radius is $r_c = m v_\perp/(qB)$, hence the orbit area is $\pi r_c^2 = \pi m^2 v_\perp^2/(qB)^2$. Taking expectation values,

$$
\langle \pi r_c^2\rangle
= \frac{\pi m^2}{(qB)^2}\,\langle v_\perp^2\rangle
\;\ge\; \frac{\pi m^2}{(qB)^2}\cdot\frac{\hbar qB}{m^2}
= \frac{\pi\hbar}{qB}
= \pi\ell_B^2,
$$

with the magnetic length $\ell_B^2 = \hbar/(qB)$. The cyclotron orbit therefore cannot enclose an area smaller than $\sim\pi\ell_B^2$. The bound is *saturated* by the lowest Landau level: there $\langle v_\perp^2\rangle = \hbar\omega_c/m = \hbar qB/m^2$ (transverse kinetic energy $\tfrac12 m\langle v_\perp^2\rangle = \tfrac12\hbar\omega_c$), giving exactly $\pi r_c^2 = \pi\ell_B^2$.

**(c)** A small orbit area means a small $r_c$, hence a small $v_\perp$ — both velocity components simultaneously small *and* sharply defined. But in a magnetic field $\hat{v}_x$ and $\hat{v}_y$ do not commute; they are conjugate variables, exactly like position and momentum. The uncertainty relation of (a) forbids them from being jointly localized near zero. Fixing the kinetic energy fixes $\langle v_\perp^2\rangle = \langle v_x^2\rangle + \langle v_y^2\rangle$, but it does **not** allow that sum to drop below $\hbar qB/m^2$: even the ground state retains an irreducible zero-point cyclotron motion with energy $\tfrac12\hbar\omega_c$. Physically, the magnetic field turns the transverse $(v_x,v_y)$ plane into a quantum phase space with a minimum cell of area $\sim\pi\ell_B^2$; the orbit cannot be squeezed below that cell without violating the velocity uncertainty relation. This is the kinematic origin of Landau quantization (§4.3).

<!-- ─── -->

★ **3. Cyclotron motion from Heisenberg.** A particle of charge $q$ moves in a uniform $\boldsymbol{B} = B\boldsymbol{e}_z$ with $\hat{H} = \hat{\boldsymbol{\pi}}^2/(2m)$ and $\boldsymbol{E} = 0$.

(a) Use the Heisenberg equation $\mathrm{d}\hat{\pi}_i/\mathrm{d}t = [\hat{\pi}_i, \hat{H}]/(\mathrm{i}\hbar)$ together with $[\hat{\pi}_x, \hat{\pi}_y] = \mathrm{i}q\hbar B$ to derive coupled equations of motion for $\hat{\pi}_x$ and $\hat{\pi}_y$.

(b) Solve them and show that $\hat{\pi}_x(t), \hat{\pi}_y(t)$ rotate at frequency $\omega_c = qB/m$, recovering classical cyclotron motion at the operator level.

(c) Verify that $\hat{\boldsymbol{\pi}}^2$ is conserved, and connect this to energy conservation in the absence of an electric field.

**Solution.**

For a uniform static field the vector potential can be chosen time-independent, so $\hat{\pi}_i$ has no explicit time dependence and the plain Heisenberg equation $\mathrm{d}\hat{\pi}_i/\mathrm{d}t = [\hat{\pi}_i,\hat{H}]/(\mathrm{i}\hbar)$ applies. The relevant commutators are $[\hat{\pi}_x,\hat{\pi}_y] = \mathrm{i}q\hbar B$ and $[\hat{\pi}_x,\hat{\pi}_z] = [\hat{\pi}_y,\hat{\pi}_z] = 0$ (since $\boldsymbol{B}$ points along the $z$-axis, $\epsilon_{xzk}B_k = \epsilon_{yzk}B_k = 0$).

**(a)** With $\hat{H} = (\hat{\pi}_x^2 + \hat{\pi}_y^2 + \hat{\pi}_z^2)/2m$, evaluate $[\hat{\pi}_x,\hat{H}]$ using the product rule. The $\hat{\pi}_x^2$ and $\hat{\pi}_z^2$ pieces commute with $\hat{\pi}_x$, so only $\hat{\pi}_y^2$ contributes:

$$
\begin{split}
[\hat{\pi}_x,\hat{H}]
&= \frac{1}{2m}\,[\hat{\pi}_x,\hat{\pi}_y^2] \\
&= \frac{1}{2m}\big([\hat{\pi}_x,\hat{\pi}_y]\hat{\pi}_y + \hat{\pi}_y[\hat{\pi}_x,\hat{\pi}_y]\big) \\
&= \frac{1}{2m}\big(\mathrm{i}q\hbar B\,\hat{\pi}_y + \hat{\pi}_y\,\mathrm{i}q\hbar B\big) \\
&= \frac{\mathrm{i}q\hbar B}{m}\,\hat{\pi}_y,
\end{split}
$$

where the c-number $\mathrm{i}q\hbar B$ was pulled out freely. Likewise, only $\hat{\pi}_x^2$ contributes to $[\hat{\pi}_y,\hat{H}]$, and with $[\hat{\pi}_y,\hat{\pi}_x] = -\mathrm{i}q\hbar B$,

$$
[\hat{\pi}_y,\hat{H}] = \frac{1}{2m}\,[\hat{\pi}_y,\hat{\pi}_x^2] = \frac{1}{2m}\big({-2\mathrm{i}q\hbar B}\,\hat{\pi}_x\big) = -\frac{\mathrm{i}q\hbar B}{m}\,\hat{\pi}_x.
$$

Dividing by $\mathrm{i}\hbar$ and writing $\omega_c = qB/m$ gives the coupled operator equations of motion

$$
\frac{\mathrm{d}\hat{\pi}_x}{\mathrm{d}t} = \omega_c\,\hat{\pi}_y,
\qquad
\frac{\mathrm{d}\hat{\pi}_y}{\mathrm{d}t} = -\omega_c\,\hat{\pi}_x.
$$

(The $z$-component is constant, $\mathrm{d}\hat{\pi}_z/\mathrm{d}t = [\hat{\pi}_z,\hat{H}]/(\mathrm{i}\hbar) = 0$, so the motion along the field is free.)

**(b)** Form the complex combination $\hat{\pi}_\pm = \hat{\pi}_x \pm \mathrm{i}\hat{\pi}_y$. Then

$$
\frac{\mathrm{d}\hat{\pi}_+}{\mathrm{d}t}
= \frac{\mathrm{d}\hat{\pi}_x}{\mathrm{d}t} + \mathrm{i}\frac{\mathrm{d}\hat{\pi}_y}{\mathrm{d}t}
= \omega_c\hat{\pi}_y - \mathrm{i}\omega_c\hat{\pi}_x
= -\mathrm{i}\omega_c(\hat{\pi}_x + \mathrm{i}\hat{\pi}_y)
= -\mathrm{i}\omega_c\,\hat{\pi}_+,
$$

a single decoupled equation with solution $\hat{\pi}_+(t) = \mathrm{e}^{-\mathrm{i}\omega_c t}\,\hat{\pi}_+(0)$. Taking real and imaginary parts,

$$
\begin{split}
\hat{\pi}_x(t) &= \hphantom{-}\cos(\omega_c t)\,\hat{\pi}_x(0) + \sin(\omega_c t)\,\hat{\pi}_y(0), \\
\hat{\pi}_y(t) &= -\sin(\omega_c t)\,\hat{\pi}_x(0) + \cos(\omega_c t)\,\hat{\pi}_y(0).
\end{split}
$$

The pair $(\hat{\pi}_x,\hat{\pi}_y)$ rotates rigidly in the velocity plane at the **cyclotron frequency** $\omega_c = qB/m$. Because the rotation matrix has c-number entries, this is the operator-level statement of classical cyclotron motion: every expectation value $\langle\hat{\pi}_x\rangle(t), \langle\hat{\pi}_y\rangle(t)$ traces a circle at frequency $\omega_c$, exactly the classical orbit. Quantum mechanics adds nothing to the *frequency* — it only constrains the *amplitude* through the velocity uncertainty relation of Problem 2.

**(c)** The kinetic energy operator $\hat{\boldsymbol{\pi}}^2 = 2m\hat{H}$ commutes with the Hamiltonian, since any operator commutes with itself:

$$
\frac{\mathrm{d}\hat{\boldsymbol{\pi}}^2}{\mathrm{d}t}
= \frac{1}{\mathrm{i}\hbar}[\hat{\boldsymbol{\pi}}^2,\hat{H}]
= \frac{1}{\mathrm{i}\hbar}[2m\hat{H},\hat{H}]
= 0.
$$

One can also see it from the explicit solution: using $\cos^2 + \sin^2 = 1$ and that the cross terms cancel,

$$
\hat{\pi}_x(t)^2 + \hat{\pi}_y(t)^2 = \hat{\pi}_x(0)^2 + \hat{\pi}_y(0)^2,
$$

while $\hat{\pi}_z$ is separately constant, so $\hat{\boldsymbol{\pi}}^2 = \hat{\pi}_x^2 + \hat{\pi}_y^2 + \hat{\pi}_z^2$ is conserved. Physically, the magnetic force $q\hat{\boldsymbol{v}}\times\boldsymbol{B}$ is always perpendicular to the velocity and therefore does **no work**; with $\boldsymbol{E} = 0$ there is no other force, so the kinetic energy $\hat{H} = \hat{\boldsymbol{\pi}}^2/2m$ is a constant of motion. The field bends the trajectory into a circle but never changes its speed — energy conservation at the operator level.

<!-- ─── -->

**4. Symmetric gauge verification.** In a uniform magnetic field $\boldsymbol{B} = B\boldsymbol{e}_z$, use the symmetric gauge $\boldsymbol{A} = \frac{B}{2}(-y, x, 0)$.

(a) Verify that $\boldsymbol{B} = \nabla \times \boldsymbol{A}$ gives $B\boldsymbol{e}_z$.

(b) Compute $[\hat{\pi}_x, \hat{\pi}_y]$ explicitly using this gauge and confirm $[\hat{\pi}_x, \hat{\pi}_y] = \mathrm{i}\hbar qB$.

(c) Interpret this non-zero commutator physically: what does it say about simultaneous measurability of velocity components?

**Solution.**

**(a)** With $\boldsymbol{A} = \tfrac{B}{2}(-y,\,x,\,0)$, the components are $A_x = -By/2$, $A_y = Bx/2$, $A_z = 0$. The curl is

$$
\begin{split}
(\nabla\times\boldsymbol{A})_x &= \partial_y A_z - \partial_z A_y = 0 - 0 = 0, \\
(\nabla\times\boldsymbol{A})_y &= \partial_z A_x - \partial_x A_z = 0 - 0 = 0, \\
(\nabla\times\boldsymbol{A})_z &= \partial_x A_y - \partial_y A_x = \partial_x\!\left(\tfrac{Bx}{2}\right) - \partial_y\!\left(-\tfrac{By}{2}\right) = \tfrac{B}{2} + \tfrac{B}{2} = B.
\end{split}
$$

Hence $\nabla\times\boldsymbol{A} = B\boldsymbol{e}_z = \boldsymbol{B}$, as required. (The "symmetric" name refers to the equal $B/2$ split between the $x$ and $y$ contributions, in contrast with the asymmetric Landau gauge $\boldsymbol{A} = B(-y,0,0)$ or $B(0,x,0)$.)

**(b)** The kinetic-momentum components in this gauge are

$$
\hat{\pi}_x = \hat{p}_x - qA_x = \hat{p}_x + \frac{qB}{2}\,\hat{y},
\qquad
\hat{\pi}_y = \hat{p}_y - qA_y = \hat{p}_y - \frac{qB}{2}\,\hat{x}.
$$

Expand the commutator by bilinearity. The terms $[\hat{p}_x,\hat{p}_y]$ and $[\hat{y},\hat{x}]$ vanish, leaving two canonical commutators:

$$
\begin{split}
[\hat{\pi}_x,\hat{\pi}_y]
&= \left[\hat{p}_x + \tfrac{qB}{2}\hat{y},\;\; \hat{p}_y - \tfrac{qB}{2}\hat{x}\right] \\
&= [\hat{p}_x,\hat{p}_y]
   - \frac{qB}{2}[\hat{p}_x,\hat{x}]
   + \frac{qB}{2}[\hat{y},\hat{p}_y]
   - \left(\tfrac{qB}{2}\right)^2[\hat{y},\hat{x}] \\
&= 0 - \frac{qB}{2}(-\mathrm{i}\hbar) + \frac{qB}{2}(+\mathrm{i}\hbar) - 0 \\
&= \frac{\mathrm{i}\hbar qB}{2} + \frac{\mathrm{i}\hbar qB}{2} \\
&= \mathrm{i}\hbar qB,
\end{split}
$$

using $[\hat{p}_x,\hat{x}] = -\mathrm{i}\hbar$ and $[\hat{y},\hat{p}_y] = +\mathrm{i}\hbar$. The result $[\hat{\pi}_x,\hat{\pi}_y] = \mathrm{i}\hbar qB$ matches the gauge-independent formula $[\hat{\pi}_i,\hat{\pi}_j] = \mathrm{i}\hbar q\,\epsilon_{ijk}B_k$ — the two halves $\mathrm{i}\hbar qB/2$ come symmetrically from the $\hat{y}$-term of $\hat{\pi}_x$ and the $\hat{x}$-term of $\hat{\pi}_y$, whereas in the Landau gauge one half would carry the whole result. The commutator is the same because it depends only on the physical field $\boldsymbol{B} = \nabla\times\boldsymbol{A}$, not on the gauge.

**(c)** A nonzero commutator $[\hat{\pi}_x,\hat{\pi}_y] = \mathrm{i}\hbar qB \neq 0$ means the velocity components $\hat{v}_x = \hat{\pi}_x/m$ and $\hat{v}_y = \hat{\pi}_y/m$ are **incompatible observables**: they have no common eigenbasis and cannot be assigned simultaneously sharp values. A measurement of $v_x$ disturbs $v_y$, and they obey the uncertainty relation $\Delta v_x\,\Delta v_y \ge \hbar qB/(2m^2)$ derived in Problem 2. In a magnetic field the two transverse velocity components behave like a conjugate pair — analogous to position and momentum — which is what makes the cyclotron motion quantize into Landau levels. With $B \to 0$ the commutator vanishes and the velocity components become jointly measurable again, recovering the familiar field-free situation where the full velocity vector is a sharp observable.

<!-- ─── -->

**5. Field strength tensor components.** Working in natural units (so the speed of light is set to one), write out all components of $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ as a $4\times 4$ matrix (rows and columns labeled $0, x, y, z$). Verify that $F_{0i} = E_i$ and $F_{ij} = -\epsilon_{ijk}B_k$ by computing a few entries explicitly from the definitions $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ and $\boldsymbol{B} = \nabla\times\boldsymbol{A}$.

**Solution.**

Set $c = 1$. Use the metric $g_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$, so the gauge four-potential has upper components $A^\mu = (\phi,\boldsymbol{A})$ and lowered components

$$
A_\mu = g_{\mu\nu}A^\nu = (\phi,\,-\boldsymbol{A}), \qquad\text{i.e.}\qquad A_0 = \phi,\quad A_i = -A^i.
$$

The derivative is $\partial_\mu = \partial/\partial x^\mu = (\partial_t,\,\nabla)$, with $\partial_0 = \partial_t$ and $\partial_i$ the ordinary spatial gradient component. The field strength tensor $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is antisymmetric, so its diagonal vanishes and only six independent entries need evaluation.

**Time-space entries $F_{0i}$.** For $i = x,y,z$,

$$
\begin{split}
F_{0i} &= \partial_0 A_i - \partial_i A_0 \\
&= \partial_t(-A^i) - \partial_i\phi \\
&= -\partial_t A^i - \partial_i\phi \\
&= E_i,
\end{split}
$$

using the definition $\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$, component-wise $E_i = -\partial_i\phi - \partial_t A^i$. Explicitly for $i=x$: $F_{0x} = \partial_t(-A_x) - \partial_x\phi = -\partial_t A_x - \partial_x\phi = E_x$.

**Space-space entries $F_{ij}$.** For spatial $i,j$,

$$
\begin{split}
F_{ij} &= \partial_i A_j - \partial_j A_i \\
&= \partial_i(-A^j) - \partial_j(-A^i) \\
&= -(\partial_i A^j - \partial_j A^i) \\
&= -\epsilon_{ijk}B_k,
\end{split}
$$

where the last step uses that the curl $B_k = \epsilon_{klm}\partial_l A^m$ is equivalent to $\partial_i A^j - \partial_j A^i = \epsilon_{ijk}B_k$ (contract $\epsilon_{ijk}B_k = \epsilon_{ijk}\epsilon_{klm}\partial_l A^m = (\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})\partial_l A^m = \partial_i A^j - \partial_j A^i$). A sample entry: $F_{xy} = \partial_x(-A_y) - \partial_y(-A_x) = -(\partial_x A_y - \partial_y A_x) = -B_z$, and indeed $-\epsilon_{xyk}B_k = -\epsilon_{xyz}B_z = -B_z$. Similarly $F_{xz} = -(\partial_x A_z - \partial_z A_x) = -\epsilon_{xzk}B_k = -\epsilon_{xzy}B_y = +B_y$ and $F_{yz} = -\epsilon_{yzk}B_k = -\epsilon_{yzx}B_x = -B_x$.

**The matrix.** Collecting all entries with rows/columns ordered $(0,x,y,z)$ and imposing antisymmetry $F_{\nu\mu} = -F_{\mu\nu}$:

$$
F_{\mu\nu} =
\begin{pmatrix}
0 & E_x & E_y & E_z \\
-E_x & 0 & -B_z & B_y \\
-E_y & B_z & 0 & -B_x \\
-E_z & -B_y & B_x & 0
\end{pmatrix}.
$$

The first row/column carries the electric field ($F_{0i} = E_i$); the lower-right $3\times3$ block carries the magnetic field through $F_{ij} = -\epsilon_{ijk}B_k$. A single antisymmetric tensor thus packages all six components of $\boldsymbol{E}$ and $\boldsymbol{B}$.

For completeness, raising both indices with the metric, $F^{\mu\nu} = g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}$, flips the sign of each entry that carries exactly one spatial index, i.e. the electric (time-space) block:

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & -E_x & -E_y & -E_z \\
E_x & 0 & -B_z & B_y \\
E_y & B_z & 0 & -B_x \\
E_z & -B_y & B_x & 0
\end{pmatrix}.
$$

The magnetic block is unchanged (two spatial indices, two sign flips that cancel). Gauge invariance of $F_{\mu\nu}$ is immediate: under $A_\mu \to A_\mu + \partial_\mu\alpha$, the extra piece is $\partial_\mu\partial_\nu\alpha - \partial_\nu\partial_\mu\alpha = 0$ since partial derivatives commute — consistent with $\boldsymbol{E}$ and $\boldsymbol{B}$ being the gauge-invariant physical fields.
