"""
Tests the premise behind Codex's round-25 item 5 ("Induce the Bellman dynamics away from the
neutral loop z=-2 and use a tropical renewal equation"): the proposal assumes optimal play under
the mean-payoff game lingers near, or repeatedly returns to and sits at, the state z=-2, which is
a genuine zero-cost fixed point of T_0 (T_0(-2)=-2 exactly, verified earlier via LTE in round 24's
A3 work). If that premise held, an excursion/renewal analysis relative to z=-2 would be a natural
tool for the exponent question in H-009.

This tests the premise directly and cheaply, reusing the already-committed, already-validated
mean-payoff-game certificates (certificate_k{10,11,12,13}.json, sigma/lam/h all present). At the
state z=-2 (mod 3^k), the minimizer's optimal digit is d=sigma[z]=0 at every tested k, and one of
the three extension choices for e (namely e=2) is exactly the self-loop back to z=-2 itself, at
zero cost. The question is whether the ADVERSARY (who picks e to maximize the game's long-run
value, using the standard mean-payoff tie-break argmax(lam, h), matching the convention already
established in mpg3.py's gain_bias_of_action) ever actually chooses that self-loop.

Result: NO, at every k in {10,11,12,13}. The adversary always strictly prefers moving away from
z=-2 (to a state with strictly higher bias h, lambda being constant/tied everywhere in a converged
solution). The zero-cost self-loop at the fixed point is a real option in the game graph but is
never the adversary's best response, so it is never used under optimal play. There is no "neutral
loop" that optimal trajectories linger in or repeatedly return to and sit at; the -2 fixed point is
visited (it must be, T_0 sends units back through it structurally) but immediately departed. This
refutes the specific renewal-near-a-sticky-fixed-point picture item 5 proposes, at the level Codex
itself flagged as a collapse condition ("if the fixed point is not actually where mass lingers,
this route should be abandoned"). It does not rule out an excursion/renewal analysis relative to
some OTHER recurrent structure, only the specific z=-2 anchor Codex named.
"""
import json
import os
from fractions import Fraction as Fr

CERT_DIR = os.path.join(os.path.dirname(__file__), '..', 'E-003-mpg-cylinder')


def transition(z, d, e, m):
    zext = z + m * e
    num = 2 ** (d + 1) * zext - 2
    if num % 3 != 0:
        return None
    return (num // 3) % m


def check(k):
    with open(os.path.join(CERT_DIR, f'certificate_k{k}.json')) as f:
        cert = json.load(f)
    mod = 3 ** k
    sigma = {int(s): d for s, d in cert['sigma'].items()}
    lam = {int(s): Fr(v[0], v[1]) for s, v in cert['lam'].items()}
    h = {int(s): Fr(v[0], v[1]) for s, v in cert['h'].items()}
    z_neg2 = (-2) % mod
    d = sigma[z_neg2]
    choices = []
    for e in range(3):
        zn = transition(z_neg2, d, e, mod)
        if zn is not None and zn in lam:
            choices.append((e, zn, lam[zn], h[zn]))
    best = max(choices, key=lambda c: (c[2], c[3]))
    self_loop = next((c for c in choices if c[1] == z_neg2), None)
    return d, choices, best, self_loop


if __name__ == "__main__":
    for k in [10, 11, 12, 13]:
        d, choices, best, self_loop = check(k)
        z_neg2 = (-2) % (3 ** k)
        print(f"k={k:2d}  sigma[-2]={d}  self-loop available at e={self_loop[0]} (h={self_loop[3]})  "
              f"adversary picks e={best[0]} h={best[3]}  "
              f"{'STAYS AT -2' if best[1] == z_neg2 else 'MOVES AWAY -> premise refuted at this k'}")
