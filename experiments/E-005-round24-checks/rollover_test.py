"""
Decisive follow-up to shallow_cylinder_occupancy.py, per Gemini's independent review (see
README.md and notes/H-003.md's "Same-day resolution" section). Tests whether C(l,r) :=
-log(q_{l,r})/r stays flat/linear as r approaches l (the original headline finding would need
this to survive), or rolls over and declines (which it does, at every l tested, confirming
the finding was a shallow-regime artifact, not a genuine asymptotic signal).

r is capped at 13 (3^13 = 1,594,323) to stay memory-safe even when run alongside other
memory-heavy jobs; this still reaches r/l up to 0.93 at l=14.
"""
import math
import time

from shallow_cylinder_occupancy import compute_counts_dp, JSTAR_FULL

RCAP = 13

if __name__ == "__main__":
    t0 = time.time()
    for l in [14, 16, 18, 20, 23]:
        j = JSTAR_FULL[l]
        rmax = min(l - 1, RCAP)
        print(f"\n=== l={l} (j={j}), r from 1 to {rmax} (r/l up to {rmax / l:.2f}) ===")
        print(f"{'r':>3} {'r/l':>6} {'-log(q)':>10} {'C=-log(q)/r':>12}")
        for r in range(1, rmax + 1):
            mr = 3 ** r
            counts = compute_counts_dp(l, j, mr)
            total = int(counts.sum())
            units = [b for b in range(mr) if b % 3 != 0]
            min_occ = int(counts[units].min())
            q = (2 * 3 ** (r - 1)) * min_occ / total
            nz = -math.log(q) if q > 0 else float("inf")
            print(f"{r:>3} {r / l:>6.3f} {nz:>10.4f} {nz / r:>12.4f}")
    print(f"\n({time.time() - t0:.1f}s)")
