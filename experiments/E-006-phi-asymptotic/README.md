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

## Attempt 3: derive phi_0's exponents from first principles, then test the ratio directly

Round 3 of the same Codex consultation derived `gamma`, `delta`, `beta` (the exponents
in `phi_0(t) ~ t^gamma*(-ln t)^delta*exp(-beta*ln^2(t/(-ln t)))`) directly from the
SAME saddlepoint expansion validated in attempt 2, by re-expressing the boxed
`l`-formula as a function of `t`. **`beta = 1/(2*ln 3) = 0.45511961...` matched an
independent hand-derived estimate (de Bruijn/Mahler-partition balance argument) done
earlier in this session, exactly** -- a real cross-check, not a coincidence.

`conjecture3_test.py` computes `phi_0(t_l)` with these derived exponents and the
ratio `R(l) := phi(t_l)/phi_0(t_l)` for `l=5..500` (`phi(t_l)` from the attempt-2
saddlepoint evaluator, `phi_0(t_l)` needing no external source at all -- Berg-
Kruppel's paper was never actually needed once the exponents were re-derived).

**Result**: `R(l)` decreases from `0.20996` (`l=5`) to a minimum `0.18272` near
`l=19-20`, then increases steadily out to `0.19953` at `l=500`, with no sign of
leveling off in the directly-computed range. Root-finding became unreliable past
`l=500` in the time available (an implementation limitation, not evidence about the
math).

**Round 4**: fed this exact data back to Codex, asking for a final, honest
assessment (not a confident-sounding guess). Codex proposed that the leading omitted
correction should be a quadratic-in-`log L` polynomial divided by `L`
(`log R = log C + (A2*x^2+A1*x+A0)/L`, `x := log L`, `L := -log t`), fit it using only
`l in {20,40,60,80}`, and predicted: (a) the dip-then-rise shape is exactly what this
correction structure produces, with a turning point at `L ~ 18.2`; (b) an
out-of-sample prediction `R_500 ~ 0.19951` (actual: `0.19953`); (c) a limiting
constant `C ~ 0.2050`.

**Independently re-verified (`fit_check.py`), not taken on faith**: refit the exact
same model on this project's own data, reproducing `C=0.204954`, and confirming both
claims to within rounding: out-of-sample `R_500` error `0.0127%` (Codex claimed
`~0.014%`), and the turning point (correctly derived via the chain rule accounting
for both the explicit `1/L` and the `x=log L` dependence, not a naive
`d/dx=0` shortcut) at `L=18.19`, matching the observed minimum (`L_19=17.93`,
`L_20=18.98`) almost exactly.

## Status

**Strong, independently-verified numerical evidence supporting Conjecture 3's
ratio-convergence claim**, with a specific candidate limit `C ~ 0.205`. This is
NOT a proof (Codex's own assessment: "numerically supported, not contradicted --
but not proved by this data"; no finite range rules out an arbitrarily slow
divergence engineered to mimic convergence through `l=500`). What would actually
settle it: an analytic next-order saddlepoint expansion with a controlled
remainder term, `O((log L)^4/L^2)`, not attempted here. See `notes/H-006.md` for
the full record and how this connects to the standing gap.
