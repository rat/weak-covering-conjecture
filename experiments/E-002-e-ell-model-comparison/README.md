# E-002: Independent statistical reverification of the e(l) growth-model comparison (H-001)

Related hypothesis: H-001 (`notes/H-001.md`).

## What was done

The computational extension (E-001) reached three levels past the previous paper's table: l=21
(j*(21)=25, fits in RAM after a memory-ceiling fix), l=22 (j*(22)=26, required 500GiB of swap
added to this machine specifically for this run; took ~10749s / ~3h with swap I/O as the
bottleneck, versus ~748s for l=21 without swap), and l=23 (j*(23)=27, ~263GiB state, ~375615s /
~104h. **Correction, 2026-07-30 (critique round)**: this successful run had no interruption, so
checkpoint/resume was never actually exercised, per H-001's own 2026-07-28 critique round
(`notes/H-001.md`, "checkpoint confirmed inert at l=23"). The checkpointing existed to guard
against the oomd kill that hit the FIRST l=23 attempt, before this run. See notes/H-001.md for
the full story, including three successive near-misses on the way to j=27). So
this is mostly an
independent, from-scratch statistical verification of the previous paper's finding (Section 7,
Empirical Result 7.2) using the same l=1..20 data (recomputed and cross-checked independently in
E-001), with more rigor than the previous paper's text reports (explicit 95% confidence intervals
and leave-one-out cross-validation, LOOCV/PRESS, in addition to AIC/BIC, as the original research
brief asked for), plus three genuinely new data points folded into the same comparison.

Fits four models to e(l) = j*(l) - l*log_4(3) on the tail l=10..23 (n=14, the previous paper used
l=10..20/n=11; same range choice, three more points): constant (stabilization), logarithmic,
square-root, slow-linear.

## Result

**With l=23 added, the plateau-frequency test crosses the conventional 0.05 threshold for the
first time.** p=0.0426 (down from 0.052 with l=22, 0.062 with l=21, 0.075 with neither), on 1
observed plateau in 22 increments. **This p-value pools all 22 increments, l=1..23, including the
steep l=1..9 region that the model comparison itself discards** (flagged in H-001's own
2026-07-28 critique round, `notes/H-001.md`, and never actually surfaced here until this
correction, 2026-07-30, critique round -- exactly the Rule 8b failure mode this project names as
its own most-validated lesson). Restricting to the same tail the model comparison actually uses
(13 increments, still 1 observed plateau) gives **p ~ 0.22**, well above the conventional
threshold. Both numbers are real and both are reported here now, side by side, rather than
headlining only the pooled figure: state the tail-only number alongside the pooled one whenever
this result is cited, per that critique round's own recommendation. Per this file's own caveat
below, treat either as "the observed increment pattern is [more/less] consistent with a
constant-e(l) source than a conventional significance cutoff would tolerate," not as a formal
p<0.05 result in the classical sense, since e(l) is deterministic, not sampled. Stabilization is disfavored even more sharply on the
information-criterion side too: ΔAIC=16.09, ΔBIC=15.45 (up from ΔAIC=11.90/ΔBIC=11.33 with l=22,
and ΔAIC=5.04/ΔBIC=4.64 with neither l=21 nor l=22). Every statistic added since l=21 has moved
in the same direction; l=23 is the third point in a row to do so.

The three slow-growth models remain statistically indistinguishable from each other by the
conventional ΔAIC>2 rule of thumb (spread up to 1.51: logarithmic ΔAIC=1.51, sqrt ΔAIC=0.72,
both relative to slow-linear as the best fit); slow-linear keeps the lead on both AIC and LOOCV
that it took over from logarithmic once l=22 was added, with sqrt in between (regressor
correlations are still ≥0.993, so this ordering is informative about how thin the margin is, not
about which model is "right"). LOOCV
RMSE: slow-linear 0.284, sqrt 0.291, logarithmic 0.299 (all three ticked up slightly from the
l=22 numbers, consistent with LOOCV naturally getting a bit more pessimistic as a genuinely new,
out-of-pattern point like l=23's tight near-misses enters the tail). 95% CIs on the growth-model
slopes are all bounded away from zero (logarithmic: [0.917, 2.233]; sqrt: [0.484, 1.132];
slow-linear: [0.063, 0.142]).

**Caveat (added after an independent critique pass)**: e(l) is an exact, deterministic sequence,
not a noisy measurement, so the AIC/BIC/LOOCV/CI machinery here is a descriptive comparison of
fit and extrapolation quality, not classical statistical inference with a real sampling
interpretation (residuals are a strongly autocorrelated deterministic sawtooth, not iid noise).
Treat every number as "how well does this functional form fit and extrapolate," not as "with 95%
confidence." This does not weaken the qualitative reading (stabilization fits comparatively
poorly; the three growth forms are mutually indistinguishable), it just describes accurately what
kind of evidence this is.

## Reproduce

```
python3 experiment.py
```

Requires numpy and scipy (both already present on this machine).
