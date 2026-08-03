"""
H-006 Codex round 6: verify the corrected cumulant expansion (6.2),
Im(log(e^{-iut(r)}*chi_r(u))) = -T_r*(u/r)^3/6 + O(u^5),
T_r := sum_j kappa_3(b_{j,r}), kappa_3(b) = 2 - 2*x^3*csch^2(x)*coth(x), x=b/2, b_j=2r*3^{-j}.

Given round 1's own definitions, individual tilted summands Y_{j,r} = r*(2/3^j)*U_j, so
X = sum_j Y_{j,r}/r, meaning each summand's OWN frequency argument, when expanding chi_r(u) =
E_r[e^{iuX}], is u/r (not u directly) -- this project's first attempt at this check used u
directly and got a huge mismatch (predicted values ~1e6 larger than observed); tracked down to
this scaling bug, not a flaw in Codex's formula. After correcting, the match is excellent.
"""
import mpmath as mp
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
from saddlepoint import M_series

mp.mp.dps = 50


def kappa3(b):
    x = b / 2
    return 2 - 2 * x ** 3 / mp.sinh(x) ** 2 * (mp.cosh(x) / mp.sinh(x))


def T_of(r, terms=300):
    T = mp.mpf(0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        b = 2 * r / denom
        if b < mp.mpf(10) ** (-40):
            break
        T += kappa3(b)
        denom *= 3
    return T


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


def t_of_r(r, terms=150):
    return M_series(r, terms) / r


if __name__ == "__main__":
    for r in [mp.mpf(100), mp.mpf(1000)]:
        T_r = T_of(r)
        t_r = t_of_r(r)
        print(f"r={float(r)}, T_r={float(T_r):.6f}")
        for u_frac in ['0.01', '0.05', '0.1', '0.2', '0.3']:
            u = mp.mpf(u_frac) * r
            chi = F_complex(r - 1j * u, 300) / F_complex(r, 300)
            log_term = mp.log(chi * mp.e ** (-1j * u * t_r))
            im_obs = log_term.imag
            pred = -T_r * (u / r) ** 3 / 6
            ratio = im_obs / pred if pred != 0 else mp.nan
            print(f"  u/r={u_frac}: im_obs={float(im_obs):.6e}  pred=-T_r*(u/r)^3/6={float(pred):.6e}  ratio={float(ratio):.4f}")
