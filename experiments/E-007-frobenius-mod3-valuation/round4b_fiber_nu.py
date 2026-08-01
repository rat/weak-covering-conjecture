"""
Round-4 follow-up: compute nu_M(A) = number of DISTINCT leading diagonals (i+3^m) achieved by
one-sided cells, across EVERY member of a fiber (not just one lexicographic witness), as Codex
specified. Since selecting at most one cell per distinct leading diagonal automatically gives a
triangular (hence full-rank) minor (already-verified Lucas property: each column is exactly zero
below its own leading diagonal, nonzero exactly at it), nu_M(A) IS the maximum-matching statistic
Codex asked for -- no separate matching algorithm needed, just counting distinct diagonals.

Report min and max nu over the whole fiber, plus the tuple length j, for the same
near-defect/control residues used in rounds 2-4 (l=4, j=7 and l=6, j=10), at M<=2 (already near
M_max for these small j, per Codex's own bound).
"""
from itertools import combinations

def F(alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def one_sided_leading_diagonals(alphas, M):
    eps = [a % 2 for a in alphas]
    n = [a // 2 for a in alphas]
    diags = set()
    for i in range(len(n)):
        for m in range(M + 1):
            digit_m = (n[i] // 3**m) % 3
            lo = alphas[i + 1] if i + 1 < len(alphas) else -1
            hi = alphas[i - 1] if i > 0 else None
            has_plus = digit_m in (0, 1) and (hi is None or alphas[i] + 2*3**m < hi)
            has_minus = (digit_m in (1, 2) and n[i] - 3**m >= 0
                         and alphas[i] - 2*3**m > lo)
            if has_plus or has_minus:
                diags.add(i + 3**m)
    return diags

def fiber_members(j, mod, target):
    out = []
    for combo in combinations(range(2 * j), j):
        alphas = tuple(sorted(combo, reverse=True))
        if F(alphas) % mod == target:
            out.append(alphas)
    return out

configs = [
    ("l=4 near-defect fiber", 7, 3**5, 10),   # near_defect_x=10 mod 243, from round-2 run
    ("l=4 control fiber",     7, 3**5, 1),    # control_x=1 mod 243
    ("l=6 near-defect fiber", 10, 3**7, 19),  # near_defect_x=19 mod 2187
    ("l=6 control fiber",     10, 3**7, 1),   # control_x=1 mod 2187
]

M = 2
print(f"=== nu_{M}(A) distribution across full fibers (not just one witness) ===")
for label, j, mod, target in configs:
    members = fiber_members(j, mod, target)
    nus = [len(one_sided_leading_diagonals(a, M)) for a in members]
    print(f"  {label}: j={j}, fiber size={len(members)}, "
          f"nu_{M} min={min(nus)} max={max(nus)} mean={sum(nus)/len(nus):.2f} "
          f"(need nu={j} for a full-rank single-scale construction)")
