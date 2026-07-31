"""
Phase-locking sweep for H-006's Conjecture 3: evaluate phi(t_l) at t_l = l*3^{-l}
for a range of l, and compare against the LEADING-ORDER saddle-point form
G0(t) = exp(-beta*ln(1/t)^2), beta = 1/(2*ln 3) (derived from the truncated
equation phi'(t) = (9/2)*phi(3t), t<2/3, by the standard de Bruijn/Mahler-partition
balance argument: try phi ~ exp(-beta*L^2), L=ln(1/t), match the leading exponential
order between phi'(t) ~ -2*beta*L/t and (9/2)*phi(3t) ~ (9/2)*exp(-beta*(L-ln3)^2)).

IMPORTANT LIMITATION, stated up front: this G0 is only the LEADING exponential
order. It omits the power-law prefactor (t^gamma) and log-log correction
(ln(-ln t)^delta) terms that Berg-Kruppel's actual eq.(9.6) g_0 carries, because
those constants were not re-extracted from L-097 with confirmed precision this
session. So this script does NOT test Conjecture 3 itself (phi/g_0 -> const).
It tests a WEAKER, necessary consequence: does ln(phi(t_l)) + beta*ln(1/t_l)^2
(the log-residual after removing the leading exponential order) behave in a
bounded, structured way as l grows, or does it diverge / oscillate wildly?
A bounded, slowly-varying residual is consistent with (necessary for, not
sufficient to prove) the phase-locking mechanism; wild unbounded growth would
refute the leading-order form itself.

Precision is set per-l from the expected magnitude (phi(t_l) ~ exp(-beta*L^2)),
plus a safety margin for cancellation in the oscillatory Fourier integral.
"""
import math
import time
import mpmath as mp


def run(l, xi_max=1200, margin_digits=40):
    t = mp.mpf(l) * mp.mpf(3) ** (-l)
    beta_f = 1 / (2 * math.log(3))
    L = -math.log(float(t))
    expected_exponent_digits = beta_f * L * L / math.log(10)
    dps = int(expected_exponent_digits) + margin_digits
    mp.mp.dps = dps

    beta = mp.mpf(1) / (2 * mp.log(3))
    # Need 9^{-N} below 10^{-dps} (tail-truncation error of the sinc product,
    # accounting for xi up to xi_max ~ 1e3-1e4): N > dps / log10(9) ~ 1.05*dps.
    N_TERMS = max(40, int(dps * 1.2) + 30)

    def integrand(xi):
        if xi == 0:
            return mp.mpf(1)
        prod = mp.mpf(1)
        denom_pow = mp.mpf(3)
        for r in range(1, N_TERMS + 1):
            arg = xi / denom_pow
            prod *= mp.sin(arg) / arg
            denom_pow *= 3
        return mp.cos(xi * (mp.mpf('0.5') - t)) * prod

    t0 = time.time()
    val = mp.quad(integrand, [0, xi_max]) / mp.pi
    elapsed = time.time() - t0

    ln_phi = mp.log(val) if val > 0 else mp.mpf('-inf')
    Lm = mp.log(1 / t)
    residual = ln_phi + beta * Lm * Lm  # ln(phi) - (-beta L^2) = ln(phi) + beta L^2

    return dict(l=l, t=t, dps=dps, N_TERMS=N_TERMS, phi=val, ln_phi=ln_phi,
                residual=residual, elapsed=elapsed)


if __name__ == "__main__":
    print(f"{'l':>3} {'t_l':>14} {'dps':>5} {'phi(t_l)':>16} {'ln(phi)':>14} "
          f"{'ln(phi)+beta*L^2':>18} {'time(s)':>8}")
    results = []
    for l in range(3, 17):
        r = run(l)
        results.append(r)
        print(f"{r['l']:3d} {float(r['t']):14.6e} {r['dps']:5d} "
              f"{float(r['phi']):16.6e} {float(r['ln_phi']):14.4f} "
              f"{float(r['residual']):18.6f} {r['elapsed']:8.1f}")

    print("\nresidual = ln(phi(t_l)) + beta*ln(1/t_l)^2, beta=1/(2 ln 3)")
    print("If this residual settles into a slowly-varying (e.g. near-linear-in-L,")
    print("matching gamma*L, or bounded oscillatory) pattern rather than diverging,")
    print("that is consistent with (not proof of) the phase-locking mechanism.")
