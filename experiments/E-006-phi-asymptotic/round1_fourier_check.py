"""
H-006 Codex round 1: verify Codex's specific closed-form Fourier-coefficient formula for H''
(the periodic correction's second derivative), against a numerically-extracted Fourier
coefficient of H itself (converted via Ĥ''(m) = -omega_m^2 * Ĥ(m)).

Codex's claim: for m != 0, omega_m = 2*pi*m/c (c = log 3),
    Ĥ''(m) = (2^{i*omega_m} / c) * i*omega_m * Gamma(1 - i*omega_m) * zeta(1 - i*omega_m)

Numerically extract Ĥ(1) by sampling D(theta) = L(theta) - Q(theta) (already confirmed
periodic and converged, from h006_r1_periodicity_test.py) over one full period, then doing
a direct DFT-style numerical Fourier integral:
    Ĥ(m) = (1/c) * integral_0^c D(theta) * e^{-i*omega_m*theta} dtheta
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import K_series

mp.mp.dps = 40
c = mp.log(3)
n_depth = 15  # depth at which D(theta) is already converged (from part 2 of the prior script)


def Q(w):
    return -w**2 / (2 * c) + (mp.mpf('0.5') - mp.log(2) / c) * w


def L(w):
    return K_series(mp.e ** w, terms=300)


def D_theta(theta):
    w = theta + n_depth * c
    return L(w) - Q(w)


# --- numerically extract Fourier coefficient Hhat(1) via direct quadrature ---
m = 1
omega_m = 2 * mp.pi * m / c


def integrand_re(theta):
    return D_theta(theta) * mp.cos(-omega_m * theta)


def integrand_im(theta):
    return D_theta(theta) * mp.sin(-omega_m * theta)


print("Computing Hhat(1) via numerical quadrature over one period [0, c)...")
re_part = mp.quad(integrand_re, [0, c / 2, c]) / c
im_part = mp.quad(integrand_im, [0, c / 2, c]) / c
Hhat_1_numeric = mp.mpc(re_part, im_part)
print(f"  Hhat(1) [Fourier coeff of H itself] = {Hhat_1_numeric}")

Hhat2_1_from_numeric = -(omega_m ** 2) * Hhat_1_numeric
print(f"  => implied Hhat''(1) = -omega_1^2 * Hhat(1) = {Hhat2_1_from_numeric}")

# --- Codex's closed-form prediction ---
print("\nCodex's closed-form prediction:")
gamma_val = mp.gamma(1 - 1j * omega_m)
zeta_val = mp.zeta(1 - 1j * omega_m)
two_pow = mp.mpf(2) ** (1j * omega_m)  # = e^{i*omega_m*ln2}
Hhat2_1_predicted = (two_pow / c) * (1j * omega_m) * gamma_val * zeta_val
print(f"  omega_1 = 2*pi/c = {omega_m}")
print(f"  Gamma(1-i*omega_1) = {gamma_val}")
print(f"  zeta(1-i*omega_1)  = {zeta_val}")
print(f"  predicted Hhat''(1) = {Hhat2_1_predicted}")

print(f"\nCOMPARISON:")
print(f"  numeric   Hhat''(1) = {Hhat2_1_from_numeric}")
print(f"  predicted Hhat''(1) = {Hhat2_1_predicted}")
diff = abs(Hhat2_1_from_numeric - Hhat2_1_predicted)
rel = diff / abs(Hhat2_1_predicted) if Hhat2_1_predicted != 0 else mp.inf
print(f"  |diff| = {diff},  relative = {rel}")
