import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image

JSTAR = {1:1,2:4,3:6,4:7,5:9,6:10,7:11,8:12}

for l in (4, 5, 7):
    j = JSTAR[l]
    mod_l = 3**l
    units = set(x for x in range(mod_l) if x % 3 != 0)
    n_units = len(units)
    covered = set()
    used_d = []
    for d in range(1, l):
        S = stratum_image(l, j, d) & units
        new = S - covered
        covered |= S
        used_d.append(d)
        print(f"  l={l} j={j}: after d={d}: |S_d|={len(S)}, cumulative union={len(covered)}/{n_units} "
              f"({100*len(covered)/n_units:.1f}%)")
        if covered == units:
            print(f"  l={l}: FULL COVERAGE using strata d={used_d} (just {len(used_d)} of up to {l-1} tested)")
            break
    else:
        missing = units - covered
        print(f"  l={l}: incomplete after all d=1..{l-1}, missing {len(missing)}: {sorted(missing)[:10]}")
    print()
