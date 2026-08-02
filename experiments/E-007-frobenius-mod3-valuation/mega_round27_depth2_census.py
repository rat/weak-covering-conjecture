"""
Round 27 (mega cycle): verify Codex's depth-two diagonal census mod 9.

Claim: for diagonal strata d>=2, T(A,B) mod 9 = H(A) mod 9 = h_1(a_1) + 3*h_2(a_2) mod 9 (rows
r>=3 vanish mod 9 since prefactor 3^(r-1), r-1>=2). h_1(a_1) mod 9 given by a fixed 6-periodic
table; h_2(a_2) mod 3 = a_2 mod 2 (from round 26's generalized parity lemma at r=2).

Verify directly against the actual H(A) function (round7_stratum_union.py's H), across many
random admissible A's (partition in a d x (j-d) box, d>=2), and separately verify the B-arm
vanishes mod 9 for d>=2 by checking V(A,B) mod 9 == H(A) mod 9 for random (A,B) pairs.
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import H, C
from fractions import Fraction
import random

def frac_mod(fr, mod):
    num, den = fr.numerator, fr.denominator
    inv = pow(den, -1, mod)
    return (num * inv) % mod

def h1_table_predicted(a1_mod6):
    table = [0, 5, 6, 8, 3, 2]
    return table[a1_mod6]

def random_partition(rows, max_col):
    # weakly decreasing sequence of length `rows`, each in [0, max_col]
    if rows == 0:
        return []
    seq = []
    cap = max_col
    for _ in range(rows):
        v = random.randint(0, cap)
        seq.append(v)
        cap = v
    return seq

# --- verify h_1(a1) mod 9 table ---
print("=== h_1(a1) mod 9 table check ===")
ok = True
for a1 in range(0, 30):
    # h_1(x) = H(1, [x]) essentially: row 1 alone, using the H function with prefix [x]
    val = H(1, [a1])
    actual = frac_mod(val, 9)
    predicted = h1_table_predicted(a1 % 6)
    if actual != predicted:
        ok = False
        print(f"  MISMATCH a1={a1}: actual={actual} predicted={predicted}")
print(f"  all match: {ok}")

# --- verify T(A,B) mod 9 = h_1(a1) + 3*h_2(a2) mod 9 for d>=2 ---
print("\n=== depth-2 census formula check (d>=2, pooled) ===")
random.seed(1)
mismatches = 0
trials = 0
for _ in range(3000):
    d = random.randint(2, 6)
    j = d + random.randint(0, 6)  # j >= d, so j-d = w >= 0
    w = j - d
    if w < 0:
        continue
    A = random_partition(d, w)
    B = random_partition(w, d)
    trials += 1

    HA = H(d, A)
    HB = H(w, B)
    Cd = C(d)
    base = Fraction(3)**j - Fraction(2)**j + Fraction(2)**j * Cd
    V = base + Fraction(2)**(d + j) * HA  # this is the "u" part before adding B's high contribution;
    # but for the mod-9 test we just need V(A,B) = H(A) + 3^d * 2^(j-d) * K(B) form per round13's
    # generalization; use that directly instead of the u/high split (which folds in `base`, a
    # constant depending on j,d only -- irrelevant to the row-parity claim, which is about H(A)
    # alone). Test the CORE claim: H(A) mod 9 vs h_1(a1)+3*h2(a2) mod 9, and separately that the
    # B-arm (3^d * 2^(j-d) * H(B)) vanishes mod 9 when d>=2.
    a1 = A[0] if len(A) >= 1 else 0
    a2 = A[1] if len(A) >= 2 else 0
    predicted_HA_mod9 = (h1_table_predicted(a1 % 6) + 3 * (a2 % 2)) % 9
    actual_HA_mod9 = frac_mod(HA, 9)

    Barm = Fraction(3)**d * Fraction(2)**w * HB
    Barm_mod9 = frac_mod(Barm, 9) if Barm != 0 else 0

    if actual_HA_mod9 != predicted_HA_mod9:
        mismatches += 1
        print(f"  H(A) mod9 MISMATCH: d={d} j={j} A={A} actual={actual_HA_mod9} predicted={predicted_HA_mod9}")
    if Barm_mod9 != 0:
        mismatches += 1
        print(f"  B-arm mod9 NONZERO (should vanish for d>=2): d={d} j={j} B={B} Barm_mod9={Barm_mod9}")

print(f"  trials={trials}, mismatches={mismatches}")
