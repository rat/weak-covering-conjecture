"""
Real-variable saddlepoint evaluator for phi(t_l), t_l = l*3^{-l}, proposed by Codex in
round 2 of the 2026-07-31 four-round "where are we stuck" consultation for H-006's
Conjecture 3 (see /home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck_round2_{prompt,out}.txt).

This replaces the earlier, genuinely-failed oscillatory Fourier-inversion approach
(phi_eval.py / sweep.py in this same folder) with a monotone REAL equation to solve
and rapidly convergent real series to sum -- no oscillatory quadrature anywhere.

Setup: X = sum_{r>=1} U_r/3^r, U_r iid Uniform[0,2]. Laplace transform:
    L(s) = E[e^{-sX}] = prod_{r>=1} (1-e^{-2s/3^r})/(2s/3^r),   K(s) := log L(s).
    h(x) = log((1-e^{-2x})/(2x))
    m(x) = -x h'(x) = 1 - 2x/(e^{2x}-1)
    v(x) = x^2 h''(x) = 1 - (x/sinh x)^2
    M(s) = -s K'(s) = sum_r m(s/3^r)
    V(s) = s^2 K''(s) = sum_r v(s/3^r)

Saddle equation: -K'(s_l) = t_l, i.e. M(s_l) = s_l * t_l. Solved as a monotone real
root-find (M is smooth, K is convex so M is monotone in the relevant range).

Saddlepoint density approximation:
    phi(t_l) = P_l * (1 + O(1/l)),
    P_l = s_l / sqrt(2*pi*V(s_l)) * exp(K(s_l) + s_l*t_l).

Sanity checks implemented before trusting any t_l result:
  - L(0) = 1 (normalization; automatic from the product form, checked directly).
  - phi(t) computed this way at MODERATE t (0.1-0.4) should be of the same order of
    magnitude as the (partially convergent, before it broke down) values the earlier
    Fourier-inversion attempt got at those same points.
"""
import math
import mpmath as mp

mp.mp.dps = 50


def h(x):
    if x == 0:
        return mp.mpf(0)
    return mp.log((1 - mp.e ** (-2 * x)) / (2 * x))


def m_func(x):
    if x == 0:
        return mp.mpf(0)
    return 1 - 2 * x / (mp.e ** (2 * x) - 1)


def v_func(x):
    if x == 0:
        return mp.mpf(0)
    return 1 - (x / mp.sinh(x)) ** 2


_TINY = mp.mpf(10) ** (-(mp.mp.dps - 8))  # must stay within representable precision


def K_series(s, terms=200):
    """K(s) = log L(s) = sum_r h(s/3^r)."""
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < _TINY:
            break
        total += h(x)
        denom *= 3
    return total


def M_series(s, terms=200):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < _TINY:
            break
        total += m_func(x)
        denom *= 3
    return total


def V_series(s, terms=200):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < _TINY:
            break
        total += v_func(x)
        denom *= 3
    return total


def solve_saddle(t, terms=200, guess=None):
    """Solve M(s) = s*t for s > 0 (monotone real root-find)."""
    def F(s):
        return M_series(s, terms) - s * t

    # bracket: M(s) -> 0 as s->0, M(s) -> infinity slowly (like log_3(s)) as s->infinity;
    # s*t grows without bound, so F(s) = M(s)-s*t goes from ~0 (s small) to -infinity
    # (s large); we want the root, use mpmath's findroot with a decent starting guess.
    if guess is None:
        guess = 1 / t if t > 0 else mp.mpf(1)
    return mp.findroot(F, guess)


def phi_saddle(t, terms=200, guess=None):
    t = mp.mpf(t)
    s = solve_saddle(t, terms, guess=guess)
    K_s = K_series(s, terms)
    V_s = V_series(s, terms)
    P = s / mp.sqrt(2 * mp.pi * V_s) * mp.e ** (K_s + s * t)
    return P, s, K_s, V_s


if __name__ == "__main__":
    print("Sanity check: L(0) = exp(K(0)) should be 1")
    print(f"  K(0) = {K_series(mp.mpf(0))}  (expect 0)")

    print("\nModerate-t cross-check against the earlier (partially-converged) Fourier attempt:")
    print(f"{'t':>8} {'phi_saddle':>18} {'s_l':>14}")
    for t in [mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.4')]:
        P, s, K_s, V_s = phi_saddle(t)
        print(f"{float(t):8.3f} {float(P):18.8f} {float(s):14.4f}")

    print("\nSweep over t_l = l*3^{-l}, l=3..40 (saddlepoint, no oscillatory integration):")
    print(f"{'l':>4} {'t_l':>16} {'s_l':>16} {'phi(t_l)':>18} {'ln(phi)':>14}")
    for l in list(range(3, 21)) + [25, 30, 35, 40]:
        t_l = mp.mpf(l) * mp.mpf(3) ** (-l)
        P, s, K_s, V_s = phi_saddle(t_l, terms=max(200, l + 50))
        ln_phi = mp.log(P) if P > 0 else mp.mpf('-inf')
        print(f"{l:4d} {float(t_l):16.6e} {float(s):16.4f} {float(P):18.6e} {float(ln_phi):14.4f}")
