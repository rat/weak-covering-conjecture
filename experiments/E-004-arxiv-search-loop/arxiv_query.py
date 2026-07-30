"""
Rate-limited arXiv API client for the H-003 search loop.
Respects: >=3s between requests, User-Agent header, official API only,
sequential (no concurrency), start/max_results pagination (<=100/call),
exponential backoff on 429 (30s -> doubling -> 10min cap).
Logs every query to arxiv_search_log.jsonl (query, timestamp, count, ids).
"""
import urllib.request, urllib.parse, time, json, sys, os
import xml.etree.ElementTree as ET

LOG_PATH = os.path.join(os.path.dirname(__file__), "arxiv_search_log.jsonl")
SEEN_PATH = os.path.join(os.path.dirname(__file__), "arxiv_seen_ids.json")
USER_AGENT = "wcc-h003-research-loop/1.0 (mailto:dr.renatotavares@gmail.com)"
BASE_URL = "http://export.arxiv.org/api/query"

_last_call = 0.0

def _rate_limit():
    global _last_call
    dt = time.time() - _last_call
    if dt < 3.0:
        time.sleep(3.0 - dt)
    _last_call = time.time()

def load_seen():
    if os.path.exists(SEEN_PATH):
        with open(SEEN_PATH) as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    with open(SEEN_PATH, "w") as f:
        json.dump(sorted(seen), f)

def _parse_atom(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = []
    for e in root.findall("a:entry", ns):
        arxid = e.findtext("a:id", default="", namespaces=ns).split("/abs/")[-1]
        title = " ".join(e.findtext("a:title", default="", namespaces=ns).split())
        summary = " ".join(e.findtext("a:summary", default="", namespaces=ns).split())
        published = e.findtext("a:published", default="", namespaces=ns)
        authors = [a.findtext("a:name", default="", namespaces=ns) for a in e.findall("a:author", ns)]
        entries.append(dict(id=arxid, title=title, summary=summary, published=published, authors=authors))
    return entries

def query(search_query, start=0, max_results=20, max_retries=5):
    seen = load_seen()
    params = {
        "search_query": search_query,
        "start": start,
        "max_results": min(max_results, 100),
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    url = BASE_URL + "?" + urllib.parse.urlencode(params)
    backoff = 30
    for attempt in range(max_retries):
        _rate_limit()
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status == 429:
                    raise urllib.error.HTTPError(url, 429, "rate limited", resp.headers, None)
                body = resp.read().decode("utf-8")
            entries = _parse_atom(body)
            new_entries = [e for e in entries if e["id"] not in seen]
            for e in entries:
                seen.add(e["id"])
            save_seen(seen)
            with open(LOG_PATH, "a") as f:
                f.write(json.dumps(dict(
                    ts=time.strftime("%Y-%m-%dT%H:%M:%S"),
                    query=search_query, start=start, max_results=max_results,
                    total_returned=len(entries), new_count=len(new_entries),
                    ids=[e["id"] for e in entries],
                )) + "\n")
            return entries, new_entries
        except Exception as ex:
            code = getattr(ex, "code", None)
            print(f"  [retry {attempt+1}/{max_retries}] error: {ex} -- backing off {backoff}s", file=sys.stderr, flush=True)
            time.sleep(min(backoff, 600))
            backoff = min(backoff * 2, 600)
    raise RuntimeError(f"query failed after {max_retries} retries: {search_query}")

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "all:test"
    entries, new = query(q, max_results=10)
    print(f"query={q!r} total={len(entries)} new={len(new)}")
    for e in new:
        print(f"  [{e['id']}] {e['title']}")
