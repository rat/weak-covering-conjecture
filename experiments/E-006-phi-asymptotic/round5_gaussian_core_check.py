"""
H-006 Codex round 5: test the FINAL claimed Gaussian-core inequality directly on our REAL X
(not the "uniform-sum model" Codex's derivation route used, which appears inconsistent with
round 1's own established fact that the r-tilted summands are TRUNCATED EXPONENTIAL, not
uniform -- flagged separately). This checks the OUTPUT claim regardless of the internal
derivation route's correctness.

Claim: log(e^{-iu*t(r)} * chi_r(u)) = -v(r)*u^2/2 - R_r(u), R_r(u) >= 0 (nonnegative remainder,
i.e. the true log-characteristic-function-ratio never EXCEEDS the pure Gaussian term), for
|u| <= r/2.
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import V_series, K_series

mp.mp.dps = 50


def F_complex(s, terms=200):
    total = mp.mpc(1, 0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total *= (1 - mp.e ** (-2 * x)) / (2 * x)
        denom *= 3
    return total


from saddlepoint import M_series


def t_of_r(r, terms=150):
    """t(r) = -K'(r), via the existing M_series (M(r) = -r*K'(r), so K'(r) = -M(r)/r)."""
    return M_series(r, terms) / r


print(f"{'r':>8} {'u/r':>8} {'log(chi)':>16} {'-v*u^2/2':>16} {'R_r(u)':>14} {'R>=0?':>8}")
for r in [mp.mpf(100), mp.mpf(1000)]:
    v = V_series(r, terms=300) / r ** 2  # v(r) := K''(r) = V_series(r)/r^2
    t_r = t_of_r(r)
    for u_frac in [mp.mpf('0.01'), mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.2'),
                   mp.mpf('0.3'), mp.mpf('0.4'), mp.mpf('0.5')]:
        u = u_frac * r
        chi = F_complex(r - 1j * u, 300) / F_complex(r, 300)
        log_term = mp.log(chi * mp.e ** (-1j * u * t_r))  # log(e^{-iut}*chi), computed as product first to avoid branch issues
        log_val = log_term.real
        imag_check = log_term.imag
        gaussian = -v * u ** 2 / 2
        R = -(log_val - gaussian)  # R_r(u) = -(log_val - gaussian) = gaussian - log_val
        ok = "YES" if R >= -mp.mpf('1e-15') else "NO <---"
        print(f"{float(r):8.0f} {float(u_frac):8.2f} {float(log_val):16.8f} {float(gaussian):16.8f} {float(R):14.8f} {ok:>8}  (im={float(imag_check):.2e})")
