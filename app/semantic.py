"""Pluggable embeddings and rank fusion; transient vectors only."""
import math
import os
from urllib.parse import urlparse
import httpx

MAX_SEMANTIC_CHUNKS = 128

def configured(provider):
    if provider == "local":
        return bool(os.getenv("LOCAL_EMBED_MODEL"))
    if provider == "cloud":
        return bool(os.getenv("CLOUD_EMBED_MODEL") and os.getenv("CLOUD_EMBED_API_KEY"))
    return False

def normalize(vector):
    if not isinstance(vector, list) or not 1 <= len(vector) <= 8192:
        raise ValueError("Invalid embedding size")
    if any(not isinstance(x, (int,float)) or isinstance(x,bool) or not math.isfinite(x) for x in vector):
        raise ValueError("Invalid embedding values")
    length=math.hypot(*vector)
    if not length or not math.isfinite(length):
        raise ValueError("Invalid embedding norm")
    return [x/length for x in vector]

async def embed(provider, texts):
    if not configured(provider):
        raise ValueError("Embedding provider is not configured")
    if provider == "local":
        base=os.getenv("LOCAL_EMBED_BASE_URL","http://127.0.0.1:11434/v1")
        url=urlparse(base)
        if url.scheme not in ("http","https") or url.hostname not in ("localhost","127.0.0.1","::1","host.docker.internal") or url.username or url.password:
            raise ValueError("Local endpoint must be loopback or host.docker.internal")
        model=os.environ["LOCAL_EMBED_MODEL"]
        headers={}
    else:
        base=os.getenv("CLOUD_EMBED_BASE_URL","https://api.openai.com/v1")
        url=urlparse(base)
        if url.scheme!="https" or not url.hostname or url.username or url.password:
            raise ValueError("Cloud endpoint must use HTTPS")
        model=os.environ["CLOUD_EMBED_MODEL"]
        headers={"Authorization":"Bearer "+os.environ["CLOUD_EMBED_API_KEY"]}
    vectors=[]
    async with httpx.AsyncClient(timeout=30, follow_redirects=False, trust_env=False) as client:
        for start in range(0,len(texts),32):
            batch=texts[start:start+32]
            response=await client.post(base.rstrip("/")+"/embeddings",headers=headers,json={"model":model,"input":batch})
            response.raise_for_status()
            data=sorted(response.json()["data"],key=lambda x:x["index"])
            if [x["index"] for x in data]!=list(range(len(batch))):
                raise ValueError("Embedding response indices mismatch")
            vectors.extend(normalize(x["embedding"]) for x in data)
    if len(vectors)!=len(texts) or len({len(v) for v in vectors})!=1:
        raise ValueError("Embedding dimensions mismatch")
    return vectors

def dense_rank(query, vectors, limit):
    """Qdrant embedded mode when installed; exact cosine otherwise."""
    try:
        from qdrant_client import QdrantClient, models
    except ImportError:
        scores=[(i,sum(a*b for a,b in zip(query,v))) for i,v in enumerate(vectors)]
        return sorted(scores,key=lambda item:(-item[1],item[0]))[:limit],"exact_cosine"
    client=QdrantClient(":memory:")
    try:
        client.create_collection("scoped",vectors_config=models.VectorParams(size=len(query),distance=models.Distance.COSINE))
        client.upsert("scoped",points=[models.PointStruct(id=i,vector=v) for i,v in enumerate(vectors)])
        hits=client.query_points("scoped",query=query,limit=limit).points
        return [(int(h.id),float(h.score)) for h in hits],"qdrant_local"
    finally:
        client.close()

def fuse(rows, lexical, dense, k):
    # RRF combines ranks, not incomparable raw scores. Dense cutoff is a
    # provisional heuristic, not a calibrated confidence threshold.
    scores={}
    for rank,h in enumerate(lexical,1):
        scores[h["chunk_id"]]=1/(60+rank)
    for rank,(index,similarity) in enumerate(dense,1):
        if similarity<=0.2:
            continue
        ident=rows[index]["chunk_id"]
        scores[ident]=scores.get(ident,0)+1/(60+rank)
    indexed={r["chunk_id"]:dict(r) for r in rows}
    ranked=sorted(scores,key=lambda ident:(-scores[ident],ident))[:k]
    return [dict(indexed[ident],score=round(scores[ident],6),score_type="rrf",citation=f"S{i}") for i,ident in enumerate(ranked,1)]

async def hybrid(rows, question, lexical, k, provider):
    if len(rows)>MAX_SEMANTIC_CHUNKS:
        raise ValueError("Selected scope exceeds semantic chunk limit")
    if not rows:
        return [],"none"
    vectors=await embed(provider,[question]+[r["text"] for r in rows])
    dense,engine=dense_rank(vectors[0],vectors[1:],min(len(rows),max(20,k*3)))
    return fuse(rows,lexical,dense,k),engine
