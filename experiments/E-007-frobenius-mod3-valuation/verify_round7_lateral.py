"""
Round-7 follow-up, before round 8.

1. Verify the core new lemma: ord_{3^l}(2) = q_l = 2*3^(l-1) (2 is a primitive root mod 3^l),
   the fact Codex's "orbit-return barrier" proof rests on.
2. A quick empirical probe of Codex's proposed remaining route ("whole-tuple additive
   cancellation"): for real R_{j-1,j} tuples (subsets of size j from {0,...,2j-1}), look at
   actual pairs of DISTINCT tuples that land in the SAME fiber mod 3^l (same residue), and
   measure the size of their symmetric difference (how many positions they actually differ
   in). If minimal same-fiber pairs already differ in very few positions, "short whole-tuple
   cancellation" is plausible and cheap; if they always differ in most positions, the idea is
   probably just as budget-starved as the earlier mechanisms.
"""
from itertools import combinations
from math import comb

# ---------- Check 1: ord_{3^l}(2) = q_l ----------

def mult_order(a, n):
    d = 1
    x = a % n
    while x != 1:
        x = (x * a) % n
        d += 1
        if d > n:
            return None
    return d

print("=== Check 1: ord_(3^l)(2) = q_l = 2*3^(l-1) ===")
ok = True
for l in range(1, 8):
    n = 3**l
    o = mult_order(2, n)
    expected = 2 * 3**(l-1)
    if o != expected:
        ok = False
        print(f"  MISMATCH l={l}: ord={o} expected={expected}")
print(f"  l=1..7: {'ALL MATCH (2 is a primitive root mod 3^l)' if ok else 'FAILURES'}")

# ---------- Check 2: same-fiber tuple pairs, symmetric-difference size ----------

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

def tuple_val_mod(combo, mod):
    alphas = sorted(combo, reverse=True)
    return sum(3**i * 2**a for i, a in enumerate(alphas)) % mod

print("\n=== Check 2: does a minimal (symdiff=2, single-swap) same-fiber pair exist? ===")
print("(targeted search: for each tuple, try swapping one exponent for one NOT currently used;")
print(" symdiff=2 is the theoretical minimum for two distinct same-size subsets)")
print(f"{'l':>3} {'j':>4} {'total_tuples':>12} {'found_symdiff2':>15}")

for l in range(2, 6):  # j=4,6,7,9 -> keep this cheap, it's O(C(2j,j)*j^2)
    j = JSTAR[l]
    mod = 3**l
    found = None
    for combo in combinations(range(2*j), j):
        S = set(combo)
        base_val = tuple_val_mod(combo, mod)
        not_in_S = [x for x in range(2*j) if x not in S]
        for out_elem in combo:
            for in_elem in not_in_S:
                new_combo = (S - {out_elem}) | {in_elem}
                if tuple_val_mod(tuple(new_combo), mod) == base_val:
                    found = (combo, tuple(sorted(new_combo)), base_val)
                    break
            if found:
                break
        if found:
            break
    status = "YES" if found else "no (none found)"
    print(f"{l:>3} {j:>4} {comb(2*j,j):>12} {status:>15}")
    if found:
        a, b, v = found
        print(f"      example: A={sorted(a, reverse=True)}  B={sorted(b, reverse=True)}  "
              f"both -> {v} (mod {mod})")
