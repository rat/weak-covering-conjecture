"""
H-006 Codex round 4: independently test estimate (6), |chi_r(u)| <= (1+u^2/r^2)^{-(N-2)/2},
for our ACTUAL X (continuous density phi, X = sum_j (2/3^j)*U_j, U_j iid Unif[0,1]).

chi_r(u) := F(r-iu)/F(r), F(s) := E[e^{-sX}] = prod_j (1-e^{-2s/3^j})/(2s/3^j) (complex s).

Note: since X has a CONTINUOUS density (not a lattice distribution), chi_r(u) should NOT be
periodic in u -- Codex's caution about lattice periodicity may not apply here. Test this directly
by scanning u over a WIDE range (well beyond any plausible inversion cutoff) and checking whether
the claimed bound (with C=1) holds throughout, or whether it fails/oscillates.
"""
import mpmath as mp

mp.mp.dps = 30


def F_complex(s, terms=200):
    """F(s) = prod_j (1-e^{-2s/3^j})/(2s/3^j), s complex."""
    total = mp.mpc(1, 0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total *= (1 - mp.e ** (-2 * x)) / (2 * x)
        denom *= 3
    return total


def chi_r(u, r, terms=200):
    return F_complex(r - 1j * u, terms) / F_complex(r, terms)


def N_of(r):
    return mp.floor(mp.log(r) / mp.log(3))


print(f"{'r':>10} {'u':>10} {'|chi_r(u)|':>16} {'bound(C=1)':>16} {'ratio':>10} {'bound_holds':>12}")
worst_ratio = mp.mpf(0)
for r in [mp.mpf(100), mp.mpf(1000), mp.mpf(10000)]:
    N = N_of(r)
    for u_frac in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(5),
                   mp.mpf(10), mp.mpf(50), mp.mpf(200), mp.mpf(1000)]:
        u = u_frac * r  # scan relative to r
        val = abs(chi_r(u, r))
        bound = (1 + (u / r) ** 2) ** (-(N - 2) / 2)
        ratio = val / bound if bound != 0 else mp.inf
        worst_ratio = max(worst_ratio, ratio)
        holds = "YES" if val <= bound * (1 + mp.mpf('1e-10')) else "NO <---"
        print(f"{float(r):10.0f} {float(u):10.2f} {float(val):16.6e} {float(bound):16.6e} {float(ratio):10.4f} {holds:>12}")

print(f"\nWorst observed ratio |chi_r(u)|/bound across all tests: {float(worst_ratio):.6f}  (should be <=1 if C=1 holds)")
