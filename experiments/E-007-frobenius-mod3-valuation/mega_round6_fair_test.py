"""
Round 6 (mega cycle): the fair, apples-to-apples test Codex specified.

R_l = units \\ (S_{l,3} u S_{l,4} u S_{l,5})  (the SAME high-strata-first setup used for l=6)

For l=6,7,8: report R_l, which residues in R_l are hit by the prescribed h=1,m=2 (P_l,Q_l) pair,
what's left after adding that pair, and whether hits occur as tau_l-paired orbits
(tau_l(x) = x + (-1)^(l-1)*3^(l-1) mod 3^l).

Also: the m=1 negative control, H(r, P_l^(1)) - H(r, Q_l) == 0 (mod 3^l) for P_l^(1)=(l-3,l-3),
Q_l=(l-4,l-4), tested EXHAUSTIVELY over all admissible common r (not just a few samples).
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

print("=== Fair test: R_l = units \\ (S_{l,3} u S_{l,4} u S_{l,5}), l=6,7,8 ===")
for l in (6, 7, 8):
    j = JSTAR[l]
    mod_l = 3**l
    units = set(x for x in range(mod_l) if x % 3 != 0)

    S345 = set()
    for d in (3, 4, 5):
        S345 |= stratum_image(l, j, d) & units
    R_l = units - S345
    print(f"\nl={l} j={j}: R_l = units \\ (S3 u S4 u S5) = {sorted(R_l)} (n={len(R_l)})")

    P_l = (l - 2, l - 3)
    Q_l = (l - 4, l - 4)
    hits = {}
    for r in range(2, j + 1):
        for name, pair in (("P", P_l), ("Q", Q_l)):
            Hval = H_h1(r, list(pair))
            F = F_from_H(j, Hval)
            res = frac_mod(F, mod_l)
            if res in R_l:
                hits.setdefault(res, []).append((r, name))

    print(f"  residues in R_l hit by (P_l,Q_l) pair: {sorted(hits.keys())}")
    left_after = R_l - set(hits.keys())
    print(f"  left after adding the pair: {sorted(left_after)} (n={len(left_after)})")

    tau = ((-1) ** (l - 1)) * 3 ** (l - 1)
    print(f"  tau_l(x) = x + ({tau}) mod {mod_l}")
    for res in sorted(hits.keys()):
        partner = (res + tau) % mod_l
        partner_neg = (res - tau) % mod_l
        in_R = partner in R_l or partner_neg in R_l
        print(f"    {res}: tau-partner={partner}, -tau-partner={partner_neg}, "
              f"partner also in R_l: {in_R}")

print("\n=== m=1 negative control: H(r,P^(1)) - H(r,Q) == 0 (mod 3^l), EXHAUSTIVE over r ===")
for l in (5, 6, 7, 8):
    j = JSTAR[l]
    mod_l = 3**l
    Q_l = (l - 4, l - 4)
    P1_l = (l - 3, l - 3)
    all_zero = True
    nonzero_examples = []
    for r in range(2, j + 1):
        Hp = H_h1(r, list(P1_l))
        Hq = H_h1(r, list(Q_l))
        diff_mod = frac_mod(Hp - Hq, mod_l)
        if diff_mod != 0:
            all_zero = False
            nonzero_examples.append((r, diff_mod))
    status = "CONTROL HOLDS (all zero)" if all_zero else f"CONTROL FALSIFIED, e.g. {nonzero_examples[:3]}"
    print(f"  l={l}: P^(1)={P1_l} Q={Q_l}, r=2..{j} exhaustive: {status}")
