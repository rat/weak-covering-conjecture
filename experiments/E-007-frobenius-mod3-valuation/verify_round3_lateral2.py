"""
Independent verification of round-3 claims (second lateral cycle): the slack/density
obstruction argument for the centered buffered-cell mechanism, and the one-sided D+/D-/Q
decomposition Codex proposed as the decisive next test.
"""
import random
from math import comb

random.seed(5)

# ---------- Check 1: the slack bound E and our own witnesses' actual E values ----------

def slack(alphas_sorted_increasing):
    a = alphas_sorted_increasing
    j = len(a)
    return (a[-1] - a[0]) - (j - 1)

print("=== Check 1: slack E for our own round-2 witnesses ===")
witnesses = {
    "l=4 near-defect": sorted((8, 7, 5, 3, 2, 1, 0)),
    "l=4 control":     sorted((10, 8, 7, 5, 2, 1, 0)),
    "l=6 near-defect": sorted((16, 12, 10, 7, 5, 4, 3, 2, 1, 0)),
    "l=6 control":     sorted((16, 14, 10, 8, 7, 4, 3, 2, 1, 0)),
}
for label, a in witnesses.items():
    j = len(a)
    E = slack(a)
    print(f"  {label}: j={j}, E={E}, max possible E=j={j}, "
          f"needed for a single m=0 (s=2) cell: E>=4 -> {'possible' if E >= 4 else 'IMPOSSIBLE'}, "
          f"needed for m=1 (s=6): E>=12 -> {'possible' if E >= 12 else 'IMPOSSIBLE'}")

# ---------- Check 2: one-sided D+/D-/Q decomposition ----------

def J(eps, n, r):
    total = 0
    for i in range(min(r, len(n) - 1) + 1):
        k = r - i
        if 0 <= k <= n[i]:
            total += (2 ** eps[i]) * comb(n[i], k)
    return total

inv2 = pow(2, -1, 3)

print("\n=== Check 2: one-sided D+ / D- / Q decomposition, and its own Lucas property ===")
ok_algebra = True
ok_lucas = True
n_lucas_checks = 0
for trial in range(300):
    ell = random.randint(2, 6)
    n = [random.randint(0, 40) for _ in range(ell)]
    eps = [random.randint(0, 1) for _ in range(ell)]
    i = random.randint(0, ell - 1)
    m = random.randint(0, 3)
    if n[i] < 3**m:
        continue

    R = i + 3**m + 3
    n_plus = n[:]; n_plus[i] += 3**m
    n_minus = n[:]; n_minus[i] -= 3**m

    for r in range(R + 1):
        J0 = J(eps, n, r)
        Jp = J(eps, n_plus, r)
        Jm = J(eps, n_minus, r)

        Dplus = Jp - J0
        Dminus = J0 - Jm
        Q = Jp - 2 * J0 + Jm
        L = ((Jp - Jm) * inv2) % 3

        # algebraic identity: L = 2*(D+ + D-) (mod 3)
        lhs = L
        rhs = (2 * (Dplus + Dminus)) % 3
        if lhs != rhs:
            ok_algebra = False
            print(f"  ALGEBRA MISMATCH i={i} m={m} r={r}: L={lhs} 2*(D++D-)={rhs}")

        # test D+/D- own Lucas property (mod 3)
        Dplus_m3 = Dplus % 3
        Dminus_m3 = Dminus % 3
        leading = i + 3**m
        expected = (2 ** eps[i]) % 3
        n_lucas_checks += 1
        if r < leading:
            if Dplus_m3 != 0 or Dminus_m3 != 0:
                ok_lucas = False
        elif r == leading:
            if Dplus_m3 != expected or Dminus_m3 != expected:
                ok_lucas = False

print(f"  Algebraic identity L=2*(D++D-) (mod 3): {'CONFIRMED' if ok_algebra else 'FAILED'}")
lucas_msg = ("HOLDS (one-sided is ALSO Lucas-triangular, contrary to the caution given)"
             if ok_lucas else
             "FAILS (Q contaminates as warned -- one-sided is NOT automatically triangular)")
print(f"  D+/D- own Lucas-triangularity ({n_lucas_checks} checks): {lucas_msg}")

if not ok_lucas:
    # show one concrete counterexample for the report
    for trial in range(50):
        ell = random.randint(2, 6)
        n = [random.randint(0, 40) for _ in range(ell)]
        eps = [random.randint(0, 1) for _ in range(ell)]
        i = random.randint(0, ell - 1)
        m = random.randint(0, 2)
        if n[i] < 3**m:
            continue
        n_plus = n[:]; n_plus[i] += 3**m
        leading = i + 3**m
        J0 = J(eps, n, leading)
        Jp = J(eps, n_plus, leading)
        Dplus = (Jp - J0) % 3
        expected = (2 ** eps[i]) % 3
        if Dplus != expected:
            print(f"\n  Example counterexample: i={i} m={m} r=leading={leading}: "
                  f"D+={Dplus}, expected={expected}, n={n}, eps={eps}")
            break
