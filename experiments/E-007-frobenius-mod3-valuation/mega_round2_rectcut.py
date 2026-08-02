"""
Round 2 (mega cycle): verify the generalized rectangular-cut formula (round 1's item 1, ranked
Codex's own top priority), which we independently re-derived by hand as a direct generalization
of the already-verified Durfee-square decomposition:

  H_{l,j}(lambda) = C_{h,m} + 2^m * H_{h,j-m}(A) + (3/2)^h * H_{l-h,m}(B)
  C_{h,m} = (2^m - 1) * ((3/2)^h - 1)

for a cut after h rows and m columns (h=m recovers the Durfee case already verified).

Then explore the actual new content: does allowing h != m (off-diagonal cuts) cover residues
that the diagonal (Durfee) strata alone miss? Concretely: at l=6, j=10, strata d=3,4,5 together
missed exactly {262, 505} (mod 729) until stratum d=2 was added. Does some off-diagonal (h,m)
stratum with h,m in a similarly cheap range already cover these two residues?
"""
from fractions import Fraction

def H(a, lam_prefix):
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

def C(h, m):
    return (Fraction(2) ** m - 1) * (Fraction(3, 2) ** h - 1)

def F_direct(alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def alphas_to_lambda(alphas, j):
    return [alphas[r - 1] - (j - r) for r in range(1, len(alphas) + 1)]

# ---------- Check 1: verify the generalized rectangular-cut formula ----------
# IMPORTANT: the identity requires lambda to actually RESPECT the (h,m) cut (rows 1..h have
# lambda_r >= m, i.e. genuinely cross the cut; rows h+1..l have lambda_r <= m). Construct such a
# lambda directly from a chosen (A,B) pair rather than forcing an arbitrary split on a random
# lambda (an earlier version of this script did the latter and was wrong for that reason -- the
# c-range split into 1..m and m+1..lambda_r is only valid when lambda_r>=m for that row).
import random
random.seed(8)
print("=== Check 1: generalized rectangular-cut formula, valid (h,m)-respecting partitions ===")
ok = True
for trial in range(300):
    l = random.randint(1, 8)
    j = random.randint(l, l + 6)
    h = random.randint(0, l)
    m = random.randint(0, j)
    A = sorted((random.randint(0, j - m) for _ in range(h)), reverse=True)
    B = sorted((random.randint(0, m) for _ in range(l - h)), reverse=True)
    lam = [m + a for a in A] + list(B)
    assert all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1)), (lam, h, m)

    Hlj = H(l, lam)
    Chm = C(h, m)
    HA = H(h, A)
    HB = H(l - h, B)
    rhs = Chm + Fraction(2) ** m * HA + Fraction(3, 2) ** h * HB

    if Hlj != rhs:
        ok = False
        print(f"  MISMATCH l={l} j={j} h={h} m={m} lam={lam}: Hlj={Hlj} rhs={rhs}")

print(f"  300 random trials, valid (h,m)-respecting partitions: {'ALL MATCH' if ok else 'FAILURES FOUND'}")

# ---------- Check 2: do off-diagonal cuts cover the l=6 holdouts {262, 505}? ----------

def frac_mod(frac, mod):
    num, den = frac.numerator, frac.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def partitions_in_box(rows, cols):
    if rows == 0:
        yield []
        return
    def rec(remaining_rows, max_part):
        if remaining_rows == 0:
            yield []
            return
        for first in range(max_part, -1, -1):
            for rest in rec(remaining_rows - 1, first):
                yield [first] + rest
    yield from rec(rows, cols)

def rect_stratum_image(l, j, h, m):
    """Full image mod 3^l of F_j over ALL lambda in l x j whose Young diagram is exactly the
    (h,m)-cut shape: A is an h x (j-m) partition (arm beyond column m in the first h rows), B is
    an (l-h) x m partition (remaining rows, bounded by column m). This enumerates the same
    (h,m)-STRATUM the Durfee case specializes (h=m=d)."""
    mod_l = 3**l
    mod_h = 3**h
    mod_lh = 3**(l - h)
    Chm = C(h, m)
    S = set()
    # base (independent of A,B): C_{h,m}
    for A in partitions_in_box(h, j - m):
        HA = H(h, A)
        for B in partitions_in_box(l - h, m):
            HB = H(l - h, B)
            val = Chm + Fraction(2)**m * HA + Fraction(3, 2)**h * HB
            # H_{l,j}(lambda) -> F_j(lambda) = 3^j - 2^j + 2^j * H_{l,j}(lambda), reduced mod 3^l
            # (only first l positions matter mod 3^l, matches the extendability framing)
            F = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * val
            S.add(frac_mod(F, mod_l))
    return S

l, j = 6, 10
holdouts = {262, 505}
print(f"\n=== Check 2: off-diagonal (h,m) cuts vs the l={l} holdouts {holdouts} ===")
for h in range(0, l + 1):
    for m in range(0, 6):  # keep m small, cheap strata only
        if h == m:
            continue  # diagonal case already tested (Durfee)
        S = rect_stratum_image(l, j, h, m)
        covers = holdouts & S
        if covers:
            print(f"  h={h} m={m}: |S|={len(S)}, COVERS holdouts: {covers}")
