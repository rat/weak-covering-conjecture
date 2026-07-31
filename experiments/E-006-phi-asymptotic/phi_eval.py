"""
Numerical evaluation of phi(t) near t=0, for H-006's Conjecture 3 phase-locking check.

phi is the density of X = sum_{r=1}^infty U_r/3^r, U_r iid Uniform[0,2].
Characteristic function: phihat(xi) = E[e^{i xi X}] = exp(i xi/2) * prod_r sinc(xi/3^r),
sinc(y) := sin(y)/y (since sum_r 3^-r = 1/2 and E[e^{i theta U}] for U~Unif[0,2] is
e^{i theta} sinc(theta)).

Fourier inversion (phi real => use the cosine form):
    phi(t) = (1/pi) * integral_0^infty cos(xi*(1/2 - t)) * prod_{r=1}^N sinc(xi/3^r) dxi

Two independent evaluators are implemented and cross-checked before trusting small-t values:
  (A) Fourier inversion via mpmath high-precision quadrature (this file).
  (B) A finite-N grid convolution (Kabaya-Iri/Rvachev's own validated recursive method),
      in phi_grid_check.py, used only as a moderate-t sanity check (its grid resolution
      cannot resolve t ~ 3^-15 directly).

Known exact facts usable as unconditional sanity checks, independent of any solver:
  - integral_0^1 phi(t) dt = 1
  - phi(t) = phi(1-t) (symmetry, since U_r ~ Unif[0,2] is symmetric about 1)
"""
import mpmath as mp

mp.mp.dps = 25  # working precision: 25 significant decimal digits (fast first pass)

N_TERMS = 40  # terms in the sinc product; 3**-40 ~ 1.2e-19 is far below working precision


def phihat_real_part_integrand(xi, t):
    """cos(xi*(1/2 - t)) * prod_{r=1}^N sinc(xi / 3^r)."""
    if xi == 0:
        return mp.mpf(1)
    prod = mp.mpf(1)
    denom_pow = mp.mpf(3)
    for r in range(1, N_TERMS + 1):
        arg = xi / denom_pow
        prod *= mp.sin(arg) / arg if arg != 0 else mp.mpf(1)
        denom_pow *= 3
    return mp.cos(xi * (mp.mpf('0.5') - t)) * prod


def phi(t, xi_max=None, verbose=False):
    """Evaluate phi(t) via Fourier inversion. t must be a mpmath mpf in [0,1]."""
    t = mp.mpf(t)
    if xi_max is None:
        # The sinc product decays super-exponentially (roughly Gaussian in log xi);
        # xi_max is chosen generously and cross-checked by doubling it below.
        xi_max = mp.mpf(2000)

    def integrand(xi):
        return phihat_real_part_integrand(xi, t)

    val = mp.quad(integrand, [0, xi_max]) / mp.pi
    if verbose:
        val2 = mp.quad(integrand, [0, xi_max * 2]) / mp.pi
        print(f"  [xi_max={xi_max}] phi={val}  [xi_max={xi_max*2}] phi={val2}  diff={abs(val-val2)}")
    return val


if __name__ == "__main__":
    print("Sanity checks (must hold regardless of small-t behavior):")

    import time
    t0 = time.time()

    # 2) Symmetry: phi(0.3) should equal phi(0.7).
    p03 = phi(mp.mpf('0.3'), xi_max=100)
    print(f"  phi(0.3)={p03}  [{time.time()-t0:.1f}s]")
    p07 = phi(mp.mpf('0.7'), xi_max=100)
    print(f"  phi(0.7)={p07}  (expect equal to phi(0.3))  [{time.time()-t0:.1f}s]")

    # 3) Convergence in xi_max at a moderate point.
    print("  xi_max convergence check at t=0.1:")
    phi(mp.mpf('0.1'), xi_max=150, verbose=True)
    print(f"  [{time.time()-t0:.1f}s]")
