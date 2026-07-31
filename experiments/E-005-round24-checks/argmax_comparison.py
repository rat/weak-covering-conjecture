"""
Resolves the "does the worst-mean-cost residue equal the worst-min-cost residue" question
flagged as a preliminary observation in notes/H-002.md. Reuses the same joint (residue, cost)
DP as mean_cost_per_residue.py (core.py, brute-force validated), extracting BOTH the argmax of
E[A|z] (mean cost, Gemini's target statistic) and the argmax of min-cost(z) (= the residue that
actually determines B*(l) = j*(l)+l) from the same array, so the comparison is exact, not two
separate runs that could disagree for unrelated numerical reasons.

Result (l=4..12): the two argmax residues coincide at only 3 of 9 l values (5, 10, 11); no
visible pattern in the other 6. See notes/H-002.md for interpretation.
"""
import sys
import time

import numpy as np

import core  # local copy, same directory (critique round, 2026-07-30: this used to import from a session-scoped scratch path that would not survive)

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19}


def compare(l):
    j = JSTAR_FULL[l]
    cmax = 3 * l + 15
    N = core.joint_counts(l, l, cmax)
    mod = 3 ** l
    units = np.arange(mod)
    units = units[units % 3 != 0]
    Nu = N[units]

    has_mass = Nu > 0
    mincost = np.argmax(has_mass, axis=1)  # first nonzero cost per residue
    argmax_mincost_idx = np.argmax(mincost)
    argmax_mincost_z = int(units[argmax_mincost_idx])
    max_mincost = int(mincost[argmax_mincost_idx])

    c = np.arange(cmax + 1)
    w = 2.0 ** (-c.astype(np.float64))
    PW = (Nu * w).sum(axis=1)
    EW = (Nu * (c * w)).sum(axis=1)
    ea = np.where(PW > 0, EW / PW, np.nan)
    argmax_mean_idx = int(np.nanargmax(ea))
    argmax_mean_z = int(units[argmax_mean_idx])

    return dict(l=l, j=j, Bstar=j + l, argmax_mean_z=argmax_mean_z,
                argmax_mincost_z=argmax_mincost_z, max_mincost=max_mincost,
                same=(argmax_mean_z == argmax_mincost_z))


if __name__ == "__main__":
    lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    print(f"{'l':>3} {'argmax_meancost':>16} {'argmax_mincost':>16} {'same?':>6}")
    for l in range(4, lmax + 1):
        t0 = time.time()
        r = compare(l)
        same = "YES" if r["same"] else "no"
        print(f"{r['l']:>3} {r['argmax_mean_z']:>16} {r['argmax_mincost_z']:>16} {same:>6}  "
              f"(max_mincost={r['max_mincost']}, B*(l)={r['Bstar']}, t={time.time()-t0:.1f}s)",
              flush=True)
