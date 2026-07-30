"""
Rate-limited Semantic Scholar Graph API client for the H-003 search loop.

Official API only (api.semanticscholar.org/graph/v1), unauthenticated tier.
Etiquette: >=3s between requests, identifying User-Agent with mailto,
sequential (no concurrency), exponential backoff (30s -> x2 -> 600s cap) on
429 / any error. Every call logged to s2_search_log.jsonl; ids deduped in
s2_seen_ids.json.

Two entry points:
  search(query)          -> paper relevance search
  citations(paper_id)    -> papers citing paper_id (paginated)
"""
import urllib.request, urllib.parse, urllib.error, time, json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(HERE, "s2_search_log.jsonl")
SEEN_PATH = os.path.join(HERE, "s2_seen_ids.json")
USER_AGENT = "wcc-h003-research-loop/1.0 (mailto:dr.renatotavares@gmail.com)"
BASE = "https://api.semanticscholar.org/graph/v1"

_last_call = 0.0
MIN_INTERVAL = 3.0


def _rate_limit():
    global _last_call
    dt = time.time() - _last_call
    if dt < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - dt)
    _last_call = time.time()


def load_seen():
    if os.path.exists(SEEN_PATH):
        with open(SEEN_PATH) as f:
            return set(json.load(f))
    return set()


def save_seen(seen):
    with open(SEEN_PATH, "w") as f:
        json.dump(sorted(seen), f)


def _get(path, params, kind, label, max_retries=5):
    url = BASE + path + "?" + urllib.parse.urlencode(params)
    backoff = 30
    for attempt in range(max_retries):
        _rate_limit()
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                body = resp.read().decode("utf-8")
            data = json.loads(body)
            with open(LOG_PATH, "a") as f:
                f.write(json.dumps(dict(
                    ts=time.strftime("%Y-%m-%dT%H:%M:%S"), source="semanticscholar",
                    kind=kind, label=label, params=params,
                    n=len(data.get("data", [])), total=data.get("total"),
                )) + "\n")
            return data
        except Exception as ex:
            print(f"  [retry {attempt+1}/{max_retries}] {label}: {ex} -- backoff {backoff}s",
                  file=sys.stderr, flush=True)
            time.sleep(min(backoff, 600))
            backoff = min(backoff * 2, 600)
    raise RuntimeError(f"S2 request failed after {max_retries} retries: {label}")


FIELDS = "paperId,externalIds,title,abstract,year,venue,authors,citationCount"


def search(query, limit=15, offset=0):
    d = _get("/paper/search", {"query": query, "limit": limit, "offset": offset,
                               "fields": FIELDS}, "search", query)
    return d.get("data", []) or []


def citations(paper_id, limit=100, offset=0):
    d = _get(f"/paper/{paper_id}/citations",
             {"limit": limit, "offset": offset,
              "fields": FIELDS.replace("paperId", "paperId")},
             "citations", f"{paper_id}@{offset}")
    return [c.get("citingPaper", {}) for c in d.get("data", []) or []]


def references(paper_id, limit=100, offset=0):
    d = _get(f"/paper/{paper_id}/references",
             {"limit": limit, "offset": offset, "fields": FIELDS},
             "references", f"{paper_id}@{offset}")
    return [c.get("citedPaper", {}) for c in d.get("data", []) or []]


def fmt(p, snippet=0):
    ex = p.get("externalIds") or {}
    ident = ex.get("ArXiv") and f"arXiv:{ex['ArXiv']}" or ex.get("DOI") or p.get("paperId", "?")
    au = ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:3])
    s = f"  {p.get('year')} [{ident}] {p.get('title')}  ({au}; {p.get('venue') or '-'}; cites={p.get('citationCount')})"
    if snippet and p.get("abstract"):
        s += "\n        " + " ".join(p["abstract"].split())[:snippet]
    return s


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "search":
        for p in search(sys.argv[2], limit=int(sys.argv[3]) if len(sys.argv) > 3 else 15):
            print(fmt(p, 300))
    elif mode == "citations":
        off = 0
        while True:
            batch = citations(sys.argv[2], offset=off)
            if not batch:
                break
            for p in batch:
                print(fmt(p))
            off += len(batch)
            if len(batch) < 100 or off >= int(sys.argv[3] if len(sys.argv) > 3 else 400):
                break
