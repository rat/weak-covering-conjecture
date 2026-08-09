"""Exact H-012 witness transition audit for (ell,j)=(6,10)->(7,11).

This uses direct exponent-tuple enumeration, independently of the Durfee
factorization code.  For

    F_j(alpha) = sum_{i=0}^{j-1} 3^i 2^{alpha_i},
    2j-1 >= alpha_0 > ... > alpha_{j-1} >= 0,

the associated partition has Durfee size

    d(alpha) = #{i : alpha_i >= j}.

The parent certificate is restricted to d<=4 (=ell-2), and the child
certificate to d'<=5.  Child fibers use the project's raw-F convention:
x is a child of r when x == r (mod 3^6).

For an actual witness-edit diagnostic, the canonical budget lift is

    E(alpha) = (alpha_0+1, ..., alpha_9+1, 0).

It preserves the Ferrers partition and its Durfee size.  It doubles raw F
(mod 3^7); equivalently, it preserves 2^{-j} F.  Exchange distance is the
number of occupied exponents replaced when passing from E(alpha) to a child
witness beta.
"""

from collections import Counter, defaultdict
from itertools import combinations


ELL = 6
J = 10
MOD_PARENT = 3**ELL
MOD_CHILD = 3 ** (ELL + 1)
PARENT_D_CAP = 4
CHILD_D_CAP = 5


def tuple_value(alpha, modulus):
    return sum(
        pow(3, i, modulus) * pow(2, exponent, modulus)
        for i, exponent in enumerate(alpha)
    ) % modulus


def durfee_size(alpha, j):
    # lambda_{i+1} >= i+1 iff alpha_i >= j.
    return sum(exponent >= j for exponent in alpha)


def enumerate_witnesses(j, modulus, d_cap):
    for ascending in combinations(range(2 * j), j):
        alpha = tuple(reversed(ascending))
        d = durfee_size(alpha, j)
        if d <= d_cap:
            yield tuple_value(alpha, modulus), d, alpha


def exponent_mask(alpha):
    return sum(1 << exponent for exponent in alpha)


parents = defaultdict(list)
parent_lifts = defaultdict(set)
embedded_lifts = defaultdict(set)
for value, d, alpha in enumerate_witnesses(J, MOD_CHILD, PARENT_D_CAP):
    parent = value % MOD_PARENT
    embedded = tuple(exponent + 1 for exponent in alpha) + (0,)
    parents[parent].append((value, d, alpha, exponent_mask(embedded)))
    parent_lifts[parent].add(value)
    # F_{j+1}(E(alpha)) == 2 F_j(alpha) (mod 3^7), since 3^10 vanishes.
    embedded_lifts[(2 * parent) % MOD_PARENT].add((2 * value) % MOD_CHILD)

children = defaultdict(list)
for value, d, beta in enumerate_witnesses(J + 1, MOD_CHILD, CHILD_D_CAP):
    children[value].append((d, beta, exponent_mask(beta)))

units_parent = [r for r in range(MOD_PARENT) if r % 3]
units_child = [x for x in range(MOD_CHILD) if x % 3]

assert sum(map(len, parents.values())) == 60_626
assert set(parents) == set(units_parent)
assert sum(map(len, children.values())) == 352_716
assert set(children) == set(units_child)

mask_census = Counter(len(parent_lifts[r]) for r in units_parent)
assert mask_census == Counter({3: 476, 2: 9, 1: 1})

raw_holes = [x for x in units_child if x not in parent_lifts[x % MOD_PARENT]]
expected_raw_holes = [37, 262, 532, 748, 910, 1001, 1216, 1531, 1621, 1720, 1936]
assert raw_holes == expected_raw_holes

embedded_mask_census = Counter(len(embedded_lifts[r]) for r in units_parent)
assert embedded_mask_census == mask_census
embedded_holes = [x for x in units_child if x not in embedded_lifts[x % MOD_PARENT]]
expected_embedded_holes = [74, 245, 524, 875, 1055, 1064, 1253, 1496, 1685, 1820, 2002]
assert embedded_holes == expected_embedded_holes

child_min_d = {x: min(d for d, _, _ in records) for x, records in children.items()}
parent_d_sets = {
    r: sorted({d for _, d, _, _ in records}) for r, records in parents.items()
}

expected_hole_min_d = {
    37: 3,
    262: 3,
    532: 3,
    748: 3,
    910: 2,
    1001: 2,
    1216: 4,
    1531: 2,
    1621: 3,
    1720: 3,
    1936: 3,
}
assert {x: child_min_d[x] for x in raw_holes} == expected_hole_min_d
assert all(
    child_min_d[x] <= max(parent_d_sets[x % MOD_PARENT]) + 1 for x in raw_holes
)

# Compute the full normalized witness-edit transition table.  The canonical
# lift E(alpha) sends a raw parent r to 2r mod 3^6, so its three correct target
# children are 2r+t*3^6, not r+t*3^6.  Minimize exchange distance among new
# witnesses satisfying d'<=d+1.  This supports all three quantifier checks:
# per-child existential, one selected witness per parent, and universal over
# every old witness.
global_child_distance = {}
global_child_pair = {}
selected_parent_radius = {}
selected_parent_witness = {}
universal_failure_witnesses = 0
universal_failure_instances = 0

for parent, parent_records in parents.items():
    embedded_parent = (2 * parent) % MOD_PARENT
    best_parent_radius = 99
    best_parent_record = None

    for old_value, d, alpha, embedded_mask in parent_records:
        distances = []
        child_pairs = []

        for digit in range(3):
            child = embedded_parent + digit * MOD_PARENT
            best_distance = 99
            best_pair = None

            for d_prime, beta, beta_mask in children[child]:
                if d_prime <= d + 1:
                    distance = (embedded_mask ^ beta_mask).bit_count() // 2
                    if distance < best_distance:
                        best_distance = distance
                        best_pair = (d_prime, beta)

            distances.append(best_distance)
            child_pairs.append(best_pair)

            if best_distance < global_child_distance.get(child, 99):
                global_child_distance[child] = best_distance
                global_child_pair[child] = (
                    old_value,
                    d,
                    alpha,
                    best_pair[0],
                    best_pair[1],
                )

        failed = sum(distance == 99 for distance in distances)
        if failed:
            universal_failure_witnesses += 1
            universal_failure_instances += failed
        else:
            radius = max(distances)
            if radius < best_parent_radius:
                best_parent_radius = radius
                best_parent_record = (old_value, d, alpha, tuple(distances), child_pairs)

    selected_parent_radius[parent] = best_parent_radius
    selected_parent_witness[parent] = best_parent_record


child_distance_census = Counter(global_child_distance.values())
assert child_distance_census == Counter({0: 1447, 1: 2, 2: 1, 3: 7, 4: 1})
assert set(global_child_distance) == set(units_child)
assert {x for x, distance in global_child_distance.items() if distance == 4} == {1253}

hole_distance_census = Counter(global_child_distance[x] for x in embedded_holes)
assert hole_distance_census == Counter({1: 2, 2: 1, 3: 7, 4: 1})

selected_radius_census = Counter(selected_parent_radius.values())
assert selected_radius_census == Counter({1: 462, 2: 10, 3: 13, 4: 1})
assert universal_failure_witnesses == 53
assert universal_failure_instances == 67

# Explicit universal-quantifier counterexample.
counterexample_alpha = tuple(range(9, -1, -1))
counterexample_value = tuple_value(counterexample_alpha, MOD_CHILD)
assert counterexample_value == 1163
assert counterexample_value % MOD_PARENT == 434
assert durfee_size(counterexample_alpha, J) == 0
counterexample_embedded_parent = (2 * 434) % MOD_PARENT
counterexample_child_minima = tuple(
    child_min_d[counterexample_embedded_parent + digit * MOD_PARENT]
    for digit in range(3)
)
assert counterexample_embedded_parent == 139
assert counterexample_child_minima == (0, 2, 1)

# Static child coverage really needs d'=5 only at residue 2002.  Under the
# canonical base permutation its old parent is r=272, whose available depths
# include d=4, so the selectable form is tight at Delta d=+1.
child_d4_image = {
    x for x, records in children.items() if any(d <= 4 for d, _, _ in records)
}
assert set(units_child) - child_d4_image == {2002}
assert child_min_d[2002] == 5
assert len(children[2002]) == 173
canonical_parent_2002 = (pow(2, -1, MOD_PARENT) * (2002 % MOD_PARENT)) % MOD_PARENT
assert canonical_parent_2002 == 272
assert parent_d_sets[canonical_parent_2002] == [3, 4]


print("=== H-012 exact witness transition: (6,10,d<=4) -> (7,11,d'<=5) ===")
print(f"parent witnesses: {sum(map(len, parents.values())):,}; covered units: {len(parents)}/486")
print(f"child witnesses:  {sum(map(len, children.values())):,}; covered units: {len(children)}/1458")
print(f"old-budget lift masks: {dict(sorted(mask_census.items()))}")
print(f"raw-F old-budget holes ({len(raw_holes)}): {raw_holes}")
print()
print("hole  parent  old digits  parent d-set  min child d  delta from max parent d")
for child in raw_holes:
    parent = child % MOD_PARENT
    old_digits = tuple(
        digit
        for digit in range(3)
        if parent + digit * MOD_PARENT in parent_lifts[parent]
    )
    d_set = parent_d_sets[parent]
    minimum = child_min_d[child]
    print(
        f"{child:4d}  {parent:4d}    {old_digits!s:9s}  {d_set!s:12s}"
        f" {minimum:6d} {minimum - max(d_set):12d}"
    )

print()
print(f"canonical-embedded holes ({len(embedded_holes)}): {embedded_holes}")
print(f"normalized all-child minimum exchange distance: {dict(sorted(child_distance_census.items()))}")
print(f"embedded-hole minimum exchange distance: {dict(sorted(hole_distance_census.items()))}")
print(f"one selected witness per parent, normalized max-of-three radius: {dict(sorted(selected_radius_census.items()))}")
print(
    "universal every-witness version: FAIL -- "
    f"{universal_failure_witnesses} witnesses, {universal_failure_instances} child instances"
)
print(
    "counterexample: raw parent 434 -> embedded parent 139, "
    "alpha=(9,8,...,0), d=0, F mod 2187=1163; "
    f"embedded-child minimum d values={counterexample_child_minima}"
)
print(
    "unique child requiring d'=5: 2002 "
    "(173 child witnesses; canonical parent 272 has depths [3,4])"
)
