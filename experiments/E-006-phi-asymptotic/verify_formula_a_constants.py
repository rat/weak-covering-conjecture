"""Independent high-precision audit for the explicit constants in the
formula-(A) proof written in notes/H-006-formula-A-proof.md.

This script is diagnostic, not a source of any inequality in the proof: the
proof gives analytic upper bounds.  It evaluates those upper-bound expressions
at 80 decimal digits, checks the integer threshold N=1500, and samples the
one-factor functions against direct numerical differentiation.
"""

import mpmath as mp

mp.mp.dps = 80


def ell(z):
    return mp.log((1 - mp.exp(-z)) / z)


def kappa(n, z):
    return (-1) ** n * z ** n * mp.diff(ell, z, n)


def kappa_formulae(z):
    x = z / 2
    csch2 = 1 / mp.sinh(x) ** 2
    coth = mp.cosh(x) / mp.sinh(x)
    return (
        1 - x ** 2 * csch2,
        2 - 2 * x ** 3 * csch2 * coth,
        6 - 4 * x ** 4 * csch2 * coth ** 2 - 2 * x ** 4 * csch2 ** 2,
    )


def main():
    a0 = 1 / (2 * mp.sqrt(2))
    q0 = mp.exp(-2 * a0)
    r0 = (1 + q0) / (1 - q0) ** 3
    t3 = 27 * mp.sqrt(2) * mp.exp(-3) * r0
    t41 = 16 * (16 * mp.exp(-4)) * (1 + q0) ** 2 / (1 - q0) ** 4
    t42 = 64 * mp.exp(-4) / (1 - q0) ** 4
    b3 = 2 + 2 * t3
    b4 = 6 + 4 * t41 + 2 * t42
    A = -mp.log(mp.sin(1))
    c_minus = (
        4 * mp.exp(-2) + 16 * mp.exp(-mp.mpf(5) / 2) / (mp.e - 1)
    ) / (1 - mp.exp(-1)) ** 2

    assert b3 < 46
    assert b4 < 675
    assert A < mp.mpf("0.173")
    assert c_minus < mp.mpf("3.28")
    assert 2 / (1 - mp.exp(-2)) ** 2 < 3
    assert 2000**4 > 393**5
    assert b3 < 63 and b4 < 785 and A < mp.mpf(1) / 5
    assert c_minus < 5
    assert (1 - mp.exp(-1)) ** -2 * (
        1 + 9 * mp.exp(-2) / (1 - 9 * mp.exp(-6))
    ) < 6
    assert 9 * mp.exp(3 / mp.e) / (2 * mp.sqrt(2 * mp.pi)) < 9
    assert 1520 / (3 * mp.sqrt(mp.pi)) < 304
    assert 2358 * mp.sqrt(2) < 3369
    assert 2 / mp.sqrt(mp.pi) < 2

    print("Analytic upper-bound expressions")
    for name, value, target in [
        ("B3", b3, 46),
        ("B4", b4, 675),
        ("-log(sin(1))", A, mp.mpf("0.173")),
        ("C_-", c_minus, mp.mpf("3.28")),
        ("2/(1-e^-2)^2", 2 / (1 - mp.exp(-2)) ** 2, 3),
    ]:
        print(f"  {name:18s} = {mp.nstr(value, 35)}  < {target}: {value < target}")

    print("\nCentral-arc threshold")
    print(f"  2000^4 = {2000**4}")
    print(f"  393^5  = {393**5}")
    print(f"  2000^(4/5) = {mp.nstr(mp.power(2000, mp.mpf(4)/5), 35)} > 393")
    print("  D4*a_N^2/24 <= (1179/24) N^(1/5) <= N/8 at N >= 2000")

    print("\nDirect formula/differentiation checks")
    max_error = mp.mpf(0)
    max_sample = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for b in [mp.mpf("0.02"), mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("1"), mp.mpf("3"), mp.mpf("10")]:
        for y in [mp.mpf("-1"), mp.mpf("-0.37"), mp.mpf("0"), mp.mpf("0.63"), mp.mpf("1")]:
            z = b * (1 + 1j * y)
            direct = [kappa(n, z) for n in (2, 3, 4)]
            closed = kappa_formulae(z)
            max_error = max(max_error, *(abs(u - v) for u, v in zip(direct, closed)))
            max_sample = [max(u, abs(v)) for u, v in zip(max_sample, closed)]
    print(f"  maximum formula error: {mp.nstr(max_error, 8)}")
    print("  maximum sampled moduli:", ", ".join(mp.nstr(v, 10) for v in max_sample))
    assert max_error < mp.mpf("1e-60")


if __name__ == "__main__":
    main()
