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

## 2026-11-27 — Chat-oriented workspace and regression coverage
- Applied the previously owner-approved chat-oriented layout with a collapsible document library, visible N25X logo, NOESIS product title, and a question composer below the evidence area. Existing retrieval endpoints and controls preserved. Multi-turn chat history is not implemented yet.
- Prior logo-bearing branch commit 7130bd848e36ae3cb15d25c2fb6db4175c0d6e28 passed GitHub Actions run 45988132952, including two pytest stages, Docker and Chromium smoke. The main-branch run 45988124488 failed at Chromium installation, not at pytest or Docker.
- Added browser acceptance checks for logo decoding, toggling the document library, disabled unconfigured providers, manual TXT upload, individual selection, select-all, source scoping, and API documentation navigation. Execution of the expanded suite is pending at commit time. This implementation and test authoring are AI-assisted; the owner independently supplies the next test scenario and acceptance result.

## 2026-11-27 — Owner mobile UX feedback
- Owner inspected a static mobile preview and rejected its narrow presentation and lack of interaction; requested a real full-width, interactive mobile workspace. A static image is not an accepted functional demo.
- AI-assisted change: default collapsed library on narrow screens, viewport-width workspace with 8px gutters, compact settings grid, larger touch targets and 16px question input. The browser suite now verifies initial mobile state and width. Public deployment is still unavailable.
- Prior expanded CI run 45990041237 failed at the disabled local-provider assertion; Python and Docker passed. Changed provider controls to start disabled until health confirms configuration and changed the test to check the reflected disabled attribute. New CI result pending.

## 2026-11-27 — Owner decision: answer scope C
- Natalie Ragulina (Netaniya) selected option C: switch between document-only answers and document results plus separate general AI knowledge. This is an explicit owner product and behavior decision.
- AI-assisted implementation: document-only default, separate answer scope and per-request consent for additional model call, question-only general request, separate unverified output and export, unavailable-provider handling. Existing grounded generation remains independently selectable. General knowledge is not presented as document evidence; no live model has been used to validate output quality.
- Mobile UX commit e0f88f06c6b172bc562e9858d8bddea819ec1bfe passed GitHub Actions run 45990594548. New mode tests added; execution pending. Owner's next task is to specify independent positive and negative acceptance examples.

## 2026-11-27 — Public portfolio demo preparation
- Owner requested a real interactive employer-facing URL before further feature work and authorized free Render hosting.
- AI-assisted demo mode separates browser sessions using signed random HttpOnly/Secure/SameSite cookies, filters document read/search/delete by owner, caps uploads and library capacity, expires demo documents after 24 hours on subsequent API traffic, and disables model calls regardless of server credentials. Public uploads restricted to test TXT/Markdown, 1 MB; local mode retains text-PDF support. No confidential data should be uploaded. This is not a production multi-user authentication system.
- Added cross-session regression and public-demo restrictions test. Deployment pending successful checks and workspace selection.

## 2026-11-27 — Owner live mobile acceptance findings
- Owner opened the deployed Render application and submitted 'Как загрузить документы' and 'Как пользоваться'. Both produced no-match results. Owner identified missing onboarding and expected operational guidance. This is direct human functional feedback, not an AI-authored finding.
- AI-assisted UI changes: visible three-language quick guide, one-click sample upload and real BM25 search, library shortcut, explicit empty-selection guidance and accurate public demo disclosure. Recognized common help questions display a labelled static guide, not simulated LLM output. No model or hosting plan changes.
- Added browser assertions for Russian help, library shortcut and sample search. Deployment is pending a passing run and separate authorization.

## 2026-11-27 — Owner requests actual AI integration
- Owner identified unavailable combined mode and inability to answer a general purpose question in the live demo. Requested AI integration work be handled by assistant.
- Prepared opt-in Groq GPT-OSS 20B public generation, preserving signed-session isolation and independent consent for general questions and grounded generation. Embedding providers remain disabled in public mode. Limits: 3 model calls/minute globally, 30/24h globally, 6/24h per browser session, 768 completion tokens per call. Counters are temporary SQLite and may reset on free-host storage loss. Provider free-tier limits remain independent.
- Mocked consent, endpoint restriction, no document transmission for general answers, budget and fallback tests added. No account, credential or real inference verified yet; existing live version remains unchanged pending CI and secret configuration.

## 2026-11-27 — Owner live RAG acceptance
- Natalie Ragulina (Netaniya) configured the replacement API secret directly in Render, then manually tested the public mobile application. Screenshots provided in conversation show a general-model answer to the project-purpose question, one-click Russian demo retrieval, and grounded generation with the question 'В какие дни работает служба поддержки?' in documents-only mode with AI generation enabled.
- Observed grounded answer: 'Служба поддержки работает с понедельника по пятницу, с 09:00 до 17:00. [S1]'. The displayed source n25x-demo-ru.txt, fragment 1, supports this answer. This is an owner-executed positive acceptance scenario, not a comprehensive RAG quality evaluation.
- Live deployment dep-dc4ngj7f3r2c73c2dmmg, application commit 1b26a907dc93b0fa61c1acf4d7476d7e24283ee0; previous automated CI run 45994925884 succeeded. Negative evidence, contradictory sources, arbitrary user upload/export on live hosting, multilingual paraphrase quality and semantic retrieval remain to be evaluated. Public demo uses BM25, not live semantic embeddings. No measured percentage of human authorship is asserted.
