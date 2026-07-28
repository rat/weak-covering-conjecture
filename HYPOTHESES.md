# Hypotheses

Last updated: 2026-07-27

| ID | Title | Status | Impact | One-line summary | Detail | Opened | Closed |
|----|-------|--------|--------|-------------------|--------|--------|--------|
| H-001 | Extend j*(l) past l=20 and characterize e(l) growth | in-progress | high | Rust reimplementation reproduces l=1..20 exactly, ~6-9x faster than Python. l=21 succeeded after a memory-wasteful parallelization fix (j*(21)=25, e(21)=8.358). l=22 needed the researcher to add swap (500GiB, since resized to 1.8TiB) since packed state already exceeded 62GB RAM; succeeded via swap I/O (j*(22)=26, e(22)=8.565, ~3h wall time), a second new data point past the previous table. Folded into E-002 (now l=10..22, n=13): dAIC against stabilization now 11.90, plateau-frequency test p=0.052. l=23 (~263GiB state) first attempt (launched 09:07) lost after ~2h to a systemd-oomd policy kill (not a crash: real memory was nowhere near exhausted); oomd disabled, and jstar-fast now checkpoints/resumes automatically (verified correct against an uninterrupted baseline before trusting it), second attempt launched 12:50, outcome pending. Needs a third critique pass (covering l=21, l=22, the swap-based methodology, and the checkpointing addition, plus l=23 once it resolves) before closure. | notes/H-001.md | 2026-07-22 | |
| H-002 | Reverify the WCC => beta=1 entropy-count bridge | open-unexplored | high | Object-identity between Tao's Syracuse variable and Wirsching's R_{j,k} confirmed independently (2026-07-22); the one non-mechanical step still open is the entropy-count conversion from set-covering to a probability lower bound. Not "verify the equivalence": the paper claims only WCC=>beta=1 plus a stated weak converse, not bidirectional equivalence. | notes/H-002.md | 2026-07-22 | |
| H-003 | Check Bajnok's sumset/critical-number theory for a non-computational bound on j*(l) | backlog | high | arXiv literature pass (2026-07-27, L-015) surfaced a general survey of minimum sizes and "critical numbers" for h-fold/restricted sumsets covering finite abelian groups. If applicable to R_{j-1,j}'s specific {sum 2^{a_i}3^i} structure, could give an actual theoretical bound/asymptotic on j*(l) instead of just more brute-force data points, the highest-impact kind of lead this pass found. Not yet scoped past the abstract. | | 2026-07-27 | |
| H-004 | Formal relation between Wirsching's 3-adic inverse-Collatz Markov process and R_{j,k} | backlog | medium-high | Tao's published paper (L-006, footnote 5) speculatively links his Syracuse-variable Markov process to "the 3-adic Markov process for the inverse Collatz map studied in [Wirsching 1998]," and separately flags Thomas 2016/2017 (L-008) as a related investigation of "3-adic irregularities." Worth checking whether either gives an independent derivation or cross-check of j*(l)/R_{j,k} covering behavior, which currently has no independent verification method past l=4. | | 2026-07-27 | |
| H-005 | Monks et al.'s "sufficient sets" as a possible independent method to bound j*(l) | backlog | medium | L-009 (Monks, Monks, Monks & Monks 2012) defines a different covering-type notion in Collatz dynamics ("sufficient sets," via orbit-intersection rather than residue-covering). If translatable to this project's setting, could serve as the missing second, independent verification method for j*(l) at l>4 (currently only the same algorithm re-run, no second method, per notes/H-001.md's honesty rules). Tractability unclear until read past the abstract. | | 2026-07-27 | |

## Notes

- 2026-07-27: arXiv-only literature search pass completed while l=23's computation ran in the
  background (see literature/INDEX.md L-006 through L-018 and its "Checked this pass" note for
  full detail). Confirmed directly from Tao's published paper (not just the blog post, L-003)
  that Wirsching 1998 is cited, and that Tao's own framing of the connection is explicitly
  speculative, not a proven bridge, reinforcing that H-002's entropy-count bridge is this
  project's own contribution to formalize. Three new backlog hypotheses opened (H-003, H-004,
  H-005); H-003 (Bajnok's sumset/critical-number survey) is flagged as the highest-priority lead
  since it is the only one pointing toward a theoretical rather than computational or
  cross-verification result. No paper found that already extends or reverifies the Weak Covering
  Conjecture itself past 1998/2003.

- H-001 carries the full technical brief (object definitions, algorithm, benchmark/verification
  requirements, "done" checklist, honesty rules) as given by the researcher at project start,
  plus the verified l=1..20 reference table with per-step timings; see notes/H-001.md.
- 2026-07-22: previous paper and original Python script received and read (paths recorded in
  literature/INDEX.md, L-004/L-005). Both hypotheses moved from backlog to open-unexplored.
  Wirsching's book (L-001) and Tao's blog post (L-003) checked directly against primary sources,
  not just against the previous paper's summary.
