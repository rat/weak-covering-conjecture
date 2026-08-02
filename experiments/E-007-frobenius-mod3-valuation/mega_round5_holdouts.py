"""
Round 5 (mega cycle) follow-up: find the actual diagonal-strata holdouts at l=7 and l=8 (the
residues NOT covered until the last stratum is added, analogous to {262,505} at l=6), then test
whether the pre-registered h=1,m=2 pair (P_l,Q_l) actually repairs them.
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image
from fractions import Fraction

def frac_mod(frac, mod):
    num, den = frac.numerator, frac.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def H_h1(r, cs):
    total = Fraction(2) ** (r - 1) - Fraction(1, 2)
    for q, cq in enumerate(cs, start=1):
        total += Fraction(3, 2) * Fraction(2) ** (q - 1) * (Fraction(3, 2) ** cq - 1)
    return total

def F_from_H(j, Hval):
    return Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Hval

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12}

for l in (7, 8):
    j = JSTAR[l]
    mod_l = 3**l
    units = set(x for x in range(mod_l) if x % 3 != 0)

    covered = set()
    used_d = []
    holdouts_before_last = None
    for d in range(1, l):
        S = stratum_image(l, j, d) & units
        prev_covered = set(covered)
        covered |= S
        used_d.append(d)
        if covered == units:
            holdouts_before_last = units - prev_covered
            print(f"l={l} j={j}: full coverage reached at d={used_d}, last stratum d={d} added "
                  f"{len(holdouts_before_last)} previously-missing residues: "
                  f"{sorted(holdouts_before_last)}")
            break
    else:
        print(f"l={l}: incomplete after all d, no holdout isolated")
        continue

    # test whether the pre-registered h=1,m=2 pair (P_l,Q_l) at SOME common r hits these holdouts
    P_l = (l - 2, l - 3)
    Q_l = (l - 4, l - 4)
    print(f"  testing h=1,m=2 pair P={P_l} Q={Q_l} against these holdouts...")
    found = {}
    for r in range(2, j + 1):
        for pair_name, pair in (("P", P_l), ("Q", Q_l)):
            Hval = H_h1(r, list(pair))
            F = F_from_H(j, Hval)
            res = frac_mod(F, mod_l)
            if res in holdouts_before_last:
                found.setdefault(res, []).append((r, pair_name, pair))
    for res in sorted(holdouts_before_last):
        print(f"    residue {res}: witnesses via (P,Q) pair = {found.get(res, 'NOT FOUND')}")
    print()
