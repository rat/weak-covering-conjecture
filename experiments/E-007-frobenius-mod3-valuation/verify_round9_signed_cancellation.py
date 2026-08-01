"""
Independent verification of Codex's round-9 signed-cancellation formula (second
consultation cycle, /home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck2_round9_out.txt).

Round 8 proved alpha_{n,k,1} = max_d Pr[Delta=d] = 1/(n(n-1)) (a genuine proof, verified),
and showed the q=1 layer's total ABSOLUTE mass is order-1 (k(n-k)/(n(n-1)) -> rho(1-rho)),
seemingly killing any union-bound approach to a vanishing remainder.

Round 9 argued this is not fatal: the SIGNED version (a characteristic-function-style
average, not a raw probability) can have real cancellation invisible to the union bound.
Specifically, for a q=1 swap a->b (a in A, b not in A), averaged over uniform k-subsets A:

    E_A[ (1/(n(n-1))) * sum_{a in A, b not in A} e^{i*theta*(b-a)} ]
      = k(n-k)/(n(n-1))^2 * (|D_n(theta)|^2 - n),   D_n(theta) := sum_{r=1}^n e^{i*theta*r}

At theta=0, this equals the O(1) mass M_1 = k(n-k)/(n(n-1)). At theta = 2*pi*j/n (j=1,...,n-1,
where D_n(theta)=0 exactly), it drops to O(1/n): -k(n-k)/(n(n-1)^2).

This script directly verifies the formula by brute-force enumeration (LHS) against the
claimed closed form (RHS), for n=9, k=4, at several frequencies including theta=0 and three
nonzero n-th-root frequencies.
"""
import cmath
import math
from itertools import combinations


def lhs(n, k, theta):
    total = 0j
    count = 0
    for A in combinations(range(n), k):
        A_set = set(A)
        B_set = [x for x in range(n) if x not in A_set]
        for a in A:
            for b in B_set:
                total += cmath.exp(1j * theta * (b - a))
        count += 1
    return total / count / (n * (n - 1))


def rhs(n, k, theta):
    Dn = sum(cmath.exp(1j * theta * r) for r in range(1, n + 1))
    return (k * (n - k)) / (n * (n - 1)) ** 2 * (abs(Dn) ** 2 - n)


if __name__ == "__main__":
    n, k = 9, 4
    print(f"n={n}, k={k}")
    for j in range(4):
        theta = 2 * math.pi * j / n
        L = lhs(n, k, theta)
        R = rhs(n, k, theta)
        print(f"  theta=2*pi*{j}/{n}:  LHS={L:.8f}  RHS={R:.8f}  "
              f"match={abs(L - R) < 1e-9}")
    print("\nConfirms: O(1) at theta=0 (the union-bound-visible mass), dropping to O(1/n)")
    print("at nonzero n-th-root frequencies -- real signed cancellation, not visible to the")
    print("absolute-value union bound that killed the round-4 controlled-remainder argument.")
