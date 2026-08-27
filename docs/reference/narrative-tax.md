<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# The Narrative Tax Register

Every science-fiction trope trades usability for storytelling. HELM makes each trade explicit and sets a default. Applied in SP-3, re-checked in SP-8. Count law: exactly 12 tropes.

| ID | Trope | Usability cost | Narrative benefit | HELM default | Rule |
|---|---|---|---|---|---|
| T01 | Dedicated console / room | Forces the reader to a fixed location | Signals hierarchy and secrecy | remove | Responsive by default |
| T02 | Transparent vertical screens | Background interference kills legibility | Shows the face through the screen | dial back | Translucency at or below 15 percent over dark only |
| T03 | Voice-first UI | Slower than direct manipulation; excludes some users | Lets people talk to the machine | dial back | Optional overlay; never the only path |
| T04 | Anthropomorphic UI | Wasteful, can be uncanny | Makes the system a character | remove | Remove for business dashboards |
| T05 | Hardware dependence | Fragile physical props | Actors need tangible things | remove | Not applicable to screen deliverables |
| T06 | Binary inputs everywhere | Loses analog control | Cheap to build | dial back | Keep sliders where ranges matter |
| T07 | Slow screen redraws | Text crawling at 48 baud | Suspenseful reveal | dial back | Boot sequence only, at most 1.2 s, skippable |
| T08 | Hidden thought-control | Nothing to look at | None for a dashboard | remove | Show results, not the act |
| T09 | Data density as decoration | Signal buried in noise | Reads as advanced in one second | dial back | Ambient zones only, marked decorative |
| T10 | Optical flares / glow | Contrast destruction | Spectacle | dial back | Single glow token, never on text |
| T11 | Nonsense reference numbers | Reader looks for meaning that is not there | Texture | remove | Every number is real or labeled synthetic |
| T12 | Enhance magic | Sets false expectations of the system | Drama | remove | Show actual drill-down paths |


A build may override a default only with a documented rationale in the SP-3 output and a matching QA line in SP-8.
