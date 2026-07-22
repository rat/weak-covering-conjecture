# Hypotheses

Last updated: 2026-07-22

| ID | Title | Status | Impact | One-line summary | Detail | Opened | Closed |
|----|-------|--------|--------|-------------------|--------|--------|--------|
| H-001 | Extend j*(l) past l=20 and characterize e(l) growth | in-progress | high | Rust reimplementation (bitset+rotation, rayon-parallelized) reproduces l=1..20 exactly, ~6-9x faster than Python. Honest benchmark reveals the REAL constraint is memory, not time: state holds (l+1) full 3^l-bit bitsets simultaneously, ~doubling at peak; l=21 is memory-marginal on this 62GB machine, l=22+ is not reachable with the dense-bitset approach at all. Contradicts the brief's "meta realista l=25-28" (extrapolated from time alone). Decision pending on how to proceed. | notes/H-001.md | 2026-07-22 | |
| H-002 | Reverify the WCC => beta=1 entropy-count bridge | open-unexplored | high | Object-identity between Tao's Syracuse variable and Wirsching's R_{j,k} confirmed independently (2026-07-22); the one non-mechanical step still open is the entropy-count conversion from set-covering to a probability lower bound. Not "verify the equivalence": the paper claims only WCC=>beta=1 plus a stated weak converse, not bidirectional equivalence. | notes/H-002.md | 2026-07-22 | |

## Notes

- H-001 carries the full technical brief (object definitions, algorithm, benchmark/verification
  requirements, "done" checklist, honesty rules) as given by the researcher at project start,
  plus the verified l=1..20 reference table with per-step timings; see notes/H-001.md.
- 2026-07-22: previous paper and original Python script received and read (paths recorded in
  literature/INDEX.md, L-004/L-005). Both hypotheses moved from backlog to open-unexplored.
  Wirsching's book (L-001) and Tao's blog post (L-003) checked directly against primary sources,
  not just against the previous paper's summary.
