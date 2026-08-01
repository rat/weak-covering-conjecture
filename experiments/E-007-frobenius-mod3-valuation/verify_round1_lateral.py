"""
Independent verification of Codex round-1 claims (lateral-thinking consultation cycle,
/tmp/codex_lateral_round1_out.txt), plus data-gathering for round 2, per Rule 8c.

Checks:
1. The exact Young-diagram identity:
     F_j(lambda) = 3^j - 2^j + sum_{(i,c) in D(lambda)} 3^i * 2^{j-1-i+c}
   against direct computation of F_j(alpha) = sum_i 3^i * 2^{alpha_i} with
   alpha_i = lambda_i + (j-1-i), for random partitions lambda fitting in the j x j square.
2. Box-weight facts: v_3(w_{i,c}) = i, and w_{i+a,c+a} = 3^a * w_{i,c}.
3. Fiber-count statistics at j*(l) and j*(l)-1 for small l (brute force over all
   C(2j,j) tuples), compared against the claimed mean-fiber estimate
   M_{j,l} = C(2j,j) / (2*3^(l-1)).
"""
import random
from itertools import combinations
from math import comb, log, pi, sqrt

random.seed(0)

# ---------- Check 1 & 2: exact identity and box-weight facts ----------

def F_j_direct(j, alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def F_j_young(j, lam):
    total = 3**j - 2**j
    for i in range(j):
        for c in range(lam[i]):
            total += 3**i * 2**(j - 1 - i + c)
    return total

def random_partition_in_square(j):
    # weakly decreasing lam_0 >= lam_1 >= ... >= lam_{j-1}, each in [0,j]
    lam = sorted((random.randint(0, j) for _ in range(j)), reverse=True)
    return lam

print("=== Check 1: exact Young-diagram identity F_j(lambda) ===")
ok1 = True
for trial in range(200):
    j = random.randint(1, 12)
    lam = random_partition_in_square(j)
    alphas = [lam[i] + (j - 1 - i) for i in range(j)]
    # sanity: alphas must be strictly decreasing and >=0, <=2j-1
    assert all(alphas[i] > alphas[i+1] for i in range(j-1)) if j > 1 else True
    assert alphas[-1] >= 0 and alphas[0] <= 2*j - 1
    lhs = F_j_direct(j, alphas)
    rhs = F_j_young(j, lam)
    if lhs != rhs:
        ok1 = False
        print(f"  MISMATCH j={j} lam={lam}: direct={lhs} young={rhs}")
print(f"  200 random trials, j up to 12: {'ALL MATCH' if ok1 else 'FAILURES FOUND'}")

print("\n=== Check 2: box-weight valuation and diagonal-scaling facts ===")
def v3(n):
    if n == 0:
        return None
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k

ok2 = True
for trial in range(500):
    j = random.randint(1, 15)
    i = random.randint(0, j - 1)
    c = random.randint(0, 20)
    w = 3**i * 2**(j - 1 - i + c)
    if v3(w) != i:
        ok2 = False
        print(f"  v3 MISMATCH i={i} c={c} j={j}: v3(w)={v3(w)}")
    a = random.randint(0, 5)
    j2 = j + a  # need a consistent j for the shifted weight; test the raw formula instead
    w_shifted = 3**(i + a) * 2**(j - 1 - i + c)  # w_{i+a, c+a} uses SAME j, shift i and c by a
    # w_{i+a,c+a} formula: 3^(i+a) * 2^(j-1-(i+a)+(c+a)) = 3^(i+a) * 2^(j-1-i+c)
    expected = 3**a * w
    if w_shifted != expected:
        ok2 = False
        print(f"  scaling MISMATCH i={i} c={c} a={a}: w_shifted={w_shifted} 3^a*w={expected}")
print(f"  500 random trials: {'ALL MATCH' if ok2 else 'FAILURES FOUND'}")

# ---------- Check 3: fiber-count statistics ----------

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

def fiber_counts(j, l):
    """Brute-force: for j-term strictly decreasing alpha_0>...>alpha_{j-1}>=0 chosen from
    range(2j), compute F_j mod 3^l for every tuple, return a count array over Z/3^l."""
    mod = 3**l
    counts = [0] * mod
    n_units_hit = 0
    for combo in combinations(range(2*j), j):
        alphas = sorted(combo, reverse=True)
        val = sum(3**i * 2**a for i, a in enumerate(alphas)) % mod
        counts[val] += 1
    return counts

def is_unit_mod3(x, l):
    return x % 3 != 0

print("\n=== Check 3: fiber-count statistics at j*(l) and j*(l)-1 (small l only) ===")
print(f"{'l':>3} {'j*':>3} {'total_tuples':>13} {'units_mod':>10} "
      f"{'hit_at_j*':>10} {'hit_at_j*-1':>12} {'holes_at_j*-1':>14} "
      f"{'mean_fib':>10} {'M_pred':>10} {'min_fib':>8} {'max_fib':>8}")

results = []
for l in range(2, 9):  # keep this tractable; l=8 -> j*=12, C(24,12)=2.7M
    j = JSTAR[l]
    mod = 3**l
    n_units = 2 * 3**(l-1)
    total_tuples = comb(2*j, j)

    counts_j = fiber_counts(j, l)
    hit_j = sum(1 for x in range(mod) if is_unit_mod3(x, l) and counts_j[x] > 0)
    fib_sizes = [counts_j[x] for x in range(mod) if is_unit_mod3(x, l)]
    mean_fib = sum(fib_sizes) / len(fib_sizes)
    min_fib = min(fib_sizes)
    max_fib = max(fib_sizes)
    M_pred = total_tuples / n_units

    jm1 = j - 1
    total_tuples_jm1 = comb(2*jm1, jm1)
    counts_jm1 = fiber_counts(jm1, l)
    hit_jm1 = sum(1 for x in range(mod) if is_unit_mod3(x, l) and counts_jm1[x] > 0)
    holes_jm1 = n_units - hit_jm1

    results.append((l, j, total_tuples, n_units, hit_j, hit_jm1, holes_jm1, mean_fib, M_pred, min_fib, max_fib))
    print(f"{l:>3} {j:>3} {total_tuples:>13} {n_units:>10} {hit_j:>10} {hit_jm1:>12} "
          f"{holes_jm1:>14} {mean_fib:>10.3f} {M_pred:>10.3f} {min_fib:>8} {max_fib:>8}")

print("\nSanity: hit_at_j* should equal units_mod (full coverage, by definition of j*(l)).")
print("Sanity: hit_at_j*-1 should be < units_mod (that's why j*-1 doesn't cover).")
