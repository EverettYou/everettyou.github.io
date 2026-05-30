#!/usr/bin/env python3
"""
Fix corrupted notebooks and add missing admonitions to section parents.
"""

import json
import os

NOTEBOOK_DIR = "/sessions/tender-admiring-allen/mnt/teaching/PHYS130B/notes_src/ch3_path-integral"

# Files to repair: section parents (currently have 0 admonitions)
SECTION_PARENTS_NEEDING_ADMONITIONS = {
    '3-2-propagator.ipynb': {
        'title': 'The propagator in path integrals',
        'content': 'The propagator $K(\\mathbf{x}_f, t_f; \\mathbf{x}_i, t_i)$ is the quantum amplitude for evolution between spacetime points. '
                  'In the path integral formulation, it is the sum over all paths weighted by $e^{iS/\\hbar}$. '
                  'Time-slicing and Gaussian integrals enable exact evaluation for free particles.'
    },
    '3-3-stationary-phase.ipynb': {
        'title': 'Stationary phase and classical paths',
        'content': 'The stationary phase approximation shows how classical paths emerge from quantum interference. '
                  'When $\\hbar$ is small, only paths with stationary action $\\delta S = 0$ contribute coherently; '
                  'all others oscillate destructively. This explains why particles follow definite classical trajectories at macroscopic scales.'
    }
}

def repair_and_add_admonition(filename, admon_info):
    """Repair corrupted notebook and add missing admonition."""
    filepath = os.path.join(NOTEBOOK_DIR, filename)

    with open(filepath, 'r') as f:
        nb = json.load(f)

    cell2 = nb['cells'][2]
    source = cell2.get('source', [])

    # Convert to string if it's a list
    if isinstance(source, list):
        source_text = ''.join(source)
    else:
        source_text = source

    # Split on newlines (may have been collapsed)
    lines = source_text.split('\n')

    # Check if admonition already exists (properly)
    if source_text.count(':::{admonition}') > 0 and source_text.count(':::') >= 2:
        print(f"SKIP: {filename} already has proper admonitions")
        return False

    # Remove any malformed admonition markers
    lines = [line for line in lines if not ('::{{' in line or ':::{admonition}' in line)]

    # Reconstruct up to Summary
    output_lines = []
    for line in lines:
        if line.strip().startswith('### Summary'):
            break
        output_lines.append(line)

    # Add the admonition before Summary
    admonition_block = [
        '',
        f"::{{{{admonition}} {admon_info['title']}",
        ":class: important",
        "",
        admon_info['content'],
        ":::{{"
    ]

    output_lines.extend(admonition_block)
    output_lines.append('')

    # Add Summary and rest
    found_summary = False
    for line in lines:
        if line.strip().startswith('### Summary'):
            found_summary = True
        if found_summary:
            output_lines.append(line)

    # Update cell source as list of strings (proper format)
    cell2['source'] = output_lines

    with open(filepath, 'w') as f:
        json.dump(nb, f, indent=1)

    print(f"FIXED: {filename} repaired and admonition added")
    return True

def main():
    for filename, admon_info in SECTION_PARENTS_NEEDING_ADMONITIONS.items():
        repair_and_add_admonition(filename, admon_info)

if __name__ == '__main__':
    main()
