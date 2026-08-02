"""
Round 9 (mega cycle) follow-up: exact null p-value for T(R) via the polynomial DP Codex
specified, rather than relying on the mean-ratio signal alone.

Tree structure: root -> 2 branches (depth 1, mod 3) -> each splits into 3 (depth 2, mod 9) ->
... -> depth 6 (leaves, individual residues mod 3^6=729, but only 486 are units -- see note
below on restricting to units only, not all 729 residues).

Polynomial P(x,y): coefficient of x^m y^t = number of ways to select m points from this subtree
such that the T-contribution from pairs whose common depth is >= current level equals t.

Recursion (matches Codex's spec): leaves start as (1+x). Going up one level with `deg` children
(deg=3 for depth 5->1, deg=2 for the final root step): take the child polynomial to the deg-th
power (convolution), then for the resulting x^m coefficient (as a polynomial in y), multiply by
y^C(m,2) (shifting every y-exponent up by C(m,2)).

Truncate at m<=24 throughout since we only need the final x^24 coefficient.
"""
from math import comb

TARGET_M = 24

def poly_mul_trunc(A, B, max_m=TARGET_M):
    """A, B: dict[(m,t)] -> coeff. Returns A*B truncated to m<=max_m."""
    C = {}
    for (m1, t1), c1 in A.items():
        if m1 > max_m:
            continue
        for (m2, t2), c2 in B.items():
            m = m1 + m2
            if m > max_m:
                continue
            t = t1 + t2
            key = (m, t)
            C[key] = C.get(key, 0) + c1 * c2
    return C

def cube_trunc(A, max_m=TARGET_M):
    return poly_mul_trunc(poly_mul_trunc(A, A, max_m), A, max_m)

def square_trunc(A, max_m=TARGET_M):
    return poly_mul_trunc(A, A, max_m)

def shift_y_by_Cm2(P):
    """Multiply the x^m coefficient (as poly in y) by y^C(m,2)."""
    out = {}
    for (m, t), c in P.items():
        shift = comb(m, 2)
        out[(m, t + shift)] = out.get((m, t + shift), 0) + c
    return out

# Base case: leaf, single unit residue.
leaf = {(0, 0): 1, (1, 0): 1}

# NOTE on tree shape: the residue tree here should reflect UNITS only (486 of them), not all 729
# residues mod 3^6. Units mod 3 are {1,2} (2 classes, matches b_1=2). Within each unit class mod
# 3, going to mod 9 splits into 3 sub-classes (all still units, since adding multiples of 3 to a
# unit keeps it coprime to 3) -- so the branching factor really is 3 at every level below the
# root, and 2 at the root, for ALL levels, exactly matching Codex's stated tree shape. Good, no
# adjustment needed: units mod 3^q always split into exactly 3 units mod 3^{q+1} per class.

P = leaf
for q in range(5, 0, -1):  # q = 5,4,3,2,1
    P = cube_trunc(P)
    P = shift_y_by_Cm2(P)

# final step: combine the two depth-1 branches (root), via squaring, no additional y-shift needed
# at the root itself since T only sums q=1..5 (root/depth-0 pairs aren't a separate "q" in the
# T formula -- checking: T(R)=sum_{q=1}^{5} Pi(q), so pairs "together at depth 0" (i.e. always,
# trivially) are NOT part of T; only q=1..5 contribute, matching our loop q=5..1 (5 iterations)
# BEFORE the final square, and the final square should NOT add another y-shift.)
P_root = square_trunc(P)

# Extract x^24 coefficients as a function of t
from collections import defaultdict
dist = defaultdict(int)
for (m, t), c in P_root.items():
    if m == TARGET_M:
        dist[t] += c

total_count = sum(dist.values())
N, n = 486, 24
expected_total = comb(N, n)
print(f"Total ways (from DP) for m=24: {total_count}")
print(f"C(486,24) = {expected_total}")
print(f"Match: {total_count == expected_total}")

T_obs = 569
tail = sum(c for t, c in dist.items() if t >= T_obs)
p_T = tail / total_count
print(f"\np_T = Pr(T(R') >= {T_obs}) = {tail} / {total_count} = {p_T:.6e}")

# also report mean and a rough std for sanity
mean_T = sum(t * c for t, c in dist.items()) / total_count
var_T = sum((t - mean_T)**2 * c for t, c in dist.items()) / total_count
print(f"E[T] (exact, from DP) = {mean_T:.3f}  (formula-based estimate was 203.728)")
print(f"std[T] (exact) = {var_T**0.5:.3f}")
print(f"z-score of observed T={T_obs}: {(T_obs-mean_T)/var_T**0.5:.2f}")
