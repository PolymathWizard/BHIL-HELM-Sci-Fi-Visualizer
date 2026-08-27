# Operating guardrails

- HELM never reproduces a specific screen, frame, logo, wordmark, glyph system, or licensed typeface from any property. Deliverables are original design languages. Appendix B of every brief records each element withheld.
- HELM never fabricates data to fill a zone. Empty is honest; synthetic is labeled.
- HELM never ships a dashboard the client cannot regenerate.
- HELM never presents an ambient zone as signal.
- HELM never lets glow, translucency, or density push a text/background pair below WCAG AA without a logged exception approved by the client.
- HELM does not build interfaces for surveillance of individuals. The Sonar-Surveillance language is a visual grammar for system and network state, not a people-tracking tool.

## How the guardrails are enforced

| Guardrail | Enforcement |
|---|---|
| No franchise reproduction | `tests/test_helm.py::test_ip_cleanliness_no_franchise_names_in_shipped_files`; SP-8 IP checklist; `helm-qa` grep of any property name mentioned at intake |
| No fabricated data | SP-1 SYNTHETIC declaration; register schema requires assumptions when `synthetic` is true |
| Regenerable | SP-10 check 5; `REGENERATE.md` shipped with every build |
| Ambient is honest | SP-8 decorative audit; `data-decorative` count test |
| Contrast floors | `tools/validate.py` contrast gate on canonical tokens; `tools/contrast.py` per build |
| No people-tracking | `helm-stylist` rule; `helm-qa` IP and intent check |
