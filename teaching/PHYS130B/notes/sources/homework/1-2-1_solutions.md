# 1.2.1 Measurement Postulate
Worked solutions for the homework problems in the [1.2.1 Measurement Postulate](../ch1_qubit/1-2-1-measurement-postulate) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Measurement probabilities and collapse.** A qubit is in the state $\vert\psi\rangle = \dfrac{2\vert 0\rangle + \sqrt{5}\vert 1\rangle}{3}$. Measure $\hat{Z}$.

(a) Compute $P(+1)$ and $P(-1)$ from the Born rule. Verify the probabilities sum to $1$.

(b) Write the state immediately after obtaining outcome $-1$, and explain in one sentence why the pre-measurement amplitudes $c_0, c_1$ play no further role in subsequent dynamics.

**Solution.**

Write $\vert\psi\rangle = c_0\vert 0\rangle + c_1\vert 1\rangle$ with $c_0 = 2/3$ and $c_1 = \sqrt 5/3$. Normalization: $\vert c_0\vert^2 + \vert c_1\vert^2 = \tfrac{4}{9} + \tfrac{5}{9} = 1$. ✓

(a) Born's rule gives the probability of outcome $m$ as the squared overlap with the corresponding eigenstate of $\hat Z$:

$$
P(+1) = \vert\langle 0\vert\psi\rangle\vert^2 = \vert c_0\vert^2 = \frac{4}{9}, \qquad P(-1) = \vert\langle 1\vert\psi\rangle\vert^2 = \vert c_1\vert^2 = \frac{5}{9}.
$$

Sum: $\tfrac{4}{9} + \tfrac{5}{9} = 1$. ✓

(b) By the collapse axiom, the post-measurement state is the eigenstate selected by the outcome:

$$
\vert\psi\rangle \xrightarrow[\text{measure }\hat Z]{\text{outcome } -1} \vert 1\rangle.
$$

The pre-measurement amplitudes $c_0, c_1$ are erased entirely — they only entered through Born-rule **probabilities**, which were drawn from once and then discarded. From this moment on, the system is in $\vert 1\rangle$, and an immediately repeated $\hat Z$ measurement would return $-1$ with certainty (Born rule on $\vert 1\rangle$: $\vert\langle 1\vert 1\rangle\vert^2 = 1$).

<!-- ─── -->

**2. Sequential measurements and filters.** Start with the state $\vert+\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)$.

(a) Measure $\hat{Z}$: find the probabilities and the post-measurement state for each outcome.

(b) Immediately after measuring $\hat{Z}$ and obtaining outcome $+1$, measure $\hat{X}$. What are the outcome probabilities now?

(c) Compare with measuring $\hat{X}$ directly on the original $\vert+\rangle$. Explain in one sentence why the two procedures give different $\hat{X}$ statistics — using the language of the lecture's Z-X-Z experiment.

**Solution.**

(a) $\hat Z$ on $\vert+\rangle$. The amplitudes of $\vert+\rangle$ in the $\hat Z$ basis are both $1/\sqrt{2}$, so

$$
P(+1) = \vert\langle 0\vert+\rangle\vert^2 = \tfrac{1}{2}, \qquad P(-1) = \vert\langle 1\vert+\rangle\vert^2 = \tfrac{1}{2}.
$$

Post-measurement: $\vert 0\rangle$ (outcome $+1$) or $\vert 1\rangle$ (outcome $-1$).

(b) Then $\hat X$, conditioned on the $+1$ branch. The state is now $\vert 0\rangle = \tfrac{1}{\sqrt{2}}(\vert+\rangle + \vert-\rangle)$, so

$$
P(+1) = \vert\langle+\vert 0\rangle\vert^2 = \tfrac{1}{2}, \qquad P(-1) = \vert\langle-\vert 0\rangle\vert^2 = \tfrac{1}{2}.
$$

A fair coin flip.

(c) Direct $\hat X$ on $\vert+\rangle$: the state is itself the $+1$ eigenstate of $\hat X$, so $P(+1) = 1$ and $P(-1) = 0$ — a deterministic outcome. The intervening $\hat Z$ measurement collapsed the $\hat X$-definite state $\vert+\rangle$ into $\vert 0\rangle$, which is in turn an equal-weight superposition in the $\hat X$ basis. Because $\hat Z$ and $\hat X$ are **incompatible**, measuring $\hat Z$ is not a passive readout — it rewrites the state, erasing the prior $\hat X$-definiteness. This is exactly the lecture's Z-X-Z behaviour: an incompatible measurement inserted in the middle destroys the original observable's sharpness.

<!-- ─── -->

**3. Measurement of a non-Pauli observable.** Consider the Hermitian observable $\hat{H} = \omega\,\hat{X} + \Delta\,\hat{Z}$ from 1.1.3 Problem 1, with $\omega, \Delta > 0$. Its eigenvalues are $E_\pm = \pm\Omega$ where $\Omega = \sqrt{\omega^2 + \Delta^2}$, and its eigenstates parametrise the Bloch axis with mixing angle $\theta_0$ defined by $\tan\theta_0 = \omega/\Delta$:

$$
\vert E_+\rangle = \cos(\theta_0/2)\,\vert 0\rangle + \sin(\theta_0/2)\,\vert 1\rangle, \qquad \vert E_-\rangle = \sin(\theta_0/2)\,\vert 0\rangle - \cos(\theta_0/2)\,\vert 1\rangle.
$$

A system is prepared in $\vert 0\rangle$ and one measures $\hat H$.

(a) List the possible outcomes.

(b) Compute the probability of each outcome. Express the answer as a function of $\Delta/\Omega$.

(c) Write the post-measurement state for each outcome.

(d) Compute $\langle\hat H\rangle$ on the prepared state $\vert 0\rangle$ in two ways — directly from $\langle 0\vert\hat H\vert 0\rangle$, and via the spectral sum $\sum_m m\,P(m)$ — and verify they agree.

**Solution.**

(a) The only possible outcomes are the eigenvalues of $\hat H$: $E_+ = +\Omega$ and $E_- = -\Omega$.

(b) By the Born rule, the probabilities are the squared overlaps with the eigenstates of $\hat H$:

$$
P(E_+) = \vert\langle E_+\vert 0\rangle\vert^2 = \cos^2(\theta_0/2) = \tfrac{1+\cos\theta_0}{2} = \tfrac{1}{2}\!\left(1 + \tfrac{\Delta}{\Omega}\right),
$$

$$
P(E_-) = \vert\langle E_-\vert 0\rangle\vert^2 = \sin^2(\theta_0/2) = \tfrac{1-\cos\theta_0}{2} = \tfrac{1}{2}\!\left(1 - \tfrac{\Delta}{\Omega}\right),
$$

using $\cos\theta_0 = \Delta/\Omega$ from the mixing-angle definition. Both probabilities are non-negative and sum to $1$. ✓

(c) Collapse to the eigenstate selected by the outcome: $\vert E_+\rangle$ or $\vert E_-\rangle$ as written above.

(d) Direct expectation:

$$
\langle 0\vert\hat H\vert 0\rangle = \langle 0\vert\,(\omega\hat X + \Delta\hat Z)\,\vert 0\rangle = \omega\,\langle 0\vert\hat X\vert 0\rangle + \Delta\,\langle 0\vert\hat Z\vert 0\rangle = \omega(0) + \Delta(1) = \Delta.
$$

Spectral sum:

$$
\sum_m m\,P(m) = (+\Omega)\cdot\tfrac{1}{2}\!\left(1 + \tfrac{\Delta}{\Omega}\right) + (-\Omega)\cdot\tfrac{1}{2}\!\left(1 - \tfrac{\Delta}{\Omega}\right) = \tfrac{\Omega + \Delta}{2} - \tfrac{\Omega - \Delta}{2} = \Delta. \quad\checkmark
$$

Both methods give $\Delta$. The agreement is general: spectral decomposition of $\hat H$ + Born rule + linearity of expectation guarantee $\langle\hat O\rangle = \sum_m m\,P(m)$ for *every* Hermitian observable and *every* state — this is the operational content of the spectral theorem.

<!-- ─── -->

**4. State inference from measurement frequencies.** An unknown qubit state $\vert\psi\rangle$ is prepared on many identical copies. Measuring the three Pauli observables on these copies yields the relative frequencies

$$
\begin{array}{l|cc}
\text{basis} & f(+1) & f(-1) \\
\hline
\hat Z & 0.70 & 0.30 \\
\hat X & 0.96 & 0.04 \\
\hat Y & 0.50 & 0.50 \\
\end{array}
$$

In the limit of infinitely many copies these frequencies equal the Born-rule probabilities. Assume this limit and reconstruct $\vert\psi\rangle$.

(a) Compute the Bloch vector $\boldsymbol n = (\langle\hat X\rangle, \langle\hat Y\rangle, \langle\hat Z\rangle)$. (Recall $\langle\hat O\rangle = P(+1) - P(-1)$ for Pauli $\hat O$.)

(b) Verify $\vert\boldsymbol n\vert = 1$, consistent with the assumption that the source produces a pure state.

(c) Convert the Bloch vector to Bloch angles $(\theta, \varphi)$ and write the state in the standard form

$$
\vert\psi\rangle = \cos(\theta/2)\,\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\,\sin(\theta/2)\,\vert 1\rangle.
$$

(d) Two of the three measurement bases give relative frequencies close to $0$ or $1$, while the third gives an equal split. Identify which Bloch-sphere axis the state's Bloch vector lies closest to, and explain in one sentence why a measurement along that axis would have made the inference unambiguous from a single basis.

**Solution.**

(a) The Pauli expectation values are differences of $\pm 1$ probabilities:

$$
\langle\hat X\rangle = 0.96 - 0.04 = 0.92, \quad \langle\hat Y\rangle = 0.50 - 0.50 = 0, \quad \langle\hat Z\rangle = 0.70 - 0.30 = 0.40.
$$

So $\boldsymbol n = (0.92,\, 0,\, 0.40)$.

(b) $\vert\boldsymbol n\vert^2 = 0.92^2 + 0 + 0.40^2 = 0.8464 + 0.1600 = 1.0064 \approx 1$. The small departure from $1$ is consistent with finite-sample statistical noise in the measured frequencies; in the infinite-copy limit assumed, the state is pure.

(c) From $\boldsymbol n = (\sin\theta\cos\varphi,\, \sin\theta\sin\varphi,\, \cos\theta)$:

- $\cos\theta = n_z = 0.40$ gives $\theta \approx 66.4^\circ$.
- $\sin\theta = \sqrt{1 - 0.16} \approx 0.917$ (positive root, since $\theta\in[0,\pi]$).
- $\sin\theta\sin\varphi = n_y = 0$ together with $\sin\theta > 0$ gives $\sin\varphi = 0$, so $\varphi = 0$ or $\pi$.
- $\sin\theta\cos\varphi = n_x = 0.92 > 0$ together with $\sin\theta > 0$ gives $\cos\varphi > 0$, so $\varphi = 0$.

The standard-form state is

$$
\vert\psi\rangle = \cos(33.2^\circ)\,\vert 0\rangle + \sin(33.2^\circ)\,\vert 1\rangle \approx 0.836\,\vert 0\rangle + 0.548\,\vert 1\rangle.
$$

(d) The Bloch vector $\boldsymbol n = (0.92, 0, 0.40)$ lies in the $xz$-plane and is closest to the $\boldsymbol{e}_x$ axis (the $n_x$ component is by far the largest). The fact that the $\hat X$ measurement gave the most lopsided frequencies — close to $96\%$ for outcome $+1$ — is exactly the diagnostic: the measurement axis nearly aligned with the Bloch vector gives a near-deterministic outcome. A measurement along $\boldsymbol{n}$ itself would give $P(+1) = 1$, $P(-1) = 0$, allowing the state to be identified from a single outcome — but that requires *already knowing* $\boldsymbol{n}$, which is what the three Pauli measurements together pin down.

<!-- ─── -->

**5. Phase erasure by complementary measurement.** A qubit is prepared in the general Bloch state $\vert\psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$. Consider two scenarios for measuring $\hat X$:

- **Scenario A (direct):** Measure $\hat X$ directly on $\vert\psi\rangle$.
- **Scenario B (preceded by $\hat Z$):** First measure $\hat Z$ (record the outcome but do not post-select); the system collapses to one of $\vert 0\rangle$ or $\vert 1\rangle$. Then measure $\hat X$ on the collapsed state.

(a) Compute $P_A(\hat X = +1)$ for Scenario A. Express the answer in terms of $\theta$ and $\varphi$.

(b) Compute $P_B(\hat X = +1)$ for Scenario B, marginalising over the (unobserved) Z outcome:

$$
P_B(\hat X = +1) = \sum_{m_1 = \pm 1} P(\hat Z = m_1)\,P(\hat X = +1\,\vert\,\text{post-}\hat Z\text{ state}).
$$

Show that $P_B(\hat X = +1) = 1/2$ — independent of $\theta$ and $\varphi$.

(c) Subtract: the difference between the two scenarios is $P_A - P_B = \tfrac{1}{2}\sin\theta\cos\varphi$. Identify which part of the initial state's Bloch vector controls this difference, and explain in one sentence why the intervening $\hat Z$ measurement *erased* this contribution.

(d) For which initial Bloch directions is the erasure ineffective ($P_A = P_B$)? Identify those locations on the Bloch sphere and explain physically why the $\hat Z$ measurement leaves them untouched.

**Solution.**

(a) Write $c_0 = \cos(\theta/2)$ and $c_1 = \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)$. The $+1$ amplitude in the $\hat X$ basis is $\langle +\vert\psi\rangle = (c_0 + c_1)/\sqrt 2$, so

$$
P_A(\hat X = +1) = \tfrac{1}{2}\vert c_0 + c_1\vert^2 = \tfrac{1}{2}\bigl(\vert c_0\vert^2 + \vert c_1\vert^2 + 2\operatorname{Re}(c_0^* c_1)\bigr) = \tfrac{1}{2}\bigl(1 + 2\operatorname{Re}(c_0^* c_1)\bigr).
$$

Compute $c_0^* c_1 = \cos(\theta/2)\,\mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2) = \tfrac{1}{2}\mathrm{e}^{\mathrm{i}\varphi}\sin\theta$, so $\operatorname{Re}(c_0^* c_1) = \tfrac{1}{2}\sin\theta\cos\varphi$. Therefore

$$
P_A(\hat X = +1) = \tfrac{1}{2}\bigl(1 + \sin\theta\cos\varphi\bigr).
$$

(Sanity check: this is $(1 + n_x)/2$, the lecture's Bloch-vector probability formula along the $\boldsymbol{e}_x$ axis — Problem 6 of 1.1.2.)

(b) The Z outcome has probability $P(\hat Z = +1) = \vert c_0\vert^2 = \cos^2(\theta/2)$ (collapses to $\vert 0\rangle$) and $P(\hat Z = -1) = \vert c_1\vert^2 = \sin^2(\theta/2)$ (collapses to $\vert 1\rangle$). From either collapsed state, the $\hat X$-basis distribution is uniform:

$$
\vert 0\rangle = \tfrac{1}{\sqrt 2}(\vert+\rangle + \vert-\rangle) \;\Rightarrow\; P(\hat X = +1\,\vert\,\vert 0\rangle) = \tfrac{1}{2},
$$

$$
\vert 1\rangle = \tfrac{1}{\sqrt 2}(\vert+\rangle - \vert-\rangle) \;\Rightarrow\; P(\hat X = +1\,\vert\,\vert 1\rangle) = \tfrac{1}{2}.
$$

Marginalising:

$$
P_B(\hat X = +1) = \cos^2(\theta/2)\cdot\tfrac{1}{2} + \sin^2(\theta/2)\cdot\tfrac{1}{2} = \tfrac{1}{2}\bigl(\cos^2(\theta/2) + \sin^2(\theta/2)\bigr) = \tfrac{1}{2}. \quad\checkmark
$$

Regardless of $\theta$ and $\varphi$, the post-$\hat Z$ $\hat X$-distribution is a fair coin.

(c) Subtracting,

$$
P_A - P_B = \tfrac{1}{2}(1 + \sin\theta\cos\varphi) - \tfrac{1}{2} = \tfrac{1}{2}\sin\theta\cos\varphi = \tfrac{1}{2}\,n_x,
$$

where $n_x$ is the $x$-component of the initial Bloch vector. The Z measurement *erased the entire $\hat X$-projection* of the initial Bloch vector. Physically, the Z measurement collapses the state into an eigenstate of $\hat Z$, both of which sit on the *z-axis* of the Bloch sphere (the equator-perpendicular pair) — so after collapse the Bloch vector has $n_x = 0$, and the $\hat X$-statistics reset to $1/2$. The relative phase $\varphi$ controls $n_x$ via $n_x = \sin\theta\cos\varphi$, and that information is what the Z measurement destroys.

(d) The difference $P_A - P_B = \tfrac{1}{2}\sin\theta\cos\varphi$ vanishes iff $\sin\theta = 0$ or $\cos\varphi = 0$:

- $\sin\theta = 0$ corresponds to $\theta = 0$ or $\pi$: the initial state is already $\vert 0\rangle$ or $\vert 1\rangle$, with Bloch vector along $\pm\boldsymbol{e}_z$. There was no $n_x$ to erase, so the Z measurement makes no difference to the $\hat X$ statistics — both scenarios give $P(\hat X = +1) = 1/2$.
- $\cos\varphi = 0$ corresponds to $\varphi = \pi/2$ or $3\pi/2$: the relative phase is $\pm\mathrm{i}$, making the initial Bloch vector lie in the $yz$-plane (no $\boldsymbol{e}_x$ component). Again $n_x = 0$ from the outset, so nothing to erase.

In both cases the initial state has $n_x = 0$, i.e. the Bloch vector is perpendicular to $\boldsymbol{e}_x$ on the Bloch sphere — and the $\hat X$ measurement was already going to give $1/2$ either way. The Z measurement erases only the part of the Bloch vector along $\boldsymbol{e}_x$, and if there is none to begin with, the erasure is invisible. This is the geometric content of "the Z measurement projects out the $\boldsymbol{e}_z$ component, discarding the rest".

<!-- ─── -->

**6. Quantum interference.** Two qubit states differ only by a relative phase:

$$
\vert\psi_1\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle), \qquad \vert\psi_2\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\vert 1\rangle), \quad \varphi\in\mathbb R.
$$

(a) Show that $\hat Z$ measurements on $\vert\psi_1\rangle$ and $\vert\psi_2\rangle$ produce identical outcome probabilities.

(b) Compute $P(+1)$ for $\hat X$ measured on $\vert\psi_2\rangle$ as a function of $\varphi$.

(c) Explain in one sentence why the relative phase is invisible to $\hat Z$ but visible to $\hat X$, in terms of how each measurement combines the amplitudes $c_0$ and $c_1$.

**Solution.**

(a) For both states the $\hat Z$-basis amplitudes have modulus $1/\sqrt 2$:

$$
P_1(\pm 1) = \left\vert\tfrac{1}{\sqrt 2}\right\vert^2 = \tfrac{1}{2}, \qquad P_2(+1) = \left\vert\tfrac{1}{\sqrt 2}\right\vert^2 = \tfrac{1}{2},\quad P_2(-1) = \left\vert\tfrac{\mathrm{e}^{\mathrm{i}\varphi}}{\sqrt 2}\right\vert^2 = \tfrac{1}{2}.
$$

The Born rule takes the modulus of each amplitude *separately*, and the unit-modulus phase $\mathrm{e}^{\mathrm{i}\varphi}$ disappears under the modulus. So both states are statistically indistinguishable in the $\hat Z$ basis.

(b) The amplitude for outcome $+1$ along $\hat X$ is

$$
\langle+\vert\psi_2\rangle = \tfrac{1}{\sqrt 2}(\langle 0\vert + \langle 1\vert)\cdot\tfrac{1}{\sqrt 2}(\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\vert 1\rangle) = \tfrac{1}{2}(1 + \mathrm{e}^{\mathrm{i}\varphi}).
$$

Squared modulus:

$$
P(+1) = \tfrac{1}{4}\vert 1 + \mathrm{e}^{\mathrm{i}\varphi}\vert^2 = \tfrac{1}{4}\bigl[(1+\cos\varphi)^2 + \sin^2\varphi\bigr] = \tfrac{1}{4}(2 + 2\cos\varphi) = \tfrac{1 + \cos\varphi}{2} = \cos^2(\varphi/2).
$$

Limits: $\varphi = 0$ gives $P(+1) = 1$ (the state is $\vert+\rangle$); $\varphi = \pi$ gives $P(+1) = 0$ (the state is $\vert-\rangle$); $\varphi = \pi/2$ gives $P(+1) = 1/2$ (the state is $\vert\mathrm{i}\rangle$, equidistant from $\vert\pm\rangle$).

(c) A $\hat Z$ measurement squares each amplitude *separately* ($P(0) = \vert c_0\vert^2$, $P(1) = \vert c_1\vert^2$), so any phase factor multiplying a single amplitude disappears. A $\hat X$ measurement, by contrast, squares the *sum* of the two amplitudes ($\langle+\vert\psi\rangle \propto c_0 + c_1$), and the relative phase between $c_0$ and $c_1$ controls whether the sum interferes constructively or destructively. **Relative phase encodes the answer to "do the amplitudes reinforce or cancel?" — a question only basis-changing measurements can ask.**

<!-- ─── -->

**7. Filter vs measurement misconception.** Consider a Stern-Gerlach setup:

$$
\hat{Z} \to \text{(filter }+1\text{)} \to \hat{X} \to \text{(filter }-1\text{)} \to \hat{Z}.
$$

Atoms enter in state $\vert 0\rangle$. The first apparatus measures $\hat Z$ and **keeps only the $+1$ branch**; the second measures $\hat X$ and **keeps only the $-1$ branch**; the third measures $\hat Z$ but has **no filter** — every atom that reaches it is measured and recorded.

(a) Compute the surviving fraction of the original beam after each apparatus.

(b) What is the final state of an atom that makes it all the way through? Give both possible outcomes of the final $\hat Z$ measurement and their conditional probabilities.

(c) A naive analysis multiplies the Born-rule outcome probabilities at every stage, obtaining $1 \times \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}$ for the surviving fraction. Identify the error in this analysis, and explain in one sentence the difference between a *filter* (post-selects a branch, discarding the rest) and a *measurement* (records the outcome on every atom but discards none).

**Solution.**

(a) Stage 1 — $\hat Z$ measurement + filter $+1$ on $\vert 0\rangle$: $P(+1) = 1$, every atom passes. Surviving fraction: $1$. State remains $\vert 0\rangle$.

Stage 2 — $\hat X$ measurement + filter $-1$ on $\vert 0\rangle$: writing $\vert 0\rangle = \tfrac{1}{\sqrt 2}(\vert+\rangle + \vert-\rangle)$, the $-1$ branch has $P(-1) = \tfrac{1}{2}$. Half the atoms pass. Surviving fraction so far: $\tfrac{1}{2}$. State of survivors: $\vert-\rangle$.

Stage 3 — $\hat Z$ measurement, **no filter**: every survivor is measured but none is discarded. Surviving fraction unchanged: $\tfrac{1}{2}$.

(b) Among the $\tfrac{1}{2}$ of atoms that arrived at Stage 3 in state $\vert-\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \vert 1\rangle)$:

$$
P(+1) = \vert\langle 0\vert-\rangle\vert^2 = \tfrac{1}{2}, \qquad P(-1) = \vert\langle 1\vert-\rangle\vert^2 = \tfrac{1}{2}.
$$

Each survivor ends in $\vert 0\rangle$ or $\vert 1\rangle$ with equal probability — a coin flip in the final $\hat Z$ readout. The original $1$–$0$ certainty in the $\hat Z$ outcome at Stage 1 has been completely erased by the intervening $\hat X$ measurement.

(c) The naive $\tfrac{1}{4}$ comes from multiplying Stage 3's $P(+1) = \tfrac{1}{2}$ into the survival count as if it were a *third filter*. It is not: Stage 3 is a measurement only — every atom that reaches it is *recorded*, not *discarded*. **A filter applies the Born rule to compute a survival probability (atoms are physically thrown away); a measurement applies the Born rule to compute an outcome probability (every atom continues, but the state collapses).** The two operations share the same probability formula but differ in whether atoms exit the beam — and the surviving fraction multiplies the *filter* probabilities only.

The lesson: be careful which apparatus is a filter and which is a bare measurement. Sequential Born-rule probabilities give survival fractions only when every stage post-selects; otherwise the unfiltered stage contributes $\times 1$ to the survival count, with its Born-rule split describing only the outcome distribution among the survivors.
