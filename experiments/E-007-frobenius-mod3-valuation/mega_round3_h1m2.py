"""
Round 3 (mega cycle): verify the collapsed h=1 rectangular-cut formula, and find actual (r,x,y)
witnesses for the l=6 holdouts 262 and 505 within the h=1,m=2 stratum, checking Codex's proposed
diagnostic: do they share the same top-row value r (clean tail-lift mechanism) or different r
(competing 2^r translates)?
"""
from fractions import Fraction

def frac_mod(frac, mod):
    num, den = frac.numerator, frac.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def H_full(a, lam_prefix):
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

def H_collapsed_h1(r, m, cs):
    """cs = [c_1,...,c_m], weakly decreasing, cs[0]<=l-1."""
    total = Fraction(2) ** (r - 1) - Fraction(1, 2)
    for q, cq in enumerate(cs, start=1):
        total += Fraction(3, 2) * Fraction(2) ** (q - 1) * (Fraction(3, 2) ** cq - 1)
    return total

print("=== Check 1: collapsed h=1 formula vs full H_{l,j} computation ===")
import random
random.seed(9)
ok = True
for trial in range(200):
    l = random.randint(2, 8)
    j = random.randint(l + 2, l + 8)
    m = random.randint(1, 5)
    r = random.randint(m, j)
    cs = sorted((random.randint(0, l - 1) for _ in range(m)), reverse=True)
    lam = [r] + list(cs)  # h=1: row1 = r, then the tail rows directly as B (since B_row = c_row
                            # only works if m>=... wait no, B here should be the ROW form, not
                            # conjugate; let's build lam directly instead: lam = [r] + B, where B
                            # is the (l-1)-row partition whose CONJUGATE is cs. Build B from cs.
    # cs are column heights (conjugate description): c_q = #rows with B_row >= q.
    # Reconstruct B (row form, length l-1, each part <= m) from cs (length m, each part <= l-1).
    B = [0] * (l - 1)
    for q, cq in enumerate(cs, start=1):
        for row in range(cq):
            B[row] += 1  # each row < cq gets a box in column q
    B = sorted(B, reverse=True)
    lam_full = [r] + B
    assert all(lam_full[i] >= lam_full[i+1] for i in range(len(lam_full)-1)), (lam_full, r, cs)

    lhs = H_full(l, lam_full)
    rhs = H_collapsed_h1(r, m, cs)
    if lhs != rhs:
        ok = False
        print(f"  MISMATCH l={l} j={j} r={r} cs={cs} lam={lam_full}: full={lhs} collapsed={rhs}")

print(f"  200 random trials: {'ALL MATCH' if ok else 'FAILURES FOUND'}")

# ---------- Check 2: find (r,x,y) witnesses for the l=6 holdouts within h=1,m=2 ----------

def F_from_H(j, Hval):
    return Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Hval

l, j = 6, 10
mod_l = 3**l
holdouts = {262, 505}
print(f"\n=== Check 2: (r,x,y) witnesses for holdouts within h=1,m=2 stratum, l={l} j={j} ===")
found = {}
for r in range(2, j + 1):
    for x in range(0, l):
        for y in range(0, x + 1):
            Hval = H_collapsed_h1(r, 2, [x, y])
            F = F_from_H(j, Hval)
            res = frac_mod(F, mod_l)
            if res in holdouts and res not in found:
                found[res] = (r, x, y)

for res in sorted(holdouts):
    print(f"  residue {res}: witness (r,x,y) = {found.get(res, 'NOT FOUND')}")

if len(found) == 2:
    (r1, x1, y1) = found[262]
    (r2, x2, y2) = found[505]
    print(f"\n  same r? {r1 == r2}  (r1={r1}, r2={r2})")
    print(f"  tail (x,y): 262->({x1},{y1})  505->({x2},{y2})")
