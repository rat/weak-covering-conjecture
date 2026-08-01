from fractions import Fraction
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image

l, j = 6, 10
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)
holdouts = {262, 505}

for d in (1, 2, 6, 7, 8, 9):
    if d >= l:
        continue
    S = stratum_image(l, j, d) & units
    covers = holdouts & S
    print(f"d={d}: |S_d ∩ units|={len(S)}/{len(units)} ({100*len(S)/len(units):.1f}%), "
          f"covers holdouts: {covers if covers else 'neither'}")
