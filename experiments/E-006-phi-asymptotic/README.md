# E-006: numerical evaluation of phi(t) near t=0, for H-006's Conjecture 3

## Attempt 1: Fourier inversion (phi_eval.py, sweep.py) -- FAILED, genuinely

`phi(t)` was evaluated via Fourier inversion of its known exact characteristic
function, using `mpmath` arbitrary precision. Validated correctly against a real,
solver-independent fact (`phi(0.3) = phi(0.7)`, since `X` is symmetric about 1/2).
But for `t_l = l*3^{-l}` with `l >= 8`, the oscillatory integral does not converge
under `mpmath.quad`: doubling the cutoff changes the answer by orders of magnitude
and even flips its sign, which is impossible for a density. `mpmath.quadosc` (the
dedicated oscillatory-integral routine) was also tried and also failed. This is a
genuine numerical-analysis failure of generic quadrature, not a "needs more time"
problem.

## Attempt 2: real-variable saddlepoint (saddlepoint.py) -- WORKS

Proposed by Codex (round 2 of the 2026-07-31 four-round "where are we stuck"
consultation, `/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck_round2_out.txt`).
Rather than inverting the characteristic function by oscillatory integration, solve
the real saddle equation `M(s) = s*t` (a monotone real root-find; `M(s) := -s*K'(s)`,
`K := log` of the Laplace transform, `M(s) = sum_r m(s/3^r)`, `m(x) = 1-2x/(e^{2x}-1)`),
then evaluate the (real, rapidly convergent) saddlepoint density formula
`phi(t) ~ s/sqrt(2*pi*V(s)) * exp(K(s)+s*t)` at the solved `s`. No oscillation
anywhere: `K`, `M`, and `V` (the second-cumulant analogue) are each sums of a
smooth, rapidly-decaying real function over `r=1,2,3,...`, truncated once terms
underflow below working precision.

**Validated two ways before trusting small-t results**:
1. `L(0) = exp(K(0)) = 1` (normalization), holds exactly.
2. At moderate `t` (0.1-0.4), where the Fourier method from attempt 1 still worked,
   the two independent methods agree to within the saddlepoint approximation's own
   expected `O(1/l)`-type error (e.g. `t=0.3`: Fourier gives `1.4867` [trusted, exact
   up to quadrature precision], saddlepoint gives `1.5093`, a ~1.5% difference,
   consistent with a genuine asymptotic approximation at a small effective scale).

**Then swept `l=3..40` (`t_l = l*3^{-l}`) with no failures at all**: the sequence
`ln(phi(t_l))` decreases smoothly and monotonically (values from `-0.98` at `l=3` to
`-804` at `l=40`), with no sign flips, no cutoff-dependence, no instability of any
kind -- the opposite of attempt 1's behavior. `l=40` corresponds to `t_l ~ 3.3e-18`,
far beyond anything attempt 1 could reach even in principle.

## Status

This is now a working, validated, arbitrary-depth evaluator for `phi(t_l)`. It does
NOT yet, by itself, test Conjecture 3 (which needs comparison against Berg-Kruppel's
specific `phi_0` normalization, not just an internally-consistent asymptotic for
`phi`). Fed the concrete numbers back to Codex in round 3 to identify the precise
next comparison. See `notes/H-006.md` for how this connects to the standing gap.
