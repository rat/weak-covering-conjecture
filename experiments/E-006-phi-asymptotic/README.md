# E-006: attempted numerical phase-locking check for H-006's Conjecture 3

## What this tests

H-006's Conjecture 3 (see `notes/H-006.md`) needs `phi(z_l)/phi_0(z_l) -> c > 0` along
`z_l ~ l*3^{-l}`. A proposed mechanism (Codex, round 27) suggested the ratio might
"phase-lock" along this specific sequence even though it need not converge off-sequence.
This experiment attempts a cheap numerical check: evaluate `phi(t_l)` for `t_l = l*3^{-l}`
and several `l`, and look for a stable pattern.

## What was built

`phi_eval.py` implements `phi(t)` via Fourier inversion of the known exact characteristic
function `phihat(xi) = exp(i*xi/2) * prod_{r=1}^N sin(xi/3^r)/(xi/3^r)` (`phi` is the density
of `X = sum_r U_r/3^r`, `U_r` iid Uniform`[0,2]`), using `mpmath` arbitrary-precision
arithmetic. `sweep.py` sweeps `l` and compares `ln(phi(t_l))` against the leading-order
saddle-point exponent `-beta*ln(1/t_l)^2`, `beta = 1/(2*ln 3)` (derived by hand from the
truncated equation `phi'(t) = (9/2)*phi(3t)` via the standard de Bruijn/Mahler-partition
balance argument -- this is only the leading exponential order, not Berg-Kruppel's full
`g_0` with its power-law and log-log correction terms, whose exact constants were not
re-extracted from L-097 this session).

## Result: the method is correctly implemented but does not converge for small t

**Validation passed**: `phi(0.3) == phi(0.7)` to all computed digits, confirming the
characteristic-function/Fourier-inversion setup is correct (`X` is symmetric about 1/2,
a real, checkable fact, independent of any solver).

**But the small-t evaluation fails, genuinely, not just slowly**: for `l >= 8`
(`t_l ~ 1.2e-3`), doubling the integration cutoff `xi_max` does not converge the integral;
values swing by orders of magnitude and change sign, which is impossible for a density.
Switching to `mpmath.quadosc` (its dedicated oscillatory-integral routine) also produced a
result inconsistent with the expected order of magnitude. This is not a "needs more time"
problem: generic numerical quadrature, even at high working precision, is not resolving
this oscillatory integral reliably once the target value becomes as small as the log^2
decay predicts (astronomic cancellation between an O(1)-amplitude oscillating integrand and
a target value as small as `1e-9` to `1e-50`+ for the `l` range of interest).

## Why, and what would actually work

This confirms the assessment already recorded in `notes/H-006.md`: evaluating this family
of atomic functions reliably near a boundary point is a real numerical-analysis problem,
not a quick script. Volk (L-099) wrote an entire dedicated paper solving exactly this for
the simpler `a=2` case, using Taylor-expansion/Horner-scheme evaluation at dyadic points
derived from the function's exact piecewise-polynomial structure, not generic quadrature.
The analogous approach here would use the exact rational polynomial-piece construction
established in Kabaya-Iri (1987, L-105, Theorem 2/Lemma 4) and Berg-Kruppel (L-096): `phi`
is polynomial (with rational coefficients, computable via a finite recursive construction)
on each interval of the complement of the underlying Cantor set, and `t_l` for large `l`
lies deep in this recursive interval hierarchy. Building that construction correctly for
`alpha=2/3` is a real, bounded implementation task, not attempted here.

## Status

Deferred, not resolved. If picked up again: implement the exact polynomial-piece recursion
with `fractions.Fraction` (exact rational arithmetic, no precision/convergence concerns) as
described above, rather than any form of numerical quadrature.
