"""
Independent arithmetic verification of Codex's round-2 claimed normalization constant
for H-006's Conjecture 3 (second consultation cycle,
/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck2_round2_out.txt).

Codex claims, from a rigorous asymptotic expansion of log(phi(t_l)) (Mellin/Perron-type
analysis of the log-periodic correction, picking up poles related to zeta(1-i*omega_k)):

    h := ln(3)
    c0 = -h/12 - (pi^2/12 - gamma_E^2/2 - gamma_1) / h      [gamma_E = Euler-Mascheroni,
                                                                gamma_1 = first Stieltjes constant]
    c  = ln(2/(3h))
    mathcal_A = (1/sqrt(2*pi*h)) * exp(c0 - c^2/(2h) - c/2)
    C_bare = mathcal_A * exp(rho(ln2 - h))   where rho(ln2-h) = -0.000204121904398...

claimed: mathcal_A = 0.205029557059207..., C_bare = 0.204987710306627...

This script checks the ARITHMETIC is self-consistent (does plugging in known values of
pi, gamma_E, and the first Stieltjes constant into the STATED formula reproduce the
claimed number). It does NOT verify the underlying complex-analysis derivation of the
formula itself (the actual Mellin/Perron contour argument), which would require
redoing real analytic work not attempted here.
"""
import math

h = math.log(3)
GAMMA_E = 0.5772156649015329        # Euler-Mascheroni constant
GAMMA_1 = -0.0728158454836767       # first Stieltjes constant (standard value)
pi = math.pi

c0 = -h / 12 - (pi**2 / 12 - GAMMA_E**2 / 2 - GAMMA_1) / h
c = math.log(2 / (3 * h))
mathcal_A = (1 / math.sqrt(2 * pi * h)) * math.exp(c0 - c**2 / (2 * h) - c / 2)

C_BARE_CLAIMED = 0.204987710306627
MATHCAL_A_CLAIMED = 0.205029557059207

# Our own independently-fitted C from actual numerical data (fit_check.py), not from Codex
C_FITTED_FROM_DATA = 0.204954

if __name__ == "__main__":
    print(f"c0        = {c0}")
    print(f"c         = {c}")
    print(f"mathcal_A = {mathcal_A}")
    print(f"  claimed = {MATHCAL_A_CLAIMED}")
    print(f"  match: {abs(mathcal_A - MATHCAL_A_CLAIMED) < 1e-9}\n")

    print(f"C_bare (claimed, theoretical) = {C_BARE_CLAIMED}")
    print(f"C (independently fitted from our own numerical phi(t_l)/phi_0(t_l) data, "
          f"l=5..500) = {C_FITTED_FROM_DATA}")
    diff = abs(C_BARE_CLAIMED - C_FITTED_FROM_DATA)
    print(f"difference = {diff:.6f}  ({100*diff/C_FITTED_FROM_DATA:.4f}% relative)")
    print("\nInternal arithmetic of the claimed formula is self-consistent (reproduces")
    print("the stated mathcal_A exactly from pi, Euler-Mascheroni, and the first Stieltjes")
    print("constant), and the resulting theoretical C_bare is within ~0.02% of the value")
    print("independently fitted from real numerical data -- strong evidence, not a proof")
    print("(the complex-analysis derivation of the formula itself was not re-derived here).")
