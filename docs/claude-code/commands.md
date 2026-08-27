# Standing commands

Three commands the client's Claude Code can run against any HELM-built dashboard, plus the framework-level commands available in this repository.

## Client commands

### rebind

```
/rebind data/q3.json
```

Replace the bound data file. Preserve every zone, component, token, and binding. Re-run SP-1 at summary depth on the new file. List every Data Register field that no longer exists and every new field that has no panel. Spot-check ten values. Do not restyle. Do not add panels.

### restyle

```
/restyle nasa-utilitarian
```

Swap the token set, keep all bindings, apply the new language's hierarchy device to zone frames, re-run the Narrative Tax Register for the new language, run contrast on every token pair, report any pair below floor. If the user names a protected property instead of a catalog slug, the command translates to the nearest language and says so.

### add-panel

```
/add-panel support carrier_capacity ring-gauge
```

Confirm the field exists in the register with an evidence class. Check the zone density budget. Insert at the next priority with `data-field` and `data-evidence`. Render the label if the tier requires it. If the budget is exceeded, propose which object to demote and stop for confirmation.

## Framework commands

| Command | Stage | Agent |
|---|---|---|
| `/helm brief` | Master, end to end | all four |
| `/helm profile <file>` | SP-1 | helm-profiler |
| `/helm intent` | SP-2 | helm-profiler |
| `/helm style <slug or recommend>` | SP-3 | helm-stylist |
| `/helm layout` | SP-4 | helm-stylist |
| `/helm components` | SP-5 | helm-builder |
| `/helm build --target html or jsx` | SP-6 | helm-builder |
| `/helm motion` | SP-7 | helm-builder |
| `/helm qa <artifact>` | SP-8 | helm-qa |
| `/snapshot <file> [prospect]` | SP-9 | helm-builder |
| `/gate` | SP-10 | helm-qa, fresh context |

## Prompts the client can paste without the skill

- **Rebind**: "Replace data/old.json with data/new.json, preserve every zone and component, re-run the fidelity spot-check, and list any Data Register field that no longer exists."
- **Restyle**: "Swap tokens/a.css for tokens/b.css, keep all bindings, re-run contrast on every token pair, and report any pair below 4.5:1."
- **Add panel**: "Insert a ring gauge bound to carrier_capacity into the Support zone at priority 3, respecting the density budget of 5 objects; if the budget is exceeded, propose which object to demote."
