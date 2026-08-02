"""
Round 26 (mega cycle): test Codex's required Witt-vector deliverable directly. Claim to check:
does varying one row a_r (holding earlier rows fixed) vary the row's own mod-3 contribution
h_r(a_r) = sum_{c=1}^{a_r} 2^(c-r-1) through all three residues {0,1,2}?

Derived closed form by hand: sum_{c=1}^{x} 2^c = 2^(x+1)-2, so mod 3 (2 = -1 mod 3) this is 0 if
x even, 2 if x odd. Hence h_r(x) mod 3 = 2^(-r) * (0 or 2) mod 3 = 0 if x even, else 2^(-r) mod 3
(= 1 if r even, 2 if r odd). Only ever 2 of 3 residues -- generalizes round 13's parity lemma
(there stated only for r=1) to every row.
"""
from fractions import Fraction
import random

def h_r(r, x):
    total = Fraction(0)
    for c in range(1, x + 1):
        total += Fraction(2) ** (c - r - 1)
    return total

def frac_mod3(fr):
    num, den = fr.numerator, fr.denominator
    inv = pow(den, -1, 3)
    return (num * inv) % 3

def predicted(r, x):
    if x % 2 == 0:
        return 0
    return 1 if r % 2 == 0 else 2

for r in range(1, 6):
    residues = sorted(set(frac_mod3(h_r(r, x)) for x in range(0, 12)))
    print(f"r={r}: residues hit by h_r(x) mod 3, x=0..11: {residues}")

random.seed(0)
mismatches = 0
for _ in range(5000):
    r = random.randint(1, 40)
    x = random.randint(0, 60)
    actual = frac_mod3(h_r(r, x))
    pred = predicted(r, x)
    if actual != pred:
        mismatches += 1
        print("MISMATCH", r, x, actual, pred)
print(f"5000 random trials, mismatches: {mismatches}")
