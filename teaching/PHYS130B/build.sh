#!/usr/bin/env bash
# Build Jupyter Book and sync HTML output to notes/
# Run from teaching/PHYS2C/: ./build.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Clear Sphinx cache to force full rebuild (avoids stale _static e.g. custom.css)
rm -rf notes_src/_build

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

# Rename _* directories to non-underscore names for GitHub Pages compatibility
# (GitHub Pages/Jekyll excludes _* directories; rename avoids duplicating files)
for dir in _static _images _sources; do
  newdir="${dir#_}"
  if [ -d "notes/$dir" ]; then
    rm -rf "notes/$newdir"
    mv "notes/$dir" "notes/$newdir"
  fi
done
python3 -c "
import os, re

# Read site url and favicon from root _config.yml
config_path = '../../_config.yml'
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = f.read()
    url_match = re.search(r'^url:\\s*[\"\\']([^\"\\']+)[\"\\']', config, re.M)
    favicon_match = re.search(r'^favicon:\\s*(\\S+)', config, re.M)
else:
    url_match = favicon_match = None
site_url = url_match.group(1).strip() if url_match else 'https://everettyou.github.io'
favicon_path = favicon_match.group(1).strip() if favicon_match else 'assets/img/logos/avatar.svg'
favicon_url = f'{site_url.rstrip(\"/\")}/{favicon_path.lstrip(\"/\")}'
favicon_tag = f'<link rel=\"icon\" href=\"{favicon_url}\" type=\"image/svg+xml\"/>'

for root, _, files in os.walk('notes'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            new = re.sub(r'_static\b', 'static', content)
            new = re.sub(r'_sources\b', 'sources', new)
            new = re.sub(r'_images\b', 'images', new)
            # Replace or insert favicon to use site avatar (single source of truth)
            if re.search(r'<link\\s+rel=[\"\\'](?:shortcut\\s+)?icon[\"\\']', new):
                new = re.sub(
                    r'<link\\s+rel=[\"\\'](?:shortcut\\s+)?icon[\"\\']\\s+href=[\"\\'][^\"\\']*[\"\\'][^>]*/?>',
                    favicon_tag,
                    new,
                    count=1
                )
            elif '</head>' in new:
                new = new.replace('</head>', f'  {favicon_tag}\\n  </head>', 1)
            if new != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new)
"

echo "Build complete. Output synced to teaching/PHYS130B/notes/"
