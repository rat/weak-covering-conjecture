"""
Independent verification of the KEY mathematical claim underlying Codex's round-2/3
derivation of H-006's normalization constant c0 (second consultation cycle,
/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck2_round3_out.txt).

Round 3 derived c0 from the Laurent expansion of Gamma(w)*zeta(1+w) at w=0:

    Gamma(w) * zeta(1+w) = 1/w^2 + A + O(w),
    A := pi^2/12 - gamma_E^2/2 - gamma_1     (gamma_E = Euler-Mascheroni, gamma_1 = first
                                                Stieltjes constant)

with "no 1/w term" (the claimed cancellation), citing this as forced by the pole structure
of Gamma(w) (simple pole at 0) times the pole of zeta(1+w) at w=0 (from zeta's own pole at 1).

This is the actual mathematical content of the derivation (not just its final numerical
output, already checked for internal consistency in verify_round2_constant.py). This
script checks it directly: does Gamma(w)*zeta(1+w) - 1/w^2 numerically converge to A as
w -> 0?
"""
import mpmath as mp

mp.mp.dps = 50


def check():
    gamma_E = mp.euler
    gamma_1 = mp.stieltjes(1)
    pi = mp.pi
    A = pi**2 / 12 - gamma_E**2 / 2 - gamma_1

    print(f"Claimed constant A = pi^2/12 - gamma_E^2/2 - gamma_1 = {A}")
    print(f"{'w':>10} {'Gamma(w)*zeta(1+w) - 1/w^2':>40}")
    for exp in range(1, 8):
        w = mp.mpf(10) ** (-exp)
        val = mp.gamma(w) * mp.zeta(1 + w) - 1 / w**2
        print(f"{float(w):10.1e} {float(val):40.15f}")

    w_tiny = mp.mpf(10) ** (-20)
    val_tiny = mp.gamma(w_tiny) * mp.zeta(1 + w_tiny) - 1 / w_tiny**2
    print(f"\nAt w=1e-20: value = {val_tiny}")
    print(f"Claimed A          = {A}")
    print(f"Difference: {abs(val_tiny - A)}")
    return A, val_tiny


if __name__ == "__main__":
    check()
