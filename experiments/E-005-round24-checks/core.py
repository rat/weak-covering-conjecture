"""
Core exact DP for the joint law of (Syrac_n mod 3^L, cost A_n).

Syrac_n = sum_{m=1}^{n} 3^{m-1} 2^{-(a_1+...+a_m)}  mod 3^L,   a_i >= 1 integers.
cost A = a_1 + ... + a_n.   P(tuple) = 2^{-A}  (a_i iid Geom(2), P(a=k)=2^{-k}).

Tao's Syrac(Z/3^n Z) is the case L = n.  The project's own budgeted covering
object lives at L > n (see report).

Trick that makes the DP a clean permutation-scatter: put
    W_m := 2^{a_1+...+a_m} S_m  = 2^{a_m} W_{m-1} + 3^{m-1},   W_0 = 0.
For each a the map W -> 2^a W + 3^{m-1} is a bijection of Z/3^L, so the scatter
has no collisions.  At the end Syrac = 2^{-A} W_n, so
    N[z, c] = D[z * 2^c mod 3^L, c].

N[z,c] = number of tuples with Syrac = z and cost = c (exact integers).
Check: sum_z N[z,c] = C(c-1, n-1).

Originally written by a B1/B2/C2 investigation subagent (2026-07-30) in a session-scoped
scratchpad; copied into this repo verbatim (critique round, same day) so mean_cost_per_residue.py,
argmax_comparison.py, and coherent_branch_search.py's dependents do not point at a temp path that
will not survive. Brute-force check in __main__ re-run and passes before this copy was trusted.
"""
import numpy as np
from math import comb


def dp_W(n, L, cmax):
    """D[W, c] = #tuples of length n, cost c, with W_n = W.  Exact for all c<=cmax."""
    M = 3 ** L
    amax = cmax - (n - 1)
    W = np.arange(M, dtype=np.int64)
    D = np.zeros((M, cmax + 1), dtype=np.int64)
    D[0, 0] = 1
    for m in range(1, n + 1):
        shift = pow(3, m - 1, M)
        E = np.zeros_like(D)
        p2 = 1
        for a in range(1, min(amax, cmax) + 1):
            p2 = (p2 * 2) % M
            p = (p2 * W + shift) % M          # bijection of Z/3^L
            E[p, a:] += D[:, : cmax + 1 - a]
        D = E
    return D


def joint_counts(n, L, cmax):
    """N[z,c] over z in Z/3^L."""
    M = 3 ** L
    D = dp_W(n, L, cmax)
    N = np.zeros_like(D)
    z = np.arange(M, dtype=np.int64)
    p2 = 1
    for c in range(cmax + 1):
        if c > 0:
            p2 = (p2 * 2) % M
        N[:, c] = D[(z * p2) % M, c]
    return N


def marginal_ok(n, cmax, N):
    tot = N.sum(axis=0)
    for c in range(cmax + 1):
        want = comb(c - 1, n - 1) if c >= n else 0
        if int(tot[c]) != want:
            return False, c, int(tot[c]), want
    return True, None, None, None


def brute(n, L, amax):
    from itertools import product
    M = 3 ** L
    inv2 = pow(2, -1, M)
    out = {}
    for tup in product(range(1, amax + 1), repeat=n):
        acc = 0
        v = 0
        for m in range(n):
            acc += tup[m]
            v = (v + pow(3, m, M) * pow(inv2, acc, M)) % M
        out[(v, sum(tup))] = out.get((v, sum(tup)), 0) + 1
    return out


if __name__ == "__main__":
    for (n, L, amax) in [(3, 3, 7), (4, 4, 6), (3, 5, 7), (4, 6, 5), (2, 4, 9)]:
        cmax = n * amax
        N = joint_counts(n, L, cmax)
        B = brute(n, L, amax)
        bad = 0
        for c in range(n, amax + 1):       # c<=amax => every part <= amax
            for z in range(3 ** L):
                if int(N[z, c]) != B.get((z, c), 0):
                    bad += 1
        print(f"n={n} L={L}: DP-vs-brute mismatches={bad}; marginal={marginal_ok(n,cmax,N)[0]}")
