# E-002 — Independent statistical reverification of the e(l) growth-model comparison (H-001)

Related hypothesis: H-001 (`notes/H-001.md`).

## What was done

The computational extension (E-001) did not reach past l=20 (memory ceiling on the available
hardware). So this is NOT a re-analysis with new data points; it is an independent, from-scratch
statistical verification of the previous paper's finding (Section 7, Empirical Result 7.2) using
the same l=1..20 data (recomputed and cross-checked independently in E-001), with more rigor than
the previous paper's text reports: explicit 95% confidence intervals and leave-one-out
cross-validation (LOOCV/PRESS) in addition to AIC/BIC, as the original research brief asked for.

Fits four models to e(l) = j*(l) - l*log_4(3) on the tail l=10..20 (n=11, matching the previous
paper's chosen range): constant (stabilization), logarithmic, square-root, slow-linear.

## Result

Confirms the previous paper's qualitative finding: pure stabilization is disfavored (ΔAIC=5.04,
ΔBIC=4.64, matching the paper's reported "ΔAIC≈5"), while the three slow-growth models remain
statistically indistinguishable from each other (ΔAIC<0.5, ΔBIC<0.5). Regressor correlations
between the three growth models are ≥0.995 (an identifiability limit, not a method failure,
matching the paper's own framing). The plateau-frequency test (1 plateau observed in 19
increments) gives p=0.075 (one-sided binomial against the paper's expected ~3.9/19 rate),
close to but not identical to the paper's reported p≈0.072 (a minor difference from how the null
rate was operationalized, not a disagreement in substance).

New beyond the previous paper's text: LOOCV RMSE is lowest for the logarithmic model (0.283)
versus sqrt (0.286) and slow-linear (0.289), a very small margin, consistent with "statistically
indistinguishable" rather than a tiebreaker. 95% CIs on the growth-model slopes are all bounded
away from zero (logarithmic: [0.215, 1.904]; sqrt: [0.102, 1.002]; slow-linear: [0.012, 0.130]),
which is additional quantitative support (not previously reported) that some positive growth is
present, on top of the qualitative AIC/plateau reading.

## Reproduce

```
python3 experiment.py
```

Requires numpy and scipy (both already present on this machine).
