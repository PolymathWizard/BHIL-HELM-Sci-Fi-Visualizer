#!/usr/bin/env python3
"""Validate an SP-1 register.json against data/schemas/register.schema.json. Stdlib only.
usage: python3 tools/validate_register.py engagements/<REF>/register.json"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate  # noqa: E402

if len(sys.argv) < 2:
    print("usage: validate_register.py <register.json>")
    sys.exit(2)
schema = json.loads((validate.SCHEMAS / "register.schema.json").read_text())
inst = json.loads(Path(sys.argv[1]).read_text())
validate.check(inst, schema, "register")
# framework rules beyond schema
for f in inst.get("fields", []):
    if f.get("role") == "kpi" and f.get("null_rate", 0) > 0.2:
        validate.err(f"register.fields[{f['name']}]: kpi with null_rate {f['null_rate']} > 0.20 needs an SP-2 override")
    if f.get("role") == "kpi" and f.get("evidence") == "STATED":
        validate.err(f"register.fields[{f['name']}]: STATED kpi must render its label on screen (note in zones.md)")
if inst.get("synthetic") and not inst.get("synthetic_assumptions"):
    validate.err("register: synthetic=true requires synthetic_assumptions")
if validate.errors:
    validate.report()
else:
    print(f"register validate: PASS ({len(inst['fields'])} fields, shape {inst['data_shape']}, synthetic={inst['synthetic']})")
sys.exit(1 if validate.errors else 0)
