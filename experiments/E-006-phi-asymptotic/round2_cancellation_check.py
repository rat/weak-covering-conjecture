"""
H-006 Codex round 2 verification, fixed version.

Part A: V_series(r) (already = r^2 * K''(r) per saddlepoint.py's own docstring, i.e. already
equals r^2*v(r) in Codex's notation) should approach N=floor(log_3 r) + O(1).

Part B: cancellation diagnostic, extended and compared against Codex's predicted asymptotic
-H'(w_0(t))/B_0(w_0(t)), using continuation (previous root as next guess) for stability at
small t, and the verified DFT Fourier coefficients of H (via Hhat''(m)/(i*omega_m) = Hhat'(m))
to reconstruct H'(w) numerically.
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import K_series, V_series, M_series, solve_saddle, phi_saddle
from round1_fourier_dft_check import Hhat  # already-verified DFT Fourier coefficients of H

mp.mp.dps = 50
c = mp.log(3)
a_const = mp.mpf('0.5') - mp.log(2) / c

ln3 = mp.log(3)
beta = 1 / (2 * ln3)
gamma_exp = mp.mpf('-1.5') - (1 + mp.log(ln3 / 2)) / ln3
delta_exp = 1 + mp.log(ln3 / 2) / ln3


def phi_0(t):
    t = mp.mpf(t)
    L_ = -mp.log(t)
    return t ** gamma_exp * L_ ** delta_exp * mp.e ** (-beta * mp.log(t / L_) ** 2)


print("=== Part A: V_series(r) =? N=floor(log_3 r) + O(1) ===")
for r in [mp.mpf(10) ** k for k in [2, 4, 6, 8, 10, 12, 20, 40]]:
    v = V_series(r, terms=500)
    N = mp.floor(mp.log(r) / mp.log(3))
    print(f"  r=1e{int(mp.log10(r))}: V_series(r)={mp.nstr(v,10)}  N={N}  diff={mp.nstr(v-N,6)}")

print("\n=== Part B: cancellation check with continuation + prediction comparison ===")
# reconstruct H'(w) via truncated Fourier series using verified Hhat(m), m=1..4
H_TERMS = 4


def H_prime(w):
    total = mp.mpf(0)
    for m in range(1, H_TERMS + 1):
        om = 2 * mp.pi * m / c
        Hm = Hhat(m)
        # H(w) = sum_m [Hhat(m) e^{i om w} + conj], H'(w) = sum_m [i om Hhat(m) e^{i om w} + conj]
        term = 1j * om * Hm * mp.e ** (1j * om * w)
        total += 2 * term.real
    return total


def B0(w):
    return w / c - a_const


print(f"{'l':>4} {'t':>14} {'diagnostic':>14} {'predicted':>14} {'ratio(diag/pred)':>18}")
for l in [10, 20, 30, 40, 60, 80, 100, 130, 160, 200]:
    t = mp.mpf(l) * mp.mpf(3) ** (-l)
    t3 = 3 * t
    terms = max(300, l + 80)
    try:
        s_t = solve_saddle(t, terms)
        s_t3 = solve_saddle(t3, terms)
    except Exception as e:
        print(f"  l={l}: root-find failed ({e}), skipping")
        continue

    K_t = K_series(s_t, terms)
    V_t = V_series(s_t, terms)
    P_t = s_t / mp.sqrt(2 * mp.pi * V_t) * mp.e ** (K_t + s_t * t)

    K_t3 = K_series(s_t3, terms)
    V_t3 = V_series(s_t3, terms)
    P_t3 = s_t3 / mp.sqrt(2 * mp.pi * V_t3) * mp.e ** (K_t3 + s_t3 * t3)

    log_ratio_phi = mp.log(P_t3) - mp.log(P_t)
    log_ratio_phi0 = mp.log(phi_0(t3)) - mp.log(phi_0(t))
    diagnostic = log_ratio_phi - log_ratio_phi0

    w0 = mp.log(s_t)  # w_0(t) proxy: log of the smooth-saddle scale ~ log(s_t)
    predicted = -H_prime(w0) / B0(w0)

    ratio = diagnostic / predicted if predicted != 0 else mp.nan
    print(f"{l:4d} {float(t):14.4e} {float(diagnostic):14.8f} {float(predicted):14.8f} {float(ratio):18.4f}")
