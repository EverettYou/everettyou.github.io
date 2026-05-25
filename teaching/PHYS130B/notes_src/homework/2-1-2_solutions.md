# 2.1.2 Symmetrization
Worked solutions for the homework problems in the [2.1.2 Symmetrization](../ch2_identical-particles/2-1-2-symmetrization) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Three-particle statistics.** For three identical particles, consider the transpositions $\hat{\mathcal{P}}_{12}, \hat{\mathcal{P}}_{23}, \hat{\mathcal{P}}_{13}$.

(a) Verify the braid-like relation $\hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12} = \hat{\mathcal{P}}_{13}$ by acting on a generic tensor basis state $\vert\alpha\rangle\otimes\vert\beta\rangle\otimes\vert\gamma\rangle$.

(b) Suppose a three-particle state $\vert\Psi\rangle$ is a simultaneous eigenstate of every transposition, $\hat{\mathcal{P}}_{ij}\vert\Psi\rangle = \lambda_{ij}\vert\Psi\rangle$ with $\lambda_{ij} \in \{\pm 1\}$. Use the identity in (a) to show that $\lambda_{13} = \lambda_{23}$, and analogous relations to conclude $\lambda_{12} = \lambda_{23} = \lambda_{13}$.

(c) Conclude that the only consistent exchange statistics for three or more identical particles in three dimensions are bosonic ($\lambda = +1$) or fermionic ($\lambda = -1$)—there is no third option.

**Solution.**

(a) The transposition $\hat{\mathcal{P}}_{ij}$ exchanges the contents of tensor slots $i$ and $j$. Apply the three factors of $\hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12}$ to $\vert\alpha\beta\gamma\rangle$, working right to left:

$$
\vert\alpha\beta\gamma\rangle
\xrightarrow{\ \hat{\mathcal{P}}_{12}\ } \vert\beta\alpha\gamma\rangle
\xrightarrow{\ \hat{\mathcal{P}}_{23}\ } \vert\beta\gamma\alpha\rangle
\xrightarrow{\ \hat{\mathcal{P}}_{12}\ } \vert\gamma\beta\alpha\rangle.
$$

The end result $\vert\gamma\beta\alpha\rangle$ has slots $1$ and $3$ interchanged relative to the start, which is exactly $\hat{\mathcal{P}}_{13}\vert\alpha\beta\gamma\rangle = \vert\gamma\beta\alpha\rangle$. Since the basis states $\vert\alpha\rangle\otimes\vert\beta\rangle\otimes\vert\gamma\rangle$ span the three-particle space and both sides are linear operators, agreement on every basis state is agreement as operators:

$$
\hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12} = \hat{\mathcal{P}}_{13}.
$$

(b) Let $\vert\Psi\rangle\neq 0$ be a simultaneous eigenstate, $\hat{\mathcal{P}}_{ij}\vert\Psi\rangle = \lambda_{ij}\vert\Psi\rangle$. Act with the operator identity from (a) and peel off one factor at a time:

$$
\begin{split}
\hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12}\vert\Psi\rangle
&= \hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\,(\lambda_{12}\vert\Psi\rangle)\\
&= \hat{\mathcal{P}}_{12}\,(\lambda_{12}\lambda_{23}\vert\Psi\rangle)\\
&= \lambda_{12}^2\,\lambda_{23}\vert\Psi\rangle = \lambda_{23}\vert\Psi\rangle,
\end{split}
$$

where the last step uses $\lambda_{12}^2 = 1$ (each eigenvalue is $\pm1$ because $\hat{\mathcal{P}}_{ij}^2 = \hat{I}$). But the left side is also $\hat{\mathcal{P}}_{13}\vert\Psi\rangle = \lambda_{13}\vert\Psi\rangle$. Equating and cancelling the nonzero $\vert\Psi\rangle$,

$$
\lambda_{13} = \lambda_{23}.
$$

The same braid identity with relabelled indices, $\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23} = \hat{\mathcal{P}}_{13}$ (check on $\vert\alpha\beta\gamma\rangle$: $\vert\alpha\beta\gamma\rangle\to\vert\alpha\gamma\beta\rangle\to\vert\gamma\alpha\beta\rangle\to\vert\gamma\beta\alpha\rangle$), gives by the identical manipulation $\lambda_{23}^2\,\lambda_{12} = \lambda_{12} = \lambda_{13}$. Combining the two results,

$$
\lambda_{12} = \lambda_{13} = \lambda_{23} \equiv \lambda.
$$

All three transpositions must share **one common eigenvalue**. (This is no accident: in $S_3$ every transposition is conjugate to every other — e.g. $\hat{\mathcal{P}}_{13} = \hat{\mathcal{P}}_{12}\hat{\mathcal{P}}_{23}\hat{\mathcal{P}}_{12}^{-1}$ — and conjugate operators have equal eigenvalues on a common eigenstate.)

(c) Each $\hat{\mathcal{P}}_{ij}$ squares to the identity, so $\lambda^2 = 1$ and $\lambda \in \{+1, -1\}$ — there is no continuous or intermediate value. Part (b) forces this single $\lambda$ to be the *same* for every pair. Hence a physical state of three (or, by the same conjugacy argument, $N \ge 3$) identical particles is either

- totally **symmetric**, $\lambda = +1$ for all transpositions — **bosons**, or
- totally **antisymmetric**, $\lambda = -1$ for all transpositions — **fermions**.

No "mixed" assignment (some $+1$, some $-1$) and no third species survives: those are exactly the only two one-dimensional representations of the permutation group $S_N$. The clause "in three dimensions" is essential. The decisive input was $\hat{\mathcal{P}}_{ij}^2 = \hat{I}$ — exchanging two particles twice is the identity. In two dimensions, a double exchange is a closed loop that can wind, the exchange operators generate the *braid* group rather than $S_N$, and $\hat{\mathcal{P}}^2 \neq \hat{I}$ is allowed. That loophole admits **anyons** with $\lambda = \mathrm{e}^{\mathrm{i}\theta}$ for arbitrary $\theta$ (see §2.3.1); it is closed in 3D.

<!-- ─── -->

**2. Exchange projectors.** For two particles, define $\hat{\Sigma}_\pm = \tfrac{1}{2}(\hat{I} \pm \hat{\mathcal{P}}_{12})$. Show that $\hat{\Sigma}_\pm^2 = \hat{\Sigma}_\pm$, $\hat{\Sigma}_+ \hat{\Sigma}_- = 0$, and $\hat{\Sigma}_+ + \hat{\Sigma}_- = \hat{I}$, and verify that $\hat{\Sigma}_+\vert\Psi\rangle$ is symmetric and $\hat{\Sigma}_-\vert\Psi\rangle$ is antisymmetric under $\hat{\mathcal{P}}_{12}$. Conclude that every two-particle state decomposes uniquely as $\vert\Psi\rangle = \hat{\Sigma}_+\vert\Psi\rangle + \hat{\Sigma}_-\vert\Psi\rangle$.

**Solution.**

The single fact driving everything is $\hat{\mathcal{P}}_{12}^2 = \hat{I}$.

*Idempotence.* Expand the square, using $\hat{\mathcal{P}}_{12}^2 = \hat{I}$:

$$
\hat{\Sigma}_\pm^2 = \tfrac14(\hat{I} \pm \hat{\mathcal{P}}_{12})^2
= \tfrac14\big(\hat{I} \pm 2\hat{\mathcal{P}}_{12} + \hat{\mathcal{P}}_{12}^2\big)
= \tfrac14\big(2\hat{I} \pm 2\hat{\mathcal{P}}_{12}\big)
= \tfrac12(\hat{I} \pm \hat{\mathcal{P}}_{12}) = \hat{\Sigma}_\pm.
$$

*Orthogonality.* The cross terms cancel and $\hat{\mathcal{P}}_{12}^2 = \hat{I}$:

$$
\hat{\Sigma}_+\hat{\Sigma}_- = \tfrac14(\hat{I} + \hat{\mathcal{P}}_{12})(\hat{I} - \hat{\mathcal{P}}_{12})
= \tfrac14\big(\hat{I} - \hat{\mathcal{P}}_{12}^2\big) = \tfrac14(\hat{I} - \hat{I}) = 0.
$$

(The same computation with the factors reversed gives $\hat{\Sigma}_-\hat{\Sigma}_+ = 0$.)

*Completeness.* The $\hat{\mathcal{P}}_{12}$ terms cancel on addition:

$$
\hat{\Sigma}_+ + \hat{\Sigma}_- = \tfrac12(\hat{I} + \hat{\mathcal{P}}_{12}) + \tfrac12(\hat{I} - \hat{\mathcal{P}}_{12}) = \hat{I}.
$$

Idempotent, mutually orthogonal, and summing to $\hat{I}$: $\hat{\Sigma}_\pm$ are complementary projectors.

*Symmetry of the projected states.* Act with $\hat{\mathcal{P}}_{12}$ and again use $\hat{\mathcal{P}}_{12}^2 = \hat{I}$:

$$
\hat{\mathcal{P}}_{12}\,\hat{\Sigma}_+\vert\Psi\rangle
= \tfrac12\big(\hat{\mathcal{P}}_{12} + \hat{\mathcal{P}}_{12}^2\big)\vert\Psi\rangle
= \tfrac12\big(\hat{\mathcal{P}}_{12} + \hat{I}\big)\vert\Psi\rangle
= +\,\hat{\Sigma}_+\vert\Psi\rangle,
$$

$$
\hat{\mathcal{P}}_{12}\,\hat{\Sigma}_-\vert\Psi\rangle
= \tfrac12\big(\hat{\mathcal{P}}_{12} - \hat{\mathcal{P}}_{12}^2\big)\vert\Psi\rangle
= \tfrac12\big(\hat{\mathcal{P}}_{12} - \hat{I}\big)\vert\Psi\rangle
= -\,\hat{\Sigma}_-\vert\Psi\rangle.
$$

So $\hat{\Sigma}_+\vert\Psi\rangle$ is an eigenstate with eigenvalue $+1$ (symmetric) and $\hat{\Sigma}_-\vert\Psi\rangle$ with eigenvalue $-1$ (antisymmetric).

*Unique decomposition.* Completeness gives the decomposition immediately:

$$
\vert\Psi\rangle = \hat{I}\vert\Psi\rangle = (\hat{\Sigma}_+ + \hat{\Sigma}_-)\vert\Psi\rangle = \hat{\Sigma}_+\vert\Psi\rangle + \hat{\Sigma}_-\vert\Psi\rangle,
$$

a symmetric piece plus an antisymmetric piece. Uniqueness: suppose $\vert\Psi\rangle = \vert\psi_+\rangle + \vert\psi_-\rangle$ with $\hat{\mathcal{P}}_{12}\vert\psi_\pm\rangle = \pm\vert\psi_\pm\rangle$. Then $\hat{\Sigma}_+\vert\psi_+\rangle = \tfrac12(\hat I + \hat{\mathcal{P}}_{12})\vert\psi_+\rangle = \vert\psi_+\rangle$ and $\hat{\Sigma}_+\vert\psi_-\rangle = \tfrac12(\hat I + \hat{\mathcal{P}}_{12})\vert\psi_-\rangle = \tfrac12(\vert\psi_-\rangle - \vert\psi_-\rangle) = 0$, so $\hat{\Sigma}_+\vert\Psi\rangle = \vert\psi_+\rangle$; likewise $\hat{\Sigma}_-\vert\Psi\rangle = \vert\psi_-\rangle$. The two components are forced to be $\hat{\Sigma}_\pm\vert\Psi\rangle$, so the decomposition is unique. This is the explicit statement that the two-particle space splits cleanly, $\mathcal{H}^{\otimes 2} = \mathcal{H}_+ \oplus \mathcal{H}_-$, into bosonic and fermionic sectors. (For $N \ge 3$ the analogous projectors still exist, but $\mathcal{H}^{\otimes N}$ also contains mixed-symmetry sectors that are neither; only the totally symmetric and totally antisymmetric pieces are physical — cf. Problem 1.)

<!-- ─── -->

**3. Generalized Pauli exclusion.** The lecture shows the two-fermion state vanishes when $\vert\alpha_1\rangle = \vert\alpha_2\rangle$. Here we extend this vanishing to linear dependence.

(a) Show that $\vert\alpha_1, \alpha_2\rangle_- = 0$ whenever $\vert\alpha_2\rangle = c\,\vert\alpha_1\rangle$ for any $c \in \mathbb{C}$.

(b) For three fermions, show that $\vert\alpha_1, \alpha_2, \alpha_3\rangle_-$ vanishes whenever $\vert\alpha_3\rangle \in \mathrm{span}\{\vert\alpha_1\rangle, \vert\alpha_2\rangle\}$. (Hint: use linearity in the third slot and the two-fermion result.)

(c) Argue from multilinearity and antisymmetry that $\vert\alpha_1, \ldots, \alpha_N\rangle_-$ depends only on the $N$-dimensional subspace spanned by $\{\vert\alpha_i\rangle\}$, up to an overall scalar, and vanishes whenever these states are linearly dependent. This is the geometric form of Pauli exclusion: the physical fermionic state is determined by the filled subspace, not by a choice of basis inside it.

(d) Contrast with bosons. Show by explicit counterexample that $\vert\alpha, \alpha\rangle_+ \ne 0$ for any nonzero $\vert\alpha\rangle$, and that $\vert\alpha_1, c\,\alpha_1\rangle_+ \ne 0$ for any $c \ne 0$. Bosons admit no analogous linear-dependence vanishing.

**Solution.**

(a) The two-fermion antisymmetric state is $\vert\alpha_1,\alpha_2\rangle_- = \tfrac{1}{\sqrt2}\big(\vert\alpha_1\rangle\otimes\vert\alpha_2\rangle - \vert\alpha_2\rangle\otimes\vert\alpha_1\rangle\big)$. It is **linear in each slot**. Substitute $\vert\alpha_2\rangle = c\,\vert\alpha_1\rangle$ and pull the scalar out:

$$
\vert\alpha_1, c\,\alpha_1\rangle_-
= \frac{1}{\sqrt2}\big(\vert\alpha_1\rangle\otimes c\vert\alpha_1\rangle - c\vert\alpha_1\rangle\otimes\vert\alpha_1\rangle\big)
= \frac{c}{\sqrt2}\big(\vert\alpha_1\alpha_1\rangle - \vert\alpha_1\alpha_1\rangle\big) = 0.
$$

The two terms are identical and cancel — antisymmetry kills any state with proportional arguments.

(b) The three-fermion state $\vert\alpha_1,\alpha_2,\alpha_3\rangle_-$ is multilinear and totally antisymmetric. First note that a three-fermion state with **two equal arguments** vanishes: if slots $i$ and $j$ carry the same single-particle state, then exchanging those slots leaves the state unchanged, $\hat{\mathcal{P}}_{ij}\vert\cdots\rangle = +\vert\cdots\rangle$, while antisymmetry demands $\hat{\mathcal{P}}_{ij}\vert\cdots\rangle = -\vert\cdots\rangle$; a vector equal to minus itself is zero. (Equivalently, the Slater-determinant sum has two identical columns.)

Now let $\vert\alpha_3\rangle = a\,\vert\alpha_1\rangle + b\,\vert\alpha_2\rangle$ lie in $\mathrm{span}\{\vert\alpha_1\rangle,\vert\alpha_2\rangle\}$. Linearity in the third slot gives

$$
\vert\alpha_1,\alpha_2,\alpha_3\rangle_-
= a\,\vert\alpha_1,\alpha_2,\alpha_1\rangle_- + b\,\vert\alpha_1,\alpha_2,\alpha_2\rangle_-.
$$

In the first term slots $1$ and $3$ are equal; in the second, slots $2$ and $3$ are equal. By the observation just made, **both terms vanish**, so $\vert\alpha_1,\alpha_2,\alpha_3\rangle_- = 0$.

(c) The antisymmetrized state $\vert\alpha_1,\ldots,\alpha_N\rangle_-$ is multilinear in each slot and totally antisymmetric under any pairwise exchange. Two structural facts follow:

- *Adding a multiple of another argument changes nothing.* Replacing $\vert\alpha_i\rangle \to \vert\alpha_i\rangle + c\,\vert\alpha_j\rangle$ ($j\neq i$) produces an extra term with $\vert\alpha_j\rangle$ in both slots $i$ and $j$; that term has a repeated argument and vanishes (part b's mechanism). So this "shear" leaves the state invariant.
- *Rescaling an argument rescales the state.* Replacing $\vert\alpha_i\rangle \to c\,\vert\alpha_i\rangle$ multiplies the whole state by $c$.

These are exactly the elementary column operations on a determinant. Any change of basis inside $V \equiv \mathrm{span}\{\vert\alpha_i\rangle\}$ is a composition of such operations, i.e. a matrix $T$; it multiplies the state by the single scalar $\det T$. Therefore the state depends only on the subspace $V$, not on which basis of $V$ was chosen — up to an overall scalar (and after normalization, up to a phase). If the $\{\vert\alpha_i\rangle\}$ are **linearly dependent**, some $\vert\alpha_k\rangle$ is a combination of the others; expanding that slot by linearity produces only terms with a repeated argument, each zero, so the whole state vanishes. Physically: a fermionic many-body state is labelled by the *filled subspace* $V$ (which $N$-dimensional subspace of single-particle states is occupied), and $N$ fermions cannot be packed into fewer than $N$ independent states.

(d) Bosons use the **plus** sign, so the two terms reinforce instead of cancelling. First, $\vert\alpha,\alpha\rangle_+ = \vert\alpha\rangle\otimes\vert\alpha\rangle$ (the lecture's normalized form for a doubly-occupied mode); if $\vert\alpha\rangle\neq 0$ then $\big\|\,\vert\alpha\rangle\otimes\vert\alpha\rangle\,\big\| = \big\|\,\vert\alpha\rangle\,\big\|^2 \neq 0$, so $\vert\alpha,\alpha\rangle_+ \neq 0$. Second, for proportional arguments the unnormalized symmetric combination is

$$
\tfrac{1}{\sqrt2}\big(\vert\alpha_1\rangle\otimes c\vert\alpha_1\rangle + c\vert\alpha_1\rangle\otimes\vert\alpha_1\rangle\big) = \frac{2c}{\sqrt2}\,\vert\alpha_1\alpha_1\rangle = \sqrt2\,c\,\vert\alpha_1\alpha_1\rangle,
$$

which is nonzero for every $c\neq 0$. (Its norm $\sqrt2\,\vert c\vert$ exceeds $1$, signalling the repeated-mode normalization correction of Problem 4 — but it certainly does not vanish.)

There is no bosonic linear-dependence vanishing: the symmetrizer never cancels terms. Many bosons piling into one state is allowed — indeed it is the basis of Bose–Einstein condensation — whereas the antisymmetrizer forbids the fermionic analog outright.

<!-- ─── -->

**4. Bosonic normalization factor.** Work at the state level, with single-particle modes drawn from an orthonormal basis.

(a) For two bosons in distinct modes $\vert\alpha\rangle, \vert\beta\rangle$ with $\alpha \ne \beta$, verify that the lecture's prefactor $1/\sqrt{2!}$ gives a unit-norm state $\vert\alpha, \beta\rangle_+$. For two bosons in the same mode, verify that the normalized state is $\vert\alpha, \alpha\rangle_+ = \vert\alpha\rangle \otimes \vert\alpha\rangle$, whose prefactor differs from the naive $1/\sqrt{2!}$ by an extra factor of $\sqrt{2!}$.

(b) Three bosons with occupations $n_\alpha = 2,\ n_\beta = 1$. Enumerate the six terms in the unnormalized sum $\sum_{\pi \in S_3} \vert\alpha_{\pi(1)} \alpha_{\pi(2)} \alpha_{\pi(3)}\rangle$ (with $\alpha_1 = \alpha_2 = \alpha$, $\alpha_3 = \beta$), observe that only three distinct orthonormal orderings appear (each with multiplicity $2!$), and compute the norm squared of the full sum: $(2!)^2 \cdot 3 = 3!\cdot 2!$.

(c) General formula. For $N$ bosons with occupation numbers $\{n_\alpha\}$ on an orthonormal basis, count the number of distinct orderings ($N!/\prod_\alpha n_\alpha!$) and the multiplicity of each ($\prod_\alpha n_\alpha!$). Deduce that the unnormalized sum has norm squared $N!\,\prod_\alpha n_\alpha!$, hence

$$
\mathcal{N}_+ = \frac{1}{\sqrt{N!\,\prod_\alpha n_\alpha!}}.
$$

(d) Explain in one sentence why fermions require no analogous $n_\alpha!$ correction.

**Solution.**

(a) *Distinct modes.* With the prefactor $1/\sqrt{2!}$, $\vert\alpha,\beta\rangle_+ = \tfrac{1}{\sqrt2}\big(\vert\alpha\beta\rangle + \vert\beta\alpha\rangle\big)$. Its norm squared, with tensor inner products factorizing as $\langle\mu\nu\vert\mu'\nu'\rangle = \langle\mu\vert\mu'\rangle\langle\nu\vert\nu'\rangle$, is

$$
\langle\alpha,\beta\vert\alpha,\beta\rangle_+
= \tfrac12\big(\langle\alpha\beta\vert\alpha\beta\rangle + \langle\alpha\beta\vert\beta\alpha\rangle + \langle\beta\alpha\vert\alpha\beta\rangle + \langle\beta\alpha\vert\beta\alpha\rangle\big).
$$

For orthonormal modes with $\alpha\neq\beta$: the "diagonal" terms are $\langle\alpha\beta\vert\alpha\beta\rangle = \langle\beta\alpha\vert\beta\alpha\rangle = 1$, and the "cross" terms are $\langle\alpha\beta\vert\beta\alpha\rangle = \langle\alpha\vert\beta\rangle\langle\beta\vert\alpha\rangle = 0$. Hence $\langle\alpha,\beta\vert\alpha,\beta\rangle_+ = \tfrac12(1+0+0+1) = 1$ — unit norm. The naive $1/\sqrt{2!}$ is correct here.

*Same mode.* Now both bosons occupy $\vert\alpha\rangle$, so $\alpha_1 = \alpha_2 = \alpha$ and the permanent sum has two identical terms:

$$
\sum_{\pi\in S_2}\vert\alpha_{\pi(1)}\alpha_{\pi(2)}\rangle = \vert\alpha\alpha\rangle + \vert\alpha\alpha\rangle = 2\,\vert\alpha\alpha\rangle.
$$

The naive prefactor $1/\sqrt{2!}$ would give $\tfrac{2}{\sqrt2}\vert\alpha\alpha\rangle = \sqrt2\,\vert\alpha\alpha\rangle$, which has norm $\sqrt2 \neq 1$. The correctly normalized state is just $\vert\alpha,\alpha\rangle_+ = \vert\alpha\rangle\otimes\vert\alpha\rangle$, obtained from the unnormalized sum $2\vert\alpha\alpha\rangle$ by dividing by $2 = \sqrt{2!}\cdot\sqrt{2!}$. Compared with the naive $1/\sqrt{2!}$, the true prefactor carries one **extra** $1/\sqrt{2!} = 1/\sqrt{n_\alpha!}$ — the repeated-occupation correction. Equivalently $\mathcal{N}_+ = 1/\sqrt{N!\,\prod n_\alpha!} = 1/\sqrt{2!\cdot 2!} = 1/2$, and $\tfrac12\cdot 2\vert\alpha\alpha\rangle = \vert\alpha\alpha\rangle$. ✓

(b) With $\alpha_1 = \alpha_2 = \alpha$ and $\alpha_3 = \beta$, the term for permutation $\pi$ is $\vert\alpha_{\pi(1)}\rangle\otimes\vert\alpha_{\pi(2)}\rangle\otimes\vert\alpha_{\pi(3)}\rangle$; the mode $\beta$ sits in whichever slot $k$ has $\pi(k)=3$. Running over $S_3$:

| $\pi$ | slot of $\beta$ | term |
|-------|-----------------|------|
| $e$ | 3 | $\vert\alpha\alpha\beta\rangle$ |
| $(12)$ | 3 | $\vert\alpha\alpha\beta\rangle$ |
| $(23)$ | 2 | $\vert\alpha\beta\alpha\rangle$ |
| $(123)$ | 2 | $\vert\alpha\beta\alpha\rangle$ |
| $(13)$ | 1 | $\vert\beta\alpha\alpha\rangle$ |
| $(132)$ | 1 | $\vert\beta\alpha\alpha\rangle$ |

Only **three distinct orderings** appear — $\vert\alpha\alpha\beta\rangle$, $\vert\alpha\beta\alpha\rangle$, $\vert\beta\alpha\alpha\rangle$ — each occurring with multiplicity $2! = 2$ (the $2!$ ways of permuting the two identical $\alpha$ labels among themselves). So

$$
\sum_{\pi\in S_3}\vert\alpha_{\pi(1)}\alpha_{\pi(2)}\alpha_{\pi(3)}\rangle = 2\big(\vert\alpha\alpha\beta\rangle + \vert\alpha\beta\alpha\rangle + \vert\beta\alpha\alpha\rangle\big).
$$

The three distinct orderings are orthonormal (distinct arrangements of orthonormal modes), so the norm squared is

$$
\Big\|\textstyle\sum_\pi\cdots\Big\|^2 = 2^2\cdot(1+1+1) = (2!)^2\cdot 3 = 12 = 3!\cdot 2!.
$$

(c) For $N$ bosons with occupations $\{n_\alpha\}$, $\sum_\alpha n_\alpha = N$, on orthonormal modes: the $N!$ permutations in the sum produce orderings of the multiset of mode labels. The number of **distinct** orderings is the multinomial coefficient

$$
\#\{\text{orderings}\} = \frac{N!}{\prod_\alpha n_\alpha!},
$$

and each distinct ordering is reached by exactly $\prod_\alpha n_\alpha!$ permutations — the ways of shuffling identical labels within their occupied slots. Hence the unnormalized sum equals $\big(\prod_\alpha n_\alpha!\big)$ times the sum over distinct orderings. Those distinct orderings are mutually orthonormal, so

$$
\Big\|\textstyle\sum_{\pi\in S_N}\cdots\Big\|^2
= \Big(\prod_\alpha n_\alpha!\Big)^2 \times \frac{N!}{\prod_\alpha n_\alpha!}
= N!\,\prod_\alpha n_\alpha!.
$$

To make the state unit-norm we divide by the square root of this, giving

$$
\mathcal{N}_+ = \frac{1}{\sqrt{N!\,\prod_\alpha n_\alpha!}}.
$$

(Checks: $n_\alpha=2,n_\beta=1$ gives $3!\cdot2! = 12$, matching part b; the all-distinct case $n_\alpha\le1$ gives $\prod n_\alpha! = 1$ and recovers $1/\sqrt{N!}$.)

(d) Fermions obey the Pauli exclusion principle, so every occupation number is $n_\alpha \in \{0,1\}$, making $n_\alpha! = 1$ and the correction factor $\prod_\alpha n_\alpha! = 1$ trivially — there is never a repeated mode to over-count (a repeated mode would make the antisymmetric state vanish outright, not merely rescale it).

<!-- ─── -->

**5. Insertion and deletion as inverses.** Work in a single-mode Fock space throughout.

(a) Fermionic case. The fermionic Fock space for one mode contains only the vacuum $\mathbb{1}$ and the occupied state $\vert\alpha\rangle$. Apply the insertion and deletion rules to compute all four of $\vert\alpha\rangle \rhd_- \mathbb{1}$, $\vert\alpha\rangle \rhd_- \vert\alpha\rangle$, $\vert\alpha\rangle \lhd_- \mathbb{1}$, and $\vert\alpha\rangle \lhd_- \vert\alpha\rangle$. Verify that $\vert\alpha\rangle \rhd_- \vert\alpha\rangle = 0$ (Pauli) and $\vert\alpha\rangle \lhd_- \mathbb{1} = 0$.

(b) Verify that deletion undoes insertion on the vacuum, and insertion undoes deletion on the occupied state:

$$
\vert\alpha\rangle \lhd_- \bigl(\vert\alpha\rangle \rhd_- \mathbb{1}\bigr) = \mathbb{1}, \qquad \vert\alpha\rangle \rhd_- \bigl(\vert\alpha\rangle \lhd_- \vert\alpha\rangle\bigr) = \vert\alpha\rangle.
$$

Combining both, conclude that $\vert\alpha\rangle \lhd_- \bigl(\vert\alpha\rangle \rhd_- \vert\Psi\rangle\bigr) + \vert\alpha\rangle \rhd_- \bigl(\vert\alpha\rangle \lhd_- \vert\Psi\rangle\bigr) = \vert\Psi\rangle$ for every $\vert\Psi\rangle$ in the single-mode fermionic Fock space.

(c) Bosonic case. Let $\vert\alpha^n\rangle$ denote the $n$-boson state in a single mode (with $\vert\alpha^0\rangle = \mathbb{1}$ and $\vert\alpha^1\rangle = \vert\alpha\rangle$). Using the recursive definition, prove by induction on $n$:

$$
\vert\alpha\rangle \rhd_+ \vert\alpha^n\rangle = (n+1)\,\vert\alpha^{n+1}\rangle, \qquad \vert\alpha\rangle \lhd_+ \vert\alpha^n\rangle = n\,\vert\alpha^{n-1}\rangle.
$$

(d) Compute $\vert\alpha\rangle \lhd_+ \bigl(\vert\alpha\rangle \rhd_+ \vert\alpha^n\rangle\bigr) - \vert\alpha\rangle \rhd_+ \bigl(\vert\alpha\rangle \lhd_+ \vert\alpha^n\rangle\bigr)$ and show the result is $(2n+1)\,\vert\alpha^n\rangle$, not $\vert\alpha^n\rangle$. Conclude that the bare bosonic insertion and deletion rules are mutual inverses only up to a particle-number-dependent multiplicity, whereas the fermionic rules are already exact inverses. The bosonic normalization is addressed in §2.1.3.

**Solution.**

Recall the rules. Insertion: $\vert\alpha\rangle\rhd_\pm\mathbb{1} = \vert\alpha\rangle$ and $\vert\alpha\rangle\rhd_\pm(\vert\beta\rangle\otimes\vert\Psi\rangle) = \vert\alpha\rangle\otimes\vert\beta\rangle\otimes\vert\Psi\rangle \pm \vert\beta\rangle\otimes(\vert\alpha\rangle\rhd_\pm\vert\Psi\rangle)$. Deletion: $\vert\alpha\rangle\lhd_\pm\mathbb{1} = 0$ and $\vert\alpha\rangle\lhd_\pm(\vert\beta\rangle\otimes\vert\Psi\rangle) = \delta_{\alpha\beta}\vert\Psi\rangle \pm \vert\beta\rangle\otimes(\vert\alpha\rangle\lhd_\pm\vert\Psi\rangle)$.

(a) Evaluate the four fermionic ($-$) operations in turn. The two base cases are immediate: $\vert\alpha\rangle\rhd_-\mathbb{1} = \vert\alpha\rangle$ (insertion into the vacuum) and $\vert\alpha\rangle\lhd_-\mathbb{1} = 0$ (nothing can be deleted from the vacuum).

For $\vert\alpha\rangle\rhd_-\vert\alpha\rangle$, write the target as $\vert\alpha\rangle = \vert\alpha\rangle\otimes\mathbb{1}$ (so $\beta=\alpha,\ \Psi=\mathbb{1}$) and apply the recursive insertion rule:

$$
\vert\alpha\rangle\rhd_-\vert\alpha\rangle = \vert\alpha\rangle\otimes\vert\alpha\rangle - \vert\alpha\rangle\otimes(\vert\alpha\rangle\rhd_-\mathbb{1}) = \vert\alpha\alpha\rangle - \vert\alpha\rangle\otimes\vert\alpha\rangle = 0.
$$

The minus sign of the fermionic rule cancels the two copies — this **is** the Pauli exclusion principle. For $\vert\alpha\rangle\lhd_-\vert\alpha\rangle$, again with $\beta=\alpha,\ \Psi=\mathbb{1}$, the recursive deletion rule gives

$$
\vert\alpha\rangle\lhd_-\vert\alpha\rangle = \delta_{\alpha\alpha}\,\mathbb{1} - \vert\alpha\rangle\otimes(\vert\alpha\rangle\lhd_-\mathbb{1}) = \mathbb{1} - \vert\alpha\rangle\otimes 0 = \mathbb{1}.
$$

Summary: $\vert\alpha\rangle\rhd_-\mathbb{1} = \vert\alpha\rangle$, $\ \vert\alpha\rangle\rhd_-\vert\alpha\rangle = 0$, $\ \vert\alpha\rangle\lhd_-\mathbb{1} = 0$, $\ \vert\alpha\rangle\lhd_-\vert\alpha\rangle = \mathbb{1}$.

(b) Compose the results of (a):

$$
\vert\alpha\rangle\lhd_-\big(\vert\alpha\rangle\rhd_-\mathbb{1}\big) = \vert\alpha\rangle\lhd_-\vert\alpha\rangle = \mathbb{1},
\qquad
\vert\alpha\rangle\rhd_-\big(\vert\alpha\rangle\lhd_-\vert\alpha\rangle\big) = \vert\alpha\rangle\rhd_-\mathbb{1} = \vert\alpha\rangle.
$$

Deletion undoes insertion on the vacuum; insertion undoes deletion on the occupied state. Now define, for any $\vert\Psi\rangle$ in the two-dimensional single-mode fermionic Fock space,

$$
\mathcal{D}[\Psi] \equiv \vert\alpha\rangle\lhd_-\big(\vert\alpha\rangle\rhd_-\vert\Psi\rangle\big) + \vert\alpha\rangle\rhd_-\big(\vert\alpha\rangle\lhd_-\vert\Psi\rangle\big).
$$

Evaluate on the two basis states:

- $\vert\Psi\rangle = \mathbb{1}$: first term $= \vert\alpha\rangle\lhd_-\vert\alpha\rangle = \mathbb{1}$; second term $= \vert\alpha\rangle\rhd_-(\vert\alpha\rangle\lhd_-\mathbb{1}) = \vert\alpha\rangle\rhd_-0 = 0$. Sum $= \mathbb{1}$.
- $\vert\Psi\rangle = \vert\alpha\rangle$: first term $= \vert\alpha\rangle\lhd_-(\vert\alpha\rangle\rhd_-\vert\alpha\rangle) = \vert\alpha\rangle\lhd_-0 = 0$; second term $= \vert\alpha\rangle\rhd_-(\vert\alpha\rangle\lhd_-\vert\alpha\rangle) = \vert\alpha\rangle\rhd_-\mathbb{1} = \vert\alpha\rangle$. Sum $= \vert\alpha\rangle$.

So $\mathcal{D}[\Psi] = \vert\Psi\rangle$ on both basis states; since insertion and deletion are linear, $\mathcal{D}[\Psi] = \vert\Psi\rangle$ for **every** $\vert\Psi\rangle$ in the space. This is the first-quantized precursor of the fermionic anticommutator $\{\hat{a}_\alpha, \hat{a}^\dagger_\alpha\} = \hat{I}$ (§2.1.3): the *sum* of "insert-then-delete" and "delete-then-insert" is the identity.

(c) Write $\vert\alpha^n\rangle = \vert\alpha\rangle^{\otimes n}$, the $n$-fold tensor product (already symmetric), with $\vert\alpha^0\rangle = \mathbb{1}$.

*Insertion, $\vert\alpha\rangle\rhd_+\vert\alpha^n\rangle = (n+1)\vert\alpha^{n+1}\rangle$.* Base case $n=0$: $\vert\alpha\rangle\rhd_+\mathbb{1} = \vert\alpha\rangle = 1\cdot\vert\alpha^1\rangle$. ✓ Inductive step: assume the claim for $n$. Write $\vert\alpha^{n+1}\rangle = \vert\alpha\rangle\otimes\vert\alpha^n\rangle$ (so $\beta=\alpha,\ \Psi=\alpha^n$) and apply the bosonic ($+$) rule:

$$
\begin{split}
\vert\alpha\rangle\rhd_+\vert\alpha^{n+1}\rangle
&= \vert\alpha\rangle\otimes\vert\alpha\rangle\otimes\vert\alpha^n\rangle + \vert\alpha\rangle\otimes\big(\vert\alpha\rangle\rhd_+\vert\alpha^n\rangle\big)\\
&= \vert\alpha^{n+2}\rangle + \vert\alpha\rangle\otimes(n+1)\vert\alpha^{n+1}\rangle\\
&= \vert\alpha^{n+2}\rangle + (n+1)\vert\alpha^{n+2}\rangle = (n+2)\,\vert\alpha^{n+2}\rangle.
\end{split}
$$

This is the claim with $n\to n+1$, completing the induction.

*Deletion, $\vert\alpha\rangle\lhd_+\vert\alpha^n\rangle = n\,\vert\alpha^{n-1}\rangle$.* Base case $n=0$: $\vert\alpha\rangle\lhd_+\mathbb{1} = 0 = 0\cdot\vert\alpha^{-1}\rangle$. ✓ Inductive step: assume the claim for $n$. With $\vert\alpha^{n+1}\rangle = \vert\alpha\rangle\otimes\vert\alpha^n\rangle$ and $\delta_{\alpha\alpha}=1$,

$$
\begin{split}
\vert\alpha\rangle\lhd_+\vert\alpha^{n+1}\rangle
&= \delta_{\alpha\alpha}\,\vert\alpha^n\rangle + \vert\alpha\rangle\otimes\big(\vert\alpha\rangle\lhd_+\vert\alpha^n\rangle\big)\\
&= \vert\alpha^n\rangle + \vert\alpha\rangle\otimes n\,\vert\alpha^{n-1}\rangle\\
&= \vert\alpha^n\rangle + n\,\vert\alpha^n\rangle = (n+1)\,\vert\alpha^n\rangle,
\end{split}
$$

the claim with $n\to n+1$. Both formulas hold for all $n\ge 0$. (Intuitively: insertion drops $\vert\alpha\rangle$ into each of $n+1$ gaps of $\vert\alpha^{n+1}\rangle$, all identical, giving the multiplicity $n+1$; deletion removes $\vert\alpha\rangle$ from each of the $n$ occupied slots, giving $n$.)

(d) Substitute the formulas from (c), being careful that the operations are linear so scalars pull through:

$$
\begin{split}
\vert\alpha\rangle\lhd_+\big(\vert\alpha\rangle\rhd_+\vert\alpha^n\rangle\big)
&= \vert\alpha\rangle\lhd_+\big((n+1)\vert\alpha^{n+1}\rangle\big)
= (n+1)\,(n+1)\,\vert\alpha^n\rangle = (n+1)^2\,\vert\alpha^n\rangle,\\[4pt]
\vert\alpha\rangle\rhd_+\big(\vert\alpha\rangle\lhd_+\vert\alpha^n\rangle\big)
&= \vert\alpha\rangle\rhd_+\big(n\,\vert\alpha^{n-1}\rangle\big)
= n\cdot n\,\vert\alpha^n\rangle = n^2\,\vert\alpha^n\rangle.
\end{split}
$$

Their difference is

$$
\vert\alpha\rangle\lhd_+\big(\vert\alpha\rangle\rhd_+\vert\alpha^n\rangle\big) - \vert\alpha\rangle\rhd_+\big(\vert\alpha\rangle\lhd_+\vert\alpha^n\rangle\big)
= \big[(n+1)^2 - n^2\big]\,\vert\alpha^n\rangle = (2n+1)\,\vert\alpha^n\rangle.
$$

The result is $(2n+1)\vert\alpha^n\rangle$, **not** $\vert\alpha^n\rangle$: the bare bosonic insertion/deletion rules fail to be exact mutual inverses, missing by an $n$-dependent multiplicity. Contrast the fermionic case (part b), where the analogous combination — there a *sum*, the anticommutator pattern — returned $\vert\Psi\rangle$ exactly. The cure is to rescale: defining $\hat{a}^\dagger_\alpha,\hat{a}_\alpha$ to carry $\sqrt{n}$-type normalization factors converts the bare rules into operators obeying $[\hat{a}_\alpha,\hat{a}^\dagger_\alpha] = \hat{I}$ exactly. That construction is the subject of §2.1.3.

<!-- ─── -->

**6. Slater determinant overlap.** Derive the central identity relating many-fermion inner products to determinants of single-particle overlaps.

(a) For arbitrary (possibly non-orthogonal) single-particle states $\vert\alpha_1\rangle, \vert\alpha_2\rangle, \vert\beta_1\rangle, \vert\beta_2\rangle$, compute $\langle\alpha_1, \alpha_2 \vert \beta_1, \beta_2\rangle_-$ directly from the two-fermion antisymmetric definition, and show it equals $\det M$ with $M_{ij} = \langle\alpha_i \vert \beta_j\rangle$.

(b) Specialize to orthonormal $\{\vert\alpha_i\rangle\}$ and verify $\langle\alpha_1, \alpha_2 \vert \alpha_1, \alpha_2\rangle_- = 1$.

(c) Hydrogen molecule. Let $\vert L\rangle, \vert R\rangle$ be unit-norm but non-orthogonal left and right atomic orbitals with real overlap $\langle L \vert R\rangle = s \in [0, 1]$. Compute $\langle L, R \vert L, R\rangle_-$ and interpret the limits $s \to 0$ (atoms far apart) and $s \to 1$ (atoms merge; linear dependence forces the antisymmetric state to vanish, a generalized form of Pauli exclusion).

(d) State without proof the $N$-fermion generalization $\langle\alpha_1, \ldots, \alpha_N \vert \beta_1, \ldots, \beta_N\rangle_- = \det\langle\alpha_i \vert \beta_j\rangle$. Briefly note the bosonic analog, which replaces the determinant with the permanent of the same matrix.

**Solution.**

(a) The two-fermion antisymmetric states are $\vert\beta_1,\beta_2\rangle_- = \tfrac{1}{\sqrt2}\big(\vert\beta_1\beta_2\rangle - \vert\beta_2\beta_1\rangle\big)$ and, dualizing, $\langle\alpha_1,\alpha_2\vert = \tfrac{1}{\sqrt2}\big(\langle\alpha_1\alpha_2\vert - \langle\alpha_2\alpha_1\vert\big)$. Their overlap, expanding the product of two binomials, is

$$
\langle\alpha_1,\alpha_2\vert\beta_1,\beta_2\rangle_-
= \tfrac12\Big(\langle\alpha_1\alpha_2\vert\beta_1\beta_2\rangle - \langle\alpha_1\alpha_2\vert\beta_2\beta_1\rangle - \langle\alpha_2\alpha_1\vert\beta_1\beta_2\rangle + \langle\alpha_2\alpha_1\vert\beta_2\beta_1\rangle\Big).
$$

Each two-particle inner product factorizes over the tensor slots, $\langle\mu\nu\vert\mu'\nu'\rangle = \langle\mu\vert\mu'\rangle\langle\nu\vert\nu'\rangle$:

$$
\langle\alpha_1,\alpha_2\vert\beta_1,\beta_2\rangle_-
= \tfrac12\Big(\langle\alpha_1\vert\beta_1\rangle\langle\alpha_2\vert\beta_2\rangle - \langle\alpha_1\vert\beta_2\rangle\langle\alpha_2\vert\beta_1\rangle - \langle\alpha_2\vert\beta_1\rangle\langle\alpha_1\vert\beta_2\rangle + \langle\alpha_2\vert\beta_2\rangle\langle\alpha_1\vert\beta_1\rangle\Big).
$$

The first and fourth products are identical; so are the second and third. The $\tfrac12$ cancels the resulting factor of $2$:

$$
\langle\alpha_1,\alpha_2\vert\beta_1,\beta_2\rangle_-
= \langle\alpha_1\vert\beta_1\rangle\langle\alpha_2\vert\beta_2\rangle - \langle\alpha_1\vert\beta_2\rangle\langle\alpha_2\vert\beta_1\rangle.
$$

With $M_{ij} \equiv \langle\alpha_i\vert\beta_j\rangle$ this is $M_{11}M_{22} - M_{12}M_{21} = \det M$, exactly the $2\times2$ determinant. No orthogonality was assumed.

(b) For orthonormal $\{\vert\alpha_i\rangle\}$ taken as the bra states and with $\beta_j = \alpha_j$, the matrix is $M_{ij} = \langle\alpha_i\vert\alpha_j\rangle = \delta_{ij}$, the identity. Hence

$$
\langle\alpha_1,\alpha_2\vert\alpha_1,\alpha_2\rangle_- = \det\mathbb{I} = 1,
$$

so the prefactor $1/\sqrt{2!}$ correctly normalizes the antisymmetric state when the modes are orthonormal.

(c) Here $\vert\alpha_1\rangle = \vert\beta_1\rangle = \vert L\rangle$ and $\vert\alpha_2\rangle = \vert\beta_2\rangle = \vert R\rangle$, with $\langle L\vertL\rangle = \langle R\vertR\rangle = 1$ and $\langle L\vertR\rangle = \langle R\vertL\rangle = s$ real. The overlap matrix and its determinant are

$$
M = \begin{pmatrix}\langle L\vertL\rangle & \langle L\vertR\rangle\\ \langle R\vertL\rangle & \langle R\vertR\rangle\end{pmatrix}
= \begin{pmatrix}1 & s\\ s & 1\end{pmatrix},
\qquad
\langle L,R\vert L,R\rangle_- = \det M = 1 - s^2.
$$

*Limit $s\to 0$* (atoms far apart, orbitals effectively orthogonal): $\langle L,R\vert L,R\rangle_- \to 1$. The antisymmetric two-electron state is properly normalized — two well-separated, independent fermions, one on each atom.

*Limit $s\to 1$* (atoms merged, $\vert R\rangle\to\vert L\rangle$): $\langle L,R\vert L,R\rangle_- \to 0$. The orbitals become linearly dependent, and the antisymmetric state collapses to the zero vector — one cannot place two fermions in what has become a single orbital. (A unit physical state would require dividing by $\sqrt{1-s^2}$, which diverges as $s\to1$, signalling that the state ceases to exist.) This is the generalized Pauli exclusion of Problem 3 made quantitative: the norm $1-s^2$ interpolates smoothly between "two distinct states available" ($s=0$) and "exclusion" ($s=1$).

(d) The $N$-fermion generalization is the **Slater-determinant overlap identity**

$$
\langle\alpha_1,\ldots,\alpha_N\vert\beta_1,\ldots,\beta_N\rangle_- = \det\big[\langle\alpha_i\vert\beta_j\rangle\big]_{1\le i,j\le N},
$$

an $N\times N$ determinant of single-particle overlaps. (It follows from the antisymmetric definition: the $N!$ permutations in bra and ket combine, by orthogonality of distinct slot assignments, into the Leibniz sum $\sum_\pi \mathrm{sgn}(\pi)\prod_i \langle\alpha_i\vert\beta_{\pi(i)}\rangle$.) The vanishing of a determinant with dependent columns reproduces Pauli exclusion automatically. The **bosonic** analog uses the *same* overlap matrix but with the all-plus signs, replacing the determinant by the **permanent**:

$$
\langle\alpha_1,\ldots,\alpha_N\vert\beta_1,\ldots,\beta_N\rangle_+ = \operatorname{perm}\big[\langle\alpha_i\vert\beta_j\rangle\big],
$$

which has no sign cancellation and therefore no linear-dependence vanishing — bosons may share states freely.

<!-- ─── -->

**7. Fermion counting.** How many independent antisymmetric states can be formed by placing $N$ fermions into $D$ single-particle modes (with $D \geq N$)? Give the combinatorial formula as a binomial coefficient. What happens when $N > D$, and how does this connect to the Pauli exclusion principle?

**Solution.**

By the geometric form of Pauli exclusion (Problem 3c), an $N$-fermion antisymmetric state is determined entirely by **which** $N$ of the $D$ modes are occupied — each mode holds $0$ or $1$ fermion, and the occupied set fixes the Slater determinant up to a phase. Counting independent states is therefore counting size-$N$ subsets of a $D$-element set:

$$
\#\{\text{fermionic states}\} = \binom{D}{N} = \frac{D!}{N!\,(D-N)!}.
$$

For example, $D = 5$ modes and $N = 3$ fermions give $\binom{5}{3} = 10$ states.

When $N > D$, the formula gives $\binom{D}{N} = 0$ — **no antisymmetric states exist**. The reason is the pigeonhole principle: placing more than $D$ fermions into $D$ modes forces at least two fermions into the same mode, so the Slater determinant has two identical columns and vanishes. This is exactly the Pauli exclusion principle in counting form: a system of $D$ single-particle modes can hold **at most $D$** fermions. (It is the microscopic origin of atomic shell filling and of the degeneracy pressure that supports white dwarfs and neutron stars.)

<!-- ─── -->

**8. Boson counting.** How many independent symmetric states can be formed by placing $N$ bosons into $D$ single-particle modes? Derive the combinatorial formula (stars and bars) as a binomial coefficient, and contrast with the fermionic count from the previous problem. Explain why there is no upper bound on $N$ at fixed $D$ for bosons.

**Solution.**

A symmetric $N$-boson state is determined by its **occupation numbers** $(n_1, n_2, \ldots, n_D)$, the number of bosons in each of the $D$ modes, subject to $n_i \ge 0$ and $\sum_{i=1}^D n_i = N$. (Bosons carry no labels and have no exclusion constraint, so only the occupation tuple matters.) Counting independent states means counting such tuples.

*Stars and bars.* Represent the configuration as a row of $N$ stars (the bosons) and $D-1$ bars (dividers separating the $D$ modes):

$$
\underbrace{\star\star\,|\,\star\,|\;\;|\,\star\star\star\cdots}_{N\ \text{stars},\ D-1\ \text{bars}}
$$

Every arrangement of these $N + (D-1)$ symbols corresponds to exactly one occupation tuple (the stars before the first bar fill mode $1$, those between bars $1$ and $2$ fill mode $2$, and so on; an empty gap means $n_i = 0$). The number of arrangements is the number of ways to choose which of the $N + D - 1$ positions hold the stars:

$$
\#\{\text{bosonic states}\} = \binom{N + D - 1}{N} = \binom{N + D - 1}{D - 1}.
$$

For example, $N = 3$ bosons in $D = 2$ modes give $\binom{4}{3} = 4$ states: occupations $(3,0), (2,1), (1,2), (0,3)$.

*Contrast with fermions.* The fermion count $\binom{D}{N}$ requires $D \ge N$ and **vanishes** for $N > D$. The boson count $\binom{N+D-1}{N}$ is positive for **every** $N \ge 0$ at any fixed $D \ge 1$, and grows without bound — polynomially in $N$, like $N^{D-1}/(D-1)!$ for large $N$. The difference is the Pauli exclusion principle: fermion occupations are capped at $n_i \le 1$ (choosing a *subset* of modes), whereas boson occupations $n_i \in \{0,1,2,\ldots\}$ are unrestricted (choosing a *multiset*). Because any number of bosons can pile into a single mode, there is no ceiling on $N$ at fixed $D$ — the physical content of Bose–Einstein statistics and, in the extreme, of Bose–Einstein condensation.
