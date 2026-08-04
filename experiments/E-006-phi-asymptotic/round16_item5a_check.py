"""
H-006 Codex round 16: verify item 5(a), the K''(r) expansion via the exact-recurrence remainder.

A(r) := w/c - 1/2 + (log(d)-1)/c + H''(w) - H'(w),  w:=log(r), c:=log(3), d:=2
Test: Q(r) := e^{d*r}/r^2 * (V_series(r) - A(r)) = O(1)  (should stay bounded, not blow up)

H', H'' reconstructed SPECTRALLY (not by finite differences, which Codex warned would be
swamped) using the already-verified Fourier coefficients Hhat(m) from round 1 (m=1..4).
"""
import sys
sys.path.insert(0, '/home/rat/weak-covering-conjecture/experiments/E-006-phi-asymptotic')
import mpmath as mp
from saddlepoint import V_series
from round1_fourier_dft_check import Hhat

mp.mp.dps = 40
c = mp.log(3)
d = mp.mpf(2)
H_TERMS = 4


def H_prime(w):
    total = mp.mpf(0)
    for m in range(1, H_TERMS + 1):
        om = 2 * mp.pi * m / c
        Hm = Hhat(m)
        term = 1j * om * Hm * mp.e ** (1j * om * w)
        total += 2 * term.real
    return total


def H_double_prime(w):
    total = mp.mpf(0)
    for m in range(1, H_TERMS + 1):
        om = 2 * mp.pi * m / c
        Hm = Hhat(m)
        term = (1j * om) ** 2 * Hm * mp.e ** (1j * om * w)
        total += 2 * term.real
    return total


def A_of_r(r):
    w = mp.log(r)
    return w / c - mp.mpf('0.5') + (mp.log(d) - 1) / c + H_double_prime(w) - H_prime(w)


print(f"{'r':>12} {'V_series(r)':>16} {'A(r)':>16} {'Delta':>14} {'Q=Delta*e^(dr)/r^2':>20}")
for r in [mp.mpf(5), mp.mpf(10), mp.mpf(20), mp.mpf(30), mp.mpf(50)]:
    Vr = V_series(r, terms=max(300, int(r) + 100))  # NOT divided by r^2: compare to A(r) directly
    A_r = A_of_r(r)
    delta = Vr - A_r
    Q = delta * mp.e ** (d * r) / r ** 2
    print(f"{float(r):12.2f} {float(Vr):16.10f} {float(A_r):16.10f} {mp.nstr(delta,6):>14} {mp.nstr(Q,8):>20}")
