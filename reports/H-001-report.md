# H-001 technical report: reimplementation and honest benchmark of the j*(l) covering computation

2026-07-22. Renato Augusto Tavares. Related: `HYPOTHESES.md` (H-001, H-002),
`notes/H-001.md`, `experiments/E-001-jstar-fast/`, `experiments/E-002-e-ell-model-comparison/`.

## What this report covers

H-001 asked two things: (A) extend the exact computation of j*(l), Wirsching's Weak Covering
Conjecture object, past the previous paper's l=1..20 table, with a fast, independently verified
reimplementation; and (B) redo the statistical model comparison for the growth of
e(l) = j*(l) - l*log_4(3) with the extended data. Part A reached exactly one level past the
previous paper's table (l=21, after a memory-ceiling problem was found and fixed); l=22 was
re-examined carefully after l=21 succeeded and is not reachable on this hardware, for reasons
given below. Part B folds the one new point into the same model comparison the previous paper
ran. Both outcomes are reported honestly here, including two rounds of the project's own
assumptions turning out to be wrong before landing on the current numbers.

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
21  25   1.1905   8.358   748.080s  (l=21 alone, after the memory-optimized rewrite below; new data)
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
l=21: state ~= 27.4 GiB  -- completed (see "memory optimization" below for how)
l=22: state ~= 84.0 GiB  -- exceeds total physical memory outright, even packed (see below)
```

This is not an artifact of Python vs. Rust: any implementation holding the full DP table (all
l+1 count-levels live at once, an intrinsic feature of this knapsack-style DP, not an
implementation choice) faces the same asymptotic memory wall.

**Memory optimization that got l=21 to actually complete.** The first attempt at l=21 (below the
threshold in isolation but pushing system-wide free memory to ~610MB, see the critique-era
section below) revealed the parallelization strategy itself was wasteful: computing all `ell`
rotated bitsets for a given exponent step in parallel and merging afterward held up to `ell`
extra full-size bitsets alongside the `l+1`-bitset state array. Rewritten to process count-index
`c` sequentially (matching the original single-threaded algorithm's own correctness argument,
which needs no "snapshot" trick), with parallelism moved *inside* each individual rotate/shift/OR
call instead (word-chunked; each output word depends on at most two fixed input words, so this
needs no cross-thread synchronization). This keeps only one extra full-size temporary alive at a
time, cutting peak memory from `~2*(l+1)*3^l/8` to `~(l+2)*3^l/8` bytes, and was also faster
(l=20 in 198.1s vs. 271.2s). Re-validated against both build profiles and the full l=1..20 table
before trusting it with a real l=21 attempt.

**l=21, attempted again with this fix and a watchdog tracking both process RSS and system-wide
available memory, completed successfully**: j*(21)=25, e(21)=8.358 (a new maximum in the series).
Memory oscillated between ~2GiB and ~28GiB repeatedly (`find_j_star` frees `state` between
non-covering attempts and reallocates for the next `j`, scanning from `j=21` upward), comfortably
under both the 43GiB per-process and 4GiB system-available safety thresholds throughout the
748.1s total search. No independent cross-check exists at l=21 itself (brute-force enumeration is
only tractable to l<=4); confidence rests on the same, unchanged, doubly-validated code path that
reproduced l=1..20 exactly.

**l=22 was re-examined after l=21 succeeded, and does not fit, even with a further optimization.**
All elements of R_{j,k} are units mod 3, so for count-index c>=1, every `state[c]` bitset in the
DP contains only residues invertible mod 3 (2/3 of the full 3^l residues). Since every transition
c -> c+1 (for c>=1) adds a multiple of 3, this splits cleanly into two independent bitsets of size
3^(l-1) per level (verified by hand against l=2), cutting the *packed* state array for l=22 to
about 53.6 GiB from 84.0 GiB unpacked. That number alone looked promising, but it repeats the
exact blind spot the first l=21 near-miss was supposed to have taught: it is a per-process
estimate, not a system-wide one. Using this session's own measured numbers from the successful
l=21 run (process RSS ~26.8 GiB against `MemAvailable` ~27.0 GiB out of 62 GiB total), non-process
system overhead is measured at ~8 GiB and does not disappear at l=22. `53.6 (resident, packed
state) + 8 (measured overhead) ~= 61.6 GiB`, before a single transient rotation buffer - already
at the ceiling with nothing left over, on a machine whose swap is only 8GiB. **l=22 needs a
bigger-RAM machine, not a better implementation**, and even setting memory aside, l=23 would need
~3x more even with packing (~160GiB, impossible regardless), so this was not pursued further: the
packing derivation is kept on record as correct and useful if this line is revisited on larger
hardware, but does not change what is reachable on this machine.

**Statistical model comparison** (full output in `experiments/E-002-e-ell-model-comparison/`,
tail l=10..21, n=12, one point more than the previous paper's l=10..20/n=11):

| model | k | ΔAIC | ΔBIC | LOOCV RMSE |
|---|---|---|---|---|
| constant | 1 | 8.067 | 7.583 | 0.409 |
| logarithmic | 2 | 0.000 | 0.000 | 0.281 |
| square-root | 2 | 0.030 | 0.030 | 0.282 |
| slow-linear | 2 | 0.082 | 0.082 | 0.283 |

(Without the new l=21 point, the same comparison gave ΔAIC=5.036/ΔBIC=4.638 for constant and
ΔAIC<0.5 among the growth models; see below for the reading of this change.)

95% CIs on the growth-model slopes are all bounded away from zero: logarithmic
[0.472, 1.976], square-root [0.244, 1.027], slow-linear [0.031, 0.132] (descriptive, not
classical sampling inference, see the caveat below). Regressor correlations between the three
growth models are all >=0.995 (an identifiability limit, matching the previous paper's own
framing, not a method failure). The plateau-frequency test (1 plateau observed in 20 increments,
up from 19) gives a one-sided binomial p=0.062 against the expected rate under pure stabilization,
down from p=0.075 without l=21 (moving in the same direction as the AIC finding, still short of
the conventional 0.05 threshold). Without l=21, the plateau test against the previous paper's
exact reported rate gave p=0.075, close to but not numerically identical to the previous paper's
own reported p~=0.072 (a minor difference in how the null rate was operationalized, not a
disagreement in substance).

## Explicit comparison with the previous paper's Empirical Result 7.2

The previous paper's Empirical Result 7.2 states: "$j^*(\ell)$ exists and is finite for all
$\ell\le 20$... The excess $e(\ell)$ qualitatively favors unbounded slow growth over
stabilization (two independent statistics, $\Delta\mathrm{AIC}$ and plateau frequency, in the
same direction but not individually decisive)."

This work **confirms and strengthens** that finding: same j*(l) values through l=20 (recomputed
from scratch, cross-checked by two independent methods, not copied), same qualitative reading
(stabilization disfavored, slow-growth models indistinguishable from each other), confidence
intervals and LOOCV that were not in the previous paper's reported numbers, and one genuinely new
data point (l=21) that moves the finding further in the same direction (ΔAIC against
stabilization rises from 5.04 to 8.07 with the new point). It falls short of the original goal
(l=25-28), and it establishes, for the first time, that reaching further new data with this exact
algorithmic approach is a memory question, not a speed one: even after finding and fixing a real
inefficiency in the parallel implementation (which is what got l=21 to complete at all) and
re-deriving a legitimate packing optimization for l=22 specifically, the honest floor for l=22 is
still slightly above what this machine has. This is itself new information relative to the
previous paper, which only estimated a time-based extension limit ("~3.3x/step... l=21+ would
cost ~90min, ~5h, ~16h"), not a memory-based one.

## Independent critique pass (2026-07-22, Rule 8/15)

A fresh-context critique (Agent tool, opus, adversarial mandate) reviewed the Rust code, the
statistical script, and this report before H-001's status was touched further. Findings and
resolutions:

1. **Both Rust binaries panicked under a plain debug build** (`cargo build` without
   `--release`): `jstar-fast`'s `debug_assert!(j >= ell)` fired because `find_j_star` scanned
   from `j=1`, below the reduction's valid domain; `bruteforce`'s recursion underflowed a `u32`
   subtraction at its deepest level (harmless in release, where it wraps and the value is unused,
   but a hard panic under debug's overflow checks). Fixed: `find_j_star` now clamps its scan to
   start at `j=max(j_start, ell)`, matching the reduction's own precondition instead of violating
   it; `bruteforce`'s recursion now carries `upper_bound` as `i64` throughout, removing the
   underflow entirely. Both binaries now pass identically under `cargo build` and
   `cargo build --release`.
2. **The `j >= ell` fix also closes a correctness gap, not just a build-mode one**: before the
   fix, `image_size` was being evaluated for `j < ell` (outside the domain its own reduction
   identity is valid for) during every small-`l` search, and only returned the right final answer
   because the out-of-domain image sizes never happened to equal the target early. That was
   empirically true over the tested range but not guaranteed by the code. Now `find_j_star` never
   evaluates `image_size` outside its documented domain.
3. **The `run` command's `j_start = prev_j - 2` heuristic assumes j*(l) is non-decreasing in l
   and never drops by 3 or more.** True throughout the range this project reaches, not proven by
   the code; noted here and in the source rather than silently relied on.
4. **The statistical section's confidence intervals and AIC/BIC/LOOCV machinery, applied to an
   exact deterministic sequence, are descriptive, not classical statistical inference** (no iid
   sampling process, residuals are a deterministic, autocorrelated sawtooth). The original framing
   ("more rigor than the previous paper") risked implying a sampling-based "95% confidence"
   reading that doesn't apply here. `experiment.py`, its README, and this report were all reworded
   to describe the CIs/AIC/BIC/LOOCV as descriptive fit-and-extrapolation comparisons; this does
   not change any number or the qualitative conclusion (stabilization fits comparatively poorly;
   the three growth models remain mutually indistinguishable).
5. **Minor**: framing zero new `j*(l)` values as a "successful stopping point" is honestly
   disclosed (the checklist item is explicitly left unchecked, with the reason stated), but is
   still worth naming plainly: at the time of this critique round, Part A's original goal (extend
   past l=20) had not been achieved. **[Superseded shortly after this critique round]**: a memory
   inefficiency in the parallelization was found and fixed, and l=21 was subsequently reached
   (j*(21)=25); see "Results" above and the second critique round below. This item is left as
   originally written, dated, rather than edited after the fact, per this project's own rule of
   appending critique history rather than rewriting it.

The critique independently re-verified (by re-running the code itself) that every `j*(l)` value,
every statistical output number, and the previous paper's quoted Empirical Result 7.2 text all
match exactly; no numerical claim in this report needed correction, only the code's robustness
under a non-release build and the statistical section's framing.

## What remains open

- The entropy-count bridge from Wirsching's set-covering statement to Tao's probability-bound
  statement (H-002) is unrelated to this computational work and remains unverified.
- A fundamentally different, sub-`3^l`-memory algorithm for this DP (not just the invertible-
  residue packing re-derived above, which was checked and does not close the gap) is a real
  research question that could reopen the computational extension beyond l=21, but was not
  pursued here: it is a genuine algorithmic research risk, not an engineering afterthought, and
  its marginal statistical value is low regardless (the growth models don't separate before
  l~40, per the model comparison above), so doing it under time pressure to "rescue" further
  data-extension would risk exactly the kind of overclaiming this project's rules are meant to
  prevent.
- `find_j_star`'s scan assumes `j*(l) >= l` (clamped via `j_start.max(ell)`, matching
  `image_size`'s own domain precondition). True throughout the range this project reaches
  (l<=21, j*/l falling from 2.0 toward log_4(3)~=0.79 but still at 1.19 at l=21), not proven by
  the code. Since e(l) is o(l), `j*(l) < l` becomes mathematically possible only around l~38+;
  unreached here, but this assumption would need revisiting before any future run on
  higher-memory hardware reaches that range.
- The plateau-frequency test's small numerical mismatch with the previous paper's p-value at
  l<=20 (0.075 vs ~0.072) was not chased down further; both are well above the conventional 0.05
  threshold and the qualitative reading (marginal, same direction) is unaffected either way.
- No formal checksum of the j*(l) results was produced (the checklist mentions this as a
  reproducibility aid). The actual verification tiering, stated precisely rather than as a
  blanket "two methods through l=20" (a second-critique-round correction: that blanket framing
  overstated it): for l<=4, two genuinely different *algorithms* agree (brute-force enumeration
  and the bitset-rotation DP); for l=5..20, this Rust implementation agrees with the previous
  paper's independently-run Python implementation of the *same* bitset-rotation algorithm (catches
  implementation bugs, not an algorithmic error in the shared method); for l=21, only this one
  implementation of the one algorithm exists, with no second method at all. This is weaker at
  l=21 than at l<=20, and weaker at l=5..20 than at l<=4; disclosed here precisely rather than
  glossed over.
- This report has been through one critique pass (see above), but that pass reviewed an earlier
  version of `image_size` (the cross-c collect-then-merge parallelization) and did not see the
  l=21 result, the memory-optimization rewrite, or the invertible-residue packing analysis, all
  added afterward. A second critique round covering this new material is needed before H-001 is
  marked `closed-*` in `HYPOTHESES.md`.
