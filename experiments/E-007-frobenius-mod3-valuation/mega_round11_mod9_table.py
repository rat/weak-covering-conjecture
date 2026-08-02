"""
Round 11 (mega cycle): per-mod-9-class stratum coverage table, per Codex's spec, at (l,j)=(6,8).
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image

l, j = 6, 8
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)

I = {}
for d in range(1, 5):  # d=1..4
    I[d] = stratum_image(l, j, d) & units

unit_classes = [1, 2, 4, 5, 7, 8]
U_r = {r: {x for x in units if x % 9 == r} for r in unit_classes}
low_union = I[1] | I[2] | I[3] | I[4]
R4 = units - low_union

print(f"=== Per-mod-9-class stratum coverage table, (l,j)=({l},{j}) ===")
print(f"{'r':>3} {'|U_r|':>6} " + " ".join(f"|I{d}|" for d in range(1, 5)) +
      f"  |union|  |R4∩U_r|")
for r in unit_classes:
    Ur = U_r[r]
    counts = [len(I[d] & Ur) for d in range(1, 5)]
    union_count = len(low_union & Ur)
    r4_count = len(R4 & Ur)
    print(f"{r:>3} {len(Ur):>6} " + " ".join(f"{c:>4}" for c in counts) +
          f"    {union_count:>4}     {r4_count:>4}")

print("\n=== Overlap histogram h_{r,k} = #{x in U_r : x in exactly k of I_1..I_4} ===")
print(f"{'r':>3}  k=0  k=1  k=2  k=3  k=4")
for r in unit_classes:
    Ur = U_r[r]
    h = [0, 0, 0, 0, 0]
    for x in Ur:
        k = sum(1 for d in range(1, 5) if x in I[d])
        h[k] += 1
    print(f"{r:>3} " + " ".join(f"{c:>4}" for c in h))

# ---------- decisive refinement for r=4,8: cumulative residual support at mod 27, 81 ----------
print("\n=== Cumulative residual R_t = U \\ union(I_1..I_t), occupied cylinders mod 27 and 81, r in {4,8} ===")
for a, modn in ((3, 27), (4, 81)):
    print(f"\n  -- depth a={a} (mod {modn}) --")
    cumulative = set()
    for t in range(0, 5):
        if t > 0:
            cumulative |= I[t]
        R_t = units - cumulative
        R_t_48 = {x for x in R_t if x % 9 in (4, 8)}
        cyl = {}
        for x in R_t_48:
            cyl.setdefault(x % modn, []).append(x)
        sizes = sorted((len(v) for v in cyl.values()), reverse=True)
        print(f"    t={t}: |R_t ∩ {{4,8 mod 9}}| = {len(R_t_48)}, "
              f"{len(cyl)} occupied mod-{modn} cylinders, sizes={sizes}")
