# /project:fix-issue — Fix a Reported Issue

Address a specific issue from `feedback.md` or `progress.md`.

## Usage

```
/project:fix-issue <notebook-name> "<description>"
```

Example: `/project:fix-issue 1-3-3-heisenberg-picture "Math formulas are corrupted"`

## Instructions

1. **Read companion docs:**
   - `.claude/experience.md` — corruption patterns and fix recipes
   - `.claude/design.md` — correct conventions

2. **Read the notebook** using Python `json.load`.

3. **Diagnose the issue:**
   - If corruption: identify which pattern (char-by-char, missing `\n`, collapsed content)
   - If content issue: identify what violates design.md
   - If feedback: match professor's comment to specific cells/lines

4. **Fix using Python json.load/json.dump** (NEVER NotebookEdit or Edit on .ipynb):
   ```python
   import json
   with open(path) as f:
       nb = json.load(f)
   # Make targeted fixes to nb['cells'][i]['source']
   with open(path, 'w') as f:
       json.dump(nb, f, indent=1, ensure_ascii=False)
   ```

5. **Validate after fixing:**
   - Run `safe_edit.py validate` or the inline validation checks
   - Verify the fix resolved the issue
   - Check no new corruption was introduced

6. **Update tracking files:**
   - Mark the issue resolved in `progress.md`
   - If from `feedback.md`, add "**DONE**" annotation with date and summary
