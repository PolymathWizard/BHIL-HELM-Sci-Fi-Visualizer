---
description: Insert a component bound to a field into a named zone, respecting the density budget
argument-hint: <zone> <field> [component]
---
Parse `$ARGUMENTS` as zone, field, and optional component name from `data/canonical/components.json`. Confirm the field exists in `register.json` with an evidence class. Check the zone's density budget in `zones.md`; if inserting exceeds it, propose which existing object to demote and stop for confirmation. Otherwise insert the component at the next priority, bind it with `data-field` and `data-evidence`, render the evidence label if the tier requires it, and re-run fidelity on the new value via helm-qa. Ambient components go to Stream only and carry `data-decorative="true"`.
