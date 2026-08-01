"""
Round-4 follow-up (before round 5): actually run the "rectangle-coverage test" Codex
proposed in round 3 and reiterated in round 4, rather than just estimating it by hand.

For real (l, j) pairs (j = j*(l) or j*(l)-1, the real R_{j-1,j} budget), exhaustively try
EVERY root A in [1, 2j-1] and EVERY one of the 3^(l-1) digit sequences of the two-state
transducer (child(P,d), gap-5 revise-then-append gadget), keep only leaves that are valid
j-term-extendable (last exponent >= j-l, so there's room for a canonical decreasing tail
down to 0), and record which residues mod 3^l are actually achieved. Compare to the true
unit count 2*3^(l-1).

This directly answers, computationally, whether this specific transducer family can realize
enough of the rectangle to matter, instead of relying on the worst-case resource-accounting
argument (root >= 5*(l-1), which is far bigger than the real budget 2j-1 for realistic j,l).
"""
from itertools import product

def build_leaf(A, digits):
    """digits: tuple of 0/1/2, length l-1. Returns the l-tuple of exponents, or None if
    any intermediate exponent goes negative (invalid)."""
    P = (A,)
    for d in digits:
        a = P[-1]
        new_a = a + 2 * d
        new_b = a - 5 + 2 * d
        if new_b < 0:
            return None
        P = P[:-1] + (new_a, new_b)
    return P

def F(P):
    return sum(3**i * 2**a for i, a in enumerate(P))

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

print("=== Rectangle-coverage test: real (l, j) budgets, exhaustive over root A and digit path ===")
print(f"{'l':>3} {'j':>4} {'2j-1':>6} {'units_mod':>10} {'achieved':>9} {'frac':>7}   note")

for l in range(2, 9):
    for j_label, j in ((("j*(l)"), JSTAR[l]), ("j*(l)-1", JSTAR[l] - 1)):
        max_root = 2 * j - 1
        mod = 3**l
        units_total = 2 * 3**(l - 1)
        achieved = set()
        n_digit_seqs = 3**(l - 1)
        for digits in product(range(3), repeat=l - 1):
            for A in range(1, max_root + 1):
                leaf = build_leaf(A, digits)
                if leaf is None:
                    continue
                if not all(leaf[i] > leaf[i+1] for i in range(len(leaf) - 1)):
                    continue
                if leaf[-1] < j - l:
                    continue  # not enough room for a canonical decreasing tail to 0
                if leaf[0] > max_root:
                    continue  # exceeds rectangle's alpha_0 bound (redundant given A<=max_root)
                val = F(leaf) % mod
                achieved.add(val)
        frac = len(achieved) / units_total
        print(f"{l:>3} {j:>4} {max_root:>6} {units_total:>10} {len(achieved):>9} {frac:>7.3f}   ({j_label})")
