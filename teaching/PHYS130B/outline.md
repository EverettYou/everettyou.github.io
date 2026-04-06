# PHYS 130B — Storyline Outline

## Central Narrative

Quantum mechanics is the language of nature at the smallest scales. This course builds the framework in six chapters, each answering one driving question:

1. **Qubit** — How does one quantum system work? (Axioms: states, measurement, dynamics)
2. **Identical Particles** — What happens when we have many? (Tensor product → symmetry → statistics)
3. **Path Integral** — How does classical physics emerge? (Sum over paths → stationary phase → classical limit)
4. **Phase and Gauge** — What does phase mean physically? (Gauge field → Aharonov-Bohm → Berry phase → topology)
5. **Perturbation Theory** — What if we can't solve exactly? (Systematic approximations for real problems)
6. **Quantum Foundations** — What is quantum information? (Mixed states → entanglement → decoherence → error correction)

The arc: start with the simplest quantum system (one qubit), scale up (many particles), connect to classical physics (path integral), explore the role of phase (gauge theory), develop practical tools (perturbation theory), and close the circle by revisiting the foundations with the mature language of quantum information.

---

## Ch1. Qubit

<!-- The simplest quantum system as the stage for all axioms: states, observables, measurement, dynamics. -->

### 1.1 States and Observables

- 1.1.1 Qubits

  - start with a genreal discussion about what is physics
    - quantum is abstract to many, because far from our daily life
    - facing such a mysterious system, how do we study its physics
    - Important: Key objective of physics theory: (a) description (b) prediction 
    - Pull back: how does quantum physics describe - everything is a vector, and predict - meansurement and time evluation all are operators (see "Everything Is a Vector" in notebooks/AlgebraicMethods)

  - Quickly cut in to introduce qubit
    - mathematically, 2-dim Hilbert space, each state described by a vector
    - physically, multiple realizations, any two-level system, list a few mainstream quantum computing platform
    - [don't deviate to discuss spins and SG experiements]

- 1.1.2 State and Representation

  - Mathematical preparation (all using qubit as example)
    - Review ket and bra notation, their representation as vectors
    - Scalar product
    - Orthnormal basis

  - Formally introduce qubit again
    - What are the computational basis states
    - Generall form of pure state of a qubit
      - as linear combination of basis
      - as two component complex vector
      - a tip on how to convert betwen them
    - Borns rule, interpretation of amplitudes
    - normalization condition to ensure probability sum to 1
    - emphasize overall phase is not physical, as they do not affect measurement probability -- the only source of knowledge about the system
    - cont degrees of freedoms, write state as theta and phi, check normalization -- at this point it seems that theta and phi are just introduced as parameters no physical meaning, but then we say (theta, phi pinpoint a point on a sphere, one-to-one correspondance of a qubit state and a point on the sphere, naturally leads to conept of Bloch sphere)

  - Directly summarize X, Y, Z basis
    - Introduce and Show the Bloch sphere
    - make a table to spell out their basis states (reuse the Key Points on the Bloch Sphere table)
    - introduce spin expectation values n as theta and phi -- here we use Pauli operators without introduction, but this leaves a open question, what are they, how do we formulate physical observables 
   
- 1.1.3 Hermitian Operators
  - a opening paragraph point out all observables are represented by Hermitian operator (motivate curioucity)
  - Mathematical preparation 
    - state is described by complex parameters in state vector, but obervation (measurement outcome) must all be real. How to ensure reality?
      - complex number: z -> x= Re(z) = (z+ z*)/2, such that x = x*
      - same idea for operator, O = O^\dagger. Show definition of Hermitian operator in a box
    - Operators are matrices
      - general rules to represent an operator as a matrix: matrix element O_{ij}=<i|O|j>
      - a tip to show how to fill in the matrix given how operator acts on basis states, say X operator as example
      - Hermitian conjugate in the matrix form
    - Eigenvalues and eigenvectors (this part can follow the current note)
    - Spectral decomposition

  - Pauli Operators
    - count dof of Hermitian operators on a qubit -- only 4 linearily independent ones
    - directly introduce them in a table, table should show both spin (sigma) and quantum info (X,Y,Z) notation, with matrix form and action rules on basis states (using X,Y,Z form on 0,1 basis)
    - another table to show their spectral decomposition, show operator, split by eigenvalues, corresponding eigen states (vector form), projection operator (matrix form), projection operator (operator form like (I+Z)/2)
    - algebraic properties of Pauli operator:
      - how they multiply (see the multiplication formular in AlgebraicMethod.nb)
      - commutation relations
      - anti-commutation relations
    - expectation values
      - show the general rule
      - use qubit state as an example: (just state the result, and hide verification in dropdown box)
        - in terms of alpha, beta (complex coefficients), what is spin vector
        - in terms of theta, phi, what is spin vector


### 1.2 Measurement

- 1.2.1 Measurement Postulate

  - start with stern_gerlach experiement as a concrete example of measurement
    - show setup picture in the main pannel 
    - use a information box to discuss Z-Z-Z experiement, outside of box list what we learnt in items (outcome is binary, repeatedly measure Z can confirmed outcome -> existance of physical reality)
    - use a information box for Z-X-Z experiement, outside of box list what we learnt in items (X measurement can wash out Z measurement outcomes -> non-commuting measurement can change reality)
    (see QubitsAndEntanglement.nb in _refs for reference)

  - state the goal: build a mathematical model for outcome probability distribution P(m|psi,O) for m=+-1
    - constraint: P(m|psi,O) >=0
    - solution: model P(m|psi,O) as an expectation value of a positive semi-definite operator <psi|P_{O=m}|psi>, a box to define what is PSD operator
    - fact: repeatedly measure O on |O=m> state (the eigensate of O of eigenvalue m) will return m with probability 1 -> P_{O=m}= |O=m> <O=m|. 
    add a dropdown box to show it is indeed the case that O=m has prob 1 and O=m' (m neq m') has prob 0. (see notation in 1-1-3)

  - Directly state the measurement postulate (three axioms) use the notation developed above, state collapse can be represented using a long arrow with $O=m$ on top to denote prior state becomes posterior state (reuse some material from current note, the current Example: Probabilities and State Collapse has content leaked out, fix it)

  [current note: expectation value and variance move to 1.2.2 and projective measurement move to 1.2.3]
  - show how the theory explains SG experiement directly solving the puzzle at the begining


- 1.2.2 Uncertainty and Incompatibility

  - start with brief intro of statistics: expectation value and variance
    - define them from probability thoery
    - state the result of them for given state and observable

  - Commutator
    - A definition [A,B]=AB-BA in a box
    - out site the box briefly comment physical meaning (operator applied order)
    - example: A = take on socks, B= take on shoes, C=take on hat, AB not commuting, AC commute, -- build physical intuition: commuting ~ a sense of indenpendence
    - briefly list properties of commutators
    [No need to repeat commutator and anticommutator for Pauli]

    - a box stating Theorem: Commuting Operators Share, a dropdown box for proof, and ouside: corollary

  - Uncertainty principle
    - a box to state the Theorem
    - a note to emphasize the setting is repeated measurement of identical copies of the same state, not simutaneous or sequential measurement of a single copy of the state
    - a hidden box to prove
    
    [No complementarity, no further discussion of sequential measurement]

- 1.2.3 Measurement Operators
  - Define measurement operator in a box
    - list its properaties outside
    - a box comment on spectral dec
    - briefly remind how it is used in measurement prob and state collapse
  - A table listing measurement operators for Pauli observables
  - State Collapse as Bayesian Updating
  - Degenerate Measurements

  
### 1.3 Time Evolution

- 1.3.1 Unitary Evolution

  - introduce unitary operator
    - motivation: like a pure phase factor z* z = 1, s.t. z = e^{i theta} (theta in R)
    - math defintion U^\dagger U = I
      (implies U inverse by conjugate)
      (key property: just discuss preserve inner product (both overlap and norm))
    - Hermitian generator: U = exp(i G) such that G^\dagger = G
      - define matrix exp via Taylor
      - use spectiral decomposition to compute matrix exp
      - for U(theta)=exp(i G theta), G can be extracted from derrivative
  -  Why time evolution must be unitary? (see MatrixAlgebra argument, from information preservance) psi(t) = U(t) psi, phi(t) = U(t) phi
    - Hamiltonian as generator of unitary time evolution. U(t)=exp(-iHt)
    - Schordinger equation, derive in a box

- 1.3.2 Schordinger Picture
  - state evolves observable static
  - Show Schordinger equation again
    - Solution: time evolution operator 
    - Properties of Time-evolution operator

  - Briefly some examples for qubits
    - Rabbi oscillator
    - Spin precession
  
- 1.3.3 Heisenberg Picture
  - state static observable evolves (more like the classical physics mindset)
    because <O>(t)= <psi|U(t)dagger O U(t)|psi> has two interpretations
  - Show Heisenberg equation (no need to subscript S or H, just be simple)
    (hide derivation in box)
     - a example in a box for spin precession in Heisenberg picture
  - conserved quantitie and conservation laws
    - [A,H]=0, implies d/dt <A>=0
    - relation to symmetry, define symmetry as unitary transformation that leaves H invariant (conserved quantity generate unitary transformation)

  - Extend the discussion to introduce Lie algebra and lie group, focus on U(1) and SU(2), use qubit as example, discuss the importance of these groups in descibing fudamental interactions U(1)xSU(2)xSU(3)

**Narrative notes:**
Ch1 establishes the complete quantum framework on a single qubit: states are vectors, observables are Hermitian operators, measurement collapses and yields probabilities, dynamics is unitary. The qubit is both the simplest playground and the building block for everything that follows. The open question at the end: we know how one quantum system works — what happens when we have many?

---

## Ch2. Identical Particles

<!-- Extend the single-qubit framework to many-body systems. What new physics emerges? -->

### 2.1 Bosons and Fermions

- 2.1.1 Tensor Product

  - start with a motivating paragraph about Extend the single-qubit framework to many-body systems. What new physics emerges?
  - many-body states
    - state space: each quantum system described by Hilbert space, composition = tensor product Hilbert space (as stated in the current Key Concept box)
    - two qubits case: basis states, orthonormality
    - general case: many-body system
      [remove product state ande entangled state, they belongs to 6.2.1]
      basis (standard notation, mode label alpha can label position, momentum, spin, or just generally single-particle mode), orthonormality, representation of generic state
  - many-body operators
    - single-body operators
    - two-body operators
    - general case: operator expanded by ket bra in many-body Hilbert space
    - Example: Pauli string operator, multi-qubit system any Hermitian operator learning combination of Pauli strings with real coeff, O = \bigotimes_i O_i, where O_i=I_i,X_i,Y_i,Z_i (unify the symbol for identity operator, currently is a mix of I and mathbb I)
  
- 2.1.2 Symmetrization
  - Introduce idea of identical particle
    - analogy: money in the bank are identical, you can not talk about the $1 today vs $1 yesterday, they are indistinguishable.
    - implication of probability
    - consequence: wave funcation symmetry under permutation -> only two choices symmetric, antisymmetric

  - Symmetric and antisymmetric states (adapt from current notes)
    - To preserve symmetry, particle must be add to or removed from the system using insersion and deletion rules
    - Describe how they works (follow notes in SecondeQuantization.nb)

- 2.1.3 Second Quantization
  - compare the picture between 1st and 2nd quantization
  - Fock space 
  - Ceation annihilation operators (better make a table for side-by-side compare of bosons and fermions)
    - work out how creation/annihilation acts on bosons vs fermions states
    - summarize creation annihilation algebraic relations (commutator or anticommutator)
    - introduce number operator
   [Try to make a big table to side-by-side compare bosons and fermions in all different aspects, wave function, state space, creation anihilation, number, and so on, think of most complete comparison]

  - Boson enhancement (apply a^dagger on superposition state of multiple numbers, show that amplitude enhance by sqrt(n) for |n>)
  - Pauli exclusion (apply a^dagger on 1 fermion state, state quenched, 0 probabiility)
  [Current notes is detailed enough]

### 2.2 Angular Momentum

- 2.2.1 Angular Momentum Algebra

  - Motivate: in Ch1 we studied one qubit (spin-1/2). What about higher spin? What constrains the possible values of angular momentum?
  - Angular momentum commutation relations
    - State [J_i, J_j] = i eps_{ijk} J_k in a box — this is the defining relation
    - Physical origin: rotation generators, briefly connect to 1.3.3 (Lie algebra of SU(2))
  - Casimir operator J^2
    - commutes with all J_i, so J^2 and J_z can be simultaneously diagonalized
    - eigenvalues: J^2 = j(j+1), J_z = m, with -j <= m <= j
  - Ladder operators J_+ and J_-
    - definition, commutation relations
    - action: raise/lower m by 1
    - normalization coefficients (state in box, derive in dropdown)
  - Main result: angular momentum quantization
    - j = 0, 1/2, 1, 3/2, ... (half-integer or integer)
    - for each j, there are (2j+1) states
    - derive from ladder operator hitting the top/bottom (in dropdown)
  - Matrix representations
    - spin-1/2: recover Pauli matrices (connect back to Ch1)
    - spin-1: write out the 3x3 matrices
    - general pattern: (2j+1)-dimensional representation

- 2.2.2 Spin Representations

  - Spin as intrinsic angular momentum
    - not orbital (no r x p), purely quantum degree of freedom
    - spin-statistics connection: integer spin = bosons, half-integer = fermions (state as fact, proved in QFT)
  - Spin-1/2 in detail
    - basis states, Pauli matrices (recap from 1.1.3, now as spin operators)
    - spinor rotations: R(n,theta) = exp(-i theta n.sigma/2)
    - the 2pi mystery: spinors pick up a minus sign under 2pi rotation, need 4pi for identity
  - Spin-1
    - three basis states, 3x3 matrices
    - rotation matrices for spin-1
  - General spin-j
    - (2j+1)-dimensional irreducible representation
    - rotation operator D^j(R) = exp(-i theta n.J)
    - Wigner D-matrices (define, no need to derive)

- 2.2.3 Addition of Angular Momenta

  - The problem: two angular momenta J_1 and J_2, what is the total J = J_1 + J_2?
  - Two bases for the same space
    - uncoupled basis: |j_1, m_1> |j_2, m_2> — good quantum numbers are m_1, m_2
    - coupled basis: |j, m> — good quantum numbers are j, m
    - both are complete, related by a unitary change of basis
  - Triangle rule: j ranges from |j_1 - j_2| to j_1 + j_2 in integer steps
    - state in box, verify dimension count: sum of (2j+1) = (2j_1+1)(2j_2+1)
  - Clebsch-Gordan coefficients
    - definition: <j_1, m_1; j_2, m_2 | j, m>
    - selection rule: m = m_1 + m_2
    - properties: orthogonality, reality
    - no need to derive general formula — use tables or CG calculator
  - Key example: two spin-1/2 particles
    - 2 x 2 = 4 states: triplet (j=1, symmetric, 3 states) + singlet (j=0, antisymmetric, 1 state)
    - write out all four states explicitly
    - physical meaning: singlet is maximally entangled, zero total spin
  - Application: spin-orbit coupling
    - total J = L + S, the coupled basis diagonalizes the spin-orbit Hamiltonian
    - brief mention of fine structure (preview of perturbation theory in Ch5)

### 2.3 Anyons

- 2.3.1 Exchange Statistics

  - The question: what phase do you get when you exchange two identical particles?
  - 3D: exchange twice = identity, so phase^2 = 1, only bosons or fermions
  - 2D: exchange twice ≠ identity (topology of paths), any phase allowed
    - braid group vs permutation group
    - show figure: clockwise ≠ counterclockwise in 2D
  - Define anyons: particles with exchange phase theta ≠ 0, pi
    - abelian vs non-abelian (brief mention)
  - Charge-flux composite model (toy model for abelian anyons)
    - Aharonov-Bohm phase: theta_AB = q Phi / hbar
    - three statistics: braid, exchange, spin — all from AB phase
    - attention box: charge-on-flux and flux-on-charge are the same interaction (no double counting)
  - Summary table: 3D vs 2D

- 2.3.2 Fractional Quantum Hall Anyons

  - The fractional quantum Hall effect: filling fraction nu = 1/m, incompressible liquid
    - Laughlin wavefunction (state, don't derive)
  - Anyon excitations: fractional charge e/m, fractional statistics
    - state properties in a box
  - Apply charge-flux picture: compute braiding and exchange phases for nu = 1/3
  - Emergent statistics: the anyonic behavior is not fundamental, it emerges from many-body correlations

- 2.3.3 Toric Code

  - Particles from qubits: the simplest model of topological order
  - Hamiltonian: qubits on edges, star (A_v) and plaquette (B_p) operators
  - Excitations: e (charge, star violation) and m (flux, plaquette violation)
  - String anticommutation: Z-string crosses X-loop → phase -1 → identifies e as charge, m as pi-flux
  - Anyon statistics: all derived from string anticommutation
    - e and m are bosons (same-type strings commute)
    - epsilon = e x m is a fermion (topological spin: m orbits e within the composite, crosses once, phase -1)
    - mutual braiding table
  - Remarkable conclusion: fermions emerge from bosonic qubits
  - Quantum error correction: logical qubits in ground-state degeneracy, topological protection

**Narrative notes:**
Ch2 extends the single-qubit framework to many-body systems. The central theme is **symmetry constrains physics**: identical particles must be bosons or fermions (in 3D), angular momentum is quantized by the algebra of rotations, and in 2D, topology allows anyons. The key surprise: statistics is not always fundamental — it can emerge (toric code). The open question: we've been working in the operator formalism. Is there another way to think about quantum mechanics that connects to classical physics?

---

## Ch3. Path Integral

### 3.1 Quantization

<!-- Motivating question: Is light a particle or a wave? The historical debate of optics is the perfect
     prelude to quantum mechanics, because quantum mechanics resolves the debate by unifying both pictures.
     The three lessons follow the historical arc: particle theory → wave theory → unification.
     The punchline: Action = Phase. This single identification connects classical and quantum mechanics. -->

- 3.1.1 Geometric Optics

  - [Motivate with the historical debate: what is the nature of light? Newton's corpuscle vs Huygens' wave]
  - Particle theory of light: light travels in rays (corpuscles flying in straight lines)
  - Speed of light in a medium: v = c/n, where n is the refractive index
  - Geometrical laws from the particle picture:
    - rectilinear propagation: particles travel in straight lines in uniform media
    - reflection: angle of incidence = angle of reflection (elastic bounce)
    - refraction: Snell's law n_1 sin(theta_1) = n_2 sin(theta_2)
  - Fermat's principle: light travels the path that makes the travel time stationary
    - "stationary" not "least" — the travel time is unchanged to first order under small path variations
    - [stress this: the word is *stationary*, not *minimum*; same subtlety as Hamilton's principle later]
    - derive Snell's law from Fermat's principle
  - The action of light: travel time T = integral ds / v(x) = (1/c) integral n(x) ds
    - the optical path length integral n ds plays the role of an action
  - Geometric optics is powerful — but it cannot explain diffraction or interference
    - [set up the historical tension: the particle picture fails for some experiments]

- 3.1.2 Physical Optics

  - Wave theory of light: light is a wave with wavelength lambda and frequency omega
  - Huygens' principle: every point on a wavefront is a source of secondary wavelets
    - wavefront = surface of equal phase (constant-phase contour)
    - the new wavefront is the envelope of all secondary wavelets
  - Re-derive reflection and refraction from the wave picture
    - same predictions as geometric optics — so how do we decide between the two theories?
  - Interference and diffraction: the decisive experiments
    - Young's double slit: wave amplitude psi = psi_1 + psi_2, intensity I = |psi|^2 shows fringes
    - the wave theory wins: geometric optics cannot explain interference patterns
  - Connect amplitude to probability: intensity I = |psi|^2 gives the probability of detecting a photon
    - [foreshadow Born's rule: this is exactly the quantum mechanical interpretation]
  - Why Fermat's principle works: stationary time = stationary phase
    - the phase accumulated along a path: phi = (2 pi / lambda) integral n ds = omega T
    - when lambda is small compared to the scale of variation, only paths near the stationary-phase path contribute constructively
    - geometric optics (ray picture) emerges from wave optics in the short-wavelength limit

- 3.1.3 Particle-Wave Unification

  - [The punchline lesson: unify the particle and wave pictures]
  - The deep pattern: particle mechanics has the same structure as geometric optics
    - particle trajectory ↔ light ray
    - Hamilton's principle (stationary action) ↔ Fermat's principle (stationary time)
    - action S = integral L dt ↔ optical path integral n ds
    - classical mechanics = "ray optics" for matter
  - The key insight: **Action = Phase**
    - in optics: phase phi = (2 pi / lambda) integral n ds ∝ travel time (the optical action)
    - in mechanics: phase phi = S / hbar (the mechanical action in units of hbar)
    - this identification is the bridge from classical to quantum
  - What is "action"? Examples across physics:
    - light: optical path length (travel time × c)
    - particle (relativistic): proper time integral, S = -mc^2 integral d tau
    - particle (non-relativistic limit): S = integral (K - V) dt
    - [don't dive into field theory actions — keep it concrete]
  - Quantization = raise the action to the exponent as a phase, sum over all possibilities
    - amplitude to go A → B: sum over all paths of exp(i S[path] / hbar)
    - classical limit: when S >> hbar, only the stationary-phase path survives → classical trajectory
    - quantum regime: when S ~ hbar, all paths contribute → interference, diffraction
  - [This is Feynman's path integral — state the idea here, develop the formalism in §3.2]
  - Preview of consequences:
    - Schrödinger equation: the differential form of the path integral (§3.2)
    - WKB and Bohr-Sommerfeld: the semiclassical limit (§3.3)
    - Wick rotation: imaginary time and statistical mechanics (§3.4)

### 3.2 Schrödinger Equation from Path Integral

<!-- Theme: Phase = Action, revisited.
     3.1 ended with: ψ ~ exp(iS/ℏ), quantization = sum over paths.
     3.2 makes this precise, derives Schrödinger, then closes the loop:
     the propagator for a free particle IS exp(iS_cl/ℏ) — Phase = Action.
     Arc: propagator framework → infinitesimal time slice → Schrödinger equation → free particle solution → propagator = exp(iS_cl/ℏ). -->

- 3.2.1 Path Integral Formulation

  - **Propagator**: define K(x,t; x',t') as the amplitude for a particle at x' at time t' to be found at x at time t. This is the central object — it determines everything:
    - ψ(x,t) = ∫ K(x,t; x',t') ψ(x',t') dx'
    - [box: propagator definition and its role]
  - **Feynman's path integral**: K = ∫ D[x(t)] exp(iS[x]/ℏ) — sum over ALL paths from (x',t') to (x,t), weighted by exp(iS/ℏ). This is the quantization rule from §3.1.3 made precise.
  - **Infinitesimal propagator** (one time slice δt): now focus on what happens over a single small step. For Lagrangian L = ½m(dx/dt)² − V(x), the action over δt is:
    - S_slice = ½ m (x − x')²/δt − V(x) δt
    - [box; derive from L·δt with velocity ≈ (x−x')/δt in dropdown]
  - The time-slice path integral formula:
    - ψ(x, t+δt) = C ∫ exp(iS_slice/ℏ) ψ(x', t) dx'
    - This is Huygens' principle for matter waves (cf. §3.1.2): each point x' sends a wavelet to x, weighted by phase exp(iS/ℏ).
    - [box: time-slice formula]

- 3.2.2 Deriving the Schrödinger Equation

  - Take δt → 0 and Taylor expand both sides of the time-slice formula.
  - **Step 1: Gaussian integral over x'**
    - Substitute δx = x' − x. The kinetic phase exp(imδx²/2ℏδt) oscillates rapidly except near δx ≈ 0 (width ~ √(ℏδt/m)).
    - Expand ψ(x+δx, t) in Taylor series: ψ + δx ∂ψ/∂x + ½δx² ∂²ψ/∂x²
  - **Step 2: Evaluate the Gaussian moments**
    - ⟨1⟩ = √(2πiℏδt/m), ⟨δx⟩ = 0, ⟨δx²⟩ = iℏδt/m
    - [box: Gaussian moment formulas; derivation in dropdown]
  - **Step 3: Collect terms to O(δt)**
    - LHS: ψ + δt ∂ψ/∂t. RHS: after Gaussian integration and expanding the potential phase.
    - Normalization fixed: C = √(m/2πiℏδt).
    - O(δt) terms give: **iℏ ∂ψ/∂t = −(ℏ²/2m) ∂²ψ/∂x² + V(x)ψ**
    - [box: Schrödinger equation — THE key result of this unit]
  - The Schrödinger equation is not postulated — it is derived from the path integral.
  - Two equivalent pictures: path integral (global, sum over histories) ↔ Schrödinger equation (local, differential equation).

- 3.2.3 Free Particle Propagator

  - Apply the Schrödinger equation to the simplest case: V = 0.
  - **Plane wave solution**: ψ = exp(ikx − iωt) solves the free Schrödinger equation with ω = ℏk²/2m (E = p²/2m). [box]
  - **Propagator from plane waves**: the propagator is built by superposition — sum plane waves over all k:
    - K(x,t; x',0) = ∫ dk/(2π) exp(ik(x−x') − iℏk²t/2m)
    - This is a Gaussian integral in k. Evaluate it:
    - K = √(m/2πiℏt) exp(im(x−x')²/2ℏt)
    - [box: free particle propagator; Gaussian evaluation in dropdown]
  - **Phase = Classical Action**: the exponent is (i/ℏ) × m(x−x')²/2t. But m(x−x')²/2t is exactly the classical action for a free particle traveling from x' to x in time t (straight-line path, constant velocity).
    - The propagator is: K = (normalization) × exp(iS_cl/ℏ)
    - [box: K ~ exp(iS_cl/ℏ) — the Phase = Action theme from §3.1.3 realized]
  - **Closing the circle**: §3.1 proposed ψ ~ exp(iS/ℏ). §3.2.1 formalized the path integral. §3.2.2 derived Schrödinger. Now the free particle confirms: the propagator is the exponential of the classical action. Phase = Action is not just an analogy — it is exact for the free particle, and approximately true in general (→ §3.3 stationary phase).

### 3.3 Stationary Phase

- 3.3.1 Stationary Phase Approximation

  - The mathematical method: for integrals of the form integral f(x) exp(i g(x)/epsilon), as epsilon → 0 the dominant contribution comes from stationary points of g(x)
  - State the result: integral ~ f(x_0) exp(i g(x_0)/epsilon) sqrt(2 pi epsilon / |g''(x_0)|)
    - box for formula, dropdown for derivation
  - Apply to path integral: as hbar → 0, the dominant path is delta S = 0 (classical path)
    - quantum fluctuations: second variation of S gives Gaussian corrections
  - The correspondence principle made precise: classical mechanics = stationary phase of quantum mechanics

- 3.3.2 WKB Approximation

  - Ansatz: psi(x) = A(x) exp(i phi(x) / hbar)
    - substitute into Schrödinger equation, expand in powers of hbar
    - leading order: Hamilton-Jacobi equation for phi → classical trajectory
    - next order: amplitude A determined by probability conservation
  - WKB wavefunction in classically allowed / forbidden regions
  - Connection formulas at turning points (state, don't fully derive)
  - Tunneling: exponential suppression exp(-1/hbar integral |p| dx) in classically forbidden region

- 3.3.3 Bohr-Sommerfeld Quantization

  - For bound states: single-valuedness of wavefunction → quantization condition
    - oint p dx = (n + 1/2) 2 pi hbar
    - the 1/2 comes from turning point phases (Maslov index)
  - Apply to harmonic oscillator: recover E_n = (n + 1/2) hbar omega exactly
  - Apply to hydrogen atom: recover Bohr energy levels (approximately)
  - Connection to path integral: quantization = constructive interference of periodic orbits

### 3.4 Imaginary Time

- 3.4.1 Wick Rotation

  - Replace t → -i tau (imaginary time, or Euclidean time)
  - The propagator becomes: K_E = integral D[x] exp(-S_E / hbar)
    - oscillating integrand → decaying integrand (much better behaved!)
  - Euclidean action S_E: minus sign on kinetic energy, like a particle in inverted potential
  - Connection to statistical mechanics: exp(-S_E / hbar) looks like a Boltzmann weight

- 3.4.2 Statistical Mechanics

  - The key identity: exp(-beta H) is the imaginary-time evolution operator with tau = beta hbar
    - the thermal density matrix IS the imaginary-time propagator
  - Partition function Z = Tr exp(-beta H) = integral K_E(x, beta hbar; x, 0) dx
    - sum over all closed paths in imaginary time (periodic boundary conditions)
  - Thermal averages from path integral: <O> = (1/Z) integral D[x] O[x] exp(-S_E / hbar)
  - Free energy, internal energy, entropy — all from Z
  - Key insight: quantum mechanics at finite temperature = classical statistical mechanics in one higher dimension

- 3.4.3 Instantons

  - Goal: compute the energy splitting Delta of a double-well potential using the Euclidean path integral
  - Step 1 — the transition amplitude in terms of energy eigenstates:
    - <a| exp(-HT/hbar) |-a> = sum over n of psi_n(a) psi_n*(-a) exp(-E_n T/hbar)
    - for large T, dominated by the two lowest states E_± = E_0 ± Delta
    - simplifies to: exp(-E_0 T/hbar) sinh(Delta T / hbar)
  - Step 2 — the same amplitude from the path integral: dilute instanton gas
    - the instanton: classical solution in the inverted potential, rolling from -a to +a in Euclidean time
    - single instanton has action S_0, contributes K exp(-S_0/hbar) where K is a fluctuation prefactor
    - over long time T, the particle can tunnel back and forth many times (I, I-Ibar-I, ...)
    - to go from -a to +a: odd number of transitions
    - dilute gas approximation: instantons are widely separated, sum independently
    - sum over odd n: sum (K exp(-S_0/hbar) T)^n / n! = sinh(K exp(-S_0/hbar) T)
  - Step 3 — match the two expressions:
    - same sinh structure → Delta = hbar K exp(-S_0/hbar)
    - the exponential factor exp(-S_0/hbar) agrees with WKB tunneling
    - the instanton method additionally determines the prefactor K
  - Why splitting happens: without tunneling, two degenerate ground states (one per well); the instanton "links" the wells, forcing the states to hybridize into symmetric/antisymmetric combinations
  - [the prefactor K involves a functional determinant — mention but don't derive in detail]

**Narrative notes:**
Ch3 answers "how does classical physics emerge?" The path integral is the bridge: quantum mechanics is a sum over all paths, classical mechanics is the single path that dominates when hbar is small. The optics analogy (wave optics → ray optics = quantum → classical) provides the intuition. Stationary phase, WKB, and Bohr-Sommerfeld make the classical limit quantitative. Imaginary time reveals a deep connection: quantum dynamics ↔ statistical mechanics. The open question: the path integral involves phase exp(i S / hbar). What is the physical meaning of this phase? What happens when a charged particle moves in a field and the phase becomes geometric?

---

## Ch4. Phase and Gauge

<!-- The chapter has one through-line: phase is physical.
     4.1 discovers gauge fields from phase invariance, then finds they describe electromagnetism.
     4.2 elevates phase to the central observable: Berry phase, Aharonov-Bohm, flux ring physics.
     4.3 applies gauge coupling to uniform B: Landau levels and the quantum Hall effect.
     4.4 reveals the deepest surprise: spin itself emerges from gauge topology (monopole harmonics). -->

### 4.1 Gauge Field

- 4.1.1 Gauge Principle

  - Phase ambiguity: the wavefunction psi and e^{i alpha} psi describe the same physics
    - this is a global U(1) symmetry
  - Promote to local: psi(x) → e^{i alpha(x)} psi(x) — does physics still remain invariant?
    - No! The derivative d/dx picks up an extra term from the spatially varying phase
  - Fix it: introduce a gauge field A that absorbs the extra term
    - covariant derivative: D = d - i (q/hbar) A, transforms covariantly under local phase rotation
  - Rewrite the gauge-invariant Hamiltonian: H = (p - qA)^2 / 2m + q Phi
    - [this is forced on us by the requirement of local phase invariance — we haven't assumed electromagnetism]

- 4.1.2 Electromagnetic Coupling

  - What does this Hamiltonian describe? Study the Heisenberg equations of motion
    - compute d<x>/dt → kinetic momentum pi = p - qA
    - compute d<pi>/dt → find m a = q(E + v x B)
    - [this IS the Lorentz force!]
  - Meanwhile, identify E and B from the gauge potentials:
    - E = -grad Phi - dA/dt, B = curl A
    - field strength tensor F_{mu nu} = d_mu A_nu - d_nu A_mu encodes both
  - The discovery: demanding local phase invariance of quantum mechanics automatically produces electromagnetism
    - the gauge field A IS the electromagnetic vector potential
    - the gauge principle doesn't just accommodate EM — it *requires* it

- 4.1.3 Gauge Invariance

  - Gauge transformations: how psi, A, Phi transform consistently
    - psi → e^{i alpha} psi, A → A + (hbar/q) grad alpha, Phi → Phi - (hbar/q) d alpha/dt
    - the Schrödinger equation is invariant under the combined transformation
  - What is gauge-invariant (physical): charge density rho, current j, E, B, energy levels, transition probabilities
  - What is gauge-dependent (unphysical): A, Phi, canonical momentum p, the phase of psi
    - canonical momentum p vs kinetic momentum pi = p - qA: only pi is gauge-invariant
  - [summary: gauge symmetry is not a symmetry of nature — it is a redundancy of description]

### 4.2 Berry Phase

<!-- Berry phase is the central concept of this chapter: phase accumulated along a path.
     The Aharonov-Bohm effect is Berry phase in real space. The flux ring is the concrete model.
     By placing Berry phase here (not at the end), everything that follows becomes an application. -->

- 4.2.1 Berry Phase

  - Phase accumulated adiabatically along a path in parameter space
    - adiabatic theorem: slow changes keep the system in the instantaneous eigenstate
    - the phase is NOT just the dynamical phase integral E dt — there is a geometric piece
    - Berry phase: gamma = i oint <n| grad_R |n> . dR
  - Berry connection A_n = i <n| grad_R |n> — a gauge field in parameter space
    - Berry curvature F = curl A — gauge-invariant, physically measurable
  - Connect to Phase = Action from Ch3:
    - d/dx (phase) = momentum → de Broglie relation p = hbar k
    - d/dt (phase) = energy → Planck relation E = hbar omega
    - A and Phi are "potential momentum" and "potential energy" that shift the phase
    - a particle moving through a gauge field accumulates Berry phase = (q/hbar) integral A . dx - (q/hbar) integral Phi dt
  - Key example: spin-1/2 in a slowly rotating B field
    - Berry phase = half the solid angle subtended by B on the sphere

- 4.2.2 Aharonov-Bohm Effect

  - Berry phase induces interference in an electromagnetic field
  - Setup: charged particle moves around a solenoid (B = 0 outside, but A ≠ 0)
    - two paths around the solenoid acquire different Berry phases
    - relative phase = (q/hbar) times enclosed magnetic flux
    - interference pattern shifts with flux, even though the particle never enters B ≠ 0
  - Physical meaning: the gauge potential A is physically real in quantum mechanics
    - classically, only E and B matter; quantum mechanically, A matters through phase
  - Flux quantization: single-valuedness of wavefunction demands Phi = n Phi_0
    - flux quantum Phi_0 = h/q (or h/2e for Cooper pairs in superconductors)
  - Experimental confirmation (Tonomura et al.)

- 4.2.3 Flux Ring

  - Concrete model: a charged particle on a ring of radius R threaded by magnetic flux Phi
  - Hamiltonian in angular coordinate theta:
    - H = (1/2mR^2)(p_theta - q Phi / 2 pi)^2
    - [just the free-particle-on-a-ring Hamiltonian with a shifted angular momentum]
  - Eigenstates: e^{i n theta}, eigenvalues: E_n = (hbar^2 / 2mR^2)(n - Phi/Phi_0)^2
    - energy spectrum is periodic in flux with period Phi_0 — the AB effect in action
  - Physical consequences:
    - tunneling rate across half ring depends on flux (direct verification of AB phase)
    - persistent current: I = -dE/dPhi — current flows in the ground state!
    - application: SQUID (superconducting quantum interference device)
  - Special case: Phi = Phi_0/2 (pi-flux)
    - ground state becomes doubly degenerate (n=0 and n=1 have same energy)
    - protected by time-reversal + translation symmetry
    - [connection to quantum anomaly: the degeneracy cannot be lifted without breaking a symmetry]

### 4.3 Landau Level

- 4.3.1 Cyclotron Motion

  - Classical charged particle in uniform B field
    - Lorentz force → circular orbits (cyclotron motion)
    - cyclotron frequency: omega_c = qB/m
    - magnetic length: l_B = sqrt(hbar/qB) — the characteristic quantum scale
  - Classical Hall effect: crossed E and B fields → Hall voltage, Hall resistance R_H = B/nq
  - But at low temperature: the integer quantum Hall effect
    - Hall conductance sigma_xy = n e^2/h, exactly quantized to integer multiples
    - why? This demands a quantum explanation → need Landau levels

- 4.3.2 Landau Quantization

  - Semiclassical quantization (Bohr-Sommerfeld from §3.3): circular orbit area quantized
    - E_n = (n + 1/2) hbar omega_c — preview of exact result
  - Quantum Hamiltonian: H = (p - qA)^2 / 2m in uniform B
  - Landau gauge A = (0, Bx, 0): p_y is conserved, problem reduces to shifted harmonic oscillator
    - energy levels: E_n = (n + 1/2) hbar omega_c — exact! Massively degenerate.
    - guiding center coordinates: [X, Y] = i l_B^2 (noncommuting!)
    - two sets of ladder operators: a, a† (energy) and b, b† (guiding center / degeneracy)
    - quantum numbers: n (Landau level index), m (guiding center position)
  - Complex coordinate z = x + iy: wavefunctions in symmetric gauge
    - lowest Landau level: psi ~ z^m exp(-|z|^2 / 4 l_B^2) — analytic functions × Gaussian
    - degeneracy per Landau level = total flux / flux quantum = BA / Phi_0

- 4.3.3 Quantum Hall Effect

  - Filling Landau levels: filling factor nu = N_electrons / N_states = n hbar / (eB) × (2 pi)
    - integer filling → completely filled Landau levels → gap to excitations
  - Charge pumping argument for quantized Hall conductance
    - thread one flux quantum through a Corbino disk → exactly one charge transferred
    - sigma_xy = e / Phi_0 = e^2/h per filled level → sigma_xy = n e^2/h
  - Fractional quantum Hall effect: sigma_xy = (p/q) e^2/h at fractional filling
    - connect back to Ch2 anyons: quasiparticles with fractional charge and fractional statistics
  - [the quantum Hall effect sits at the intersection of gauge physics, topology, and many-body physics]

### 4.4 Spin and Monopole

<!-- The deepest result: spin-1/2 is not an independent axiom — it emerges from gauge topology.
     The classical spinning top motivates angular momentum, the monopole provides the gauge field,
     and monopole harmonics show that half-integer angular momentum arises naturally. -->

- 4.4.1 Classical Spin

  - The classical spinning top: angular momentum L from rotational motion
    - decomposition: orbital L = r x p vs spin S (intrinsic angular momentum of the body)
  - Precession in a torque: dL/dt = tau → Larmor precession in a magnetic field
  - The electromagnetic analogy: a spinning charge generates a magnetic dipole
    - gyromagnetic ratio g relates angular momentum to magnetic moment: mu = g (q/2m) L
  - The puzzle: orbital angular momentum is always integer (single-valued wavefunctions on a sphere)
    - but experiments show half-integer angular momentum (Stern-Gerlach)
    - where does spin-1/2 come from? [the monopole will answer this]

- 4.4.2 Dirac Monopole

  - Electromagnetic analogy: what if magnetic charges existed?
    - div B = rho_m ≠ 0, but B = curl A implies div B = 0 — contradiction
  - Dirac's resolution: A must have a string singularity (Dirac string)
    - write down the gauge field configuration for a monopole
    - the string is unphysical if the AB phase around it is trivial: exp(i q g / hbar) = 1
    - Dirac quantization condition: q g = n hbar/2
  - Remarkable consequence: if one monopole exists anywhere, all electric charges are quantized
  - Two-patch formulation: cover the sphere with two gauge patches (north/south)
    - the patches are related by a gauge transformation on the overlap (the equator)
    - the winding number of the transition function = monopole charge (topology of U(1) bundle)

- 4.4.3 Monopole Harmonics

  - Wavefunctions on a sphere with a monopole at the center
    - Hamiltonian: kinetic energy on the sphere with gauge field A_monopole
    - Schrödinger equation → modified angular equation
  - SU(2) symmetry: total angular momentum J = L + (monopole contribution)
    - angular momentum algebra still works: [J_i, J_j] = i epsilon_{ijk} J_k
    - but j >= |q| where q is the monopole quantum number
    - states labeled |q, j, m> with monopole harmonics Y_{q,j,m}
  - The punchline: when q = 1/2, the monopole harmonics ARE spin-1/2 spinors
    - half-integer angular momentum = orbital motion in a monopole background
    - spin is not a separate axiom — it emerges from gauge topology
    - [deep connection: the topology of the U(1) gauge bundle on S^2 encodes the spin]
  - [connection to Berry phase from §4.2: the Berry curvature of spin-1/2 IS the field of a monopole at the origin of parameter space]

**Narrative notes:**
Ch4 reveals that phase is not just a number — it is geometric and physical. The gauge principle (4.1) shows that local phase invariance requires the electromagnetic field. Berry phase (4.2) makes phase accumulation the central observable, with Aharonov-Bohm and the flux ring as concrete realizations. Landau levels (4.3) apply gauge coupling to uniform B, culminating in the quantum Hall effect. The deepest surprise comes last (4.4): spin-1/2 itself is not an independent postulate but emerges from gauge topology through the monopole. The open question: all these exact results rely on symmetry or topology. What do we do when the problem is too complicated to solve exactly?
---

## Ch5. Perturbation Theory — When Exact Solutions Fail

<!-- The reference notebook (Tong) organizes perturbation theory around a clear pedagogical arc:
     Time-independent: toy model (2x2 qubit) → non-degenerate PT (Hellmann-Feynman approach) → degenerate PT (effective Hamiltonian)
     Time-dependent: interaction picture → Dyson series → Green's function → Feynman diagrams → Fermi's golden rule → adiabatic process
     Our outline follows this arc closely, keeping the Hellmann-Feynman theorem as the organizing principle. -->

### 5.1 Time-Independent Perturbation Theory

- 5.1.1 Toy Model

  - Motivation: most quantum systems cannot be solved exactly
    - strategy: start from a solvable H_0, add a small perturbation lambda V
  - General idea: expand eigenvalues and eigenstates as power series in lambda
    - E_n = E_n^(0) + lambda E_n^(1) + lambda^2 E_n^(2) + ...
    - |n> = |n^(0)> + lambda |n^(1)> + ...
  - A 2x2 qubit model: H = H_0 + lambda V
    - solve exactly by diagonalization (it's just a 2x2 matrix)
    - Taylor expand the exact eigenvalues in lambda → see the perturbative series emerge
  - Key physics: level repulsion
    - two levels that would cross at lambda = 0 instead repel each other
    - the gap is proportional to the matrix element <1|V|2>
  - Convergence: the series works when lambda V is small compared to the energy gap
    - breakdown when perturbation ~ energy gap → preview of degenerate PT

- 5.1.2 Non-Degenerate Perturbation Theory

  - Setup: H(lambda) = H_0 + lambda V, non-degenerate spectrum of H_0
  - The Hellmann-Feynman theorem: dE_n/d(lambda) = <n(lambda)| dH/d(lambda) |n(lambda)>
    - the exact energy derivative equals the expectation value of the perturbation in the exact eigenstate
    - [this is the organizing principle: energy corrections follow from expectation values]
  - First-order energy: E_n^(1) = <n^(0)|V|n^(0)>
    - Hellmann-Feynman at lambda=0: just the expectation value of V in the unperturbed state
  - First-order state: |n^(1)> = sum_{m≠n} <m^(0)|V|n^(0)> / (E_n^(0) - E_m^(0)) |m^(0)>
    - state acquires admixture of other levels, weighted by matrix element / energy gap
  - Second-order energy: E_n^(2) = sum_{m≠n} |<m^(0)|V|n^(0)>|^2 / (E_n^(0) - E_m^(0))
    - Hellmann-Feynman applied to the first-order corrected state
    - always lowers the ground state energy (variational principle)
  - Physical intuitions:
    - energy correction = expectation value of perturbation (1st order) + virtual transitions (2nd order)
    - state correction = hybridization with nearby levels
    - perturbation theory fails when energy denominators vanish → degeneracy!
  - Application: verify against the exact qubit model from §5.1.1

- 5.1.3 Degenerate Perturbation Theory

  - The problem: if E_n^(0) = E_m^(0), the non-degenerate formulas diverge
    - the perturbation lifts the degeneracy — but which linear combinations are the right zeroth-order states?
  - Generalized Hellmann-Feynman: within the degenerate subspace, V acts as an effective matrix
    - diagonalize V within the degenerate subspace → picks the correct zeroth-order states
    - first-order energies = eigenvalues of V restricted to the degenerate subspace
  - Effective Hamiltonian: project H onto the degenerate subspace
    - H_eff = P H P, where P projects onto the degenerate subspace
    - includes both direct (1st order) and virtual (2nd order) contributions from outside the subspace
    - [the effective Hamiltonian is the systematic tool for degenerate PT]
  - Application: spin-1 model (three-fold degeneracy split by perturbation)
  - Comparison: degenerate vs non-degenerate — when to use which, and how they connect

### 5.2 Time-Dependent Perturbation Theory

- 5.2.1 Interaction Picture

  - Setup: H(t) = H_0 + V(t), where V(t) may be time-dependent
  - Three pictures of quantum mechanics:
    - Schrödinger picture: states evolve, operators fixed
    - Heisenberg picture: operators evolve, states fixed
    - Interaction picture: states evolve with V, operators evolve with H_0
  - Interaction picture formalism:
    - |psi_I(t)> = e^{iH_0 t/hbar} |psi_S(t)>
    - V_I(t) = e^{iH_0 t/hbar} V(t) e^{-iH_0 t/hbar}
    - equation of motion: i hbar d/dt |psi_I> = V_I(t) |psi_I>
  - Dyson series: the formal solution for the time-evolution operator
    - U_I(t) = T exp(-i/hbar integral_0^t V_I(t') dt')
    - expand order by order: U_I = 1 + U^(1) + U^(2) + ...
    - time-ordering operator T: later times to the left
  - Green's function: the retarded propagator G(t) = -i theta(t) U_I(t)
    - [connection to Feynman propagator and path integral from Ch3]
  - Feynman diagrams: pictorial representation of each term in the Dyson series
    - vertices = interactions, lines = free propagation
    - [brief introduction — systematic diagrammatics is for a QFT course]

- 5.2.2 Fermi's Golden Rule

  - Transition amplitude: c_{i→f}(t) = <f| U_I(t) |i> — amplitude to go from |i> to |f>
  - First-order transition probability: P_{i→f} = |c_{i→f}^(1)|^2
  - For a constant perturbation turned on at t=0:
    - P ~ |<f|V|i>|^2 (sin((E_f - E_i)t/2hbar) / (E_f - E_i)/2)^2
    - the sinc-squared function peaks at E_f = E_i: energy conservation emerges at long times
  - Transition rate — Fermi's golden rule:
    - Gamma_{i→f} = (2 pi / hbar) |<f|V|i>|^2 rho(E_i)
    - rate = matrix element squared × density of final states
  - Selection rules: transitions forbidden when matrix elements vanish by symmetry
  - Adiabatic process: when V(t) changes slowly compared to energy gaps
    - the system stays in the instantaneous eigenstate (adiabatic theorem)
    - connection to Berry phase (§4.2): the geometric phase accumulated during adiabatic evolution

- 5.2.3 Applications

  - Harmonic perturbation: V(t) = V cos(omega t)
    - resonance condition: hbar omega = E_f - E_i (absorption) or E_i - E_f (stimulated emission)
    - connection to spectroscopy: probe energy levels by scanning omega
  - Electric dipole transitions: coupling to light
    - selection rules for hydrogen: Delta l = ±1, Delta m = 0, ±1
  - Lifetime and linewidth: Gamma gives the decay rate, Delta E ~ hbar Gamma (energy-time uncertainty)
  - Linear response and Hall conductance:
    - apply time-dependent PT to compute current response to an electric field
    - Kubo formula: sigma_xy = sum_{n≠m} f(E_n)(1-f(E_m)) 2 Im(<n|j_x|m><m|j_y|n>) / (E_n - E_m)^2
    - for filled Landau levels: sigma_xy = n e^2/h — exact quantization from perturbation theory!
    - [connects Ch5 back to §4.3: the quantum Hall effect is a linear response result]

**Narrative notes:**
Ch5 provides the practical toolkit for problems that can't be solved exactly. The organizing principle is Hellmann-Feynman: energy corrections are expectation values. The toy model builds intuition (level repulsion), non-degenerate PT gives the workhorse formulas, and degenerate PT introduces the effective Hamiltonian. Time-dependent PT leads to Fermi's golden rule (transition rates) and the Kubo formula (linear response), connecting back to the quantum Hall effect. The open question: perturbation theory assumes a pure state and unitary evolution. What happens when the system interacts with an environment? What is lost, and what new physics emerges?
---

## Ch6. Quantum Foundations — Open Systems and Information

<!-- Ch6 revisits the foundations with mature tools. The arc:
     6.1 extends quantum states beyond pure states (density matrix, entropy, thermal physics)
     6.2 explores the most quantum phenomenon (entanglement, Bell inequality)
     6.3 generalizes measurement (POVM, quantum channels)
     6.4 confronts reality: decoherence = measurement + forgetting, master equation, error correction -->

### 6.1 Density Matrix

- 6.1.1 Mixed States

  - Motivation: so far, we assumed complete knowledge of the quantum state (pure state). What if we don't?
  - Classical ignorance: an ensemble of possible states {p_i, |psi_i>}
    - can't describe with a single ket — need a new object
  - Density matrix: rho = sum p_i |psi_i><psi_i|
    - properties: Hermitian, positive semi-definite, Tr(rho) = 1
  - Pure state: rho = |psi><psi|, satisfies rho^2 = rho, Tr(rho^2) = 1
  - Mixed state: rho^2 ≠ rho, Tr(rho^2) < 1
    - purity Tr(rho^2) as a measure of "how mixed"
  - Expectation values: <O> = Tr(rho O) — the density matrix encodes all measurable information
  - Time evolution: i hbar d rho/dt = [H, rho] (von Neumann equation)
  - Ensemble ambiguity: different ensembles can give the same rho → same physics
    - the density matrix is the physical object, not the ensemble

- 6.1.2 Entropy

  - Von Neumann entropy: S(rho) = -Tr(rho ln rho)
    - S = 0 for pure states, S = ln d for maximally mixed state in d dimensions
  - Properties: non-negative, invariant under unitaries, concave
  - Connection to information: S measures how much we don't know about the state
  - Maximum entropy principle: among all rho with a given <H>, the one that maximizes S is
    - rho = exp(-beta H) / Z, where Z = Tr(exp(-beta H))
    - [this DERIVES the thermal state — the Boltzmann distribution is not an assumption but a consequence of maximum ignorance]
  - Partition function Z and thermodynamics: F = -k_B T ln Z, <E> = -d(ln Z)/d(beta)

- 6.1.3 Quantum Statistics

  - Apply max-entropy thermal state to a single bosonic mode: H = epsilon b^dagger b
    - thermal density matrix: rho = exp(-beta epsilon b^dagger b) / Z
    - partition function: Z = 1/(1 - exp(-beta epsilon))
    - average occupation: <n> = 1/(exp(beta epsilon) - 1) — the Bose-Einstein distribution
    - [chemical potential = 0 for simplicity; one mode is sufficient to see the physics]
  - Apply to a single fermionic mode: H = epsilon c^dagger c
    - c^dagger c has eigenvalues 0, 1 only (Pauli exclusion)
    - Z = 1 + exp(-beta epsilon)
    - average occupation: <n> = 1/(exp(beta epsilon) + 1) — the Fermi-Dirac distribution
  - Comparison: bosons bunch (can pile up), fermions exclude (at most one per state)
    - [connects back to Ch2: statistics constrains thermodynamics]
  - The classical limit: when exp(beta epsilon) >> 1, both reduce to Boltzmann distribution

### 6.2 Entanglement

- 6.2.1 Composite Systems

  - Composite Hilbert space: H_AB = H_A tensor H_B (recall §2.1.1, now with density matrix language)
  - The partial trace: rho_A = Tr_B(rho_AB)
    - goal: rho_A must reproduce all expectation values <O_A> = Tr(rho_AB (O_A tensor I_B))
    - computation: define partial trace via basis, work through examples
    - physical meaning: "trace out" the degrees of freedom you don't observe → the environment
  - Key result: even if rho_AB is pure, rho_A can be mixed
    - this is the signature of entanglement
  - Product states vs entangled states:
    - product: rho_AB = rho_A tensor rho_B, or |psi_AB> = |phi_A> tensor |chi_B>
    - entangled: cannot be written as a product → reduced state is mixed
  - Schmidt decomposition: any bipartite pure state = sum lambda_k |a_k>|b_k>
    - Schmidt rank 1 = product, rank > 1 = entangled
  - Entanglement entropy: S(rho_A) for a pure bipartite state
    - S = 0 iff product state; measures "how entangled"

- 6.2.2 Entanglement Measures

  - Entanglement entropy (recap): the standard measure for pure bipartite states
  - Concurrence (for two qubits): a computable entanglement measure for mixed states
    - definition, formula, relation to entanglement of formation
  - Entanglement witnesses: operators W such that Tr(W rho) < 0 detects entanglement
    - can detect entanglement without full state tomography
  - The hierarchy of quantum correlations:
    - separable ⊂ PPT (positive partial transpose) ⊂ all states
    - separable states can have classical correlations but no entanglement
  - Bell states: four maximally entangled two-qubit states
    - write them out, show they form an orthonormal basis
    - each has S(rho_A) = ln 2 (maximum for a qubit)

- 6.2.3 Bell Inequality

  - EPR paradox: entangled particles seem to have "spooky action at a distance"
    - EPR's argument: quantum mechanics must be incomplete — hidden variables?
  - Bell's theorem: no local hidden variable theory can reproduce all quantum predictions
  - CHSH inequality: |<CHSH>| <= 2 for any local hidden variable theory
    - quantum mechanics allows up to 2 sqrt(2) (Tsirelson's bound)
    - the singlet state achieves this maximum violation
  - Experimental tests: loophole-free Bell tests (2015) confirm quantum mechanics
  - No-communication theorem: entanglement enables correlations, not signaling
  - Quantum teleportation: using entanglement + classical communication to transmit a quantum state
    - the protocol, why it doesn't violate no-communication

### 6.3 Generalized Measurement

- 6.3.1 Projective Measurement

  - Recap of measurement postulate from Ch1, now in density matrix language
    - outcome probability: p_m = Tr(P_m rho)
    - post-measurement state: rho → P_m rho P_m / p_m
  - Repeated measurements and the quantum Zeno effect
    - frequent measurement freezes evolution
  - Compatible observables: commuting operators can be measured simultaneously

- 6.3.2 POVM

  - Motivation: projective measurement is not the most general measurement
  - POVM (Positive Operator-Valued Measure): a set {E_m} with E_m >= 0, sum E_m = I
    - outcome probability: p_m = Tr(E_m rho)
    - more general than projective: E_m need not be projectors, need not be orthogonal
  - Why POVMs? They describe measurements on a subsystem, or measurements with noise
  - Example: unambiguous state discrimination
    - two non-orthogonal states cannot be perfectly distinguished
    - POVM allows: "state 1", "state 2", or "inconclusive" — never wrong, sometimes unsure
  - Connection to projective measurement on a larger system (Naimark's theorem)

- 6.3.3 Quantum Channels

  - Motivation: what is the most general evolution of a density matrix?
    - unitary evolution is reversible: rho → U rho U†
    - what about irreversible processes? (measurement, decoherence, noise)
  - Quantum channel: a completely positive, trace-preserving (CPTP) map
  - Kraus representation: rho → sum K_i rho K_i†, with sum K_i† K_i = I
  - Common channels:
    - depolarizing: rho → (1-p) rho + p I/d
    - dephasing: off-diagonal elements decay
    - amplitude damping: models spontaneous emission
  - Unitary evolution and projective measurement are special cases of quantum channels

### 6.4 Open Quantum Systems

- 6.4.1 Decoherence

  - The problem: isolated quantum systems maintain coherence forever. Real systems don't.
  - Decoherence: interaction with environment → off-diagonal elements of rho decay
    - start with |psi> = (|0> + |1>)/sqrt(2), entangle with environment, trace out environment
    - pure state → mixed state: the superposition "looks classical"
  - The key insight: decoherence = measurement by the environment, then forgetting the outcome
    - environment "measures" the system (entanglement), but nobody reads the result (partial trace)
    - this IS a quantum channel: the dephasing channel emerges from this picture
    - [connect to §6.3.3: decoherence is a specific quantum channel]
  - Decoherence timescale: typically very fast for macroscopic systems
    - explains why we don't see macroscopic superpositions
  - Decoherence-free subspaces: subspaces immune to certain types of environment coupling

- 6.4.2 Lindblad Master Equation

  - Goal: equation of motion for rho of a system coupled to an environment
    - start from unitary evolution of system + environment, trace out environment
  - Lindblad equation: d rho/dt = -i[H, rho] + sum gamma_k (L_k rho L_k† - 1/2 {L_k† L_k, rho})
    - first term: unitary (Hamiltonian) evolution
    - second term: dissipation, described by Lindblad (jump) operators L_k
  - Physical meaning of Lindblad operators:
    - L = |0><1|: spontaneous emission (amplitude damping)
    - L = sigma_z: pure dephasing (connects back to §6.4.1)
  - Steady states: d rho/dt = 0 — the system relaxes to equilibrium
    - for thermal bath: steady state is the thermal state rho = exp(-beta H)/Z from §6.1.2
  - Quantum jump interpretation: between jumps, system evolves with non-Hermitian H_eff; at random times, a jump L_k occurs
    - [connects back to measurement: each jump is a measurement event]

- 6.4.3 Error Correction

  - The problem: decoherence and noise destroy quantum information. Can we protect it?
  - No-cloning theorem: cannot copy unknown quantum states → classical repetition code fails
  - Quantum error correction: encode logical qubits in entangled states of many physical qubits
    - 3-qubit bit-flip code: encode |0> → |000>, |1> → |111>
    - measure syndrome (parity checks), correct without measuring the logical qubit
    - [key idea: measure WHAT error occurred, not WHAT state the qubit is in]
  - General framework: stabilizer codes, code distance
  - Connection to toric code (§2.3.3): topological error correction as the most robust approach
    - the anyonic excitations of Ch2 reappear as error syndromes
  - Threshold theorem: below a critical error rate, arbitrarily long quantum computations are possible
  - Course comes full circle: from qubits (Ch1) to protecting qubits (Ch6)

**Narrative notes:**
Ch6 returns to foundations with new maturity. The density matrix handles ignorance (6.1), maximum entropy derives thermal physics, and Bose-Einstein/Fermi-Dirac distributions emerge from a single-mode calculation. Entanglement (6.2) — the most quantum phenomenon — is quantified, witnessed, and tested by Bell's inequality. Generalized measurements and quantum channels (6.3) provide the complete framework. The final unit (6.4) confronts reality: decoherence is measurement-then-forgetting, the Lindblad equation governs open dynamics, and error correction shows quantum information can be protected — connecting back to the toric code of Ch2 and closing the circle.