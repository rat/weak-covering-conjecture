"""
H-006 round 15 direct inversion, v2: fixed-grid Simpson integration instead of adaptive mp.quad
(which was too slow / got stuck), since the integrand is smooth and decaying.
"""
import mpmath as mp
import time

mp.mp.dps = 30


def K_complex(s, terms):
    total = mp.mpc(0, 0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += mp.log((1 - mp.e ** (-2 * x)) / (2 * x))
        denom *= 3
    return total


def K_real(s, terms):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += mp.log((1 - mp.e ** (-2 * x)) / (2 * x))
        denom *= 3
    return total


def M_real(s, terms):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += 1 - 2 * x / (mp.e ** (2 * x) - 1)
        denom *= 3
    return total


def V_real(s, terms):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for r in range(1, terms + 1):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 5)):
            break
        total += 1 - (x / mp.sinh(x)) ** 2
        denom *= 3
    return total


def R_ratio(s, terms, y_max=20, n_points=400):
    t = M_real(s, terms) / s
    K_s = K_real(s, terms)
    V_s = V_real(s, terms) / s ** 2
    sqrtV = mp.sqrt(V_s)

    h = mp.mpf(2 * y_max) / n_points
    total = mp.mpc(0, 0)
    # Simpson's rule over [-y_max, y_max], n_points intervals (n_points+1 nodes)
    for i in range(n_points + 1):
        y = -y_max + i * h
        arg = s + 1j * y / sqrtV
        val = K_complex(arg, terms) - K_s + 1j * t * y / sqrtV
        f = mp.e ** val
        if i == 0 or i == n_points:
            w = 1
        elif i % 2 == 1:
            w = 4
        else:
            w = 2
        total += w * f
    integral = total * h / 3
    return integral / mp.sqrt(2 * mp.pi)


if __name__ == "__main__":
    print(f"{'N':>4} {'R_N':>22} {'N*(R_N-1)':>14} {'time_s':>8}")
    for N in [7, 8, 9, 10, 11, 12]:
        s = mp.mpf(3) ** N / 2
        terms = N + 80
        t0 = time.time()
        R = R_ratio(s, terms=terms, y_max=15, n_points=300)
        dt = time.time() - t0
        val = N * (R.real - 1)
        print(f"{N:4d} {mp.nstr(R,10):>22} {float(val):14.6f} {dt:8.1f}   (im={float(R.imag):.2e})")

    print(f"\nPredicted limit: -1/12 = {float(mp.mpf(-1)/12):.6f}")
