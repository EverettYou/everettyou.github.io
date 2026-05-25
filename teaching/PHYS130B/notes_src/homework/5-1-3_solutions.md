# 5.1.3 Degenerate Perturbation Theory
Worked solutions for the homework problems in the [5.1.3 Degenerate Perturbation Theory](../ch5_perturbation-theory/5-1-3-degenerate-perturbation-theory) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Why the old formula fails.** Start from the non-degenerate first-order state correction formula and explain precisely where divergence appears for a $d$-fold degenerate level. Which hidden assumption about labeling eigenstates fails?

**Solution.**

The non-degenerate first-order state correction reads

$$
\vert n^{(1)}\rangle=\sum_{m\neq n}\vert m\rangle\,\frac{V_{mn}}{E_n-E_m},
\qquad V_{mn}=\langle m\vert\hat V\vert n\rangle.
$$

Suppose the level $E_n$ is $d$-fold degenerate, with an orthonormal basis
$\vert n,\alpha\rangle$, $\alpha=1,\dots,d$, all at the *same* energy $E_n$.
Pick one of them, $\vert n,\alpha\rangle$, and apply the formula. The sum "over
$m\neq n$" must be read as a sum over every basis state other than
$\vert n,\alpha\rangle$ itself — and that includes the $d-1$ partners
$\vert n,\beta\rangle$, $\beta\neq\alpha$, in the *same* manifold. For each of
those,

$$
E_n-E_m=E_n-E_n=0,
$$

so the coefficient is $V_{n\beta,n\alpha}/0$. Unless every off-diagonal
in-manifold matrix element $V_{n\beta,n\alpha}$ happens to vanish — which a
generic perturbation does not arrange — the correction diverges. The same zero
denominator reappears in the second-order energy
$\sum_{m\neq n}\vert V_{mn}\vert^2/(E_n-E_m)$.

The hidden assumption is about *labeling*. Non-degenerate perturbation theory
assumes each unperturbed eigenstate is uniquely picked out by its energy, so
that as $\lambda\to0$ the perturbed state $\vert n(\lambda)\rangle$ has one and
only one limit, namely $\vert n\rangle$. For a degenerate level this is false:
the energy $E_n$ does *not* single out a state, only a $d$-dimensional
subspace, and any orthonormal basis of that subspace is an equally legal
choice — the basis is fixed only up to a $U(d)$ rotation. The perturbation
$\hat V$ generally selects a *particular* basis as the $\lambda\to0$ limit of
the exact eigenstates, and a generic starting basis is not it. Feeding the
wrong basis into a formula that presumes the right one is what produces the
$0/0$. The minimal fix is to first diagonalize $\hat V$ inside the manifold; in
that basis the dangerous numerators $V_{n\beta,n\alpha}$ ($\beta\neq\alpha$)
vanish and the indeterminate terms drop out, while the intra-manifold mixing is
fixed by the diagonalization itself rather than by the divergent ratio.

<!-- ─── -->

**2. Block first, levels later.** For a degenerate manifold with basis $\{\vert n,\alpha\rangle\}_{\alpha=1}^d$, define
$W^{(n)}_{\alpha\beta}=\langle n,\alpha\vert\hat V\vert n,\beta\rangle$.

(a) Show that first-order shifts are eigenvalues of $W^{(n)}$.

(b) Show that eigenvectors of $W^{(n)}$ define the good zeroth-order basis.

(c) Explain why this removes the divergence problem before applying higher-order corrections.

**Solution.**

Work with the in-manifold energy matrix $E_{n,\alpha\beta}(\lambda)$, whose
eigenvalues are the physical energies that grow out of the manifold under
$\hat H(\lambda)=\hat H_0+\lambda\hat V$.

**(a)** The first (degenerate) Hellmann-Feynman identity, evaluated at
$\lambda=0$, gives

$$
\partial_\lambda E_{n,\alpha\beta}\big\vert_{\lambda=0}
=\langle n,\alpha\vert\hat V\vert n,\beta\rangle=W^{(n)}_{\alpha\beta}.
$$

Hence to first order

$$
E_{n,\alpha\beta}(\lambda)=E_n\,\delta_{\alpha\beta}+\lambda\,W^{(n)}_{\alpha\beta}+O(\lambda^2).
$$

The first term is $E_n$ times the $d\times d$ identity; it commutes with
everything and merely shifts all eigenvalues by $E_n$. The physical energies
are the eigenvalues of the full matrix, so they are $E_n+\lambda w_a+O(\lambda^2)$,
where $w_1,\dots,w_d$ are the eigenvalues of the Hermitian matrix $W^{(n)}$.
The first-order shifts $E^{(1)}_{n,a}=w_a$ are exactly the eigenvalues of
$W^{(n)}$. Because $W^{(n)}$ is Hermitian its eigenvalues are real, as energy
shifts must be.

**(b)** The "good" zeroth-order basis is the basis of unperturbed states that
the exact perturbed eigenstates $\vert n,a(\lambda)\rangle$ actually reduce to
as $\lambda\to0$. Diagonalize $W^{(n)}$,

$$
W^{(n)}\vert n,a\rangle=w_a\,\vert n,a\rangle,
$$

and adopt $\{\vert n,a\rangle\}$ as the manifold basis. In this basis the
effective block is $E_n\hat I_d+\lambda\,\mathrm{diag}(w_1,\dots,w_d)+O(\lambda^2)$ —
already diagonal at order $\lambda$. Its eigenvectors are the fixed vectors
$\vert n,a\rangle$, independent of $\lambda$ to leading order, so each perturbed
eigenstate emerges continuously from one definite $\vert n,a\rangle$. Any other
choice is a $U(d)$ rotation $\vert n,\alpha\rangle=\sum_a U_{a\alpha}\vert n,a\rangle$
of this one; in a rotated basis the order-$\lambda$ block is *not* diagonal,
and to diagonalize it one needs an order-$1$ (not small) rotation even though
the perturbation is infinitesimal. A basis that requires a discontinuous jump
to track the eigenstates cannot be a valid zeroth-order limit. Only the
eigenbasis of $W^{(n)}$ connects smoothly, so it is the good basis — provided
the eigenvalues $w_a$ are distinct (the degenerate case is Problem 5).

**(c)** In the good basis $W^{(n)}$ is diagonal, $V_{na,nb}=w_a\,\delta_{ab}$,
so every *off-diagonal in-manifold* matrix element vanishes. These off-diagonal
elements are precisely the numerators that sat over the zero denominator
$E_n-E_n$ in Problem 1. With the numerator forced to zero, the indeterminate
$0/0$ becomes a plain absent term: the higher-order sums need only run over
states $m$ in *other* manifolds, where $E_n-E_m\neq0$ and every contribution is
finite. Diagonalizing $W^{(n)}$ *before* touching any higher-order correction
is what guarantees this — it resolves all intra-manifold mixing in advance,
leaving second-order perturbation theory only the well-behaved cross-manifold
transitions. Applying a higher-order formula in a generic basis would leave the
divergence in place, so the block diagonalization must come first.

<!-- ─── -->

**3. Effective Hamiltonian and dark state.** Consider a three-level system with $\hat H_0=\Delta\,\vert 3\rangle\langle 3\vert$ ($\Delta>0$), so the ground manifold $\{\vert 1\rangle,\vert 2\rangle\}$ is doubly degenerate at $E=0$. Add

$$
\hat V=\mu\,(\vert 1\rangle\langle 2\vert+\vert 2\rangle\langle 1\vert)+\lambda\,(\vert 3\rangle\langle 1\vert+\vert 3\rangle\langle 2\vert+\mathrm{h.c.}),
$$

with real $\mu,\lambda$ and $\vert\mu\vert,\vert\lambda\vert\ll\Delta$.

(a) Compute $\hat P_d\hat V\hat P_d$ in $\{\vert 1\rangle,\vert 2\rangle\}$, where $\hat P_d$ projects onto the degenerate subspace. Read off the first-order splitting.

(b) Set $\mu=0$. Build the second-order effective Hamiltonian $\hat H^{(2)}_{\mathrm{eff}}$ in $\{\vert 1\rangle,\vert 2\rangle\}$ from virtual transitions through $\vert 3\rangle$. Diagonalize and identify the bright state with shift $-2\lambda^2/\Delta$ and the dark state with zero shift.

(c) Still with $\mu=0$, show that the dark state is an *exact* zero-energy eigenstate of $\hat H_0+\hat V$ (not only at second order), and explain in one sentence why.

(d) Restore $\mu\ne 0$. Show that for the symmetric coupling here (equal $\vert 3\rangle\langle 1\vert$ and $\vert 3\rangle\langle 2\vert$ matrix elements), $\hat P_d\hat V\hat P_d=\mu\hat X$ and the second-order rank-1 matrix $\propto\begin{pmatrix}1&1\\1&1\end{pmatrix}$ commute, so the two splittings share an eigenbasis and combine independently. Write the two ground-manifold energies to order $\mu+\lambda^2$.

**Solution.**

**(a)** The projector onto the degenerate manifold is
$\hat P_d=\vert1\rangle\langle1\vert+\vert2\rangle\langle2\vert$. Split $\hat V$
into its two pieces. The $\lambda$ piece,
$\lambda(\vert3\rangle\langle1\vert+\vert3\rangle\langle2\vert+\mathrm{h.c.})$,
always has one leg on $\vert3\rangle$; sandwiched between two $\hat P_d$ it gives
zero because $\hat P_d\vert3\rangle=0$. Only the $\mu$ piece survives:

$$
\hat P_d\hat V\hat P_d=\mu\,(\vert1\rangle\langle2\vert+\vert2\rangle\langle1\vert)
\simeq\mu\begin{pmatrix}0&1\\1&0\end{pmatrix}=\mu\hat X,
$$

in the ordered basis $(\vert1\rangle,\vert2\rangle)$. Its eigenvalues are
$\pm\mu$, with eigenvectors $\vert\pm\rangle=(\vert1\rangle\pm\vert2\rangle)/\sqrt2$.
The first-order energies in the manifold are therefore $E^{(1)}_\pm=\pm\mu$:
the degeneracy is lifted already at first order, with splitting $2\mu$, and the
first-order good basis is $\{\vert+\rangle,\vert-\rangle\}$.

**(b)** Set $\mu=0$, so
$\hat V=\lambda(\vert3\rangle\langle1\vert+\vert3\rangle\langle2\vert+\vert1\rangle\langle3\vert+\vert2\rangle\langle3\vert)$.
The first-order block $\hat P_d\hat V\hat P_d$ now vanishes entirely, so any
splitting is a second-order effect. The only state outside the manifold is
$\vert3\rangle$ at energy $\Delta$, so for $i,j\in\{1,2\}$

$$
(H^{(2)}_{\mathrm{eff}})_{ij}
=\sum_{m\notin d}\frac{\langle i\vert\hat V\vert m\rangle\langle m\vert\hat V\vert j\rangle}{E_d-E_m}
=-\frac{1}{\Delta}\langle i\vert\hat V\vert3\rangle\langle3\vert\hat V\vert j\rangle.
$$

Every coupling matrix element is the same: $\langle i\vert\hat V\vert3\rangle=\lambda$
and $\langle3\vert\hat V\vert j\rangle=\lambda$ for $i,j\in\{1,2\}$. Hence all
four entries equal $-\lambda^2/\Delta$:

$$
\hat H^{(2)}_{\mathrm{eff}}=-\frac{\lambda^2}{\Delta}\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

The matrix $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is rank one, with eigenvalue
$2$ (eigenvector $\vert+\rangle=(\vert1\rangle+\vert2\rangle)/\sqrt2$) and
eigenvalue $0$ (eigenvector $\vert-\rangle=(\vert1\rangle-\vert2\rangle)/\sqrt2$).
Therefore

$$
\hat H^{(2)}_{\mathrm{eff}}\vert+\rangle=-\frac{2\lambda^2}{\Delta}\vert+\rangle,
\qquad
\hat H^{(2)}_{\mathrm{eff}}\vert-\rangle=0.
$$

The **bright state** is $\vert B\rangle=\vert+\rangle=(\vert1\rangle+\vert2\rangle)/\sqrt2$,
with second-order shift $-2\lambda^2/\Delta$; the **dark state** is
$\vert D\rangle=\vert-\rangle=(\vert1\rangle-\vert2\rangle)/\sqrt2$, with zero
shift.

**(c)** Still $\mu=0$. Check $\vert D\rangle=(\vert1\rangle-\vert2\rangle)/\sqrt2$
against $\hat H_0+\hat V$ directly.

For $\hat H_0$: $\hat H_0\vert D\rangle=\Delta\vert3\rangle\langle3\vert D\rangle=0$,
since $\vert D\rangle$ has no $\vert3\rangle$ component.

For $\hat V$, group the terms by which bra they carry:

$$
\hat V=\lambda\,\vert3\rangle(\langle1\vert+\langle2\vert)+\lambda\,(\vert1\rangle+\vert2\rangle)\langle3\vert.
$$

Acting on $\vert D\rangle$: the second term gives
$\lambda(\vert1\rangle+\vert2\rangle)\langle3\vert D\rangle=0$ because
$\langle3\vert D\rangle=0$; the first term gives

$$
\lambda\,\vert3\rangle(\langle1\vert+\langle2\vert)\frac{\vert1\rangle-\vert2\rangle}{\sqrt2}
=\lambda\,\vert3\rangle\,\frac{1-1}{\sqrt2}=0.
$$

So $\hat V\vert D\rangle=0$ and $(\hat H_0+\hat V)\vert D\rangle=0$ — exactly,
for any $\lambda$, not merely at second order. In one sentence: the
perturbation couples $\vert3\rangle$ only to the *symmetric* combination
$\vert1\rangle+\vert2\rangle$, so the antisymmetric $\vert D\rangle$ lies in the
kernel of $\hat V$ (the two coupling paths $3\to1$ and $3\to2$ interfere
destructively) and stays decoupled from $\vert3\rangle$ to all orders.

**(d)** Restore $\mu\neq0$. From (a), $\hat P_d\hat V\hat P_d=\mu\hat X$. From
(b), the second-order matrix is $-\tfrac{\lambda^2}{\Delta}M$ with
$M=\begin{pmatrix}1&1\\1&1\end{pmatrix}=\hat I+\hat X$. They commute:

$$
\Big[\mu\hat X,\;-\tfrac{\lambda^2}{\Delta}(\hat I+\hat X)\Big]
=-\tfrac{\mu\lambda^2}{\Delta}\big([\hat X,\hat I]+[\hat X,\hat X]\big)=0.
$$

Commuting Hermitian matrices share an eigenbasis — here
$\{\vert+\rangle,\vert-\rangle\}$, the eigenbasis of $\hat X$, which also
diagonalizes $M$ ($M\vert+\rangle=2\vert+\rangle$, $M\vert-\rangle=0$). So the
first-order ($\mu$) and second-order ($\lambda^2$) contributions add
independently on each of $\vert+\rangle,\vert-\rangle$. The two ground-manifold
energies, kept to first order in $\mu$ and second order in $\lambda$, are

$$
E_B=E_+=+\mu-\frac{2\lambda^2}{\Delta},
\qquad
E_D=E_-=-\mu.
$$

The bright state $\vert B\rangle=\vert+\rangle$ collects the $+\mu$ first-order
shift *and* the $-2\lambda^2/\Delta$ second-order shift; the dark state
$\vert D\rangle=\vert-\rangle$ collects only the $-\mu$ first-order shift and
stays dark ($0$ at second order). In fact $\vert D\rangle$ remains an *exact*
eigenstate even for $\mu\neq0$: $\hat H_0\vert D\rangle=0$, the $\lambda$ part
of $\hat V$ still annihilates it as in (c), and the $\mu$ part gives
$\mu\hat X\vert D\rangle=-\mu\vert D\rangle$, so $(\hat H_0+\hat V)\vert D\rangle=-\mu\vert D\rangle$
with $E_D=-\mu$ holding to all orders.

<!-- ─── -->

**4. Hydrogen Stark splitting.** In hydrogen (ignoring spin), use basis
$\{\vert 2,0,0\rangle,\vert 2,1,0\rangle,\vert 2,1,1\rangle,\vert 2,1,-1\rangle\}$ and
$\hat V=e\mathcal E_0\hat{z}$.

(a) Use selection rules $\Delta\ell=\pm1$, $\Delta m=0$ to write the effective matrix structure.

(b) Explain why two states split linearly while two remain unsplit at first order.

(c) State the symmetry reason in one sentence.

**Solution.**

**(a)** The perturbation $\hat V=e\mathcal E_0\hat{z}$ is built from $\hat{z}$, a
parity-odd, rank-one spherical tensor with zero $m$-component, so
$\langle n\ell m\vert\hat{z}\vert n\ell'm'\rangle$ is nonzero only when
$\ell'=\ell\pm1$ and $m'=m$. Scan the $n=2$ basis
$(\vert200\rangle,\vert210\rangle,\vert211\rangle,\vert21,-1\rangle)$:

- $\vert200\rangle$ ($\ell=0,m=0$) couples to $\vert210\rangle$ ($\ell=1,m=0$): $\Delta\ell=+1$, $\Delta m=0$ — allowed.
- $\vert211\rangle$ ($m=1$) and $\vert21,-1\rangle$ ($m=-1$) would each need a same-$m$ partner with $\ell$ shifted by one; the $n=2$ shell has no $\ell=0$ or $\ell=2$ state at $m=\pm1$, so neither couples to anything.
- Diagonal elements vanish: $\langle2\ell m\vert\hat{z}\vert2\ell m\rangle=0$ because a state of definite $\ell$ has definite parity while $\hat{z}$ is parity-odd.

So in the basis order above

$$
W=e\mathcal E_0\begin{pmatrix}0&z_0&0&0\\ z_0&0&0&0\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix},
\qquad z_0=\langle200\vert\hat{z}\vert210\rangle=-3a_0,
$$

with $a_0$ the Bohr radius. The matrix is a single $2\times2$ off-diagonal
block in $\{\vert200\rangle,\vert210\rangle\}$ plus a $2\times2$ zero block in
$\{\vert211\rangle,\vert21,-1\rangle\}$.

**(b)** The $2\times2$ block $\begin{pmatrix}0&w\\w&0\end{pmatrix}$ with
$w=-3ea_0\mathcal E_0$ has eigenvalues $\pm\vert w\vert=\pm3ea_0\mathcal E_0$
and eigenvectors $(\vert200\rangle\pm\vert210\rangle)/\sqrt2$. These two states
acquire energy shifts $\pm3ea_0\mathcal E_0$, *linear* in the field — the
linear Stark effect. The states $\vert211\rangle$ and $\vert21,-1\rangle$ lie in
the zero block; $W$ gives them no first-order shift, so they stay degenerate at
first order. Their response is quadratic, $O(\mathcal E_0^2)$, arising only
from second-order virtual coupling to states in other $n$ shells.

**(c)** In one sentence: $\hat{z}$ is odd under parity and conserves $m$, so
within the $n=2$ shell it can connect only the opposite-parity, equal-$m$ pair
$\vert200\rangle\leftrightarrow\vert210\rangle$ — the accidental
$\ell$-degeneracy of hydrogen places states of both parities at the same
energy, which is what permits a first-order (linear) effect — whereas
$\vert211\rangle$ and $\vert21,-1\rangle$ have no opposite-parity partner at the
same $m$ in the shell and so cannot be split until second order.

<!-- ─── -->

**5. Residual degeneracy.** For
$\hat H_{\text{eff}}=\begin{pmatrix}a&b\\b^*&c\end{pmatrix}$:

(a) find eigenvalues,

(b) give the condition for no first-order splitting,

(c) explain what physical information must then be checked at second order (or via symmetry).

**Solution.**

**(a)** For $\hat H_{\text{eff}}=\begin{pmatrix}a&b\\b^*&c\end{pmatrix}$
(Hermitian, so $a,c$ real), the characteristic equation is
$(a-E)(c-E)-\vert b\vert^2=0$, i.e. $E^2-(a+c)E+(ac-\vert b\vert^2)=0$. Hence

$$
E_\pm=\frac{a+c}{2}\pm\sqrt{\left(\frac{a-c}{2}\right)^2+\vert b\vert^2}.
$$

**(b)** The first-order splitting is
$E_+-E_-=2\sqrt{\left(\tfrac{a-c}{2}\right)^2+\vert b\vert^2}$. It vanishes only
when the square root is zero, and since both terms under it are non-negative,
that requires *both*

$$
a=c\qquad\text{and}\qquad b=0,
$$

i.e. $\hat H_{\text{eff}}=a\,\hat I$ is a multiple of the identity. Then the
manifold stays degenerate: first-order perturbation theory produces no
splitting at all.

**(c)** When $\hat H^{(1)}_{\text{eff}}\propto\hat I$, the first-order matrix is
itself degenerate and carries no information — every basis diagonalizes it, so
it can pick out neither a good basis nor a splitting. One must build the
*second-order* effective Hamiltonian, the matrix of virtual excursions to
states outside the manifold,

$$
(H^{(2)}_{\text{eff}})_{\alpha\beta}
=\sum_{m\notin d}\frac{\langle\alpha\vert\hat V\vert m\rangle\langle m\vert\hat V\vert\beta\rangle}{E_d-E_m},
$$

and diagonalize *that*; its eigenvalues are the second-order shifts and its
eigenvectors the good basis. If the second-order matrix lifts the degeneracy,
that resolves it. If it too is $\propto\hat I$, the exact degeneracy is not an
accident of low order but is enforced by a symmetry: one should then identify
the conserved quantity or group representation responsible — a multidimensional
irreducible representation of a (possibly non-abelian) symmetry group, or a
Kramers doublet protected by time-reversal — since in that case no finite order
of perturbation theory will split it.

<!-- ─── -->

**6. When to switch methods.** For each Hamiltonian below, decide whether non-degenerate or degenerate perturbation theory is appropriate at first order, and justify in one sentence:

(a) Hydrogen $n=2$ manifold in a small uniform electric field $\mathcal E\hat{z}$.

(b) The $n=1$ ground state of hydrogen in the same field.

(c) Two bands with gap $\gg V$ and $V$ mixing across the gap.

(d) Two nearly-degenerate bands with gap $\ll V$.

**Solution.**

**(a) Degenerate** perturbation theory. The hydrogen $n=2$ level is four-fold
degenerate (ignoring spin), and $\hat V=e\mathcal E z$ has a nonzero matrix
element *inside* the manifold, $\langle200\vert z\vert210\rangle\neq0$, so the
in-manifold block must be diagonalized first — this is the linear Stark effect.

**(b) Non-degenerate** perturbation theory. The $n=1$ ground state is a single
non-degenerate level (ignoring spin), so the ordinary expansion applies; parity
forces $\langle100\vert z\vert100\rangle=0$, so the shift is purely
second-order (the quadratic Stark effect).

**(c) Non-degenerate** perturbation theory. With the gap much larger than the
coupling, $V/\text{gap}\ll1$, so the coupling-over-gap expansion converges and
the cross-gap mixing is a small, controlled correction.

**(d) Degenerate** (quasi-degenerate) perturbation theory. With gap $\ll V$ the
two bands form a near-degenerate manifold; the coupling-over-gap ratio is
large, so one must diagonalize $V$ *exactly* within the $2\times2$
near-degenerate block (treating the small gap as an in-block term) and only
then perturb in the coupling to remote bands.

<!-- ─── -->

**7. Flux ring with cosine perturbation.** Recall the flux ring of §4.2.3: a particle on a ring of radius $R$ threaded by flux $\Phi$ has angular-momentum eigenstates $\vert n\rangle$ with wavefunctions $\psi_n(\theta) = \mathrm{e}^{\mathrm{i}n\theta}/\sqrt{2\pi}$, $n \in \mathbb{Z}$, and energies

$$
E_n(\Phi) = E_0\,(n - \varphi)^{2}, \qquad E_0 = \frac{\hbar^{2}}{2mR^{2}}, \qquad \varphi = \Phi/\Phi_0.
$$

Add a static azimuthal potential

$$
\hat V = V_0\cos\theta, \qquad V_0 \ll E_0.
$$

At $\varphi = 1/2$ the two lowest branches $\vert 0\rangle$ and $\vert 1\rangle$ cross at $E_0(1/2) = E_1(1/2) = E_0/4$ — a two-fold degeneracy that the perturbation may lift.

**Scope.** Treat only the degenerate doublet $\{\vert 0\rangle,\vert 1\rangle\}$ at first order in $V_0$. The next-nearest unperturbed levels at this flux are $\vert -1\rangle$ and $\vert 2\rangle$ with $E_{-1}(1/2) = E_2(1/2) = 9E_0/4$ — separated from the doublet by a gap of $2E_0 \gg V_0$. They couple to the doublet through $\hat V$ but only via virtual excursions that contribute at order $V_0^{2}/E_0$, which is smaller than the first-order shift $V_0$ by the small ratio $V_0/E_0 \ll 1$; ignore them.

(a) Compute the matrix elements $\langle n\vert\cos\theta\vert m\rangle$ in the angular-momentum basis. Show that $\hat V$ couples only **nearest neighbours** $n \leftrightarrow n \pm 1$, and identify the value of the coupling.

(b) At $\varphi = 1/2$, build the $2 \times 2$ effective Hamiltonian $\hat H_\text{eff}$ for the doublet at first order in $\hat V$ and write it in the form $\hat H_\text{eff} = (\text{const})\,\hat I + (\text{coupling})\,\hat\sigma^{x}$.

(c) Diagonalise $\hat H_\text{eff}$ to obtain the first-order energy shifts and the gap $\Delta E$ that opens at the crossing. Identify the **good zeroth-order basis** — the symmetric and antisymmetric combinations of $\vert 0\rangle$ and $\vert 1\rangle$ — and write the corresponding probability densities $\vert\psi_{\pm}(\theta)\vert^{2}$.

(d) Slightly off the crossing, set $\varphi = 1/2 + \delta$ with $\vert\delta\vert$ small. Build the $2 \times 2$ matrix at general $\delta$ (within the same doublet truncation) and find the perturbed energies $E_{\pm}(\delta)$. Describe in words the shape of $E_{\pm}(\varphi)$ near $\varphi = 1/2$ — the **avoided crossing**.

(e) **Generic flux: non-degenerate perturbation theory.** Move away from the crossing. For $\vert\varphi\vert < 1/2$ the ground state is the non-degenerate angular-momentum state $\vert 0\rangle$ with energy $E_0(\varphi) = E_0\varphi^{2}$. Apply the second-order non-degenerate perturbation formula

$$
E_n(\varphi) = E_n^{(0)}(\varphi) + \langle n\vert\hat V\vert n\rangle + \sum_{m\neq n}\frac{\vert\langle m\vert\hat V\vert n\rangle\vert^{2}}{E_n^{(0)}(\varphi) - E_m^{(0)}(\varphi)} + \mathcal{O}(V_0^{3})
$$

to compute the perturbed ground-state energy $E_0(\varphi)$ through order $V_0^{2}$. Show that the expression diverges at $\varphi = \pm 1/2$, recovering the breakdown signalled by the doublet treatment in (b)–(c).

**Solution.**

**(a)** Matrix element of $\cos\theta$ in the plane-wave basis:

$$
\langle n\vert\cos\theta\vert m\rangle = \frac{1}{2\pi}\int_0^{2\pi}\cos\theta\,\mathrm{e}^{\mathrm{i}(m-n)\theta}\,\mathrm{d}\theta.
$$

Using $\cos\theta = \tfrac{1}{2}(\mathrm{e}^{\mathrm{i}\theta} + \mathrm{e}^{-\mathrm{i}\theta})$,

$$
\langle n\vert\cos\theta\vert m\rangle = \frac{1}{4\pi}\int_0^{2\pi}\!\!\bigl(\mathrm{e}^{\mathrm{i}(m-n+1)\theta} + \mathrm{e}^{\mathrm{i}(m-n-1)\theta}\bigr)\mathrm{d}\theta = \tfrac{1}{2}\,(\delta_{n,m+1} + \delta_{n,m-1}).
$$

So $\langle n\vert\cos\theta\vert m\rangle = 1/2$ when $\vert n - m\vert = 1$, and zero otherwise: $\hat V = V_0\cos\theta$ couples each angular-momentum eigenstate only to its **nearest neighbours** $\vert n\pm 1\rangle$, with matrix element $V_0/2$.

**(b)** Within the doublet $\{\vert 0\rangle,\vert 1\rangle\}$ at $\varphi = 1/2$, the unperturbed Hamiltonian is just $(E_0/4)\hat I$. The perturbation block is

$$
W = V_0\begin{pmatrix} \langle 0\vert\cos\theta\vert 0\rangle & \langle 0\vert\cos\theta\vert 1\rangle \\ \langle 1\vert\cos\theta\vert 0\rangle & \langle 1\vert\cos\theta\vert 1\rangle\end{pmatrix} = \frac{V_0}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} = \frac{V_0}{2}\hat\sigma^{x},
$$

using $\langle 0\vert\cos\theta\vert 1\rangle = 1/2$ from (a) and zero diagonal entries. The first-order effective Hamiltonian on the doublet is therefore

$$
\hat H_\text{eff} = \frac{E_0}{4}\hat I + \frac{V_0}{2}\hat\sigma^{x}.
$$

**(c)** The $\hat\sigma^{x}$ block has eigenvalues $\pm 1$ with eigenstates $\vert\pm\rangle = (\vert 0\rangle \pm \vert 1\rangle)/\sqrt 2$. So

$$
E_\pm = \frac{E_0}{4} \pm \frac{V_0}{2},
\qquad
\Delta E = E_+ - E_- = V_0,
$$

the gap that the perturbation opens at the crossing. The **good zeroth-order basis** is the pair of symmetric / antisymmetric combinations,

$$
\vert +\rangle = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt 2},\qquad \vert -\rangle = \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt 2},
$$

which diagonalise $\hat V$ on the doublet and emerge continuously from the perturbed eigenstates as $V_0 \to 0$. Their real-space wavefunctions are $\psi_\pm(\theta) = (1 \pm \mathrm{e}^{\mathrm{i}\theta})/\sqrt{4\pi}$, with probability densities

$$
\vert\psi_+(\theta)\vert^{2} = \frac{1 + \cos\theta}{2\pi}\quad(\text{peaked at }\theta = 0),
\qquad
\vert\psi_-(\theta)\vert^{2} = \frac{1 - \cos\theta}{2\pi}\quad(\text{peaked at }\theta = \pi).
$$

The two eigenstates are *standing waves* localised at opposite sides of the ring: $\vert +\rangle$ at $\theta = 0$ where $\cos\theta$ is maximal (so $\hat V$ is most repulsive, raising its energy), and $\vert -\rangle$ at $\theta = \pi$ where $\cos\theta$ is minimal (lowering its energy). The first-order shifts $\pm V_0/2$ are exactly the matrix-element-weighted overlap of these standing waves with the potential.

**(d)** Set $\varphi = 1/2 + \delta$ and expand the diagonal energies:

$$
E_0(\varphi) = E_0\varphi^{2} = E_0\bigl(\tfrac{1}{4} + \delta + \delta^{2}\bigr),
\qquad
E_1(\varphi) = E_0(1-\varphi)^{2} = E_0\bigl(\tfrac{1}{4} - \delta + \delta^{2}\bigr).
$$

The $2 \times 2$ matrix in the doublet basis (still truncating to these two levels) is

$$
\hat H_{2\times 2}(\delta) = \begin{pmatrix} E_0(1/4 + \delta + \delta^{2}) & V_0/2 \\ V_0/2 & E_0(1/4 - \delta + \delta^{2})\end{pmatrix}
= \bigl[\tfrac{E_0}{4} + E_0\delta^{2}\bigr]\hat I + E_0\delta\,\hat\sigma^{z} + \frac{V_0}{2}\hat\sigma^{x}.
$$

For small $\vert\delta\vert$ the $E_0\delta^{2}$ shift is negligible. The eigenvalues are

$$
E_\pm(\delta) = \frac{E_0}{4} \pm \sqrt{(E_0\delta)^{2} + (V_0/2)^{2}}.
$$

This is the standard **avoided-crossing** profile:

- At $\delta = 0$: the gap is exactly $\Delta E = V_0$, with eigenstates $\vert\pm\rangle$ from (c).
- For $\vert E_0\delta\vert \gg V_0/2$: $E_\pm \approx E_0/4 \pm E_0\vert\delta\vert$ — the unperturbed linear branches $E_0(\varphi) = E_0(1/4 + \delta)$ and $E_1(\varphi) = E_0(1/4 - \delta)$, with eigenstates approaching $\vert 0\rangle$ and $\vert 1\rangle$.

In the $(\varphi, E)$ plane, what would have been a sharp X-shaped crossing of the two linear unperturbed branches at $\varphi = 1/2$ has been rounded into a **hyperbolic anti-crossing** with minimum gap $V_0$ at the centre. The perturbation has lifted the degeneracy and replaced level crossing by level repulsion — the same mechanism that opens **band gaps** in periodic potentials at the boundary of every Brillouin zone.

**(e) Generic flux: non-degenerate perturbation theory.** For $\vert\varphi\vert < 1/2$ the diagonal element vanishes by the selection rule of (a), $\langle 0\vert\hat V\vert 0\rangle = 0$, so $E_0^{(1)}(\varphi) = 0$. The second-order sum is restricted to $m = \pm 1$ by the same rule, with $\vert\langle\pm 1\vert\hat V\vert 0\rangle\vert^{2} = V_0^{2}/4$. The unperturbed gaps are

$$
E_0^{(0)}(\varphi) - E_{+1}^{(0)}(\varphi) = E_0\bigl[\varphi^{2} - (1 - \varphi)^{2}\bigr] = E_0(2\varphi - 1),
$$

$$
E_0^{(0)}(\varphi) - E_{-1}^{(0)}(\varphi) = E_0\bigl[\varphi^{2} - (-1 - \varphi)^{2}\bigr] = -E_0(2\varphi + 1).
$$

Hence

$$
\begin{split}
E_0(\varphi) &= E_0\varphi^{2} + \frac{V_0^{2}}{4}\left[\frac{1}{E_0(2\varphi - 1)} + \frac{1}{-E_0(2\varphi + 1)}\right] + \mathcal{O}(V_0^{3})\\
&= E_0\varphi^{2} + \frac{V_0^{2}}{4 E_0}\cdot\frac{(2\varphi + 1) - (2\varphi - 1)}{(2\varphi - 1)(2\varphi + 1)} + \mathcal{O}(V_0^{3})\\
&= E_0\varphi^{2} - \frac{V_0^{2}}{2 E_0\,(1 - 4\varphi^{2})} + \mathcal{O}(V_0^{3}).
\end{split}
$$

The second-order shift is finite throughout the open interval $\vert\varphi\vert < 1/2$ and is *negative* — the bottom branch always bends down under a perturbation that couples it only to higher levels (each term in the sum carries a negative denominator).

**Breakdown at $\varphi = \pm 1/2$.** The factor $1 - 4\varphi^{2}$ vanishes there, and the non-degenerate formula diverges. This divergence is not a calculational mistake but a *signal* that the basic premise — non-degenerate level $\vert 0\rangle$ with all other levels well separated — fails: at $\varphi = +1/2$ the level $\vert 0\rangle$ becomes degenerate with $\vert 1\rangle$, and at $\varphi = -1/2$ with $\vert -1\rangle$. The first-order matrix element $V_0/2$ between $\vert 0\rangle$ and its degenerate partner can no longer be treated as a small denominator-suppressed correction; one must instead diagonalise it exactly within the degenerate doublet, exactly as in (b)–(c).

**Order-of-magnitude contrast.** Away from the crossing, the perturbative shift is of order $V_0^{2}/E_0$ — quadratic in the perturbation strength and suppressed by the (open) gap. At the crossing the splitting is of order $V_0$ — *linear* in the perturbation strength. This promotion from $\mathcal{O}(V_0^{2}/E_0)$ to $\mathcal{O}(V_0)$ is the qualitative fingerprint of degeneracy lifting and explains why states near a level crossing respond so much more strongly to small perturbations than states far from any crossing — a phenomenon that underlies, for example, the giant susceptibility of materials near quantum critical points and the high responsivity of qubits operated at sweet-spot flux degeneracies.
