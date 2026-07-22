# Hypotheses

Last updated: 2026-07-22

| ID | Title | Status | Impact | One-line summary | Detail | Opened | Closed |
|----|-------|--------|--------|-------------------|--------|--------|--------|
| H-001 | Extend j*(l) past l=20 and characterize e(l) growth | backlog | high | Reimplement the j*(l) covering computation (Rust/C++, bitset+rotation, redução j>=l) fast enough to push exact data past l=20, then redo AIC/BIC model comparison for e(l)=j*(l)-log_4(3)*l with the extended data. | notes/H-001.md | 2026-07-22 | |
| H-002 | Independently reverify Section 9.1's beta=1 equivalence proof | backlog | high | The previous paper's proof that Wirsching's Weak Covering Conjecture is algebraically equivalent to Tao's beta=1 conjecture has not been independently reverified; the whole project's motivation rests on it. | | 2026-07-22 | |

## Notes

- H-001 carries the full technical brief (object definitions, algorithm, benchmark/verification
  requirements, "done" checklist, honesty rules) as given by the researcher at project start;
  see notes/H-001.md.
- Pending: previous paper and original Python script have not yet been received. Do not start
  H-001's reimplementation work until the reference table (l=1..20) and the algorithm are
  confirmed against the primary source, per Rule 11.
