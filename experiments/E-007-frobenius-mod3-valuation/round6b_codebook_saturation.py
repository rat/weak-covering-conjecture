"""
The actual Durfee codebook-saturation test (round 1's original proposal), now that the full
decomposition formula (including the derived C_d) is confirmed exact.

For fixed (l, j, d): every partition lambda in the j x j square with Durfee size EXACTLY d
decomposes as (A, B) with A a d x (j-d) partition, B a (j-d) x d partition. Then

  F_j(lambda) mod 3^l = u_A + 3^d * ((high_A + high_B) mod 3^(l-d))

where u_A = (base-terms) mod 3^d depends only on A, high_A is A's contribution above digit d,
and high_B = 2^(j-d)*H(B) mod 3^(l-d) depends only on B.

Sufficient condition for this Durfee-d stratum ALONE to cover every unit mod 3^l: for every u
actually achieved by some A, {high_A values for that u} + {all high_B values} = Z/3^(l-d).
"""
from fractions import Fraction
from itertools import combinations_with_replacement

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
    """frac has a power-of-2 denominator; mod is a power of 3; 2 is invertible mod 3^k."""
    num, den = frac.numerator, frac.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def partitions_in_box(rows, cols):
    """all weakly-decreasing partitions with `rows` parts (allowing 0), each part <= cols."""
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

def run(l, j, d):
    mod_l = 3**l
    mod_d = 3**d
    mod_hi = 3**(l - d)
    Cd = C(d)
    base = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Cd

    # A ranges over d-row partitions, each part <= j-d (top-right arm)
    u_to_highA = {}
    for A in partitions_in_box(d, j - d):
        HA = H(d, A)
        val = base + Fraction(2)**(d + j) * HA
        u = frac_mod(val, mod_d) if mod_d > 1 else 0
        high = frac_mod((val - u) / mod_d if mod_d > 1 else val, mod_hi) if mod_hi > 1 else 0
        u_to_highA.setdefault(u, set()).add(high)

    # B ranges over (j-d)-row partitions, each part <= d (bottom-left arm)
    B_set = set()
    for B in partitions_in_box(j - d, d):
        HB = H(j - d, B)
        val = Fraction(2)**(j - d) * HB
        high = frac_mod(val, mod_hi) if mod_hi > 1 else 0
        B_set.add(high)

    print(f"  l={l} j={j} d={d}: {len(u_to_highA)} distinct u values (mod 3^{d}), "
          f"|B_set|={len(B_set)} (of {mod_hi} possible mod 3^{l-d})")

    saturated_count = 0
    not_saturated = []
    for u, highA_set in u_to_highA.items():
        sumset = set()
        for a in highA_set:
            for b in B_set:
                sumset.add((a + b) % mod_hi)
        if len(sumset) == mod_hi:
            saturated_count += 1
        else:
            not_saturated.append((u, len(highA_set), len(sumset), mod_hi))

    print(f"    saturated for {saturated_count}/{len(u_to_highA)} achieved u values "
          f"(need mod_hi={mod_hi} each)")
    if not_saturated:
        print(f"    NOT saturated examples (u, |A_{{d,u}}|, |sumset|, target): {not_saturated[:5]}")
    return saturated_count, len(u_to_highA)

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15}

print("=== Durfee codebook-saturation test, real (l,j), several d values ===")
for l in range(2, 7):
    j = JSTAR[l]
    for d in range(1, j):
        run(l, j, d)
    print()
