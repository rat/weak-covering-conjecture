"""
Follow-up to round 3: now that the one-sided D+/D- Lucas-triangularity is independently confirmed
(2218 checks, exact, no contamination from Q), redo the cell count on our existing witnesses using
the much less restrictive ONE-SIDED admissibility (only one direction needs to fit, not both).
"""
from math import comb

def one_sided_cells(alphas, M):
    """(i,m,sign) with digit_m(n_i) allowing a legal move in direction `sign` (+1 or -1) that
    keeps the full tuple admissible (strictly between neighbors), with no admissibility
    requirement on the OTHER direction."""
    eps = [a % 2 for a in alphas]
    n = [a // 2 for a in alphas]
    cells = []
    for i in range(len(n)):
        for m in range(M + 1):
            digit_m = (n[i] // 3**m) % 3
            lo = alphas[i + 1] if i + 1 < len(alphas) else -1
            hi = alphas[i - 1] if i > 0 else None
            # + direction: needs digit_m in {0,1} so n_i+3^m doesn't carry past this digit
            if digit_m in (0, 1):
                a_plus = alphas[i] + 2 * 3**m
                if (hi is None or a_plus < hi):
                    cells.append((i, m, '+'))
            # - direction: needs digit_m in {1,2} and n_i-3^m>=0
            if digit_m in (1, 2) and n[i] - 3**m >= 0:
                a_minus = alphas[i] - 2 * 3**m
                if a_minus > lo:
                    cells.append((i, m, '-'))
    return cells

witnesses = {
    "l=4 near-defect (E=2)": (8, 7, 5, 3, 2, 1, 0),
    "l=4 control (E=4)":     (10, 8, 7, 5, 2, 1, 0),
    "l=6 near-defect (E=7)": (16, 12, 10, 7, 5, 4, 3, 2, 1, 0),
    "l=6 control (E=7)":     (16, 14, 10, 8, 7, 4, 3, 2, 1, 0),
}

print("=== One-sided cell counts (much less restrictive than the two-sided buffered version) ===")
for label, alphas in witnesses.items():
    for M in (0, 1, 2):
        cells = one_sided_cells(alphas, M)
        distinct_positions = len(set((i, m) for i, m, s in cells))
        print(f"  {label}, M<={M}: {len(cells)} oriented one-sided cells "
              f"({distinct_positions} distinct (i,m) positions with at least one direction)")
    print()

# tuple length j for comparison against the "need ~j pivots" requirement
for label, alphas in witnesses.items():
    print(f"  {label}: tuple length j={len(alphas)}")
