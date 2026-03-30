# /project:build — Build the Jupyter Book

Build the lecture notes and optionally preview the output.

## Usage

```
/project:build [--preview]
```

## Instructions

1. **Pre-build validation:**
   - Run `/project:validate` to catch corruption before building
   - If critical issues found, report them and ask whether to proceed

2. **Clear stale build cache:**
   ```bash
   cd /path/to/PHYS130B
   rm -rf notes_src/_build
   ```

3. **Run the build:**
   ```bash
   ./build.sh
   ```
   This script:
   - Clears `_build/`
   - Runs `jupyter-book build notes_src/`
   - Syncs output to `notes/`
   - Patches `_static` → `static` and `_images` → `images` for GitHub Pages

4. **Check build output** for errors or warnings:
   - MyST parse errors (missing blank lines, bad admonitions)
   - Missing cross-references
   - LaTeX rendering issues

5. **If `--preview`**, start a local server:
   ```bash
   python -m http.server 4000 -d notes &
   ```
   Report the URL: `http://localhost:4000`

6. **Report build status:** success/failure with any warnings.
