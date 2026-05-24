# 2.1.1 Tensor Product
Worked solutions for the homework problems in the [2.1.1 Tensor Product](../ch2_identical-particles/2-1-1-tensor-product) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Identifying entangled states.** Three two-qubit states:

$$
\vert\Psi_1\rangle = \tfrac{1}{\sqrt 2}\bigl(\vert 00\rangle + \vert 01\rangle\bigr),\qquad \vert\Psi_2\rangle = \tfrac{1}{\sqrt 2}\bigl(\vert 00\rangle + \vert 11\rangle\bigr),\qquad \vert\Psi_3\rangle = \tfrac{1}{\sqrt 2}\bigl(\vert 01\rangle + \vert 10\rangle\bigr).
$$

A state is a **product state** if it can be written as $\vert\psi_A\rangle\otimes\vert\psi_B\rangle$ for some single-qubit kets $\vert\psi_A\rangle, \vert\psi_B\rangle$; otherwise it is **entangled**.

(a) For each $\vert\Psi_i\rangle$, attempt to write it as a product. For the product cases, give explicit $\vert\psi_A\rangle, \vert\psi_B\rangle$.

(b) For each non-product (entangled) case, argue from the failed factorization equations *why* no decomposition exists.

(c) The general two-qubit state $\alpha_{00}\vert 00\rangle + \alpha_{01}\vert 01\rangle + \alpha_{10}\vert 10\rangle + \alpha_{11}\vert 11\rangle$ is a product state if and only if $\alpha_{00}\alpha_{11} = \alpha_{01}\alpha_{10}$ (the "determinant condition"). Verify this criterion on each of the three states above and confirm it agrees with your conclusions in (a)–(b).

**Solution.**

(a) Set $\vert\psi_A\rangle = \alpha_0\vert 0\rangle + \alpha_1\vert 1\rangle$ and $\vert\psi_B\rangle = \beta_0\vert 0\rangle + \beta_1\vert 1\rangle$. The product expands as

$$
\vert\psi_A\rangle\otimes\vert\psi_B\rangle = \alpha_0\beta_0\vert 00\rangle + \alpha_0\beta_1\vert 01\rangle + \alpha_1\beta_0\vert 10\rangle + \alpha_1\beta_1\vert 11\rangle.
$$

**$\vert\Psi_1\rangle$**: amplitudes $(\tfrac{1}{\sqrt 2}, \tfrac{1}{\sqrt 2}, 0, 0)$. We need $\alpha_0\beta_0 = \alpha_0\beta_1 = \tfrac{1}{\sqrt 2}$ and $\alpha_1\beta_0 = \alpha_1\beta_1 = 0$. The second pair forces $\alpha_1 = 0$ (since $\beta_0, \beta_1$ can't both vanish without ruining $\alpha_0\beta_0$), and the first gives $\beta_0 = \beta_1$. Normalising with $\alpha_0 = 1$ and $\beta_0 = \beta_1 = \tfrac{1}{\sqrt 2}$:

$$
\vert\Psi_1\rangle = \vert 0\rangle\otimes\tfrac{1}{\sqrt 2}(\vert 0\rangle + \vert 1\rangle) = \vert 0\rangle\otimes\vert+\rangle. \quad\text{Product.}
$$

**$\vert\Psi_2\rangle$**: amplitudes $(\tfrac{1}{\sqrt 2}, 0, 0, \tfrac{1}{\sqrt 2})$. The factorization requires $\alpha_0\beta_1 = 0$ AND $\alpha_1\beta_0 = 0$. The first forces either $\alpha_0 = 0$ or $\beta_1 = 0$; either choice immediately kills one of $\alpha_0\beta_0$ or $\alpha_1\beta_1$, both of which need to be $\tfrac{1}{\sqrt 2}\neq 0$. **Entangled** — no factorization exists.

**$\vert\Psi_3\rangle$**: amplitudes $(0, \tfrac{1}{\sqrt 2}, \tfrac{1}{\sqrt 2}, 0)$. The factorization requires $\alpha_0\beta_0 = 0$ AND $\alpha_1\beta_1 = 0$ — same obstruction as $\vert\Psi_2\rangle$. Either choice kills the cross terms. **Entangled.**

(b) The structural obstruction: a product state's four amplitudes are determined by only $2+2 = 4$ complex numbers via *two products* per amplitude, so the four amplitudes are *correlated*. A state with $\alpha_{00} = \alpha_{11} \neq 0$ but $\alpha_{01} = \alpha_{10} = 0$ (like $\vert\Psi_2\rangle$) requires the cross terms to vanish *and* the diagonal terms to be nonzero — incompatible for any factorization, because the cross terms $\alpha_0\beta_1, \alpha_1\beta_0$ can vanish only if some single-qubit amplitude vanishes, which then forces the diagonals to vanish too. The "entanglement" is the *pattern* of zeros: $\vert\Psi_2\rangle$ and $\vert\Psi_3\rangle$ have non-product zero/non-zero patterns.

(c) Compute $\alpha_{00}\alpha_{11} - \alpha_{01}\alpha_{10}$ for each:

- $\vert\Psi_1\rangle$: $(\tfrac{1}{\sqrt 2})(0) - (\tfrac{1}{\sqrt 2})(0) = 0$. Determinant condition **satisfied** → product. ✓
- $\vert\Psi_2\rangle$: $(\tfrac{1}{\sqrt 2})(\tfrac{1}{\sqrt 2}) - (0)(0) = \tfrac{1}{2}$. Determinant condition **fails** → entangled. ✓
- $\vert\Psi_3\rangle$: $(0)(0) - (\tfrac{1}{\sqrt 2})(\tfrac{1}{\sqrt 2}) = -\tfrac{1}{2}$. Determinant condition **fails** → entangled. ✓

The determinant condition is the **non-zero $2\times 2$ minor** test: a 2-qubit state's amplitude matrix $\begin{pmatrix}\alpha_{00} & \alpha_{01} \\ \alpha_{10} & \alpha_{11}\end{pmatrix}$ has rank 1 (i.e. is a product of column-and-row vectors) iff its determinant vanishes. **Determinant nonzero = entangled.** This rank-1 criterion is the simplest case of the general **Schmidt rank** classification of bipartite states — a state is product iff its amplitude matrix has rank 1, and the rank measures "how entangled" it is.

<!-- ─── -->

**2. Operator products via the mixed-product rule.** The mixed-product rule states that for tensor-product operators acting on the same composite system,

$$
(\hat A\otimes\hat B)(\hat C\otimes\hat D) = (\hat A\hat C)\otimes(\hat B\hat D).
$$

This is the algebraic backbone of multi-qubit operator manipulation. Apply it concretely.

(a) Compute $(\hat X\otimes\hat Y)(\hat Z\otimes\hat I)$ two ways: (i) using the mixed-product rule and Pauli multiplication ($\hat X\hat Z = -\mathrm{i}\hat Y$, $\hat Y\hat I = \hat Y$); (ii) by explicit matrix multiplication of the two $4\times 4$ matrices.

(b) Verify the two answers agree.

(c) Use the mixed-product rule to compute $(\hat X\otimes\hat Y)^2$ in two-qubit form. Express your answer as a single Pauli string with sign.

**Solution.**

(a) **(i) Mixed-product rule.** Slot 1 holds $\hat X\hat Z$; slot 2 holds $\hat Y\hat I$. Using the Pauli multiplication law $\hat\sigma^i\hat\sigma^j = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k$ (1.1.3),

$$
\hat X\hat Z = -\mathrm{i}\hat Y, \qquad \hat Y\hat I = \hat Y.
$$

So

$$
(\hat X\otimes\hat Y)(\hat Z\otimes\hat I) = (\hat X\hat Z)\otimes(\hat Y\hat I) = (-\mathrm{i}\hat Y)\otimes\hat Y = -\mathrm{i}\,\hat Y\otimes\hat Y.
$$

**(ii) Explicit matrix multiplication.** Build $\hat X\otimes\hat Y$ and $\hat Z\otimes\hat I$ as $4\times 4$ Kronecker products:

$$
\hat X\otimes\hat Y = \begin{pmatrix} 0 & 0 & 0 & -\mathrm{i} \\ 0 & 0 & \mathrm{i} & 0 \\ 0 & -\mathrm{i} & 0 & 0 \\ \mathrm{i} & 0 & 0 & 0 \end{pmatrix},\qquad \hat Z\otimes\hat I = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}.
$$

Multiplying (column $k$ of the second matrix is just $\pm e_k$, so we pick up the corresponding column of the first matrix with sign):

$$
(\hat X\otimes\hat Y)(\hat Z\otimes\hat I) = \begin{pmatrix} 0 & 0 & 0 & \mathrm{i} \\ 0 & 0 & -\mathrm{i} & 0 \\ 0 & -\mathrm{i} & 0 & 0 \\ \mathrm{i} & 0 & 0 & 0 \end{pmatrix}.
$$

(b) Compare with $-\mathrm{i}\,\hat Y\otimes\hat Y$. The matrix $\hat Y\otimes\hat Y$ has corner entries $(-\mathrm{i})(-\mathrm{i}) = -1$ at $(1,4)$ and $(\mathrm{i})(\mathrm{i}) = -1$ at $(4,1)$, and central entries $(-\mathrm{i})(\mathrm{i}) = +1$ at $(2,3)$ and $(\mathrm{i})(-\mathrm{i}) = +1$ at $(3,2)$:

$$
\hat Y\otimes\hat Y = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix},\quad -\mathrm{i}\hat Y\otimes\hat Y = \begin{pmatrix} 0 & 0 & 0 & \mathrm{i} \\ 0 & 0 & -\mathrm{i} & 0 \\ 0 & -\mathrm{i} & 0 & 0 \\ \mathrm{i} & 0 & 0 & 0 \end{pmatrix}.
$$

Matches part (ii) exactly. $\checkmark$

The mixed-product rule **factor-by-factor** evaluation is dramatically simpler than the $4\times 4$ matrix calculation — a $16$-entry product becomes two $2\times 2$ products, each of which is just a Pauli multiplication. This is the practical benefit of working in tensor-product form: the algebra of $N$-qubit operators reduces to $N$ separate single-qubit algebras.

(c) Apply mixed-product rule to the square:

$$
(\hat X\otimes\hat Y)^2 = (\hat X\hat X)\otimes(\hat Y\hat Y) = \hat I\otimes\hat I.
$$

So squaring any "single Pauli on each qubit" string gives $\hat I\otimes\hat I = \hat I_{\mathrm{2-qubit}}$. This is the natural generalisation of the single-qubit identity $(\hat\sigma^a)^2 = \hat I$ to multi-qubit Pauli strings, and the property that makes Pauli strings ideal eigenoperators of two-level measurements: each has eigenvalues $\pm 1$, generalising the qubit-level result of 1.1.3 P7.

<!-- ─── -->

**3. The SWAP operator.** Define the **SWAP** operator $\hat S$ on two qubits by its action on the computational basis:

$$
\hat S\vert ab\rangle = \vert ba\rangle \quad\text{for all } a, b \in \{0, 1\}.
$$

(a) Write $\hat S$ as a $4\times 4$ matrix in the ordered basis $\{\vert 00\rangle, \vert 01\rangle, \vert 10\rangle, \vert 11\rangle\}$.

(b) Show that $\hat S^2 = \hat I$ (the SWAP is an involution). Conclude that its eigenvalues are $\pm 1$.

(c) Identify the **symmetric** ($+1$) and **antisymmetric** ($-1$) eigenspaces of $\hat S$. Give a basis for each, and state their dimensions.

(d) Show that $\hat S$ admits the Pauli-string decomposition

$$
\hat S = \tfrac{1}{2}\bigl(\hat I\otimes\hat I + \hat X\otimes\hat X + \hat Y\otimes\hat Y + \hat Z\otimes\hat Z\bigr).
$$

(Hint: build each Pauli-string matrix and sum, or use the trace-projection method from 1.1.3 P5 on the 2-qubit Pauli basis.)

**Solution.**

(a) The action $\hat S\vert ab\rangle = \vert ba\rangle$ gives: $\vert 00\rangle\to\vert 00\rangle$, $\vert 01\rangle\to\vert 10\rangle$, $\vert 10\rangle\to\vert 01\rangle$, $\vert 11\rangle\to\vert 11\rangle$. So the matrix (column $j$ is the image of basis vector $j$) is

$$
\hat S = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
$$

(b) Applying SWAP twice swaps $a, b$ then swaps them back: $\hat S^2\vert ab\rangle = \hat S\vert ba\rangle = \vert ab\rangle$. So $\hat S^2 = \hat I$. If $\lambda$ is an eigenvalue of $\hat S$ with eigenvector $\vert v\rangle$, applying twice gives $\lambda^2\vert v\rangle = \vert v\rangle$, so $\lambda^2 = 1$, $\lambda = \pm 1$.

(c) Eigenvectors of $\hat S$ in the computational basis:

- $\hat S\vert 00\rangle = \vert 00\rangle$: eigenvalue $+1$.
- $\hat S\vert 11\rangle = \vert 11\rangle$: eigenvalue $+1$.
- $\hat S\,\tfrac{1}{\sqrt 2}(\vert 01\rangle + \vert 10\rangle) = \tfrac{1}{\sqrt 2}(\vert 10\rangle + \vert 01\rangle)$: eigenvalue $+1$.
- $\hat S\,\tfrac{1}{\sqrt 2}(\vert 01\rangle - \vert 10\rangle) = \tfrac{1}{\sqrt 2}(\vert 10\rangle - \vert 01\rangle) = -\tfrac{1}{\sqrt 2}(\vert 01\rangle - \vert 10\rangle)$: eigenvalue $-1$.

The **symmetric** ($+1$) eigenspace is 3-dimensional, spanned by $\{\vert 00\rangle, \vert 11\rangle, \tfrac{1}{\sqrt 2}(\vert 01\rangle + \vert 10\rangle)\}$. The **antisymmetric** ($-1$) eigenspace is 1-dimensional, spanned by $\{\tfrac{1}{\sqrt 2}(\vert 01\rangle - \vert 10\rangle)\}$. Dimension count: $3 + 1 = 4 = \dim(\mathbb C^2\otimes\mathbb C^2)$. ✓

The eigenspaces correspond exactly to the **triplet** (symmetric, 3-d) and **singlet** (antisymmetric, 1-d) of two-qubit angular momentum — and they will reappear naturally in 2.1.2 (Symmetrization) as the boson and fermion sectors.

(d) **Verification of the Pauli-string formula.** Build each term and sum. Using the matrices computed in Problem 6 and elsewhere:

- $\hat I\otimes\hat I = \mathrm{diag}(1,1,1,1)$
- $\hat X\otimes\hat X$ has $1$ at the four anti-diagonal positions $(1,4), (2,3), (3,2), (4,1)$
- $\hat Y\otimes\hat Y$ has $-1$ at $(1,4)$ and $(4,1)$, and $+1$ at $(2,3)$ and $(3,2)$
- $\hat Z\otimes\hat Z = \mathrm{diag}(1,-1,-1,1)$

Sum entry by entry. The diagonal $(1,1) = 1 + 0 + 0 + 1 = 2$. Diagonal $(2,2) = 1 + 0 + 0 + (-1) = 0$. Diagonal $(3,3) = 0$, $(4,4) = 2$. Off-diagonal $(1,4) = 0 + 1 + (-1) + 0 = 0$ and $(4,1) = 0$. Off-diagonal $(2,3) = 0 + 1 + 1 + 0 = 2$ and $(3,2) = 2$. All other entries vanish.

Dividing by $2$:

$$
\tfrac{1}{2}\bigl(\hat I\otimes\hat I + \hat X\otimes\hat X + \hat Y\otimes\hat Y + \hat Z\otimes\hat Z\bigr) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \hat S. \quad\checkmark
$$

This decomposition is the operator-level statement of the **identity for the swap of two spin-1/2 particles**, $\hat S = \tfrac{1}{2}(\hat I + \hat\sigma_1\cdot\hat\sigma_2)$ — where $\hat\sigma_1\cdot\hat\sigma_2 = \sum_a \hat\sigma_1^a\hat\sigma_2^a$. It connects directly to the Heisenberg interaction of Problem 6: a Heisenberg coupling is essentially "twice the SWAP minus the identity," and its symmetric/antisymmetric eigenstates are exactly the SWAP eigenstates (triplet/singlet).

<!-- ─── -->

**4. Expectation in product states.** For a product state $\vert\psi\rangle = \vert\psi_A\rangle \otimes \vert\psi_B\rangle$, prove that

$$
\langle\psi\vert\,(\hat A\otimes\hat B)\,\vert\psi\rangle = \langle\psi_A\vert\hat A\vert\psi_A\rangle\,\langle\psi_B\vert\hat B\vert\psi_B\rangle.
$$

Explain in one sentence what physical statement this factorization expresses, and why it must **fail** for entangled states.

**Solution.**

Three facts about tensor products are needed.

*(i) Bra of a product factorizes.* From $\vert\psi\rangle = \vert\psi_A\rangle\otimes\vert\psi_B\rangle$,

$$
\langle\psi\vert = \bigl(\vert\psi_A\rangle\otimes\vert\psi_B\rangle\bigr)^\dagger = \langle\psi_A\vert\otimes\langle\psi_B\vert.
$$

*(ii) Mixed-product rule on a product ket:*

$$
(\hat A\otimes\hat B)\bigl(\vert\psi_A\rangle\otimes\vert\psi_B\rangle\bigr) = (\hat A\vert\psi_A\rangle)\otimes(\hat B\vert\psi_B\rangle).
$$

*(iii) Tensor-product inner product factorizes:*

$$
\bigl(\langle\phi_A\vert\otimes\langle\phi_B\vert\bigr)\bigl(\vert\chi_A\rangle\otimes\vert\chi_B\rangle\bigr) = \langle\phi_A\vert\chi_A\rangle\,\langle\phi_B\vert\chi_B\rangle.
$$

Combine: apply (ii) to the ket, (i) to the bra, then (iii):

$$
\langle\psi\vert(\hat A\otimes\hat B)\vert\psi\rangle = \bigl(\langle\psi_A\vert\otimes\langle\psi_B\vert\bigr)\bigl[(\hat A\vert\psi_A\rangle)\otimes(\hat B\vert\psi_B\rangle)\bigr] = \langle\psi_A\vert\hat A\vert\psi_A\rangle\,\langle\psi_B\vert\hat B\vert\psi_B\rangle. \quad\checkmark
$$

**Physical meaning.** In a product state, the joint expectation $\langle\hat A\otimes\hat B\rangle$ equals the *product* of the two local expectations $\langle\hat A\rangle_A\langle\hat B\rangle_B$: the measurements on A and on B are **statistically independent**, with no correlations between them. There are no joint statistics that cannot be reconstructed from the two single-particle distributions.

For an **entangled** state this factorization **fails**: there exist observables $\hat A,\hat B$ for which $\langle\hat A\otimes\hat B\rangle \neq \langle\hat A\rangle\langle\hat B\rangle$ on the entangled state. Problem 5(d) computes the explicit case for $\vert\Phi^+\rangle = (\vert 00\rangle + \vert 11\rangle)/\sqrt 2$: $\langle\hat Z_1\rangle = \langle\hat Z_2\rangle = 0$ separately, but $\langle\hat Z_1\hat Z_2\rangle = +1$ — perfect correlation despite individually random measurements. The non-factorization of joint expectation values is the operational signature of entanglement.

<!-- ─── -->

**5. Single-body and two-body Z measurements.** For two qubits, define the single-body observables $\hat Z_1 = \hat Z\otimes\hat I$ and $\hat Z_2 = \hat I\otimes\hat Z$, and the two-body observable $\hat Z_1\hat Z_2 = \hat Z\otimes\hat Z$.

(a) Show $[\hat Z_1, \hat Z_2] = 0$ using the mixed-product rule. State physically why operators on different particles always commute.

(b) Find the four simultaneous eigenstates of $\hat Z_1$ and $\hat Z_2$. State their $(\hat Z_1, \hat Z_2)$ eigenvalue pairs.

(c) Show $[\hat Z_1, \hat Z_1\hat Z_2] = 0$. Identify the eigenvalues of $\hat Z_1\hat Z_2$ and explain physically: $\hat Z_1\hat Z_2$ measures the **parity** $(-1)^{n_0+n_1}$ where $n_i$ is the result of measuring $\hat Z_i = +1 \to n_i = 0$, $\hat Z_i = -1 \to n_i = 1$.

(d) For the **entangled** state $\vert\Phi^+\rangle = \tfrac{1}{\sqrt 2}(\vert 00\rangle + \vert 11\rangle)$ (from Problem 1(b)), compute $\langle\hat Z_1\rangle$, $\langle\hat Z_2\rangle$, and $\langle\hat Z_1\hat Z_2\rangle$. Interpret the result: individual $\hat Z$-measurements are random ($\langle\hat Z_i\rangle = 0$), but the parity $\hat Z_1\hat Z_2$ is *deterministic*. Why does this contradict the product-state factorization rule of Problem 4?

**Solution.**

(a) Mixed-product rule:

$$
\hat Z_1\hat Z_2 = (\hat Z\otimes\hat I)(\hat I\otimes\hat Z) = (\hat Z\hat I)\otimes(\hat I\hat Z) = \hat Z\otimes\hat Z,
$$

$$
\hat Z_2\hat Z_1 = (\hat I\otimes\hat Z)(\hat Z\otimes\hat I) = (\hat I\hat Z)\otimes(\hat Z\hat I) = \hat Z\otimes\hat Z.
$$

The two products are equal, so $[\hat Z_1, \hat Z_2] = 0$. Physically, operators carrying $\hat Z$ on qubit 1 and qubit 2 act on *different tensor factors*; multiplication in different slots commutes because each slot independently uses $\hat Z\cdot\hat I = \hat I\cdot\hat Z = \hat Z$.

(b) The four computational basis states are simultaneous eigenstates: $\hat Z\vert i\rangle = (1-2i)\vert i\rangle$ gives eigenvalue $+1$ for $\vert 0\rangle$ and $-1$ for $\vert 1\rangle$. So

| State | $\hat Z_1$ | $\hat Z_2$ |
|---|---|---|
| $\vert 00\rangle$ | $+1$ | $+1$ |
| $\vert 01\rangle$ | $+1$ | $-1$ |
| $\vert 10\rangle$ | $-1$ | $+1$ |
| $\vert 11\rangle$ | $-1$ | $-1$ |

(c) Since $\hat Z_1$ and $\hat Z_2$ commute, $\hat Z_1$ commutes with any function of them, including their product. Explicitly $[\hat Z_1, \hat Z_1\hat Z_2] = \hat Z_1[\hat Z_1, \hat Z_2] + [\hat Z_1, \hat Z_1]\hat Z_2 = 0$.

The eigenvalue of $\hat Z_1\hat Z_2$ on $\vert ab\rangle$ is the product of the individual eigenvalues: $+1$ for $\vert 00\rangle$ and $\vert 11\rangle$ (both qubits the same), $-1$ for $\vert 01\rangle$ and $\vert 10\rangle$ (qubits opposite). So $\hat Z_1\hat Z_2$ has eigenvalues $\{+1, +1, -1, -1\}$ — **two doubly-degenerate sectors**.

This is the **parity** observable: it returns $+1$ when both qubits are in the same state ($\vert 00\rangle$ or $\vert 11\rangle$, $n_0 + n_1$ even) and $-1$ when they differ ($\vert 01\rangle$ or $\vert 10\rangle$, $n_0 + n_1$ odd). Parity is a single bit of *correlation* information that the joint measurement extracts; it does not specify which of the two same-parity states the system is in.

(d) On $\vert\Phi^+\rangle = \tfrac{1}{\sqrt 2}(\vert 00\rangle + \vert 11\rangle)$, the $\hat Z_1$ outcomes are $+1$ (from $\vert 00\rangle$) and $-1$ (from $\vert 11\rangle$) with probability $\tfrac{1}{2}$ each. So

$$
\langle\hat Z_1\rangle = (\tfrac{1}{2})(+1) + (\tfrac{1}{2})(-1) = 0, \quad \langle\hat Z_2\rangle = 0\ \text{(by symmetry)}.
$$

But the *parity* is **always $+1$** on $\vert\Phi^+\rangle$: both $\vert 00\rangle$ and $\vert 11\rangle$ have $\hat Z_1\hat Z_2 = +1$. So

$$
\langle\hat Z_1\hat Z_2\rangle = +1.
$$

**Contradiction with product-state factorization.** If $\vert\Phi^+\rangle$ were a product state, Problem 4 would force $\langle\hat Z_1\hat Z_2\rangle = \langle\hat Z_1\rangle\langle\hat Z_2\rangle = 0\cdot 0 = 0$. The actual value is $+1$ — a glaring violation of factorization. This is the operational signature of **entanglement**: the two qubits' individual measurements are random, but their *correlation* is deterministic. **The joint expectation value cannot be recovered from the local expectations alone**, because the state carries information about the correlation that no single-particle description can capture. This is the foundation of every entangled-state-based protocol in quantum information, and it shows up here directly from the lecture's tensor-product machinery.

<!-- ─── -->

**6. Heisenberg interaction matrix.** The Heisenberg interaction is $\hat{H} = J(\hat{X}\otimes\hat{X} + \hat{Y}\otimes\hat{Y} + \hat{Z}\otimes\hat{Z})$.

(a) Write $\hat{H}$ as a $4\times 4$ matrix.

(b) How many Pauli strings appear?

**Solution.**

(a) Build each two-qubit Pauli string as a Kronecker product in the ordered basis $\{\vert 00\rangle, \vert 01\rangle, \vert 10\rangle, \vert 11\rangle\}$. With $\hat X = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$, $\hat Y = \begin{pmatrix}0 & -\mathrm{i} \\ \mathrm{i} & 0\end{pmatrix}$, $\hat Z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$:

$$
\hat X\otimes\hat X = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}, \qquad \hat Y\otimes\hat Y = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix},
$$

$$
\hat Z\otimes\hat Z = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
$$

(For $\hat Y\otimes\hat Y$ the corner entries are $(-\mathrm{i})(-\mathrm{i}) = -1$ and $(\mathrm{i})(\mathrm{i}) = -1$, while the central entries are $(-\mathrm{i})(\mathrm{i}) = +1$.) Adding the three and multiplying by $J$:

$$
\hat H = J\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 2 & 0 \\ 0 & 2 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
$$

The off-diagonal $2J$ in the central block comes from $\hat X\otimes\hat X$ and $\hat Y\otimes\hat Y$ (each contributes $+1$ there); in the corner entries those same two strings cancel ($+1$ from $\hat X\otimes\hat X$, $-1$ from $\hat Y\otimes\hat Y$). Diagonalising the central block $\begin{pmatrix}-1 & 2 \\ 2 & -1\end{pmatrix}$ gives eigenvalues $-1 \pm 2 \in \{+1, -3\}$, so $\hat H$ has spectrum $J\{+1, +1, +1, -3\}$: a three-fold-degenerate **triplet** at energy $+J$ (the states $\vert 00\rangle$, $\vert 11\rangle$, and $(\vert 01\rangle + \vert 10\rangle)/\sqrt 2$) and a **singlet** at $-3J$ (the antisymmetric $(\vert 01\rangle - \vert 10\rangle)/\sqrt 2$). The triplet/singlet structure is exactly the SWAP eigenspace structure of Problem 3 — this is the origin of magnetic ordering in the Heisenberg model.

(b) **Three Pauli strings appear:** $\hat X\otimes\hat X$, $\hat Y\otimes\hat Y$, and $\hat Z\otimes\hat Z$, each with the real coefficient $J$. Every term is a genuine two-qubit Pauli string — a tensor product of single-qubit Paulis, here with no identity factor. For comparison, a *general* Hermitian operator on two qubits needs up to $4^2 = 16$ Pauli strings; the Heisenberg Hamiltonian uses only $3$ because it is highly constrained: isotropic (the three axes enter symmetrically), traceless, and purely an interaction (no single-body terms of the form $\hat I\otimes\hat\sigma$ or $\hat\sigma\otimes\hat I$).

<!-- ─── -->

**7. Pauli string decomposition.** Decompose $\vert 00\rangle\langle 00\vert$ into Pauli strings $\hat\sigma_1^{s_1}\otimes\hat\sigma_2^{s_2}$ with $\hat\sigma^s\in\{\hat I, \hat X, \hat Y, \hat Z\}$.

(a) Use the single-qubit identity $\vert 0\rangle\langle 0\vert = \tfrac{1}{2}(\hat I + \hat Z)$ and tensor-product factorization to expand $\vert 00\rangle\langle 00\vert$ in the 16-term Pauli basis. How many strings have non-zero coefficient?

(b) Verify (a) independently using the trace-projection formula $c_{s_1 s_2} = \tfrac{1}{4}\operatorname{Tr}\!\bigl[(\hat\sigma^{s_1}\otimes\hat\sigma^{s_2})\,\vert 00\rangle\langle 00\vert\bigr]$ (from 1.1.3 P5, generalised to two qubits).

(c) Generalise: what are the non-zero Pauli-string coefficients for a 2-qubit projector $\vert ij\rangle\langle ij\vert$ in general?

**Solution.**

(a) Start from $\vert 0\rangle\langle 0\vert = \tfrac{1}{2}(\hat I + \hat Z)$, verifiable by direct matrix sum: $\tfrac{1}{2}(\hat I + \hat Z) = \tfrac{1}{2}\bigl(\begin{smallmatrix}1 & 0 \\ 0 & 1\end{smallmatrix}\bigr) + \tfrac{1}{2}\bigl(\begin{smallmatrix}1 & 0 \\ 0 & -1\end{smallmatrix}\bigr) = \bigl(\begin{smallmatrix}1 & 0 \\ 0 & 0\end{smallmatrix}\bigr) = \vert 0\rangle\langle 0\vert$.

The two-qubit projector factorizes:

$$
\vert 00\rangle\langle 00\vert = (\vert 0\rangle\langle 0\vert)\otimes(\vert 0\rangle\langle 0\vert) = \tfrac{1}{2}(\hat I + \hat Z)\otimes\tfrac{1}{2}(\hat I + \hat Z).
$$

Expanding by bilinearity of $\otimes$:

$$
\vert 00\rangle\langle 00\vert = \tfrac{1}{4}\bigl(\hat I\otimes\hat I + \hat I\otimes\hat Z + \hat Z\otimes\hat I + \hat Z\otimes\hat Z\bigr).
$$

Exactly **four Pauli strings** have non-zero coefficient: $\hat I\otimes\hat I$, $\hat I\otimes\hat Z$, $\hat Z\otimes\hat I$, $\hat Z\otimes\hat Z$, each with coefficient $\tfrac{1}{4}$. All 12 strings containing $\hat X$ or $\hat Y$ have coefficient zero.

(b) Apply the trace-projection formula. Using $\operatorname{Tr}(\vert 00\rangle\langle 00\vert\cdot\hat O) = \langle 00\vert\hat O\vert 00\rangle$,

$$
c_{s_1 s_2} = \tfrac{1}{4}\langle 00\vert(\hat\sigma^{s_1}\otimes\hat\sigma^{s_2})\vert 00\rangle = \tfrac{1}{4}\langle 0\vert\hat\sigma^{s_1}\vert 0\rangle\,\langle 0\vert\hat\sigma^{s_2}\vert 0\rangle.
$$

The diagonal matrix element $\langle 0\vert\hat\sigma\vert 0\rangle$ equals $1$ for $\hat\sigma\in\{\hat I, \hat Z\}$ (both diagonal with $1$ in the upper-left), and $0$ for $\hat\sigma\in\{\hat X, \hat Y\}$ (zero diagonal entries in the Z basis). So $c_{s_1 s_2}$ is non-zero only when *both* $\hat\sigma^{s_1}$ and $\hat\sigma^{s_2}$ are in $\{\hat I, \hat Z\}$, yielding the four coefficients $\tfrac{1}{4}\cdot 1\cdot 1 = \tfrac{1}{4}$ — matching (a). $\checkmark$

(c) For a general $\vert ij\rangle\langle ij\vert$ with $i, j\in\{0, 1\}$, the factorization is $\vert i\rangle\langle i\vert\otimes\vert j\rangle\langle j\vert$ with $\vert k\rangle\langle k\vert = \tfrac{1}{2}(\hat I + (-1)^k\hat Z) = \tfrac{1}{2}(\hat I + \langle\hat Z\rangle_k\hat Z)$. So

$$
\vert ij\rangle\langle ij\vert = \tfrac{1}{4}\bigl[\hat I\otimes\hat I + (-1)^j\hat I\otimes\hat Z + (-1)^i\hat Z\otimes\hat I + (-1)^{i+j}\hat Z\otimes\hat Z\bigr].
$$

Always **four** non-zero Pauli strings (the diagonal $\{I, Z\}\otimes\{I, Z\}$ block), with $\pm\tfrac{1}{4}$ coefficients determined by the signs $(-1)^i, (-1)^j$. Computational-basis projectors always live in the diagonal $\{I, Z\}^{\otimes 2}$ sector — a general principle: the Pauli-string expansion of any operator diagonal in the computational basis is supported entirely on tensor products of $\hat I$ and $\hat Z$.

<!-- ─── -->

**8. Hilbert-space parametrization.** For $N$ qubits, how many independent real parameters specify

(a) a general normalized state in $(\mathbb{C}^2)^{\otimes N}$, and

(b) a normalized product state $\vert\psi_1\rangle\otimes\cdots\otimes\vert\psi_N\rangle$?

(c) What does the difference between (a) and (b) represent physically? Tabulate the two counts for $N = 1, 2, 3, 10$ to illustrate the scaling.

**Solution.**

(a) A general $N$-qubit state lives in $(\mathbb{C}^2)^{\otimes N} = \mathbb{C}^{2^N}$, so it is specified by $2^N$ complex amplitudes — that is, $2\cdot 2^N = 2^{N+1}$ real numbers. Two constraints cut this count:

- Normalization $\sum\vert\Psi_{\alpha_1\cdots\alpha_N}\vert^2 = 1$ removes $1$ real parameter.
- The global phase is unobservable, removing $1$ more.

Hence a general normalized $N$-qubit state carries

$$
2^{N+1} - 2 \quad\text{independent real parameters.}
$$

(This is the $n$-level count $2n - 2$ from 1.1.2 Problem 8, evaluated at $n = 2^N$. Check $N = 1$: $2^2 - 2 = 2$, the two Bloch-sphere angles $(\theta, \varphi)$.)

(b) A product state $\vert\psi_1\rangle\otimes\cdots\otimes\vert\psi_N\rangle$ is fixed by choosing each single-qubit factor independently. Each factor is a normalized qubit state — a Bloch-sphere point — carrying $2^{1+1} - 2 = 2$ real parameters. With $N$ independent factors:

$$
2N \quad\text{independent real parameters.}
$$

(Phase subtlety: each factor carries its own phase freedom, but a rephasing $\vert\psi_k\rangle\to\mathrm{e}^{\mathrm{i}\phi_k}\vert\psi_k\rangle$ multiplies the whole product by $\mathrm{e}^{\mathrm{i}(\phi_1 + \cdots + \phi_N)}$ — a single global phase. So $N$ per-factor phases collapse into one unphysical global phase; counting each factor as a Bloch-sphere point already accounts for this correctly.)

(c) The difference

$$
\Delta(N) = \bigl(2^{N+1} - 2\bigr) - 2N
$$

is the number of parameters a general state carries **beyond** anything a product state can reach. These "extra" parameters describe **entanglement** — correlations not attributable to any single particle. As $N$ grows, product-state parameters scale *linearly* ($2N$), while the full count scales *exponentially* ($2^{N+1} - 2$); entangled states overwhelmingly dominate the Hilbert space, and product states become an exponentially thin slice.

| $N$ | Full state $2^{N+1} - 2$ | Product state $2N$ | Entanglement $\Delta$ |
|---|---|---|---|
| 1 | 2 | 2 | 0 |
| 2 | 6 | 4 | 2 |
| 3 | 14 | 6 | 8 |
| 10 | 2046 | 20 | 2026 |

For a single qubit ($N=1$), there is no second particle to entangle with, so $\Delta = 0$. From $N = 2$ onward, the entanglement count strictly exceeds the product count, and at $N = 10$ the entanglement degrees of freedom outnumber product-state parameters by a factor of $\sim 100$. This **exponential separation** is the central computational resource of quantum information — a classical description of the state would require listing all $2^{N+1} - 2$ parameters, whereas a product state only $2N$. Quantum dynamics in the entangled sector is precisely the dynamics that cannot be efficiently simulated by classical bookkeeping of single-particle states.
