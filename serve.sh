#!/usr/bin/env bash
# Build PHYS2C notes and serve Jekyll site locally.
# Run from repo root: ./serve.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 1. Build Jupyter Book (updates teaching/PHYS2C/notes/)
if [ -f "teaching/PHYS2C/build.sh" ]; then
  echo "Building PHYS2C notes..."
  ./teaching/PHYS2C/build.sh
fi

# 2. Serve Jekyll
echo "Starting Jekyll server..."
bundle exec jekyll serve "$@"
