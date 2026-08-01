"""
Independent verification of Codex round-2 claims (lateral-thinking cycle,
/tmp/codex_lateral_round2_out.txt), plus data-gathering for round 3.

Checks:
1. The window-2 "revise-then-append" congruence:
     V_{r+1}(P_d) - V_r(P) = 3^{r-1} 2^a (4^d - 1) + 3^r 2^b
                            ≡ 3^r (2^a d + 2^b)  (mod 3^{r+1})
   and that d=0,1,2 really does realize all three ternary digit lifts at level r,
   for concrete numeric prefixes (not just algebra).
2. Data for round 3: the collision statistic kappa_{j,l} and the lift-mask
   distribution L_{j,l}(m), computed directly from brute-force fiber counts
   (l=2..8), as Codex requested as a non-tautological test of fiber balance.

(The Macdonald eigenvalue citation, Macdonald *Symmetric Functions and Hall
Polynomials* 2nd ed., Ch VI §4, formula (4.15), p.324, was checked separately
by fetching the primary source PDF directly -- confirmed exact, page and
formula number both correct, see round-3 prompt / notes/H-003.md.)
"""
import random
from itertools import combinations
from math import comb

random.seed(1)

# ---------- Check 1: window-2 gadget ----------

def V(alphas):
    """alphas: list of exponents at positions 0..len-1 (position i weight 3^i)."""
    return sum(3**i * 2**a for i, a in enumerate(alphas))

print("=== Check 1: window-2 revise-then-append gadget ===")
ok = True
for trial in range(50):
    r = random.randint(2, 8)
    a = random.randint(10, 40)          # position r-1 exponent for d=0
    b = random.randint(0, a - 1)        # position r exponent, must be < a (most restrictive case)
    prev = a + 5 + random.randint(0, 10)  # position r-2 exponent, must exceed a+4
    # build an arbitrary strictly-decreasing prefix for positions 0..r-2
    prefix = [prev]
    cur = prev
    for _ in range(r - 2):
        cur += random.randint(1, 5)
        prefix.append(cur)
    prefix = list(reversed(prefix))  # positions 0..r-2, strictly decreasing left to right is
                                      # NOT what we need; we need alpha_0>alpha_1>...>alpha_{r-2}=prev
    # Actually just construct directly: alpha_0 > alpha_1 > ... > alpha_{r-3} > alpha_{r-2}=prev
    prefix = []
    cur = prev
    for i in range(r - 1):
        prefix.append(cur)
        cur += random.randint(1, 5)
    prefix = list(reversed(prefix))  # now strictly decreasing, prefix[-1] == prev
    assert prefix[-1] == prev
    assert all(prefix[i] > prefix[i+1] for i in range(len(prefix)-1))

    V_r_base = V(prefix)  # this is V_{r-1} in the paper's indexing (sum over positions 0..r-2)
    Vr_original = V_r_base + 3**(r-1) * 2**a  # V_r(P): append original a at position r-1

    digits = []
    for d in (0, 1, 2):
        a_d = a + 2 * d
        assert prev > a_d > b, f"ordering violated: prev={prev} a_d={a_d} b={b}"
        Vr1 = V_r_base + 3**(r-1) * 2**a_d + 3**r * 2**b
        diff = Vr1 - Vr_original
        expected_closed_form = 3**(r-1) * 2**a * (4**d - 1) + 3**r * 2**b
        if diff != expected_closed_form:
            ok = False
            print(f"  CLOSED-FORM MISMATCH r={r} a={a} b={b} d={d}: diff={diff} expected={expected_closed_form}")
        mod = 3**(r+1)
        diff_mod = diff % mod
        expected_mod = (3**r * (2**a * d + 2**b)) % mod
        if diff_mod != expected_mod:
            ok = False
            print(f"  MOD-{mod} MISMATCH r={r} a={a} b={b} d={d}: diff_mod={diff_mod} expected_mod={expected_mod}")
        # digit at level r: (Vr1 mod 3^{r+1}) // 3^r  minus (Vr_original's digit contribution)
        digit_r = (diff_mod // (3**r)) % 3
        digits.append(digit_r)

    if sorted(digits) != [0, 1, 2]:
        ok = False
        print(f"  DID NOT REALIZE ALL 3 LIFTS: r={r} a={a} b={b} digits={digits}")

print(f"  50 random trials: {'ALL PASS (closed form exact, all 3 lifts realized)' if ok else 'FAILURES FOUND'}")

# ---------- Check 2: data for round 3 (kappa, lift-mask) ----------

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12,9:13,10:15,11:16,12:17,13:18,14:19,15:20,
         16:20,17:21,18:22,19:23,20:24,21:25,22:26,23:27}

def fiber_counts(j, l):
    mod = 3**l
    counts = [0] * mod
    for combo in combinations(range(2*j), j):
        alphas = sorted(combo, reverse=True)
        val = sum(3**i * 2**a for i, a in enumerate(alphas)) % mod
        counts[val] += 1
    return counts

def is_unit(x):
    return x % 3 != 0

print("\n=== Check 2: kappa_{j,l} collision statistic and lift-mask L_{j,l}(m), at j*(l)-1 ===")
print(f"{'l':>3} {'j*-1':>5} {'N':>10} {'U':>8} {'kappa':>10}   L(0) L(1) L(2) L(3)")
for l in range(2, 9):
    jm1 = JSTAR[l] - 1
    mod = 3**l
    N = comb(2*jm1, jm1)
    U = 2 * 3**(l-1)
    counts = fiber_counts(jm1, l)

    # kappa: U/(N(N-1)) * sum_x n_x(n_x-1), over units x mod 3^l
    s = 0
    for x in range(mod):
        if is_unit(x):
            n = counts[x]
            s += n * (n - 1)
    kappa = (U / (N * (N - 1))) * s

    # lift-mask L(m), FIXED: since x mod 3 = xbar mod 3 for x = xbar + u*3^(l-1) (l>=2), a
    # parent xbar's unit-ness mod 3 determines ALL THREE lifts' unit-ness at once (never mixed).
    # Restricting to non-unit xbar trivially forces m=0 for all 3 (structurally, since F_j never
    # produces non-unit values at all -- verified below), so that bucket carries no information
    # about coverage; the meaningful quantity restricts xbar to UNIT parent classes only.
    mod_parent = 3**(l - 1)
    # sanity: confirm every nonzero-count residue really is a unit mod 3 (F_j always odd-mod-3)
    nonunit_nonzero = [x for x in range(mod) if not is_unit(x) and counts[x] > 0]
    assert not nonunit_nonzero, f"l={l}: found nonzero counts at non-unit residues: {nonunit_nonzero[:5]}"

    L = [0, 0, 0, 0]
    trivial_nonunit_parents = 0
    for xbar in range(mod_parent):
        if not is_unit(xbar):
            trivial_nonunit_parents += 1
            continue  # excluded: structurally always m=0, not a real signal
        m = 0
        for u in range(3):
            xl = xbar + u * mod_parent
            if counts[xl] > 0:
                m += 1
        L[m] += 1

    print(f"{l:>3} {jm1:>5} {N:>10} {U:>8} {kappa:>10.4f}   {L[0]:>4} {L[1]:>4} {L[2]:>4} {L[3]:>4}"
          f"   (excluded {trivial_nonunit_parents} trivial non-unit parents)")

print("\nNote: L(m) now restricted to UNIT parent classes mod 3^(l-1) only (see fix comment above --")
print("the original formula's non-unit-parent bucket was a pure artifact: F_j never produces a")
print("non-unit value, so non-unit parents trivially have m=0 for all l, confirmed by assertion).")
print("L(0) here (unit parent, but NONE of its 3 unit children are hit) is the real 'deterministic")
print("hole' signal Codex was after; L(3) is full 3-way splitting.")
