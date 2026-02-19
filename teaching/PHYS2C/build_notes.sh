#!/usr/bin/env bash
# Build Jupyter Book and sync HTML output to notes/
# Run from teaching/PHYS2C/: ./build_notes.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate venv if present (local or repo root; use Jupyter Book 1.x for _config.yml + _toc.yml)
if [ -d ".venv" ]; then
  . .venv/bin/activate
elif [ -d "../../.venv" ]; then
  . ../../.venv/bin/activate
fi

# Build Jupyter Book
cd notes_src
jupyter-book build .

# Sync _build/html/ to notes/
cd "$SCRIPT_DIR"
mkdir -p notes
if command -v rsync &> /dev/null; then
  rsync -av --delete notes_src/_build/html/ notes/
else
  rm -rf notes/*
  cp -r notes_src/_build/html/* notes/
fi

echo "Build complete. Output synced to teaching/PHYS2C/notes/"
