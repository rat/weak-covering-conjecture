"""
H-006 Codex round 3: corrected cancellation-rate diagnostic, per Codex's diagnosis. The
factor-~127 discrepancy in round 2 was attributed to comparing against Berg-Kruppel's phi_0
(different smooth prefactor/O(1/B_0) terms), not to the saddle proxy or Fourier derivative.
Fix: build phi_0_same using the SAME saddle-formula structure as phi_saddle, but with Q (smooth
part only, H=0) instead of L=Q+H, so the ONLY difference between phi_saddle and phi_0_same is
the periodic correction H itself.
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import K_series, V_series, solve_saddle, phi_saddle
from round1_fourier_dft_check import Hhat

mp.mp.dps = 50
c = mp.log(3)
a_const = mp.mpf('0.5') - mp.log(2) / c


def Q(w):
    return -w**2 / (2 * c) + a_const * w


def Qp(w):
    return -w / c + a_const


def Qpp(w):
    return -1 / c


def B0(w):
    return -Qp(w)


def L(w):
    return K_series(mp.e ** w, terms=400)


def H_of(w):
    return L(w) - Q(w)


def H_prime(w, terms=4):
    total = mp.mpf(0)
    for m in range(1, terms + 1):
        om = 2 * mp.pi * m / c
        Hm = Hhat(m)
        term = 1j * om * Hm * mp.e ** (1j * om * w)
        total += 2 * term.real
    return total


def w0_of_t(t, guess=None):
    """Root-find the SMOOTH-only saddle: t = e^{-w}*B0(w)."""
    def F(w):
        return mp.e ** (-w) * B0(w) - t
    if guess is None:
        guess = mp.log(1 / t)
    return mp.findroot(F, guess)


def phi0_same(w0, t):
    """Same saddle-formula STRUCTURE as phi_saddle (P = s/sqrt(2*pi*V)*exp(K+s*t)), but with
    Q instead of L (H=0). NOTE: must include the leading s=e^{w0} prefactor, matching
    phi_saddle's own P = s/sqrt(...)*exp(...) exactly -- missing it was round-3's first bug."""
    Vs = Qpp(w0) - Qp(w0)  # V_smooth(w) = Q''(w) - Q'(w), matching V(s)=s^2 K''(s)=L''-L' in w-coords
    s0 = mp.e ** w0
    return s0 / mp.sqrt(2 * mp.pi * Vs) * mp.e ** (Q(w0) + s0 * t)


print(f"{'l':>4} {'t':>12} {'diag_corrected':>16} {'D_FD':>14} {'D_1':>14} {'diag/D_FD':>12} {'D_FD/D_1':>12}")
for l in [10, 20, 30, 40, 60, 80, 100]:
    t = mp.mpf(l) * mp.mpf(3) ** (-l)
    t3 = 3 * t
    terms_saddle = max(300, l + 80)

    s_t = solve_saddle(t, terms_saddle)
    s_t3 = solve_saddle(t3, terms_saddle)
    K_t = K_series(s_t, terms_saddle)
    V_t = V_series(s_t, terms_saddle)
    logphi_t = mp.log(s_t / mp.sqrt(2 * mp.pi * V_t)) + K_t + s_t * t
    K_t3 = K_series(s_t3, terms_saddle)
    V_t3 = V_series(s_t3, terms_saddle)
    logphi_t3 = mp.log(s_t3 / mp.sqrt(2 * mp.pi * V_t3)) + K_t3 + s_t3 * t3

    w0_t = w0_of_t(t)
    w0_t3 = w0_of_t(t3)
    logphi0_t = mp.log(phi0_same(w0_t, t))
    logphi0_t3 = mp.log(phi0_same(w0_t3, t3))

    diagnostic = (logphi_t3 - logphi0_t3) - (logphi_t - logphi0_t)

    D_FD = H_of(w0_t3) - H_of(w0_t)
    D_1 = -H_prime(w0_t) / B0(w0_t)

    r1 = diagnostic / D_FD if D_FD != 0 else mp.nan
    r2 = D_FD / D_1 if D_1 != 0 else mp.nan
    print(f"{l:4d} {float(t):12.3e} {float(diagnostic):16.8f} {float(D_FD):14.8f} {float(D_1):14.8f} {float(r1):12.4f} {float(r2):12.4f}")
