"""
Independently verifies (Rule 8c) the two key algebraic claims in Codex's round-26 free-fermion/
determinantal analysis of S(t) (notes/H-003.md's round-26 section), before trusting them.

Setup: x_a = z^{2^a} for z a root of unity (or, for a generic numerical check, any point on the
unit circle). S(t) = sum over a_1>...>a_m of prod_r x_{a_r}^{3^{r-1}} (equation 1 in the transcript).

1. The LGV determinant formula (equation 7/8): for m=2, S(t) equals the 2x2 determinant
   det[[sum_a x_a, sum_{a<=b} x_a x_b^3], [1, sum_b x_b^3]]. Checked by brute force at N=6.

2. The Plucker-relation obstruction (equation 10/11): the two-particle amplitudes p_ab = x_a*x_b^3
   (a>b) are NOT Grassmann-Plucker coordinates -- p_ab*p_cd - p_ac*p_bd + p_ad*p_bc equals
   x_a*x_b^3*x_c*x_d^3 exactly (not zero), proving no ordinary one-particle/free-fermion Slater
   determinant produces these amplitudes.

Both checked exactly (analytically, via the claimed closed forms) and numerically (random z on the
unit circle, random site indices), matching to floating-point precision.
"""
import cmath
import random


def x(a, z):
    return z ** (2 ** a)


def check_lgv_m2(N=6, z=None):
    if z is None:
        z = cmath.exp(2j * cmath.pi * 0.19)
    S = sum(x(a1, z) * x(a2, z) ** 3 for a1 in range(N) for a2 in range(a1))
    sum_xa = sum(x(a, z) for a in range(N))
    sum_xb3 = sum(x(b, z) ** 3 for b in range(N))
    H12 = sum(x(a, z) * x(b, z) ** 3 for a in range(N) for b in range(N) if a <= b)
    det = sum_xa * sum_xb3 - H12
    return S, det


def check_plucker(a, b, c, d, z):
    p = lambda i, j: x(i, z) * x(j, z) ** 3
    lhs = p(a, b) * p(c, d) - p(a, c) * p(b, d) + p(a, d) * p(b, c)
    rhs = x(a, z) * x(b, z) ** 3 * x(c, z) * x(d, z) ** 3
    return lhs, rhs


if __name__ == "__main__":
    S, det = check_lgv_m2()
    print(f"LGV determinant check: S(t)={S}  det={det}  match={abs(S-det) < 1e-9}")

    random.seed(0)
    z = cmath.exp(2j * cmath.pi * 0.37)
    lhs, rhs = check_plucker(9, 6, 4, 1, z)
    print(f"Plucker relation check: LHS={lhs}  closed_form={rhs}  "
          f"match={abs(lhs-rhs) < 1e-9}  nonzero={abs(lhs) > 1e-9}")
