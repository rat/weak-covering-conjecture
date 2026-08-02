"""
Round 29 (mega cycle): verify Codex's asymptotic claims.

1. Exact identity: for a uniform partition lambda in an l x j box (l rows, each <= j), padded to
   l rows, with G0 = j - lambda_1, G1 = lambda_1 - lambda_2:
       #{G0=a, G1=b} = C(l+j-a-b-2, l-2)
   (via the standard bijection lambda -> l-subset of {0,...,l+j-1}, x_i = lambda_i + l - i).
   Check this against direct brute-force partition enumeration for small (l,j), and check the
   total over all (a,b) equals C(l+j,l) (total partitions in the box).

2. Asymptotic: Pr(G0=a,G1=b) -> alpha^2 * beta^(a+b) as l,j->infinity with j/l->rho, where
   alpha=1/(1+rho), beta=rho/(1+rho). Check numerically at moderately large l with j=round(rho*l),
   rho = log(3)/log(4).
"""
from math import comb, log
from fractions import Fraction

def partitions_in_box(rows, cols):
    if rows == 0:
        yield ()
        return
    def rec(remaining_rows, max_part):
        if remaining_rows == 0:
            yield ()
            return
        for first in range(max_part, -1, -1):
            for rest in rec(remaining_rows - 1, first):
                yield (first,) + rest
    yield from rec(rows, cols)

def brute_G0G1_counts(l, j):
    counts = {}
    for A in partitions_in_box(l, j):
        lam1 = A[0] if len(A) >= 1 else 0
        lam2 = A[1] if len(A) >= 2 else 0
        G0 = j - lam1
        G1 = lam1 - lam2
        counts[(G0, G1)] = counts.get((G0, G1), 0) + 1
    return counts

print("=== Part 1: exact identity check ===")
for (l, j) in [(4, 5), (5, 6), (6, 4), (3, 8)]:
    brute = brute_G0G1_counts(l, j)
    ok = True
    for (a, b), cnt in brute.items():
        n = l + j - a - b - 2
        predicted = comb(n, l - 2) if n >= l - 2 >= 0 else (1 if l - 2 == 0 and n >= 0 else 0)
        # handle l=2 edge case: C(n,0)=1 for n>=0
        if l - 2 == 0:
            predicted = 1 if n >= 0 else 0
        elif n < l - 2:
            predicted = 0
        else:
            predicted = comb(n, l - 2)
        if predicted != cnt:
            ok = False
            print(f"  MISMATCH l={l} j={j} (a,b)=({a},{b}): brute={cnt} predicted={predicted}")
    total_brute = sum(brute.values())
    total_predicted = comb(l + j, l)
    print(f"  (l={l},j={j}): per-cell match={ok}, total_brute={total_brute}, C(l+j,l)={total_predicted}, match={total_brute==total_predicted}")

print("\n=== Part 2: asymptotic check ===")
rho = log(3) / log(4)
l = 300
j = round(rho * l)
alpha = 1 / (1 + rho)
beta = rho / (1 + rho)

# exact Pr(G0=a,G1=b) via the formula, normalized by C(l+j,l)
from math import comb as C
import math

def log_C(n, k):
    if k < 0 or k > n:
        return float('-inf')
    return math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)

logC_total = log_C(l + j, l)

print(f"rho={rho:.6f}, l={l}, j={j}, alpha={alpha:.6f}, beta={beta:.6f}")
print(f"{'a':>3} {'b':>3} {'exact_Pr':>14} {'asymptotic':>14} {'rel_err':>10}")
max_rel_err = 0
for a in range(0, 4):
    for b in range(0, 4):
        n = l + j - a - b - 2
        if n < l - 2:
            continue
        logp = log_C(n, l - 2) - logC_total
        exact_p = math.exp(logp)
        asym_p = alpha**2 * beta**(a + b)
        rel_err = abs(exact_p - asym_p) / asym_p
        max_rel_err = max(max_rel_err, rel_err)
        print(f"{a:>3} {b:>3} {exact_p:>14.8f} {asym_p:>14.8f} {rel_err:>10.4%}")

print(f"\nmax relative error (should shrink as l grows, l=300 here): {max_rel_err:.4%}")
