<!-- DERIVED copy of prompts/sp-03-style-language-selector.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-03: Style Language Selector

*Choose the design language whose native strengths match the data shape and reader, and make the trade-offs explicit.*

## Goal

Match, do not pick. The SP-1 data shape and the SP-2 Decision Map resolve to a first-fit language and one alternate through the matching table. Then pay the narrative tax knowingly.

## Inputs

| Input | Form |
|---|---|
| SP-1 data shape | One primary shape |
| SP-2 Decision Map | Primary reader and setting |
| `[Style Intent]` | Catalog language, mood, or "recommend" |
| `[Constraints]` | Mandatory brand colors, motion tolerance |
| Catalog | `data/canonical/catalog.json` |
| Matching table | `data/canonical/matching.json` |
| Trope register | `data/canonical/tropes.json` |

## Procedure

1. If `[Style Intent]` names a language, validate it against the data shape and log any mismatch as INFERENCE. If it names a mood, map the mood to the nearest data-shape row. If "recommend", apply the matching table directly.
2. Propose the first-fit language and one alternate with rationale for each, tagged INFERENCE.
3. Produce the Lineage Card: palette relationships, type stack, hierarchy device, motion grammar, sound cue, native strength, native weakness. Type is specified as a category; shipped faces are open-license matches.
4. Run the Narrative Tax Register: list every trope the language carries and set each to keep / dial back / remove. Any departure from the HELM default needs a one-line rationale.
5. Map mandatory brand colors into the accent role. Compute contrast against the language's panel token and note the implications for SP-8.
6. Confirm no franchise-identifying element survives into the build: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a screen. List anything withheld for Appendix B.
7. If blending two languages, take palette and type from one and hierarchy device from the other. Never motion from both. Record the rationale.

## Output contract

- **Selected language** plus alternate, each with rationale (INFERENCE)
- **Lineage Card** (nine fields)
- **Narrative Tax Register**: Trope | Usability cost | Narrative benefit | HELM setting | Rationale if not default
- **Brand-color mapping note** with computed contrast ratios
- **IP-cleanliness confirmation** and the Appendix B withheld list
- **Blend rationale** if applicable

## Gates

- One language per screen unless the blend rationale is documented.
- The Sonar-Surveillance language may be used for system and network state only, never for tracking individuals.
- Glow, if the language uses it, is a single box-shadow token and never applied to text.

## Claude Code handoff

Subagent: `helm-stylist` (see `.claude/agents/helm-stylist.md`). Command: `/helm style recommend`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
