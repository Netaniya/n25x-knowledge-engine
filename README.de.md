# N25X Knowledge Engine

[English](README.md) · Deutsch

**Version 0.2.0 — lokaler Prototyp für dokumentenbasierte Recherche**

Projektinitiatorin und Verantwortliche: Natalie Ragulina (Netaniya). Die Implementierung erfolgt KI-gestützt. Der öffentliche Prototyp ist von den privaten Studio-Projekten getrennt.

## Funktionen

- PDF (textbasiert), TXT und Markdown bis 5 MB, maximal 150 PDF-Seiten.
- Textabschnitte und Seitenreferenzen in SQLite; BM25-Suche mit Quellen.
- Deutsche (Standard), englische und russische Oberfläche, drei Farbschemata, gespeicherte Einstellungen.
- Fiktives Beispieldokument und direkt anklickbare Quellenverweise.
- Optionaler LLM-Endpunkt für generierte Antworten; ohne Schlüssel reine Textsuche.
- REST-API, OpenAPI, automatisierte Tests, Docker- und CI-Konfiguration.

## Start (Python 3.12 oder 3.13)

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Öffne http://127.0.0.1:8000, wähle "Beispiel laden" und starte die Recherche. Erwartet: Montag bis Freitag, 09:00–17:00 Uhr. API: http://127.0.0.1:8000/docs.

Docker: `docker compose up --build`. Die Konfiguration bindet an localhost. Die Docker-Ausführung und Remote-CI müssen noch überprüft werden.

## KI und Datenschutz

LLM_API_KEY und LLM_MODEL konfigurieren; optional LLM_BASE_URL. Nur wenn die KI-Checkbox aktiviert wird, gehen Frage und Textauszüge an den Anbieter. Kosten sind möglich. Keine vertraulichen Daten und keine API-Schlüssel im Repository speichern. Quellen-IDs allein beweisen keine inhaltliche Richtigkeit.

## Grenzen und nächste Schritte

Lokale Einzelbenutzer-Anwendung ohne Anmeldung, Mandantentrennung oder produktionsreife Sicherheitsmaßnahmen. Kein OCR, keine validierte semantische Suche und kein verifiziertes Cloud-Deployment. Nicht öffentlich als Upload-Dienst bereitstellen. Qdrant, LangChain, Kubernetes, Monitoring und Evaluierung sind geplant, nicht implementiert.

## Zusammenarbeit und Qualität

[Arbeitsjournal](docs/WORK_LOG.md) · [Abnahmetests / Acceptance](docs/ACCEPTANCE.md) · [Architektur (EN)](README.md#architecture). Die erste manuelle Prüfung durch die Projektverantwortliche wurde berichtet; Details und erneute Abnahme folgen. Es wurde noch keine Open-Source-Lizenz gewählt.

## Gezielte Recherche und Export

Wähle die gewünschten Dokumente und maximal 1, 2, 4, 6 oder 8 Treffer. Die API filtert vor dem Ranking und vor der optionalen KI-Generierung. Die BM25-Werte sind Relevanzwerte, keine Vertrauenswahrscheinlichkeiten. Der lokale TXT-Export enthält Frage, Antwortmodus, Antwort und Quellen. Exportierte Auszüge können vertrauliche Daten enthalten. Die Dokumentauswahl gilt für die nächste Anfrage; ein Sprachwechsel übersetzt keine Dokumentinhalte.

## Optionale hybride Suche (Entwicklung v0.2.0)

BM25 ist Standard und benötigt kein Modell. Für lokale Embeddings: kompatiblen lokalen Dienst starten, LOCAL_EMBED_MODEL und optional LOCAL_EMBED_BASE_URL setzen (Standard http://127.0.0.1:11434/v1). Für Cloud-Embeddings: CLOUD_EMBED_MODEL, CLOUD_EMBED_API_KEY und optional CLOUD_EMBED_BASE_URL (HTTPS) konfigurieren. Nur nach ausdrücklicher Zustimmung pro Anfrage werden Frage und ausgewählte Textabschnitte übertragen. Kosten sind möglich. Kein automatischer Cloud-Fallback. Die Antwortgenerierung ist separat zu aktivieren.

`python -m pip install -r requirements-semantic.txt` aktiviert die lokale Qdrant-Suche im Arbeitsspeicher. Ohne Paket wird exakte Kosinusähnlichkeit verwendet. Vektoren werden je Anfrage neu erstellt, maximal 128 Abschnitte. RRF-Werte sind keine Wahrscheinlichkeiten. Tests mit realen Modellen, dauerhafte Vektorindizierung, LangChain und Deployment stehen noch aus. [Architekturentscheidung](docs/adr/0001-hybrid-retrieval.md).
