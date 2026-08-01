import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image

l, j = 6, 10
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)

Ss = {}
for d in (2, 3, 4, 5):
    Ss[d] = stratum_image(l, j, d) & units

for combo_name, combo in [
    ("S2 ∪ S3", Ss[2] | Ss[3]),
    ("S2 ∪ S3 ∪ S4", Ss[2] | Ss[3] | Ss[4]),
    ("S2 ∪ S3 ∪ S4 ∪ S5", Ss[2] | Ss[3] | Ss[4] | Ss[5]),
]:
    missing = units - combo
    print(f"{combo_name}: {len(combo)}/{len(units)} units, missing={sorted(missing)}")
