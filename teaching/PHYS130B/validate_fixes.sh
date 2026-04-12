#!/bin/bash

files=(
  "notes_src/ch1_qubit/1-1-1-what-is-a-qubit.ipynb"
  "notes_src/ch1_qubit/1-1-2-state-and-representation.ipynb"
  "notes_src/ch1_qubit/1-1-3-hermitian-operators.ipynb"
  "notes_src/ch1_qubit/1-1-states-and-observables.ipynb"
  "notes_src/ch1_qubit/1-2-1-measurement-postulate.ipynb"
  "notes_src/ch1_qubit/1-2-2-uncertainty-and-incompatibility.ipynb"
  "notes_src/ch1_qubit/1-2-measurement.ipynb"
  "notes_src/ch2_identical-particles/2-1-3-second-quantization.ipynb"
  "notes_src/ch2_identical-particles/2-2-2-spin-representations.ipynb"
  "notes_src/ch2_identical-particles/2-3-1-exchange-statistics.ipynb"
)

echo "Validating all modified files..."
echo "================================"

passed=0
failed=0

for file in "${files[@]}"; do
  echo -n "Validating $file ... "
  if python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate "$file" > /dev/null 2>&1; then
    echo "✅ PASS"
    ((passed++))
  else
    echo "❌ FAIL"
    ((failed++))
  fi
done

echo "================================"
echo "Results: $passed passed, $failed failed"
