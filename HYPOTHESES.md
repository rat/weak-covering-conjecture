# Hypotheses

Last updated: 2026-07-22

| ID | Title | Status | Impact | One-line summary | Detail | Opened | Closed |
|----|-------|--------|--------|-------------------|--------|--------|--------|
| H-001 | Extend j*(l) past l=20 and characterize e(l) growth | in-progress | high | Rust reimplementation reproduces l=1..20 exactly, ~6-9x faster than Python; real constraint is memory, not time (state holds (l+1) full 3^l-bit bitsets simultaneously). Attempted l=21 alone with a memory watchdog: system-wide headroom collapsed (~610MB free of 62GB) before completion, confirming l=20 is this machine's practical ceiling for the dense-bitset approach, well short of the brief's "l=25-28". Moving to Part B (statistical analysis) with the existing l=1..20 data, per the researcher's decision and the checklist's own valid-stopping-point clause. | notes/H-001.md | 2026-07-22 | |
| H-002 | Reverify the WCC => beta=1 entropy-count bridge | open-unexplored | high | Object-identity between Tao's Syracuse variable and Wirsching's R_{j,k} confirmed independently (2026-07-22); the one non-mechanical step still open is the entropy-count conversion from set-covering to a probability lower bound. Not "verify the equivalence": the paper claims only WCC=>beta=1 plus a stated weak converse, not bidirectional equivalence. | notes/H-002.md | 2026-07-22 | |

## Notes

- H-001 carries the full technical brief (object definitions, algorithm, benchmark/verification
  requirements, "done" checklist, honesty rules) as given by the researcher at project start,
  plus the verified l=1..20 reference table with per-step timings; see notes/H-001.md.
- 2026-07-22: previous paper and original Python script received and read (paths recorded in
  literature/INDEX.md, L-004/L-005). Both hypotheses moved from backlog to open-unexplored.
  Wirsching's book (L-001) and Tao's blog post (L-003) checked directly against primary sources,
  not just against the previous paper's summary.
