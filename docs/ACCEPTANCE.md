# Acceptance / Abnahme

Run locally with Python as documented. Use only fictional sample data. Record version, browser, date, expected and actual results, and reviewer. Do not mark unexecuted tests as passed.

| Test | Expected / Erwartung | v0.1.2 result |
|---|---|---|
| DE/EN switch | All application labels update; document text remains unchanged / UI übersetzt, Dokumenttext unverändert | Pending |
| Persistence | Language and theme survive reload / Einstellungen bleiben erhalten | Pending |
| Demo | Load example, run search; support hours 09:00–17:00 / Beispiel und Recherche | Pending |
| Citations | Source link jumps to its passage / Quellenlink springt zur Textstelle | Pending |
| Delete | Document and indexed chunks removed / Dokument und Abschnitte gelöscht | Pending |
| No match | Explicit localized no-match message / lokalisierter Hinweis ohne Treffer | Pending |
| Upload rejection | Empty, invalid or oversized file rejected / ungültige Datei abgelehnt | Pending |
| Mobile | No horizontal overflow at 390px / kein horizontaler Überlauf | Pending |
| Keyboard | Focus visible, labels associated / sichtbarer Fokus | Pending |
| Generation | Mock validates source IDs; real model not yet verified / Mock, kein Live-Test | Pending |
| Container and CI | Build and smoke test pass / Build und Smoke-Test erfolgreich | Pending |

## Quality gates / Qualitätsziele

A 100/100 internal target requires evidenced acceptance, retrieval evaluation, security review, accessibility, reproducible container deployment, observability, and real cloud validation. This is not a certification. The current MVP does not meet all gates.

## v0.1.3 additions

| Test | Expected | Status |
|---|---|---|
| Fresh session | German default; EN/RU selectable | Pending browser test |
| Source scope | Excluded document never returned; empty selection returns no match | Backend test passed |
| Result depth | Maximum selected number of results | Backend test passed |
| Russian query | Matches Russian source text | Pending full suite |
| Evidence export | TXT contains original question and source excerpts | Pending browser test |
| Relevance | Score marked BM25, not confidence | Pending browser test |

## v0.2.0 hybrid acceptance (pending)

- Lexical mode never contacts embedding endpoint; missing consent returns HTTP 400.
- Local and consented cloud adapter: mock vector test, verify scoped sources and fallback.
- Run tests with and without Qdrant installed. Verify actual local/hosted models with multilingual paraphrases and irrelevant questions. Measure Recall@k and false positives before claims about quality.
- Review privacy controls: selected chunks are transmitted to the cloud only after consent. Confirm language and theme settings and offline fallback in browser.

## v0.2.0 portfolio MVP — 2026-11-27

| Check | Observed result | Evidence |
|---|---|---|
| Python/API, optional Qdrant, Docker, Chromium | Pass | [CI 46002577620](https://github.com/Netaniya/n25x-knowledge-engine/actions/runs/46002577620) |
| Responsive 390/1280 px, German initial default, RU/EN and attribution | Pass in CI | Same run |
| Live Russian positive and missing-evidence RAG | Pass for tested sample | Owner screenshots, work log |
| Live German/English support hours | Pass for tested sample | [Browser run](https://agent.tinyfish.ai/runs/63ef2c9c-3d04-4b43-96dc-6d45756a72b9) |
| Live Render TXT download | Pass (prior live run) | Same browser run |
| GitHub Pages default, attribution, languages, sample retrieval, source anchors, selection, library and AI link | Pass in observed browser scenario | [Browser run](https://agent.tinyfish.ai/runs/88b4aff3-9749-4daf-9442-4ffc335f2ab2) |
| Pages actual export download and exact 390/1280 px viewport tests | Not confirmed | Browser environment limitation |
| Real semantic embedding evaluation, security audit, arbitrary-document robustness | Not completed | Future work |

Deployed Render app commit 85c83967f539beb653d3d8ee55d2a207cb20027d; deploy dep-dc4nsiu1egvs73960i00 live. Pages branch commit 0a0d5ee508e2b64f90640780cac2f97e0ea8e21d. Historical pending entries above retained for provenance. MVP release acceptance is not production certification.

## Completion regression — 2026-11-27
[CI 46008069953](https://github.com/Netaniya/n25x-knowledge-engine/actions/runs/46008069953) passed Python/API with and without optional Qdrant, Docker, Chromium app smoke and standalone Pages smoke. Pages checkout tested at 390/1280 px; actual TXT download and content, custom test upload, source selection and removal verified. Mock semantic ranking with scope, consent and invalid-ID fallback, signed-cookie tampering and security headers passed. Live semantic provider acceptance and independent security audit remain separate. See [security scope](SECURITY.md).
