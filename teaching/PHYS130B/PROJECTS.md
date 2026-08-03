# PHYS 130B — Research Projects

Aggregated catalog of every research project assigned across the PHYS 130B (Quantum Mechanics) lecture notes. One project per `x.y` section (§2.3 offers two). Each entry is copied verbatim from the `## Project` cell of the corresponding section-parent notebook.

**How projects are assessed** (course policy): research projects are graded on **correctness, novelty, and presentation**. They are genuine scientific inquiry — literature survey + computation + scientific writing, achievable in ~2 weeks with AI assistance — not extended homework. Students complete two projects per quarter and present if enrollment permits.

---

## Contents

- **Chapter 1: Qubit**
  - §1.1 States and Observables — *Quantum State Tomography via Classical Shadow Measurements*
  - §1.2 Measurement — *Quantum Process Tomography and Gate Fidelity Characterization*
  - §1.3 Time Evolution — *Pulse Shaping and GRAPE Optimization for Quantum Gate Design*
- **Chapter 2: Identical Particles**
  - §2.1 Bosons and Fermions — *Bose-Einstein Condensation in Trapped Ultracold Atoms*
  - §2.2 Angular Momentum — *Ultracold Fermi Gases and the BCS-BEC Crossover*
  - §2.3 Anyons — *Simulating the Toric Code: Emergent Anyons and Error Correction*
  - §2.3 Anyons — *Abelian Anyons and Chern-Simons Theory*
- **Chapter 3: Path Integral**
  - §3.1 Quantization — *Path Integral Monte Carlo for Quantum Many-Body Systems*
  - §3.2 Propagator — *Quantum Revivals and the Talbot Effect*
  - §3.3 Stationary Phase — *Semiclassical Theory of Quantum Chaos: Gutzwiller Trace Formula*
  - §3.4 Imaginary Time — *Quantum Phase Transitions via Imaginary-Time Path Integrals*
- **Chapter 4: Phase and Gauge**
  - §4.1 Gauge Field — *Lattice Gauge Theory in 1+1 Dimensions*
  - §4.2 Berry Phase — *Aharonov-Bohm Interferometry and Topological Transport*
  - §4.3 Landau Level — *Quantum Hall Fractionalization and Composite Fermions*
  - §4.4 Spin and Monopole — *Magnetic Monopole Searches and Charge Quantization*
- **Chapter 5: Perturbation Theory**
  - §5.1 Time-Independent Perturbation Theory — *Quantum Chemistry: Perturbative Corrections to the Helium Atom*
  - §5.2 Time-Dependent Perturbation Theory — *Cavity QED and the Jaynes-Cummings Model: Rabi Splitting and Collapse-Revival*
- **Chapter 6: Quantum Foundations**
  - §6.1 Density Matrix — *Classical Shadow Tomography: Efficient Quantum State Estimation*
  - §6.2 Entanglement — *Measurement-Induced Entanglement Phase Transitions*
  - §6.3 Generalized Measurement — *Quantum State Discrimination and Quantum Illumination*
  - §6.4 Open Quantum Systems — *Non-Markovian Dynamics and Quantum Memory Effects*

---

# Chapter 1: Qubit

## §1.1 States and Observables

*Source notebook: `notes_src/ch1_qubit/1-1-states-and-observables.ipynb`*

### Project: Quantum State Tomography via Classical Shadow Measurements

**Objective:** Implement classical shadow tomography to reconstruct arbitrary quantum states from weak, non-invasive measurements.

**Background:** Shadow tomography uses randomized measurements followed by efficient classical post-processing. The approach scales logarithmically with state dimension and is robust to noise — key advantages for near-term quantum devices.

**Suggested Approach:**

- Literature survey on classical shadow formalism (Huang et al., *Nature Phys.* 2020)
- Implementation: simulate quantum device, apply random Clifford rotations, measure computational basis, reconstruct fidelity $F = \langle\psi_{\text{true}}\vert\rho_{\text{reconstructed}}\vert\psi_{\text{true}}\rangle$
- Benchmark against standard tomography for various qubit states
- Discuss noise robustness and connection to Bloch sphere geometry

**Expected Deliverable:** Research report (6–8 pages) including literature review, protocol description, numerical results on 1–2 qubit systems, comparison with alternative methods, and near-term applicability discussion.

---

## §1.2 Measurement

*Source notebook: `notes_src/ch1_qubit/1-2-measurement.ipynb`*

### Project: Quantum Process Tomography and Gate Fidelity Characterization

**Objective:** Build a framework for characterizing single-qubit quantum gate operations and estimating fidelity on quantum devices.

**Background:** Full protocol development requiring state preparations across multiple bases, applying unknown channels, measuring in complementary bases, and reconstructing channel representation through least-squares fitting. Single-qubit characterization requires approximately 18 measurement experiments.

**Expected Deliverable:** Research report (6–8 pages) containing theory overview, experimental protocol, numerical gate characterization results, error decomposition into quantum error types, and comparison with published hardware benchmarks.

---

## §1.3 Time Evolution

*Source notebook: `notes_src/ch1_qubit/1-3-time-evolution.ipynb`*

### Project: Pulse Shaping and GRAPE Optimization for Quantum Gate Design

**Objective:** Design optimal control techniques (GRAPE: Gradient Ascent Pulse Engineering) for implementing robust quantum gates under realistic Hamiltonian constraints and decoherence.

**Hamiltonian Model:** $\hat{H} = \frac{\omega_0}{2}\hat{\sigma}^z + \Omega(t)\hat{\sigma}^x$ with dephasing rate $\gamma_\phi$ and spontaneous emission $\gamma_1$.

**Suggested Approach:**

- Literature survey of optimal control theory for quantum systems
- Derive GRAPE algorithm; parametrize pulses using basis functions
- Solve Liouville–von Neumann equations numerically
- Optimize fidelity through gradient-based methods

**Expected Deliverable:** Research report (6–8 pages) covering optimal control theory, GRAPE algorithm derivation, numerical results for 1–2 qubit gates, fidelity-time trade-offs, robustness analysis, and experimental implementation discussion.

---

# Chapter 2: Identical Particles

## §2.1 Bosons and Fermions

*Source notebook: `notes_src/ch2_identical-particles/2-1-bosons-and-fermions.ipynb`*

### Project: Bose-Einstein Condensation in Trapped Ultracold Atoms

**Objective:** Simulate BEC in harmonic traps using the Gross-Pitaevskii equation to explore phase transitions, condensate dynamics, and connections to identical particle statistics.

**Background:** BEC occurs below critical temperature $T_c = 2\pi\hbar^2 n^{2/3}/(mk_B)$ when macroscopic boson populations occupy identical quantum states. The condensate follows the nonlinear Gross-Pitaevskii equation with mean-field coupling $g\vert\psi\vert^2$.

**Suggested Approach:**

- Literature survey of Gross-Pitaevskii equation and BEC mean-field theory
- Derive GP equation from second quantization using Bogoliubov approximation
- Implement 1D GP solver via split-step Fourier method or imaginary-time evolution
- Use harmonic trap $V(x) = \tfrac{1}{2}m\omega^2 x^2$ for ground state calculations
- Conduct imaginary-time evolution showing condensate fraction vs. temperature transition
- Excite condensate to observe collective modes; extract frequencies
- Extensions: 2D vortex formation, tuning interaction strength, finite-temperature corrections

**Expected Deliverable:** Research report (7–10 pages) covering GP theory derivation, numerical methods with convergence analysis, ground state evolution and phase transition, collective mode analysis, benchmarks against experiments, and condensed matter/quantum optics connections.

**Key References:** Pethick & Smith *Bose-Einstein Condensation in Dilute Gases*; Stringari *Collective Excitations of a Trapped Bose-Condensed Gas*; Cornell, Wieman, and Ketterle experimental BEC work.

---

## §2.2 Angular Momentum

*Source notebook: `notes_src/ch2_identical-particles/2-2-angular-momentum.ipynb`*

### Project: Ultracold Fermi Gases and the BCS-BEC Crossover

**Objective:** Model the continuous evolution from weakly-paired fermions to bosonic molecules by tuning interactions.

**Suggested Approach:**

- Literature survey of mean-field BCS theory
- Derive gap equations from the pairing Hamiltonian
- Numerical self-consistent iteration for the gap and chemical potential
- Plot phase diagrams showing gap and coherence length across the crossover
- Analyze fermionic vs. bosonic excitations
- Examine angular momentum constraints on pairing

**Expected Deliverable:** Research report (7–10 pages) with theory, numerical solutions, phase diagrams, excitation spectra analysis, and experimental comparisons from ultracold Fermi gas laboratories.

---

## §2.3 Anyons

*Source notebook: `notes_src/ch2_identical-particles/2-3-anyons.ipynb`*

### Project: Simulating the Toric Code: Emergent Anyons and Error Correction

**Objective:** Implement the toric code on a finite lattice, identify its ground-state degeneracy, create and braid anyonic excitations, and benchmark its performance as a quantum error-correcting code.

**Background:** The toric code is both a paradigmatic model of topological order and the foundation of modern surface-code quantum error correction. On a torus, the ground-state space is 4-fold degenerate, and excitations come in two types (charges and fluxes) whose composite is a fermion. Understanding this model bridges fundamental physics (emergent particles, topological phases) and practical quantum computing (fault-tolerant error correction).

**Suggested Approach:**
- Build the toric code Hamiltonian for an $L \times L$ lattice (start with $L = 2$, which is feasible). Diagonalize to verify the 4-fold ground-state degeneracy on a torus.
- Create charge and flux excitations by applying string operators. Verify that charges/fluxes are created in pairs and that the string itself is unobservable.
- Demonstrate the mutual $\pi$ phase: take a charge around a flux and measure the Berry phase.
- Implement a simple error model (independent bit-flip and phase-flip with probability $p$). Run syndrome measurements and minimum-weight perfect matching decoding.
- Plot logical error rate vs physical error rate for different lattice sizes. Estimate the error threshold.

**Expected Deliverable:** Research report (5–8 pages) with: model definition, numerical verification of ground-state degeneracy, demonstration of anyonic excitations and their statistics, error correction simulation results with threshold estimate, and discussion of surface code variants used in current experiments (Google Willow, IBM, etc.).


### Project: Abelian Anyons and Chern-Simons Theory

**Objective:** Learn the K-matrix formalism for abelian topological phases, compute anyon spectra and statistics rigorously, and apply it to the fractional quantum Hall effect and the toric code.

**Background:** The charge-flux composite picture introduced in §2.3.1 provides useful intuition for anyonic statistics, but it is ultimately a toy model. The correct mathematical framework is **Chern-Simons (CS) gauge theory**, where statistics are computed exactly from the field theory action — no hand-waving about "charge around flux" is needed. For abelian anyons, the theory is fully characterized by an integer matrix $K$ and a set of charge vectors.

**Key Concepts to Investigate:**

1. **The Chern-Simons action.** The effective field theory for an abelian topological phase with $n$ gauge fields $a^I_\mu$ is:

    $$
    S = \int \mathrm{d}^3 x \; \frac{K_{IJ}}{4\pi} \epsilon^{\mu\nu\rho} a^I_\mu \partial_\nu a^J_\rho
    $$

    where $K$ is a symmetric integer matrix. Understand what $K$ encodes and how it determines all topological data.

2. **Anyon sectors.** Anyons are labeled by integer charge vectors $\boldsymbol{l} = (l_1, \ldots, l_n)^T$. The **anyon lattice** — the set of all allowed anyon types — is determined by $K$: two charge vectors $\boldsymbol{l}$ and $\boldsymbol{l}'$ label the same anyon if $\boldsymbol{l} - \boldsymbol{l}' = K \boldsymbol{m}$ for some integer vector $\boldsymbol{m}$. The number of distinct anyons is $\vert\det K\vert$.

3. **Topological spin.** The topological spin (self-statistics) of an anyon $\boldsymbol{l}$ is:

$$
h_{\boldsymbol{l}} = \frac{\boldsymbol{l}^T K^{-1} \boldsymbol{l}}{2} \pmod{1}, \qquad \theta_{\boldsymbol{l}} = 2\pi h_{\boldsymbol{l}}
$$

The exchange phase equals the topological spin phase: $\theta_{\mathrm{ex}} = \theta_{\boldsymbol{l}}$.

4. **Mutual braiding.** The braiding phase when anyon $\boldsymbol{l}_a$ encircles anyon $\boldsymbol{l}_b$ is:

$$
\theta_{ab} = 2\pi \, \boldsymbol{l}_a^T K^{-1} \boldsymbol{l}_b
$$

5. **Fusion rules.** Anyon fusion is denoted $a \times b$ and corresponds to vector addition of charge vectors: $\boldsymbol{l}_{a \times b} = \boldsymbol{l}_a + \boldsymbol{l}_b \pmod{K}$. Determine the fusion group for each $K$.

6. **Ribbon relation.** The topological spin and braiding are not independent. For a composite anyon $a \times b$, the ribbon identity relates self-statistics to mutual braiding:

    $$
    \theta_{a \times b} = \theta_a + \theta_b + \theta_{ab}
    $$

    This is a consistency condition: the spin of a composite is the sum of individual spins plus their mutual braiding.


**Suggested Approach:**
- Start with the simplest case: $K = (k)$ (a $1 \times 1$ matrix). This is the $U(1)_k$ Chern-Simons theory describing the $\nu = 1/k$ Laughlin state. Show that there are $k$ anyon sectors labeled by $l = 0, 1, \ldots, k-1$. Compute the topological spin $h_l = l^2/(2k)$ and the braiding phase $\theta_{ab} = 2\pi \, ab/k$. Reproduce the results for $k = 3$ (the $\nu = 1/3$ state): exchange angle $\pi/3$, braiding phase $2\pi/3$.
- Next, study the toric code: $K = \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}$. Show that $\vert\det K\vert = 4$ gives four anyon sectors. Identify $1, e, m, \varepsilon$ with specific charge vectors, compute all topological spins and mutual braiding phases, and verify they match the results from §2.3.3.
- Verify the ribbon relation explicitly for $\varepsilon = e \times m$ in both examples.
- (Optional) Explore a more exotic example: the $K = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ theory or the hierarchy state $K = \begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix}$. How many anyon types exist? What are their statistics?

**Key References:**
- X.-G. Wen, *Quantum Field Theory of Many-Body Systems* (Oxford, 2004), Ch. 8–9
- D. Tong, *Lectures on the Quantum Hall Effect* (arXiv:1606.06687), §5
- A. Kitaev, *Anyons in an exactly solved model and beyond* (arXiv:cond-mat/0506438)
- S. B. Bravyi and A. Kitaev, *Quantum codes on a lattice with boundary* (arXiv:quant-ph/9811052)

**Expected Deliverable:** Research report (5–8 pages) with: derivation of the $K$-matrix formulas for spin and braiding, complete anyon tables for $U(1)_3$ and the toric code, verification of the ribbon relation, comparison with the charge-flux composite picture (explain where and why the toy model breaks down), and optionally one additional $K$-matrix example.

---

# Chapter 3: Path Integral

## §3.1 Quantization

*Source notebook: `notes_src/ch3_path-integral/3-1-quantization.ipynb`*

### Project: Path Integral Monte Carlo for Quantum Many-Body Systems

**Objective:** Implement Path Integral Monte Carlo (PIMC) to compute finite-temperature properties of quantum systems and explore the connection between imaginary-time path integrals and classical statistical mechanics of "quantum worldlines."

**Background:** The path integral formulation reveals a profound connection: finite-temperature quantum mechanics $\hat{\rho} = \mathrm{e}^{-\beta H}$ is equivalent to sampling classical polymer chains (worldlines) in imaginary time. This insight is the foundation of ab initio computational methods for quantum materials, including electronic structure of real solids at finite temperature. PIMC is particularly powerful for bosons (no sign problem) and low-density systems, making it a workhorse method in quantum chemistry and materials science.

**Suggested Approach:**
- **Literature Survey**: Study the path integral formulation and PIMC methods. Read David Tong's lecture notes on path integrals, or "Quantum Monte Carlo" (Ceperley & Alder, Rev. Mod. Phys. 1980). Understand the connection between imaginary-time path integrals and statistical mechanics of classical polymers.
- Start with a simple model: the harmonic oscillator or a chain of coupled oscillators at finite temperature.
- Implement a primitive PIMC algorithm: discretize imaginary time into $M$ slices, represent each configuration as a path $(x_0, x_1, \ldots, x_M)$ on the imaginary-time lattice, and use Metropolis sampling to generate paths weighted by $\mathrm{e}^{-S_{eff}}$.
- Verify against analytical results: compute ground state energy, thermal expectation values $\langle x^2 \rangle$, and specific heat as functions of temperature.
- Extend to a two-body interacting system (e.g., a Lennard-Jones pair potential or a quartic potential) and study how interactions modify thermodynamic properties.
- Quantify convergence: investigate how results depend on the number of slices $M$ (finer imaginary-time grid). Extrapolate to the continuum limit.
- Interpretation: explain how a classical random walk (polymer chain) in imaginary time computes quantum thermal averages.

**Expected Deliverable:** A research report (5–10 pages) with documented code. Include: (i) algorithm pseudocode and implementation details, (ii) numerical results (ground state, thermal properties) compared to exact or high-accuracy benchmarks, (iii) convergence analysis in $M$, (iv) physical interpretation of worldlines and the imaginary-time ensemble, (v) discussion of PIMC applications in real materials and current limitations.

**Key References:** D. M. Ceperley, Rev. Mod. Phys. 67, 279 (1995); R. P. Feynman & A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill); path integral Monte Carlo reviews in modern computational physics.

---

## §3.2 Propagator

*Source notebook: `notes_src/ch3_path-integral/3-2-propagator.ipynb`*

### Project: Quantum Revivals and the Talbot Effect

**Objective:** Study quantum carpets—spatiotemporal patterns of probability density—arising from the free particle propagator, connect to the Talbot effect in optics, and uncover the hidden periodic structure beneath quantum interference.

**Background:** The free particle propagator exhibits a striking phenomenon: at rational times $t = 2\pi M/(\hbar k^2)$, the probability density returns to a periodic pattern (quantum revival), while at irrational times it fills space densely (ergodic-like behavior). This is closely related to the Talbot effect in classical optics: when coherent light passes through a periodic grating, the intensity pattern repeats periodically in the paraxial direction even though diffraction causes spreading. The quantum analog reveals how periodic boundary conditions and rational multiples of $\hbar$ create exact revivals—a frontier in understanding coherence and control in quantum systems.

**Suggested Approach:**
- Compute the free particle propagator $K(x,t; x_0, 0) = \sqrt{m/(2\pi \mathrm{i}\hbar t)} \mathrm{e}^{\mathrm{i}m(x-x_0)^2/(2\hbar t)}$ and visualize $|K|^2$ as a 2D "carpet" with space on the x-axis and time on the y-axis.
- Initialize a localized Gaussian wavepacket and evolve it under the free particle Hamiltonian; track $|\psi(x,t)|^2$.
- Identify quantum revivals: plot $|\psi(x,t)|^2$ at times $t_n = 2\pi M_n/(\hbar k^2)$ for various integers $M_n$. Describe the periodic structure.
- Introduce a periodic initial condition (e.g., a Bloch state or a periodic superposition) and study how the carpet pattern changes; compare to the Talbot effect.
- Compute Loschmidt echo or fidelity to quantify how closely the carpet returns to its initial structure at revival times.
- Extend to a weakly perturbed system (add a small potential $V(x)$) and explore how revivals degrade—a probe of decoherence.

**Expected Deliverable:** A research report (5–10 pages) with code and visualizations. Include: (i) numerical computation and visualization of quantum carpets, (ii) demonstration of quantum revivals and their connection to Talbot periodicity, (iii) analysis of the period as a function of $\hbar$ and initial momentum, (iv) comparison of quantum vs. classical optics Talbot effects, (v) investigation of how perturbations destroy revivals, with implications for quantum control and decoherence.

**Key References:** J. H. Hannay & M. V. Berry, Physica D 17, 385 (1985) [quantum revivals]; F. Haake et al., Phys. Rev. A 47, 2506 (1993); M. Berry & M. Keating, J. Phys. A 23, 4839 (1990) [Talbot effect].

---

## §3.3 Stationary Phase

*Source notebook: `notes_src/ch3_path-integral/3-3-stationary-phase.ipynb`*

### Project: Semiclassical Theory of Quantum Chaos: Gutzwiller Trace Formula

**Objective:** Implement the Gutzwiller trace formula, which connects quantum energy levels to classical periodic orbits, and test it on a simple chaotic billiard system to uncover the hidden classical structure in quantum chaos.

**Background:** One of the deepest insights of semiclassical physics is that quantum spectra encode information about classical dynamics. The Gutzwiller trace formula expresses the quantum density of states as a sum over all classical periodic orbits, weighted by the actions and stability properties (monodromy matrices) of those orbits. This formula is a frontier tool for understanding quantum chaos: systems whose classical counterparts are chaotic (exponential sensitivity to initial conditions) still possess a dense, deterministic quantum spectrum, yet that spectrum bears the mathematical fingerprint of the underlying chaotic dynamics. Applications range from quantum dots and microwave cavities to nuclear physics.

**Suggested Approach:**
- Start with a simple integrable system (2D harmonic oscillator): find its classical periodic orbits analytically and compute the Gutzwiller formula. Verify that it reproduces the known quantum spectrum.
- Study a 2D billiard system (e.g., square or circular billiard): compute its classical periodic orbits numerically by ray tracing (bounce maps).
- For each periodic orbit, calculate the action $S_p = \oint p \, \mathrm{d}q$ and the stability eigenvalues (Lyapunov exponents from the monodromy matrix).
- Construct the Gutzwiller trace: $\rho(E) = \rho_0(E) + \sum_p \rho_p(E)$, where $\rho_0$ is the smooth part and $\rho_p$ is the oscillating contribution from periodic orbit $p$.
- Compare to the quantum spectrum obtained by diagonalizing the Hamiltonian numerically in a finite domain. Do short periodic orbits dominate? Which orbits contribute most to oscillations?
- Explore a chaotic billiard (e.g., stadium or Sinai billiard): show that the classical periodic orbits are now exponentially proliferating, yet the Gutzwiller formula still provides a quantitative account of spectral oscillations.

**Expected Deliverable:** A research report (5–10 pages) with code. Include: (i) classical billiard dynamics and periodic orbit enumeration, (ii) derivation and implementation of the Gutzwiller formula, (iii) quantum spectrum (from numerics) vs. semiclassical prediction (from Gutzwiller), (iv) quantitative comparison: residue analysis, quality of fit, (v) physical interpretation: why do classical periodic orbits predict quantum levels?, (vi) discussion of quantum chaos and the classical-quantum correspondence.

**Key References:** M. C. Gutzwiller, *Chaos in Classical and Quantum Mechanics* (Springer, 1990); D. Ullmo, Rep. Prog. Phys. 71, 026001 (2008) [quantum chaos and periodic orbits]; E. B. Bogomolny et al., Phys. Rev. Lett. 85, 2486 (2000).

---

## §3.4 Imaginary Time

*Source notebook: `notes_src/ch3_path-integral/3-4-imaginary-time.ipynb`*

### Project: Quantum Phase Transitions via Imaginary-Time Path Integrals

**Objective:** Study the transverse-field Ising model using the path integral formulation in imaginary time, implement Monte Carlo sampling of Euclidean worldlines, and explore quantum phase transitions as a function of field strength.

**Background:** The path integral in imaginary time provides a bridge between quantum mechanics and classical statistical mechanics, revealing that quantum phase transitions can be understood through a classical lens: mapping the (1+1)D quantum Ising model to a 2D classical Ising model with defects (instantons). This classical mapping is powerful and intuitive: quantum tunneling between ordered states becomes a classical defect (kink) in the imaginary-time worldline. Quantum phase transitions—abrupt changes in ground state properties at zero temperature—correspond to classical phase transitions of the effective classical system. This perspective is essential for understanding quantum criticality and has applications from condensed matter to quantum field theory.

**Suggested Approach:**
- Set up the transverse-field Ising Hamiltonian: $\hat{H} = -J\sum_i \hat{\sigma}_i^z \hat{\sigma}_{i+1}^z - \Gamma \sum_i \hat{\sigma}_i^x$, where $\Gamma$ is the transverse field and $J$ is the interaction strength.
- Construct the path integral: for each quantum spin configuration, discretize imaginary time into slices and form a (1+1)D classical Ising model on the lattice.
- Implement a path integral Monte Carlo (or classical MC on the effective 2D system): sample worldlines weighted by the effective partition function.
- Vary $\Gamma/J$ from $0$ (ordered, all spins aligned in $z$-direction) to $\infty$ (disordered, field dominates). Compute the ground state energy, magnetization $\langle \hat{\sigma}^z \rangle$, and correlation length.
- Identify the quantum phase transition at $\Gamma/J \sim 1$: analyze how order parameter and correlation length diverge; extract critical exponents and compare to known universality class (Ising universality in 1D quantum = Ising universality in 2D classical).
- Visualize worldlines: show how instantons (domain walls in imaginary time) proliferate as the transition is approached.

**Expected Deliverable:** A research report (5–10 pages) with code and visualizations. Include: (i) path integral formulation and classical mapping, (ii) Monte Carlo algorithm pseudocode, (iii) phase diagram and transition point, (iv) order parameter, correlation length, and critical exponents, (v) visualization of worldlines and instanton dynamics, (vi) physical interpretation: how do instantons signal the transition?, (vii) connection to classical phase transitions and universality.

**Key References:** S. Sachdev, *Quantum Phase Transitions* (Cambridge, 2nd ed., 2011); J. Cardy, *Scaling and Renormalization in Statistical Physics* (Cambridge, 1996); path integral Monte Carlo methods for quantum spin systems.

---

# Chapter 4: Phase and Gauge

## §4.1 Gauge Field

*Source notebook: `notes_src/ch4_phase-and-gauge/4-1-gauge-field.ipynb`*

### Project: Lattice Gauge Theory in 1+1 Dimensions

**Objective:** Implement a lattice gauge theory (a discrete spacetime version of Yang-Mills theory) on a 1+1D lattice, study the phase structure and confinement mechanisms, and explore connections to condensed matter systems.

**Background:** Gauge theories are the foundation of the Standard Model, yet they are notoriously difficult to study nonperturbatively. Lattice gauge theory—formulated on a discrete spacetime grid—enables exact numerical simulation via Monte Carlo methods. In 1+1D (space and time), pure Yang-Mills theory confines: quarks cannot be separated to infinity without infinite energy cost. This confinement is a frontier question in QCD, and 1+1D is a laboratory where the mechanism is transparent and calculable. Recent connections to topological phases and quantum information make lattice gauge theories an active frontier.

**Suggested Approach:**
- Discretize the Yang-Mills action on a 1D spatial lattice with time evolution: $S = \sum_t \sum_n \operatorname{Tr}(U_{n,t} U_{n+1,t}^\dagger U_{n,t+1}^\dagger U_{n+1,t+1})$ for $SU(2)$ or $U(1)$ link variables.
- Implement a Metropolis or heat-bath Monte Carlo algorithm to sample link configurations at inverse temperature $\beta$.
- Compute the plaquette average $\langle \operatorname{Tr}(P) \rangle$ (order parameter), correlators, and screening lengths.
- Study the phase transition: deconfined phase (large $T$, $\beta$ small) vs. confined phase (small $T$, $\beta$ large).
- Insert a static quark-antiquark pair (Wilson loop operator) and measure the potential energy as a function of separation. Show linear confinement ($V(r) \sim r$) in the confined phase and screening in the deconfined phase.
- Relate to Hamiltonian lattice gauge theory and quantum simulations on neutral atoms or superconducting qubits.

**Expected Deliverable:** Research report with code. Include: (i) lattice Yang-Mills formulation and discretization, (ii) Monte Carlo algorithm and implementation details, (iii) phase diagram and order parameters, (iv) Wilson loop measurements and confinement signatures, (v) comparison with analytical predictions, (vi) discussion of quantum simulator implementations.

**Key References:** J. B. Kogut, Rev. Mod. Phys. 51, 659 (1979); D. B. Kaplan, Rev. Mod. Phys. 80, 1285 (2008); lattice QCD reviews.

---

## §4.2 Berry Phase

*Source notebook: `notes_src/ch4_phase-and-gauge/4-2-berry-phase.ipynb`*

### Project: Aharonov-Bohm Interferometry and Topological Transport

**Objective:** Model and numerically simulate Aharonov-Bohm interferometry in a mesoscopic ring, studying the role of flux quantization, disorder, and quantum coherence in topological transport phenomena.

**Background:** The Aharonov-Bohm effect—quantum phase shift from a magnetic field threading a closed loop—is one of the most elegant demonstrations that gauge potentials have physical significance. In mesoscopic systems (small conductors where quantum coherence is maintained over macroscopic distances), AB oscillations in transport properties provide direct evidence of flux quantization and topological protection. This is frontier territory: understanding persistent currents, quantum Hall transport, and topological insulators all relies on AB physics. Recent advances in quantum simulators have achieved unprecedented precision in simulating AB rings with cold atoms.

**Suggested Approach:**
- Compute the single-particle eigenstates and energy spectrum of a particle constrained to a 1D ring with magnetic flux $\Phi = \oint \boldsymbol{A} \cdot \mathrm{d}\boldsymbol{l}$.
- Show that energy levels are periodic in $\Phi$ with period $\Phi_0 = h/q$ (flux quantum); compute the modulation amplitude (Aharonov-Bohm oscillations).
- Compute transport properties: persistent current $I(\Phi)$ and its correlation with the flux. Show periodicity and discuss the role of disorder.
- Introduce disorder (random impurities on the ring) and study how localization suppresses the persistent current and smears AB oscillations.
- Add electron-electron interactions (Hubbard model on the ring) and explore competing effects: interaction-enhanced orbital magnetization vs. Anderson localization.
- Relate to experimental systems: mesoscopic metal rings, quantum Hall edge channels, and topological insulators.

**Expected Deliverable:** Research report with code. Include: (i) Hamiltonian formulation on a ring with flux, (ii) eigensolver results and AB oscillations, (iii) persistent current calculations with and without disorder, (iv) spectral and transport properties, (v) comparison with experimental observations, (vi) implications for topological transport and quantum simulators.

**Key References:** Y. Aharonov & D. Bohm, Phys. Rev. 115, 485 (1959); D. Yu. Sharvin & Y. V. Sharvin, JETP Lett. 34, 272 (1981); topological transport reviews.

---

## §4.3 Landau Level

*Source notebook: `notes_src/ch4_phase-and-gauge/4-3-landau-level.ipynb`*

### Project: Quantum Hall Fractionalization and Composite Fermions

**Objective:** Investigate the fractional quantum Hall effect (FQHE) in a two-dimensional electron gas using composite fermion theory and exact diagonalization, exploring how electron-electron interactions generate topologically ordered states.

**Background:** At integer filling factors $\nu = n$ (where $n$ is an integer), the quantum Hall effect is well-understood: electrons fill $n$ Landau levels, and Hall conductance is quantized to $\sigma_{xy} = n e^2/h$. But at fractional fillings (e.g., $\nu = 1/3, 2/5$), remarkable new states emerge: the fractional quantum Hall effect, with fractionally quantized Hall conductance and exotic quasiparticle excitations (anyons). The composite fermion picture—viewing electrons as bound to an even number of flux quanta, forming emergent fermions—provides deep insight. This is a frontier in understanding topological order, and has implications for topological quantum computing.

**Suggested Approach:**
- Set up a small 2D lattice (or disk geometry) with $N \approx 8$–10 electrons in a perpendicular magnetic field, using the lowest Landau level (LLL) projection.
- Use exact diagonalization to compute ground and excited state wavefunctions at filling fraction $\nu = 1/3$ and $\nu = 2/3$.
- Analyze the ground state structure: compute entanglement entropy, topological entanglement entropy, and edge degeneracy (signatures of topological order).
- Implement the composite fermion picture: rewrite states in terms of flux-attached fermions and compare the CF ground state to exact results.
- Compute excitation spectrum and quasihole/quasiparticle properties: compare with Laughlin wavefunction predictions.
- Measure the fractional charge of quasiholes and investigate anyonic statistics (braiding properties).

**Expected Deliverable:** Research report with code. Include: (i) Hamiltonian in the LLL and lattice discretization, (ii) exact diagonalization algorithm and implementation, (iii) ground state properties and topological characterization, (iv) composite fermion analysis and comparison with exact results, (v) excitation spectrum and quasiparticle properties, (vi) physical significance for topological quantum information.

**Key References:** D. C. Tsui, H. L. Störmer, & A. C. Gossard, Phys. Rev. Lett. 48, 1559 (1982); J. K. Jain, Composite Fermions (Cambridge University Press); topological order reviews.

---

## §4.4 Spin and Monopole

*Source notebook: `notes_src/ch4_phase-and-gauge/4-4-spin-and-monopole.ipynb`*

### Project: Magnetic Monopole Searches and Charge Quantization

**Objective:** Investigate the relationship between magnetic monopole existence and charge quantization, and analyze current experimental searches for monopoles in diverse physical systems.

**Background:** Dirac showed that the existence of even a single magnetic monopole would explain charge quantization—why electron charge appears in discrete units. Though monopoles have never been observed as fundamental particles, they emerge in condensed matter (spin ice), topological field theories, and grand unified theories. Modern searches span particle physics (LHC, noble liquid detectors), condensed matter (synthetic monopoles in cold atoms), and materials science (rare-earth pyrochlores). Understanding how monopoles constrain quantum mechanics (via the Dirac quantization condition $\mu_0 qg=2\pi n\hbar$) and their role in topological phenomena is an active frontier.

**Suggested Approach:**
- Derive the Dirac quantization condition from requiring single-valuedness of the wavefunction on a manifold with a magnetic monopole source.
- Compute the angular momentum decomposition of a monopole field (monopole harmonics) and relate to atomic physics and scattering.
- Survey current experimental searches: describe 3–4 approaches (e.g., track detector searches at LHC, noble liquid ionization signatures, neutron diffraction in spin ice, synthetic monopoles in ultracold atoms).
- For each search, extract: detection principle, expected monopole properties (mass, magnetic charge), sensitivity, and current limits on monopole abundance.
- Use the Dirac quantization condition to relate monopole mass scales to coupling unification in grand unified theories.
- Discuss condensed matter realizations: monopole-like excitations in artificial spin ice and quantum spin liquids; are these "real" monopoles?

**Expected Deliverable:** Comprehensive research report (6–10 pages) with code for computations and visualizations. Include: (i) derivation of Dirac quantization from quantum mechanics, (ii) monopole harmonics and angular momentum structure, (iii) detailed summaries of 4 experimental searches with diagrams, (iv) detection sensitivities and exclusion limits, (v) condensed matter realizations and their physical significance, (vi) critical assessment of what we've learned and future directions.

**Key References:** P. A. M. Dirac, Proc. Roy. Soc. A 133, 60 (1931); K. A. Milton, Rep. Prog. Phys. 69, 1637 (2006); recent monopole search reviews and condensed matter perspectives.

---

# Chapter 5: Perturbation Theory

## §5.1 Time-Independent Perturbation Theory

*Source notebook: `notes_src/ch5_perturbation-theory/5-1-time-independent-perturbation-theory.ipynb`*

### Project: Quantum Chemistry: Perturbative Corrections to the Helium Atom

The helium atom is a prototypical test of perturbation theory: it has two electrons interacting via Coulomb repulsion, and no closed-form solution. This project explores how perturbation theory captures electron correlation.

**Objective**: Implement variational and perturbation-theoretic approaches to the helium ground state energy, and compare against exact (full configuration interaction) calculations.

**Suggested Approach**:

1. **Variational baseline**: Use the variational principle with a trial wavefunction

   $$\psi(\boldsymbol{r}_1, \boldsymbol{r}_2) = \psi_{1s}(r_1; Z_{\text{eff}}) \psi_{1s}(r_2; Z_{\text{eff}})$$

   where $Z_{\text{eff}}$ is screened by electron-electron repulsion. Optimize over $Z_{\text{eff}}$ to find the best upper bound on the ground state energy.

2. **Perturbation theory**: Treat the electron-electron repulsion $\hat{V} = e^2/\vert\boldsymbol{r}_1 - \boldsymbol{r}_2\vert$ as a perturbation around independent-particle hydrogen-like atoms. Compute first and second-order corrections to the ground state energy.

3. **Exact reference**: Use numerical full configuration interaction or benchmark against published CI results (e.g., FCI energy for helium).

4. **Extension**: Apply the same electron-repulsion perturbation $\hat{V}$ to the lowest excited configuration $1s2s$ of helium. Show that first-order perturbation theory splits this level into a singlet (para-helium) and a triplet (ortho-helium) state separated by twice the exchange integral, and compare the predicted splitting against the measured ortho/para-helium energy difference.

**Expected Deliverable**:

- Numerical code (Python/Mathematica) implementing variational and perturbation methods
- Plot: ground state energy as a function of perturbation order (variational, 1st order, 2nd order, exact)
- Convergence analysis: at what order does the perturbative series saturate?
- Brief report (2–3 pages) discussing accuracy, physical insights (electron correlation, screening), and relevance to quantum chemistry (e.g., density functional theory as an alternative)

**Frontier relevance**: Perturbative corrections to many-electron atoms underpin quantum chemistry calculations used in drug discovery, materials science, and catalysis. Understanding where perturbation theory succeeds/fails is critical for developing better approximation methods.

---

## §5.2 Time-Dependent Perturbation Theory

*Source notebook: `notes_src/ch5_perturbation-theory/5-2-time-dependent-perturbation-theory.ipynb`*

### Project: Cavity QED and the Jaynes-Cummings Model: Rabi Splitting and Collapse-Revival

The Jaynes-Cummings model describes a two-level atom coupled to a single cavity mode. It exhibits rich dynamics: Rabi oscillations, collapse of oscillations due to photon decay, and surprising revival behavior. This project uses time-dependent perturbation theory and exact solvers to explore the frontier of quantum optics.

**Objective**: Study the dynamics of atom-cavity coupling, compute Rabi splitting, and discover collapse-revival phenomena—physics at the heart of cavity QED and superconducting qubit systems.

**Suggested Approach**:

1. **Setup**: Write the Jaynes-Cummings Hamiltonian

   $$\hat{H} = \hbar \omega_0 \hat{\sigma}^+\hat{\sigma}^- + \hbar \omega_c \hat{a}^\dagger\hat{a} + \hbar g (\hat{\sigma}^+ \hat{a} + \hat{\sigma}^- \hat{a}^\dagger)$$

   where $g$ is the coupling strength, and $\omega_0, \omega_c$ are atomic and cavity frequencies.

2. **Weak coupling limit** ($g \ll \vert\omega_0 - \omega_c\vert$): Apply time-dependent perturbation theory to compute transition rates and predict Rabi frequency.

3. **Strong coupling regime**: Solve the Hamiltonian exactly (analytically or numerically). Observe:
   - Rabi splitting: vacuum Rabi oscillations at frequency $\Omega_R \approx 2g$
   - Collapse-revival: oscillations decay (collapse) due to photon leakage, then partially revive

4. **Dissipation model**: Include cavity decay $\kappa$ (photon escape) and atomic spontaneous emission $\gamma$. Use the Lindblad master equation.

5. **Experimental connections**: Compare to superconducting qubit data (circuit QED, transmons) or optical cavity QED (Rydberg atoms, trapped ions).

**Expected Deliverable**:

- Code implementing: Rabi model, Jaynes-Cummings Hamiltonian, Lindblad dissipation
- Plots: (1) time evolution of atom and cavity populations; (2) collapse and revival of Rabi oscillations; (3) dissipation effects on dynamics
- Analysis: extract Rabi frequency from oscillations; measure collapse and revival timescales; compare weak-coupling perturbative prediction to exact result
- Brief report (2–3 pages) explaining the physics, experimental applications, and limitations of perturbation theory in the strong-coupling regime

**Frontier relevance**: Cavity QED is a testbed for quantum technologies. The Jaynes-Cummings model and its extensions underpin superconducting qubit systems (IBM, Google, Rigetti), trapped-ion quantum computers, and quantum simulators. Understanding how perturbation theory breaks down and exact solutions emerge is essential for engineering quantum devices.

---

# Chapter 6: Quantum Foundations

## §6.1 Density Matrix

*Source notebook: `notes_src/ch6_quantum-foundations/6-1-density-matrix.ipynb`*

### Project: Classical Shadow Tomography: Efficient Quantum State Estimation

**Objective:** Study the classical shadow protocol (Huang et al., 2020) for estimating exponentially many properties of a quantum state using only $O(\log M)$ random measurements. Implement the protocol for a few-qubit system and compare its efficiency to full state tomography.

**Background:** Full quantum state tomography requires exponentially many measurements in the number of qubits. The classical shadow protocol revolutionizes this by using random Clifford unitaries and classical post-processing to efficiently estimate expectation values. This is one of the major breakthroughs in quantum information science in the past decade.

**Suggested Approach:**
1. **Literature Survey:** Read Huang et al. (arXiv:2011.02993) and understand: (a) random Clifford sampling, (b) classical snapshot construction, (c) median-of-means post-processing for robust estimation.
2. **Implementation:** Write Python code to:
   - Generate random Clifford circuits for 2-3 qubits
   - Simulate measurement outcomes
   - Reconstruct classical shadow estimates
   - Compute expectation values of observables
3. **Comparison:** For a known 2-3 qubit state:
   - Estimate observables using classical shadows
   - Compare to full state tomography
   - Measure sample complexity and computational cost as a function of system size
4. **Extension:** Explore robustness to noise and realistic measurement errors.

**Expected Deliverable:** 
- Code implementing classical shadow protocol
- Numerical comparison: shadows vs. tomography (accuracy vs. sample count)
- Brief scientific summary (1-2 pages) explaining why classical shadows are more efficient than tomography and when they should be preferred in practice.

**Frontier Aspect:** This is an active research frontier. Understanding shadows opens doors to applications in quantum error correction, entanglement detection, and quantum machine learning.

---

## §6.2 Entanglement

*Source notebook: `notes_src/ch6_quantum-foundations/6-2-entanglement.ipynb`*

### Project: Measurement-Induced Entanglement Phase Transitions

**Objective:** Study how repeated measurements drive a phase transition between volume-law and area-law entanglement in random quantum circuits. Implement a 1D random Clifford circuit with variable measurement rate and compute entanglement entropy as a function of measurement probability.

**Background:** A major recent discovery (2018 onwards) is that measurements can *create* phase transitions in the entanglement structure of quantum systems. Without measurements, random unitary circuits maintain volume-law entanglement. But at a critical measurement rate, the system undergoes a sharp transition to area-law entanglement. This is a fundamentally new phenomenon at the intersection of quantum information, condensed matter, and statistical mechanics.

**Suggested Approach:**
1. **Literature Survey:** Read key papers (Li et al., Chan et al., 2019) on measurement-induced transitions. Understand: (a) volume-law vs. area-law entanglement, (b) critical exponents, (c) Clifford circuits and efficient simulation.
2. **Implementation:** Code a 1D circuit with:
   - Random 2-qubit Clifford gates
   - Single-qubit measurements at variable rate $p$
   - Efficient entanglement entropy calculation using stabilizer formalism
3. **Simulation:** Measure entanglement entropy $S(L)$ across the system as you vary:
   - Measurement probability $p$ (scan from 0 to 1)
   - System size $L$
4. **Analysis:** From the simulation results:
   - Identify the critical measurement rate $p_c$
   - Compute critical exponents and compare to theoretical predictions

**Expected Deliverable:**
- Code implementing 1D random circuit with measurements
- Phase diagram: $S(L)$ vs. $p$, showing transition from volume-law to area-law
- Estimate of critical measurement rate $p_c$
- Scientific summary explaining the physics of measurement-induced transitions and their implications for quantum information preservation.

**Frontier Aspect:** This is a hot topic in quantum information and statistical mechanics. Understanding measurement-driven transitions connects to quantum error correction, quantum scrambling, and the fundamental role of observation in quantum systems.

---

## §6.3 Generalized Measurement

*Source notebook: `notes_src/ch6_quantum-foundations/6-3-generalized-measurement.ipynb`*

### Project: Quantum State Discrimination and Quantum Illumination

**Objective:** Study optimal quantum measurement strategies for distinguishing non-orthogonal states. Implement the Helstrom bound (optimal discrimination error rate) and extend to quantum illumination, a quantum sensing protocol that outperforms classical radar in the low-SNR regime.

**Background:** Quantum mechanics forbids perfect discrimination of non-orthogonal quantum states. But quantum measurements (especially POVMs) can minimize the error probability. Quantum illumination extends this to quantum radar: entangled photons are used to detect a target with sensitivity surpassing classical radar. This is an active frontier in quantum sensing with practical applications.

**Suggested Approach:**
1. **Literature Survey:** 
   - Helstrom measurement: optimal error probability for distinguishing two quantum states
   - Quantum illumination (Tan et al., Shapiro, etc.): entanglement-enhanced detection
2. **Part A: State Discrimination**
   - For two non-orthogonal qubit states, compute the Helstrom bound analytically
   - Design an optimal POVM to achieve this bound
   - Simulate measurement outcomes and verify error rate
3. **Part B: Quantum Illumination**
   - Model entangled photon pairs sent to a target (50/50 beam splitter)
   - Simulate the return signal with noise
   - Compare quantum (entangled) strategy to classical (separable) strategy
   - Compute the advantage in signal detection probability
4. **Analysis:** Quantify quantum advantage in terms of SNR improvement.

**Expected Deliverable:**
- Derivation and numerical verification of Helstrom bound for qubit discrimination
- Code implementing optimal POVM-based measurement
- Numerical comparison: quantum vs. classical illumination (detection sensitivity vs. photon number)
- Scientific summary explaining why entanglement helps detect targets below classical limits.

**Frontier Aspect:** Quantum illumination is a frontier application of quantum information to practical sensing and metrology. Understanding optimal quantum measurements is crucial for quantum advantage in real-world applications.

---

## §6.4 Open Quantum Systems

*Source notebook: `notes_src/ch6_quantum-foundations/6-4-open-quantum-systems.ipynb`*

### Project: Non-Markovian Dynamics and Quantum Memory Effects

**Objective:** Study non-Markovian extensions of the Lindblad master equation. Implement the Hierarchical Equations of Motion (HEOM) for a spin-boson model and quantify non-Markovianity using rigorous measures (BLP or RHP).

**Background:** The Lindblad equation assumes Markovian (memoryless) dynamics. But real open quantum systems often have memory: the environment's response depends on the system's past state. Non-Markovian dynamics are ubiquitous in photosynthesis, quantum biology, and solid-state systems. Understanding when and how non-Markovianity matters is a frontier in open quantum systems theory.

**Suggested Approach:**
1. **Literature Survey:** 
   - Lindblad (Markovian) vs. non-Markovian master equations
   - HEOM: an exact method for non-Markovian dynamics (Tanimura, Ishizaki)
   - Non-Markovianity measures: BLP (Breuer-Laine-Piilo), RHP (Rivas-Huelga-Plenio)
2. **Part A: Spin-Boson Model**
   - Formulate a two-level system coupled to a thermal bath
   - Solve exactly using HEOM
   - Compare to Lindblad approximation
3. **Part B: Time Dynamics**
   - Compute system coherence $\rho_{01}(t)$ as a function of temperature and coupling strength
   - Measure populations and coherences
   - Identify regimes where Markovian approximation breaks down
4. **Part C: Non-Markovianity Measure**
   - Implement a non-Markovianity measure (e.g., BLP based on distinguishability)
   - Quantify degree of non-Markovianity as a function of model parameters
   - Determine critical conditions for significant memory effects

**Expected Deliverable:**
- Code implementing HEOM solver for spin-boson model
- Comparison: exact HEOM vs. Lindblad master equation (population and coherence dynamics)
- Non-Markovianity measure as a function of temperature and coupling
- Scientific summary explaining when non-Markovian effects matter and how to detect them experimentally.

**Frontier Aspect:** Non-Markovian quantum dynamics is a frontier in understanding open systems beyond the Markovian approximation. Applications range from quantum biology to quantum error correction to quantum simulation.

---
