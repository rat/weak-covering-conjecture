"""
Deep dive on Gemini's round-25 item 9 ("Continuous Order-Simplex Geometry and Isoperimetric
Pushforward Measures"), requested explicitly by the researcher after the first pass only checked
the item's basic volume-scale necessary condition (which passed comfortably). This script checks
the actual claim: that once Vol(Delta_{j,l}) >> 3^l*log(3^l), Milman's isoperimetric machinery
forces the pushforward measure to cover (Z/3^lZ)^*, i.e. that a FIXED constant multiple of
3^l*log(3^l) is a correct (eventually sufficient) covering threshold.

Method: for each l with a known exact j*(l) (l=1..23), compute Vol(Delta_{j,l}) = C(j+l,j) (the
number of admissible rank-ordered exponent tuples) at j=j*(l)-1, i.e. the largest budget at which
covering has NOT yet happened. The minimum constant C(l) for which the claimed threshold would
correctly predict "not yet covering" at this point is Vol(Delta_{j*(l)-1,l}) / (3^l*ln(3^l)) --
any FIXED C below this value would have (wrongly) predicted covering before it actually happened.

Result: C(l) is NOT bounded. It grows from under 1 (l<=4) through ~1-10 (l=5..19) to ~24.5 at
l=23, and is still climbing with no sign of leveling off over the available range. This means no
single fixed constant C makes "Vol(Delta_{j,l}) > C*3^l*log(3^l) implies covering" correct for all
l: for large enough l, this criterion would incorrectly predict covering strictly before it
actually happens, by a widening margin. Separately, the excess budget the isoperimetric threshold
implies (j_isoperi(l) - j_pigeon(l), where j_pigeon is the pure pigeonhole/domain-size-only bound)
stays essentially flat (3-4) across l=5..23, while the TRUE excess (j*(l) - j_pigeon(l)) grows
steadily (4 to 9 over the same range) -- the isoperimetric threshold, taken as stated with any
fixed multiplier, is cleared well before actual covering, by a widening gap.

This does not disprove that some corrected, dimension-aware version of Milman's machinery could
work (the simplex's actual dimension j*(l)+1 grows with l, and genuine isoperimetric/concentration
constants often do carry dimension-dependent factors that Gemini's stated formula, a plain
`3^l*log(3^l)` with no explicit dimension term, omits). That corrected, harder version was not
attempted here -- it would need real new isoperimetric-geometry derivation, not a data check. What
IS established: item 9's claim exactly as stated, a fixed-constant volume threshold, is refuted by
this project's own exact j*(l) table.
"""
from math import comb, log

DATA = [
    (1, 1), (2, 4), (3, 6), (4, 7), (5, 9), (6, 10), (7, 11), (8, 12),
    (9, 13), (10, 15), (11, 16), (12, 17), (13, 18), (14, 19), (15, 20),
    (16, 20), (17, 21), (18, 22), (19, 23), (20, 24), (21, 25), (22, 26),
    (23, 27),
]


def j_pigeon(l, target):
    j = 0
    while comb(j + l, j) < target:
        j += 1
    return j


if __name__ == "__main__":
    print(f"{'l':>3} {'j*-1':>5} {'Vol(j*-1)':>18} {'3^l ln3^l':>15} {'min_C_needed':>13}")
    for l, jstar in DATA:
        codomain = 3 ** l
        j_before = jstar - 1
        vol_before = comb(j_before + l, j_before) if j_before >= 0 else 0
        thresh = codomain * log(codomain) if codomain > 1 else codomain
        print(f"{l:>3} {j_before:>5} {vol_before:>18} {thresh:>15.3e} {vol_before/thresh:>13.3f}")

    print()
    print(f"{'l':>3} {'j*(l)':>6} {'j_pigeon':>9} {'excess_true':>12} {'j_isoperi(C=1)':>15} {'excess_isoperi':>15}")
    for l, jstar in DATA:
        codomain = 3 ** l
        jp = j_pigeon(l, codomain)
        ji = j_pigeon(l, codomain * log(codomain) if codomain > 1 else codomain)
        print(f"{l:>3} {jstar:>6} {jp:>9} {jstar-jp:>12} {ji:>15} {ji-jp:>15}")
