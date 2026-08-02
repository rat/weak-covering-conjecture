"""
Round 12 (mega cycle) follow-up: before attempting Codex's full abstract "formal preimage
fiber" inversion machinery (hard to map onto our concrete forward-enumeration implementation
without guessing at correspondences), we found and verified a much simpler, direct algebraic
explanation for part of the picture: for DIAGONAL Durfee strata d>=2 (which is what I_1..I_4 in
our table actually are -- h=m=d), the "B" arm's prefactor (3/2)^d * 2^j has 3-adic valuation
EXACTLY d, so it vanishes mod 3^min(d,anything>=d) -- in particular mod 9 whenever d>=2. This
means for d=2,3,4, the achievable residue MOD 9 depends ONLY on A, not on B at all.

Verify this directly, then examine what values of A actually achieve residues 4 and 8 mod 9 at
d=3 and d=4 (the weak strata), to see if there's a further clean reason those are rare.
"""
from fractions import Fraction

def H(a, lam_prefix):
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

def C(d):
    return (Fraction(2) ** d - 1) * (Fraction(3, 2) ** d - 1)

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

l, j = 6, 8

print("=== Check: does varying B ever change the value mod 9, for d=1,2,3,4? ===")
for d in (1, 2, 3, 4):
    Cd = C(d)
    base = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Cd
    A_list = list(partitions_in_box(d, j - d))
    B_list = list(partitions_in_box(l - d, d))
    # for a FIXED A, check if val mod 9 is constant across all B
    A0 = A_list[0]
    HA0 = H(d, A0)
    vals_mod9 = set()
    for B in B_list:
        HB = H(l - d, B)
        val = base + Fraction(2)**d * HA0 + Fraction(3, 2)**d * HB
        vals_mod9.add(frac_mod(val, 9))
    print(f"  d={d}: fixing A, varying B over all {len(B_list)} choices -> "
          f"{len(vals_mod9)} distinct value(s) mod 9: {vals_mod9} "
          f"({'B has NO effect mod 9' if len(vals_mod9)==1 else 'B DOES affect mod 9'})")

print("\n=== For d=3,4: full distribution of achievable residues mod 9, varying A only ===")
for d in (3, 4):
    Cd = C(d)
    base = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Cd
    A_list = list(partitions_in_box(d, j - d))
    achieved = {}
    for A in A_list:
        HA = H(d, A)
        val = base + Fraction(2)**d * HA  # B-independent part (mod 9, since B vanishes)
        r9 = frac_mod(val, 9)
        achieved.setdefault(r9, []).append(A)
    print(f"\n  d={d}: {len(A_list)} total A choices, distribution over mod-9 residues:")
    for r9 in sorted(achieved):
        print(f"    residue {r9} mod 9: {len(achieved[r9])} A-values, e.g. {achieved[r9][0]}")
    print(f"    residues 4,8 achieved by any A? {4 in achieved}, {8 in achieved}")
