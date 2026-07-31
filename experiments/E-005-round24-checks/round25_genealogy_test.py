"""
A first, bounded pass at Codex's round-25 item 4 ("genealogy of hard residues as a typed killed
branching walk"): does the residue achieving max min-cost (the one determining j*(l), B*(l)) at
level l descend from the analogous champion at level l-1 (i.e. is `argmax_z(l) mod 3^(l-1) ==
argmax_z(l-1)`), or does the "hardest residue" lineage switch between levels?

This is a much smaller first step than Codex's full proposal (a complete multi-terminal decision
diagram over z -> c_n(z), with branching-process statistics extracted from the whole frontier,
not just the single champion). That fuller version needs either a smarter analytic/transfer-
operator approach or many more exact data points than are currently reachable (this per-residue
full-cost computation via the joint DP is only practical to about l=12-13 before cost balloons,
see mean_cost_per_residue.py's own documented ceiling).

Result (l=4..12, 8 transitions, reusing core.py's already-validated joint DP): the champion
switches lineage in 6 of 8 transitions (only l=8->9 and l=10->11 stay on the same branch). This
is genuinely informative (rules out a naive single-persistent-champion picture) but far too little
data to discriminate between the three branching-process regimes item 4 named (log-corrected,
finite-variance sqrt(n), or stable/heavy-tailed). Recorded as attempted-but-inconclusive given the
data ceiling, not as a dead end or a resolved finding either way.
"""
import time

import numpy as np

import core

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19}


def argmax_mincost(l):
    j = JSTAR_FULL[l]
    cmax = 3 * l + 15
    N = core.joint_counts(l, l, cmax)
    mod = 3 ** l
    units = np.arange(mod)
    units = units[units % 3 != 0]
    Nu = N[units]
    has_mass = Nu > 0
    mincost = np.argmax(has_mass, axis=1)
    idx = np.argmax(mincost)
    return int(units[idx]), int(mincost[idx])


if __name__ == "__main__":
    results = {}
    for l in range(4, 13):
        t0 = time.time()
        z, c = argmax_mincost(l)
        results[l] = z
        print(f"l={l:2d} argmax_z={z:8d} mincost={c:3d} (t={time.time()-t0:.1f}s)", flush=True)

    print("\n=== ancestry check: is argmax_z(l+1) mod 3^l == argmax_z(l)? ===")
    for l in range(4, max(results)):
        z_l = results[l]
        z_l1 = results[l + 1]
        ancestor = z_l1 % (3 ** l)
        print(f"l={l:2d}->l={l+1:2d}: argmax_z({l})={z_l:8d}  "
              f"argmax_z({l+1}) mod 3^{l}={ancestor:8d}  same_lineage={ancestor == z_l}")
