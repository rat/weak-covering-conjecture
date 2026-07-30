"""
Batch driver over arxiv_query.py: runs a list of queries in one process so the
>=3s inter-request rate limit paces the whole batch, printing compact output.

Usage: python3 batch_arxiv.py queries.txt   (one query per line, '#' comments ok)
       python3 batch_arxiv.py -            (queries on stdin)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arxiv_query


def run(queries, max_results=12, snippet=260):
    for q in queries:
        try:
            entries, new = arxiv_query.query(q, max_results=max_results)
        except Exception as ex:
            print(f"\n### QUERY {q!r}\n  FAILED: {ex}", flush=True)
            continue
        print(f"\n### QUERY {q!r}  total={len(entries)} new={len(new)}", flush=True)
        for e in entries:
            tag = "NEW" if e in new else "old"
            print(f"  [{tag}] {e['id']} ({e['published'][:7]}) {e['title']}", flush=True)
            if tag == "NEW":
                print(f"        {e['summary'][:snippet]}", flush=True)


if __name__ == "__main__":
    src = sys.stdin if sys.argv[1] == "-" else open(sys.argv[1])
    qs = [ln.strip() for ln in src if ln.strip() and not ln.startswith("#")]
    mr = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    run(qs, max_results=mr)
