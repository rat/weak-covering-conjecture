"""
H-006 Codex round 14: verify V_r-N and T_r-2N are uniform-in-rho constants (not just bounded)
across N, confirming the claimed extension of formula (A) from the subsequence r_N=3^N/2 to all
r=rho*3^N/2, rho in [1,3).
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
    print(f"{'rho':>6} {'N':>4}   {'V_r-N':>12} {'T_r-2N':>12}")
    for rho in [mp.mpf('1.0'), mp.mpf('1.3'), mp.mpf('1.5'), mp.mpf('2.0'), mp.mpf('2.5'), mp.mpf('2.9')]:
        for N in [10, 20, 30, 40]:
            r = rho * mp.mpf(3) ** N / 2
            T_r, V_r = TV(r)
            print(f"{float(rho):6.2f} {N:4d}   {float(V_r-N):12.6f} {float(T_r-2*N):12.6f}")
        print()
