"""
Round 6 (second lateral cycle): implement and test the ORIGINAL round-1 Durfee-square
codebook-saturation sufficient condition, filling in a gap Codex never actually specified
(the constant C_d in H_{j,j}(lambda) = C_d + 2^d*H_{d,j-d}(A) + (3/2)^d*H_{j-d,d}(B)) by deriving
it directly from the H_{a,b} definition (Codex's own round-2-confirmed notation), splitting the
Young diagram into its Durfee square plus the two rectangular arms A (top-right, d x (j-d)) and
B (bottom-left, (j-d) x d).

Hand derivation (checked below numerically before trusting it):
  C_d = (2^d - 1) * ((3/2)^d - 1)
  the d x d square contributes exactly C_d
  the arm A contributes exactly 2^d * H_{d,j-d}(A)
  the arm B contributes exactly (3/2)^d * H_{j-d,d}(B)

Then implement the actual codebook-saturation test at real (l, j, d).
"""
from itertools import combinations
from fractions import Fraction

def F_direct(alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def alphas_to_lambda(alphas, j):
    # lambda_r = alpha_{r-1} - (j-r), r=1..j (1-indexed lambda); alphas sorted descending
    return [alphas[r - 1] - (j - r) for r in range(1, j + 1)]

def H(a, b, lam_prefix):
    """H_{a,b}(lambda) using only the first `a` parts of lam_prefix (each part <= b implied by
    construction). Returns an exact Fraction (can be non-integer, per Codex's own caution)."""
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

def durfee_size(lam, j):
    d = 0
    for q in range(1, j + 1):
        lq = lam[q - 1] if q - 1 < len(lam) else 0
        if lq >= q:
            d = q
        else:
            break
    return d

def C(d):
    return (Fraction(2) ** d - 1) * (Fraction(3, 2) ** d - 1)

print("=== Check: hand-derived full Durfee decomposition, against direct F_j computation ===")
import random
random.seed(6)
ok = True
for trial in range(200):
    j = random.randint(2, 9)
    alphas = sorted(random.sample(range(0, 2 * j), j), reverse=True)
    lam = alphas_to_lambda(alphas, j)
    d = durfee_size(lam, j)
    A = [lam[r - 1] - d for r in range(1, d + 1)]           # top-right arm, d parts, each <= j-d
    B = [lam[r - 1] for r in range(d + 1, j + 1)]           # bottom-left arm, j-d parts, each <= d

    Hjj = H(j, j, lam)
    Cd = C(d)
    HA = H(d, j - d, A)
    HB = H(j - d, d, B)
    rhs_Hjj = Cd + Fraction(2) ** d * HA + Fraction(3, 2) ** d * HB

    F_val = F_direct(alphas)
    F_from_formula = Fraction(3) ** j - Fraction(2) ** j + Fraction(2) ** j * rhs_Hjj

    if Hjj != rhs_Hjj or F_val != F_from_formula:
        ok = False
        print(f"  MISMATCH j={j} d={d} alphas={alphas}: Hjj={Hjj} rhs={rhs_Hjj} "
              f"F_direct={F_val} F_formula={F_from_formula}")

print(f"  200 random trials: {'ALL MATCH (full Durfee decomposition, including derived C_d, confirmed exact)' if ok else 'FAILURES FOUND'}")
