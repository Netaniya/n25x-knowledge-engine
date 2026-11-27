# ADR 0001 — Hybrid retrieval / Hybride Suche
Date: 2026-11-27
Status: Accepted by project owner; implementation and validation in progress.

## Decision
Natalie Ragulina (Netaniya) explicitly chose the combined architecture: local and optional hosted embedding providers with a BM25 fallback. Keep German as default UI language; English and Russian remain optional. No national flags.

## Implementation choices
AI-assisted technical proposal: pluggable OpenAI-compatible embedding endpoints, explicit per-query provider selection, no automatic cloud fallback, reciprocal rank fusion (RRF) of lexical and vector results. Use Qdrant local in-memory mode when installed; exact cosine fallback otherwise. SQLite remains authoritative; vectors are transient, rebuilt per query for the scoped library. This avoids stale indexes and deletion synchronization for the MVP but is not scalable production indexing. Limit semantic requests to 128 selected chunks; larger scope falls back to BM25. No provider calls in default lexical mode. Cloud requires explicit consent and administrator configuration, and may incur charges. Generation is separately opt-in.

## Abnahme / Acceptance
- Verify lexical mode without network calls.
- Verify local and cloud provider adapters with mocks, no cloud call without consent, and fallback when provider fails.
- Verify selected documents only, vector dimension validation, rank fusion, multilingual paraphrase benchmark with real embeddings, and Qdrant integration.
- Real model, Qdrant, CI and browser acceptance must be reported separately.
- Persistent vector indexing, LangChain integration and deployment remain follow-up work.

References: https://github.com/qdrant/qdrant-client ; https://developers.openai.com/api/reference/resources/embeddings/methods/create
