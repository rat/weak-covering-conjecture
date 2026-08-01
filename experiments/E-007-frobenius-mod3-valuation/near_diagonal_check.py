"""
Direct enumeration of H-006's near-diagonal anti-concentration quantity, as precisely
formalized by Codex in round 6 of the second consultation cycle
(/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck2_round6_out.txt).

For [n]={0,...,n-1}, k-subset A, q-subset D subset A (deletions), q-subset I subset
[n]\\A (insertions), B := (A\\D) union I. W_k(S) := sum_{r=1}^k 3^{k-r}*2^{s_r} for
S={s_1<...<s_k} (the branch statistic from this project's own generating polynomial).
Delta := W_k(A) - W_k(B).

alpha_{n,k,q} := max_d Pr[Delta = d]   (point anti-concentration)

Codex's claim: this is "directly enumerable at small n,k,q." This script does exactly
that (exact enumeration, not simulation) for a few small parameter sets, to get real
data on whether alpha decays as q grows (supporting the needed anti-concentration) or
stays high (would suggest a real obstruction).
"""
from itertools import combinations
from collections import Counter


def W(S):
    """S: increasing tuple of exponents. W_k(S) = sum_r 3^{k-r} * 2^{s_r}, r=1..k (1-indexed)."""
    k = len(S)
    return sum(3 ** (k - r) * 2 ** S[r - 1] for r in range(1, k + 1))


def alpha(n, k, q):
    universe = list(range(n))
    deltas = Counter()
    total = 0
    for A in combinations(universe, k):
        A_set = set(A)
        rest = [x for x in universe if x not in A_set]
        wA = W(tuple(sorted(A)))
        for D in combinations(A, q):
            D_set = set(D)
            keep = tuple(sorted(A_set - D_set))
            for I in combinations(rest, q):
                B = tuple(sorted(keep + I))
                wB = W(B)
                deltas[wA - wB] += 1
                total += 1
    max_count = max(deltas.values())
    return max_count / total, total, len(deltas)


if __name__ == "__main__":
    print(f"{'n':>3} {'k':>3} {'q':>3} {'alpha':>12} {'total_triples':>14} {'distinct_deltas':>16}")
    for n, k in [(8, 4), (10, 5), (12, 6)]:
        for q in range(1, min(k, n - k) + 1):
            a, total, distinct = alpha(n, k, q)
            print(f"{n:3d} {k:3d} {q:3d} {a:12.6f} {total:14d} {distinct:16d}")

    print("\nCentral point (n=2k) q=1 check: is alpha_{2k,k,1} = 1/Catalan(k) (Codex's round-7")
    print("claim, WRONG, see round 8) or alpha_{2k,k,1} = 1/(n*(n-1)) (correct, round-8)?")
    import math
    for n, k in [(8, 4), (10, 5), (12, 6), (14, 7)]:
        a, total, distinct = alpha(n, k, 1)
        cat_k = math.comb(2 * k, k) // (k + 1)
        n_n1 = n * (n - 1)
        print(f"n={n:3d} k={k}: measured 1/alpha={1/a:.1f}   "
              f"Catalan(k)={cat_k:6d} (match={abs(1/a-cat_k)<0.5})   "
              f"n(n-1)={n_n1:6d} (match={abs(1/a-n_n1)<0.5})")

    print("\nGeneral (non-central, k != n/2) check of alpha_{n,k,1} = 1/(n*(n-1)),")
    print("Codex's round-8 corrected + proven formula, for ALL 1<=k<n:")
    for n, k in [(9, 3), (9, 4), (10, 3), (10, 4), (11, 4), (12, 4), (12, 5)]:
        a, total, distinct = alpha(n, k, 1)
        n_n1 = n * (n - 1)
        print(f"n={n:3d} k={k}: measured 1/alpha={1/a:.2f}   n(n-1)={n_n1}   "
              f"match={abs(1/a-n_n1)<0.5}")
