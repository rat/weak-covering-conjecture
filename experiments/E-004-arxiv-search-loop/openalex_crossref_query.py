"""
Rate-limited OpenAlex + CrossRef clients for the H-003 search loop.

Both are official, free, ToS-compliant APIs used in "polite pool" mode
(identifying mailto in the User-Agent and, for OpenAlex, the mailto= param).
Etiquette here is deliberately stricter than either service requires:
>=3s between requests per source, sequential, exponential backoff
(30s -> x2 -> 600s cap) on any error including 429.

Every call is logged to openalex_search_log.jsonl / crossref_search_log.jsonl.

Why OpenAlex matters for this task: unlike the arXiv API (metadata-only), OpenAlex
exposes `filter=fulltext.search:` over indexed full text, and a citation-graph
filter (`filter=cites:Wxxxx`), so phrases that only appear *inside* a paper are
reachable.
"""
import urllib.request, urllib.parse, time, json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
MAILTO = "dr.renatotavares@gmail.com"
USER_AGENT = f"wcc-h003-research-loop/1.0 (mailto:{MAILTO})"

_last = {}
MIN_INTERVAL = 3.0


def _rate_limit(source):
    dt = time.time() - _last.get(source, 0.0)
    if dt < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - dt)
    _last[source] = time.time()


def _log(source, rec):
    with open(os.path.join(HERE, f"{source}_search_log.jsonl"), "a") as f:
        rec = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%S"), source=source, **rec)
        f.write(json.dumps(rec) + "\n")


def _get(source, url, label, max_retries=4):
    backoff = 30
    for attempt in range(max_retries):
        _rate_limit(source)
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as ex:
            print(f"  [retry {attempt+1}/{max_retries}] {source}/{label}: {ex}"
                  f" -- backoff {backoff}s", file=sys.stderr, flush=True)
            if attempt == max_retries - 1:
                _log(source, dict(label=label, error=str(ex)))
                return None
            time.sleep(min(backoff, 600))
            backoff = min(backoff * 2, 600)
    return None


# ---------------- OpenAlex ----------------
OA_BASE = "https://api.openalex.org/works"
OA_SELECT = "id,doi,title,publication_year,cited_by_count,authorships,primary_location,abstract_inverted_index"


def _oa_abstract(w):
    inv = w.get("abstract_inverted_index")
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[k] for k in sorted(pos))


def oa_query(params, label):
    p = dict(params)
    p.setdefault("mailto", MAILTO)
    p.setdefault("per_page", 20)
    p.setdefault("select", OA_SELECT)
    url = OA_BASE + "?" + urllib.parse.urlencode(p)
    d = _get("openalex", url, label)
    if d is None:
        return []
    res = d.get("results", []) or []
    _log("openalex", dict(label=label, params=params,
                          count=d.get("meta", {}).get("count"), n=len(res)))
    return res


def oa_search(text, per_page=20, extra=None):
    """Title/abstract relevance search."""
    p = {"search": text, "per_page": per_page}
    if extra:
        p.update(extra)
    return oa_query(p, f"search:{text}")


def oa_fulltext(text, per_page=20):
    """Search indexed FULL TEXT (not just metadata) - unavailable on the arXiv API."""
    return oa_query({"filter": f"fulltext.search:{text}", "per_page": per_page},
                    f"fulltext:{text}")


def oa_cited_by(work_id, per_page=50, page=1):
    """Works citing work_id (OpenAlex Wxxxx id or a DOI url)."""
    return oa_query({"filter": f"cites:{work_id}", "per_page": per_page, "page": page},
                    f"cites:{work_id}@p{page}")


def oa_fmt(w, snippet=0):
    au = ", ".join((a.get("author") or {}).get("display_name", "")
                   for a in (w.get("authorships") or [])[:3])
    loc = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "-"
    s = (f"  {w.get('publication_year')} [{(w.get('id') or '').split('/')[-1]}"
         f" {w.get('doi') or ''}] {w.get('title')}\n"
         f"        {au}; {loc}; cited_by={w.get('cited_by_count')}")
    if snippet:
        ab = _oa_abstract(w)
        if ab:
            s += "\n        ABS: " + ab[:snippet]
    return s


# ---------------- CrossRef ----------------
CR_BASE = "https://api.crossref.org/works"


def cr_search(text, rows=15, extra=None):
    p = {"query.bibliographic": text, "rows": rows, "mailto": MAILTO,
         "select": "DOI,title,author,issued,container-title,abstract,is-referenced-by-count"}
    if extra:
        p.update(extra)
    url = CR_BASE + "?" + urllib.parse.urlencode(p)
    d = _get("crossref", url, f"search:{text}")
    if d is None:
        return []
    items = d.get("message", {}).get("items", []) or []
    _log("crossref", dict(label=f"search:{text}",
                          total=d.get("message", {}).get("total-results"), n=len(items)))
    return items


def cr_fmt(it, snippet=0):
    t = (it.get("title") or ["?"])[0]
    au = ", ".join(f"{a.get('family','')}" for a in (it.get("author") or [])[:3])
    yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
    ct = (it.get("container-title") or ["-"])[0]
    s = f"  {yr} [{it.get('DOI')}] {t}\n        {au}; {ct}; cited={it.get('is-referenced-by-count')}"
    if snippet and it.get("abstract"):
        s += "\n        ABS: " + " ".join(it["abstract"].split())[:snippet]
    return s


if __name__ == "__main__":
    mode = sys.argv[1]
    arg = sys.argv[2]
    if mode == "oa":
        for w in oa_search(arg):
            print(oa_fmt(w, 300))
    elif mode == "oaft":
        for w in oa_fulltext(arg):
            print(oa_fmt(w, 300))
    elif mode == "cites":
        for w in oa_cited_by(arg):
            print(oa_fmt(w))
    elif mode == "cr":
        for it in cr_search(arg):
            print(cr_fmt(it, 300))
