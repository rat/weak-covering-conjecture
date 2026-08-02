"""
Round 18 (mega cycle): run Codex's preregistered 12-cell family-level test for "controlled
3-adic dynamics", per the round-18 clarification:

  A_{l,j}^(5) = union_{d=1}^{min(l,j)} stratum_image(L=5, j, d)   (subset of units mod 3^5)
  R_{l,j}^(5) = units mod 3^5  minus  A_{l,j}^(5)

Grid: (l,j) in {4,5} x {0,1,2,3,4,5}. For each cell: n=|R|, T(R) = sum over pairs of v_3(x-y),
exact p-value via the tree-recursive polynomial null DP (generalized from mega_round9's K=6 case
to general K, here K=5 fixed). Then the two predeclared aggregate checks: G=sum T, exact product
null for G via convolution of the 12 per-cell null laws, and C=#{p<=0.01} with the Markov bound.
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image
from math import comb
from collections import defaultdict
from itertools import combinations

K = 5
MOD = 3 ** K
UNITS = set(x for x in range(MOD) if x % 3 != 0)
N_TOTAL = len(UNITS)
assert N_TOTAL == 2 * 3 ** (K - 1)

def v3(n):
    if n == 0:
        return K  # convention: identical residues don't occur (R has distinct elements); guard only
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v

def T_stat(R):
    total = 0
    for x, y in combinations(sorted(R), 2):
        total += v3(abs(x - y))
    return total

def poly_mul_trunc(A, B, max_m):
    C = {}
    for (m1, t1), c1 in A.items():
        if m1 > max_m:
            continue
        for (m2, t2), c2 in B.items():
            m = m1 + m2
            if m > max_m:
                continue
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

_dp_cache = {}
def null_dist_for_n(n):
    """Exact null distribution of T over a uniform random n-subset of the N_TOTAL=162 units,
    mod-3^5 tree (branching 3 at depths 5,4,3,2 going up, then 2 at the root)."""
    if n in _dp_cache:
        return _dp_cache[n]
    leaf = {(0, 0): 1, (1, 0): 1}
    P = leaf
    for q in range(K - 1, 0, -1):  # K-1 = 4 iterations: q=4,3,2,1
        P = cube_trunc(P, n)
        P = shift_y_by_Cm2(P)
    P_root = square_trunc(P, n)
    dist = defaultdict(int)
    for (m, t), c in P_root.items():
        if m == n:
            dist[t] += c
    total = sum(dist.values())
    expected = comb(N_TOTAL, n)
    assert total == expected, f"DP total mismatch at n={n}: {total} vs {expected}"
    _dp_cache[n] = dist
    return dist

def p_value(T_obs, dist):
    total = sum(dist.values())
    tail = sum(c for t, c in dist.items() if t >= T_obs)
    return tail / total

# --- build the 12 cells ---
results = {}
for l in (4, 5):
    for j in range(0, 6):
        A = set()
        for d in range(1, min(l, j) + 1):
            A |= stratum_image(5, j, d) & UNITS
        R = UNITS - A
        n = len(R)
        T_obs = T_stat(R)
        dist = null_dist_for_n(n)
        p = p_value(T_obs, dist)
        mean_T = sum(t * c for t, c in dist.items()) / sum(dist.values())
        results[(l, j)] = dict(n=n, T=T_obs, p=p, mean_T=mean_T)
        print(f"(l={l}, j={j}): |A|={len(A)}, n=|R|={n}, T={T_obs}, E[T]={mean_T:.2f}, p={p:.3e}")

print()
# --- predeclared checks ---
G = sum(r['T'] for r in results.values())
print(f"G = sum T = {G}")

# exact product null for G: convolve the 12 per-cell null T-distributions (each already computed
# as dist over t for the cell's own n; here we convolve distributions directly, weighting by
# probability, i.e. work with (t, prob) and convolve probabilities)
from functools import reduce

def to_prob_dist(dist):
    total = sum(dist.values())
    return {t: c / total for t, c in dist.items()}

prob_dists = []
for (l, j), r in results.items():
    dist = null_dist_for_n(r['n'])
    prob_dists.append(to_prob_dist(dist))

def convolve_prob(A, B):
    C = defaultdict(float)
    for t1, p1 in A.items():
        for t2, p2 in B.items():
            C[t1 + t2] += p1 * p2
    return C

G_null = reduce(convolve_prob, prob_dists)
p_prod = sum(p for t, p in G_null.items() if t >= G)
print(f"p_prod = Pr_0(G >= {G}) = {p_prod:.6e}")

C_count = sum(1 for r in results.values() if r['p'] <= 0.01)
print(f"C = #cells with p<=0.01 = {C_count}  (Markov bound: Pr(C>=3)<=0.04)")

hits = [(l, j) for (l, j), r in results.items() if r['p'] <= 0.01]
print(f"hit cells: {hits}")
l_levels_hit = set(l for l, j in hits)
jmod3_hit = set(j % 3 for l, j in hits)
print(f"l-levels spanned: {l_levels_hit}, j mod 3 orbits spanned: {jmod3_hit}")

print()
if p_prod <= 1e-3 and C_count >= 3 and len(l_levels_hit) == 2 and len(jmod3_hit) == 3:
    print("VERDICT: real first-stage signal (passes both predeclared checks).")
else:
    print("VERDICT: local-obstruction result only (fails predeclared bar) -- do not fit a recurrence.")
