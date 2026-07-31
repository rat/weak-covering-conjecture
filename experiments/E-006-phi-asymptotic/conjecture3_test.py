"""
Direct numerical test of H-006's Conjecture 3, using gamma/delta/beta derived from
first principles (round 3 of the 2026-07-31 four-round Codex consultation,
/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck_round3_out.txt), NOT extracted from
Berg-Kruppel's inaccessible primary source.

Conjecture 3: phi(z_l)/phi_0(z_l) -> c > 0 along z_l ~ l*3^{-l}, where
    phi_0(t) ~ t^gamma * (-ln t)^delta * exp(-beta * ln^2(t / (-ln t)))
is the truncated-equation saddlepoint asymptotic (Berg-Kruppel eq. 9.6's qualitative
form, as cited secondhand in this project's own notes/H-006.md).

Codex derived, from the SAME saddlepoint machinery validated in saddlepoint.py
(cross-checked: its beta matches an independent hand-derived estimate exactly):

    a := ln(3)
    beta  = 1/(2a)
    gamma = -3/2 - (1 + ln(a/2))/a
    delta = 1 + ln(a/2)/a

and the prediction phi(t_l)/phi_0(t_l) -> kappa, a specific constant (not just "some
constant", an explicitly computable one via C(1)), as l -> infinity along t_l = l*3^{-l}.

This script computes phi_0(t_l) with these exact exponents and phi(t_l) via the
already-validated saddlepoint.py evaluator, and reports the ratio's behavior.
"""
import mpmath as mp
from saddlepoint import phi_saddle

mp.mp.dps = 60

a = mp.log(3)
beta = 1 / (2 * a)
gamma = mp.mpf('-1.5') - (1 + mp.log(a / 2)) / a
delta = 1 + mp.log(a / 2) / a


def phi_0(t):
    t = mp.mpf(t)
    L = -mp.log(t)
    return t ** gamma * L ** delta * mp.e ** (-beta * mp.log(t / L) ** 2)


if __name__ == "__main__":
    print(f"a = ln(3)   = {float(a):.10f}")
    print(f"beta        = {float(beta):.10f}  (expect ~0.4551196133, matches hand-derived estimate)")
    print(f"gamma       = {float(gamma):.10f}")
    print(f"delta       = {float(delta):.10f}\n")

    print(f"{'l':>4} {'t_l':>16} {'phi(t_l)':>16} {'phi_0(t_l)':>16} {'ratio':>16} {'ln(ratio)':>14}")
    prev_ratio = None
    for l in list(range(5, 41, 1)):
        t_l = mp.mpf(l) * mp.mpf(3) ** (-l)
        P, s, K_s, V_s = phi_saddle(t_l, terms=max(200, l + 60))
        p0 = phi_0(t_l)
        ratio = P / p0
        ln_ratio = mp.log(ratio)
        delta_str = ""
        if prev_ratio is not None:
            delta_str = f"  (d={float(ratio-prev_ratio):+.6f})"
        print(f"{l:4d} {float(t_l):16.6e} {float(P):16.6e} {float(p0):16.6e} "
              f"{float(ratio):16.8f} {float(ln_ratio):14.6f}{delta_str}")
        prev_ratio = ratio

    print("\nIf ratio settles to a constant (not drifting monotonically or diverging), that is")
    print("direct numerical support for Conjecture 3's ratio-convergence claim, using an")
    print("independently-derived phi_0, not Berg-Kruppel's original paper.")
