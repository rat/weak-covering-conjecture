"""
H-006 Codex round 11: test estimate (3) at the actual crossover regime Codex identified,
u/r = N^{-5/12} (NOT the fixed u/r=0.1..10 tested in round 10, which Codex correctly pointed out
don't probe the regime that matters for uniformity as N->infinity).

r_N = 3^N/2, U_N = r_N * N^{-5/12}. Test the bound at u=U_N and nearby log-spaced points.
"""
import mpmath as mp

mp.mp.dps = 60


def F_complex(s, terms=None):
    if terms is None:
        terms = 300
    total = mp.mpc(1, 0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total *= (1 - mp.e ** (-2 * x)) / (2 * x)
        denom *= 3
    return total


A = mp.mpf(2)

print(f"{'N':>4} {'r_N':>14} {'u/r=N^-5/12':>14} {'N_active':>10} {'M':>6} {'log|chi|':>14} {'log(bound)':>14} {'margin':>10} {'holds?':>8}")
for N in [10, 15, 20, 25, 30]:
    N_mp = mp.mpf(N)
    r_N = mp.mpf(3) ** N / 2
    u_over_r = N_mp ** (mp.mpf('-5') / 12)
    u = u_over_r * r_N

    # N_active = #{j: x_j>=1}, x_j=(2/3^j)*r_N
    N_active = 0
    j = 1
    while (2 / mp.mpf(3) ** j) * r_N >= 1:
        N_active += 1
        j += 1
    N_active_mp = mp.mpf(N_active)
    logN = mp.log(N_active_mp) if N_active_mp > 0 else mp.mpf(0)
    threshold = A * logN
    M = 0
    j = 1
    while True:
        xj = (2 / mp.mpf(3) ** j) * r_N
        if xj < threshold:
            break
        M += 1
        j += 1
    M_mp = mp.mpf(M)

    terms_needed = N + 60
    chi = F_complex(r_N + 1j * u, terms_needed) / F_complex(r_N, terms_needed)
    log_chi = mp.log(abs(chi))
    bound_log = N_active_mp ** (-A) - (M_mp / 2) * mp.log(1 + u_over_r ** 2)
    margin = bound_log - log_chi
    ok = "YES" if margin >= -mp.mpf('1e-6') else "NO <---"
    print(f"{N:4d} {float(r_N):14.4e} {float(u_over_r):14.6f} {float(N_active_mp):10.0f} {float(M_mp):6.0f} "
          f"{float(log_chi):14.8f} {float(bound_log):14.8f} {float(margin):10.6f} {ok:>8}")
