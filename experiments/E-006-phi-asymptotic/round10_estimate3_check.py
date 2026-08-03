"""
H-006 Codex round 10: verify the new medium-frequency estimate (3),
    |chi_r(u)| <= e^{C*N^{-A}} * (1+u^2/r^2)^{-M/2}
where N = #{j: x_j>=1} ~ log_3(r), M = #{j: x_j >= A*log(N)} = N - O(loglog N), x_j = a_j*r,
a_j = 2/3^j.

Part 1: verify the per-factor inequality |1-e^{-x}*e^{-i*theta}|/(1-e^{-x}) <= coth(x/2).
Part 2: verify the full product bound (3) directly against our exact chi_r(u) = F(r+iu)/F(r),
for several r, u, and a specific choice of A (Codex left A free; test A=2 as a reasonable pick,
and confirm the bound holds with an honestly-computed constant C, or at least holds with M
defined precisely via a stated A).
"""
import mpmath as mp

mp.mp.dps = 40


def F_complex(s, terms=300):
    total = mp.mpc(1, 0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total *= (1 - mp.e ** (-2 * x)) / (2 * x)
        denom *= 3
    return total


print("=== Part 1: per-factor inequality |1-e^{-x}e^{-i theta}|/(1-e^{-x}) <= coth(x/2) ===")
worst = mp.mpf(0)
for x in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(5), mp.mpf(10)]:
    for theta in [mp.mpf('0.1'), mp.mpf('1.0'), mp.mpf('2.0'), mp.mpf('3.0'), mp.mpf(mp.pi)]:
        lhs = abs(1 - mp.e ** (-x) * mp.e ** (-1j * theta)) / (1 - mp.e ** (-x))
        rhs = mp.cosh(x / 2) / mp.sinh(x / 2)  # coth(x/2)
        ratio = lhs / rhs
        worst = max(worst, ratio)
        if ratio > 1 + mp.mpf('1e-10'):
            print(f"  VIOLATION x={float(x)} theta={float(theta)}: lhs={float(lhs):.6f} rhs={float(rhs):.6f}")
print(f"  worst lhs/rhs ratio across grid: {float(worst):.6f} (should be <=1)")

print("\n=== Part 2: full product bound (3), A=2 ===")
A = mp.mpf(2)
print(f"{'r':>8} {'u/r':>8} {'N':>6} {'M':>6} {'log|chi|':>14} {'log(bound)':>14} {'margin':>10} {'holds?':>8}")
for r in [mp.mpf(100), mp.mpf(1000), mp.mpf(10000)]:
    # N = #{j: x_j>=1}, x_j = (2/3^j)*r
    N = 0
    j = 1
    while (2 / mp.mpf(3) ** j) * r >= 1:
        N += 1
        j += 1
    N = mp.mpf(N)
    logN = mp.log(N) if N > 0 else mp.mpf(0)
    threshold = A * logN
    M = 0
    j = 1
    while True:
        xj = (2 / mp.mpf(3) ** j) * r
        if xj < threshold:
            break
        M += 1
        j += 1
    M = mp.mpf(M)
    C_const = mp.mpf(1)  # Codex left C unspecified; test whether C=1 suffices as a first guess
    for u_frac in [mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('2.0'), mp.mpf('10.0')]:
        u = u_frac * r
        chi = F_complex(r + 1j * u) / F_complex(r)
        log_chi = mp.log(abs(chi))
        bound_log = C_const * N ** (-A) - (M / 2) * mp.log(1 + (u / r) ** 2)
        margin = bound_log - log_chi
        ok = "YES" if margin >= -mp.mpf('1e-6') else "NO <---"
        print(f"{float(r):8.0f} {float(u_frac):8.2f} {float(N):6.0f} {float(M):6.0f} "
              f"{float(log_chi):14.6f} {float(bound_log):14.6f} {float(margin):10.6f} {ok:>8}")
