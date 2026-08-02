"""
Round 9 (mega cycle): ball-saturation + ultrametric-clustering test at (l,j)=(6,8), per Codex's
precise round-9 specification.

First get the actual R_4 (the 24-element residual set), then compute the observed T(R_4) and
K(R_4) statistics, compare against the given null MEAN formulas as a first signal, before
attempting the full exact null-distribution DP for precise p-values.
"""
import sys
sys.path.insert(0, '/tmp/claude-1000/-home-rat-weak-covering-conjecture/a8d2d60e-9133-436f-a13c-a0fb27ee7018/scratchpad')
from round7_stratum_union import stratum_image
from math import comb

l, j = 6, 8
mod_l = 3**l
units = set(x for x in range(mod_l) if x % 3 != 0)

low_strata_union = set()
for d in range(1, l - 1):  # d=1..4
    low_strata_union |= stratum_image(l, j, d) & units

R4 = sorted(units - low_strata_union)
print(f"R_4 (residual, uncovered by d<=4): n={len(R4)}")
print(f"  {R4}")

def v3(n):
    if n == 0:
        return None
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k

# ---------- T(R) = sum over pairs of v_3(x-y) ----------
T_obs = 0
for i in range(len(R4)):
    for kk in range(i + 1, len(R4)):
        d = abs(R4[i] - R4[kk])
        T_obs += v3(d)

n = len(R4)
N = len(units)  # 486
E_T = 0
for q in range(1, 6):
    bq = 2 * 3**(q - 1)
    ball_size = 3**(l - q)
    E_Pi_q = comb(n, 2) * (ball_size - 1) / (N - 1)
    E_T += E_Pi_q

print(f"\nT(R_4) observed = {T_obs}")
print(f"E[T] under uniform-random 24-subset null = {E_T:.3f}")
print(f"ratio observed/expected = {T_obs / E_T:.3f}")

# ---------- K(R) = sum_q (162/b_q) * h(q,0) ----------
K_obs = 0
F_table = {}
for q in range(1, 6):
    bq = 2 * 3**(q - 1)
    balls_occupied = set(x % (3**q) for x in R4)
    h_q_0 = bq - len(balls_occupied)
    F_q = h_q_0 / bq
    F_table[q] = (h_q_0, bq, F_q)
    K_obs += (162 / bq) * h_q_0

print(f"\nF_4(q) table: q -> (h(q,0)=#empty balls, b_q=#total balls, F(q)=frac saturated)")
for q in range(1, 6):
    print(f"  q={q}: {F_table[q]}")

print(f"\nK(R_4) observed = {K_obs:.3f}")

E_K = 0
for q in range(1, 6):
    bq = 2 * 3**(q - 1)
    ball_size = 3**(l - q)
    E_F_q = comb(N - ball_size, n) / comb(N, n)
    E_h_q_0 = E_F_q * bq
    E_K += (162 / bq) * E_h_q_0
print(f"E[K] under uniform-random 24-subset null = {E_K:.3f}")
print(f"ratio observed/expected = {K_obs / E_K:.3f}")
