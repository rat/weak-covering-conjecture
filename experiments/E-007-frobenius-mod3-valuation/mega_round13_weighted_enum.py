"""
Round 13 (mega cycle) follow-up: forward DP for the weighted box enumerator
P_{a,b}^{(k)}(residue) = #{A in a x b partition box : H(A) === residue (mod 3^k)},
as Codex requested (a histogram DP, not an inverse solver), verified against direct enumeration,
then used to scan a small grid of (a,b) for a recurrence/period.
"""
from fractions import Fraction

def H_direct(a, lam_prefix):
    total = Fraction(0)
    for r in range(1, a + 1):
        lam_r = lam_prefix[r - 1] if r - 1 < len(lam_prefix) else 0
        for c in range(1, lam_r + 1):
            total += Fraction(3) ** (r - 1) * Fraction(2) ** (c - r - 1)
    return total

def frac_mod(frac, mod):
    num, den = frac.numerator, frac.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def partitions_in_box(rows, cols):
    if rows == 0:
        yield []
        return
    def rec(remaining_rows, max_part):
        if remaining_rows == 0:
            yield []
            return
        for first in range(max_part, -1, -1):
            for rest in rec(remaining_rows - 1, first):
                yield [first] + rest
    yield from rec(rows, cols)

def histogram_direct(a, b, k):
    mod = 3**k
    hist = [0] * mod
    for A in partitions_in_box(a, b):
        r = frac_mod(H_direct(a, A), mod)
        hist[r] += 1
    return hist

def histogram_dp(a, b, k):
    """DP over rows 1..a, state = (prev_row_value, H mod 3^k), weakly decreasing rows in [0,b]."""
    mod = 3**k
    inv2 = pow(2, -1, mod)
    # dp[prev_val] = {h_mod: count}
    dp = {v: {0: 1} for v in range(b + 1)}  # before any row placed: prev_val is a free upper
                                              # bound choice for row 1 (any value 0..b), h=0
    # Actually simplify: track state after processing r rows: (last placed value, h mod).
    # Initialize "row 0" sentinel with last value = b (max allowed), h=0.
    state = {(b, 0): 1}
    for r in range(1, a + 1):
        new_state = {}
        pow3_r_minus1 = pow(3, r - 1, mod)
        for (prev_val, h), cnt in state.items():
            for val in range(0, prev_val + 1):
                # row r contributes: 3^{r-1} * sum_{c=1}^{val} 2^{c-r-1}
                #                  = 3^{r-1} * 2^{-r-1} * (2^{val+1}-2)   [if val>0, else 0]
                if val == 0:
                    contrib = 0
                else:
                    inv_2_r1 = pow(2, -(r + 1), mod) if (r + 1) > 0 else pow(2, r + 1, mod)
                    # 2^{-(r+1)} mod `mod`: use modular inverse of 2^{r+1}
                    inv_2_r1 = pow(pow(2, r + 1, mod), -1, mod)
                    two_val1_minus2 = (pow(2, val + 1, mod) - 2) % mod
                    contrib = (pow3_r_minus1 * inv_2_r1 % mod) * two_val1_minus2 % mod
                new_h = (h + contrib) % mod
                key = (val, new_h)
                new_state[key] = new_state.get(key, 0) + cnt
        state = new_state
    hist = [0] * mod
    for (last_val, h), cnt in state.items():
        hist[h] += cnt
    return hist

print("=== Verify DP against direct enumeration ===")
ok = True
for (a, b, k) in [(3, 5, 2), (4, 4, 2), (2, 6, 2), (3, 5, 3)]:
    direct = histogram_direct(a, b, k)
    dp = histogram_dp(a, b, k)
    match = direct == dp
    if not match:
        ok = False
    print(f"  a={a} b={b} k={k}: direct={direct} dp={dp} match={match}")
print(f"  Overall: {'ALL MATCH' if ok else 'MISMATCH FOUND'}")

print("\n=== Scan a small grid of (a,b) at k=2 (mod 9), unit residues only ===")
unit_residues = [1, 2, 4, 5, 7, 8]
for a in range(1, 6):
    for b in range(1, 8):
        if a > 6 or b > 8:
            continue
        hist = histogram_dp(a, b, 2)
        counts = [hist[r] for r in unit_residues]
        print(f"  a={a} b={b}: counts at residues {unit_residues} = {counts}  "
              f"(total unit A's = {sum(counts)}, total A's = {sum(hist)})")
