# SP-01: Data & Input Deconstruction

*Turn whatever the client hands over into a Data Register that tells the builder what can honestly be shown.*

## Goal

Profile every field before a single pixel is styled. Half of failed sci-fi dashboards are styled around data that could never support the drama.

## Inputs

| Input | Form |
|---|---|
| `[Data Sources]` | CSV, JSON, XLSX, database extract, API sample, or narrative description |
| `[Client / Engagement]` | Name and REF code for the register header |
| Evidence policy | `data/canonical/evidence_tiers.json` |

## Procedure

1. Load every source. Record filename, row count, column count, export date if present, and whether the source is a system of record.
2. Profile every field: type, cardinality, null rate, range, units, update frequency, sample values.
3. Identify candidate KPIs, dimensions (time, geography, segment, entity), and context fields.
4. Detect hierarchy: parent/child keys, roll-ups, many-to-one joins.
5. Flag duplicates, mixed units, outliers beyond three standard deviations, inconsistent labels, and dates in more than one format.
6. Classify each field's evidence: system-of-record extract = VERIFIED; two independent extracts agreeing = CORROBORATED; single undated export = UNCORROBORATED; derived or estimated = INFERENCE; targets, goals, or client-stated benchmarks = STATED.
7. Determine the data shape: time-series / categorical comparison / hierarchy / geospatial / flow / status-grid / telemetry / text-heavy / relationship-graph / mixed. This is the key that SP-3 matches against.
8. If the input is narrative only, build a synthetic dataset, mark every row SYNTHETIC, and state each assumption as a numbered line.
9. Rank three candidate headline metrics by decision relevance, with one sentence each on why.

## Output contract

- **Data Register** table: Field | Type | Cardinality | Null rate | Units | Source | Quality | Role (KPI / dimension / context) | Evidence class
- **Data Shape Summary**: one primary shape, secondary shapes if mixed, and the rationale
- **Quality Flags**: numbered list with severity (blocks / degrades / cosmetic)
- **Candidate Headlines**: three metrics, ranked
- **Synthetic Declaration** (if applicable): assumptions list and the SYNTHETIC row count
- `data/register.json` written to the engagement directory in the schema at `data/schemas/register.schema.json`

## Gates

- No field leaves SP-1 without an evidence class.
- Any field with a null rate above 20 percent is flagged; it cannot be a headline metric without an SP-2 override.
- STATED fields cannot be headline metrics until reconciled or labeled on screen.

## Claude Code handoff

Subagent: `helm-profiler` (see `.claude/agents/helm-profiler.md`). Command: `/helm profile data/source.csv`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
