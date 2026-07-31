"""
Tests Codex's round-25 item 1 ("weighted 3-adic path-set fractal"): compute the constrained
output entropy at the critical budget rate alpha=log_4(3), and check whether it sits below
(1-delta)*log(3) by a persistent gap (which would be Codex's proposed disproof mechanism) or
approaches log(3) (consistent with, though not proof of, covering).

Rather than building Codex's proposed truncated transducer/transfer-operator machinery from
scratch, this uses the ALREADY VALIDATED exact tuple-count DP (compute_counts_dp) at the true
critical budget j*(l) directly: the Shannon entropy of the (normalized) per-residue tuple-count
distribution, per symbol (divided by l), is exactly the quantity Codex's proposal is trying to
estimate via a transfer-operator approximation, computed here exactly instead.

Result: the entropy DEFICIT from log(3) SHRINKS as l grows (0.131 at l=4 down to ~0.046 at
l=15-16), not staying at a persistent (1-delta) gap. This is evidence AGAINST Codex's proposed
disproof mechanism, which needed a persistent gap to conclude "only 3^{(1-delta)n} cylinders
occur." A power-law fit of the deficit (l=8..15 data) gives an exponent of ~0.75-0.78 (deficit
~ C/l^0.78), i.e. decaying slower than 1/l but faster than 1/sqrt(l) -- flagged explicitly as a
small-l fit (l<=16 only) with the SAME caution this project already learned the hard way earlier
this session (notes/H-003.md's rollover-test correction): a promising-looking small-l trend is
not evidence of the true asymptotic without pushing further or an independent check. Not treated
as a finding about e(l)'s growth rate; recorded as a data point only.
"""
import math
import time

import numpy as np

from shallow_cylinder_occupancy import compute_counts_dp, JSTAR_FULL

LOG3 = math.log(3)


def entropy_per_symbol(l):
    j = JSTAR_FULL[l]
    n = 3 ** l
    counts = compute_counts_dp(l, j, n)
    units = np.arange(n)
    units = units[units % 3 != 0]
    c = counts[units].astype(np.float64)
    total = c.sum()
    p = c / total
    H = -np.sum(p * np.log(np.where(p > 0, p, 1)))
    return H / l


if __name__ == "__main__":
    print(f"{'l':>3} {'j*':>3} {'H_per_symbol':>14} {'H/log3':>8} {'deficit':>10} {'t':>6}")
    for l in range(4, 17):
        t0 = time.time()
        per_symbol = entropy_per_symbol(l)
        deficit = LOG3 - per_symbol
        print(f"{l:>3} {JSTAR_FULL[l]:>3} {per_symbol:>14.6f} {per_symbol/LOG3:>8.4f} "
              f"{deficit:>10.6f} {time.time()-t0:>6.1f}", flush=True)
