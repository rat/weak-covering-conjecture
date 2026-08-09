"""Exact falsification of the unchanged Delta-j=1 H-012 induction.

The requested (6,10)->(7,11) transition succeeds (see
round4_h012_child_fiber.py), as does the next transition.  But iterating that
same budget rule from the covered base (6,10) reaches (10,14), and R_{13,14}
misses two units modulo 3^10.  Hence no witness repair of any Durfee depth,
let alone one with Delta d<=1, exists for those children at cost Delta j=1.

This script identifies the two children with an exact fiber-count DP and
cross-checks their identities with a structurally separate big-integer
support-bitset DP.  It also supplies explicit witnesses for their normalized
parents at (ell,j)=(9,13).
"""

from math import comb

import numpy as np


def fiber_counts_dp(ell, j):
    modulus = 3**ell
    dp = np.zeros((j + 1, modulus), dtype=np.int64)
    dp[0, 0] = 1
    p3 = [pow(3, k, modulus) for k in range(j)]
    p2 = pow(2, 2 * j - 1, modulus)
    inv2 = pow(2, -1, modulus)
    for t in range(2 * j):
        for k in range(min(j - 1, t), -1, -1):
            dp[k + 1] += np.roll(dp[k], (p3[k] * p2) % modulus)
        p2 = (p2 * inv2) % modulus
    assert int(dp[j].sum()) == comb(2 * j, j)
    return dp[j]


def support_bitset_dp(ell, j):
    """Support only, using cyclic rotations of Python integer bitsets."""
    modulus = 3**ell
    full = (1 << modulus) - 1
    state = [0] * (j + 1)
    state[0] = 1
    for t, exponent in enumerate(range(2 * j - 1, -1, -1)):
        for k in range(min(j - 1, t), -1, -1):
            shift = (pow(3, k, modulus) * pow(2, exponent, modulus)) % modulus
            bits = state[k]
            rotated = ((bits << shift) | (bits >> (modulus - shift))) & full
            state[k + 1] |= rotated
    return state[j]


def holes_from_counts(counts):
    return [r for r, count in enumerate(counts) if r % 3 and count == 0]


def holes_from_bits(bits, modulus):
    return [r for r in range(modulus) if r % 3 and not ((bits >> r) & 1)]


def F(exponents):
    return sum(3**i * 2**a for i, a in enumerate(exponents))


def ternary(n, width):
    out = []
    for _ in range(width):
        out.append(str(n % 3))
        n //= 3
    return "".join(reversed(out))


def main():
    cases = ((9, 13), (10, 14), (10, 15))
    count_results = {}
    bit_results = {}
    for ell, j in cases:
        counts = fiber_counts_dp(ell, j)
        bits = support_bitset_dp(ell, j)
        holes_counts = holes_from_counts(counts)
        holes_bits = holes_from_bits(bits, 3**ell)
        assert holes_counts == holes_bits
        count_results[(ell, j)] = counts
        bit_results[(ell, j)] = bits
        units = 2 * 3 ** (ell - 1)
        print(
            f"ell={ell}, j={j}: tuples={int(counts.sum())}, "
            f"covered units={units-len(holes_counts)}/{units}, holes={holes_counts}"
        )

    holes = holes_from_counts(count_results[(10, 14)])
    assert holes == [37912, 47389]
    assert not holes_from_counts(count_results[(9, 13)])
    assert not holes_from_counts(count_results[(10, 15)])

    # Backtracked exact parent witnesses in R_{12,13}.  Their same-diagram
    # embeddings E(A) cover one child over the normalized base 2F(A); the
    # listed j=14 hole is another child over that same base.
    certificates = (
        (37912, (21, 20, 14, 13, 12, 10, 8, 7, 5, 4, 3, 2, 1)),
        (47389, (23, 19, 13, 11, 10, 9, 7, 6, 5, 4, 3, 2, 1)),
    )
    mod9 = 3**9
    mod10 = 3**10
    print("\nUnrepaired-child certificates:")
    for target, parent in certificates:
        parent_value = F(parent)
        embedded = tuple(a + 1 for a in parent) + (0,)
        embedded_value = F(embedded)
        assert embedded_value % mod10 == (2 * parent_value) % mod10
        assert target % mod9 == embedded_value % mod9
        assert count_results[(9, 13)][parent_value % mod9] > 0
        assert count_results[(10, 14)][target] == 0
        assert count_results[(10, 15)][target] > 0
        depth = sum(a >= 13 for a in parent)
        digit_jump = ((target - embedded_value) % mod10) // mod9
        print(
            f"target={target}={ternary(target,10)}_3, parent={parent_value%mod9}, "
            f"A={parent}, d(A)={depth}, E(A) mod 3^10={embedded_value%mod10}, "
            f"missing child jump={digit_jump}*3^9"
        )

    print(
        "\nConclusion: (9,13) covers every unit mod 3^9, but two of its normalized "
        "children have no (10,14) witness at any Durfee depth.  The unchanged "
        "Delta-j=1 induction from (6,10) is therefore false; Delta j=2 repairs both."
    )


if __name__ == "__main__":
    main()
