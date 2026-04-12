#!/usr/bin/env python3
"""Swap sections 6.1 (Entanglement) and 6.2 (Density Matrix) in the Jupyter Book."""

import json, os, re, glob, shutil

BASE = "/sessions/tender-admiring-allen/mnt/teaching/PHYS130B/notes_src"
CH6 = os.path.join(BASE, "ch6_quantum-foundations")

# ── Step 1: Rename files via temp intermediary ──────────────────────────
# Old 6-1-* → tmp-old1-*, Old 6-2-* → tmp-old2-*
# Then tmp-old1-* → 6-2-*, tmp-old2-* → 6-1-*

files_61 = sorted(glob.glob(os.path.join(CH6, "6-1-*.ipynb")))
files_62 = sorted(glob.glob(os.path.join(CH6, "6-2-*.ipynb")))

print("=== Step 1: Renaming files ===")

# Phase 1: rename to temp
for f in files_61:
    base = os.path.basename(f)
    tmp = os.path.join(CH6, "tmp-old1-" + base)
    os.rename(f, tmp)
    print(f"  {base} → tmp-old1-{base}")

for f in files_62:
    base = os.path.basename(f)
    tmp = os.path.join(CH6, "tmp-old2-" + base)
    os.rename(f, tmp)
    print(f"  {base} → tmp-old2-{base}")

# Phase 2: tmp-old1 (was 6-1) → 6-2, tmp-old2 (was 6-2) → 6-1
for f in sorted(glob.glob(os.path.join(CH6, "tmp-old1-6-1-*.ipynb"))):
    base = os.path.basename(f).replace("tmp-old1-6-1-", "6-2-")
    dest = os.path.join(CH6, base)
    os.rename(f, dest)
    print(f"  {os.path.basename(f)} → {base}")

for f in sorted(glob.glob(os.path.join(CH6, "tmp-old2-6-2-*.ipynb"))):
    base = os.path.basename(f).replace("tmp-old2-6-2-", "6-1-")
    dest = os.path.join(CH6, base)
    os.rename(f, dest)
    print(f"  {os.path.basename(f)} → {base}")

print(f"\nFiles after rename:")
for f in sorted(glob.glob(os.path.join(CH6, "6-[12]-*.ipynb"))):
    print(f"  {os.path.basename(f)}")

# ── Step 2: Update internal section numbers in all Ch6 notebooks ────────
print("\n=== Step 2: Updating section numbers inside notebooks ===")

# Mapping of old → new for section references
# Old 6.1 (Entanglement) → New 6.2
# Old 6.2 (Density Matrix) → New 6.1
# We need to be careful about ordering: use temp placeholders

def update_cell_source(source_lines, replacements):
    """Apply replacements to cell source lines."""
    text = ''.join(source_lines)
    for old, new in replacements:
        text = text.replace(old, new)
    # Convert back to list of lines
    lines = []
    for line in text.split('\n'):
        lines.append(line + '\n')
    if lines:
        lines[-1] = lines[-1].rstrip('\n')  # last line no trailing newline if original didn't have it
    return lines

def update_notebook(filepath, replacements):
    """Update all cells in a notebook with the given replacements."""
    with open(filepath) as f:
        nb = json.load(f)
    
    changed = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown' and cell['source']:
            old_text = ''.join(cell['source'])
            new_text = old_text
            for old, new in replacements:
                new_text = new_text.replace(old, new)
            if new_text != old_text:
                # Rebuild source as list of lines
                lines = new_text.split('\n')
                new_source = []
                for i, line in enumerate(lines):
                    if i < len(lines) - 1:
                        new_source.append(line + '\n')
                    else:
                        new_source.append(line)
                cell['source'] = new_source
                changed = True
    
    if changed:
        with open(filepath, 'w') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"  Updated: {os.path.basename(filepath)}")
    return changed

# For files that WERE 6-2 (now named 6-1): update 6.2→6.1, 6-2→6-1
# For files that WERE 6-1 (now named 6-2): update 6.1→6.2, 6-1→6-2
# But cross-references between them need careful handling.
#
# Strategy: Two-pass with temporary placeholders
# Pass 1: old-6.1→__TEMP_ENT__, old-6.2→__TEMP_DM__
# Pass 2: __TEMP_ENT__→6.2, __TEMP_DM__→6.1

# Process ALL .ipynb files in ALL chapters (cross-refs exist)
all_notebooks = sorted(glob.glob(os.path.join(BASE, "**/*.ipynb"), recursive=True))
# Skip _build directory
all_notebooks = [f for f in all_notebooks if '/_build/' not in f]

print(f"  Processing {len(all_notebooks)} notebooks...")

# Pass 1: Replace old numbers with placeholders
pass1_replacements = [
    # Section numbers in text (6.1.x → __ENT_x__, 6.2.x → __DM_x__)
    ("§6.1.1", "§__ENT1__"),
    ("§6.1.2", "§__ENT2__"),
    ("§6.1.3", "§__ENT3__"),
    ("§6.2.1", "§__DM1__"),
    ("§6.2.2", "§__DM2__"),
    ("§6.2.3", "§__DM3__"),
    ("§6.1", "§__ENT__"),
    ("§6.2", "§__DM__"),
    # Titles: "# 6.1.x" and "# 6.2.x"
    ("# 6.1.1 ", "# __ENT1__ "),
    ("# 6.1.2 ", "# __ENT2__ "),
    ("# 6.1.3 ", "# __ENT3__ "),
    ("# 6.2.1 ", "# __DM1__ "),
    ("# 6.2.2 ", "# __DM2__ "),
    ("# 6.2.3 ", "# __DM3__ "),
    ("# 6.1 ", "# __ENT__ "),
    ("# 6.2 ", "# __DM__ "),
    # File references (links): 6-1-x → __ent_x__, 6-2-x → __dm_x__
    ("6-1-1-composite-systems", "__ent1_composite-systems__"),
    ("6-1-2-entanglement-measures", "__ent2_entanglement-measures__"),
    ("6-1-3-bell-inequality", "__ent3_bell-inequality__"),
    ("6-2-1-mixed-states", "__dm1_mixed-states__"),
    ("6-2-2-partial-trace", "__dm2_partial-trace__"),
    ("6-2-3-entropy", "__dm3_entropy__"),
    ("6-1-entanglement", "__ent_entanglement__"),
    ("6-2-density-matrix", "__dm_density-matrix__"),
    # Equation labels
    ("eq-6-1-", "eq-__eqent__-"),
    ("eq-6-2-", "eq-__eqdm__-"),
    # Topics table numbers
    ("* - 6.1.1\n", "* - __TENT1__\n"),
    ("* - 6.1.2\n", "* - __TENT2__\n"),
    ("* - 6.1.3\n", "* - __TENT3__\n"),
    ("* - 6.2.1\n", "* - __TDM1__\n"),
    ("* - 6.2.2\n", "* - __TDM2__\n"),
    ("* - 6.2.3\n", "* - __TDM3__\n"),
]

for f in all_notebooks:
    update_notebook(f, pass1_replacements)

# Pass 2: Placeholders → new numbers (Entanglement=6.2, DensityMatrix=6.1)
pass2_replacements = [
    ("§__ENT1__", "§6.2.1"),
    ("§__ENT2__", "§6.2.2"),
    ("§__ENT3__", "§6.2.3"),
    ("§__DM1__", "§6.1.1"),
    ("§__DM2__", "§6.1.2"),
    ("§__DM3__", "§6.1.3"),
    ("§__ENT__", "§6.2"),
    ("§__DM__", "§6.1"),
    ("# __ENT1__ ", "# 6.2.1 "),
    ("# __ENT2__ ", "# 6.2.2 "),
    ("# __ENT3__ ", "# 6.2.3 "),
    ("# __DM1__ ", "# 6.1.1 "),
    ("# __DM2__ ", "# 6.1.2 "),
    ("# __DM3__ ", "# 6.1.3 "),
    ("# __ENT__ ", "# 6.2 "),
    ("# __DM__ ", "# 6.1 "),
    ("__ent1_composite-systems__", "6-2-1-composite-systems"),
    ("__ent2_entanglement-measures__", "6-2-2-entanglement-measures"),
    ("__ent3_bell-inequality__", "6-2-3-bell-inequality"),
    ("__dm1_mixed-states__", "6-1-1-mixed-states"),
    ("__dm2_partial-trace__", "6-1-2-partial-trace"),
    ("__dm3_entropy__", "6-1-3-entropy"),
    ("__ent_entanglement__", "6-2-entanglement"),
    ("__dm_density-matrix__", "6-1-density-matrix"),
    ("eq-__eqent__-", "eq-6-2-"),
    ("eq-__eqdm__-", "eq-6-1-"),
    ("* - __TENT1__\n", "* - 6.2.1\n"),
    ("* - __TENT2__\n", "* - 6.2.2\n"),
    ("* - __TENT3__\n", "* - 6.2.3\n"),
    ("* - __TDM1__\n", "* - 6.1.1\n"),
    ("* - __TDM2__\n", "* - 6.1.2\n"),
    ("* - __TDM3__\n", "* - 6.1.3\n"),
]

for f in all_notebooks:
    update_notebook(f, pass2_replacements)

# ── Step 3: Update _toc.yml ─────────────────────────────────────────────
print("\n=== Step 3: Updating _toc.yml ===")
toc_path = os.path.join(BASE, "_toc.yml")
with open(toc_path) as f:
    toc = f.read()

# Replace ch6 section — use placeholder approach  
toc = toc.replace("ch6_quantum-foundations/6-1-entanglement", "ch6_quantum-foundations/__SLOT_ENT__")
toc = toc.replace("ch6_quantum-foundations/6-1-1-composite-systems", "ch6_quantum-foundations/__SLOT_ENT1__")
toc = toc.replace("ch6_quantum-foundations/6-1-2-entanglement-measures", "ch6_quantum-foundations/__SLOT_ENT2__")
toc = toc.replace("ch6_quantum-foundations/6-1-3-bell-inequality", "ch6_quantum-foundations/__SLOT_ENT3__")
toc = toc.replace("ch6_quantum-foundations/6-2-density-matrix", "ch6_quantum-foundations/__SLOT_DM__")
toc = toc.replace("ch6_quantum-foundations/6-2-1-mixed-states", "ch6_quantum-foundations/__SLOT_DM1__")
toc = toc.replace("ch6_quantum-foundations/6-2-2-partial-trace", "ch6_quantum-foundations/__SLOT_DM2__")
toc = toc.replace("ch6_quantum-foundations/6-2-3-entropy", "ch6_quantum-foundations/__SLOT_DM3__")

# Now swap: ENT→6-2, DM→6-1
toc = toc.replace("__SLOT_ENT__", "6-2-entanglement")
toc = toc.replace("__SLOT_ENT1__", "6-2-1-composite-systems")
toc = toc.replace("__SLOT_ENT2__", "6-2-2-entanglement-measures")
toc = toc.replace("__SLOT_ENT3__", "6-2-3-bell-inequality")
toc = toc.replace("__SLOT_DM__", "6-1-density-matrix")
toc = toc.replace("__SLOT_DM1__", "6-1-1-mixed-states")
toc = toc.replace("__SLOT_DM2__", "6-1-2-partial-trace")
toc = toc.replace("__SLOT_DM3__", "6-1-3-entropy")

# Now we need to swap the ORDER of the two section blocks in the TOC
# Currently: 6-2-entanglement (was first), 6-1-density-matrix (was second)
# after replacement. We need 6-1 first, then 6-2.
# Let's find and swap the blocks.
lines = toc.split('\n')
new_lines = []
i = 0
block_61 = []
block_62 = []
in_block = None

while i < len(lines):
    line = lines[i]
    # Detect start of section blocks in ch6
    if 'ch6_quantum-foundations/6-2-entanglement' in line and 'sections' not in lines[i-1] if i > 0 else False:
        # This is the entanglement parent (now numbered 6-2, but appears first in file)
        in_block = 'ent'
        block_62.append(line)
        i += 1
        # Collect subsections
        while i < len(lines):
            if lines[i].strip().startswith('- file: ch6_quantum-foundations/6-2-') or lines[i].strip() == 'sections:':
                block_62.append(lines[i])
                i += 1
            elif lines[i].strip().startswith('- file: ch6_quantum-foundations/6-1-'):
                break
            else:
                break
        continue
    elif 'ch6_quantum-foundations/6-1-density-matrix' in line:
        in_block = 'dm'
        block_61.append(line)
        i += 1
        while i < len(lines):
            if lines[i].strip().startswith('- file: ch6_quantum-foundations/6-1-') or lines[i].strip() == 'sections:':
                block_61.append(lines[i])
                i += 1
            elif lines[i].strip().startswith('- file: ch6_quantum-foundations/6-'):
                break
            else:
                break
        # Now output block_61 first, then block_62
        new_lines.extend(block_61)
        new_lines.extend(block_62)
        continue
    else:
        new_lines.append(line)
        i += 1

toc = '\n'.join(new_lines)

with open(toc_path, 'w') as f:
    f.write(toc)
print("  _toc.yml updated")

# ── Step 4: Update index.md (main) ──────────────────────────────────────
print("\n=== Step 4: Updating index.md ===")
idx_path = os.path.join(BASE, "index.md")
with open(idx_path) as f:
    idx = f.read()

# Swap the entries in Ch6 table
idx = idx.replace(
    "* - 6.1\n  - [Entanglement](ch6_quantum-foundations/6-1-entanglement)\n  - §16.1, §16.2\n* - 6.2\n  - [Density Matrix](ch6_quantum-foundations/6-2-density-matrix)\n  - §16.3",
    "* - 6.1\n  - [Density Matrix](ch6_quantum-foundations/6-1-density-matrix)\n  - §16.3\n* - 6.2\n  - [Entanglement](ch6_quantum-foundations/6-2-entanglement)\n  - §16.1, §16.2"
)

with open(idx_path, 'w') as f:
    f.write(idx)
print("  index.md updated")

# ── Step 5: Update ch6/index.md ─────────────────────────────────────────
print("\n=== Step 5: Updating ch6/index.md ===")
ch6idx_path = os.path.join(CH6, "index.md")
with open(ch6idx_path) as f:
    ch6idx = f.read()

ch6idx = ch6idx.replace(
    "* - 6.1\n  - [Entanglement](6-1-entanglement)\n  - §16.1, §16.2\n* - 6.2\n  - [Density Matrix](6-2-density-matrix)\n  - §16.3",
    "* - 6.1\n  - [Density Matrix](6-1-density-matrix)\n  - §16.3\n* - 6.2\n  - [Entanglement](6-2-entanglement)\n  - §16.1, §16.2"
)

with open(ch6idx_path, 'w') as f:
    f.write(ch6idx)
print("  ch6/index.md updated")

print("\n=== Done! ===")
print("Old 6.1 (Entanglement) → New 6.2")
print("Old 6.2 (Density Matrix) → New 6.1")
