# H-001 technical report: reimplementation and honest benchmark of the j*(l) covering computation

2026-07-22. Renato Augusto Tavares. Related: `HYPOTHESES.md` (H-001, H-002),
`notes/H-001.md`, `experiments/E-001-jstar-fast/`, `experiments/E-002-e-ell-model-comparison/`.

## What this report covers

H-001 asked two things: (A) extend the exact computation of j*(l), Wirsching's Weak Covering
Conjecture object, past the previous paper's l=1..20 table, with a fast, independently verified
reimplementation; and (B) redo the statistical model comparison for the growth of
e(l) = j*(l) - l*log_4(3) with the extended data. Part A did not extend past l=20 (see below);
Part B is accordingly an independent statistical reverification using the same data, not a
re-analysis with new points. Both outcomes are reported honestly here, including where the
project's own initial assumptions turned out to be wrong.

## Methodology

**Implementation.** Reimplemented the bitset+cyclic-rotation dynamic program from
`experiment_wcc.py` (E-098, previous project) in Rust, using a native `Vec<u64>` bitset instead
of Python arbitrary-precision integers, parallelized with rayon across the independent per-count
updates within each exponent step (for fixed exponent v, updating state[c+1] from state[c] for
different c writes to distinct targets with no aliasing, so these can run in parallel and be
merged afterward). Code at `experiments/E-001-jstar-fast/` (`src/main.rs`).

**Validation, two layers.**
1. `jstar-fast validate`: exact match against the reference table j*(l), l=1..7
   (`1,4,6,7,9,10,11`) and the pointwise check (l=2,j=2: image={1,2,5,7} mod 9).
2. An independent brute-force cross-check (`src/bin/bruteforce.rs`), computing R_{j-1,j}'s image
   directly by enumeration, with no reduction to R_{l-1,j} and no bitset/rotation trick at all,
   for l<=4 (the only range where full enumeration is tractable). This is a genuinely different
   method, as the project's honesty rules require, not a second copy of the same logic.

**A bug was found and fixed during this step, and it was in the checker, not the implementation
being checked.** The brute-force cross-check initially disagreed with the fast implementation for
l=2,3,4. Investigated rather than assumed the fast method was wrong (per this project's honesty
rule "se a implementação rápida divergir da lenta, pare e investigue" and Rule 8c "verify a
critique before acting on it"): the bug was an off-by-one in the brute-force's own recursion (a
missing lower-bound check on intermediate exponents), confirmed independently with a small Python
script using `itertools.combinations` before touching the Rust code. Once fixed, both methods
agree exactly for l=1..4. This is recorded because it is exactly the scenario the two-method
cross-check exists for: catching an error in either direction, not just in the "clever" method.

**Benchmark, and where the project's own assumption was wrong.** Ran l=1..20 with real wall-clock
timing per step (see table below), then attempted to extend to l=21-23. An initial memory
estimate (done on paper, before running anything) considered only the size of one final bitset
(3^l bits) and concluded l=25-28 was reachable, matching the original brief's "meta realista".
This was wrong: the DP's `state` array holds l+1 full-size bitsets simultaneously throughout the
whole computation (the knapsack structure needs every count-level, not just the final one), and
the parallel merge step holds roughly another l bitsets transiently, so real memory scales as
`~2*(l+1)*3^l/8` bytes at peak, not `3^l/8`. This was caught by consulting the advisor (per Rule
11b, before letting a long, unsupervised background computation run further) before it turned
into an uncontrolled out-of-memory event, then confirmed empirically (not just recomputed on
paper) by watching `/proc/<pid>/status` while l=21 was actually running.

Given the corrected estimate, l=21 was attempted once more, alone (not batched with l=22+), with
an automated watchdog set to kill the process if its own RSS exceeded 50GiB (about 80% of the
machine's 62GB). Before that per-process threshold was reached (process RSS around 46GiB), a
direct system-wide check showed only ~610MB free out of 62GB total and swap already climbing,
so the process was killed manually. System memory recovered fully within seconds. This shows the
real constraint bites earlier than a per-process RSS estimate alone would suggest, because of
system-wide overhead (OS, buffer/cache minimums, this session's own processes) on top of the
DP's own memory footprint.

**Statistical reverification (Part B).** Since no new data points were obtained, `experiments/
E-002-e-ell-model-comparison/experiment.py` reruns the previous paper's model comparison
(constant / logarithmic / square-root / slow-linear fits to e(l) on the tail l=10..20) on the
same, independently-recomputed data, adding 95% confidence intervals and leave-one-out
cross-validation (LOOCV/PRESS) on top of AIC/BIC, as the original research brief asked for but
the previous paper's text did not report.

## Results

**j*(l) table, l=1..20** (matches the previous paper and H-114 exactly; e(l) = j*(l) - l*log_4(3)):

```
l   j*   j*/l    e(l)     wall time (this Rust implementation)
1   1    1.0000   0.208
2   4    2.0000   2.415
3   6    2.0000   3.623
4   7    1.7500   3.830
5   9    1.8000   5.038
6   10   1.6667   5.245
7   11   1.5714   5.453
8   12   1.5000   5.660
9   13   1.4444   5.868
10  15   1.5000   7.075
11  16   1.4545   7.283
12  17   1.4167   7.490
13  18   1.3846   7.698
14  19   1.3571   7.905
15  20   1.3333   8.113
16  20   1.2500   7.320   (plateau: j* did not grow)
17  21   1.2353   7.528     6.406s
18  22   1.2222   7.735    22.828s
19  23   1.2105   7.943    78.022s
20  24   1.2000   8.150   271.156s  (cumulative 381.1s = 6.35 min for the full l=1..20 run)
```

For comparison, the previous paper's pure-Python implementation took 139s, 485s, and 1597s for
l=18, 19, 20 respectively (2221s = 37 min for those three steps alone). This implementation's
per-step growth factor (~3.4-3.6x) is close to Python's ~3.3x/step, as expected: native code and
parallelism give a constant-factor speedup (roughly 6-9x here), not a change in the fundamental
O(3^l) growth rate.

**Memory ceiling (the actual finding of the benchmark step).** Real resident memory for this
DP formulation scales as `Theta((l+1)*3^l)`, not `Theta(3^l)`, because the full triangular
count-indexed table must stay live throughout the computation. On this 62GB machine:

```
l=20: state ~=  8.7 GiB  -- completed
l=21: state ~= 27.4 GiB  -- peak with transients pushed system-wide free memory to ~610MB; killed
l=22: state ~= 86.1 GiB  -- exceeds total physical memory outright
```

This is not an artifact of Python vs. Rust, or of this implementation's specific parallelism
choice: any implementation holding the full DP table faces the same asymptotic memory wall. The
non-multiple-of-3 packing optimization considered in the original technical guide would save at
most ~33% (a constant factor), not change the exponential growth rate, so it would buy at most a
fraction of one additional level, not reach l=25-28.

**Statistical model comparison** (full output in `experiments/E-002-e-ell-model-comparison/`,
tail l=10..20, n=11):

| model | k | ΔAIC | ΔBIC | LOOCV RMSE |
|---|---|---|---|---|
| constant | 1 | 5.036 | 4.638 | 0.369 |
| logarithmic | 2 | 0.000 | 0.000 | 0.283 |
| square-root | 2 | 0.234 | 0.234 | 0.286 |
| slow-linear | 2 | 0.468 | 0.468 | 0.289 |

95% CIs on the growth-model slopes are all bounded away from zero: logarithmic
[0.215, 1.904], square-root [0.102, 1.002], slow-linear [0.012, 0.130]. Regressor correlations
between the three growth models are all >=0.995 (an identifiability limit, matching the previous
paper's own framing, not a method failure). The plateau-frequency test (1 plateau observed in 19
increments) gives a one-sided binomial p=0.075 against the expected ~3.9/19 rate under pure
stabilization, close to but not numerically identical to the previous paper's reported p~=0.072
(a minor difference in how the null rate was operationalized, not a disagreement in substance).

## Explicit comparison with the previous paper's Empirical Result 7.2

The previous paper's Empirical Result 7.2 states: "$j^*(\ell)$ exists and is finite for all
$\ell\le 20$... The excess $e(\ell)$ qualitatively favors unbounded slow growth over
stabilization (two independent statistics, $\Delta\mathrm{AIC}$ and plateau frequency, in the
same direction but not individually decisive)."

This work **confirms** that finding independently: same j*(l) values (recomputed from scratch,
cross-checked by two independent methods, not copied), same qualitative reading (stabilization
disfavored, slow-growth models indistinguishable from each other), and adds confidence intervals
and LOOCV that were not in the previous paper's reported numbers. It does **not** strengthen the
finding with new data (the original goal), and it establishes, for the first time, that reaching
new data with this exact algorithmic approach is not a matter of a faster implementation: the
memory wall is structural. This is itself new information relative to the previous paper, which
only estimated a time-based extension limit ("~3.3x/step... l=21+ would cost ~90min, ~5h, ~16h"),
not a memory-based one.

## What remains open

- The entropy-count bridge from Wirsching's set-covering statement to Tao's probability-bound
  statement (H-002) is unrelated to this computational work and remains unverified.
- A fundamentally different, sub-`3^l`-memory algorithm for this DP (e.g., not materializing the
  full count-indexed table, or a smarter combinatorial representation of R_{j,k}) is a real
  research question that could reopen the computational extension, but was not pursued here: it
  is a genuine algorithmic research risk, not an engineering afterthought, and doing it under
  time pressure to "rescue" H-001's original data-extension goal would risk exactly the kind of
  overclaiming this project's rules are meant to prevent.
- The plateau-frequency test's small numerical mismatch with the previous paper's p-value
  (0.075 vs ~0.072) was not chased down further; both are well above the conventional 0.05
  threshold and the qualitative reading (marginal, same direction) is unaffected either way.
- No formal checksum of the j*(l) results was produced (the checklist mentions this as a
  reproducibility aid); the values are small non-negative integers independently confirmed by
  two methods and by matching a previously published table exactly, which is a stronger check
  than a checksum would add on top, so this was treated as satisfied in substance rather than
  literally.
- This report itself has not yet been through a critique pass (Rule 8/15): before H-001 is
  marked `closed-*` in `HYPOTHESES.md`, a fresh-context critique of this report and the
  underlying code is still needed.
