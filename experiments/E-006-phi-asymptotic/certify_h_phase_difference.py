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


if __name__ == "__main__":
    main()
