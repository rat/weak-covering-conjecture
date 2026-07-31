"""
Directly measures H_{n,Q} itself (A1's own bulk quantity, round-24 section "A1: a genuine
follow-up attempt", notes/H-003.md), before attempting Codex's round-25 item 7 (recasting H_{n,Q}
as a weighted-directed-circulant-graph / lattice covering-radius problem via Marklof-Strombergsson
and Kannan-Lovasz/Banaszczyk transference). Building that machinery correctly is substantial new
work; measuring H_{n,Q} directly at reachable n first, near the actual critical budget ratio, is
cheap (core.py's joint DP already gives Gamma_{n,Q} exactly, since G_n IS core.py's Syrac_n up to
an index shift: Gamma_{n,Q} = {G_n(gaps): sum(gaps)<=Q} matches core.joint_counts(n,n,Q)'s support
over cost<=Q) and settles whether the reformulation is even promising before investing in the
lattice construction.

H_{n,Q} := max gap, in the log_4-phase orbit of P_n = <4> (the order-3^(n-1) cyclic subgroup of
(Z/3^nZ)^*, since ord(4)=3^(n-1) via LTE), among phases of points in Gamma_{n,Q}. Computed via an
exact discrete-log table (4^k mod 3^n for k=0..3^(n-1)-1) and the circular max-gap of the sorted
phase set.

A1's reduction: H_{l-1,Q}=o(l) at budget Q within o(l) of the WCC threshold would prove WCC
outright, but A1 itself flagged "proving H_{n,Q}=o(l) near the critical budget would itself be the
whole theorem" -- an anticipated, not yet checked, difficulty.

Result: at n=8, H/n only drops below 1 once Q/n reaches about 2.0-2.25, and full phase saturation
(H=1) needs Q/n~2.5. The best PROVEN direct-covering ratio (E-003's mean-payoff solver) is only
119/104~1.1442. So making H_{n,Q} small requires roughly DOUBLE the budget ratio that direct
covering already achieves -- at the actual proven critical ratio, H_{n,Q} is empirically enormous
(comparable to the full phase-circle size, not o(n)). This is a genuine, if small-n, confirmation
of A1's own anticipated difficulty: this reduction does not appear to make the problem easier at
reachable scales, so Codex's item 7 lattice-covering-radius construction was not attempted --
it would be chasing a quantity already shown, by direct measurement, not to be small where it
would need to be.
"""
import numpy as np

import core


def gamma_set(n, Q):
    N = core.joint_counts(n, n, Q)
    total = N[:, n:Q + 1].sum(axis=1)
    return np.where(total > 0)[0]


def phase_table(n):
    mod = 3 ** n
    order = 3 ** (n - 1)
    phase = {}
    v = 1
    for k in range(order):
        phase[v] = k
        v = (v * 4) % mod
    return phase, order


def h_nq(n, Q):
    phase, order = phase_table(n)
    zs = gamma_set(n, Q)
    phases = sorted(phase[int(z)] for z in zs if int(z) in phase)
    if not phases:
        return None, order, 0
    gaps = [(phases[i + 1] - phases[i]) for i in range(len(phases) - 1)]
    gaps.append(order - phases[-1] + phases[0])
    return max(gaps), order, len(phases)


if __name__ == "__main__":
    n = 8
    for ratio in [1.0, 1.1442, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]:
        Q = max(n, round(ratio * n))
        Hmax, order, npts = h_nq(n, Q)
        if Hmax is None:
            print(f"n={n} Q={Q} (Q/n={Q/n:.3f}): EMPTY")
            continue
        print(f"n={n} Q={Q} (Q/n={Q/n:.3f}): |phases|={npts}/{order} "
              f"H_max={Hmax} H/n={Hmax/n:.3f}", flush=True)
