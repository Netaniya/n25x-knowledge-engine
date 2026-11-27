# Work log

## 2026-11-27 — Initial AI-assisted scaffold
- Project owner: Natalie Ragulina (Netaniya).
- Owner selected standalone public portfolio project and explicitly excluded private Studio code.
- AI-assisted implementation: initial FastAPI service, SQLite storage, BM25, browser UI and optional LLM configuration with fallback.
- Local archive tests: 12 passed; target repository and browser tests pending.

## 2026-11-27 — Theme selection
- Owner requested turquoise/blue palette and selectable themes. Added three CSS-variable palettes and local preference persistence.

## 2026-11-27 — GitHub repository
- Owner created the public repository Netaniya/n25x-knowledge-engine and initial README commit f16cd14e4050ec384b1fccbc0ab0871c427b8248.
- Owner requested code review, manual acceptance testing, and documentation of her contributions. These reviews and tests are pending, not recorded as completed.
- AI-assisted source transfer prepared; independent verification of the remote tree and CI is required.

## 2026-11-27 — Owner review and bilingual milestone
- Natalie Ragulina reported that she reviewed and tested v0.1.1 and found it broadly consistent with the agreed scope. Exact test cases, environment and evidence were not supplied; a second review is planned.
- Owner requested German and English UI/documentation and further quality improvements. AI-assisted implementation adds persistent DE/EN selection, example data, source links and accessibility improvements. No private project code reused.
- New acceptance scenarios are listed in docs/ACCEPTANCE.md; v0.1.2 is not marked accepted until independently verified.

- Local working-copy validation: 13 pytest tests passed; JavaScript syntax check passed. Browser navigation blocked by execution environment; browser smoke test added to CI, result pending. No acceptance score claimed.

## 2026-11-27 — Trilingual research controls (v0.1.3)
- Owner requested Russian as an optional third language, retaining German as the default, and comparison with leading document intelligence applications.
- AI-assisted implementation adds source selection, server-side source scoping, configurable result depth, visible BM25 relevance and local evidence export. Benchmark references: docs/BENCHMARK.md.
- Local backend test run: 13 passed, 2 UI-dependent cases deselected. Git blob hashes for backend and tests match the published files. End-to-end acceptance and cloud deployment remain pending.

## 2026-11-27 — Owner review and design policy
- Project owner continues to report reviewing, testing, studying the implementation, researching improvements and directing changes. Specific additional test cases and results are not yet supplied; no additional acceptance tests are marked passed on that basis.
- Owner specified a neutral language selector without national flags. Source inspection confirmed that the current selector contains only Deutsch, English and Русский, with no regional-indicator flag emoji or flag-icon references in the HTML. No application code change was needed.
- Contribution tracking distinguishes human product direction, repository setup, review, manual testing and acceptance from AI-assisted implementation, documentation and automated checks. No measured percentage of authorship or effort is established; record concrete contributions and evidence rather than inventing quantitative metrics.

## 2026-11-27 — Owner code review, v0.1.3
- Owner reports reviewing app/main.py, finding no errors during her inspection and considering the implementation consistent with agreed requirements. Reviewed file at recording time: blob 236881ff42187a8c665f80a04824168e679c3a0e. This is a self-reported manual code review, not a proof of absence of defects or a completed functional acceptance test.
- Next design decision: choose the semantic retrieval architecture, including local versus hosted embeddings, multilingual requirements, and a measurable comparison against the existing BM25 baseline.

## 2026-11-27 — Architecture decision and hybrid retrieval
- Owner explicitly chose the combined local/cloud architecture. See docs/adr/0001-hybrid-retrieval.md. AI-assisted implementation adds provider adapters, source-scoped embeddings, rank fusion, local Qdrant option, fallback and consent controls. Code is in feature/hybrid-retrieval pending review. No live provider requests, model purchases or credentials added. Tests authored; execution and real-model quality still need confirmation.

## 2026-11-27 — Owner inspection of hybrid development branch
- Owner reports opening and reviewing the proposed implementation. No specific defect findings or executed test cases reported at this stage. Next owner task: author independent multilingual retrieval test cases with expected evidence and negative controls, then review actual results before acceptance.

## 2026-11-27 — Product naming decision
- Natalie Ragulina (Netaniya), project owner, selected N25X NOESIS from seven proposed names. This is her explicit product and creative decision. The name refers to understanding and intellectual analysis.
- Naming selection is recorded; trademark/domain clearance and actual rebranding are not yet completed. Existing repository name remains unchanged.

## 2026-11-27 — Owner interface decision
- Natalie Ragulina (Netaniya) explicitly selected option B, the intelligent chat layout: a central conversational workspace with document library accessible through a sidebar, rather than a three-column research studio or dashboard. This is her product/UX decision.
- Preserve source traceability, German default language with English and Russian options, and theme selection. Detailed layout implementation and functional acceptance remain pending.

- Owner reviewed and approved the illustrated chat-first UI concept. This is approval of the design direction, not acceptance of a working frontend. Next: select visual identity and implement the approved interface, then validate it in browser.

## 2026-11-27 — Master brand identity
- Project owner Natalie Ragulina (Netaniya) rejected earlier visual variants, specified a universal minimal N25X wordmark without extra symbols, chose the fifth monochrome concept as the starting point, requested blue tones and compact proportions, and explicitly approved the final blue design for all her GitHub projects. The compact web image is in branding/n25x-logo.webp. Full-resolution original saved separately. Trademark/design similarity clearance is pending.
