# Contributing to BHIL-HELM

## The one rule

`data/canonical/` is the source of truth. Everything under `tokens/`, `docs/catalog/`, `docs/reference/`, and `docs/prompts/` is generated. Edit canonical, run the builders, commit both.

```
python3 tools/validate.py
python3 tools/build_tokens.py
python3 tools/build_docs.py
python3 tools/sync_prompts.py
python3 tools/check_drift.py
python3 tools/em_dash_sweep.py
python3 -m pytest -q tests/
mkdocs build --strict
```

## Count laws

Fifteen languages. Twelve tropes. Five evidence tiers in fixed order. Eleven matching rules. Fourteen components. Changing any of these is a framework decision: open a Language proposal issue, update the schema `const`, the validator, and the tests deliberately, in one PR.

## IP cleanliness

No franchise name, logo, wordmark, glyph system, licensed font, or fan-recreation font enters any shipped file. Lineage references live only in `data/canonical/lineage_register.json` and its derived page. The test suite greps for property names and fails the build.

## Prose

No em dashes. Use commas, colons, or periods. The sweep runs in CI.

## Commits

Conventional commits scoped to the framework: `feat(helm): ...`, `fix(helm): ...`, `docs(helm): ...`, `chore(helm): ...`.

## Licensing

Code, schemas, and tokens are MIT. Prose content (prompts, docs) is CC BY 4.0. By contributing you agree your contribution is licensed the same way.
