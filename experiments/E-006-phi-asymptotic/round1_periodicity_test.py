"""
H-006 Codex round 1 (2026-08-03): verify the central new claim -- that L(w) := K(e^w)
(K = log Laplace transform, from the ALREADY-VALIDATED saddlepoint.py machinery) has a
genuinely non-constant log-periodic correction H(w) := L(w) - Q(w), Q(w) := -w^2/(2c) +
(1/2 - log(2)/c)*w, c := log(3).

First: hand-check the claimed recurrence L(w+c) - L(w) = log(1-e^{-2e^w}) - w - log(2).
Second (the decisive test): compute D(w) := L(w) - Q(w) at several different phases
theta = w mod c, each evaluated at increasing "depth" n (w = theta + n*c), and check
whether D converges (as n grows) to a LIMIT that depends on theta (real periodicity,
supports Codex's claim) or converges to the SAME limit regardless of theta (H is
actually constant, refutes Codex's claim).
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import K_series

mp.mp.dps = 50
c = mp.log(3)


def Q(w):
    return -w**2 / (2 * c) + (mp.mpf('0.5') - mp.log(2) / c) * w


def L(w):
    return K_series(mp.e ** w, terms=400)


# --- Part 1: hand-check the recurrence ---
print("=== Part 1: recurrence L(w+c) - L(w) =? log(1-e^{-2e^w}) - w - log(2) ===")
for w0 in [mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('5.5'), mp.mpf('12.0')]:
    lhs = L(w0 + c) - L(w0)
    rhs = mp.log(1 - mp.e ** (-2 * mp.e ** w0)) - w0 - mp.log(2)
    diff = abs(lhs - rhs)
    print(f"  w0={float(w0):6.2f}: LHS={mp.nstr(lhs,20)}  RHS={mp.nstr(rhs,20)}  |diff|={mp.nstr(diff,5)}")

# --- Part 2: decisive periodicity test ---
print("\n=== Part 2: does D(w) = L(w) - Q(w) converge to a THETA-DEPENDENT limit? ===")
thetas = [mp.mpf('0.0'), mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75')]
# depths chosen so e^w stays in a range K_series (terms=400) safely handles
for theta_frac in thetas:
    theta = theta_frac * c  # theta in [0, c)
    print(f"\n  theta = {float(theta_frac):.2f}*c = {float(theta):.4f}:")
    prev_D = None
    for n in [5, 10, 15, 20, 25, 30]:
        w = theta + n * c
        Dval = L(w) - Q(w)
        delta = "" if prev_D is None else f"  delta_from_prev={mp.nstr(Dval - prev_D, 6)}"
        print(f"    n={n:3d}  w={float(w):10.4f}  D(w)={mp.nstr(Dval, 15)}{delta}")
        prev_D = Dval
