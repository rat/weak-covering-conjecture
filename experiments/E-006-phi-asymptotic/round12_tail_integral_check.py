"""
H-006 Codex round 12: verify the analytic tail-integral chain.

1. Exact incomplete-beta formula: J_M(a) := integral_a^infty (1+t^2)^{-M/2} dt
   =? (1/2)*B_{(1+a^2)^{-1}}(( M-1)/2, 1/2), via numerical quadrature vs mpmath's betainc.

2. Elementary bound: J_M(a) <=? 1/(a*(M-1)) * (1+a^2)^{-(M-2)/2}.

3. R_N (the estimate-3-based upper bound on T_N) trend across N=10..30: does it actually shrink
   as claimed, consistent with T_N <= O(N^{-1/12})*exp(-0.5*N^{1/6}*(1+o(1)))?

4. Cross-check against a DIRECT numerical integration of the true tail integral
   sqrt(K''(r_N)/(2pi)) * integral_{|u|>U_N} |chi_{r_N}(u)| du (using the exact complex product,
   not estimate (3)'s bound), for one moderate N, to see if the TRUE T_N is comparable to R_N
   (should have T_N <= R_N if everything is consistent).
"""
import mpmath as mp

mp.mp.dps = 40


def J_M_numeric(M, a, upper=None):
    if upper is None:
        upper = a + 200  # integrand decays like t^{-M}, M>=8ish here, converges fast
    return mp.quad(lambda t: (1 + t**2) ** (-M / 2), [a, upper, upper * 5, upper * 20])


def J_M_beta(M, a):
    x = 1 / (1 + a**2)
    # mpmath's betainc(a,b,0,x) gives the (lower) incomplete beta integral from 0 to x
    return mp.mpf('0.5') * mp.betainc(mp.mpf(M - 1) / 2, mp.mpf('0.5'), 0, x)


print("=== Part 1: exact incomplete-beta formula for J_M(a) ===")
for M, a in [(6, mp.mpf('0.5')), (10, mp.mpf('1.0')), (20, mp.mpf('0.3')), (8, mp.mpf('2.0'))]:
    num = J_M_numeric(M, a)
    beta_form = J_M_beta(M, a)
    print(f"  M={M}, a={float(a)}: numeric={mp.nstr(num,10)}  beta_formula={mp.nstr(beta_form,10)}  "
          f"match={abs(num-beta_form)<mp.mpf('1e-8')}")

print("\n=== Part 2: elementary bound J_M(a) <= 1/(a(M-1)) * (1+a^2)^{-(M-2)/2} ===")
for M, a in [(6, mp.mpf('0.5')), (10, mp.mpf('1.0')), (20, mp.mpf('0.3')), (8, mp.mpf('2.0'))]:
    exact = J_M_numeric(M, a)
    bound = 1 / (a * (M - 1)) * (1 + a**2) ** (-(mp.mpf(M) - 2) / 2)
    holds = exact <= bound
    print(f"  M={M}, a={float(a)}: exact={mp.nstr(exact,8)}  elementary_bound={mp.nstr(bound,8)}  holds={holds}")

print("\n=== Part 3: R_N trend across N (using T-bound formula) ===")


def K_series(s, terms=None):
    if terms is None:
        terms = 300
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += mp.log((1 - mp.e ** (-2 * x)) / (2 * x))
        denom *= 3
    return total


def V_series(s, terms=None):
    if terms is None:
        terms = 300
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += 1 - (x / mp.sinh(x)) ** 2
        denom *= 3
    return total


A = mp.mpf(2)
print(f"{'N':>4} {'sigma_N':>14} {'a_N':>12} {'M_N':>6} {'T_bound(R_N)':>16}")
for N in [10, 15, 20, 25, 30, 40, 50]:
    N_mp = mp.mpf(N)
    r_N = mp.mpf(3) ** N / 2
    sigma_N2 = V_series(r_N, terms=N + 60) / r_N ** 2
    sigma_N = mp.sqrt(sigma_N2)
    a_N = N_mp ** (mp.mpf('-5') / 12)

    N_active = 0
    j = 1
    while (2 / mp.mpf(3) ** j) * r_N >= 1:
        N_active += 1
        j += 1
    N_active_mp = mp.mpf(N_active)
    logN = mp.log(N_active_mp)
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

    C_const = N_active_mp ** (-A)  # matches e^{C*N^{-A}} with C=1 as tested in round 10
    T_bound = mp.sqrt(2 / mp.pi) * mp.e ** C_const * (r_N * sigma_N) / (a_N * (M_mp - 1)) * (1 + a_N**2) ** (-(M_mp - 2) / 2)
    print(f"{N:4d} {float(sigma_N):14.6e} {float(a_N):12.6f} {float(M_mp):6.0f} {mp.nstr(T_bound, 8):>16}")
