#!/usr/bin/env python3
"""
Unify all 21 section parent notebooks to consistent structure:
  Cell 0: # x.y Title
  Cell 1: ### Topics, ### Overview, ### Key Concepts, ### Learning Objectives
  Cell 2: (empty)

Rules:
- Remove Prompts admonitions (only at x.x.x level)
- Remove empty Brief Introductions
- Merge non-empty Brief Introduction content into Overview
- Consolidate multi-cell content into single cell
- Ensure consistent section ordering
"""
import json, glob, os, re

BASE = "/sessions/tender-admiring-allen/mnt/teaching/PHYS130B/notes_src"

def get_section_parents():
    parents = []
    for ch_dir in sorted(glob.glob(f"{BASE}/ch*")):
        for f in sorted(glob.glob(f"{ch_dir}/[0-9]-[0-9]-*.ipynb")):
            parts = os.path.basename(f).split('-')
            if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and not parts[2].isdigit():
                parents.append(f)
    return parents

def extract_section(text, heading_pattern, next_heading_level='##'):
    """Extract content under a heading, up to the next heading of same or higher level."""
    # Find the heading
    m = re.search(heading_pattern, text, re.MULTILINE)
    if not m:
        return None, text

    start = m.start()
    heading_end = m.end()

    # Find next heading at same or higher level
    rest = text[heading_end:]
    next_m = re.search(r'^#{2,3}\s', rest, re.MULTILINE)
    if next_m:
        end = heading_end + next_m.start()
    else:
        end = len(text)

    content = text[heading_end:end].strip()
    # Remove this section from text
    remaining = text[:start] + text[end:]
    return content, remaining

def extract_topics_table(text):
    """Extract the Topics list-table block."""
    m = re.search(r'(### Topics\s*\n\s*```\{list-table\}.*?```)', text, re.DOTALL)
    if m:
        return m.group(1), text[:m.start()] + text[m.end():]
    # Also try without code fence
    m = re.search(r'(### Topics\s*\n.*?)(?=\n###\s|\Z)', text, re.DOTALL)
    if m:
        return m.group(1).strip(), text[:m.start()] + text[m.end():]
    return None, text

def collect_all_content(nb):
    """Collect all markdown content from all cells, excluding title and prompts."""
    parts = []
    for ci, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'markdown':
            continue
        src = ''.join(cell['source']).strip()
        if not src:
            continue
        # Skip title cell (first cell with # x.y)
        if ci == 0 and re.match(r'^# \d+\.\d+\s', src):
            continue
        # Skip prompts cells
        if ':::{admonition} Prompts' in src or ':::{admonition} Prompt' in src:
            continue
        parts.append(src)
    return '\n\n'.join(parts)

def extract_overview_content(text):
    """Extract overview/introduction content from various heading styles."""
    content_parts = []

    # Try various heading names for overview-like content
    for pattern in [
        r'^### Overview\s*$',
        r'^## Overview\s*$',
        r'^## Overview and Navigation\s*$',
        r'^### Why.*Matters?\s*$',
        r'^### Why This Matters\s*$',
        r'^## Why.*Matters?\s*$',
        r'^### Physical Significance\s*$',
    ]:
        m = re.search(pattern, text, re.MULTILINE)
        if m:
            # Get content under this heading
            start = m.end()
            rest = text[start:]
            next_h = re.search(r'^#{2,3}\s', rest, re.MULTILINE)
            if next_h:
                content = rest[:next_h.start()].strip()
            else:
                content = rest.strip()
            if content and len(content) > 10:
                content_parts.append(content)

    # Try Brief Introduction content
    for pattern in [
        r'^## Brief Introduction\s*$',
        r'^### Brief Introduction\s*$',
    ]:
        m = re.search(pattern, text, re.MULTILINE)
        if m:
            start = m.end()
            rest = text[start:]
            next_h = re.search(r'^#{1,2}\s', rest, re.MULTILINE)
            if next_h:
                content = rest[:next_h.start()].strip()
            else:
                content = rest.strip()
            # Clean up sub-headings within Brief Intro
            content = re.sub(r'^###\s+.*$', '', content, flags=re.MULTILINE)
            content = content.strip()
            if content and len(content) > 10:
                content_parts.append(content)

    return '\n\n'.join(content_parts) if content_parts else None

def extract_key_concepts(text):
    """Extract Key Concepts content."""
    for pattern in [
        r'^### Key Concepts Summary?\s*$',
        r'^### Key Concepts\s*$',
        r'^## Key Concepts\s*$',
    ]:
        m = re.search(pattern, text, re.MULTILINE)
        if m:
            start = m.end()
            rest = text[start:]
            next_h = re.search(r'^#{2,3}\s', rest, re.MULTILINE)
            if next_h:
                content = rest[:next_h.start()].strip()
            else:
                content = rest.strip()
            if content and len(content) > 10:
                return content
    return None

def extract_learning_objectives(text):
    """Extract Learning Objectives content."""
    m = re.search(r'^### Learning Objectives?\s*$', text, re.MULTILINE)
    if m:
        start = m.end()
        rest = text[start:]
        next_h = re.search(r'^#{2,3}\s', rest, re.MULTILINE)
        if next_h:
            content = rest[:next_h.start()].strip()
        else:
            content = rest.strip()
        if content and len(content) > 10:
            return content
    return None

def extract_glossary(text):
    """Extract Glossary content."""
    m = re.search(r'^(#{2,3}\s+Glossary.*$)', text, re.MULTILINE)
    if m:
        start = m.start()
        rest = text[start:]
        # Glossary goes to end typically
        return rest.strip()
    return None

# Section-specific overview content for notebooks that lack it
OVERVIEW_DEFAULTS = {
    "1-1": "The quantum world begins with the simplest possible system: a single two-state particle. In this section, we develop the mathematical language of quantum states, observables, and the Bloch sphere representation that makes the abstract concrete. These ideas form the foundation for everything that follows in quantum mechanics.",
    "2-1": "When we bring identical quantum particles together, something remarkable happens: the symmetry of nature forces us to treat them as genuinely indistinguishable. This constraint leads to the division of all particles into bosons and fermions, with profound consequences for the structure of matter—from the stability of atoms to the behavior of superconductors and neutron stars.",
    "2-2": "Angular momentum in quantum mechanics is far richer than its classical counterpart. Spin emerges as a purely quantum degree of freedom with no classical analog, and the algebra of angular momentum—governed by commutation relations—determines everything from atomic spectra to particle physics selection rules.",
    "2-3": "In two spatial dimensions, the topology of particle exchanges admits possibilities beyond bosons and fermions. Anyons—particles with fractional exchange statistics—are not merely theoretical curiosities: they appear in the fractional quantum Hall effect and are candidates for building fault-tolerant quantum computers through topological braiding.",
    "3-1": "The path integral formulation offers a radically different perspective on quantum mechanics. Rather than solving differential equations, we sum over all possible histories of a system, weighted by a phase proportional to the classical action. This approach reveals deep connections between quantum mechanics, classical mechanics, and optics.",
    "3-2": "The propagator encodes the complete dynamics of a quantum system: given the state at one time, it determines the state at any later time. Computing propagators via the path integral leads to exact results for free particles and harmonic oscillators, and provides a systematic framework for perturbative calculations in more complex systems.",
    "3-3": "When quantum systems approach the classical limit, the path integral is dominated by paths near the classical trajectory. The stationary phase approximation makes this precise, connecting quantum amplitudes to classical action, and leading to powerful semiclassical methods including the WKB approximation and Bohr-Sommerfeld quantization.",
    "3-4": "Replacing real time with imaginary time transforms quantum mechanics into statistical mechanics. This Wick rotation connects the quantum propagator to the thermal partition function, enabling powerful computational techniques—from lattice simulations of quantum field theory to quantum Monte Carlo methods for many-body physics.",
    "4-1": "The phase of a quantum wavefunction is not directly observable, yet it contains essential physics. Gauge invariance—the freedom to redefine this phase locally—leads to the introduction of gauge fields, which describe how charged particles couple to electromagnetic potentials. This is the starting point for understanding all fundamental interactions in nature.",
    "4-2": "A charged particle circling a magnetic flux tube acquires a quantum phase even in regions where the magnetic field vanishes. The Aharonov-Bohm effect demonstrates that electromagnetic potentials, not just fields, have direct physical consequences in quantum mechanics—a profound departure from classical electromagnetism.",
    "4-3": "A charged particle in a uniform magnetic field has a spectrum of discrete, highly degenerate energy levels—the Landau levels. This quantization underlies the quantum Hall effect, one of the most precisely measured phenomena in physics, and connects to deep ideas in topology and condensed matter.",
    "4-4": "The Dirac monopole—a hypothetical magnetic point charge—leads to a beautiful interplay between topology, gauge theory, and angular momentum quantization. The monopole's vector potential cannot be defined globally, requiring gauge patches that encode topological information about the field configuration.",
    "4-5": "When a quantum system is slowly transported around a closed loop in parameter space, it acquires a geometric phase—the Berry phase—that depends only on the path taken, not on the speed of traversal. This phase has observable consequences across physics, from molecular spectra to the quantum Hall effect and topological insulators.",
    "5-1": "Most quantum systems cannot be solved exactly. Perturbation theory provides a systematic way to approximate eigenvalues and eigenstates by treating the difference from a solvable system as a small correction. This is arguably the most widely used tool in all of theoretical physics.",
    "5-2": "When a quantum system is driven by a time-varying external field, transitions between energy levels occur. Time-dependent perturbation theory provides the framework for computing transition rates, leading to Fermi's golden rule—the workhorse formula for decay rates, absorption spectra, and scattering cross sections across all of physics.",
    "6-1": "Entanglement is the defining feature of quantum mechanics that has no classical counterpart. When two quantum systems become entangled, the state of the whole cannot be decomposed into independent states of the parts. This leads to correlations that violate classical bounds, as demonstrated by Bell's theorem, and forms the basis of quantum information science.",
    "6-2": "Pure quantum states describe systems about which we have maximal knowledge. But in practice—due to thermal noise, decoherence, or entanglement with an environment—we often face incomplete information. The density matrix provides a unified description of both pure and mixed states, and is essential for understanding open quantum systems.",
    "6-3": "The textbook projective measurement is only one type of quantum measurement. The generalized measurement framework—POVMs and quantum instruments—describes the full range of physically realizable measurements, including weak measurements, approximate measurements, and measurements that extract partial information while minimizing disturbance.",
    "6-4": "No quantum system is truly isolated. Interaction with an environment causes decoherence—the loss of quantum coherence that makes the quantum-to-classical transition. The theory of open quantum systems, formalized through quantum channels and the Lindblad master equation, describes how quantum information leaks into the environment.",
}

KEY_CONCEPTS_DEFAULTS = {
    "2-1": "- **Tensor product**: Composite Hilbert space $\\mathcal{H}_A \\otimes \\mathcal{H}_B$ for multi-particle systems.\n- **Indistinguishability**: Identical particles have no individual identity; states must be symmetrized or antisymmetrized.\n- **Bosons and fermions**: Symmetric (bosons) vs. antisymmetric (fermions) under particle exchange.\n- **Pauli exclusion**: No two identical fermions can occupy the same quantum state.\n- **Second quantization**: Creation and annihilation operators that automatically enforce exchange symmetry.",
    "2-2": "- **Angular momentum algebra**: $[J_i, J_j] = i\\hbar \\epsilon_{ijk} J_k$ governs all angular momentum in quantum mechanics.\n- **Spin-1/2 representation**: Pauli matrices $\\sigma_x, \\sigma_y, \\sigma_z$ as generators for the simplest nontrivial representation.\n- **Addition of angular momentum**: Combining two spins via Clebsch-Gordan coefficients; singlet and triplet states.\n- **Spin-orbit coupling**: Interaction between orbital and spin angular momentum, producing fine structure.",
    "2-3": "- **Configuration space topology**: In 2D, the fundamental group of the configuration space is the braid group, not the permutation group.\n- **Abelian anyons**: Particles that acquire a phase $e^{i\\theta}$ with $0 < \\theta < \\pi$ under exchange.\n- **Non-Abelian anyons**: Exchange applies a unitary matrix (not just a phase) to a degenerate ground state manifold.\n- **Topological quantum computing**: Braiding non-Abelian anyons implements fault-tolerant quantum gates.",
    "3-1": "- **Action principle**: Classical path extremizes the action $S[x] = \\int L\\, dt$.\n- **Path integral**: Quantum amplitude as sum over all paths $\\int \\mathcal{D}x\\, e^{iS[x]/\\hbar}$.\n- **Classical limit**: As $\\hbar \\to 0$, the path integral is dominated by the classical path (stationary phase).\n- **Wave-particle duality**: Path integral connects particle trajectories (paths) to wave interference (phases).",
    "3-2": "- **Propagator**: $K(x_f, t_f; x_i, t_i) = \\langle x_f | e^{-iHt/\\hbar} | x_i \\rangle$ encodes full quantum dynamics.\n- **Time slicing**: Discretize the path integral into $N$ short-time propagators.\n- **Free particle**: Gaussian propagator $K \\propto e^{im(x_f-x_i)^2/2\\hbar t}$.\n- **Correlation functions**: Time-ordered expectation values computed via functional derivatives.",
    "3-3": "- **Stationary phase**: In the $\\hbar \\to 0$ limit, dominant contribution from classical path.\n- **WKB approximation**: Semiclassical wavefunction $\\psi \\sim e^{iS/\\hbar}/\\sqrt{p(x)}$.\n- **Bohr-Sommerfeld**: Quantization condition $\\oint p\\, dx = 2\\pi\\hbar(n + 1/2)$.\n- **Instantons**: Tunneling paths in imaginary time connecting classically forbidden regions.",
    "3-4": "- **Wick rotation**: $t \\to -i\\tau$ transforms oscillatory path integral into convergent Euclidean integral.\n- **Partition function**: $Z = \\text{Tr}(e^{-\\beta H})$ as imaginary-time path integral with periodic boundary conditions.\n- **Ground state projection**: Long imaginary-time evolution projects onto the ground state.\n- **Quantum-classical correspondence**: $d$-dimensional quantum system maps to $(d+1)$-dimensional classical statistical system.",
    "5-2": "- **Interaction picture**: Hybrid of Schrödinger and Heisenberg pictures; states evolve under the perturbation only.\n- **Dyson series**: Systematic expansion of the time-evolution operator in powers of the perturbation.\n- **Fermi's golden rule**: Transition rate $\\Gamma = \\frac{2\\pi}{\\hbar}|\\langle f|V|i\\rangle|^2 \\rho(E_f)$ for transitions into a continuum.\n- **Selection rules**: Symmetry constraints on which matrix elements $\\langle f|V|i\\rangle$ are nonzero.",
    "6-1": "- **Tensor product**: Composite system Hilbert space $\\mathcal{H}_A \\otimes \\mathcal{H}_B$; dimension grows multiplicatively.\n- **Entangled states**: States that cannot be written as $|\\psi\\rangle_A \\otimes |\\phi\\rangle_B$.\n- **Bell states**: Four maximally entangled two-qubit states forming a complete basis.\n- **Bell inequality (CHSH)**: Classical correlations bounded by 2; quantum mechanics achieves $2\\sqrt{2}$.\n- **No-communication theorem**: Entanglement cannot transmit information faster than light.",
    "6-3": "- **Projective measurement**: Von Neumann's postulate with orthogonal projectors.\n- **POVM**: Positive operator-valued measure; generalized measurement with non-orthogonal outcomes.\n- **Naimark dilation**: Every POVM can be realized as a projective measurement on a larger system.\n- **Quantum state tomography**: Reconstructing $\\rho$ from measurement statistics on informationally complete sets.",
    "6-4": "- **Quantum channels**: Completely positive, trace-preserving (CPTP) maps describing general state evolution.\n- **Kraus representation**: $\\rho \\mapsto \\sum_k K_k \\rho K_k^\\dagger$ with $\\sum_k K_k^\\dagger K_k = I$.\n- **Decoherence**: Loss of off-diagonal elements in the density matrix due to environment interaction.\n- **Lindblad equation**: $\\dot{\\rho} = -i[H,\\rho] + \\sum_k (L_k \\rho L_k^\\dagger - \\frac{1}{2}\\{L_k^\\dagger L_k, \\rho\\})$ for Markovian open systems.",
}

LEARNING_OBJ_DEFAULTS = {
    "1-1": "- Represent a qubit state as a vector in $\\mathbb{C}^2$ and on the Bloch sphere.\n- Compute eigenvalues and eigenstates of Pauli matrices.\n- Distinguish between a physical spin-1/2 system and the abstract qubit.",
    "1-2": "- Apply the Born rule to compute measurement probabilities.\n- Evaluate commutators and verify uncertainty relations.\n- Describe state collapse and its Bayesian interpretation.",
    "1-3": "- Solve the Schrödinger equation for time-independent Hamiltonians.\n- Compute the time evolution of spin states in magnetic fields.\n- Construct basic quantum gates from unitary operators.",
}

def process_notebook(path):
    fname = os.path.basename(path)
    sec_id = fname.split('-')[0] + '-' + fname.split('-')[1]

    with open(path, 'r') as f:
        nb = json.load(f)

    # Get title cell
    title_src = ''.join(nb['cells'][0]['source']).strip()

    # Collect all content (excluding title and prompts)
    all_content = collect_all_content(nb)

    # Extract components
    topics, remaining = extract_topics_table(all_content)
    overview_content = extract_overview_content(all_content)
    key_concepts = extract_key_concepts(all_content)
    learning_obj = extract_learning_objectives(all_content)
    glossary = extract_glossary(all_content)

    # Use defaults if missing
    if not overview_content or len(overview_content.strip()) < 20:
        overview_content = OVERVIEW_DEFAULTS.get(sec_id, None)

    if not key_concepts and sec_id in KEY_CONCEPTS_DEFAULTS:
        key_concepts = KEY_CONCEPTS_DEFAULTS[sec_id]

    if not learning_obj and sec_id in LEARNING_OBJ_DEFAULTS:
        learning_obj = LEARNING_OBJ_DEFAULTS[sec_id]

    # Build unified content cell
    parts = []

    # 1. Topics table (always first)
    if topics:
        parts.append(topics)

    # 2. Overview
    if overview_content:
        parts.append(f"### Overview\n\n{overview_content}")

    # 3. Key Concepts
    if key_concepts:
        parts.append(f"### Key Concepts\n\n{key_concepts}")

    # 4. Learning Objectives
    if learning_obj:
        parts.append(f"### Learning Objectives\n\n{learning_obj}")

    # 5. Glossary (if present, at end)
    if glossary:
        parts.append(glossary)

    unified = '\n\n'.join(parts)

    # Clean up: remove duplicate headings, multiple blank lines
    unified = re.sub(r'\n{3,}', '\n\n', unified)

    # Build new notebook
    # Convert unified to source list
    lines = unified.split('\n')
    unified_source = [l + '\n' for l in lines[:-1]]
    if lines[-1]:
        unified_source.append(lines[-1])

    new_cells = [
        nb['cells'][0],  # Title cell
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": unified_source,
            "id": "unified-content"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [],
            "id": "empty-end"
        }
    ]

    nb['cells'] = new_cells

    with open(path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    # Report
    sections = []
    if topics: sections.append('Topics')
    if overview_content: sections.append('Overview')
    if key_concepts: sections.append('Key Concepts')
    if learning_obj: sections.append('Learning Obj')
    if glossary: sections.append('Glossary')
    print(f"  {fname}: {' → '.join(sections)}")

def main():
    parents = get_section_parents()
    print(f"Processing {len(parents)} section parent notebooks\n")

    for p in parents:
        process_notebook(p)

    print(f"\nDone: all {len(parents)} notebooks unified")

if __name__ == '__main__':
    main()
