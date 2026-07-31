"""
Tests Gemini's round-25 item 8 ("Disproof Strategy via 3-Adic Syracuse Attractor Cycles"): lift the
z=-2 fixed point of T_0 to a family r_l = (-2) mod 3^l and check whether its required covering
budget j(r_l) exceeds log_4(3)*l + O(sqrt(l)), as a seed for a constructive disproof of WCC.

IMPORTANT scale note (caught before trusting any number here, per Rule 8c): core.py's joint DP
reports cost in Tao's A/B-scale (Syrac_n's "cost A = a_1+...+a_n" over gap variables a_i>=1), NOT
Wirsching's j-scale. This project already found and fixed exactly this mismatch once (H-002's C1
finding): B(z) = j(z) + l. A first pass here that skipped this conversion produced an internally
impossible result (B(-2)=11 at l=4 appearing to exceed the true global max j*(4)=7, which cannot
happen since j*(l) IS defined as that max) -- caught immediately as a consistency check, not
accepted. All numbers below are in the correct j-scale (j(z) = B(z) - l).

Result: z=-2 is the genuine global-argmax residue at l=4 (j(-2)=j*(4)=7 exactly), but the ratio
j(-2)/j*(l) declines monotonically from 1.0 (l=4) to 0.706 (l=12), and clearing the stated
threshold l*log_4(3)+sqrt(l) is inconsistent (yes at l=4,5,6,7,8,10, no at l=9,11,12) rather than
growing by an increasing margin. This is the same shape as this round's B3-rollover lesson: a real
small-l coincidence that fades rather than strengthens. Closed as a disproof lead.
"""
import numpy as np
from math import log, sqrt

import core

JSTAR_FULL = {1: 1, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 16,
              12: 17, 13: 18, 14: 19}
LOG4_3 = log(3) / log(4)


def mincost_array_B_scale(l):
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
    print(f"{'l':>3} {'j(-2)':>6} {'j*(l)':>6} {'is_argmax':>10} {'threshold':>10} {'exceeds?':>9}")
    for l in range(4, 13):
        B = mincost_array_B_scale(l)
        z = (-2) % (3 ** l)
        Bz = int(B[z])
        jz = Bz - l
        jmax = int(B.max()) - l
        is_argmax = int(B.max()) == Bz
        thresh = l * LOG4_3 + sqrt(l)
        print(f"{l:>3} {jz:>6} {jmax:>6} {str(is_argmax):>10} {thresh:>10.3f} "
              f"{'YES' if jz > thresh else 'no':>9}")
