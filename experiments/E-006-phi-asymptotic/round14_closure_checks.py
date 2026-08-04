"""
H-006 Codex round 14: verify the checkable pieces (Codex's own sandbox failed this round, so
none of this was self-checked -- independent verification here is not redundant).

A) F(x) = e^{-x}(1+4e^{-x}+e^{-2x})/(1-e^{-x})^4 =? sum_{n>=1} n^3 e^{-nx}
B) F(x) = 6/x^4 + 1/120 - x^2/504 + O(x^4) as x->0
C) sum_{k>=0} log(coth(x_k/2)) <= 3*q, x_k=3^k*x_0, q=e^{-x_0}, for q<=1/3
"""
import mpmath as mp

mp.mp.dps = 40


def F_closed(x):
    e = mp.e ** (-x)
    return e * (1 + 4 * e + e ** 2) / (1 - e) ** 4


def F_series(x, terms=2000):
    total = mp.mpf(0)
    for n in range(1, terms + 1):
        total += n ** 3 * mp.e ** (-n * x)
    return total


print("=== Part A: F(x) closed form vs series ===")
for x in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('2.0')]:
    closed = F_closed(x)
    series = F_series(x)
    print(f"  x={float(x)}: closed={mp.nstr(closed,15)}  series={mp.nstr(series,15)}  match={abs(closed-series)<mp.mpf('1e-30')}")

print("\n=== Part B: Laurent expansion F(x) = 6/x^4 + 1/120 - x^2/504 + O(x^4) ===")
for x in [mp.mpf('0.001'), mp.mpf('0.01'), mp.mpf('0.05'), mp.mpf('0.1')]:
    actual = F_closed(x)
    predicted = 6 / x ** 4 + mp.mpf(1) / 120 - x ** 2 / 504
    diff = actual - predicted
    print(f"  x={float(x)}: actual={mp.nstr(actual,15)}  predicted={mp.nstr(predicted,15)}  "
          f"diff={mp.nstr(diff,6)}  diff/x^4={mp.nstr(diff/x**4,6)}")

print("\n=== Part C: sum_k log(coth(x_k/2)) <= 3q, x_k=3^k*x_0, q=e^{-x_0} ===")
for x0 in [mp.mpf('1.0'), mp.mpf('1.5'), mp.mpf('2.0'), mp.mpf('3.0')]:
    q = mp.e ** (-x0)
    total = mp.mpf(0)
    for k in range(0, 30):
        xk = mp.mpf(3) ** k * x0
        total += mp.log(mp.cosh(xk / 2) / mp.sinh(xk / 2))  # log(coth(xk/2))
    bound = 3 * q
    holds = total <= bound
    print(f"  x0={float(x0)}, q={float(q):.6f}: sum={mp.nstr(total,10)}  bound=3q={mp.nstr(bound,10)}  holds={holds}")

print("\n=== Also verify the tighter intermediate bound: sum <= 2q/(1-q^2)^2, q<=1/3 ===")
for x0 in [mp.mpf('1.0'), mp.mpf('1.0986')]:  # log(3) ~ 1.0986, q=1/3 boundary
    q = mp.e ** (-x0)
    total = mp.mpf(0)
    for k in range(0, 30):
        xk = mp.mpf(3) ** k * x0
        total += mp.log(mp.cosh(xk / 2) / mp.sinh(xk / 2))
    tight_bound = 2 * q / (1 - q ** 2) ** 2
    print(f"  x0={float(x0)}, q={float(q):.6f}: sum={mp.nstr(total,10)}  tight_bound={mp.nstr(tight_bound,10)}  "
          f"holds={total<=tight_bound}")
