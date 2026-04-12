#!/usr/bin/env python3
"""
Update all 21 section parent notebooks:
- Replace structure/subsections heading with ### Topics
- Format as {list-table} with Sec / Topic / Keywords
- Place Topics before Key Concepts
"""
import json
import re
import os
import glob

BASE = "/sessions/tender-admiring-allen/mnt/teaching/PHYS130B/notes_src"

# Map of section parent -> list of (subsec_id, filename, topic_title, keywords)
# We'll auto-detect subsections and read their titles

def get_section_parents():
    """Return list of (chapter_dir, section_file) tuples."""
    parents = []
    for ch_dir in sorted(glob.glob(f"{BASE}/ch*")):
        ch_name = os.path.basename(ch_dir)
        for f in sorted(glob.glob(f"{ch_dir}/[0-9]-[0-9]-*.ipynb")):
            fname = os.path.basename(f)
            # Exclude subsection files (x-y-z-*.ipynb)
            parts = fname.split('-')
            # Section parents: 1-1-xxx.ipynb (digit-digit-word)
            # Subsections: 1-1-1-xxx.ipynb (digit-digit-digit-word)
            if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit():
                if parts[2].isdigit():
                    continue  # subsection
                parents.append(f)
    return parents

def get_subsections(parent_path):
    """Find subsection files for a given section parent."""
    parent_dir = os.path.dirname(parent_path)
    parent_fname = os.path.basename(parent_path)
    # Extract section number like "1-2" from "1-2-measurement.ipynb"
    m = re.match(r'(\d+)-(\d+)-', parent_fname)
    if not m:
        return []
    ch_num, sec_num = m.group(1), m.group(2)
    prefix = f"{ch_num}-{sec_num}-"

    subsections = []
    for f in sorted(glob.glob(f"{parent_dir}/{prefix}*.ipynb")):
        fname = os.path.basename(f)
        if fname == parent_fname:
            continue
        # Check it's a subsection (x-y-z-*.ipynb)
        parts = fname.split('-')
        if len(parts) >= 4 and parts[2].isdigit():
            subsec_id = f"{ch_num}.{sec_num}.{parts[2]}"
            # Read title from notebook
            title = get_notebook_title(f)
            link_name = fname.replace('.ipynb', '')
            subsections.append((subsec_id, link_name, title))
    return subsections

def get_notebook_title(path):
    """Extract title from first cell of notebook."""
    with open(path, 'r') as f:
        nb = json.load(f)
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            src = ''.join(cell['source'])
            m = re.match(r'#\s+\d+\.\d+\.\d+\s+(.*)', src.strip())
            if m:
                return m.group(1).strip()
            # Try without subsection number
            m = re.match(r'#\s+(.*)', src.strip())
            if m:
                return m.group(1).strip()
    return os.path.basename(path).replace('.ipynb', '')

def generate_keywords(subsec_id, title, parent_path):
    """Generate keywords based on subsection content."""
    # Manual keywords map for better quality
    keywords_map = {
        # Ch1
        "1.1.1": "spin-1/2, qubit, Hilbert space",
        "1.1.2": "Pauli matrices, eigenvalues, spectral decomposition",
        "1.1.3": "Bloch sphere, pure states, geometric representation",
        # Ch1.2
        "1.2.1": "Born rule, projective measurement, expectation values",
        "1.2.2": "commutators, complementarity, Heisenberg principle",
        "1.2.3": "projectors, conditional probability, state collapse, Bayesian interpretation",
        # Ch1.3
        "1.3.1": "Schrödinger equation, unitary evolution, Hamiltonian",
        "1.3.2": "Larmor precession, magnetic resonance, Rabi oscillation",
        "1.3.3": "qubit gates, NOT, Hadamard, CNOT",
        # Ch2.1
        "2.1.1": "exchange symmetry, bosons, fermions",
        "2.1.2": "symmetrization, Slater determinant, Pauli exclusion",
        "2.1.3": "second quantization, creation/annihilation operators, Fock space",
        # Ch2.2
        "2.2.1": "angular momentum addition, Clebsch–Gordan, tensor product",
        "2.2.2": "singlet, triplet, exchange interaction",
        "2.2.3": "spin-orbit coupling, fine structure, total angular momentum",
        # Ch2.3
        "2.3.1": "2D particles, braid group, exchange phase",
        "2.3.2": "Abelian anyons, fractional statistics, Aharonov–Bohm",
        "2.3.3": "non-Abelian anyons, topological quantum computing, braiding",
        # Ch3.1
        "3.1.1": "canonical quantization, commutation relations, Poisson brackets",
        "3.1.2": "Weyl ordering, operator ordering ambiguity, symmetrization",
        "3.1.3": "functional integral, sum over paths, measure",
        # Ch3.2
        "3.2.1": "free particle propagator, Gaussian integral, kernel",
        "3.2.2": "harmonic oscillator propagator, classical action, Mehler kernel",
        "3.2.3": "correlation functions, time ordering, Green's function",
        # Ch3.3
        "3.3.1": "steepest descent, saddle point, asymptotic expansion",
        "3.3.2": "classical limit, ℏ→0, WKB connection",
        "3.3.3": "instantons, tunneling, double-well potential",
        # Ch3.4
        "3.4.1": "Wick rotation, Euclidean time, thermal partition function",
        "3.4.2": "partition function, thermal density matrix, statistical mechanics",
        "3.4.3": "quantum-classical correspondence, lattice models, transfer matrix",
        # Ch4.1
        "4.1.1": "gauge invariance, minimal coupling, covariant derivative",
        "4.1.2": "electromagnetic potentials, gauge transformation, phase",
        "4.1.3": "Wilson loop, holonomy, parallel transport",
        # Ch4.2
        "4.2.1": "Aharonov–Bohm effect, magnetic flux, topological phase",
        "4.2.2": "flux quantization, persistent currents, SQUID",
        "4.2.3": "magnetic translation, Bloch theorem, Brillouin zone",
        # Ch4.3
        "4.3.1": "Landau gauge, cyclotron frequency, degeneracy",
        "4.3.2": "symmetric gauge, angular momentum, lowest Landau level",
        "4.3.3": "quantum Hall effect, edge states, topological invariant",
        # Ch4.4
        "4.4.1": "spin coherent states, geometric phase, spinor",
        "4.4.2": "Dirac monopole, quantization condition, fiber bundle",
        "4.4.3": "Dirac string, gauge patches, topological charge",
        # Ch4.5
        "4.5.1": "Berry phase, adiabatic evolution, geometric phase",
        "4.5.2": "Berry connection, Berry curvature, Chern number",
        "4.5.3": "applications, molecular physics, band topology",
        # Ch5.1
        "5.1.1": "non-degenerate perturbation, energy corrections, state corrections",
        "5.1.2": "degenerate perturbation, effective Hamiltonian, level splitting",
        "5.1.3": "Stark effect, Zeeman effect, fine structure",
        # Ch5.2
        "5.2.1": "interaction picture, Dyson series, time-ordering",
        "5.2.2": "Fermi's golden rule, transition rate, density of states",
        "5.2.3": "harmonic perturbation, adiabatic theorem, Green's functions",
        # Ch6.1
        "6.1.1": "tensor product, composite systems, separability",
        "6.1.2": "Bell states, maximally entangled, Schmidt decomposition",
        "6.1.3": "Bell inequality, CHSH, nonlocality, Tsirelson bound",
        # Ch6.2
        "6.2.1": "density operator, pure vs mixed, Bloch ball",
        "6.2.2": "partial trace, reduced density matrix, subsystem state",
        "6.2.3": "von Neumann entropy, entanglement entropy, information",
        # Ch6.3
        "6.3.1": "POVM, generalized measurement, positive operators",
        "6.3.2": "Naimark dilation, ancilla, indirect measurement",
        "6.3.3": "quantum state tomography, informationally complete, reconstruction",
        # Ch6.4
        "6.4.1": "quantum channels, Kraus operators, CPTP maps",
        "6.4.2": "decoherence, dephasing, amplitude damping",
        "6.4.3": "Lindblad equation, master equation, Markovian dynamics",
    }
    return keywords_map.get(subsec_id, "")

def build_topics_table(subsections):
    """Build a {list-table} string for the Topics section."""
    lines = [
        "### Topics\n",
        "\n",
        "```{list-table}\n",
        ":header-rows: 1\n",
        ":widths: 8 35 57\n",
        "\n",
        "* - Sec\n",
        "  - Topic\n",
        "  - Keywords\n",
    ]
    for subsec_id, link_name, title in subsections:
        lines.append(f"* - {subsec_id}\n")
        lines.append(f"  - [{title}]({link_name})\n")
        kw = generate_keywords(subsec_id, title, "")
        lines.append(f"  - {kw}\n")
    lines.append("```\n")
    return lines

def update_notebook(parent_path):
    """Update a single section parent notebook."""
    with open(parent_path, 'r') as f:
        nb = json.load(f)

    subsections = get_subsections(parent_path)
    if not subsections:
        print(f"  WARNING: No subsections found for {parent_path}")
        return False

    topics_lines = build_topics_table(subsections)

    # Find the cell containing the structure section
    # Look for patterns: "### Structure", "### Subsections", "### Chapter Structure",
    # "### The Structure", "### Detailed Subsections", "### Key Topics"
    structure_patterns = [
        r'###\s+Structure\b',
        r'###\s+Subsections\b',
        r'###\s+Chapter Structure\b',
        r'###\s+The Structure\b',
        r'###\s+Detailed Subsections\b',
        r'###\s+Key Topics\b',
    ]

    modified = False
    for cell_idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'markdown':
            continue

        src_text = ''.join(cell['source'])

        # Check for any structure pattern
        found_pattern = None
        for pat in structure_patterns:
            if re.search(pat, src_text):
                found_pattern = pat
                break

        if found_pattern is None:
            continue

        # Found the cell with structure section
        # Now we need to:
        # 1. Find the structure heading and its content (until next ### or end)
        # 2. Replace with Topics table
        # 3. Ensure Topics appears before Key Concepts

        lines = cell['source'] if isinstance(cell['source'], list) else cell['source'].split('\n')
        # Normalize to list of lines
        if isinstance(cell['source'], str):
            lines = [l + '\n' for l in cell['source'].split('\n')]
        else:
            lines = list(cell['source'])

        # Find start of structure section
        struct_start = None
        struct_end = None
        for i, line in enumerate(lines):
            if struct_start is None:
                for pat in structure_patterns:
                    if re.search(pat, line):
                        struct_start = i
                        break
            elif struct_start is not None and struct_end is None:
                # Find end: next ### heading or end of cell
                if re.match(r'###\s+', line) and i > struct_start:
                    struct_end = i
                    break

        if struct_start is None:
            continue
        if struct_end is None:
            struct_end = len(lines)

        # Check if there's a Key Concepts section AFTER structure
        key_concepts_after = False
        key_concepts_start = None
        for i in range(struct_end, len(lines)):
            if re.search(r'###\s+Key Concepts', lines[i]):
                key_concepts_after = True
                key_concepts_start = i
                break

        # Also check if Key Concepts is BEFORE structure
        key_concepts_before = False
        key_concepts_before_start = None
        key_concepts_before_end = None
        for i in range(0, struct_start):
            if re.search(r'###\s+Key Concepts', lines[i]):
                key_concepts_before = True
                key_concepts_before_start = i
                # Find end of key concepts section
                for j in range(i + 1, struct_start + 1):
                    if re.match(r'###\s+', lines[j]) and j > i:
                        key_concepts_before_end = j
                        break
                if key_concepts_before_end is None:
                    key_concepts_before_end = struct_start
                break

        # Build new cell content
        if key_concepts_before:
            # Topics should go before Key Concepts
            # Replace: [before KC] [KC section] [structure section] [after]
            # With:    [before KC] [Topics] [KC section] [after structure]
            new_lines = lines[:key_concepts_before_start]
            new_lines.extend(topics_lines)
            new_lines.append("\n")
            new_lines.extend(lines[key_concepts_before_start:struct_start])
            new_lines.extend(lines[struct_end:])
        elif key_concepts_after:
            # Structure is before Key Concepts - just replace structure with Topics
            new_lines = lines[:struct_start]
            new_lines.extend(topics_lines)
            new_lines.append("\n")
            new_lines.extend(lines[struct_end:])
        else:
            # No Key Concepts section, just replace structure
            new_lines = lines[:struct_start]
            new_lines.extend(topics_lines)
            new_lines.append("\n")
            new_lines.extend(lines[struct_end:])

        cell['source'] = new_lines
        modified = True
        print(f"  Updated cell {cell_idx}: replaced structure section with Topics table")
        break

    if not modified:
        # No structure section found - need to add Topics table
        # Find the appropriate cell (usually cell 1 or the one with ## Brief Introduction / ## Lecture Notes)
        for cell_idx, cell in enumerate(nb['cells']):
            if cell['cell_type'] != 'markdown':
                continue
            src_text = ''.join(cell['source'])
            if '## Brief Introduction' in src_text or '## Lecture Notes' in src_text:
                lines = list(cell['source']) if isinstance(cell['source'], list) else [l + '\n' for l in cell['source'].split('\n')]

                # Find ### Overview or first ### heading
                insert_pos = None
                for i, line in enumerate(lines):
                    if re.match(r'###\s+Overview', line):
                        insert_pos = i
                        break
                    elif re.match(r'###\s+', line) and insert_pos is None:
                        insert_pos = i

                if insert_pos is None:
                    # Add at end
                    insert_pos = len(lines)

                new_lines = lines[:insert_pos]
                new_lines.extend(topics_lines)
                new_lines.append("\n")
                new_lines.extend(lines[insert_pos:])
                cell['source'] = new_lines
                modified = True
                print(f"  Added Topics table to cell {cell_idx} (no existing structure section found)")
                break

    if not modified:
        print(f"  ERROR: Could not find appropriate cell to modify in {parent_path}")
        return False

    with open(parent_path, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    return True

def main():
    parents = get_section_parents()
    print(f"Found {len(parents)} section parent notebooks\n")

    success = 0
    for p in parents:
        print(f"Processing: {os.path.basename(p)}")
        subsections = get_subsections(p)
        print(f"  Subsections: {[s[0] for s in subsections]}")
        if update_notebook(p):
            success += 1
        print()

    print(f"\nDone: {success}/{len(parents)} updated successfully")

if __name__ == '__main__':
    main()
