"""
Gemini's suggested decisive test (see notes/H-003.md, "B1/B2" section): compare the MEAN cost
E[A|z] across residues to the MAX cost B*(l) (already known exactly, = j*(l)+l). If the mean
already tracks the critical rate (1+log_4(3))*l while only the max needs 2l+O(1), that points to
an extreme-value explanation for e(l) (favoring O(log l) or O(sqrt l)); if the mean also drifts
toward 2l, that is closer to the (rejected, but not yet re-tested at this range) "linear e(l)"
reading.

Two more efficient approaches were tried and FAILED before this one (kept as a lesson, not
silently discarded, per this project's own honesty conventions):
  1. A naive direct forward recursion in Syrac-space using additive shifts (np.roll) -- wrong,
     because the increment at step m is 3^(m-1)*2^(-(a_1+...+a_m)), which depends MULTIPLICATIVELY
     on the accumulated history through all prior a_i, not just additively on a_m.
  2. Marginalizing cost out of core.py's own W-space recursion (which correctly handles point 1
     via the bijection W_m = 2^a*W_{m-1}+3^(m-1)) BEFORE applying the final Syrac = 2^-A * W_n
     transform -- wrong, because that transform genuinely needs A per path: two tuples with the
     same W_n but different total cost A land on DIFFERENT Syrac values, so a cost-marginalized
     W-space distribution mixes contributions to different z and cannot be un-mixed afterward.

Conclusion: the (residue, cost) joint distribution is not an implementation inefficiency to be
optimized away here, it is genuinely load-bearing information. This script uses core.py's own
validated joint DP directly (dp_W / joint_counts, already checked against brute force), with a
cost cutoff cmax ~ 3*l (a total cost far beyond any residue's typical range; the truncated tail's
probability mass is astronomically small, not a meaningful approximation error). Memory is
O(3^l * cmax), which caps how far l can go (practically to ~16 on this machine); this is a real,
lower ceiling than initially hoped, recorded honestly rather than glossed over.
"""
import sys
import time
import json
import numpy as np

import core  # local copy, same directory (critique round, 2026-07-30: this used to import from a session-scoped scratch path that would not survive)

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19, 15: 20, 16: 20, 17: 21, 18: 22, 19: 23, 20: 24,
              21: 25, 22: 26, 23: 27}


def mean_cost_via_core(l, cmax):
    """E[A|z] for every unit z mod 3^l, cost truncated at cmax, via core.py's validated
    joint DP. Returns (mean_ea, tail_mass) where tail_mass is the total probability NOT
    captured within cmax (should be extremely small; printed so truncation is checked, not
    assumed)."""
    N = core.joint_counts(l, l, cmax)
    M = 3 ** l
    c = np.arange(cmax + 1)
    w = 2.0 ** (-c.astype(np.float64))
    PW = (N * w).sum(axis=1)
    EW = (N * (c * w)).sum(axis=1)
    total_mass = PW.sum()
    tail_mass = 1.0 - total_mass  # should be ~0; P(Syrac=any z) sums to 1 exactly if untruncated
    units = np.arange(M)
    units = units[units % 3 != 0]
    ea = np.where(PW[units] > 0, EW[units] / PW[units], np.nan)
    return ea, units, float(tail_mass)


if __name__ == "__main__":
    lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    results = []
    t0 = time.time()
    for l in range(4, lmax + 1):
        j = JSTAR_FULL.get(l)
        Bstar = j + l if j is not None else None
        cmax = 3 * l + 15
        ea, units, tail_mass = mean_cost_via_core(l, cmax)
        max_ea = float(np.nanmax(ea))
        min_ea = float(np.nanmin(ea))
        argmax_z = int(units[np.nanargmax(ea)])
        crit = (1 + np.log(3) / np.log(4)) * l
        row = dict(l=l, jstar=j, Bstar=Bstar, cmax=cmax, tail_mass=tail_mass,
                   max_EA=max_ea, min_EA=min_ea, argmax_z=argmax_z, crit=crit,
                   twol=2 * l)
        results.append(row)
        print(f"l={l:2d} j*(l)={j} B*(l)={Bstar} cmax={cmax} tail_mass={tail_mass:.2e}  "
              f"max_z E[A|z]={max_ea:.3f}  min_z E[A|z]={min_ea:.3f}  "
              f"critical(1.7925l)={crit:.3f}  2l={2*l}  (t={time.time()-t0:.1f}s)", flush=True)
        with open("mean_cost_results.json", "w") as f:
            json.dump(results, f, indent=2)
    print(f"\ndone in {time.time()-t0:.1f}s")
