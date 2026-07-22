# E-002 — Independent statistical reverification of the e(l) growth-model comparison (H-001)

Related hypothesis: H-001 (`notes/H-001.md`).

## What was done

The computational extension (E-001) reached exactly one level past the previous paper's table:
l=21 (j*(21)=25), after a memory-ceiling problem was found and fixed enough to reach it; l=22
needs ~86GiB for the DP's state array alone and is not reachable on this hardware at all. So this
is mostly an independent, from-scratch statistical verification of the previous paper's finding
(Section 7, Empirical Result 7.2) using the same l=1..20 data (recomputed and cross-checked
independently in E-001), with more rigor than the previous paper's text reports (explicit 95%
confidence intervals and leave-one-out cross-validation, LOOCV/PRESS, in addition to AIC/BIC, as
the original research brief asked for), plus one genuinely new data point folded into the same
comparison.

Fits four models to e(l) = j*(l) - l*log_4(3) on the tail l=10..21 (n=12, the previous paper used
l=10..20/n=11; same range choice, one more point): constant (stabilization), logarithmic,
square-root, slow-linear.

## Result

**With l=21 added, the qualitative finding strengthens.** Pure stabilization is now more strongly
disfavored (ΔAIC=8.07, ΔBIC=7.58, up from ΔAIC=5.04/ΔBIC=4.64 without l=21), while the three
slow-growth models remain statistically indistinguishable from each other (ΔAIC<0.1, ΔBIC<0.1,
tighter than before). Regressor correlations between the three growth models are still ≥0.995
(an identifiability limit, not a method failure, matching the paper's own framing). The
plateau-frequency test (still 1 plateau, now in 20 increments since l=21 added one more
non-plateau step) gives p=0.062 (one-sided binomial against the expected ~4.1/20 rate), down from
p=0.075 without the new point - moving in the same direction as the AIC finding, still not below
the conventional 0.05 threshold.

New beyond the previous paper's text: LOOCV RMSE is lowest for the logarithmic model (0.281)
versus sqrt (0.282) and slow-linear (0.283), a very small margin, consistent with "statistically
indistinguishable" rather than a tiebreaker. 95% CIs on the growth-model slopes are all bounded
away from zero (logarithmic: [0.472, 1.976]; sqrt: [0.244, 1.027]; slow-linear: [0.031, 0.132]).

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
