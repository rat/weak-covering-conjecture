"""
Round-8 follow-up: Codex correctly caught that our round-7 "cheap same-fiber pair" probe was a
false positive -- it was exactly the trivial family A_j=(0,...,j-1), B_j=(1,...,j-1,j+1), whose
difference is EXACTLY 3^j, which (since j=j*(l) > l always) vanishes mod 3^(l+1) too, giving NO
real digit information at all.

The real test Codex specified: at the REAL covering budget j=j*(l), compute the lift-mask
M_l(r) = { (P(A;2)-r)/3^l mod 3 : tuple A with P(A;2) = r mod 3^l }, i.e. group tuples of size
j*(l) by their residue mod 3^l, and see how many of the 3 possible "next digit" values (mod
3^(l+1)) actually occur for each residue class. |M_l(r)|=3 (a genuine 3-way split) is the
natural-data analogue of Codex's proposed "whole-tuple triple" -- found directly, not
hand-constructed.

Uses the already-verified transfer-matrix DP (cross-checked against brute force in round 3),
extended one level up (mod 3^(l+1)) at j=j*(l).
"""
import numpy as np
from math import comb

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

def fiber_counts_dp(ell, j):
    """Exact fiber counts mod 3^ell for j-term tuples (verified against brute force, round 3)."""
    mod = 3**ell
    dp = np.zeros((j + 1, mod), dtype=np.int64)
    dp[0, 0] = 1
    pow3 = [pow(3, k, mod) for k in range(j)]
    p2 = pow(2, 2*j - 1, mod)
    inv2 = pow(2, -1, mod)
    for t in range(2*j):
        for k in range(min(j - 1, t), -1, -1):
            dp[k + 1] += np.roll(dp[k], (pow3[k] * p2) % mod)
        p2 = (p2 * inv2) % mod
    return dp[j]

print("=== Real lift-mask test: j=j*(l), residues mod 3^l, split mod 3^(l+1) ===")
print(f"{'l':>3} {'j':>4} {'units_mod':>10}   {'mask1':>6} {'mask2':>6} {'mask3':>6}   {'frac_mask3':>10}")

for l in range(2, 9):  # mod 3^(l+1) DP: for l=8 that's 3^9=19683, still cheap
    j = JSTAR[l]
    counts_hi = fiber_counts_dp(l + 1, j)  # exact fiber counts mod 3^(l+1)
    mod_hi = 3**(l + 1)
    mod_lo = 3**l
    units_lo = 2 * 3**(l - 1)

    mask_sizes = {1: 0, 2: 0, 3: 0}
    for r in range(mod_lo):
        if r % 3 == 0:
            continue  # not a unit mod 3^l, skip (F never lands here anyway)
        digits_present = set()
        for t in range(3):
            x = r + t * mod_lo
            if x < mod_hi and counts_hi[x] > 0:
                digits_present.add(t)
        if not digits_present:
            continue  # shouldn't happen at j=j*(l) since it covers mod 3^l by definition
        mask_sizes[len(digits_present)] += 1

    total_present = sum(mask_sizes.values())
    frac3 = mask_sizes[3] / total_present if total_present else 0
    print(f"{l:>3} {j:>4} {units_lo:>10}   {mask_sizes[1]:>6} {mask_sizes[2]:>6} {mask_sizes[3]:>6}   {frac3:>10.3f}")
