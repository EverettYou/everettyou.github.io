# Rule: Tooling and permissions (Cowork / Claude Code)

## Why Bash + Python I/O for writes

In **Cowork**, `Edit` and `Write` often trigger an “Always allow?” dialog **on every call**, which blocks unattended work. **`Bash`** with Python `open()` / `json.load` / `json.dump` avoids that pattern for normal file writes.

**Banned for agents (see `settings.local.json`):** `NotebookEdit` (corrupts ipynb), `Edit`, `Write`—use the patterns in `rules/notebook-editing.md` instead.

## Bash redirect trap

Shell redirects (`>`, `>>`) **to the mounted project folder** can trigger the same permission prompts. **Do not** rely on:

```bash
echo x > notes_src/foo.md
python script.py > out.txt
```

**Do** write from Python inside Bash:

```bash
python3 -c "open('path','w').write('content')"
```

## File deletion

Deletion may be sandbox-gated until approved. Prefer in-place edits. If deletion is required, follow your host’s approval flow (e.g. Cowork file-delete allowlist).

## Claude Code CLI (`settings.local.json`)

Outside Cowork, permissions may allow `Write`/`Edit`; **`NotebookEdit` should stay denied** for `.ipynb`. Project policy: use programmatic ipynb edits either way.

## Silent vs prompting tools (reference)

| Usually silent | Avoid for bulk writes |
|----------------|----------------------|
| `Read`, `Glob`, `Grep`, `Bash` (Python I/O) | `Edit`, `Write`, `NotebookEdit` |
| Validator scripts | Shell `>` into mount |
