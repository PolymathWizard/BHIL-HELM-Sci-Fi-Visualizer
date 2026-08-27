## What changed

## Canonical or derived?

- [ ] I edited `data/canonical/` and re-ran `build_tokens.py`, `build_docs.py`, `check_drift.py`
- [ ] I did not hand edit any file under `tokens/`, `docs/catalog/`, `docs/reference/`, or `docs/prompts/`

## Gates

- [ ] `python3 tools/validate.py` passes
- [ ] `python3 tools/em_dash_sweep.py` passes
- [ ] `python3 -m pytest -q tests/` passes
- [ ] `mkdocs build --strict` passes

## IP

- [ ] No franchise name, logo, glyph system, or licensed font entered a shipped file

## Commit scope

Conventional commit, scoped `helm:` (e.g. `feat(helm): add override note for retro-forward`).
