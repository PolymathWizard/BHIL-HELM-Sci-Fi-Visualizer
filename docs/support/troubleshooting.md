# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `validate.py` reports a contrast failure | A canonical token pair fell below floor | Adjust the token in `catalog.json` or log an exception in `data/canonical/contrast_exceptions.json` with approver and date |
| `check_drift.py` fails | A derived file was hand edited, or canonical changed without a rebuild | Run `build_tokens.py` and `build_docs.py`, commit the result |
| `em_dash_sweep.py` fails | An em dash entered prose | Replace with a comma, colon, or period |
| Dashboard shows "Chart library unavailable" | cdnjs unreachable | The inline fallback is rendering; connectivity is the fix, not the artifact |
| Support metric hover text does not appear | Reduced-motion or keyboard-only session | Hover text also renders on focus; tab to the metric |
| Boot screen never clears | JavaScript blocked | Boot is skippable and disappears under reduced motion; check console |
| `/restyle` refused a name | The name is a protected property | Use a catalog slug; the command names the nearest one |
| `/add-panel` stopped with a demotion proposal | Zone density budget reached | Approve the demotion or pick another zone |
| `mkdocs build --strict` fails on a link | A page moved | Fix the relative link; strict mode is the gate |
| Test `test_ip_cleanliness` fails | A property name entered a shipped file | Remove it; lineage references belong only in `lineage_register.json` and `docs/reference/lineage-register.md` |
