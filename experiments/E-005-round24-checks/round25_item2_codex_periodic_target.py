"""
Tests Codex's round-25 item 2 ("Search for an ultimately periodic hard 3-adic target and certify
it by a minimum-cycle-mean inequality"): starting from z=-2 mod 3^4 (the l=4 global-worst residue,
also this project's T_0 fixed point), greedily extend the digit stream one level at a time by
picking, among the (up to 3) children z + t*3^l for t=0,1,2, whichever has the HIGHEST cost at
level l+1, reusing core.py's already-validated joint DP. This is a first, cheap step toward
Codex's fuller proposal (build a product automaton for a genuinely periodic target and certify a
minimum-cycle-mean exceeding alpha+eps): if the greedy cost sequence does not even show a growing
linear excess over l over the reachable range, there is no periodic candidate worth the fuller
automaton construction.

Codex's own retention condition: "The T_0-loop at -2 must be retained: if it or another cheap
cycle survives in the target-restricted graph, the candidate is refuted. Merely rediscovering that
loop would be exactly the already-closed approach, not a new result." This project's own same-day
item-5 finding already showed the adversary's optimal response never uses the -2 self-loop, so
this greedy construction (which does move away from -2 immediately) is at least consistent with
that requirement.

Result (l=4..13, cost in Wirsching's j-scale after the Tao B-scale correction): the cost sequence
is 9, 10, 11, 12, 13, 14, 15, 16, 17 -- i.e. cost(l) = l+4 EXACTLY for every l in this range. This
is NOT a growing linear excess: it exactly reproduces the ALREADY KNOWN, ALREADY Gemini-reviewed
finding that j*(l)-l stays bounded (in {2,...,5}) across the whole known table l=1..23, flagged
90%-confidence discretization artifact by Gemini in a separate B1/B2 follow-up this same round (see
notes/H-003.md's "subagent's own flagged cap argument" section). The greedy trajectory tracks the
true j*(l) exactly for l=5..9 (where j*(l)=l+4), then falls exactly 1 behind starting at l=10
(where the true worst residue jumps to j*(l)=l+5, a different branch the greedy local choice does
not find, consistent with the earlier round-25 genealogy-test finding that champion lineages
switch branches). No sign of an unbounded, growing linear excess; closed as a disproof lead by the
same mechanism already flagged and independently reviewed.
"""
import core
import numpy as np

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19}


def mincost_B(l):
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
    return full


if __name__ == "__main__":
    z = (-2) % 81
    l = 4
    for _ in range(9):
        l_next = l + 1
        B_next = mincost_B(l_next)
        best_t, best_cost = None, -1
        for t in range(3):
            cand = z + t * (3 ** l)
            c = int(B_next[cand]) - l_next
            if c > best_cost:
                best_cost, best_t = c, t
        print(f"l={l}->l={l_next}: chosen_t={best_t} cost_at_next={best_cost} "
              f"(true j*({l_next})={JSTAR_FULL.get(l_next, '?')})", flush=True)
        z = z + best_t * (3 ** l)
        l = l_next
