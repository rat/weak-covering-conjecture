"""
H-006 Codex round 7: verify gamma_r := kappa_{3,r}/sigma_r^3 = T_r/V_r^1.5 = O((log r)^{-1/2}),
Codex's claim for why the genuine cubic term doesn't worsen formula (A)'s final O((log r)^{-1/4})
local-CLT rate (since O(L^{-1/2}) is strictly smaller).
"""
import mpmath as mp

mp.mp.dps = 30


def kappa2(b):
    x = b / 2
    return 1 - x ** 2 / mp.sinh(x) ** 2


def kappa3(b):
    x = b / 2
    return 2 - 2 * x ** 3 / mp.sinh(x) ** 2 * (mp.cosh(x) / mp.sinh(x))


def TV(r, terms=400):
    T = mp.mpf(0)
    V = mp.mpf(0)
    denom = mp.mpf(3)
    for j in range(1, terms + 1):
        b = 2 * r / denom
        if b < mp.mpf(10) ** (-30):
            break
        T += kappa3(b)
        V += kappa2(b)
        denom *= 3
    return T, V


if __name__ == "__main__":
    for r in [100, 1000, 1e4, 1e6, 1e8]:
        r = mp.mpf(r)
        T_r, V_r = TV(r)
        gamma_r = T_r / V_r ** mp.mpf('1.5')
        L = mp.log(r)
        ratio = gamma_r / L ** mp.mpf('-0.5')
        print(f"r={float(r):.0e}: T_r={float(T_r):.4f} V_r={float(V_r):.4f} "
              f"gamma_r={float(gamma_r):.6f} L^-0.5={float(L**-0.5):.6f} ratio={float(ratio):.4f}")
