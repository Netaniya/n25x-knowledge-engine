# Public AI deployment (N25X NOESIS)
The public demo is opt-in. Keep N25X_PUBLIC_DEMO=1.
Configure N25X_PUBLIC_AI=1, LLM_BASE_URL=https://api.groq.com/openai/v1, LLM_MODEL=openai/gpt-oss-20b, and LLM_API_KEY as a secret in Render only.
Use a separate Groq project/key on the free plan. Do not commit keys, paste them into chat, or put them in browser code. Verify the provider account remains free; do not enable billing.
Public mode uses BM25, optional consented LLM semantic relevance ranking of up to 24 selected chunks, and optional LLM generation. Semantic embeddings remain off. Ranking consumes one shared model call, generation another. Research history stays in the open browser page. Both model modes require explicit user action and disclose external data transfer. Test data only.
Application limits are 3 calls/minute, 30 calls/rolling 24 hours globally and 6 per browser session; 768 completion tokens per request. A combined answer with grounded generation may use two calls. These temporary database counters are not a billing guarantee and may reset on a free hosting restart or redeploy. Provider limits apply separately.
Verify CI before deployment. Confirm real inference with a non-sensitive question, no-document negative test, source-cited sample and consent. On failure, set N25X_PUBLIC_AI=0 and deploy; lexical search remains available.
