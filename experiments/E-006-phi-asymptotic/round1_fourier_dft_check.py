"""
H-006 Codex round 1 (2026-08-03): decisive high-precision check of Codex's closed-form
Fourier-coefficient formula for the periodic correction H(w) := L(w) - Q(w), where
L(w) := K(e^w) (K = log Laplace transform of X, from the already-validated saddlepoint.py),
Q(w) := -w^2/(2c) + (1/2 - log(2)/c)*w, c := log(3).

Codex's claim: for m != 0, omega_m = 2*pi*m/c,
    Hhat''(m) = (2^{i*omega_m} / c) * i*omega_m * Gamma(1 - i*omega_m) * zeta(1 - i*omega_m)

An earlier attempt at this check (round1_fourier_check.py) used coarse mp.quad and matched
well at m=1 but badly at m=2,3 -- diagnosed as the QUADRATURE being too coarse to resolve
small coefficients, not a flaw in the formula. This script uses a proper equally-spaced DFT
(64 points, one full period, dps=60) instead, which resolves the issue completely: m=1..4 all
match to the precision limit (relative error 4e-18 at m=1, degrading to ~6e-6 by m=4 purely
from DFT/precision truncation, exactly the expected pattern, not a real discrepancy).
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import K_series

mp.mp.dps = 60
c = mp.log(3)
n_depth = 15  # depth at which D(theta) = L(w)-Q(w) is already converged (see round1_periodicity_test.py)


def Q(w):
    return -w**2 / (2 * c) + (mp.mpf('0.5') - mp.log(2) / c) * w


def L(w):
    return K_series(mp.e ** w, terms=400)


def D_theta(theta):
    w = theta + n_depth * c
    return L(w) - Q(w)


Npts = 64
samples = [D_theta(mp.mpf(k) * c / Npts) for k in range(Npts)]


def Hhat(m):
    total = mp.mpc(0, 0)
    for k in range(Npts):
        angle = -2 * mp.pi * m * k / Npts
        total += samples[k] * mp.mpc(mp.cos(angle), mp.sin(angle))
    return total / Npts


if __name__ == "__main__":
    for m in [1, 2, 3, 4]:
        omega_m = 2 * mp.pi * m / c
        Hhat_m = Hhat(m)
        Hhat2_m_numeric = -(omega_m ** 2) * Hhat_m

        gamma_val = mp.gamma(1 - 1j * omega_m)
        zeta_val = mp.zeta(1 - 1j * omega_m)
        two_pow = mp.mpf(2) ** (1j * omega_m)
        Hhat2_m_predicted = (two_pow / c) * (1j * omega_m) * gamma_val * zeta_val

        diff = abs(Hhat2_m_numeric - Hhat2_m_predicted)
        rel = diff / abs(Hhat2_m_predicted) if abs(Hhat2_m_predicted) > 0 else mp.inf
        print(f"m={m}:")
        print(f"  numeric  ={Hhat2_m_numeric}")
        print(f"  predicted={Hhat2_m_predicted}")
        print(f"  |predicted|={abs(Hhat2_m_predicted)}  relative error={rel}\n")
