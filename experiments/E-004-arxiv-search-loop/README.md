# E-004: literature-search loop for H-003 (bounding the rank-coupled sum S(t))

Rate-limited, ToS-compliant clients plus the verification code for round 23 of H-003
(see `notes/H-003.md`, entry dated 2026-07-30).

## The methodological finding that made this round work

**The arXiv API indexes metadata only, never full text.** Every prior H-003 search round used it
exclusively. `all:"Syracuse random variable"` returns **zero** results, while OpenAlex's
`filter=fulltext.search:` returns Tao's own paper. Twenty-two rounds of "no literature found on
rank-coupled exponential sums" were partly an artifact of the search tool: Tao states this exact
obstruction in print and devotes his Section 7 to it.

## Clients (all: >=3s between requests, exponential backoff, dedup, jsonl logging)

| file | source | status |
|---|---|---|
| `arxiv_query.py` | arXiv API | works; metadata only |
| `batch_arxiv.py` | driver for the above | runs a query list in one rate-limited process |
| `openalex_crossref_query.py` | OpenAlex + CrossRef, polite pool | works; OpenAlex does full text and citation graph |
| `s2_query.py` | Semantic Scholar Graph | unauthenticated tier returns immediate 429s; never delivered a result despite full backoff |

Logs: `arxiv_search_log.jsonl` (73 queries), `openalex_search_log.jsonl`, `crossref_search_log.jsonl`.

## `verify_syrac_fourier.py`

Independent verification of everything round 23 claims. Run it with `python3 verify_syrac_fourier.py`
(a few seconds, a few MB; safe alongside the memory-committed jstar/mpg jobs). Four parts:

- **(A)** reproduces Toguchi's table (`M_n` and the argmax `k*(n)`, Zenodo 10.5281/zenodo.20490181)
  for `n = 1..9` by two independent methods. Expect nine `YES` rows.
- **(B)** verifies that `R_{l-1,j} mod 3^l` and Tao's `Syrac` are unit multiples of one common core
  sum, by exact set equality, including the project checkpoint `R_{1,2} mod 9 = {1,2,5,7}`.
- **(C)** verifies that `psi_n` is an exact convex combination of normalized layer sums (the bridge
  from Tao's object to this project's `S(t)`); weights sum to 1, value matches to `<1e-8`.
- **(D)** tabulates the measured extremal coefficient against the two thresholds that matter.

The headline consequence, derived in `notes/H-003.md`: **square-root cancellation for `S(t)` is
refuted** for `8 <= n <= 21` (already at `n=8,9`, inside the independently reproduced range), the
square-root ceiling is exactly `3^{-n/2}` with a saddle at budget ratio `4/3`, and the `L^1` Fourier
covering route is capped at `j*(l) <= 2 log_4(3) * l = 1.585 l` even if executed perfectly.

## `codex_round23_*`

The independent-model consult. **It stalled** (bubblewrap sandbox warning, then a dozen `web search:`
lines with empty queries, no verdict). It delivered exactly one substantive correction, which was
checked and acted on (see `notes/H-003.md`, "Correction 1"). The transcript is kept as
`codex_round23_transcript_INCOMPLETE.txt` so the record shows what was and was not obtained:
**Findings 5b and 6 have not been independently confirmed by a second model.**
