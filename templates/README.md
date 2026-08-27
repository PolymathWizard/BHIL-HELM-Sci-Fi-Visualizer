# Templates

Every client build inherits these. The builder (`helm-builder`) fills placeholders from the SP-1 through SP-5 outputs.

| File | Placeholders | Notes |
|---|---|---|
| `dashboard.template.html` | `CLIENT`, `REF`, `LANGUAGE_SLUG`, `LANGUAGE_ID`, `READER`, `SETTING`, `SECONDS`, `DECISION`, `DECISION_QUESTION`, `DATA_MODE`, `SYNTHETIC_BADGE`, `HELM_DATA_JSON`, `THRESHOLDS_JSON` | Zone structure is Prime, Support, Context, Status Rail, Stream. Builder adds Control and additional components per the zone map. `SYNTHETIC_BADGE` is the badge span when `DATA_MODE` is SYNTHETIC, otherwise empty. |
| `CLAUDE.md.template` | `CLIENT`, `READER`, `DECISION`, `SECONDS`, `SETTING`, `DATA_MODE`, `STATED_FIELDS`, `INFERENCE_FIELDS`, `LANGUAGE_SLUG`, `LANGUAGE_ID`, `COMPONENT_LIST`, `DENSITY_TABLE` | Shipped into the engagement root |
| `REGENERATE.md.template` | Same as above plus `ZONE_SPEC` | The exact rebuild prompt |
| `SKILL.md.template` | `CLIENT` | Shipped as `.claude/skills/helm-dashboard/SKILL.md` in the engagement |

The starter in `examples/helm-starter/` is this template filled in. Diff the two to see exactly what a build changes.

Fonts: token files name open-license category faces. The template does not hotlink any font service; it falls back to system faces. A client may self-host the named faces and add one `@font-face` block per role.
