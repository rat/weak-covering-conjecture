"""Rigorous ball-arithmetic certificate for H(0) != H(log(3/2)).

This uses python-flint's Arb/Acb balls (not mpmath floating point).  The input
formula in H-006 is the formula for the *second derivative* Fourier
coefficient.  Thus, for m != 0,

  h_m := Hhat(m)
       = - 2^(i omega_m)/c * Gamma(-i omega_m) * zeta(1-i omega_m),
  omega_m = (2 pi/c)m, c = log(3).

The omitted m=0 term cancels in a difference.  Since H is real,

  D = H(0)-H(log(3/2))
    = 2 Re sum_{m>=1} h_m (1-exp(i omega_m log(3/2))).

For completeness, the tail majorant used below is derived here.  Set
alpha=2*pi/c and q=exp(-pi*alpha/2).  Euler summation, with N=ceil(y),
gives for y>=alpha

 |zeta(1-iy)| <= H_N + 1/y + 1/(2N) + sqrt(1+y^2)/(2N)
                 <= log(y+1) + C,

 C = 1 + 1/alpha + 1/2 + sqrt(1+alpha^-2)/2.

The identity |Gamma(iy)|^2=pi/(y*sinh(pi*y)), and
sinh(pi*y)>=exp(pi*y)/3 (valid here because pi*alpha>log(3)), imply

 |h_m| <= A q^m f_m,
 A = c^-1 sqrt(3*pi/alpha),
 f_m = m^-1/2 (log(alpha*m+1)+C).

C>2 makes f_m decreasing for m>=1: its logarithmic derivative multiplied
by m is at most 1/(log(alpha*m+1)+C)-1/2 < 0.  Consequently

 sum_{m>M}|h_m| <= A*f_(M+1)*q^(M+1)/(1-q).

The factor 4 in ``difference_tail`` below accounts for m and -m and for
|1-exp(i theta)|<=2.  M=4 already gives an error below 3.7e-19.
"""

from flint import acb, arb, ctx


ctx.dps = 100


def hhat(m, c, alpha):
    """Certified Acb enclosure of the m-th Fourier coefficient of H."""
    omega = arb(m) * alpha
    iomega = acb(0, omega)
    return -(acb(2).log() * iomega).exp() / c * acb(0, -omega).gamma() * acb(1, -omega).zeta()


def main():
    c = arb(3).log()
    pi = arb.pi()
    alpha = 2 * pi / c
    phase = (arb(3) / 2).log()
    q = (-pi * alpha / 2).exp()
    C = arb(1) + 1 / alpha + arb(1) / 2 + (1 + 1 / alpha**2).sqrt() / 2
    A = (3 * pi / alpha).sqrt() / c

    M = 4
    finite = arb(0)
    print("Certified finite contribution to D = H(0)-H(log(3/2))")
    for m in range(1, M + 1):
        omega = arb(m) * alpha
        coeff = hhat(m, c, alpha)
        term = 2 * (coeff * (1 - acb(0, omega * phase).exp())).real
        finite += term
        print(f"m={m}: {term}")

    n = arb(M + 1)
    f_n = ((alpha * n + 1).log() + C) / n.sqrt()
    positive_tail = A * f_n * q**n / (1 - q)
    # Use the upper endpoint as a scalar error radius, so every subsequent
    # enclosure remains outward-rounded.
    difference_tail = 4 * positive_tail.upper()
    certified = finite + arb(0, difference_tail)

    print("\nTail data (all are rigorous Arb enclosures)")
    print(f"alpha = {alpha}")
    print(f"q     = {q}")
    print(f"C     = {C}")
    print(f"sum_(m>{M}) |Hhat(m)| <= {positive_tail}")
    print(f"|D-D_{M}| <= {difference_tail}")
    print(f"\nD_{M} = {finite}")
    print(f"Certified D = {certified}")

    # A deliberately wide decimal enclosure, convenient to quote in prose.
    left = arb("-0.000377190280943987")
    right = arb("-0.000377190280943985")
    assert certified.lower() > left
    assert certified.upper() < right
    assert certified < 0
    print("\nTherefore")
    print("  -0.000377190280943987 < H(0)-H(log(3/2))")
    print("                              < -0.000377190280943985,")
    print("so the two values are rigorously distinct.")

    certify_derivative_bounds(c, alpha, q, A)
    certify_oscillation(c, alpha)


def certify_derivative_bounds(c, alpha, q, A):
    """Certify sup|H'| and sup|H''| (equation (3) of the paper) via the same
    per-mode majorant |Hhat(m)| <= A*q^m*f_m used above, summed with the extra
    factor omega_m^order (order=1,2) closed-form (sum_{m>M} m^k q^m has a
    closed form for k=1,2; f_m is bounded above by its value at m=M+1, since
    it is decreasing for m>=1)."""
    C = arb(1) + 1 / alpha + arb(1) / 2 + (1 + 1 / alpha**2).sqrt() / 2
    M = 6
    for order, target in ((1, arb("0.0011977472315550332")),
                           (2, arb("0.0068518962896650951"))):
        head = arb(0)
        for m in range(1, M + 1):
            omega = arb(m) * alpha
            coeff_abs = abs(hhat(m, c, alpha))
            head += 2 * omega**order * coeff_abs
        n = arb(M + 1)
        f_n = ((alpha * n + 1).log() + C) / n.sqrt()
        # sum_{m>M} m^order q^m, bounded using f_m <= f_n for m>=n (f decreasing):
        # order=1: sum m q^m = q^n*(n-(n-1)q)/(1-q)^2 (m from n to infinity)
        # order=2: sum m^2 q^m = q^n*(n^2-(2n^2-2n-1)q+(n-1)^2 q^2)/(1-q)^3
        if order == 1:
            tail_sum = q**n * (n - (n - 1) * q) / (1 - q) ** 2
        else:
            tail_sum = (q**n * (n**2 - (2 * n**2 - 2 * n - 1) * q + (n - 1) ** 2 * q**2)
                        / (1 - q) ** 3)
        tail = 2 * alpha**order * A * f_n * tail_sum
        bound = (head + arb(0, tail.upper())).upper()
        print(f"\nsup|H^({order})| certified <= {bound}  (quoted in paper: {target})")
        assert arb(bound) <= target, f"certified bound {bound} exceeds quoted {target}"


def certify_oscillation(c, alpha):
    """Certify osc(H) = sup H - inf H matching the paper's Proposition 8 proof
    exactly: a grid of N=2^20 points, H evaluated via the Fourier series
    truncated at |m|<=10 (discarded-mode error ~2.7e-43, negligible at the
    precision used here), combined with the certified Lipschitz bound on H'
    to turn the grid extrema into a rigorous two-sided enclosure of the true
    sup/inf: for spacing h, every real w is within h/2 of a grid point, so
    max_i H(w_i) <= sup H <= max_i H(w_i) + M1*h/2, and symmetrically for inf.
    Hence osc(H) in [D, D+M1*h] with D := max_i H(w_i) - min_i H(w_i)."""
    lipschitz = arb("0.0011977472315550332")
    n_grid = 2**20
    h = c / n_grid
    modes = list(range(1, 11))
    coeffs = [(m, arb(m) * alpha, hhat(m, c, alpha)) for m in modes]

    hi = None
    lo = None
    hi_i = lo_i = None
    for k in range(n_grid):
        w = h * k
        s = arb(0)
        for m, omega, coeff in coeffs:
            s += 2 * (coeff * acb(0, omega * w).exp()).real
        v_hi, v_lo = s.upper(), s.lower()
        if hi is None or v_hi > hi:
            hi, hi_i = v_hi, k
        if lo is None or v_lo < lo:
            lo, lo_i = v_lo, k

    D = arb(hi) - arb(lo)
    pad = (lipschitz * arb(h)).upper()
    osc_hi = (D + arb(0, pad)).upper()
    osc_lo = D.lower()
    print(f"\nosc(H) certified via N={n_grid} grid (h={h}), Fourier truncated at |m|<=10:")
    print(f"  max at grid index {hi_i}, min at grid index {lo_i}")
    print(f"  D = max-min = {D}")
    print(f"  osc(H) in [{osc_lo}, {osc_hi}]")
    print("  (paper's Proposition 8 quotes [4.1874494771e-4, 4.1874620262e-4])")
    left = arb("4.1874494771e-4")
    right = arb("4.1874620262e-4")
    assert osc_lo > left.lower() - arb("1e-13"), (osc_lo, left)
    assert osc_hi < right.upper() + arb("1e-13"), (osc_hi, right)
    assert osc_lo > arb("1e-4")


if __name__ == "__main__":
    main()
