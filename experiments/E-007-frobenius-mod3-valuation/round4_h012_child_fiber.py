"""Exact witness-level H-012 audit for (ell,j)=(6,10)->(7,11).

An R_{j-1,j} witness is a j-subset A of {0,...,2j-1}, written in
decreasing order in F_j(A)=sum_i 3^i 2^{a_i}.  Its Durfee depth is simply
the number of chosen exponents a>=j.

The canonical j->j+1 embedding of the same Young diagram is

    E(A) = {a+1:a in A} union {0}.

It preserves Durfee depth and satisfies F_{j+1}(E(A))=2F_j(A)+3^j.
Here j=10, so modulo 3^7 this is just 2F_j(A).  Thus the natural child
fiber over a parent residue u mod 3^6 consists of the three residues over
2u mod 3^6.  Restricting to the covering certificate d<=4 at (6,10),
the canonical embeddings attain all but eleven unit children.  For every
missing child this script searches genuine d<=4 parent and d<=5 repaired-
child witnesses, subject to |d_child-d_parent|<=1, and minimizes the number
of exponent replacements from E(A) to the child witness B.

The script also prints unconditioned Durfee-depth image data so that weaker
set-level readings of "Delta d<=1" can be audited separately.
"""

from collections import defaultdict, Counter
from itertools import combinations

import numpy as np


ELL = 6
J = 10
MOD_PARENT = 3**ELL
MOD_CHILD = 3 ** (ELL + 1)
PARENT_DEPTH_CAP = 4
CHILD_DEPTH_CAP = 5


def witness_records(j, modulus):
    """Return residue -> [(bitmask, Durfee depth, decreasing exponent tuple)]."""
    powers2 = [pow(2, a, modulus) for a in range(2 * j)]
    powers3 = [pow(3, i, modulus) for i in range(j)]
    records = defaultdict(list)
    for asc in combinations(range(2 * j), j):
        desc = asc[::-1]
        value = sum(powers3[i] * powers2[a] for i, a in enumerate(desc)) % modulus
        mask = sum(1 << a for a in asc)
        depth = sum(a >= j for a in asc)
        records[value].append((mask, depth, desc))
    return records


def depth_images(records):
    images = defaultdict(set)
    for residue, witnesses in records.items():
        for _, depth, _ in witnesses:
            images[depth].add(residue)
    return images


def ternary(n, width):
    digits = []
    for _ in range(width):
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits))


def fiber_counts_dp(ell, j):
    """Structurally separate 0/1-knapsack DP cross-check of brute enumeration."""
    modulus = 3**ell
    dp = np.zeros((j + 1, modulus), dtype=np.int64)
    dp[0, 0] = 1
    pow3 = [pow(3, k, modulus) for k in range(j)]
    p2 = pow(2, 2 * j - 1, modulus)
    inv2 = pow(2, -1, modulus)
    for t in range(2 * j):
        for k in range(min(j - 1, t), -1, -1):
            dp[k + 1] += np.roll(dp[k], (pow3[k] * p2) % modulus)
        p2 = (p2 * inv2) % modulus
    return dp[j]


def main():
    parent_hi = witness_records(J, MOD_CHILD)
    child = witness_records(J + 1, MOD_CHILD)

    # Validate the canonical embedding identity on every parent witness and
    # build its image, retaining the source witness for repair comparisons.
    embedded_by_residue = defaultdict(list)
    parent_by_low_residue = defaultdict(list)
    for residue_hi, witnesses in parent_hi.items():
        for mask, depth, desc in witnesses:
            if depth > PARENT_DEPTH_CAP:
                continue
            embedded_mask = (mask << 1) | 1
            embedded_desc = tuple(a + 1 for a in desc) + (0,)
            embedded_value = sum(
                pow(3, i, MOD_CHILD) * pow(2, a, MOD_CHILD)
                for i, a in enumerate(embedded_desc)
            ) % MOD_CHILD
            assert embedded_value == (2 * residue_hi) % MOD_CHILD
            assert sum(a >= J + 1 for a in embedded_desc) == depth
            item = (embedded_mask, depth, embedded_desc, desc, residue_hi)
            embedded_by_residue[embedded_value].append(item)
            parent_by_low_residue[residue_hi % MOD_PARENT].append(item)

    units_child = {x for x in range(MOD_CHILD) if x % 3}
    embedded_image = set(embedded_by_residue) & units_child
    child_image = {
        residue
        for residue, witnesses in child.items()
        if any(depth <= CHILD_DEPTH_CAP for _, depth, _ in witnesses)
    } & units_child
    missing = sorted(units_child - embedded_image)

    assert child_image == units_child
    assert len(missing) == 11

    parent_counts_enum = np.array([len(parent_hi[r]) for r in range(MOD_CHILD)])
    child_counts_enum = np.array([len(child[r]) for r in range(MOD_CHILD)])
    parent_counts_dp = fiber_counts_dp(ELL + 1, J)
    child_counts_dp = fiber_counts_dp(ELL + 1, J + 1)
    assert np.array_equal(parent_counts_enum, parent_counts_dp)
    assert np.array_equal(child_counts_enum, child_counts_dp)

    print("=== H-012 exact witness-level child-fiber audit ===")
    print(f"parent witnesses C(20,10)={sum(map(len, parent_hi.values()))}")
    print(f"child witnesses  C(22,11)={sum(map(len, child.values()))}")
    print(f"unit children mod 3^7={len(units_child)}")
    print(
        f"canonical same-diagram image from d<={PARENT_DEPTH_CAP}: "
        f"{len(embedded_image)}; missing={len(missing)}"
    )
    print(f"missing normalized children={missing}")
    print("independent rolling-array DP cross-check: all 2*3^7 fiber counts match for j=10 and j=11")

    # Minimize exponent replacements.  Since both sets have size J+1,
    # replacements = |E(A)\\B| = popcount(E(A) xor B)/2.
    rows = []
    fixed_parent_failures = []
    for target in missing:
        base = target % MOD_PARENT
        source_parent = (pow(2, -1, MOD_PARENT) * base) % MOD_PARENT
        parents = parent_by_low_residue[source_parent]
        children = [record for record in child[target] if record[1] <= CHILD_DEPTH_CAP]

        best = None
        best_pair = None
        best_any = None
        best_any_pair = None
        delta_counter = Counter()
        for emask, dp, edesc, pdesc, parent_hi_residue in parents:
            for cmask, dc, cdesc in children:
                replacements = (emask ^ cmask).bit_count() // 2
                delta = dc - dp
                delta_counter[delta] += 1
                key_any = (replacements, abs(delta), dc, dp, cdesc, pdesc)
                if best_any is None or key_any < best_any:
                    best_any = key_any
                    best_any_pair = (emask, cmask, dp, dc, edesc, cdesc, pdesc, parent_hi_residue)
                if abs(delta) <= 1:
                    key = (replacements, abs(delta), dc, dp, cdesc, pdesc)
                    if best is None or key < best:
                        best = key
                        best_pair = (emask, cmask, dp, dc, edesc, cdesc, pdesc, parent_hi_residue)

        assert best_pair is not None
        emask, cmask, dp, dc, edesc, cdesc, pdesc, parent_hi_residue = best_pair
        removed = tuple(sorted((a for a in range(2 * (J + 1)) if (emask >> a) & 1 and not (cmask >> a) & 1), reverse=True))
        added = tuple(sorted((a for a in range(2 * (J + 1)) if (cmask >> a) & 1 and not (emask >> a) & 1), reverse=True))
        rows.append((target, source_parent, best[0], dc - dp, removed, added))
        print(
            f"target={target:4d} ({ternary(target, ELL+1)}_3), "
            f"source={source_parent:3d}, parent-fiber={len(parents):3d}, child-fiber={len(children):3d}, "
            f"min replacements={best[0]}, d:{dp}->{dc} (delta={dc-dp:+d}), "
            f"remove={removed}, add={added}"
        )
        print(f"  A={pdesc}")
        print(f"  E(A)={edesc}")
        print(f"  B={cdesc}; parent high residue={parent_hi_residue}")
        print(f"  feasible depth deltas={sorted(delta_counter)}")

        # Stronger quantifier: fix each individual parent witness in this
        # exceptional parent fiber, then minimize over child witnesses.
        per_parent = []
        for emask0, dp0, edesc0, pdesc0, parent_hi0 in parents:
            local_best = None
            for cmask0, dc0, cdesc0 in children:
                if abs(dc0 - dp0) > 1:
                    continue
                replacements0 = (emask0 ^ cmask0).bit_count() // 2
                key0 = (replacements0, abs(dc0 - dp0), dc0, cdesc0)
                if local_best is None or key0 < local_best:
                    local_best = key0
            per_parent.append((pdesc0, dp0, parent_hi0, local_best))
        fixed_parent_failures.extend(
            (target, pdesc0, dp0, parent_hi0)
            for pdesc0, dp0, parent_hi0, local_best in per_parent
            if local_best is None
        )
        feasible_costs = sorted(item[3][0] for item in per_parent if item[3] is not None)
        print(
            "  per-parent-witness min replacements under |delta d|<=1: "
            + str(feasible_costs)
            + f"; infeasible fixed parents={len(per_parent)-len(feasible_costs)}"
        )

    print("\n=== Repair summary ===")
    print("replacement histogram:", dict(sorted(Counter(row[2] for row in rows).items())))
    print("depth-delta histogram:", dict(sorted(Counter(row[3] for row in rows).items())))
    print("maximum replacements under |Delta d|<=1:", max(row[2] for row in rows))
    print(
        "fixed-parent failures among exceptional fibers (the universal-witness version):",
        len(fixed_parent_failures),
    )

    # Weaker existential depth-profile check on every natural parent/child
    # fiber, independent of the actual exponent-edit distance.
    parent_depths = defaultdict(set)
    for residue_hi, witnesses in parent_hi.items():
        for _, depth, _ in witnesses:
            if depth <= PARENT_DEPTH_CAP:
                parent_depths[residue_hi % MOD_PARENT].add(depth)
    child_depths = defaultdict(set)
    for residue, witnesses in child.items():
        for _, depth, _ in witnesses:
            if depth <= CHILD_DEPTH_CAP:
                child_depths[residue].add(depth)

    failures_abs = []
    failures_up = []
    for u, depths_p in parent_depths.items():
        base = (2 * u) % MOD_PARENT
        for digit in range(3):
            target = base + digit * MOD_PARENT
            depths_c = child_depths[target]
            if not any(abs(dc - dp) <= 1 for dp in depths_p for dc in depths_c):
                failures_abs.append((u, target, sorted(depths_p), sorted(depths_c)))
            if not any(dc <= dp + 1 for dp in depths_p for dc in depths_c):
                failures_up.append((u, target, sorted(depths_p), sorted(depths_c)))
    print("\n=== All 1458 normalized child fibers: existential depth checks ===")
    print(f"failures for |d_child-d_parent|<=1: {len(failures_abs)}")
    print(f"failures for d_child<=d_parent+1: {len(failures_up)}")

    # Cross-check exact stratum-image sizes directly from witness enumeration.
    p_images = depth_images(parent_hi)
    c_images = depth_images(child)
    print("\n=== Direct witness-enumeration stratum sizes (unit residues) ===")
    for depth in sorted(p_images):
        print(f"j=10 d={depth}: {len(p_images[depth] & units_child)} residues mod 3^7")
    for depth in sorted(c_images):
        print(f"j=11 d={depth}: {len(c_images[depth] & units_child)} residues mod 3^7")

    for cap in range(0, J + 2):
        cumulative = set().union(*(c_images[d] for d in range(cap + 1))) & units_child
        print(f"j=11 cumulative d<= {cap}: {len(cumulative)}/{len(units_child)}")
        if cumulative == units_child:
            break


if __name__ == "__main__":
    main()
