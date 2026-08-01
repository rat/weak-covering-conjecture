"""
Independent verification of round-2's core structural claim (second lateral cycle),
before building the full "mod-3 leading-influence matrix" experiment.

Codex's own instruction: "Verify this assertion directly for every generated column before
trusting any rank data." Checking exactly that assertion:

  J_r(eps, n) = sum_{i<=r} 2^eps_i * C(n_i, r-i)   (F = sum_r 3^r J_r)

  L_{r,(i,m)} = (1/2) * [J_r(eps, n + 3^m e_i) - J_r(eps, n - 3^m e_i)]  (mod 3)

  Claimed: L_{r,(i,m)} = 0 for r < i+3^m
           L_{i+3^m,(i,m)} = 2^eps_i (mod 3)   -- the "leading diagonal" claim

This is the load-bearing lemma for the whole digital-Young-diagram matrix experiment; if it's
wrong, nothing built on top of it is worth pursuing.
"""
import random
from math import comb

random.seed(4)

def J(eps, n, r):
    total = 0
    for i in range(min(r, len(n) - 1) + 1):
        k = r - i
        if 0 <= k <= n[i]:
            total += (2 ** eps[i]) * comb(n[i], k)
    return total

def inv2_mod3():
    return pow(2, -1, 3)  # 2 is its own inverse mod 3 (2*2=4=1 mod3)

print("=== Verifying the core Lucas-diagonal lemma for L_{r,(i,m)} ===")
ok = True
n_checks = 0
inv2 = inv2_mod3()

for trial in range(300):
    ell = random.randint(2, 6)          # tuple length
    n = [random.randint(0, 40) for _ in range(ell)]
    eps = [random.randint(0, 1) for _ in range(ell)]
    i = random.randint(0, ell - 1)
    m = random.randint(0, 3)
    if n[i] < 3**m:
        continue  # need n_i - 3^m >= 0 for the "-" move to be a valid nonneg n_i

    R = i + 3**m + 3  # check a few rows past the claimed leading diagonal

    n_plus = n[:]
    n_plus[i] = n[i] + 3**m
    n_minus = n[:]
    n_minus[i] = n[i] - 3**m

    for r in range(0, R + 1):
        Jp = J(eps, n_plus, r)
        Jm = J(eps, n_minus, r)
        diff = Jp - Jm
        # "1/2" is the multiplicative inverse of 2 in F_3 (2*2=4=1 mod 3), i.e. 1/2 = 2 (mod 3).
        # The whole expression lives in F_3, not in the integers -- no reason diff itself need be
        # even; fixed after an initial misreading treated this as literal integer division.
        L = (diff * inv2) % 3
        n_checks += 1

        leading = i + 3**m
        if r < leading:
            if L != 0:
                ok = False
                print(f"  MISMATCH (expected 0 below leading diagonal) i={i} m={m} r={r} "
                      f"leading={leading}: L={L}")
        elif r == leading:
            expected = (2 ** eps[i]) % 3
            if L != expected:
                ok = False
                print(f"  MISMATCH (leading diagonal value) i={i} m={m} r={r}: L={L} "
                      f"expected={expected} (eps_i={eps[i]})")

print(f"  {n_checks} (trial, r) checks across up to 300 random configurations: "
      f"{'ALL MATCH' if ok else 'FAILURES FOUND'}")
