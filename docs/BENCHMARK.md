# Product benchmark — 2026-11-27

Documentation-based comparison, not a hands-on performance comparison.

| Product | Reference | Relevant feature |
|---|---|---|
| Gemini Notebook (NotebookLM) | https://support.google.com/gemininotebook/answer/16179559 | Select sources, trace citations, save notes |
| RAGFlow | https://ragflow.io/docs | Document parsing and retrieval validation |
| Dify | https://github.com/langgenius/dify-docs/blob/main/en/cloud/use-dify/nodes/knowledge-retrieval.mdx | Source metadata filtering |
| AnythingLLM | https://docs.anythingllm.com/chatting-with-documents/introduction | Document organization |
| Open WebUI | https://docs.openwebui.com/features/chat-conversations/rag/ | Hybrid retrieval and reranking |
| Kotaemon | https://cinnamon.github.io/kotaemon/usage/ | Source selection and relevance ranking |
| Onyx | https://docs.onyx.app/overview/core_features/connectors | Organizational knowledge connectors |

Implemented in v0.1.3: selection of document sources, result-depth controls, BM25 relevance labels, local TXT evidence export and Russian localization. Independent implementation; no competitor source code copied. Next: semantic embeddings, hybrid retrieval, retrieval evaluation, secure workspace isolation and connectors. No claim of outperforming these products.

## Current MVP update
NOESIS now has live hosted lexical RAG with Groq, document-only and separate general answers, multilingual UI, temporary session isolation, and a standalone Pages fallback. Competitor references are documentation-based, not controlled head-to-head benchmarks. Semantic retrieval, durable workspaces, richer parsing, connectors and conversation history remain gaps; no parity or superiority claim.
