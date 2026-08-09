"""H-011 round 4: witness-preserving boundary maps and finite mask state.

Notation
--------
S(m,j) is the support modulo 3**m of

    F_j(a_0,...,a_{j-1}) = sum_{i=0}^{j-1} 3**i * 2**a_i,

where 2*j-1 >= a_0 > ... > a_{j-1} >= 0.

The two unconditional boundary-safe injections from j-tuples to (j+1)-tuples are

    I_2(A) = (a_0+1,...,a_{j-1}+1,0),
    I_4(A) = (a_0+2,...,a_{j-1}+2,0).

They satisfy F_{j+1}(I_2(A)) = 2*F_j(A)+3**j and
F_{j+1}(I_4(A)) = 4*F_j(A)+3**j.  Thus, when j >= m,

    2*S(m,j) union 4*S(m,j)  subseteq  S(m,j+1).                 (1)

At the real transitions checked below, equality in (1) holds at every one-budget
step except the small (m,j)=(4,4) step.  Iterating (1) handles Delta j=2.

Why this is a genuine boundary-state reduction
------------------------------------------------
Modulo 3**m, a tuple's value only depends on its first m (largest-exponent)
entries.  A decreasing m-prefix extends to a J-tuple iff its last entry is at
least J-m.  Therefore every visible prefix for a (j+1)-tuple is literally in
the I_2 image if a_0 <= 2*j, and is literally in the I_4 image if
a_{m-1} >= j-m+2.  The only prefixes not covered by this argument have the two
simultaneous boundary equalities

    a_0 = 2*j+1  and  a_{m-1} = j-m+1.                           (2)

Consequently, the computational reverse inclusion in (1) is reduced to the
single doubly-boundary-saturated prefix class (2), rather than arbitrary
tuples/carries/slack.

For q=3**n and support known modulo 3*q, define the lift mask

    M_S(r) = {a in {0,1,2}: r+a*q belongs to S}.

Multiplication by mu in {2,4} sends its digits by

    a |-> floor(mu*r/q) + mu*a  (mod 3).

Hence, under equality in (1), the exact new mask at x is the union of the two
permuted predecessor masks at 2^{-1}x and 4^{-1}x.  The finite state has at most

    (8 masks * 2 carries) * (8 masks * 3 carries) = 384

types.  No witness slack flag is needed for the two injections: both maps are
always admissible.  The census below reports how many of these types occur.
"""

from collections import Counter

import numpy as np


JSTAR = {
    2: 4,
    3: 6,
    4: 7,
    5: 9,
    6: 10,
    7: 11,
    8: 12,
    9: 13,
    10: 15,
    11: 16,
    12: 17,
}


def support(m, j):
    """Exact Boolean support S(m,j), using the repository's verified rotation DP."""
    modulus = 3**m
    dp = np.zeros((j + 1, modulus), dtype=bool)
    dp[0, 0] = True
    powers3 = [pow(3, k, modulus) for k in range(j)]
    power2 = pow(2, 2 * j - 1, modulus)
    inverse2 = pow(2, -1, modulus)

    # Scan possible exponents from 2*j-1 down to 0.  If it is the kth selected
    # exponent, its contribution is 3**k * 2**exponent.
    for exponent_step in range(2 * j):
        for k in range(min(j - 1, exponent_step), -1, -1):
            shift = powers3[k] * power2 % modulus
            dp[k + 1] |= np.roll(dp[k], shift)
        power2 = power2 * inverse2 % modulus
    return set(np.flatnonzero(dp[j]))


def lift_mask_bits(support_high, r, q):
    """Bit a is one iff r+a*q is present in support modulo 3*q."""
    return sum((int(r + a * q in support_high) << a) for a in range(3))


def boundary_step(support_high, modulus):
    """The support supplied by I_2 and I_4 at one extra budget unit."""
    return (
        {2 * x % modulus for x in support_high}
        | {4 * x % modulus for x in support_high}
    )


def corner_support(m, j):
    """Residues of the sole prefix class not literally covered by I_2 or I_4.

    The fixed visible endpoints are a_0=2*j+1 and a_{m-1}=j-m+1.
    Choose the m-2 middle entries from [j-m+2, 2*j].
    """
    modulus = 3**m
    bottom = j - m + 1
    dp = np.zeros((m - 1, modulus), dtype=bool)
    fixed = (
        pow(2, 2 * j + 1, modulus)
        + pow(3, m - 1, modulus) * pow(2, bottom, modulus)
    ) % modulus
    dp[0, fixed] = True
    power2 = pow(2, 2 * j, modulus)
    inverse2 = pow(2, -1, modulus)
    middle_pool_size = j + m - 1
    for exponent_step in range(middle_pool_size):
        for k in range(min(m - 3, exponent_step), -1, -1):
            # k middle entries have been selected; the new one's rank is k+1.
            shift = pow(3, k + 1, modulus) * power2 % modulus
            dp[k + 1] |= np.roll(dp[k], shift)
        power2 = power2 * inverse2 % modulus
    return set(np.flatnonzero(dp[m - 2]))


def permute_mask(mask, multiplier, carry):
    """Mask permutation a -> carry + multiplier*a (mod 3)."""
    out = 0
    for a in range(3):
        if mask & (1 << a):
            out |= 1 << ((carry + multiplier * a) % 3)
    return out


def predecessor_state(support_high, x, q):
    """(mask,carry) for the inverse images under 2 and 4, in that order."""
    state = []
    for multiplier in (2, 4):
        r = x * pow(multiplier, -1, q) % q
        carry = (multiplier * r // q) % 3
        state.extend((lift_mask_bits(support_high, r, q), carry))
    return tuple(state)


print("=== Exact support equality from the two boundary injections ===")
print("l  m   j->j'  delta    |S_j|    |S_j'|  |boundary|  equal  missing")

supports = {}


def get_support(m, j):
    key = (m, j)
    if key not in supports:
        supports[key] = support(m, j)
    return supports[key]


for ell in range(2, 12):
    m = ell + 2
    j = JSTAR[ell]
    j_next = JSTAR[ell + 1]
    modulus = 3**m
    old = get_support(m, j)
    boundary = old
    for _budget in range(j, j_next):
        boundary = boundary_step(boundary, modulus)
    new = get_support(m, j_next)
    missing = sorted(new - boundary)
    assert boundary <= new  # the two explicit tuple injections prove this too
    print(
        f"{ell:>1} {m:>2}  {j:>2}->{j_next:<2}    {j_next-j:>1}  "
        f"{len(old):>8} {len(new):>9} {len(boundary):>11}  "
        f"{str(boundary == new):>5}  {missing}"
    )


print("\n=== Reverse inclusion reduced to the doubly-saturated corner ===")
print(
    "m   j->j+1  corner-residues  only-2  only-4  both  none  "
    "all-new-outside-boundary"
)
for ell in range(2, 12):
    m = ell + 2
    first_budget = JSTAR[ell]
    last_budget = JSTAR[ell + 1]
    modulus = 3**m
    for j in range(first_budget, last_budget):
        old = get_support(m, j)
        new = get_support(m, j + 1)
        image2 = {2 * x % modulus for x in old}
        image4 = {4 * x % modulus for x in old}
        boundary = image2 | image4
        corner = corner_support(m, j)
        corner_outside = corner - boundary
        all_outside = new - boundary
        # This is also proved by the visible-prefix argument in the module docstring.
        assert corner_outside == all_outside
        only2 = len((corner & image2) - image4)
        only4 = len((corner & image4) - image2)
        both = len(corner & image2 & image4)
        print(
            f"{m:>2}  {j:>2}->{j+1:<2} {len(corner):>16} "
            f"{only2:>7} {only4:>7} {both:>5} {len(corner_outside):>5}  "
            f"{str(sorted(all_outside))}"
        )


print("\n=== Direct witness-map repair of old holes ===")
print("l  n   j->j'  holes  required_children  supplied  failures  predecessor-carries")
for ell in range(2, 12):
    n = ell + 1
    m = n + 1
    j = JSTAR[ell]
    j_next = JSTAR[ell + 1]
    delta = j_next - j
    multiplier = 2**delta
    q = 3**n
    old = get_support(m, j)
    old_projection = {z % q for z in old}
    holes = [x for x in range(q) if x % 3 and x not in old_projection]
    inverse = pow(multiplier, -1, q)
    carry_counts = Counter()
    failures = []
    supplied = 0
    for x in holes:
        predecessor = x * inverse % q
        carry_counts[(multiplier * predecessor // q) % 3] += 1
        predecessor_lifts = [predecessor + a * q for a in range(3)]
        is_full = all(z in old for z in predecessor_lifts)
        if not is_full:
            failures.append(x)
        else:
            # Iterating I_2 maps these three actual witnesses bijectively onto
            # the three children of x at the new budget.
            supplied += 3
    print(
        f"{ell:>1} {n:>2}  {j:>2}->{j_next:<2}  {len(holes):>5} "
        f"{3*len(holes):>18} {supplied:>9} {len(failures):>9}  "
        f"{dict(sorted(carry_counts.items()))}"
    )
    assert not failures


print("\n=== Occupied exact two-predecessor states on Delta-j=1 transitions ===")
print("l  n   j->j'  occupied (of at most 384)  equality-check")
all_states = set()
for ell in range(2, 12):
    j = JSTAR[ell]
    j_next = JSTAR[ell + 1]
    if j_next != j + 1:
        continue
    n = ell + 1
    m = n + 1
    q = 3**n
    old = get_support(m, j)
    new = get_support(m, j_next)
    states = Counter()
    exact = True
    for x in range(q):
        if x % 3 == 0:
            continue
        state = predecessor_state(old, x, q)
        states[state] += 1
        mask2, carry2, mask4, carry4 = state
        predicted = (
            permute_mask(mask2, 2, carry2)
            | permute_mask(mask4, 4, carry4)
        )
        actual = lift_mask_bits(new, x, q)
        exact &= predicted == actual
    all_states.update(states)
    print(
        f"{ell:>1} {n:>2}  {j:>2}->{j_next:<2} {len(states):>12}"
        f"{str(exact):>25}"
    )
    assert exact
print(f"union of occupied state labels across these levels: {len(all_states)} / 384")


print("\n=== Bare-mask counterexample (n=4, j=6 -> 7) ===")
n = 4
q = 3**n
old = get_support(n + 1, 6)
new = get_support(n + 1, 7)
for r in (5, 50):
    old_mask = lift_mask_bits(old, r, q)
    carry = 2 * r // q
    x = 2 * r % q
    induced = permute_mask(old_mask, 2, carry)
    actual = lift_mask_bits(new, x, q)
    print(
        f"r={r:>2}: old-mask={old_mask:03b}, carry={carry}, x=2r mod 81={x:>2}, "
        f"induced-mask={induced:03b}, actual-mask={actual:03b}"
    )
assert lift_mask_bits(old, 5, q) == lift_mask_bits(old, 50, q) == 0b001
assert 2 * 5 // q != 2 * 50 // q


print("\n=== One mask plus its carry is still insufficient ===")
print("The second predecessor distinguishes these two exact transitions:")
for r in (5, 16):
    old_mask = lift_mask_bits(old, r, q)
    carry = 2 * r // q
    x = 2 * r % q
    actual = lift_mask_bits(new, x, q)
    second_predecessor = x * pow(4, -1, q) % q
    second_mask = lift_mask_bits(old, second_predecessor, q)
    print(
        f"r={r:>2}: (old-mask,carry)=({old_mask:03b},{carry}), x={x:>2}, "
        f"second-predecessor-mask={second_mask:03b}, actual-mask={actual:03b}"
    )
assert lift_mask_bits(old, 5, q) == lift_mask_bits(old, 16, q) == 0b001
assert 2 * 5 // q == 2 * 16 // q == 0
assert lift_mask_bits(new, 10, q) == 0b001
assert lift_mask_bits(new, 32, q) == 0b111


print("\n=== Concrete witness triple for one repaired hole ===")
print("At n=4, j=6, x=25 is a hole mod 81; its inverse under 2 is r=53.")
print("Source witnesses modulo 243 and their I_2 images:")
witnesses = {
    53: (11, 10, 4, 3, 1, 0),
    134: (11, 10, 6, 2, 1, 0),
    215: (11, 8, 5, 2, 1, 0),
}
assert 25 not in {z % 81 for z in old}
for source_value, source_tuple in witnesses.items():
    target_tuple = tuple(a + 1 for a in source_tuple) + (0,)
    checked_source = sum(3**i * 2**a for i, a in enumerate(source_tuple)) % 243
    checked_target = sum(3**i * 2**a for i, a in enumerate(target_tuple)) % 243
    assert checked_source == source_value
    assert checked_target == 2 * source_value % 243
    print(
        f" {source_value:>3}: {source_tuple} -> {checked_target:>3}: {target_tuple}"
    )
assert {2 * source_value % 243 for source_value in witnesses} == {25, 106, 187}
