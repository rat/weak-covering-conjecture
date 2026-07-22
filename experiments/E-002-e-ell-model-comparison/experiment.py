#!/usr/bin/env python3
"""
Independent statistical reverification of the e(l) growth-model comparison
from the previous paper (Section 7, Empirical Result 7.2), for H-001.

IMPORTANT FRAMING: H-001's computational extension (E-001) did not reach
past l=20 (memory ceiling on the available hardware, see notes/H-001.md).
So this is NOT a re-analysis with new data points; it is an independent,
from-scratch statistical verification of the previous paper's finding using
the SAME l=1..20 data (recomputed and cross-checked independently in E-001,
not just copied from the previous paper), done with more rigor than the
previous paper's text reports: explicit confidence intervals and
leave-one-out cross-validation (LOOCV) in addition to AIC/BIC, as the
research brief originally asked for.

Models fit to e(l) = j*(l) - l*log_4(3), on the tail l=10..20 (n=11 points,
matching the previous paper's choice of range, which avoids small-l
transient behavior):
  1. constant:     e(l) = c
  2. logarithmic:  e(l) = a + b*ln(l)
  3. square-root:  e(l) = a + b*sqrt(l)
  4. slow-linear:  e(l) = a + b*l

Reproduce: python3 experiment.py
"""
import math

import numpy as np
from scipy import stats

# l, j*(l), verified independently via the Rust reimplementation (E-001),
# matching the previous paper's table (Section 7) and H-114 exactly.
DATA = [
    (1, 1), (2, 4), (3, 6), (4, 7), (5, 9), (6, 10), (7, 11), (8, 12),
    (9, 13), (10, 15), (11, 16), (12, 17), (13, 18), (14, 19), (15, 20),
    (16, 20), (17, 21), (18, 22), (19, 23), (20, 24),
]
LOG4_3 = math.log(3) / math.log(4)


def e_of_l(ell, j_star):
    return j_star - ell * LOG4_3


def fit_ols(x_design, y):
    """OLS via lstsq. Returns (coeffs, fitted, rss)."""
    coeffs, residuals, rank, sv = np.linalg.lstsq(x_design, y, rcond=None)
    fitted = x_design @ coeffs
    rss = float(np.sum((y - fitted) ** 2))
    return coeffs, fitted, rss


def aic_bic(rss, n, k):
    # Gaussian-likelihood AIC/BIC for OLS, standard form.
    if rss <= 0:
        rss = 1e-12
    aic = n * math.log(rss / n) + 2 * k
    bic = n * math.log(rss / n) + k * math.log(n)
    return aic, bic


def loocv_press(x_design, y):
    """Leave-one-out cross-validation: PRESS statistic and RMSE_cv."""
    n = len(y)
    sq_errors = []
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        coeffs, _, _ = fit_ols(x_design[mask], y[mask])
        pred_i = x_design[i] @ coeffs
        sq_errors.append((y[i] - pred_i) ** 2)
    press = float(np.sum(sq_errors))
    rmse_cv = math.sqrt(press / n)
    return press, rmse_cv


def confint_slope(x_design, y, coeffs, rss, param_idx, alpha=0.05):
    """95% CI for a coefficient, standard OLS formula."""
    n, k = x_design.shape
    dof = n - k
    sigma2 = rss / dof
    xtx_inv = np.linalg.inv(x_design.T @ x_design)
    se = math.sqrt(sigma2 * xtx_inv[param_idx, param_idx])
    tval = stats.t.ppf(1 - alpha / 2, dof)
    center = coeffs[param_idx]
    return center, center - tval * se, center + tval * se, se


def main():
    ells = np.array([ell for ell, _ in DATA], dtype=float)
    e_vals = np.array([e_of_l(ell, j) for ell, j in DATA], dtype=float)

    print("=== e(l) values (full range, l=1..20) ===")
    for (ell, j), e in zip(DATA, e_vals):
        print(f"  l={ell:2d}  j*={j:3d}  e(l)={e:7.3f}")

    # Tail range l=10..20, matching the previous paper's model comparison.
    tail_mask = ells >= 10
    ells_t = ells[tail_mask]
    e_t = e_vals[tail_mask]
    n = len(ells_t)
    print(f"\n=== Model comparison on tail l=10..20 (n={n}) ===\n")

    models = {}

    # 1. constant: e = c
    X = np.ones((n, 1))
    coeffs, fitted, rss = fit_ols(X, e_t)
    models["constant"] = dict(X=X, coeffs=coeffs, rss=rss, k=1)

    # 2. logarithmic: e = a + b*ln(l)
    X = np.column_stack([np.ones(n), np.log(ells_t)])
    coeffs, fitted, rss = fit_ols(X, e_t)
    models["logarithmic"] = dict(X=X, coeffs=coeffs, rss=rss, k=2)

    # 3. square-root: e = a + b*sqrt(l)
    X = np.column_stack([np.ones(n), np.sqrt(ells_t)])
    coeffs, fitted, rss = fit_ols(X, e_t)
    models["sqrt"] = dict(X=X, coeffs=coeffs, rss=rss, k=2)

    # 4. slow-linear: e = a + b*l
    X = np.column_stack([np.ones(n), ells_t])
    coeffs, fitted, rss = fit_ols(X, e_t)
    models["slow-linear"] = dict(X=X, coeffs=coeffs, rss=rss, k=2)

    results = {}
    for name, m in models.items():
        aic, bic = aic_bic(m["rss"], n, m["k"])
        press, rmse_cv = loocv_press(m["X"], e_t)
        results[name] = dict(aic=aic, bic=bic, rss=m["rss"], press=press,
                              rmse_cv=rmse_cv, k=m["k"], coeffs=m["coeffs"], X=m["X"])

    best_aic = min(r["aic"] for r in results.values())
    best_bic = min(r["bic"] for r in results.values())

    print(f"{'model':<14}{'k':>3}{'RSS':>10}{'AIC':>10}{'dAIC':>8}"
          f"{'BIC':>10}{'dBIC':>8}{'PRESS':>10}{'RMSE_cv':>10}")
    for name, r in results.items():
        print(f"{name:<14}{r['k']:>3}{r['rss']:>10.4f}{r['aic']:>10.3f}"
              f"{r['aic']-best_aic:>8.3f}{r['bic']:>10.3f}{r['bic']-best_bic:>8.3f}"
              f"{r['press']:>10.4f}{r['rmse_cv']:>10.4f}")

    print("\n=== Slope coefficients with 95% CI (growth models only) ===")
    for name in ["logarithmic", "sqrt", "slow-linear"]:
        r = results[name]
        center, lo, hi, se = confint_slope(r["X"], e_t, r["coeffs"], r["rss"], 1)
        print(f"  {name:<14}: slope={center:8.4f}  95% CI=[{lo:8.4f}, {hi:8.4f}]  SE={se:.4f}")

    print("\n=== Pairwise correlation of growth-model regressors (identifiability check) ===")
    reg_log = np.log(ells_t)
    reg_sqrt = np.sqrt(ells_t)
    reg_lin = ells_t
    print(f"  corr(ln l, sqrt l) = {np.corrcoef(reg_log, reg_sqrt)[0,1]:.5f}")
    print(f"  corr(ln l, l)      = {np.corrcoef(reg_log, reg_lin)[0,1]:.5f}")
    print(f"  corr(sqrt l, l)    = {np.corrcoef(reg_sqrt, reg_lin)[0,1]:.5f}")

    print("\n=== Plateau-frequency test (Delta j*(l)=0 events) ===")
    j_stars = [j for _, j in DATA]
    increments = [j_stars[i+1] - j_stars[i] for i in range(len(j_stars) - 1)]
    n_plateaus = sum(1 for d in increments if d == 0)
    n_increments = len(increments)
    print(f"  observed plateaus: {n_plateaus} out of {n_increments} increments")
    print(f"  increments: {increments}")
    # Binomial test against the previous paper's reported null (~3.9 expected in 19 increments)
    expected_rate = 3.9 / 19
    pval = stats.binomtest(n_plateaus, n_increments, expected_rate, alternative="less").pvalue
    print(f"  binomial test (P(plateau)={expected_rate:.4f}, one-sided 'fewer plateaus than expected'): "
          f"p={pval:.4f}")


if __name__ == "__main__":
    main()
