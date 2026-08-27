---
description: Swap the data file behind a HELM dashboard, preserve every zone and component, re-run fidelity
argument-hint: <new-data-file>
---
Replace the bound data file with `$ARGUMENTS`. Preserve every zone, component, token, and binding. Re-run SP-1 at summary depth on the new file to refresh `register.json`. Then delegate to helm-qa for a fidelity spot-check. List every Data Register field that no longer exists in the new file and every new field that has no panel. Do not restyle. Do not add panels.
