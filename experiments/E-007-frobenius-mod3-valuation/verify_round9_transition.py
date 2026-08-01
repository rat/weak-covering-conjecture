"""
Round-9 follow-up: run Codex's proposed "defect-transition / repair" test, the highest-value
final computation it suggested, using our own already-verified DP tools rather than waiting
for round 10.

For each l (parent level, budget j_l=j*(l)) and l+1 (child level, budget j_{l+1}=j*(l+1)):
  - Compute mask_l(r) for every r mod 3^l using j_l-term tuples (mod 3^(l+1)): which of the 3
    next-digit lifts a=0,1,2 are achieved. This classifies every child x=r+a*3^l mod 3^(l+1) as
    "attained" (a in mask) or "missing" (a not in mask) at the j_l budget.
  - Compute mask_{l+1}(x) for every x mod 3^(l+1) using j_{l+1}-term tuples (mod 3^(l+2)): since
    j_{l+1} covers ALL of mod 3^(l+1) by definition, every x gets a real mask size (1, 2, or 3)
    at this bigger budget.
  - Cross-tabulate: among x's that were "missing" at level l, what's the distribution of their
    own mask sizes at level l+1? Compare to x's that were "attained" at level l.

This directly tests Codex's three scenarios: best case (missing x's repair to mostly mask3),
danger case (missing x's stay disproportionately mask1/2, a persistent defect type), or
intermediate (some bounded repair cost).
"""
import numpy as np

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

def fiber_counts_dp(ell, j):
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

def mask_dict(ell, j):
    """mask[r] = frozenset of digits a in {0,1,2} achieved among j-term tuples' values mod
    3^(ell+1), for parent r mod 3^ell (only unit r)."""
    mod_lo = 3**ell
    mod_hi = 3**(ell + 1)
    counts_hi = fiber_counts_dp(ell + 1, j)
    masks = {}
    for r in range(mod_lo):
        if r % 3 == 0:
            continue
        present = frozenset(a for a in range(3) if counts_hi[r + a * mod_lo] > 0)
        masks[r] = present
    return masks

print("=== Defect-transition / repair test: old (level l, budget j*(l)) vs new (level l+1, budget j*(l+1)) ===\n")

for l in range(2, 8):
    lp1 = l + 1
    jl = JSTAR[l]
    jlp1 = JSTAR[lp1]
    mod_l = 3**l
    mod_lp1 = 3**lp1

    masks_l = mask_dict(l, jl)          # parent masks at level l (budget j*(l))
    masks_lp1 = mask_dict(lp1, jlp1)    # "parent" masks at level l+1 (budget j*(l+1)), i.e. each
                                          # x mod 3^(l+1) treated as its own parent for children
                                          # mod 3^(l+2)

    # classify every x mod 3^(l+1) (unit) as attained/missing at level l, and get its own
    # mask size at level l+1
    counts = {
        ("attained", 1): 0, ("attained", 2): 0, ("attained", 3): 0,
        ("missing", 1): 0, ("missing", 2): 0, ("missing", 3): 0,
    }
    old_parent_type_breakdown = {}  # (old_parent_mask_size, status) -> count of new mask sizes
    for r, mask in masks_l.items():
        for a in range(3):
            x = r + a * mod_l
            if x % 3 == 0:
                continue  # x itself must be a unit mod 3 to be a valid unit mod 3^(l+1)
            status = "attained" if a in mask else "missing"
            new_mask = masks_lp1.get(x)
            if new_mask is None:
                continue  # x not a unit, skip (shouldn't happen given the check above)
            new_size = len(new_mask)
            counts[(status, new_size)] += 1

            key = (len(mask), status)
            old_parent_type_breakdown.setdefault(key, {1: 0, 2: 0, 3: 0})
            old_parent_type_breakdown[key][new_size] += 1

    total_missing = sum(counts[("missing", s)] for s in (1, 2, 3))
    total_attained = sum(counts[("attained", s)] for s in (1, 2, 3))

    print(f"--- l={l} (budget {jl}) -> l+1={lp1} (budget {jlp1}) ---")
    print(f"  MISSING children at level l (n={total_missing}): "
          f"new mask1={counts[('missing',1)]} mask2={counts[('missing',2)]} mask3={counts[('missing',3)]}"
          + (f"  (frac mask3={counts[('missing',3)]/total_missing:.3f})" if total_missing else ""))
    print(f"  ATTAINED children at level l (n={total_attained}): "
          f"new mask1={counts[('attained',1)]} mask2={counts[('attained',2)]} mask3={counts[('attained',3)]}"
          f"  (frac mask3={counts[('attained',3)]/total_attained:.3f})")
    print()

print("=== Full breakdown by old-parent-mask-size and attained/missing status ===")
for l in range(2, 8):
    lp1 = l + 1
    jl = JSTAR[l]
    jlp1 = JSTAR[lp1]
    mod_l = 3**l
    masks_l = mask_dict(l, jl)
    masks_lp1 = mask_dict(lp1, jlp1)
    breakdown = {}
    for r, mask in masks_l.items():
        for a in range(3):
            x = r + a * mod_l
            if x % 3 == 0:
                continue
            status = "attained" if a in mask else "missing"
            new_mask = masks_lp1.get(x)
            if new_mask is None:
                continue
            key = (len(mask), status)
            breakdown.setdefault(key, {1: 0, 2: 0, 3: 0})
            breakdown[key][len(new_mask)] += 1
    print(f"l={l}:")
    for key in sorted(breakdown):
        old_size, status = key
        d = breakdown[key]
        total = sum(d.values())
        print(f"  old_mask_size={old_size} status={status:>9}  n={total:>5}  "
              f"new: mask1={d[1]:>4} mask2={d[2]:>4} mask3={d[3]:>4}")
