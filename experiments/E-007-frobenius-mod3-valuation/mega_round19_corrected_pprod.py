"""
Round 19 follow-up: Codex flagged a real methodological issue in round 18's p_prod -- the
12-cell product null double-counts the l=4/l=5 axis, since those cells are byte-identical (not
independent draws). Recompute the correct product null using only the 6 DISTINCT cells (one per
j, since l=4 and l=5 give identical R for every j in this grid).
"""
import time
from math import comb
from collections import defaultdict
from functools import reduce

K = 5
N_TOTAL = 162

def poly_mul_trunc(A, B, max_m):
    C = {}
    for (m1, t1), c1 in A.items():
        if m1 > max_m: continue
        for (m2, t2), c2 in B.items():
            m = m1 + m2
            if m > max_m: continue
            key = (m, t1 + t2)
            C[key] = C.get(key, 0) + c1 * c2
    return C

def cube_trunc(A, max_m):
    return poly_mul_trunc(poly_mul_trunc(A, A, max_m), A, max_m)

def square_trunc(A, max_m):
    return poly_mul_trunc(A, A, max_m)

def shift_y_by_Cm2(P):
    out = {}
    for (m, t), c in P.items():
        shift = comb(m, 2)
        out[(m, t + shift)] = out.get((m, t + shift), 0) + c
    return out

def null_dist_for_n(n):
    leaf = {(0, 0): 1, (1, 0): 1}
    P = leaf
    for q in range(K - 1, 0, -1):
        P = cube_trunc(P, n)
        P = shift_y_by_Cm2(P)
    P_root = square_trunc(P, n)
    dist = defaultdict(int)
    for (m, t), c in P_root.items():
        if m == n:
            dist[t] += c
    total = sum(dist.values())
    assert total == comb(N_TOTAL, n), f"mismatch at n={n}"
    return dist

def to_prob_dist(dist):
    total = sum(dist.values())
    return {t: c / total for t, c in dist.items()}

def convolve_prob(A, B):
    C = defaultdict(float)
    for t1, p1 in A.items():
        for t2, p2 in B.items():
            C[t1 + t2] += p1 * p2
    return C

# the 6 distinct cells: (n, T_obs) pairs, one per j=0..5 (l=4 and l=5 identical)
cells = [
    (162, 9396),
    (161, 9280),
    (157, 8821),
    (143, 7332),
    (96, 3581),
    (58, 1526),
]

prob_dists = []
for n, T_obs in cells:
    t0 = time.time()
    dist = null_dist_for_n(n)
    prob_dists.append(to_prob_dist(dist))
    print(f"n={n}: done in {time.time()-t0:.1f}s")

G6 = sum(t for _, t in cells)
print(f"\nG6 (sum over 6 unique cells) = {G6}")

G_null = reduce(convolve_prob, prob_dists)
p_prod_6 = sum(p for t, p in G_null.items() if t >= G6)
print(f"p_prod_6 (correct, 6-unique-cell product null) = Pr_0(G6 >= {G6}) = {p_prod_6:.6e}")
