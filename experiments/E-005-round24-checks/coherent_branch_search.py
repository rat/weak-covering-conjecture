"""
A2 follow-up (H-003 round 24, GAP A item 2): Codex proposed searching for "an eventually
periodic digit branch b_r admitting a q-step positive Perron-Frobenius inequality," i.e. a
single coherent 3-adic path whose occupancy stays persistently rare as depth r grows, as
opposed to shallow_cylinder_occupancy.py's independent argmin at each r (which could in
principle jump between unrelated branches).

Trick: reduction mod 3^r only depends on the r largest chosen exponents (this project's
value convention), so occupancy at every shallower depth r' < r is exactly recoverable from
the depth-r array by aggregating in blocks of size 3^r' (every residue mod 3^r has a unique
ancestor mod 3^r' = itself mod 3^r'). Compute the full array once at the deepest r tested,
derive every shallower level's occupancy from it, and trace the deepest argmin's ancestors
back through every level.

Finding (l=16,20,23, r up to 14): a genuinely coherent, persistent branch exists -- the
deepest-level argmin is at or within rank 4 of the minimum at EVERY shallower depth tested,
for every l tried, not the "independent argmin jumps around" null hypothesis. Its digit
sequence is NOT periodic (checked by inspection, no repeating block in 12-14 digits), so
Codex's specific "eventually periodic" mechanism is not what is happening; the coherence
itself is real. The branch is l-specific, not shared across different l (checked l=16 vs 20
vs 23: digit sequences agree only trivially at r=1, diverge immediately after). Does not
change the rollover finding (shallow_cylinder_occupancy.py / rollover_test.py): a coherent
worst branch existing is compatible with the already-established sub-linear -log(q) growth,
not evidence for or against exponential-in-l starvation.
"""
import numpy as np

from shallow_cylinder_occupancy import compute_counts_dp, JSTAR_FULL


def trace_coherent_branch(l, rdeep):
    j = JSTAR_FULL[l]
    mr = 3 ** rdeep
    counts = compute_counts_dp(l, j, mr)
    total = int(counts.sum())

    agg = {rdeep: counts.copy()}
    cur = counts
    n = mr
    for r in range(rdeep - 1, 0, -1):
        n_next = 3 ** r
        cur = cur.reshape(n // n_next, n_next).sum(axis=0)
        agg[r] = cur
        n = n_next

    units = np.arange(mr)
    units = units[units % 3 != 0]
    occ = agg[rdeep][units]
    deep_b = int(units[np.argmin(occ)])

    trace = []
    for r in range(1, rdeep + 1):
        ancestor = deep_b % (3 ** r)
        mrr = 3 ** r
        a = agg[r]
        u = np.arange(mrr)
        u = u[u % 3 != 0]
        o = a[u]
        rank = int(np.sum(o < a[ancestor])) + 1
        trace.append(dict(r=r, ancestor=ancestor, occ=int(a[ancestor]), rank=rank, n_units=len(u)))
    return dict(l=l, j=j, total=total, deep_r=rdeep, deep_b=deep_b, trace=trace)


def digits(b, r):
    ds = []
    for _ in range(r):
        ds.append(b % 3)
        b //= 3
    return ds


if __name__ == "__main__":
    for l in [16, 20, 23]:
        res = trace_coherent_branch(l, rdeep=12)
        print(f"\n=== l={l} j={res['j']} ===")
        for row in res["trace"]:
            print(f"  r={row['r']:2d} ancestor={row['ancestor']:7d} occ={row['occ']:10d} "
                  f"rank={row['rank']}/{row['n_units']}")
        print(f"  digits (LSB first): {digits(res['deep_b'], 12)}")

    print("\n=== pushing l=23 to r=14 to check persistence deeper ===")
    res = trace_coherent_branch(23, rdeep=14)
    for row in res["trace"]:
        print(f"  r={row['r']:2d} ancestor={row['ancestor']:7d} occ={row['occ']:10d} "
              f"rank={row['rank']}/{row['n_units']}")
