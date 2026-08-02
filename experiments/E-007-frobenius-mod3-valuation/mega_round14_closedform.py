"""
Round 14 (mega cycle) follow-up: verify Codex's full closed-form binomial-sum formula for the
raw H(A) mod 9 histogram, against the already-verified DP.
"""
from math import comb

def g_exact_mod9(n):
    # g(n) = (2^n - 1)/2 ; compute mod 9 using modular inverse of 2
    if n == 0:
        return 0
    inv2 = pow(2, -1, 9)
    return ((pow(2, n, 9) - 1) * inv2) % 9

# cross-check against Codex's table: n mod 6 -> g(n) mod 9 (lambda_2 even column, i.e. plain g(n))
print("=== Cross-check g(n) mod 9 table ===")
codex_table_even_col = {0: 0, 1: 5, 2: 6, 3: 8, 4: 3, 5: 2}  # "lambda_2 even" column = g(n) mod9 directly? or is this g(n)+3*g(lambda2)?
for nm6 in range(6):
    # test with an n that has this residue mod 6, e.g. n = nm6
    computed = g_exact_mod9(nm6)
    print(f"  n mod6={nm6}: computed g(n) mod9 = {computed}, Codex table 'even' col = {codex_table_even_col[nm6]}")

# ---------- Full closed-form histogram vs DP, for (a,b)=(3,5) ----------

def E_O(a, b):
    """E_n, O_n for n=0..b: cumulative binomial sums C(a-2+m,a-2) over even/odd m<=n."""
    E = [0] * (b + 1)
    O = [0] * (b + 1)
    e_run, o_run = 0, 0
    for n in range(0, b + 1):
        term = comb(a - 2 + n, a - 2) if a >= 2 else (1 if n == 0 else 0)
        if n % 2 == 0:
            e_run += term
        else:
            o_run += term
        E[n] = e_run
        O[n] = o_run
    return E, O

# Test Codex's own displayed formula literally:
#   h_r = sum_{n=0}^{b} [ 1_{r=g(n)}*E_n + 1_{r=g(n)+6}*O_n ]
# where E_n, O_n are cumulative binomial sums (defined above) and n ranges over lambda_1 values.

def closed_form_histogram_v2(a, b):
    E, O = E_O(a, b)
    h = [0] * 9
    for n in range(0, b + 1):
        gn = g_exact_mod9(n)
        h[gn] = (h[gn] + E[n]) % 10**9  # use plain ints, no mod needed except residue index
        h[(gn + 6) % 9] += O[n]
    return h

import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from mega_round13_weighted_enum import histogram_dp

print("\n=== Closed-form histogram (v2, literal reading of Codex's formula) vs DP ===")
for (a, b) in [(3, 5), (4, 4), (2, 6), (5, 5)]:
    cf = closed_form_histogram_v2(a, b)
    dp = histogram_dp(a, b, 2)
    print(f"  a={a} b={b}: closed_form={cf}")
    print(f"             dp          ={dp}")
    print(f"             match={cf == dp}")
