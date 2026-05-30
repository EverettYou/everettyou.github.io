#!/usr/bin/env python3
"""
Final version: Process PHYS130B ch1_qubit notebooks.

Handles:
1. Verify heading structure (## Lecture Notes, ### Overview, ### Summary)
2. Update Overview with actual section titles
3. Add 2-4 strategic admonitions to subsection notebooks
"""

import json
import os
import re
from pathlib import Path


def is_subsection_notebook(filename):
    """Check if notebook is a subsection (x-x-x pattern)."""
    base = filename.replace('.ipynb', '')
    parts = base.split('-')
    return len(parts) >= 3 and all(p.isdigit() for p in parts[:3])


def extract_section_titles(content):
    """Extract all section titles (### level, not ####) from content."""
    lines = content.split('\n')
    titles = []
    for line in lines:
        stripped = line.strip()
        # Match ### but not ####
        if stripped.startswith('### ') and not stripped.startswith('#### '):
            title = stripped.replace('### ', '', 1).strip()
            if title not in ['Overview', 'Summary']:  # Skip meta sections
                titles.append(title)
    return titles


def replace_overview_bullets(content):
    """Replace generic Overview bullets with actual section titles."""
    lines = content.split('\n')
    overview_idx = -1

    # Find Overview section
    for i, line in enumerate(lines):
        if line.strip() == '### Overview':
            overview_idx = i
            break

    if overview_idx == -1:
        return content

    # Find where bullet list starts and ends
    bullet_start = overview_idx + 1
    while bullet_start < len(lines) and not lines[bullet_start].strip().startswith('- '):
        bullet_start += 1

    bullet_end = bullet_start
    while bullet_end < len(lines) and lines[bullet_end].strip().startswith('- '):
        bullet_end += 1

    # Only proceed if we found bullets
    if bullet_start < len(lines) and lines[bullet_start].startswith('- Core concept'):
        # Extract real sections
        sections = extract_section_titles(content)

        # Create new bullets (up to 4)
        new_bullets = [f"- {s}" for s in sections[:4]]

        if new_bullets:
            # Replace old bullets with new ones
            # Keep the "This section covers:" line before bullets if present
            preserved = []
            for j in range(overview_idx + 1, bullet_start):
                preserved.append(lines[j])

            # Remove old bullets
            for _ in range(bullet_start, bullet_end):
                if bullet_start < len(lines):
                    lines.pop(bullet_start)

            # Insert new bullets
            insert_idx = overview_idx + len(preserved) + 1
            for bullet in reversed(new_bullets):
                lines.insert(insert_idx, bullet)

            content = '\n'.join(lines)

    return content


def add_custom_admonitions(content, filename):
    """Add custom admonitions based on notebook filename."""
    current_count = content.count(':::{admonition}')

    # Only add if we have fewer than 2 admonitions
    if current_count >= 2:
        return content

    lines = content.split('\n')

    # Find Summary section
    summary_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == '### Summary':
            summary_idx = i
            break

    if summary_idx == -1:
        return content

    # Build admonitions based on filename
    admonitions_to_add = []

    if '1-1-1' in filename:
        admonitions_to_add = [
            ('Why Superposition Matters', 'note',
             'The ability of qubits to exist in superposition is the foundation of quantum computing power. '
             'Unlike a classical bit (definitely 0 or 1), a qubit can be in a weighted combination of both states, '
             'exponentially increasing the information-carrying capacity of multiple qubits.')
        ]
    elif '1-1-2' in filename:
        admonitions_to_add = [
            ('Why the Bloch Sphere?', 'note',
             'The Bloch sphere is not just a visualization—it is a complete geometric representation of all pure qubit states. '
             'Every point on the unit sphere corresponds to exactly one state, and rotations correspond to unitary operations. '
             'This geometric picture reveals hidden symmetries and makes quantum mechanics intuitive.')
        ]
    elif '1-1-3' in filename:
        admonitions_to_add = [
            ('Hermiticity is Essential', 'important',
             'Only Hermitian operators can represent physical observables because their eigenvalues are guaranteed to be real—a requirement for measurable quantities. '
             'Non-Hermitian operators would give complex measurement outcomes, which have no physical meaning.')
        ]
    elif '1-2-1' in filename:
        if current_count < 1:
            admonitions_to_add = [
                ('The Mystery of Measurement', 'warning',
                 'Measurement in quantum mechanics is qualitatively different from classical observation. '
                 'The act of measurement irreversibly changes the system, collapsing the superposition to a definite eigenstate. '
                 'This is not a limitation of our apparatus—it is fundamental to quantum theory.')
            ]
    elif '1-2-2' in filename:
        if current_count < 1:
            admonitions_to_add = [
                ('Uncertainty is Fundamental', 'important',
                 'The uncertainty principle is not due to experimental imprecision. '
                 'It reflects a deep truth: complementary observables cannot be simultaneously well-defined. '
                 'For non-commuting operators like $\\sigma^x$ and $\\sigma^z$, they share no common eigenbasis.')
            ]
    elif '1-2-3' in filename:
        if current_count < 1:
            admonitions_to_add = [
                ('Pure vs. Mixed States', 'important',
                 'Pure states (described by kets) are the result of complete preparation. '
                 'Mixed states arise from partial information or from tracing out part of an entangled system. '
                 'The density matrix elegantly handles both, making it essential for open quantum systems.')
            ]
    elif '1-3-1' in filename:
        admonitions_to_add = [
            ('Why Unitary Evolution?', 'important',
             'Unitarity is the mathematical expression of probability conservation. '
             'Any evolution that does not preserve the norm $\\langle\\psi|\\psi\\rangle = 1$ would violate the Born rule. '
             'The Hamiltonian being Hermitian ensures that $e^{-i\\hat{H}t/\\hbar}$ is automatically unitary.')
        ]
    elif '1-3-2' in filename:
        if current_count < 1:
            admonitions_to_add = [
                ('Rabi Oscillations and Quantum Control', 'note',
                 'The periodic exchange of population between energy levels driven by a resonant field underlies NMR, ESR, and quantum gates. '
                 'By controlling the Rabi frequency $\\Omega$, we can precisely manipulate quantum states—the foundation of quantum computing.')
            ]
    elif '1-3-3' in filename:
        if current_count < 1:
            admonitions_to_add = [
                ('Heisenberg and Schrödinger Pictures', 'note',
                 'In the Schrödinger picture, states evolve and operators are fixed. '
                 'In the Heisenberg picture, operators evolve while states are fixed. '
                 'Both are equivalent; the choice depends on which picture simplifies the calculation.')
            ]

    # Add admonitions before Summary
    for title, admon_class, admon_text in admonitions_to_add:
        admonition = f'\n:::{{{admon_class}}} {title}\n:class: {admon_class}\n{admon_text}\n:::\n'
        lines.insert(summary_idx, admonition)
        summary_idx += 1  # Move index forward after insertion

    return '\n'.join(lines)


def process_notebook(filepath):
    """Process a single notebook."""
    filename = os.path.basename(filepath)
    is_subsection = is_subsection_notebook(filename)

    print(f"  {filename:45s}", end=' ', flush=True)

    try:
        with open(filepath, 'r') as f:
            notebook = json.load(f)

        if len(notebook['cells']) < 3:
            print("SKIP (too few cells)")
            return False

        content_cell = notebook['cells'][2]

        if content_cell.get('cell_type') != 'markdown':
            print("SKIP (not markdown)")
            return False

        # Extract content
        if isinstance(content_cell['source'], list):
            current_content = ''.join(content_cell['source'])
        else:
            current_content = content_cell['source']

        modified_content = current_content

        if is_subsection:
            # Update Overview bullets with real section titles
            modified_content = replace_overview_bullets(modified_content)

            # Add strategic admonitions
            modified_content = add_custom_admonitions(modified_content, filename)

        # Write back
        content_cell['source'] = modified_content

        with open(filepath, 'w') as f:
            json.dump(notebook, f, indent=1)

        print("OK")
        return True

    except Exception as e:
        print(f"ERROR: {e}")
        return False


def main():
    """Process all notebooks."""
    base_dir = Path('/sessions/tender-admiring-allen/mnt/teaching/PHYS130B/notes_src/ch1_qubit')

    if not base_dir.exists():
        print(f"ERROR: Directory {base_dir} not found")
        return

    notebooks = sorted(base_dir.glob('*.ipynb'))

    if not notebooks:
        print("No notebooks found")
        return

    subsection_count = sum(1 for nb in notebooks if is_subsection_notebook(nb.name))
    parent_count = len(notebooks) - subsection_count

    print(f"\nFound {len(notebooks)} notebooks")
    print(f"  {subsection_count} subsection (x-x-x)")
    print(f"  {parent_count} section parent (x-x)")
    print("\nProcessing:")
    print("=" * 70)

    processed = 0
    for notebook_path in notebooks:
        if process_notebook(str(notebook_path)):
            processed += 1

    print("=" * 70)
    print(f"\nCompleted: {processed}/{len(notebooks)} notebooks")


if __name__ == '__main__':
    main()
