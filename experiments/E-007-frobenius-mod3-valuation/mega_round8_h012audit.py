"""
Round 8 (mega cycle): H-012 premise audit, per Codex's narrowed spec.

At (l,j)=(6,8) (note: j=8 < j*(6)=10, deliberately a SMALLER budget than the real covering
threshold, to test generality of the "d<=l-2 suffices" phenomenon away from the one j value
already tested):

1. Verify the d<=l-2 construction (union of strata d=1..4) is well-defined (already established
   machinery, just confirming it runs at this new (l,j)).
2. Bucket every residue by its "two-stratum signature": which of the TOP TWO effective strata
   (d=l-1=5, d=l=6, the ones EXCLUDED by d<=l-2) it belongs to. Four possible signatures:
   (in d=5? in d=6?) in {(F,F),(F,T),(T,F),(T,T)}.
3. "Status" = whether the residue IS covered by the low strata (d<=4) or not.
4. Falsification test: does any signature bucket contain BOTH statuses (covered and not-covered)?
   If yes, the "status determined by top-two-signature" compression claim is false.

Interpretation choices (recorded for the record, not verified by Codex before running): a
residue may be reachable by neither d<=4 nor d in {5,6} at this smaller j=8 (since j*(6)=10>8,
full coverage isn't guaranteed at j=8 even using ALL d); such residues are still assigned
status=NOT-covered (by low strata) and whatever signature their d=5/d=6 membership gives (possibly
(F,F) if unreachable by either).
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image

l, j = 6, 8
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)

low_strata_union = set()
for d in range(1, l - 1):  # d=1..4 (l-2=4)
    low_strata_union |= stratum_image(l, j, d) & units

S5 = stratum_image(l, j, 5) & units
S6 = stratum_image(l, j, 6) & units  # d=6=l, the "full" effective stratum

print(f"=== H-012 premise audit at (l,j)=({l},{j}), e=j-l={j-l} ===")
print(f"  |low_strata_union (d<=4)| = {len(low_strata_union)} / {len(units)} units")
print(f"  |S5| = {len(S5)}, |S6| = {len(S6)}")
print(f"  |S5 u S6| = {len(S5 | S6)}, full coverage via ALL d<=6? "
      f"{(low_strata_union | S5 | S6) == units}")

buckets = {}
for x in units:
    sig = (x in S5, x in S6)
    status = x in low_strata_union
    buckets.setdefault(sig, {True: 0, False: 0})[status] += 1

print("\n  signature (in S5?, in S6?) -> {status=covered_by_low: count, status=not_covered: count}")
compression_holds = True
for sig, counts in sorted(buckets.items()):
    both = counts[True] > 0 and counts[False] > 0
    if both:
        compression_holds = False
    print(f"    {sig}: covered={counts[True]}, not_covered={counts[False]}"
          f"{'  <-- MIXED, falsifies compression' if both else ''}")

print(f"\n  Compression claim (status determined by top-2-signature): "
      f"{'HOLDS at this (l,j)' if compression_holds else 'FALSIFIED at this (l,j)'}")
