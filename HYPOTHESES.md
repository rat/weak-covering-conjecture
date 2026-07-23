# Hypotheses

Last updated: 2026-07-23

| ID | Title | Status | Impact | One-line summary | Detail | Opened | Closed |
|----|-------|--------|--------|-------------------|--------|--------|--------|
| H-001 | Extend j*(l) past l=20 and characterize e(l) growth | in-progress | high | Rust reimplementation reproduces l=1..20 exactly, ~6-9x faster than Python. l=21 succeeded after a memory-wasteful parallelization fix (j*(21)=25, e(21)=8.358). l=22 needed the researcher to add swap (500GiB, since resized to 1.8TiB) since packed state already exceeded 62GB RAM; succeeded via swap I/O (j*(22)=26, e(22)=8.565, ~3h wall time), a second new data point past the previous table. Folded into E-002 (now l=10..22, n=13): dAIC against stabilization now 11.90, plateau-frequency test p=0.052. l=23 (~263GiB state) launched 2026-07-23 09:07 via detached process with a memory watchdog; outcome pending. Needs a third critique pass (covering l=21, l=22, and the swap-based methodology, plus l=23 once it resolves) before closure. | notes/H-001.md | 2026-07-22 | |
| H-002 | Reverify the WCC => beta=1 entropy-count bridge | open-unexplored | high | Object-identity between Tao's Syracuse variable and Wirsching's R_{j,k} confirmed independently (2026-07-22); the one non-mechanical step still open is the entropy-count conversion from set-covering to a probability lower bound. Not "verify the equivalence": the paper claims only WCC=>beta=1 plus a stated weak converse, not bidirectional equivalence. | notes/H-002.md | 2026-07-22 | |

## Notes

- H-001 carries the full technical brief (object definitions, algorithm, benchmark/verification
  requirements, "done" checklist, honesty rules) as given by the researcher at project start,
  plus the verified l=1..20 reference table with per-step timings; see notes/H-001.md.
- 2026-07-22: previous paper and original Python script received and read (paths recorded in
  literature/INDEX.md, L-004/L-005). Both hypotheses moved from backlog to open-unexplored.
  Wirsching's book (L-001) and Tao's blog post (L-003) checked directly against primary sources,
  not just against the previous paper's summary.
