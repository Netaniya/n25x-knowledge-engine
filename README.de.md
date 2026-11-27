![N25X](branding/n25x-logo.webp)

# N25X NOESIS — v0.2.0

Mehrsprachiges KI-Recherchesystem für Dokumente · funktionsfähiger Portfolio-MVP

Projektinitiatorin und Verantwortliche: Natalie Ragulina (Netaniya). KI-gestützte Entwicklung; eigene Produktentscheidungen, Mitwirkung am Deployment und manuelle Abnahme sind im Arbeitsjournal dokumentiert.

[Portfolio-Demo (GitHub Pages)](https://netaniya.github.io/n25x-knowledge-engine/) · [KI-Anwendung (Render)](https://n25x-noesis.onrender.com/) · [English](README.md)

## Funktionen
- Optionale semantische KI-Relevanzsuche über Groq (bis zu 24 ausgewählte Abschnitte, ausdrückliche Einwilligung), BM25-Rückfall und temporärer Rechercheverlauf (20 Anfragen, kein automatischer Gesprächskontext).
- Deutsch beim ersten Besuch, Englisch und Russisch auswählbar; drei Farbschemata, responsive Oberfläche.
- Öffentliche Demo: TXT/Markdown, temporäre getrennte Sitzungen, BM25-Suche, Dokumentauswahl, anklickbare Quellen, TXT-Export.
- Reale KI-Antworten mit GPT-OSS 20B über Groq nach Einwilligung. Dokumentenmodus und getrenntes allgemeines KI-Wissen.
- Browser-Demo auf GitHub Pages mit echter lokaler Textsuche ohne Server oder API-Schlüssel; keine KI-Generierung, Datenverlust beim Neuladen.
- Lokale Version zusätzlich mit textbasierten PDFs, SQLite und optionalen Embedding-Adaptern.

## Technik und Start
Python, FastAPI, SQLite, JavaScript, BM25, Groq API, Docker, GitHub Actions, Playwright, Render und GitHub Pages. Lokale Installation, Architektur und Konfiguration siehe [README](README.md), [ADR](docs/adr/0001-hybrid-retrieval.md) und [Deployment](docs/PUBLIC_AI.md).

## Qualität und Grenzen
[CI 46002577620](https://github.com/Netaniya/n25x-knowledge-engine/actions/runs/46002577620): Python/API, optionales Qdrant, Docker und Chromium erfolgreich. Reale KI-Antworten in Deutsch, Englisch und Russisch in einzelnen Beispielszenarien überprüft. [Abnahme](docs/ACCEPTANCE.md), [Arbeitsjournal](docs/WORK_LOG.md), [Vergleich auf Dokumentationsbasis](docs/BENCHMARK.md).

Kostenloses Hosting kann bei Inaktivität pausieren. Öffentliche Uploads: nur Testdaten, TXT/Markdown bis 1 MB, temporär. Begrenzte KI-Aufrufe (3/min, 30/24h global, 6/Sitzung/24h; Zähler können zurückgesetzt werden). Keine vertraulichen Daten. Keine produktionsreife Authentifizierung, dauerhafte Cloud-Speicherung, OCR oder dauerhafter Gesprächskontext. Öffentliche Suche mit BM25 und optionaler KI-Relevanzsuche; keine validierte dauerhafte Vektorindizierung. Quellen-IDs garantieren keine inhaltliche Richtigkeit.

© 2026 Natalie Ragulina (Netaniya). Alle Rechte vorbehalten für projekteigene Inhalte. Lizenzen von Drittkomponenten bleiben unberührt.
