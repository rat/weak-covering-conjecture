"""
A2/B3 check (H-003 round 24, GAP A item 2 / GAP B item 3): occupancy of shallow
residue cylinders mod 3^r under the exact critical-budget ensemble (j = j*(l)).

Key trick: reduction mod 3^r only depends on the r LARGEST chosen exponents (the
low-order rank positions in this project's value = sum_i 2^{a_i} 3^i convention),
so the same validated rotation-DP that computes exact tuple counts mod 3^l can be
run with modulus n = 3^r instead, for r << l. This makes the array O(3^r), not
O(3^l), so l can be pushed far beyond what full-modulus DPs (H-002's dp_extend.py)
can reach in memory -- the cost no longer depends on l except through the number of
DP steps (O(l) rank layers x O(l+j) exponent candidates), independent of the array
size. Sanity-checked to exactly reproduce the full-modulus DP's own mod-3^r
aggregation before trusting it (see check_reduced_modulus_dp below).

q_{l,r} := (2*3^(r-1)) * min_b p_{l,r}(b) / total, the quantity A2/B3 both target
(a starved cylinder means q is very small; B3 wants a bound on how small).

Finding (l=4..23, exact j*(l), r up to 12): -log(q_{l,r}) grows roughly linearly in
r and is largely INDEPENDENT of l once l is comfortably larger than r (checked at
fixed r, at r~sqrt(l), and at fixed ratios r/l~0.33 and ~0.7). No sign of q decaying
exponentially in l at any tested scaling -- weighs against A2's refutation hope in
this range, and is suggestive (not proof) for B3: if q_{l,r} ~ exp(-c*r) holds
robustly as r grows with l (r = l^delta), it would give a much stronger e(l) lower
bound than the "sub-polynomial" case B3 asked for. NOT confirmed past l=23: a naive
attempt to extrapolate j for l>23 (constant offset, or the proven-safe rho_13 bound
with a small guessed constant) undershoots the true j*(l) and breaks the covering
property itself well before l=80 (min_occ hits 0, i.e. q=0). Extending this
analysis past l=23 needs a properly justified j(l) schedule, not naive
extrapolation -- deferred, not attempted further here.
"""
import numpy as np
import gc
import math
import time

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19, 15: 20, 16: 20, 17: 21, 18: 22, 19: 23, 20: 24,
              21: 25, 22: 26, 23: 27}


def compute_counts_dp(l, j, n):
    """Exact count, per residue mod n, of admissible l-term tuples (rotation-DP,
    validated in H-002's dp_extend.py against brute force for l<=11). n need not
    be 3^l: any modulus works, since the DP tracks partial sums mod n directly."""
    max_exp = l + j - 1
    state = [np.zeros(n, dtype=np.int64) for _ in range(l + 1)]
    state[0][0] = 1
    for v in range(max_exp, -1, -1):
        p2 = pow(2, v, n)
        for c in range(l - 1, -1, -1):
            if not state[c].any():
                continue
            p3 = pow(3, c, n)
            offset = (p2 * p3) % n
            state[c + 1] += np.roll(state[c], offset)
    result = state[l].copy()
    del state
    gc.collect()
    return result


def check_reduced_modulus_dp():
    """Sanity check: reduced-modulus DP must exactly match full-modulus DP,
    aggregated by residue mod 3^r. Run before trusting anything below."""
    for l in [6, 7, 8]:
        j = JSTAR_FULL[l]
        full = compute_counts_dp(l, j, 3 ** l)
        for r in [1, 2, 3]:
            if r >= l:
                continue
            mr = 3 ** r
            agg_full = full.reshape(3 ** l // mr, mr).sum(axis=0)
            reduced = compute_counts_dp(l, j, mr)
            assert np.array_equal(agg_full, reduced), f"MISMATCH l={l} r={r}"
    print("sanity check passed: reduced-modulus DP == aggregated full-modulus DP")


def q_lr(l, j, r):
    mr = 3 ** r
    counts = compute_counts_dp(l, j, mr)
    total = int(counts.sum())
    units = [b for b in range(mr) if b % 3 != 0]
    min_occ = int(counts[units].min())
    return (2 * 3 ** (r - 1)) * min_occ / total, total, min_occ


if __name__ == "__main__":
    check_reduced_modulus_dp()
    t0 = time.time()
    print(f"\n{'l':>3} {'r':>3} {'-log(q_lr)/l':>13}")
    for l in range(4, 24):
        j = JSTAR_FULL[l]
        for r in range(1, min(l, 11)):
            q, total, min_occ = q_lr(l, j, r)
            nz = -math.log(q) / l if q > 0 else float("inf")
            print(f"{l:>3} {r:>3} {nz:>13.4f}")
    print(f"\n({time.time() - t0:.1f}s)")
