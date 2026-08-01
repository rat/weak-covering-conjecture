"""
Independent verification of round-1 claims from the SECOND lateral-thinking consultation cycle
(/tmp/codex_lateral2_round1_out.txt), before trusting anything, per Rule 8c.

Checks:
1. The Mahler/digital-Young jet identity: with alpha_i = eps_i + 2*n_i (eps_i in {0,1}),
     F(alpha) = sum_i 3^i 2^eps_i 4^n_i = sum_{r>=0} 3^r * sum_{i<=r} 2^eps_i * C(n_i, r-i)
   verified by direct numerical comparison.
2. v_3(4^(3^m) - 1) = m+1, for m=0..6.
3. The noncommutative matrix representation:
     M_a = [[1, 2^a],[0,3]]
     M_{alpha_{j-1}} ... M_{alpha_0} * (0,1)^T = (F(alpha), 3^j)^T
   verified for random valid strictly-decreasing tuples.
4. The adjacent-rank-swap value-change formula (sign checked directly, not assumed).
"""
import random
from math import comb

random.seed(3)

# ---------- Check 1: Mahler/digital-Young jet identity ----------

def F_direct(alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def F_jet(alphas, r_max):
    """sum_r 3^r * sum_{i<=r} 2^eps_i * C(n_i, r-i), r=0..r_max. eps_i, n_i derived from alpha_i."""
    eps = [a % 2 for a in alphas]
    n = [a // 2 for a in alphas]
    total = 0
    for r in range(r_max + 1):
        inner = 0
        for i in range(min(r, len(alphas) - 1) + 1):
            inner += 2**eps[i] * comb(n[i], r - i)
        total += 3**r * inner
    return total

print("=== Check 1: Mahler/digital-Young jet identity ===")
ok1 = True
for trial in range(100):
    j = random.randint(1, 8)
    # random strictly decreasing tuple
    alphas = sorted(random.sample(range(0, 2 * j + 5), j), reverse=True)
    direct = F_direct(alphas)
    # r_max needs to be large enough to capture all terms fully (jet sum is a finite sum matching
    # F exactly once r_max >= max possible position+binomial-degree; use a generous bound)
    r_max = max(alphas) + len(alphas) + 2
    jet = F_jet(alphas, r_max)
    if direct != jet:
        ok1 = False
        print(f"  MISMATCH j={j} alphas={alphas}: direct={direct} jet={jet}")
print(f"  100 random trials: {'ALL MATCH' if ok1 else 'FAILURES FOUND'}")

# ---------- Check 2: v_3(4^(3^m) - 1) = m+1 ----------

def v3(n):
    if n == 0:
        return None
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k

print("\n=== Check 2: v_3(4^(3^m) - 1) = m+1 ===")
ok2 = True
for m in range(0, 7):
    val = 4**(3**m) - 1
    v = v3(val)
    if v != m + 1:
        ok2 = False
        print(f"  MISMATCH m={m}: v3={v} expected={m+1}")
print(f"  m=0..6: {'ALL MATCH' if ok2 else 'FAILURES FOUND'}")

# ---------- Check 3: noncommutative matrix representation ----------

def mat_mult(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

def M(a):
    return [[1, 2**a], [0, 3]]

print("\n=== Check 3: noncommutative matrix representation ===")
ok3 = True
for trial in range(100):
    j = random.randint(1, 8)
    alphas = sorted(random.sample(range(0, 2 * j + 5), j), reverse=True)
    # product M_{alpha_{j-1}} ... M_{alpha_0}, i.e. rightmost is M_{alpha_0} (applied first to v)
    prod = [[1, 0], [0, 1]]
    for a in reversed(alphas):  # multiply in order alpha_0, alpha_1, ..., alpha_{j-1} from the right
        prod = mat_mult(prod, M(a))
    # prod = M_{alpha_{j-1}} * ... * M_{alpha_0} (built up correctly by right-multiplying in order)
    v = [0, 1]
    result = [prod[0][0]*v[0] + prod[0][1]*v[1], prod[1][0]*v[0] + prod[1][1]*v[1]]
    expected = (F_direct(alphas), 3**j)
    if tuple(result) != expected:
        ok3 = False
        print(f"  MISMATCH j={j} alphas={alphas}: result={result} expected={expected}")
print(f"  100 random trials: {'ALL MATCH' if ok3 else 'FAILURES FOUND'}")

# ---------- Check 4: adjacent-rank-swap value-change formula ----------

print("\n=== Check 4: adjacent-rank-swap value change (sign checked directly) ===")
ok4 = True
for trial in range(50):
    j = random.randint(2, 8)
    alphas = sorted(random.sample(range(0, 2 * j + 5), j), reverse=True)
    i = random.randint(0, j - 2)
    a, b = alphas[i], alphas[i + 1]  # position i has 'a' (larger), position i+1 has 'b' (smaller)
    swapped = alphas[:]
    swapped[i], swapped[i + 1] = b, a  # formal swap (breaks strict decrease, that's fine, just a
                                        # value computation, not a valid tuple)
    diff = F_direct(swapped) - F_direct(alphas)
    # Codex's claimed formula: diff = -2*3^i*(2^a - 2^b)
    claimed = -2 * 3**i * (2**a - 2**b)
    if diff != claimed:
        ok4 = False
        print(f"  MISMATCH j={j} i={i} a={a} b={b}: diff={diff} claimed={claimed} "
              f"(ratio={diff/claimed if claimed else 'N/A'})")
print(f"  50 random trials: {'ALL MATCH' if ok4 else 'MISMATCHES (see above; may be a sign/convention issue)'}")
