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
