# PHYS 130B — Storyline Outline

## Central Narrative

<!-- Write your storyline vision here. The narrative arc: -->
<!-- Axioms (qubit) → Many-body (bosons, fermions, anyons) → Classical connection (path integral) → Gauge & phase → Perturbation theory → Open systems & quantum information -->

---

## Ch1. Qubit — Axioms of Quantum Mechanics

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
<!-- What story does this chapter tell? What question does it open for Ch2? -->

---

## Ch2. Identical Particles — From One to Many

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
- 2.2.2 Spin Representations
- 2.2.3 Addition of Angular Momenta

### 2.3 Anyons

- 2.3.1 Exchange Statistics
- 2.3.2 Fractional Quantum Hall Anyons
- 2.3.3 Toric Code

**Narrative notes:**
<!-- What story does this chapter tell? What question does it open for Ch3? -->

---

## Ch3. Path Integral — Connecting Quantum and Classical

<!-- Come back to foundations: how does classical mechanics emerge? The path integral bridges quantum and classical. -->

### 3.1 Quantization

- 3.1.1 Classical to Quantum
- 3.1.2 Physical Optics
- 3.1.3 Quantum Mechanics as Optics

### 3.2 Propagator

- 3.2.1 Path Integral Formulation
- 3.2.2 Free Particle Propagator
- 3.2.3 Schrödinger Equation

### 3.3 Stationary Phase

- 3.3.1 Stationary Phase Approximation
- 3.3.2 WKB Approximation
- 3.3.3 Bohr-Sommerfeld Quantization

### 3.4 Imaginary Time

- 3.4.1 Wick Rotation
- 3.4.2 Statistical Mechanics
- 3.4.3 Instantons

**Narrative notes:**
<!-- What story does this chapter tell? What question does it open for Ch4? -->

---

## Ch4. Phase and Gauge — Particle Motion in Fields

<!-- Build on the path integral: what happens when a charged particle moves in a gauge field? Phase becomes geometric. -->

### 4.1 Gauge Field

- 4.1.1 Gauge Transformations
- 4.1.2 Gauge Connection
- 4.1.3 Electromagnetic Coupling

### 4.2 Flux Ring

- 4.2.1 Aharonov-Bohm Effect
- 4.2.2 Flux Quantization
- 4.2.3 Gauge Invariance

### 4.3 Landau Level

- 4.3.1 Cyclotron Motion
- 4.3.2 Landau Quantization
- 4.3.3 Quantum Hall Effect

### 4.4 Spin and Monopole

- 4.4.1 Orbital vs Spin
- 4.4.2 Dirac Monopole
- 4.4.3 Monopole Harmonics

### 4.5 Berry Phase

- 4.5.1 Berry Phase
- 4.5.2 Applications
- 4.5.3 Topology

**Narrative notes:**
<!-- What story does this chapter tell? What question does it open for Ch5? -->

---

## Ch5. Perturbation Theory — When Exact Solutions Fail

<!-- Not everything is exactly solvable. Systematic approximations for ground states and dynamics. -->

### 5.1 Time-Independent Perturbation Theory

- 5.1.1 Toy Model
- 5.1.2 Non-Degenerate Perturbation Theory
- 5.1.3 Degenerate Perturbation Theory

### 5.2 Time-Dependent Perturbation Theory

- 5.2.1 Interaction Picture
- 5.2.2 Fermi's Golden Rule
- 5.2.3 Applications

**Narrative notes:**
<!-- What story does this chapter tell? What question does it open for Ch6? -->

---

## Ch6. Quantum Foundations — Open Systems and Information

<!-- The quantum system is not isolated. Decoherence, measurement, entanglement, and the limits of quantum mechanics. -->

### 6.1 Density Matrix

- 6.1.1 Mixed States
- 6.1.2 Partial Trace
- 6.1.3 Entropy

### 6.2 Entanglement

- 6.2.1 Composite Systems
- 6.2.2 Entanglement Measures
- 6.2.3 Bell Inequality

### 6.3 Generalized Measurement

- 6.3.1 Projective Measurement
- 6.3.2 POVM
- 6.3.3 Quantum Channels

### 6.4 Open Quantum Systems

- 6.4.1 Decoherence
- 6.4.2 Lindblad Master Equation
- 6.4.3 Error Correction

**Narrative notes:**
<!-- What story does this chapter tell? How does the course come full circle? -->
