"""
Round 10 (mega cycle): proof-oriented 3-adic trie certificate for R_4, per Codex's spec.

At each depth a=1..5, list cylinder (residue mod 3^a) occupancies for R_4, the collision
increment sum_v C(n_v,2) per depth (decomposing T), identify heavy cylinders, and for the
heaviest, trace WHY the low-stratum (d<=4) construction misses every element in that cylinder.
"""
from math import comb

R4 = [40, 76, 121, 148, 152, 157, 175, 215, 229, 238, 265, 274, 310, 337, 445, 472, 508, 562,
      580, 607, 647, 688, 715, 724]

print(f"R_4 (n={len(R4)}): {R4}\n")

T_total = 0
for a in range(1, 6):
    mod = 3**a
    buckets = {}
    for x in R4:
        buckets.setdefault(x % mod, []).append(x)
    increment = sum(comb(len(v), 2) for v in buckets.values())
    T_total += increment
    nonsingleton = {k: v for k, v in buckets.items() if len(v) > 1}
    print(f"depth a={a} (mod {mod}): {len(buckets)} occupied cylinders, "
          f"collision increment sum C(n,2) = {increment}")
    for k, v in sorted(nonsingleton.items(), key=lambda kv: -len(kv[1])):
        print(f"    cylinder {k} (mod {mod}): {len(v)} points -> {v}")
print(f"\nTotal T (sum of increments a=1..5) = {T_total}  (should match T_obs=569)")

# Identify the heaviest cylinder at each depth, and trace its base-3 digits
print("\n=== Heaviest cylinder trace ===")
mod5 = 3**5  # =243, the deepest level tested (q=1..5, l=6 so max depth before hitting individual
              # residues is 5; recall units are mod 3^6=729, so depth 5 still groups 3 elements
              # each typically)
buckets5 = {}
for x in R4:
    buckets5.setdefault(x % mod5, []).append(x)
heaviest_key = max(buckets5, key=lambda k: len(buckets5[k]))
print(f"heaviest depth-5 cylinder: residue {heaviest_key} mod {mod5}, "
      f"members: {buckets5[heaviest_key]}")

# base-3 digit expansion of the heaviest cylinder's representative
def to_base3(n, digits=6):
    out = []
    for _ in range(digits):
        out.append(n % 3)
        n //= 3
    return list(reversed(out))

for x in R4:
    print(f"  {x} mod 729 -> base3 digits (MSB first): {to_base3(x)}")
