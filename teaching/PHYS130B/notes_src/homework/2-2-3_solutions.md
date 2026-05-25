# 2.2.3 Addition of Angular Momenta
Worked solutions for the homework problems in the [2.2.3 Addition of Angular Momenta](../ch2_identical-particles/2-2-3-addition-of-angular-momenta) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Angular momentum addition.** For $j_1 = 1$ and $j_2 = 3/2$, list all allowed values of $J$ using the triangle rule. Verify

$$
\sum_J (2J+1) = (2j_1+1)(2j_2+1).
$$

**Solution.**

*Allowed total angular momenta.* The triangle rule states that adding $j_1$ and $j_2$ produces

$$
J \in \{\vert j_1 - j_2\vert,\; \vert j_1 - j_2\vert + 1,\; \ldots,\; j_1 + j_2\},
$$

with neighboring values separated by one unit. Here

$$
\vert j_1 - j_2\vert = \left\vert 1 - \tfrac32\right\vert = \tfrac12, \qquad j_1 + j_2 = 1 + \tfrac32 = \tfrac52,
$$

so stepping up by one unit at a time,

$$
J \in \left\{\tfrac12,\; \tfrac32,\; \tfrac52\right\}.
$$

All three values are half-integer — as they must be, since coupling an integer spin ($j_1 = 1$) to a half-integer spin ($j_2 = 3/2$) always yields a half-integer total.

*Dimension check.* Each $J$-multiplet contributes $2J+1$ states ($M$ running from $-J$ to $+J$):

$$
2J+1 = \begin{cases} 2 & J = \tfrac12,\\ 4 & J = \tfrac32,\\ 6 & J = \tfrac52.\end{cases}
$$

Summing,

$$
\sum_J (2J+1) = 2 + 4 + 6 = 12.
$$

The uncoupled basis $\vert j_1, m_1\rangle\vert j_2, m_2\rangle$ has dimension

$$
(2j_1+1)(2j_2+1) = (2\cdot 1 + 1)(2\cdot\tfrac32 + 1) = 3 \times 4 = 12.
$$

The two counts agree: $12 = 12$. ✓ The coupled basis accounts for exactly every state of $\mathcal{H}_{j_1}\otimes\mathcal{H}_{j_2}$, so the decomposition $1 \otimes \tfrac32 = \tfrac12 \oplus \tfrac32 \oplus \tfrac52$ is complete.

<!-- ─── -->

**2. Total angular momentum.** For two spin-1/2 particles, derive the triplet and singlet states from scratch. Start from the stretched state $\vert 1,1\rangle=\vert\uparrow\uparrow\rangle$, apply $\hat J_-$ to obtain $\vert 1,0\rangle$, then determine $\vert 0,0\rangle$ by orthogonality and normalization.

**Solution.**

*Building blocks.* For a single spin-1/2, the lowering operator acts as $\hat J_-\vert\uparrow\rangle = \hbar\vert\downarrow\rangle$ and $\hat J_-\vert\downarrow\rangle = 0$ — the coefficient $\hbar\sqrt{(s+m)(s-m+1)}$ equals $\hbar\sqrt{1\cdot 1} = \hbar$ for $s = m = \tfrac12$. The total lowering operator is $\hat J_- = \hat J_{1-} + \hat J_{2-}$, each piece acting on its own particle. The general multiplet formula is

$$
\hat J_-\vert J,M\rangle = \hbar\sqrt{(J+M)(J-M+1)}\;\vert J,M-1\rangle.
$$

*Stretched state.* The state $\vert\uparrow\uparrow\rangle$ has $M = m_1 + m_2 = +1$, the maximum possible, and is the unique state at that $M$. It must therefore be the top of the $J = 1$ multiplet:

$$
\vert 1,1\rangle = \vert\uparrow\uparrow\rangle.
$$

*Lower the triplet.* Apply $\hat J_-$ two ways. By the multiplet formula with $J = 1$, $M = 1$:

$$
\hat J_-\vert 1,1\rangle = \hbar\sqrt{(1+1)(1-1+1)}\;\vert 1,0\rangle = \hbar\sqrt{2}\;\vert 1,0\rangle.
$$

By direct action on $\vert\uparrow\uparrow\rangle$:

$$
\hat J_-\vert\uparrow\uparrow\rangle = (\hat J_{1-} + \hat J_{2-})\vert\uparrow\uparrow\rangle = \hbar\vert\downarrow\uparrow\rangle + \hbar\vert\uparrow\downarrow\rangle.
$$

Equating the two and dividing by $\hbar\sqrt 2$,

$$
\vert 1,0\rangle = \frac{1}{\sqrt 2}\bigl(\vert\uparrow\downarrow\rangle + \vert\downarrow\uparrow\rangle\bigr).
$$

Lower once more. By the formula with $J = 1$, $M = 0$: $\hat J_-\vert 1,0\rangle = \hbar\sqrt{(1)(2)}\;\vert 1,-1\rangle = \hbar\sqrt 2\,\vert 1,-1\rangle$. Directly,

$$
\hat J_-\,\frac{1}{\sqrt 2}\bigl(\vert\uparrow\downarrow\rangle + \vert\downarrow\uparrow\rangle\bigr) = \frac{1}{\sqrt 2}\bigl(\hbar\vert\downarrow\downarrow\rangle + \hbar\vert\downarrow\downarrow\rangle\bigr) = \hbar\sqrt 2\,\vert\downarrow\downarrow\rangle,
$$

so $\vert 1,-1\rangle = \vert\downarrow\downarrow\rangle$. The three triplet states are

$$
\vert 1,1\rangle = \vert\uparrow\uparrow\rangle, \qquad \vert 1,0\rangle = \tfrac{1}{\sqrt2}\bigl(\vert\uparrow\downarrow\rangle + \vert\downarrow\uparrow\rangle\bigr), \qquad \vert 1,-1\rangle = \vert\downarrow\downarrow\rangle.
$$

*The singlet by orthogonality.* The $M = 0$ subspace is two-dimensional, spanned by $\vert\uparrow\downarrow\rangle$ and $\vert\downarrow\uparrow\rangle$. One combination is the triplet $\vert 1,0\rangle$; the remaining orthogonal direction is the only candidate for $\vert 0,0\rangle$. Write $\vert 0,0\rangle = a\vert\uparrow\downarrow\rangle + b\vert\downarrow\uparrow\rangle$. Orthogonality to $\vert 1,0\rangle$ requires

$$
\langle 1,0\vert 0,0\rangle = \frac{1}{\sqrt 2}(a + b) = 0,
$$

which forces $b = -a$.

Normalization gives $\vert a\vert^2 + \vert b\vert^2 = 2\vert a\vert^2 = 1$, so $\vert a\vert = 1/\sqrt2$. The Condon–Shortley phase convention fixes the coefficient of the highest-$m_1$ component ($\vert\uparrow\downarrow\rangle$, $m_1 = +\tfrac12$) to be positive, $a = +1/\sqrt2$. Hence

$$
\vert 0,0\rangle = \frac{1}{\sqrt 2}\bigl(\vert\uparrow\downarrow\rangle - \vert\downarrow\uparrow\rangle\bigr).
$$

*Consistency check.* A genuine $J = 0$ state is annihilated by every component of $\hat{\boldsymbol J}$. Indeed $\hat J_z\vert 0,0\rangle = 0$ (each term has $M = 0$), and

$$
\hat J_-\vert 0,0\rangle = \frac{1}{\sqrt2}\bigl(\hbar\vert\downarrow\downarrow\rangle - \hbar\vert\downarrow\downarrow\rangle\bigr) = 0, \qquad \hat J_+\vert 0,0\rangle = \frac{1}{\sqrt2}\bigl(\hbar\vert\uparrow\uparrow\rangle - \hbar\vert\uparrow\uparrow\rangle\bigr) = 0.
$$

Since $\hat J^2 = \hat J_-\hat J_+ + \hat J_z^2 + \hbar\hat J_z$, all three terms vanish on $\vert 0,0\rangle$, confirming $\hat J^2\vert 0,0\rangle = 0$, i.e. $J = 0$. The count is $3 + 1 = 4 = 2\times 2$: the triplet plus the singlet exhaust the two-spin Hilbert space, $\tfrac12\otimes\tfrac12 = 1 \oplus 0$.

<!-- ─── -->

**3. Coupling scheme.** Two identical fermions occupy the same spatial orbital $\phi(\boldsymbol r)$. Explain why the spin state must be the singlet and why triplet spin states are forbidden.

**Solution.**

*The antisymmetry requirement.* Identical fermions obey the spin-statistics theorem: the total many-body wavefunction must be **antisymmetric** under exchange of all coordinates of the two particles. For two particles the full state factorizes (when spatial and spin degrees of freedom are independent) as

$$
\Psi = \Psi_{\text{space}}(\boldsymbol r_1, \boldsymbol r_2)\;\otimes\;\chi_{\text{spin}}(s_1, s_2),
$$

and exchanging the particles acts as $\hat P_{12} = \hat P_{12}^{\text{space}}\,\hat P_{12}^{\text{spin}}$. Antisymmetry of the whole means

$$
\hat P_{12}\Psi = -\Psi.
$$

*The spatial part is symmetric.* Both fermions occupy the **same** orbital $\phi$, so the spatial wavefunction is the product

$$
\Psi_{\text{space}}(\boldsymbol r_1, \boldsymbol r_2) = \phi(\boldsymbol r_1)\,\phi(\boldsymbol r_2).
$$

Swapping $\boldsymbol r_1 \leftrightarrow \boldsymbol r_2$ leaves this unchanged: $\hat P_{12}^{\text{space}}\Psi_{\text{space}} = +\Psi_{\text{space}}$. (Two distinct orbitals could be combined symmetrically or antisymmetrically; a single shared orbital admits only the symmetric product.)

*Therefore the spin part must be antisymmetric.* For the product to satisfy $\hat P_{12}\Psi = -\Psi$ while the spatial factor contributes $+1$, the spin factor must contribute $-1$:

$$
(+1)\times(\text{spin parity}) = -1,
$$

so $\hat P_{12}^{\text{spin}}\chi_{\text{spin}} = -\chi_{\text{spin}}$.

*Identifying the spin state.* From Problem 2, the two-spin-1/2 states split by exchange parity:

- the **triplet** $\vert 1, M\rangle$ ($J = 1$, three states) is **symmetric**, $\hat P_{12}^{\text{spin}}\vert 1,M\rangle = +\vert 1,M\rangle$;
- the **singlet** $\vert 0,0\rangle$ ($J = 0$, one state) is **antisymmetric**, $\hat P_{12}^{\text{spin}}\vert 0,0\rangle = -\vert 0,0\rangle$.

The only antisymmetric spin state is the singlet, so the two electrons must be spin-paired:

$$
\chi_{\text{spin}} = \vert 0,0\rangle = \tfrac{1}{\sqrt2}\bigl(\vert\uparrow\downarrow\rangle - \vert\downarrow\uparrow\rangle\bigr).
$$

The three triplet states are **forbidden**: pairing a symmetric spatial part with a symmetric triplet gives a fully symmetric $\Psi$, which would violate fermion antisymmetry. This is exactly the Pauli exclusion principle in its wavefunction form — and the reason the helium ground state ($1s^2$) has both electrons in the $1s$ orbital locked into a spin singlet.

<!-- ─── -->

★ **4. Spin-orbit coupling.** A particle of orbital angular momentum $\hat{\boldsymbol L}$ and spin $\hat{\boldsymbol S}$ (with spin quantum number $s = 1/2$) has a **spin-orbit interaction**

$$
\hat H_\text{SO} = \lambda\,\hat{\boldsymbol L}\cdot\hat{\boldsymbol S},
$$

where $\lambda$ is a real coupling constant of dimension energy$/\hbar^{2}$. Let $\hat{\boldsymbol J} = \hat{\boldsymbol L} + \hat{\boldsymbol S}$ be the total angular momentum, and let $\vert\ell, s; j, m_j\rangle$ denote the **coupled basis** — the simultaneous eigenstates of $\{\hat L^{2}, \hat S^{2}, \hat J^{2}, \hat J_z\}$ with eigenvalues $\hbar^{2}\ell(\ell+1)$, $\hbar^{2}s(s+1)$, $\hbar^{2}j(j+1)$, and $\hbar m_j$, where the orbital quantum number $\ell = 0, 1, 2, \ldots$, the total quantum number $j \in \{\vert\ell - s\vert,\ldots,\ell + s\}$, and the magnetic quantum number $m_j \in \{-j,\ldots,+j\}$.

(a) Show that

$$
\hat{\boldsymbol L}\cdot\hat{\boldsymbol S} = \frac{1}{2}\bigl(\hat J^{2} - \hat L^{2} - \hat S^{2}\bigr).
$$

(b) Use (a) to compute $\langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle$ in the coupled state $\vert\ell, \tfrac12; j, m_j\rangle$. Verify the answer is independent of $m_j$.

(c) For the hydrogen $2p$ level ($\ell = 1$), find the **fine-structure splitting** $\Delta E$ between the $j = 3/2$ and $j = 1/2$ sublevels in terms of $\lambda$.

**Solution.**

*The operator identity.* Define the total angular momentum $\hat{\boldsymbol J} = \hat{\boldsymbol L} + \hat{\boldsymbol S}$ and square it:

$$
\begin{split}
\hat J^2 &= (\hat{\boldsymbol L} + \hat{\boldsymbol S})\cdot(\hat{\boldsymbol L} + \hat{\boldsymbol S})\\
&= \hat L^2 + \hat S^2 + \hat{\boldsymbol L}\cdot\hat{\boldsymbol S} + \hat{\boldsymbol S}\cdot\hat{\boldsymbol L}.
\end{split}
$$

The orbital operator $\hat{\boldsymbol L}$ acts on the spatial factor of the Hilbert space and the spin operator $\hat{\boldsymbol S}$ on the spin factor; they live on different tensor slots, so $[\hat L_i, \hat S_j] = 0$ for all $i, j$. Consequently the two cross terms are equal,

$$
\hat{\boldsymbol L}\cdot\hat{\boldsymbol S} = \sum_i \hat L_i\hat S_i = \sum_i \hat S_i\hat L_i = \hat{\boldsymbol S}\cdot\hat{\boldsymbol L},
$$

and they combine: $\hat J^2 = \hat L^2 + \hat S^2 + 2\,\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}$. Solving,

$$
\hat{\boldsymbol L}\cdot\hat{\boldsymbol S} = \frac12\bigl(\hat J^2 - \hat L^2 - \hat S^2\bigr). \qquad\checkmark
$$

*Expectation in the coupled basis.* The coupled states $\vert\ell,\tfrac12; j, m_j\rangle$ are simultaneous eigenstates of $\hat J^2$, $\hat L^2$, and $\hat S^2$ — so $\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}$ is **diagonal** in this basis. With $\hat J^2 \to \hbar^2 j(j+1)$, $\hat L^2 \to \hbar^2\ell(\ell+1)$, and $\hat S^2 \to \hbar^2 s(s+1) = \hbar^2\cdot\tfrac34$ (since $s = \tfrac12$),

$$
\langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle = \frac{\hbar^2}{2}\left[\,j(j+1) - \ell(\ell+1) - \tfrac34\,\right].
$$

*Hydrogen $2p$.* The $2p$ level has $\ell = 1$. Coupling to $s = \tfrac12$ gives $j = \ell \pm \tfrac12 = \tfrac32$ or $\tfrac12$ (the triangle rule). Evaluate the bracket for each:

$$
\begin{split}
j = \tfrac32:\quad \langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle &= \frac{\hbar^2}{2}\left[\tfrac32\cdot\tfrac52 - 1\cdot 2 - \tfrac34\right] = \frac{\hbar^2}{2}\cdot\frac{15 - 8 - 3}{4} = +\frac{\hbar^2}{2},\\
j = \tfrac12:\quad \langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle &= \frac{\hbar^2}{2}\left[\tfrac12\cdot\tfrac32 - 1\cdot 2 - \tfrac34\right] = \frac{\hbar^2}{2}\cdot\frac{3 - 8 - 3}{4} = -\hbar^2.
\end{split}
$$

*Fine-structure splitting.* The spin-orbit Hamiltonian is $\hat H_{SO} = \lambda\,\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}$, so the energy shift of each level is $E_j = \lambda\,\langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle$:

$$
E_{3/2} = +\frac{\lambda\hbar^2}{2}, \qquad E_{1/2} = -\lambda\hbar^2.
$$

The splitting between the two fine-structure levels is

$$
\Delta E = E_{3/2} - E_{1/2} = \frac{\lambda\hbar^2}{2} - (-\lambda\hbar^2) = \frac{3}{2}\,\lambda\hbar^2.
$$

For $\lambda > 0$ the $2p_{3/2}$ level lies above $2p_{1/2}$. As a check, the degeneracy-weighted "center of gravity" is unshifted: $(2j+1)$-weighted average $= \tfrac{1}{6}\bigl[4\cdot(+\tfrac{\lambda\hbar^2}{2}) + 2\cdot(-\lambda\hbar^2)\bigr] = \tfrac16(2\lambda\hbar^2 - 2\lambda\hbar^2) = 0$, as it must be since $\operatorname{Tr}\hat{\boldsymbol L}\cdot\hat{\boldsymbol S} = 0$.

<!-- ─── -->

★ **5. Spin-1 and spin-1/2 coupling.** Consider spin-1 particle $A$ and spin-1/2 particle $B$, with total $\hat{\boldsymbol J}=\hat{\boldsymbol S}_A+\hat{\boldsymbol S}_B$ and Hamiltonian

$$
\hat H=-\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B.
$$

Work in the uncoupled basis $\vert 1,m_A\rangle\vert\tfrac12,m_B\rangle$.

(a) Since $\hat J_z$ commutes with $\hat H$, block-diagonalize $\hat H$ by fixed $M=m_A+m_B$. Diagonalize each $M$ block, then identify $J$ from

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B
=\frac12\bigl(\hat J^2-\hat S_A^2-\hat S_B^2\bigr),
$$

so each eigenvalue determines whether the state belongs to $J=\tfrac32$ or $J=\tfrac12$. Check that for each fixed $J$, the allowed $M$ values run from $-J$ to $J$.

(b) Build the unitary matrix $U$ from uncoupled to coupled basis,

$$
\vert J,M\rangle=\sum_{m_A,m_B} U_{(m_A,m_B),(J,M)}\,\vert 1,m_A;\tfrac12,m_B\rangle,
$$

with $U_{(m_A,m_B),(J,M)}=\langle1,m_A;\tfrac12,m_B\vert J,M\rangle$. Explain why each fixed-$M$ sub-block of $U$ is exactly a Clebsch--Gordan coefficient matrix. Compute explicitly the $M=\tfrac12$ block.

(c) Define projectors

$$
\hat P_{J}=\sum_{M=-J}^{J}\vert J,M\rangle\langle J,M\vert,
\qquad J\in\left\{\tfrac12,\tfrac32\right\}.
$$

Using the coupled states from parts (a)--(b), verify

$$
\hat P_{1/2}+\hat P_{3/2}=\hat I,
\qquad
\hat P_{1/2}\hat P_{3/2}=0.
$$

Then show these projectors can be written as functions of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$:

$$
\hat P_{1/2}=-\frac{2}{3}\left(\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B-\frac{1}{2}\hat I\right),
\qquad
\hat P_{3/2}=\frac{2}{3}\left(\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B+\hat I\right).
$$

**Solution.**

Throughout this problem set $\hbar = 1$, so spin operators are dimensionless and $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ is measured in units of $\hbar^2$ — the convention in which the projector formulas of part (c) hold as written.

The uncoupled basis has $3\times 2 = 6$ states $\vert m_A\rangle\vert m_B\rangle$ with $m_A\in\{1,0,-1\}$ and $m_B\in\{+\tfrac12,-\tfrac12\}$. The triangle rule gives $J\in\{\tfrac12,\tfrac32\}$, with $2 + 4 = 6$ coupled states — the dimension matches.

**(a) Block-diagonalization and diagonalization.**

Since $\hat H = -\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$, we diagonalize $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ block by block; each eigenvalue $\mu$ of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ gives energy $E = -\mu$ under $\hat H$.

Since $[\hat J_z, \hat H] = 0$, states of different $M = m_A + m_B$ do not mix; $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ is block-diagonal in $M$. Sorting the six uncoupled states:

| $M$ | uncoupled states $\vert m_A, m_B\rangle$ | block size |
|------|------------------------------------------|------------|
| $+\tfrac32$ | $\vert 1,+\tfrac12\rangle$ | $1\times 1$ |
| $+\tfrac12$ | $\vert 1,-\tfrac12\rangle,\;\vert 0,+\tfrac12\rangle$ | $2\times 2$ |
| $-\tfrac12$ | $\vert 0,-\tfrac12\rangle,\;\vert -1,+\tfrac12\rangle$ | $2\times 2$ |
| $-\tfrac32$ | $\vert -1,-\tfrac12\rangle$ | $1\times 1$ |

Write the coupling operator in ladder form:

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B = \hat S_{Az}\hat S_{Bz} + \tfrac12\bigl(\hat S_{A+}\hat S_{B-} + \hat S_{A-}\hat S_{B+}\bigr).
$$

The relevant ladder coefficients are $\hat S_{A\pm}\vert m_A\rangle = \sqrt{(1\mp m_A)(1\pm m_A + 1)}\,\vert m_A\pm 1\rangle$ (so $\hat S_{A\pm}$ acting between $m_A = 0$ and $m_A = \pm1$ carries a factor $\sqrt2$), and $\hat S_{B\pm}$ flips $m_B$ with coefficient $1$.

*The $M = \pm\tfrac32$ blocks.* For the stretched state $\vert 1,+\tfrac12\rangle$ both ladder terms vanish ($\hat S_{A+}$ and $\hat S_{B+}$ annihilate the top weights), leaving only $\hat S_{Az}\hat S_{Bz} = (1)(\tfrac12) = +\tfrac12$. Likewise $\vert -1,-\tfrac12\rangle$ gives $(-1)(-\tfrac12) = +\tfrac12$. So both $1\times 1$ blocks are already eigenstates of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ with eigenvalue $\mu = +\tfrac12$.

*The $M = +\tfrac12$ block.* In the ordered basis $\{\vert 1,-\tfrac12\rangle,\;\vert 0,+\tfrac12\rangle\}$:

- $\hat S_{Az}\hat S_{Bz}$ is diagonal: $(1)(-\tfrac12) = -\tfrac12$ on the first state, $(0)(+\tfrac12) = 0$ on the second.
- $\tfrac12\hat S_{A+}\hat S_{B-}$ maps $\vert 0,+\tfrac12\rangle \to \tfrac12\sqrt2\,\vert 1,-\tfrac12\rangle = \tfrac{1}{\sqrt2}\vert 1,-\tfrac12\rangle$, and annihilates $\vert 1,-\tfrac12\rangle$.
- $\tfrac12\hat S_{A-}\hat S_{B+}$ maps $\vert 1,-\tfrac12\rangle \to \tfrac{1}{\sqrt2}\vert 0,+\tfrac12\rangle$, and annihilates $\vert 0,+\tfrac12\rangle$.

Collecting the matrix elements,

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B\Big\vert_{M=1/2} = \begin{pmatrix} -\tfrac12 & \tfrac{1}{\sqrt2}\\[2pt] \tfrac{1}{\sqrt2} & 0 \end{pmatrix}.
$$

The characteristic equation for the eigenvalues $\mu$ of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ is $\mu^2 + \tfrac12\mu - \tfrac12 = 0$, with roots

$$
\mu = \frac{-\tfrac12 \pm \sqrt{\tfrac14 + 2}}{2} = \frac{-\tfrac12 \pm \tfrac32}{2} = \left\{+\tfrac12,\;-1\right\}.
$$

The normalized eigenvectors of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ (one per $\mu$) are

$$
\mu = +\tfrac12:\;\; \tfrac{1}{\sqrt3}\vert 1,-\tfrac12\rangle + \sqrt{\tfrac23}\,\vert 0,+\tfrac12\rangle, \qquad
\mu = -1:\;\; \sqrt{\tfrac23}\,\vert 1,-\tfrac12\rangle - \tfrac{1}{\sqrt3}\vert 0,+\tfrac12\rangle.
$$

*The $M = -\tfrac12$ block.* In the basis $\{\vert 0,-\tfrac12\rangle,\;\vert -1,+\tfrac12\rangle\}$ the same computation gives

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B\Big\vert_{M=-1/2} = \begin{pmatrix} 0 & \tfrac{1}{\sqrt2}\\[2pt] \tfrac{1}{\sqrt2} & -\tfrac12 \end{pmatrix},
$$

with the same $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ eigenvalues $\mu \in \{+\tfrac12,\,-1\}$ and eigenvectors

$$
\mu = +\tfrac12:\;\; \sqrt{\tfrac23}\,\vert 0,-\tfrac12\rangle + \tfrac{1}{\sqrt3}\vert -1,+\tfrac12\rangle, \qquad
\mu = -1:\;\; \tfrac{1}{\sqrt3}\vert 0,-\tfrac12\rangle - \sqrt{\tfrac23}\,\vert -1,+\tfrac12\rangle.
$$

*Identifying $J$.* On any coupled state, $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ is a number because $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B = \tfrac12(\hat J^2 - \hat S_A^2 - \hat S_B^2)$ with $\hat S_A^2 = 1(2) = 2$ and $\hat S_B^2 = \tfrac12\cdot\tfrac32 = \tfrac34$:

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B = \tfrac12 J(J+1) - \tfrac{11}{8}.
$$

Inverting the two eigenvalues of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$: $\mu = +\tfrac12 \Rightarrow J(J+1) = \tfrac{15}{4} \Rightarrow J = \tfrac32$; $\mu = -1 \Rightarrow J(J+1) = \tfrac34 \Rightarrow J = \tfrac12$. Collecting the coupled states (Condon–Shortley convention):

$$
\begin{split}
\vert\tfrac32,+\tfrac32\rangle &= \vert 1,+\tfrac12\rangle,\\
\vert\tfrac32,+\tfrac12\rangle &= \tfrac{1}{\sqrt3}\vert 1,-\tfrac12\rangle + \sqrt{\tfrac23}\,\vert 0,+\tfrac12\rangle,\\
\vert\tfrac32,-\tfrac12\rangle &= \sqrt{\tfrac23}\,\vert 0,-\tfrac12\rangle + \tfrac{1}{\sqrt3}\vert -1,+\tfrac12\rangle,\\
\vert\tfrac32,-\tfrac32\rangle &= \vert -1,-\tfrac12\rangle,
\end{split}
$$

$$
\begin{split}
\vert\tfrac12,+\tfrac12\rangle &= \sqrt{\tfrac23}\,\vert 1,-\tfrac12\rangle - \tfrac{1}{\sqrt3}\vert 0,+\tfrac12\rangle,\\
\vert\tfrac12,-\tfrac12\rangle &= \tfrac{1}{\sqrt3}\vert 0,-\tfrac12\rangle - \sqrt{\tfrac23}\,\vert -1,+\tfrac12\rangle.
\end{split}
$$

The eigenvalue $\mu = +\tfrac12$ of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ ($J=\tfrac32$) appears at $M = +\tfrac32, +\tfrac12, -\tfrac12, -\tfrac32$ — exactly $M$ from $-J$ to $J$ — and $\mu = -1$ ($J=\tfrac12$) appears at $M = +\tfrac12, -\tfrac12$, again $-J$ to $J$. ✓ The corresponding **energy** eigenvalues under $\hat H = -\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ are $E_{3/2} = -\mu = -\tfrac12$ (4-fold) and $E_{1/2} = +1$ (2-fold).

**(b) The change-of-basis matrix.**

The selection rule $M = m_A + m_B$ means a coupled state $\vert J,M\rangle$ expands only over uncoupled states of the same $M$. Hence $U$, ordered by $M$, is **block-diagonal**: the $M = \pm\tfrac32$ sectors are $1\times 1$ and the $M = \pm\tfrac12$ sectors are $2\times 2$. Each block's entries are by definition the coefficients $\langle 1,m_A;\tfrac12,m_B\vert J,M\rangle$ for fixed $M$ — i.e. precisely the Clebsch–Gordan coefficients. Because both the uncoupled and coupled states within a fixed-$M$ subspace are orthonormal bases of that subspace, each block is a (real, orthogonal) unitary matrix; that is the content of "each fixed-$M$ sub-block is a CG matrix."

For $M = +\tfrac12$, rows labelled by uncoupled $(m_A, m_B) \in \{(1,-\tfrac12),\,(0,+\tfrac12)\}$ and columns by coupled $(J,M) \in \{(\tfrac32,\tfrac12),\,(\tfrac12,\tfrac12)\}$, the eigenvectors from part (a) give

$$
U^{(M=1/2)} = \begin{pmatrix} \langle 1,1;\tfrac12,-\tfrac12\vert\tfrac32,\tfrac12\rangle & \langle 1,1;\tfrac12,-\tfrac12\vert\tfrac12,\tfrac12\rangle\\[4pt] \langle 1,0;\tfrac12,\tfrac12\vert\tfrac32,\tfrac12\rangle & \langle 1,0;\tfrac12,\tfrac12\vert\tfrac12,\tfrac12\rangle \end{pmatrix} = \begin{pmatrix} \sqrt{\tfrac13} & \sqrt{\tfrac23}\\[4pt] \sqrt{\tfrac23} & -\sqrt{\tfrac13} \end{pmatrix}.
$$

Its columns are orthonormal and $\det U^{(M=1/2)} = -\tfrac13 - \tfrac23 = -1$, confirming it is orthogonal. (The $M = +\tfrac32$ block is the $1\times 1$ matrix $(1)$; the $M = -\tfrac12$ and $M = -\tfrac32$ blocks follow identically from the corresponding states above.)

**(c) The projectors.**

*Completeness, $\hat P_{1/2} + \hat P_{3/2} = \hat I$.* The six coupled states listed in (a) are mutually orthonormal: within each $2\times 2$ block they are orthonormal by construction (eigenvectors of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ in that $M$ sector), and states from different $M$ blocks are automatically orthogonal because $\hat J_z$ has different eigenvalues. Six orthonormal vectors span the entire 6-dimensional space, so they form a complete basis:

$$
\sum_{J,M}\vert J,M\rangle\langle J,M\vert = \hat I.
$$

Splitting the sum into its $J = \tfrac32$ and $J = \tfrac12$ parts is exactly $\hat P_{3/2} + \hat P_{1/2} = \hat I$. ✓

*Orthogonality, $\hat P_{1/2}\hat P_{3/2} = 0$.* Using $\langle\tfrac12,M\vert\tfrac32,M'\rangle = 0$ (coupled states with different $J$ are orthogonal),

$$
\hat P_{1/2}\hat P_{3/2} = \sum_{M,M'}\vert\tfrac12,M\rangle\underbrace{\langle\tfrac12,M\vert\tfrac32,M'\rangle}_{=\,0}\langle\tfrac32,M'\vert = 0. \qquad\checkmark
$$

So $\hat P_{1/2}$ and $\hat P_{3/2}$ are complementary orthogonal projectors, as projectors onto the two coupled subspaces must be.

*Projectors as functions of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$.* Part (a) showed $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ is constant on each coupled subspace, with eigenvalue $\mu = +\tfrac12$ on the $J = \tfrac32$ space and $\mu = -1$ on the $J = \tfrac12$ space. Its spectral decomposition is therefore

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B = \tfrac12\,\hat P_{3/2} - 1\cdot\hat P_{1/2}.
$$

Together with the completeness relation $\hat I = \hat P_{3/2} + \hat P_{1/2}$, this is a $2\times 2$ linear system for the two projectors. Adding the two equations,

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B + \hat I = \bigl(\tfrac12 + 1\bigr)\hat P_{3/2} + (-1 + 1)\hat P_{1/2} = \tfrac32\,\hat P_{3/2},
$$

so $\hat P_{3/2} = \tfrac23\bigl(\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B + \hat I\bigr)$.

Forming instead $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B - \tfrac12\hat I$,

$$
\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B - \tfrac12\hat I = \bigl(\tfrac12 - \tfrac12\bigr)\hat P_{3/2} + \bigl(-1 - \tfrac12\bigr)\hat P_{1/2} = -\tfrac32\,\hat P_{1/2},
$$

so $\hat P_{1/2} = -\tfrac23\bigl(\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B - \tfrac12\hat I\bigr)$.

These are exactly the stated formulas. As a check, evaluate them on each subspace: on $J = \tfrac32$ ($\mu = +\tfrac12$), $\hat P_{3/2} = \tfrac23(\tfrac12 + 1) = 1$ and $\hat P_{1/2} = -\tfrac23(\tfrac12 - \tfrac12) = 0$; on $J = \tfrac12$ ($\mu = -1$), $\hat P_{3/2} = \tfrac23(-1 + 1) = 0$ and $\hat P_{1/2} = -\tfrac23(-1 - \tfrac12) = 1$. Each projector is $1$ on its own subspace and $0$ on the other. ✓ The construction works because $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ has only two distinct eigenvalues $\mu \in \{+\tfrac12,-1\}$, so any function of $\hat{\boldsymbol S}_A\cdot\hat{\boldsymbol S}_B$ — in particular each projector — is fixed by its two values via linear (Lagrange) interpolation.


<!-- ─── -->

**6. Lande g-factor.** An atom has orbital angular momentum $\ell$ and spin $s$, coupling to total $j = \vert\ell - s\vert, \ldots, \ell + s$. In a weak external magnetic field $B$ along $\boldsymbol{e}_z$, the magnetic energy is

$$
\hat H_Z = -\boldsymbol{\hat\mu}\cdot\boldsymbol B = -\bigl(g_L\hat L_z + g_S\hat S_z\bigr)\mu_B B/\hbar,
$$

with $g_L = 1$, $g_S = 2$ (electron values), and $\mu_B = e\hbar/(2m_e)$ the Bohr magneton.

(a) In the coupled basis $\vert\ell, s; j, m_j\rangle$, the operator $\hat L_z + 2\hat S_z = \hat J_z + \hat S_z$ is not diagonal in $j$ alone (it mixes different $j$ values within the same $m_j$). Within a fixed-$j$ subspace, any vector operator $\hat{\boldsymbol V}$ has matrix elements proportional to those of $\hat{\boldsymbol J}$:

$$
\langle j, m_j\vert\hat S_z\vert j, m_j\rangle = \frac{\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol S}\rangle}{\hbar^2 j(j+1)}\,\hbar m_j.
$$

This is the **vector-projection identity**: within a fixed-$j$ subspace, the expectation of any vector operator equals the component along $\hat{\boldsymbol J}$, scaled by $m_j/j(j+1)$. (The perpendicular components average to zero by axial symmetry about $\hat{\boldsymbol J}$ — cf. 2.2.1 P5 for the same averaging on $\hat J_x$, $\hat J_y$.)

(b) Using $\hat{\boldsymbol J}\cdot\hat{\boldsymbol S} = \tfrac{1}{2}(\hat J^2 - \hat L^2 + \hat S^2)$ (derive this by squaring $\hat{\boldsymbol L} = \hat{\boldsymbol J} - \hat{\boldsymbol S}$), show

$$
\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol S}\rangle = \frac{\hbar^2}{2}\bigl[j(j+1) - \ell(\ell+1) + s(s+1)\bigr].
$$

(c) Combine (a) and (b) to derive the **Lande g-factor**

$$
g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)},
$$

so that the Zeeman energy shift in the coupled basis is $\Delta E = g_J\mu_B B m_j$.

(d) Evaluate $g_J$ for hydrogen $2p_{3/2}$ ($\ell = 1, s = 1/2, j = 3/2$) and $2p_{1/2}$ ($\ell = 1, s = 1/2, j = 1/2$). Show $g_J(2p_{3/2}) = 4/3$ and $g_J(2p_{1/2}) = 2/3$. The two fine-structure levels Zeeman-split by *different* amounts under the same field — the experimental signature that distinguishes spin from orbital angular momentum.

**Solution.**

(a) The vector-projection identity says that within a fixed-$j$ subspace, any vector operator $\hat{\boldsymbol V}$ (one that transforms as a 3-vector under rotations) has matrix elements proportional to those of $\hat{\boldsymbol J}$:

$$
\langle j, m_j\vert\hat V_z\vert j, m_j\rangle = \frac{\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol V}\rangle_j}{\hbar^2 j(j+1)}\,\hbar m_j,
$$

where $\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol V}\rangle_j$ is the (state-independent) scalar overlap on the fixed-$j$ subspace. The intuition: $\hat{\boldsymbol J}$ generates rotations of the $j$-multiplet, and any vector operator's expectation values are determined by its projection onto $\hat{\boldsymbol J}$ — perpendicular components average to zero by axial symmetry (cf. 2.2.1 P5). Applied to $\hat{\boldsymbol V} = \hat{\boldsymbol S}$:

$$
\langle\hat S_z\rangle_{j, m_j} = \frac{\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol S}\rangle_j}{\hbar^2 j(j+1)}\,\hbar m_j.
$$

(b) Square the operator identity $\hat{\boldsymbol L} = \hat{\boldsymbol J} - \hat{\boldsymbol S}$:

$$
\hat L^2 = \hat J^2 + \hat S^2 - 2\hat{\boldsymbol J}\cdot\hat{\boldsymbol S},
$$

so $\hat{\boldsymbol J}\cdot\hat{\boldsymbol S} = \tfrac{1}{2}\bigl(\hat J^2 - \hat L^2 + \hat S^2\bigr)$.

On the coupled basis $\vert\ell, s; j, m_j\rangle$ — simultaneous eigenstates of $\hat J^2, \hat L^2, \hat S^2$ — the expectation value is

$$
\langle\hat{\boldsymbol J}\cdot\hat{\boldsymbol S}\rangle = \tfrac{\hbar^2}{2}\bigl[j(j+1) - \ell(\ell+1) + s(s+1)\bigr]. \quad\checkmark
$$

(c) The Zeeman Hamiltonian rewrites as $\hat H_Z = -(\hat J_z + \hat S_z)\mu_B B/\hbar$ (using $g_L = 1, g_S = 2$). On the coupled state $\vert\ell, s; j, m_j\rangle$:

$$
\langle\hat H_Z\rangle = -\bigl(\langle\hat J_z\rangle + \langle\hat S_z\rangle\bigr)\mu_B B/\hbar = -\bigl(\hbar m_j + \langle\hat S_z\rangle\bigr)\mu_B B/\hbar.
$$

Substitute $\langle\hat S_z\rangle$ from (a) and (b):

$$
\langle\hat S_z\rangle = \frac{\hbar^2/2\cdot[j(j+1) - \ell(\ell+1) + s(s+1)]}{\hbar^2 j(j+1)}\hbar m_j = \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}\hbar m_j.
$$

Then

$$
\Delta E_Z = -\langle\hat H_Z\rangle = \mu_B B m_j\left[1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}\right] = g_J\mu_B B m_j,
$$

with

$$
\boxed{g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}.}
$$

(d) Substitute $\ell = 1$, $s = 1/2$ for hydrogen $2p$.

**$2p_{3/2}$** ($j = 3/2$): $j(j+1) = 15/4$, $s(s+1) = 3/4$, $\ell(\ell+1) = 2$. Numerator: $15/4 + 3/4 - 2 = 18/4 - 2 = 5/2$. Denominator: $2 \cdot 15/4 = 15/2$. Ratio: $(5/2)/(15/2) = 1/3$.

$$
g_J(2p_{3/2}) = 1 + 1/3 = 4/3.
$$

**$2p_{1/2}$** ($j = 1/2$): $j(j+1) = 3/4$, $s(s+1) = 3/4$, $\ell(\ell+1) = 2$. Numerator: $3/4 + 3/4 - 2 = 3/2 - 2 = -1/2$. Denominator: $2 \cdot 3/4 = 3/2$. Ratio: $(-1/2)/(3/2) = -1/3$.

$$
g_J(2p_{1/2}) = 1 - 1/3 = 2/3.
$$

**Physical interpretation.** Even though $2p_{3/2}$ and $2p_{1/2}$ have the same $\ell$ and $s$, they Zeeman-split by *different* amounts under the same applied field — $g_J$ depends on $j$, not on $\ell$ and $s$ separately. Hydrogen $2p_{3/2}$ splits twice as fast as $2p_{1/2}$ ($g_J = 4/3$ vs $2/3$). This is the **anomalous Zeeman effect** for atoms with $L \neq 0$ and $S \neq 0$ — the signature that orbital and spin angular momenta combine via the vector-projection identity, not as separate additive contributions. Experimentally, the line splitting patterns of $2p_{3/2} \to 1s_{1/2}$ and $2p_{1/2} \to 1s_{1/2}$ transitions under an external field encode the values of $g_J$ for each level — historically how *spin* was first inferred from atomic spectra.

<!-- ─── -->

**7. Two-electron exchange interaction.** Two electrons interact through the **exchange Hamiltonian** $\hat H_{\mathrm{ex}} = -J\,\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$ (with $J$ the exchange coupling, $\hat S = \hat\sigma/2$ in units of $\hbar$). This is the simplest two-spin Heisenberg model — the same operator appearing in 2.1.1 Problem 6 as the lattice Heisenberg interaction.

(a) Express $\hat H_{\mathrm{ex}}$ in terms of the total spin operators using $\hat S_{\mathrm{tot}}^2 = \hat S_1^2 + \hat S_2^2 + 2\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$.

(b) Evaluate $\hat H_{\mathrm{ex}}$ on the singlet $\vert 0,0\rangle$ and on each triplet state $\vert 1, M\rangle$. Show that the triplet has energy $-J/4$ and the singlet has energy $+3J/4$.

(c) Hence the singlet-triplet splitting is

$$
\Delta E_{\mathrm{st}} = E_{\mathrm{singlet}} - E_{\mathrm{triplet}} = J.
$$

For $J > 0$ (ferromagnetic coupling), the triplet is the ground state — aligned spins are favoured. For $J < 0$ (antiferromagnetic coupling), the singlet is the ground state — anti-aligned spins. Compare with the lattice Heisenberg model spectrum from 2.1.1 P6.

(d) Connect to two-electron chemistry. The Hund's rule for filled subshells favours maximal $S$ (triplet > singlet). Argue that this reflects an effectively *ferromagnetic* exchange between two electrons in the same orbital, originating from the electron-electron Coulomb repulsion combined with the antisymmetry of the spatial wavefunction (recall 2.2.3 Problem 3).

**Solution.**

(a) From $\hat S_{\mathrm{tot}}^2 = \hat S_1^2 + \hat S_2^2 + 2\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$, solve for the dot product:

$$
\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2 = \tfrac{1}{2}\bigl(\hat S_{\mathrm{tot}}^2 - \hat S_1^2 - \hat S_2^2\bigr).
$$

So

$$
\hat H_{\mathrm{ex}} = -J\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2 = -\tfrac{J}{2}\bigl(\hat S_{\mathrm{tot}}^2 - \hat S_1^2 - \hat S_2^2\bigr).
$$

In units where $\hbar = 1$, $\hat S_1^2 = \hat S_2^2 = 3/4$ (each is spin-1/2 with $s(s+1) = 3/4$), so

$$
\hat H_{\mathrm{ex}} = -\tfrac{J}{2}\hat S_{\mathrm{tot}}^2 + \tfrac{J}{2}\cdot\tfrac{3}{2} = -\tfrac{J}{2}\hat S_{\mathrm{tot}}^2 + \tfrac{3J}{4}.
$$

(b) On the **triplet** $\vert 1, M\rangle$, $\hat S_{\mathrm{tot}}^2 = 1\cdot 2 = 2$:

$$
E_{\mathrm{triplet}} = -\tfrac{J}{2}\cdot 2 + \tfrac{3J}{4} = -J + \tfrac{3J}{4} = -\tfrac{J}{4}.
$$

On the **singlet** $\vert 0, 0\rangle$, $\hat S_{\mathrm{tot}}^2 = 0$:

$$
E_{\mathrm{singlet}} = 0 + \tfrac{3J}{4} = +\tfrac{3J}{4}.
$$

Both triplet states have the same energy (degenerate, 3-fold) and the singlet sits at a different energy. $\checkmark$

(c) Splitting:

$$
\Delta E_{\mathrm{st}} = E_{\mathrm{singlet}} - E_{\mathrm{triplet}} = \tfrac{3J}{4} - (-\tfrac{J}{4}) = J.
$$

For $J > 0$ (the sign convention where $-J\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$ favours aligned spins): $E_{\mathrm{triplet}} < E_{\mathrm{singlet}}$, the triplet is the ground state, **ferromagnetic** coupling. For $J < 0$: signs reverse, singlet is the ground state, **antiferromagnetic** coupling.

**Comparison with 2.1.1 P6.** The lattice Heisenberg Hamiltonian $\hat H = J(\hat X\otimes\hat X + \hat Y\otimes\hat Y + \hat Z\otimes\hat Z) = 4J\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$ (the factor of $4$ comes from $\hat X = 2\hat S_x$ etc.) has eigenvalues $J\{+1, +1, +1, -3\}$ on the four two-qubit states. Translating to the present sign convention $\hat H_{\mathrm{ex}} = -J\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2$, the triplet sits at $-J/4$ (triply degenerate) and singlet at $+3J/4$ — exactly the singlet-triplet structure 2.1.1 P6 found, with the sign and prefactor adjusted by the change of normalization. The two problems describe the *same* physics from two perspectives: 2.1.1 P6 computed the Heisenberg Hamiltonian's spectrum directly in the tensor-product basis; here we use angular-momentum addition to reach the same result through coupled $\vert J, M\rangle$ states.

(d) **Hund's rules and exchange.** In a multi-electron atom, when two electrons occupy degenerate orbitals (e.g., two electrons in the three $2p$ orbitals of nitrogen), Hund's first rule says the lowest energy configuration has *maximum total spin* $S$. This is empirically a *ferromagnetic* preference for aligned spins.

The origin is electrostatic, not magnetic. The Pauli principle (2.2.3 P3) requires the total many-electron wavefunction to be antisymmetric. For two electrons:

- A **symmetric** spatial wavefunction (e.g., both in the same orbital) pairs with the **antisymmetric** spin singlet.
- An **antisymmetric** spatial wavefunction (e.g., distributed over two orthogonal orbitals with the $(\phi_1\phi_2 - \phi_2\phi_1)/\sqrt 2$ combination) pairs with the **symmetric** spin triplet.

The antisymmetric spatial wavefunction keeps the two electrons *spatially apart* (it vanishes at $\boldsymbol r_1 = \boldsymbol r_2$), reducing the Coulomb repulsion. So the triplet — paired with antisymmetric spatial part — has *lower* Coulomb energy than the singlet. The effective spin Hamiltonian $\hat H_{\mathrm{ex}}$ then has $J > 0$ (ferromagnetic), even though the underlying interaction is the spin-independent Coulomb repulsion.

**The exchange interaction is therefore not a magnetic interaction at all** — it is the Coulomb repulsion *projected* through the antisymmetry constraint into an effective spin-dependent term. This is the fundamental origin of magnetism in atoms (Hund's rules) and solids (Heisenberg ferromagnets and antiferromagnets), and the reason a single algebraic identity — $\hat{\boldsymbol S}_1\cdot\hat{\boldsymbol S}_2 = \tfrac{1}{2}(\hat S_{\mathrm{tot}}^2 - \hat S_1^2 - \hat S_2^2)$ — controls so much of magnetic ordering physics.
