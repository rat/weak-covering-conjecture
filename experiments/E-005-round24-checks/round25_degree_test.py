"""
Tests the naive/direct reading of Codex's round-25 item 10 ("nonzero 3-adic discrete degree"):
if the RAW tuple count per residue, at the true critical budget j*(l), were always nonzero mod 3,
that would be a necessary (not sufficient) condition consistent with the "nonzero degree forces
surjectivity" mechanism Codex proposes. Item 10 actually proposes a more sophisticated grouped
("macro-cell") topological degree over blocks of b ranks, via a SAT search for a "connected
cubical chain" -- not attempted here, both because it is Codex's own lowest-confidence item (21%)
and because a properly faithful implementation needs real additional design work. This script
tests the much cheaper NECESSARY CONDITION first, reusing the already-validated exact tuple-count
DP.

Result: FAILS. At every l=4..13 tested, roughly 1/3 of residues (stably ~0.33, not drifting) have
tuple count divisible by 3 at the critical budget j*(l). The raw per-residue tuple count is not a
"nonzero mod 3" invariant. This does not rule out a more sophisticated topological degree notion
(a signed/oriented count could differ from the raw unsigned tuple count), but it does show the
simplest, most direct reading of "nonzero mod 3" does not hold, a real, if partial, negative data
point recorded honestly rather than left unchecked.
"""
import numpy as np

from shallow_cylinder_occupancy import compute_counts_dp, JSTAR_FULL


def check(l):
    j = JSTAR_FULL[l]
    n = 3 ** l
    counts = compute_counts_dp(l, j, n)
    units = np.arange(n)
    units = units[units % 3 != 0]
    c = counts[units]
    div3 = int(np.sum(c % 3 == 0))
    return len(units), div3


if __name__ == "__main__":
    print(f"{'l':>3} {'j*':>3} {'total_residues':>14} {'divisible_by_3':>15} {'frac':>8}")
    for l in range(4, 14):
        total, div3 = check(l)
        print(f"{l:>3} {JSTAR_FULL[l]:>3} {total:>14} {div3:>15} {div3/total:>8.4f}", flush=True)
