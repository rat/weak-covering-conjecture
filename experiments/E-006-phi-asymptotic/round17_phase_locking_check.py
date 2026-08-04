"""
H-006 item 5(b) Opus deep-dive: independently verify the core, most decisive new claim --
that H(theta) evaluated at theta = -log(lambda) mod c is genuinely NONCONSTANT across lambda,
using the ALREADY-VALIDATED exact H(w):=L(w)-Q(w) computation from round 1 (NOT Opus's own code,
NOT the truncated 4-term Fourier reconstruction -- the exact machinery via K_series).

Also spot-check the gamma+delta identity claimed: gamma+delta = -(1/c+1/2).
"""
import mpmath as mp

mp.mp.dps = 50
c = mp.log(3)
a_const = mp.mpf('0.5') - mp.log(2) / c
n_depth = 20  # depth at which D(theta)=L(w)-Q(w) is already fully converged (round 1 showed
              # convergence by n=5 already)


def Q(w):
    return -w**2 / (2 * c) + a_const * w


def K_series(s, terms=400):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += mp.log((1 - mp.e ** (-2 * x)) / (2 * x))
        denom *= 3
    return total


def L(w):
    return K_series(mp.e ** w, terms=400)


def H_exact(theta):
    """H(theta), theta in [0,c), via exact L(w)-Q(w) at large depth (round-1 method)."""
    w = theta + n_depth * c
    return L(w) - Q(w)


print("=== H(theta) at theta = -log(lambda) mod c, for lambda in Opus's table ===")
print(f"{'lambda':>8} {'theta=-log(lambda) mod c':>26} {'H(theta)':>18}")
vals = {}
for lam in [mp.mpf('1.0'), mp.mpf('1.2'), mp.mpf('1.5'), mp.mpf('1.8'),
            mp.mpf('2.0'), mp.mpf('2.4'), mp.mpf('2.8'), mp.mpf('3.0')]:
    theta = (-mp.log(lam)) % c
    Hval = H_exact(theta)
    vals[float(lam)] = float(Hval)
    print(f"{float(lam):8.2f} {float(theta):26.10f} {mp.nstr(Hval,15):>18}")

Hmax = max(vals.values())
Hmin = min(vals.values())
print(f"\nH range across these lambda: min={Hmin:.10f} max={Hmax:.10f} spread={Hmax-Hmin:.3e}")
print(f"H(lambda=1) == H(lambda=3)? {abs(vals[1.0]-vals[3.0])<1e-40} "
      f"(should match exactly since -log(3)=-c=0 mod c)")

print("\n=== Consistency: is the pattern non-monotonic (peak in the middle), matching Opus's claim? ===")
lams_sorted = sorted(vals.keys())
for lam in lams_sorted:
    print(f"  lambda={lam:.2f}: H={vals[lam]:.10f}")
