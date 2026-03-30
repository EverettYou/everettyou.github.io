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
- 1.2.2 Uncertainty and Incompatibility
- 1.2.3 Measurement Operators

### 1.3 Time Evolution

- 1.3.1 Unitary Evolution
- 1.3.2 Spin Dynamics
- 1.3.3 Heisenberg Picture

**Narrative notes:**
<!-- What story does this chapter tell? What question does it open for Ch2? -->

---

## Ch2. Identical Particles — From One to Many

<!-- Extend the single-qubit framework to many-body systems. What new physics emerges? -->

### 2.1 Bosons and Fermions

- 2.1.1 Tensor Product
- 2.1.2 Symmetrization
- 2.1.3 Second Quantization

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
