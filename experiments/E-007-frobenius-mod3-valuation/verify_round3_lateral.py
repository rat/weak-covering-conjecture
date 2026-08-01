"""
Independent verification of Codex round-3 claims (lateral-thinking cycle,
/tmp/codex_lateral_round3_out.txt), plus extending the round-2 fiber statistics
using Codex's proposed transfer-matrix DP (much faster than brute force).

Checks:
1. Hand re-derivation of the two-state transducer's closed form:
     F_{r+1}(P_d) - F_r(P) = 3^r * 2^a * (d-1)  (mod 3^{r+1})
   for P_d = (..., c, a+2d, a-5+2d), c-a>=5.
2. Codex's own check(depth) function, run verbatim for depth=2..10.
3. Codex's numpy transfer-matrix DP for fiber_counts, cross-checked exactly
   against the brute-force fiber_counts from round 1/2 for l=2..8 (must match
   every single entry, not just aggregate stats).
4. If (3) passes, use the DP to extend the round-2 kappa/L(0) statistics to
   l=9 and l=10 (the exact open question round 2 flagged: does the pattern
   survive past l=8, where brute force became impractical?).
5. The "arbitrary packing" feasibility bound B_s^opt = sum_y (c_{y,0}+c_{y,1}+c_{y,2}
   - 3*min(c_{y,0},c_{y,1},c_{y,2})) for the triple-packing idea, at j*(l)-1 for
   several l, to see whether the leftover is small enough to be promising.
"""
import random
import numpy as np
from math import comb, log
from itertools import combinations

random.seed(2)

# ---------- Check 1: hand-verify the two-state transducer closed form ----------

def F(P):
    return sum(3**i * 2**a for i, a in enumerate(P))

def child(P, d):
    a = P[-1]
    return P[:-1] + (a + 2*d, a - 5 + 2*d)

print("=== Check 1: two-state transducer closed form, numeric spot check ===")
print("  (bug found and fixed here: original harness built P with r+1 elements")
print("  instead of r, an off-by-one in prefix construction, not in Codex's claim --")
print("  see Check 2 below, which runs Codex's OWN check() verbatim and passed cleanly)")
ok = True
for trial in range(50):
    r = random.randint(1, 10)  # r = len(P); 'a' sits at position r-1
    a = random.randint(20, 60)
    if r == 1:
        P = (a,)
    else:
        c = a + 5 + random.randint(0, 10)  # position r-2 value, must exceed a+4
        prefix = [c]
        cur = c
        for _ in range(r - 2):
            cur += random.randint(1, 5)
            prefix.append(cur)
        prefix = list(reversed(prefix))  # length r-1, strictly decreasing, ends at c
        P = tuple(prefix) + (a,)
    assert len(P) == r
    assert all(P[i] > P[i+1] for i in range(len(P)-1))

    Fr_P = F(P)
    mod = 3**(r + 1)
    for d in (0, 1, 2):
        Pd = child(P, d)
        assert all(Pd[i] > Pd[i+1] for i in range(len(Pd)-1)), f"order violated {Pd}"
        assert Pd[-2] - Pd[-1] == 5
        diff = F(Pd) - Fr_P
        expected = (3**r * 2**a * (d - 1)) % mod
        if diff % mod != expected:
            ok = False
            print(f"  MISMATCH r={r} a={a} d={d}: diff%mod={diff%mod} expected={expected}")
print(f"  50 random trials: {'ALL MATCH' if ok else 'FAILURES FOUND'}")

# ---------- Check 2: Codex's own check(depth) function, verbatim ----------

print("\n=== Check 2: Codex's check(depth) function, run verbatim for depth=2..10 ===")
def check(depth):
    A = 5 * (depth - 1)
    nodes = [(A,)]
    for r in range(1, depth):
        new = []
        mod = 3**(r + 1)
        for P in nodes:
            kids = [child(P, d) for d in range(3)]
            assert all(all(Q[i] > Q[i+1] for i in range(len(Q)-1)) for Q in kids)
            assert all(Q[-2] - Q[-1] == 5 for Q in kids)
            assert {F(Q) % mod for Q in kids} == {(F(P) + t * 3**r) % mod for t in range(3)}
            new.extend(kids)
        nodes = new

    mod = 3**depth
    assert {F(P) % mod for P in nodes} == {(2**A + 3*k) % mod for k in range(3**(depth - 1))}
    return len(nodes)

for depth in range(2, 11):
    n = check(depth)
    print(f"  depth={depth}: PASSED, {n} leaf nodes = 3^{depth-1} = {3**(depth-1)}")

# ---------- Check 3: Codex's numpy DP fiber_counts, cross-checked vs brute force ----------

print("\n=== Check 3: numpy transfer-matrix DP vs brute-force fiber counts, l=2..8 ===")

def fiber_counts_dp(ell, j):
    mod = 3**ell
    dp = np.zeros((j + 1, mod), dtype=np.int64)
    dp[0, 0] = 1
    pow3 = [pow(3, k, mod) for k in range(j)]
    p2 = pow(2, 2*j - 1, mod)
    inv2 = pow(2, -1, mod)

    for t in range(2*j):
        for k in range(min(j - 1, t), -1, -1):
            dp[k + 1] += np.roll(dp[k], (pow3[k] * p2) % mod)
        p2 = (p2 * inv2) % mod

    out = dp[j]
    assert int(out.sum()) == comb(2*j, j)
    assert not out[np.arange(mod) % 3 == 0].any()
    return out

def fiber_counts_brute(j, l):
    mod = 3**l
    counts = [0] * mod
    for combo in combinations(range(2*j), j):
        alphas = sorted(combo, reverse=True)
        val = sum(3**i * 2**a for i, a in enumerate(alphas)) % mod
        counts[val] += 1
    return counts

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

ok3 = True
for l in range(2, 9):
    j = JSTAR[l] - 1  # test at j*(l)-1, the interesting case
    brute = fiber_counts_brute(j, l)
    dp = fiber_counts_dp(l, j)
    if list(dp) != brute:
        ok3 = False
        mismatches = [i for i in range(len(brute)) if dp[i] != brute[i]]
        print(f"  MISMATCH l={l} j={j}: {len(mismatches)} residues differ, e.g. {mismatches[:5]}")
    else:
        print(f"  l={l} j={j}: DP matches brute force exactly ({3**l} residues, sum={int(dp.sum())})")
print(f"  Overall: {'DP CONFIRMED IDENTICAL TO BRUTE FORCE' if ok3 else 'DP DISAGREES -- DO NOT TRUST'}")

# ---------- Check 4: extend kappa / L(0) to l=9, l=10 using the (now trusted) DP ----------

if ok3:
    print("\n=== Check 4: extending kappa, L(0) to l=9, l=10 via the verified DP ===")
    print(f"{'l':>3} {'j*-1':>5} {'N':>12} {'U':>8} {'kappa':>10}   L(0) L(1) L(2) L(3)")
    for l in (9, 10):
        j = JSTAR[l] - 1
        mod = 3**l
        N = comb(2*j, j)
        U = 2 * 3**(l - 1)
        counts = fiber_counts_dp(l, j)

        units_mask = (np.arange(mod) % 3) != 0
        n_u = counts[units_mask].astype(np.float64)
        s = float(np.sum(n_u * (n_u - 1)))
        kappa = (U / (N * (N - 1))) * s

        mod_parent = 3**(l - 1)
        L = [0, 0, 0, 0]
        for xbar in range(mod_parent):
            if xbar % 3 == 0:
                continue
            m = 0
            for u in range(3):
                if counts[xbar + u * mod_parent] > 0:
                    m += 1
            L[m] += 1

        print(f"{l:>3} {j:>5} {N:>12} {U:>8} {kappa:>10.4f}   {L[0]:>4} {L[1]:>4} {L[2]:>4} {L[3]:>4}")

# ---------- Check 5: triple-packing feasibility bound B_s^opt ----------

    print("\n=== Check 5: triple-packing arbitrary-packing feasibility bound B_s^opt ===")
    print("(B_s^opt = sum over parent classes mod 3^(l-1) of unavoidable leftover after")
    print(" greedily forming as many {c0,c1,c2}-limited triples as possible per class;")
    print(" if this is already large relative to U, the packing route can't close GAP A)")
    print(f"{'l':>3} {'j*-1':>5} {'U':>8} {'B_opt':>10} {'B_opt/U':>10}")
    for l in range(3, 11):
        j = JSTAR[l] - 1
        mod = 3**l
        U = 2 * 3**(l - 1)
        counts = fiber_counts_dp(l, j) if l >= 2 else None
        mod_parent = 3**(l - 1)
        B_opt = 0
        for xbar in range(mod_parent):
            if xbar % 3 == 0:
                continue
            c = [int(counts[xbar + u * mod_parent]) for u in range(3)]
            t = min(c)
            b = sum(c) - 3 * t
            B_opt += b
        print(f"{l:>3} {j:>5} {U:>8} {B_opt:>10} {B_opt/U:>10.4f}")
