"""
Round 28 (mega cycle): verify Codex's W_{l,j}(q,eps) formula and small-case table by direct
brute-force enumeration of admissible (A,B,d) triples.
"""
from math import comb

def partitions_in_box(rows, cols):
    if rows == 0:
        yield ()
        return
    def rec(remaining_rows, max_part):
        if remaining_rows == 0:
            yield ()
            return
        for first in range(max_part, -1, -1):
            for rest in rec(remaining_rows - 1, first):
                yield (first,) + rest
    yield from rec(rows, cols)

def W_bruteforce(l, j):
    """Returns dict (q,eps) -> count, pooled over d=2..min(l,j)."""
    counts = {(q, eps): 0 for q in range(6) for eps in range(2)}
    for d in range(2, min(l, j) + 1):
        w = j - d
        num_B = comb(j, d)  # number of partitions in (w x d) box == C(j,d)
        for A in partitions_in_box(d, w):
            a1 = A[0] if len(A) >= 1 else 0
            a2 = A[1] if len(A) >= 2 else 0
            q = a1 % 6
            eps = a2 % 2
            counts[(q, eps)] += num_B
    return counts

targets = {
    (2, 2): [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    (2, 3): [(3,0),(3,3),(0,0),(0,0),(0,0),(0,0)],
    (3, 3): [(4,0),(3,3),(0,0),(0,0),(0,0),(0,0)],
    (3, 4): [(10,0),(10,14),(12,6),(0,0),(0,0),(0,0)],
}

all_ok = True
for (l, j), expected in targets.items():
    counts = W_bruteforce(l, j)
    computed = [(counts[(q,0)], counts[(q,1)]) for q in range(6)]
    ok = computed == expected
    all_ok &= ok
    print(f"(l={l},j={j}): computed={computed}")
    print(f"            expected={expected}  match={ok}")
    # checksum
    total = sum(counts.values())
    predicted_total = sum(comb(j, d)**2 for d in range(2, min(l, j) + 1))
    print(f"            checksum: total={total} predicted_total={predicted_total} match={total==predicted_total}")

print(f"\nALL MATCH: {all_ok}")
