"""
Round 4 (mega cycle): verify Codex's pre-registered falsifiable m=2 lift law:

  U(x,y) = (3/2)^x - 1 + 2*((3/2)^y - 1)
  U(a+2, a+1) - U(a, a) = (3/2)^(a+2)   for a >= 1

  P_l = (l-2, l-3), Q_l = (l-4, l-4)
  H(r, P_l) - H(r, Q_l) = (3/2)^(l-1) == (-1)^(l-1) * 3^(l-1)  (mod 3^l)

for l = 5, 6, 7, 8, at ANY common admissible r.
"""
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

def U(x, y):
    return (Fraction(3, 2) ** x - 1) + 2 * (Fraction(3, 2) ** y - 1)

print("=== Check A: general U(a+2,a+1) - U(a,a) = (3/2)^(a+2) ===")
ok = True
for a in range(1, 8):
    lhs = U(a + 2, a + 1) - U(a, a)
    rhs = Fraction(3, 2) ** (a + 2)
    if lhs != rhs:
        ok = False
        print(f"  MISMATCH a={a}: lhs={lhs} rhs={rhs}")
print(f"  a=1..7: {'ALL MATCH' if ok else 'FAILURES'}")

print("\n=== Check B: H(r,P_l) - H(r,Q_l) == (-1)^(l-1) * 3^(l-1) (mod 3^l), l=5..8, any r ===")
ok = True
for l in (5, 6, 7, 8):
    P = (l - 2, l - 3)
    Q = (l - 4, l - 4)
    mod = 3 ** l
    expected = ((-1) ** (l - 1)) * 3 ** (l - 1)
    expected_mod = expected % mod
    for r in (3, 5, 7, 10):  # a few arbitrary common admissible r values
        Hp = H_h1(r, list(P))
        Hq = H_h1(r, list(Q))
        diff = Hp - Hq
        diff_mod = frac_mod(diff, mod)
        if diff_mod != expected_mod:
            ok = False
            print(f"  MISMATCH l={l} r={r} P={P} Q={Q}: diff_mod={diff_mod} expected={expected_mod}")
        else:
            pass
    print(f"  l={l}: P={P} Q={Q} predicted_diff={('+' if expected>0 else '-')}3^{l-1}, "
          f"checked r in {{3,5,7,10}}: {'all match' if ok else 'MISMATCH (see above)'}")

print(f"\nOverall: {'ALL PREDICTIONS CONFIRMED' if ok else 'SOME PREDICTIONS FAILED'}")
