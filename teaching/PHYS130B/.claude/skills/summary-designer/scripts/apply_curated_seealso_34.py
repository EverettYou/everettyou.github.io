#!/usr/bin/env python3
"""Replace See Also bullets in the 34 notebooks that were TOC-auto-filled.

Content-informed links + glosses (plain `- [Title](path): gloss` format).
Run from `teaching/PHYS130B/`. Edit the `CURATED` map in this file, then run this script (see `skills/summary-designer/SKILL.md`).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def _repo_root() -> Path:
    for d in Path(__file__).resolve().parents:
        if (d / "notes_src").is_dir():
            return d
    raise RuntimeError("Could not locate repo root (notes_src/)")


ROOT = _repo_root()
SEE_ALSO_START = re.compile(r"(?m)^:::\{admonition\}\s+See Also\s*$")

# Multiline: only the list lines (no admonition fences).
CURATED: dict[str, str] = {
    "notes_src/ch1_qubit/1-1-2-state-and-representation.ipynb": """- [1.1.1 What is a Qubit](1-1-1-what-is-a-qubit): Two-level Hilbert space, Bloch-sphere picture, and what “state” means before bases and inner products.
- [1.1.3 Hermitian Operators](1-1-3-hermitian-operators): Observables, Pauli operators, and expectation values that use the representations developed here.
- [1.2.1 Measurement Postulate](1-2-1-measurement-postulate): Born probabilities and collapse—where the state–representation machinery meets experiment.""",
    "notes_src/ch1_qubit/1-1-3-hermitian-operators.ipynb": """- [1.1.2 State and Representation](1-1-2-state-and-representation): Bras, kets, inner products, and Bloch geometry used to interpret expectation values.
- [1.2.1 Measurement Postulate](1-2-1-measurement-postulate): Eigenvalues as outcomes and projectors built from the spectral theory of observables.
- [1.2.2 Uncertainty and Incompatibility](1-2-2-uncertainty-and-incompatibility): Commutators, simultaneous eigenstates, and the Robertson inequality for non-commuting observables.""",
    "notes_src/ch1_qubit/1-3-1-unitary-evolution.ipynb": """- [1.1.3 Hermitian Operators](1-1-3-hermitian-operators): Hermitian generators (especially $\\hat{H}$) whose spectral calculus defines $\\mathrm{e}^{-\\mathrm{i}\\hat{H}t/\\hbar}$.
- [1.3.2 Schrödinger Picture](1-3-2-schrodinger-picture): From $\\hat{U}(t)$ to the Schrödinger equation and the state’s differential equation of motion.
- [1.3.3 Heisenberg Picture](1-3-3-heisenberg-picture): Equivalent operator dynamics, commutator equations of motion, and conservation laws.""",
    "notes_src/ch1_qubit/1-3-3-heisenberg-picture.ipynb": """- [1.3.1 Unitary Evolution](1-3-1-unitary-evolution): Time-evolution operators, unitarity, and the Hamiltonian as generator.
- [1.3.2 Schrödinger Picture](1-3-2-schrodinger-picture): States evolve, operators fixed—contrasts directly with the Heisenberg picture used here.
- [1.1.3 Hermitian Operators](1-1-3-hermitian-operators): Operator algebra, commutators, and spectra underlying $\\mathrm{d}\\hat{O}/\\mathrm{d}t$ equations.""",
    "notes_src/ch2_identical-particles/2-1-1-tensor-product.ipynb": """- [1.1.2 State and Representation](../ch1_qubit/1-1-2-state-and-representation): Single-particle Hilbert spaces and tensor structure before imposing exchange symmetry.
- [2.1.2 Symmetrization](2-1-2-symmetrization): Symmetric/antisymmetric subspaces, (anti)symmetrization projectors, and many-body state construction.
- [2.1.3 Second Quantization](2-1-3-second-quantization): Occupation-number bases and ladder operators built on tensor-product many-body Hilbert space.""",
    "notes_src/ch2_identical-particles/2-1-3-second-quantization.ipynb": """- [2.1.2 Symmetrization](2-1-2-symmetrization): Permutation-symmetric many-body wavefunctions and the origin of commutation vs anticommutation rules.
- [2.3.1 Exchange Statistics](2-3-1-exchange-statistics): Bosons, fermions, and the physical consequences of indistinguishability in 3D.
- [2.1.1 Tensor Product](2-1-1-tensor-product): Multi-particle Hilbert space as a tensor product before second-quantized bookkeeping.""",
    "notes_src/ch2_identical-particles/2-2-1-angular-momentum-algebra.ipynb": """- [1.1.3 Hermitian Operators](../ch1_qubit/1-1-3-hermitian-operators): Self-adjoint observables and spectral notions reused for $\\hat{J}^2,\\hat{J}_z$.
- [2.2.2 Spin Representations](2-2-2-spin-representations): From $su(2)$ commutation relations to spin-$j$ representations and ladder operators.
- [2.2.3 Addition of Angular Momenta](2-2-3-addition-of-angular-momenta): Tensoring representations, Clebsch–Gordan series, and coupled bases.""",
    "notes_src/ch2_identical-particles/2-2-2-spin-representations.ipynb": """- [2.2.1 Angular Momentum Algebra](2-2-1-angular-momentum-algebra): $[J_i,J_j]=\\mathrm{i}\\hbar\\epsilon_{ijk}J_k$, ladders, and multiplets—the algebra this section represents explicitly as matrices.
- [2.2.3 Addition of Angular Momenta](2-2-3-addition-of-angular-momenta): Tensor products of $SU(2)$ irreps and coupled bases after fixing spin-$j$ matrices here.
- [1.1.3 Hermitian Operators](../ch1_qubit/1-1-3-hermitian-operators): Pauli matrices as $2\\times 2$ observables—the same operators promoted here to the spin-$\\tfrac{1}{2}$ representation.""",
    "notes_src/ch2_identical-particles/2-2-3-addition-of-angular-momenta.ipynb": """- [2.2.2 Spin Representations](2-2-2-spin-representations): Irreps and tensor-product Hilbert spaces whose coupled bases are built with Clebsch–Gordan coefficients here.
- [2.2.1 Angular Momentum Algebra](2-2-1-angular-momentum-algebra): Ladder operators, $J_\\pm$, and the triangle rule that decide which total $J$ appear in $j_1\\otimes j_2$.
- [2.1.2 Symmetrization](2-1-2-symmetrization): Identical particles in product spaces—singlet vs triplet constraints when two fermions share an orbital (as in the homework coupling problems).""",
    "notes_src/ch2_identical-particles/2-3-1-exchange-statistics.ipynb": """- [2.1.2 Symmetrization](2-1-2-symmetrization): (Anti)symmetry of many-body wavefunctions under particle exchange.
- [2.3.2 Fractional Quantum Hall Anyons](2-3-2-fractional-quantum-hall-anyons): Beyond bosons/fermions—braiding and fractional statistics in 2D.
- [2.1.1 Tensor Product](2-1-1-tensor-product): Configuration-space Hilbert space before restricting to symmetry sectors.""",
    "notes_src/ch2_identical-particles/2-3-2-fractional-quantum-hall-anyons.ipynb": """- [2.3.1 Exchange Statistics](2-3-1-exchange-statistics): Charge-flux composites and braid statistics—the setup this lesson uses for FQH anyon phases.
- [4.2.2 Aharonov-Bohm Effect](../ch4_phase-and-gauge/4-2-2-aharonov-bohm-effect): Phase from charge encircling flux—the mechanism behind the charge-flux statistics calculation in the Overview and Summary.
- [2.3.3 Toric Code](2-3-3-toric-code): Another setting where anyons arise as quasiparticles—concrete lattice model complementing continuum FQH intuition.""",
    "notes_src/ch2_identical-particles/2-3-3-toric-code.ipynb": """- [2.3.2 Fractional Quantum Hall Anyons](2-3-2-fractional-quantum-hall-anyons): Anyonic fusion and braiding intuition from 2D topological phases.
- [6.4.3 Error Correction](../ch6_quantum-foundations/6-4-3-error-correction): Stabilizer formalism and fault tolerance—Toric code as a canonical example.
- [2.3.1 Exchange Statistics](2-3-1-exchange-statistics): Indistinguishability, superselection, and the road from permutations to braids.""",
    "notes_src/ch3_path-integral/3-1-2-physical-optics.ipynb": """- [3.1.1 Geometric Optics](3-1-1-geometric-optics): Fermat’s principle and the short-wavelength limit that wave optics must reproduce.
- [3.1.3 Wave-Particle Duality](3-1-3-wave-particle-duality): Action–phase correspondence and the conceptual bridge to quantum amplitudes.
- [3.2.1 Path Integral Formulation](3-2-1-path-integral-formulation): Sums over paths—making the optics-to-quantum analogy quantitative.""",
    "notes_src/ch3_path-integral/3-2-1-path-integral-formulation.ipynb": """- [3.1.3 Wave-Particle Duality](3-1-3-wave-particle-duality): $S/\\hbar$ as phase—motivation for summing $\\mathrm{e}^{\\mathrm{i}S/\\hbar}$ over trajectories.
- [3.2.2 Schrödinger Equation](3-2-2-schrodinger-equation): Recovering time evolution from the path-integral composition law and short-time kernels.
- [3.2 Propagator](3-2-propagator): Section overview—propagator composition, slicing, and the continuum limit.""",
    "notes_src/ch3_path-integral/3-2-2-schrodinger-equation.ipynb": """- [3.2.1 Path Integral Formulation](3-2-1-path-integral-formulation): Path integral definition and infinitesimal time step that yields the Schrödinger equation.
- [3.2.3 Free Particle Propagator](3-2-3-free-particle-propagator): Exact Gaussian kernel—concrete solution illustrating propagator methods.
- [1.3.1 Unitary Evolution](../ch1_qubit/1-3-1-unitary-evolution): Unitary generated by $\\hat{H}$—same physics as path-integral composition with Hermitian Hamiltonians.""",
    "notes_src/ch3_path-integral/3-2-3-free-particle-propagator.ipynb": """- [3.2.2 Schrödinger Equation](3-2-2-schrodinger-equation): Green’s function / kernel viewpoint tied to propagation in time.
- [3.3.1 Stationary Phase Approximation](3-3-1-stationary-phase-approximation): Semiclassical evaluation of oscillatory path integrals beyond the free particle.
- [3.2.1 Path Integral Formulation](3-2-1-path-integral-formulation): Composition, normalization, and the continuum limit that fixes propagator factors.""",
    "notes_src/ch3_path-integral/3-3-1-stationary-phase-approximation.ipynb": """- [3.2.3 Free Particle Propagator](3-2-3-free-particle-propagator): Exact propagator as a benchmark before asymptotic methods.
- [3.3.2 WKB Approximation](3-3-2-wkb-approximation): Connection formulas and turning points—semiclassical quantization in one dimension.
- [3.1.3 Wave-Particle Duality](3-1-3-wave-particle-duality): Stationary-phase intuition linking classical trajectories to dominant quantum paths.""",
    "notes_src/ch3_path-integral/3-3-2-wkb-approximation.ipynb": """- [3.3.1 Stationary Phase Approximation](3-3-1-stationary-phase-approximation): Asymptotics of rapidly oscillating integrals and classical limits.
- [3.3.3 Bohr-Sommerfeld Quantization](3-3-3-bohr-sommerfeld-quantization): Quantization rules from WKB matching and periodic-orbit conditions.
- [3.2.3 Free Particle Propagator](3-2-3-free-particle-propagator): Exact quadratic path integral—concrete oscillatory integral before turning-point analysis.""",
    "notes_src/ch3_path-integral/3-3-3-bohr-sommerfeld-quantization.ipynb": """- [3.3.2 WKB Approximation](3-3-2-wkb-approximation): Turning points, connection formulas, and quantization integrals that lead to the Bohr–Sommerfeld rule used here.
- [3.2.1 Path Integral Formulation](3-2-1-path-integral-formulation): Semiclassical constructive interference on periodic orbits—the path-integral reading stated in this lesson’s Summary.
- [3.2.3 Free Particle Propagator](3-2-3-free-particle-propagator): Exact quadratic path integral as a worked oscillatory integral before turning-point matching.""",
    "notes_src/ch3_path-integral/3-4-1-wick-rotation.ipynb": """- [3.3.3 Bohr-Sommerfeld Quantization](3-3-3-bohr-sommerfeld-quantization): Semiclassical tunneling exponents—compare with Euclidean instanton actions.
- [3.4.2 Black Hole Temperature](3-4-2-black-hole-temperature): Periodic imaginary time and thermal interpretation of Wick-rotated geometries.
- [3.4.3 Instantons](3-4-3-instantons): Non-perturbative saddles of the Euclidean action—finite-temperature and tunneling physics.""",
    "notes_src/ch3_path-integral/3-4-2-black-hole-temperature.ipynb": """- [3.4.1 Wick Rotation](3-4-1-wick-rotation): Imaginary time, periodic kernels, and $\\beta = \\hbar\\Delta\\tau$—used explicitly here right after §3.4.1.
- [3.4.3 Instantons](3-4-3-instantons): Other Euclidean semiclassics in the same chapter; tunneling saddles complement the horizon-smoothness argument, not the WKB line of §3.3.""",
    "notes_src/ch4_phase-and-gauge/4-3-2-landau-quantization.ipynb": """- [4.3.1 Cyclotron Motion](4-3-1-cyclotron-motion): Symmetric gauge, Landau levels as harmonic oscillators, and guiding-center versus cyclotron degrees of freedom.
- [4.3.3 Quantum Hall Effect](4-3-3-quantum-hall-effect): Filled Landau levels, edge states, and quantized Hall conductance.
- [4.1.3 Gauge Invariance](4-1-3-gauge-invariance): Gauge choices for $\\boldsymbol{A}$ and physical content of Landau versus symmetric gauges.""",
    "notes_src/ch4_phase-and-gauge/4-3-3-quantum-hall-effect.ipynb": """- [4.3.2 Landau Quantization](4-3-2-landau-quantization): Landau levels, degeneracy $N_\\Phi$, and the quantum spectrum in uniform $B$.
- [4.2.2 Aharonov-Bohm Effect](4-2-2-aharonov-bohm-effect): Gauge potentials, flux threading, and interference—edge transport and topology motifs.
- [4.3.1 Cyclotron Motion](4-3-1-cyclotron-motion): Classical cyclotron frequency and kinetic momentum algebra underlying the quantum plateau problem.""",
    "notes_src/ch4_phase-and-gauge/4-4-1-classical-spin.ipynb": """- [2.2.2 Spin Representations](../ch2_identical-particles/2-2-2-spin-representations): Lie algebra of angular momentum and spin-$\\tfrac{1}{2}$ as the quantum upgrade of classical $\\boldsymbol{S}$.
- [4.4.2 Dirac Monopole](4-4-2-dirac-monopole): Dirac string, vector potentials on patches, and the geometric phase preview for monopole harmonics.
- [4.2.1 Berry Phase](4-2-1-berry-phase): Geometric phases when parameters (or $\\boldsymbol{n}$) adiabatically traverse a closed path.""",
    "notes_src/ch5_perturbation-theory/5-2-1-interaction-picture.ipynb": """- [5.1.2 Non-Degenerate Perturbation Theory](5-1-2-non-degenerate-perturbation-theory): Spectral perturbation of time-independent Hamiltonians—contrasts with time-dependent $\\hat{V}(t)$ here.
- [5.2.2 Fermi's Golden Rule](5-2-2-fermis-golden-rule): Transition rates from the interaction picture and Dyson expansion to long-time behavior.
- [1.3.2 Schrödinger Picture](../ch1_qubit/1-3-2-schrodinger-picture): State evolution in the Schrödinger picture versus operator evolution in the interaction picture.""",
    "notes_src/ch5_perturbation-theory/5-2-3-applications.ipynb": """- [5.2.2 Fermi's Golden Rule](5-2-2-fermis-golden-rule): Rates, linewidth, and resonance—the formulas applied here to spectroscopy and response.
- [5.2.1 Interaction Picture](5-2-1-interaction-picture): Time-ordered evolution and amplitudes $c_f^{(1)}(t)$ that underlie harmonic driving and Kubo response in this lesson.
- [4.3.3 Quantum Hall Effect](../ch4_phase-and-gauge/4-3-3-quantum-hall-effect): The Kubo–Landau-level calculation of $\\sigma_{xy}=\\nu e^2/h$ cited from this lesson’s prompts and Overview.""",
    "notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb": """- [1.2.3 Measurement Operators](../ch1_qubit/1-2-3-measurement-operators): Projective maps on pure states—density matrices package the same data when mixing is present.
- [6.1.2 Entropy](6-1-2-entropy): Von Neumann entropy and uncertainty measures for mixed states.
- [6.2.1 Product States and Entanglement](6-2-1-product-and-entangled-states): Reduced states from partial traces—mixedness as entanglement with an environment.""",
    "notes_src/ch6_quantum-foundations/6-1-2-entropy.ipynb": """- [6.1.1 Mixed States](6-1-1-mixed-states): Density matrices, convex combinations, and the state space on which entropy is defined.
- [6.1.3 Quantum Statistics](6-1-3-quantum-statistics): Thermal states from entropy maximization—entropy as a variational principle.
- [6.2.2 Entanglement Entropy](6-2-2-entanglement-entropy): Entropy of subsystems—distinct but related use of partial trace and $\\mathrm{Tr}\\,\\rho\\ln\\rho$.""",
    "notes_src/ch6_quantum-foundations/6-3-1-projective-measurement.ipynb": """- [1.2.1 Measurement Postulate](../ch1_qubit/1-2-1-measurement-postulate): Born rule and collapse—finite-dimensional projective measurement as the axiom revisited.
- [6.1.1 Mixed States](6-1-1-mixed-states): Post-measurement mixed ensembles and classical ignorance versus quantum coherence.
- [6.3.2 POVM](6-3-2-povm): Generalized measurements beyond orthogonal projectors—Naimark dilation viewpoint.""",
    "notes_src/ch6_quantum-foundations/6-3-2-povm.ipynb": """- [6.3.1 Projective Measurement](6-3-1-projective-measurement): Projection-valued measures as the special case of POVMs.
- [6.3.3 Quantum Channels](6-3-3-quantum-channels): CPTP maps and instruments that realize POVM outcomes with auxiliary systems.
- [1.2.3 Measurement Operators](../ch1_qubit/1-2-3-measurement-operators): Effects, Kraus rank-one updates, and generalized outcomes.""",
    "notes_src/ch6_quantum-foundations/6-3-3-quantum-channels.ipynb": """- [6.3.2 POVM](6-3-2-povm): Measurement operators and classical post-processing—Kraus and instrument viewpoints adjacent to general CPTP maps.
- [6.4.1 Decoherence](6-4-1-decoherence): Noise as CPTP dynamics on states—the physical setting channels abstract here are meant to model.
- [6.1.1 Mixed States](6-1-1-mixed-states): Output states are generally mixed when system and ancilla are entangled or traced out—density-matrix language used throughout this lesson.""",
    "notes_src/ch6_quantum-foundations/6-4-1-decoherence.ipynb": """- [6.3.3 Quantum Channels](6-3-3-quantum-channels): Completely positive trace-preserving maps—mathematical frame for noise and decoherence.
- [6.4.2 Lindblad Master Equation](6-4-2-lindblad-master-equation): Markovian open-system generators, Lindblad operators, and positivity.
- [6.1.1 Mixed States](6-1-1-mixed-states): Mixed reduced states from tracing out an environment—purity loss as decoherence signature.""",
    "notes_src/ch6_quantum-foundations/6-4-2-lindblad-master-equation.ipynb": """- [6.4.1 Decoherence](6-4-1-decoherence): Environment-induced superselection and timescales before Markovian master equations.
- [6.4.3 Error Correction](6-4-3-error-correction): Fighting channel noise—dynamical decoupling and quantum error correction as open-system control.
- [6.3.3 Quantum Channels](6-3-3-quantum-channels): CPTP structure and complete positivity constraints on Lindblad forms.""",
    "notes_src/ch6_quantum-foundations/6-4-3-error-correction.ipynb": """- [6.4.2 Lindblad Master Equation](6-4-2-lindblad-master-equation): Noise models and error rates that codes are designed to suppress.
- [2.3.3 Toric Code](../ch2_identical-particles/2-3-3-toric-code): Stabilizer group, anyonic excitations, and a concrete topological code template.
- [6.3.1 Projective Measurement](6-3-1-projective-measurement): Syndrome measurements as (near-)projective readout of error subspaces.""",
}


def text_to_source(text: str) -> list[str]:
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            out.append(line + "\n")
        else:
            if line:
                out.append(line)
    return out


def lecture_cell_index(nb: dict) -> int | None:
    for i, c in enumerate(nb.get("cells", [])):
        if c.get("cell_type") != "markdown":
            continue
        src = c.get("source", [])
        if not isinstance(src, list):
            continue
        t = "".join(src)
        if "## Lecture Notes" in t and "### Summary" in t:
            return i
    return None


def replace_seealso_bullets(md: str, bullet_body: str) -> str | None:
    m = SEE_ALSO_START.search(md)
    if not m:
        return None
    start = m.start()
    chunk = md[start:]
    lines = chunk.split("\n")
    end_off = None
    for j in range(1, len(lines)):
        if lines[j].strip() == ":::":
            end_off = start + len("\n".join(lines[: j + 1]))
            if end_off < len(md) and md[end_off] == "\n":
                end_off += 1
            break
    if end_off is None:
        return None
    new_block = (
        "\n\n:::{admonition} See Also\n:class: seealso\n\n"
        + bullet_body.strip()
        + "\n:::\n"
    )
    return md[:start] + new_block + md[end_off:]


def main() -> int:
    n = 0
    for rel, body in sorted(CURATED.items()):
        p = ROOT / rel
        if not p.exists():
            print("missing", rel, file=sys.stderr)
            continue
        nb = json.loads(p.read_text(encoding="utf-8"))
        li = lecture_cell_index(nb)
        if li is None:
            print("no lecture", rel, file=sys.stderr)
            continue
        cell = nb["cells"][li]
        md = "".join(cell["source"])
        new_md = replace_seealso_bullets(md, body)
        if new_md is None:
            print("no See Also block", rel, file=sys.stderr)
            continue
        if new_md == md:
            print("unchanged", rel)
            continue
        cell["source"] = text_to_source(new_md)
        p.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
        print("updated", rel)
        n += 1
    print("total", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
