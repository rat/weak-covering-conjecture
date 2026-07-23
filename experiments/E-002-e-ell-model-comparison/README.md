# E-002 — Independent statistical reverification of the e(l) growth-model comparison (H-001)

Related hypothesis: H-001 (`notes/H-001.md`).

## What was done

The computational extension (E-001) reached two levels past the previous paper's table: l=21
(j*(21)=25, fits in RAM after a memory-ceiling fix) and l=22 (j*(22)=26, required 500GiB of swap
added to this machine specifically for this run; took ~10749s / ~3h with swap I/O as the
bottleneck, versus ~748s for l=21 without swap). l=23 would need ~263GiB of state, technically
within the 500GiB swap budget but likely far slower; attempted separately, see notes/H-001.md
for its outcome. So this is mostly an independent, from-scratch statistical verification of the
previous paper's finding (Section 7, Empirical Result 7.2) using the same l=1..20 data
(recomputed and cross-checked independently in E-001), with more rigor than the previous paper's
text reports (explicit 95% confidence intervals and leave-one-out cross-validation, LOOCV/PRESS,
in addition to AIC/BIC, as the original research brief asked for), plus two genuinely new data
points folded into the same comparison.

Fits four models to e(l) = j*(l) - l*log_4(3) on the tail l=10..22 (n=13, the previous paper used
l=10..20/n=11; same range choice, two more points): constant (stabilization), logarithmic,
square-root, slow-linear.

## Result

**With l=21 and l=22 added, the qualitative finding strengthens further.** Pure stabilization is
now much more strongly disfavored (ΔAIC=11.90, ΔBIC=11.33, up from ΔAIC=8.07/ΔBIC=7.58 with only
l=21, and ΔAIC=5.04/ΔBIC=4.64 with neither). The three slow-growth models remain statistically
indistinguishable from each other (ΔAIC<0.6, ΔBIC<0.6), though slow-linear now edges out
logarithmic and sqrt on both AIC and LOOCV, a reversal from the l=21-only comparison (where
logarithmic was marginally ahead) that is itself informative only about how thin this margin is,
not about which model is "right" (regressor correlations are still ≥0.994). The plateau-frequency
test (still just 1 plateau, now in 21 increments) gives p=0.052, the closest yet to the
conventional 0.05 threshold without crossing it, continuing to move in the same direction as
every other statistic added so far.

New beyond the previous paper's text: LOOCV RMSE is now lowest for slow-linear (0.282) versus
sqrt (0.284) and logarithmic (0.288), still a very small margin. 95% CIs on the growth-model
slopes are all bounded away from zero (logarithmic: [0.704, 2.094]; sqrt: [0.370, 1.075];
slow-linear: [0.048, 0.136]).

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
