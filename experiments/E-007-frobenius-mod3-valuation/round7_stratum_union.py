"""
Round 7 follow-up: compute the ACTUAL stratum images S_d (subsets of Z/3^l, not just the
conditional-saturation-rate proxy from round 6), and their exceptional complements E_d, for
l=6, j=10 (the richest tested case), across d=3,4,5 -- then check pairwise/triple overlaps of
the E_d's, per Codex's specification, to see whether the union covers everything.
"""
from fractions import Fraction

def C(d):
    return (Fraction(2) ** d - 1) * (Fraction(3, 2) ** d - 1)

def H(a, lam_prefix):
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

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

def stratum_image(l, j, d):
    mod_l = 3**l
    mod_d = 3**d
    mod_hi = 3**(l - d)
    Cd = C(d)
    base = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Cd

    u_to_highA = {}
    for A in partitions_in_box(d, j - d):
        HA = H(d, A)
        val = base + Fraction(2)**(d + j) * HA
        u = frac_mod(val, mod_d)
        high = frac_mod((val - u) / mod_d, mod_hi)
        u_to_highA.setdefault(u, set()).add(high)

    B_set = set()
    for B in partitions_in_box(j - d, d):
        HB = H(j - d, B)
        val = Fraction(2)**(j - d) * HB
        high = frac_mod(val, mod_hi)
        B_set.add(high)

    S = set()
    for u, highA_set in u_to_highA.items():
        for a in highA_set:
            for b in B_set:
                high = (a + b) % mod_hi
                residue = (u + mod_d * high) % mod_l
                S.add(residue)
    return S

l, j = 6, 10
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)
n_units = len(units)

print(f"=== Actual stratum images S_d and exceptional sets E_d (restricted to units), l={l} j={j} ===")
Ss = {}
Es = {}
for d in (3, 4, 5):
    S = stratum_image(l, j, d)
    S_units = S & units
    E = units - S_units
    Ss[d] = S_units
    Es[d] = E
    print(f"  d={d}: |S_d ∩ units|={len(S_units)} / {n_units} units "
          f"({100*len(S_units)/n_units:.1f}%), |E_d|={len(E)}")

print("\n=== Pairwise and triple overlaps of exceptional sets ===")
ds = list(Es.keys())
for i in range(len(ds)):
    for k in range(i + 1, len(ds)):
        d1, d2 = ds[i], ds[k]
        overlap = Es[d1] & Es[d2]
        print(f"  |E_{d1} ∩ E_{d2}| = {len(overlap)}")

triple = Es[3] & Es[4] & Es[5]
print(f"  |E_3 ∩ E_4 ∩ E_5| = {len(triple)}")

union_S = Ss[3] | Ss[4] | Ss[5]
print(f"\n  |S_3 ∪ S_4 ∪ S_5| = {len(union_S)} / {n_units} units "
      f"({100*len(union_S)/n_units:.2f}%)")
if len(union_S) == n_units:
    print("  FULL COVERAGE achieved by the union of these three strata.")
else:
    still_missing = units - union_S
    print(f"  Still missing {len(still_missing)} units: {sorted(still_missing)[:20]}")
