"""
H-006 Codex round 8: rough plausibility check (dense grid sampling, NOT interval-certified as
Codex specified -- that's beyond reasonable scope here) of the medium-frequency modulus claim (M):
    log|psi_r(t)| <= -t^2/4   for T_c <= |t| <= T_6
where psi_r(t) := chi_r(u), u = t/sigma_r, sigma_r = sqrt(V_r)/r (standard deviation of X under
the r-tilt), T_c = 2*sqrt(log(L)), T_6 = theta_6*sqrt(L), L = log(r).

theta_6 is left unspecified by Codex (depends on an undetermined constant K); test across a
broad range of standardized t covering plausible values of both cutoffs.
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp

mp.mp.dps = 40


def kappa2(b):
    x = b / 2
    return 1 - x ** 2 / mp.sinh(x) ** 2


def V_of(r, terms=400):
    V = mp.mpf(0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        b = 2 * r / denom
        if b < mp.mpf(10) ** (-30):
            break
        V += kappa2(b)
        denom *= 3
    return V


def F_complex(s, terms=300):
    total = mp.mpc(1, 0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total *= (1 - mp.e ** (-2 * x)) / (2 * x)
        denom *= 3
    return total


print(f"{'r':>10} {'L':>8} {'T_c':>10} {'sigma_r':>14} {'t':>10} {'u/r':>10} {'log|psi|':>14} {'-t^2/4':>12} {'M<=0?':>8}")
for r in [mp.mpf(100), mp.mpf(1000), mp.mpf(10000), mp.mpf(1e6), mp.mpf(1e8)]:
    V_r = V_of(r)
    sigma_r = mp.sqrt(V_r) / r
    L = mp.log(r)
    T_c = 2 * mp.sqrt(mp.log(L))
    worst_margin = -mp.inf
    for t_frac in [mp.mpf('1.0'), mp.mpf('1.5'), mp.mpf('2.0'), mp.mpf('3.0'),
                   mp.mpf('4.0'), mp.mpf('6.0'), mp.mpf('8.0')]:
        t = T_c * t_frac
        u = t / sigma_r
        chi = F_complex(r - 1j * u) / F_complex(r)
        log_mod = mp.log(abs(chi))
        bound = -t ** 2 / 4
        margin = bound - log_mod  # want margin >= 0 for M<=0
        worst_margin = min(worst_margin, margin) if worst_margin != -mp.inf else margin
        ok = "YES" if margin >= -mp.mpf('1e-8') else "NO <---"
        print(f"{float(r):10.0e} {float(L):8.3f} {float(T_c):10.4f} {float(sigma_r):14.6e} "
              f"{float(t):10.4f} {float(u/r):10.5f} {float(log_mod):14.6f} {float(bound):12.6f} {ok:>8}")
    print(f"   worst margin at r={float(r):.0e}: {float(worst_margin):.6f}  (>=0 means bound held)\n")
