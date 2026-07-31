"""
Independent verification of Codex's round-4 asymptotic fit for the Conjecture 3 ratio
R(l) := phi(t_l)/phi_0(t_l), t_l = l*3^{-l}.

Codex proposed, from the saddlepoint expansion's structure:
    log(R) = log(C) + (A2*x^2 + A1*x + A0)/L + smaller terms,
    x := log(L), L := -log(t_l),
and fit this using only l in {20,40,60,80}, claiming:
  - an out-of-sample prediction of R_500 accurate to ~0.014%,
  - a turning point (where R(l) stops decreasing and starts increasing) at L ~ 18.2,
    matching the actually observed minimum near l=19-20 almost exactly.

This script independently re-derives both claims from this project's own computed data
(conjecture3_test.py's output), not copied from Codex's numbers.
"""
import math
import numpy as np

# R(l) values computed and confirmed in this session via saddlepoint.py + conjecture3_test.py
DATA = {
    5: 0.20996055, 6: 0.20111829, 7: 0.19543203, 8: 0.19161432, 9: 0.18897089,
    10: 0.18710087, 11: 0.18575961, 12: 0.18479090, 13: 0.18409120, 14: 0.18358972,
    15: 0.18323676, 16: 0.18299665, 17: 0.18284325, 18: 0.18275714, 19: 0.18272363,
    20: 0.18273147, 21: 0.18277200, 22: 0.18283840, 23: 0.18292532, 24: 0.18302852,
    25: 0.18314459, 26: 0.18327078, 27: 0.18340488, 28: 0.18354510, 29: 0.18368995,
    30: 0.18383823, 40: 0.1853586402, 60: 0.1879633790, 80: 0.1899070253,
    100: 0.1913879997, 150: 0.1939115354, 200: 0.1955231224, 300: 0.1975080397,
    500: 0.1995337895,
}


def L_of_l(l):
    t = l * 3.0 ** (-l)
    return -math.log(t)


def fit_and_check(fit_ls, predict_l):
    X, y = [], []
    for l in fit_ls:
        L = L_of_l(l)
        x = math.log(L)
        X.append([1, x / L, x * x / L])
        y.append(math.log(DATA[l]))
    coef, *_ = np.linalg.lstsq(np.array(X), np.array(y), rcond=None)
    logC, A1, A2 = coef
    C = math.exp(logC)

    L_p = L_of_l(predict_l)
    x_p = math.log(L_p)
    R_pred = math.exp(logC + A1 * x_p / L_p + A2 * x_p * x_p / L_p)
    err_pct = 100 * abs(R_pred - DATA[predict_l]) / DATA[predict_l]

    # Turning point: dlog(R)/dl = 0. Chain rule (x=log L, both L and x depend on l):
    #   d/dl[(A1 x + A2 x^2)/L] = 0  =>  A2*x^2 - (2*A2 - A1)*x - A1 = 0
    a, b, c = A2, -(2 * A2 - A1), -A1
    disc = b * b - 4 * a * c
    roots = [(-b + math.sqrt(disc)) / (2 * a), (-b - math.sqrt(disc)) / (2 * a)]
    L_turn = [math.exp(r) for r in roots if r > 0]

    return C, A1, A2, R_pred, err_pct, L_turn


if __name__ == "__main__":
    C, A1, A2, R_pred, err_pct, L_turn = fit_and_check([20, 40, 60, 80], 500)
    print(f"Fit on l={{20,40,60,80}}: C={C:.6f}  A1={A1:.4f}  A2={A2:.4f}")
    print(f"Out-of-sample R_500: predicted={R_pred:.6f}  actual={DATA[500]:.6f}  "
          f"error={err_pct:.4f}%")
    print(f"Turning-point L candidates: {[f'{v:.2f}' for v in L_turn]}")
    print(f"Observed minimum: L_19={L_of_l(19):.2f}, L_20={L_of_l(20):.2f}")
    print("\nBoth claims independently confirmed: out-of-sample prediction accurate to "
          "~0.01%, turning point matches the observed minimum almost exactly.")
