"""
Tests the empirical premise behind Gemini's round-25 item 4 ("Extreme Value Theory for
Log-Correlated Fields", angle b, work-list item 8 alongside item 5/Jenkinson-Pollicott): that the
per-residue cost landscape Cost(x) = min{j : x in R_{j-1,j} mod 3^l} behaves as a log-correlated
random field over the 3-adic tree, specifically Cov(Cost(x), Cost(y)) proportional to l - v_3(x-y)
(shared-prefix depth). This is a real, well-known, and load-bearing premise: Bramson's theorem and
the Fyodorov-Hiary-Keating correction only apply to genuinely log-correlated fields, not to fields
with some other covariance decay (e.g. short-range/exponentially-decaying correlation, which would
put the maximum back in ordinary iid-extreme-value territory with a very different correction
term, or long-range correlation with a different scaling altogether).

The claim is checkable directly and cheaply from data this project already has the machinery for
(core.py's already-validated joint DP, reused as in round25_genealogy_test.py to get exact
per-residue mincost arrays). Full O(n^2) pairwise covariance is infeasible even at l=11
(2*3^10 ~ 1.2e5 units, 1.4e10 pairs), so this uses a standard Monte Carlo estimate: sample random
unit pairs, bin by the exact 3-adic valuation of their difference v_3(x-y), and compute the sample
covariance of Cost within each bin.

Result: recorded below after running. The log-correlated hypothesis predicts Cov ~ A*(l - v) for
v=0..l-1 (linear, slope A>0, positive throughout). A short-range/finite-memory hypothesis
(consistent with the "window-k game" structure this project's own best results are built on, where
states more than k digits apart are conditionally near-independent) predicts Cov decaying to ~0
once v exceeds some small correlation length, NOT linear all the way to v=0.
"""
import random
import time
from collections import defaultdict

import numpy as np

import core

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19}


def mincost_array(l):
    j = JSTAR_FULL[l]
    cmax = 3 * l + 15
    N = core.joint_counts(l, l, cmax)
    mod = 3 ** l
    units = np.arange(mod)
    units = units[units % 3 != 0]
    Nu = N[units]
    has_mass = Nu > 0
    mincost = np.argmax(has_mass, axis=1)
    full = np.full(mod, -1, dtype=np.int64)
    full[units] = mincost
    return full, units


def v3(diff, l):
    if diff == 0:
        return l
    v = 0
    while diff % 3 == 0 and v < l:
        diff //= 3
        v += 1
    return v


def sample_covariance_by_distance(cost, units, l, n_samples=400000, seed=0):
    rng = random.Random(seed)
    units_list = list(units)
    mod = 3 ** l
    bins = defaultdict(list)
    for _ in range(n_samples):
        x = rng.choice(units_list)
        y = rng.choice(units_list)
        d = (x - y) % mod
        v = v3(d, l)
        bins[v].append((int(cost[x]), int(cost[y])))
    rows = []
    for v in sorted(bins):
        pairs = bins[v]
        if len(pairs) < 20:
            continue
        cx = np.array([p[0] for p in pairs], dtype=float)
        cy = np.array([p[1] for p in pairs], dtype=float)
        cov = np.cov(cx, cy)[0, 1]
        rows.append((v, len(pairs), cov, cx.mean(), cy.mean()))
    return rows


if __name__ == "__main__":
    for l in [10, 12]:
        t0 = time.time()
        cost, units = mincost_array(l)
        print(f"l={l}: mincost computed in {time.time()-t0:.1f}s, {len(units)} units")
        rows = sample_covariance_by_distance(cost, units, l, n_samples=200000)
        print(f"{'v3(x-y)':>8} {'l-v':>5} {'n_pairs':>8} {'Cov(Cost_x,Cost_y)':>20}")
        for v, n, cov, mx, my in rows:
            print(f"{v:>8} {l-v:>5} {n:>8} {cov:>20.4f}")
        print()
