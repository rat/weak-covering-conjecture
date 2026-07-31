# E-007: Frobenius-mod-3 non-vanishing check for S(t) (H-003, GAP A)

## What this tests

From the 2026-07-31 four-round Codex consultation on H-003/H-006's open fronts (full
prompts/responses in `/home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck_round*.txt`).
Codex proposed reducing the exponential sum's generating polynomial mod 3, using that
`(1+u)^3 = 1+u^3 mod 3` (Frobenius) exactly matches the `X -> X^3` step in this
project's rank-coupling recursion, and that `Phi_{3^L}(1+u) = u^{2*3^{L-1}} mod 3`
(3 is totally ramified in `Z[zeta_{3^L}]`). So `S(t) = 0` for some/every `t` coprime
to 3 (`S(t)` values at different `t` are Galois conjugates of each other) forces
`u^{2*3^{L-1}} | G_{N,m}(u) mod 3`, where `G_{N,m}(u) := F_{N,m}(1+u) mod 3` and
`F_{N,m}(X) = sum over N>a_0>...>a_{m-1}>=0 of X^{sum_i 2^{a_i} 3^i}` (the generating
polynomial for `S(t) = F_{N,m}(zeta_{3^L}^t)`).

## What was verified

`valuation_check.py`:
1. Brute-force verifies the recursion `F_{N,m}(X) = F_{N-1,m}(X) + X^{2^{N-1}} *
   F_{N-1,m-1}(X^3)` against a direct enumeration, N=1..6, exact match every case.
2. Computes the u-adic valuation (order of vanishing at u=0) of `G_{2j,j}(u) mod 3`
   for the actual `R_{j-1,j}` parameters this project uses (`N=2j`, `m=j`: `j`
   exponents drawn from domain `{0,...,2j-1}`), for `j=1..30`.

**Result: the valuation stays at 0 or 1 for every `j` tested**, including `j=30`
(corresponding to `l ~ 27-38` via `j ~ log_4(3)*l`, well past this project's current
computed frontier `l=23`). Since the vanishing threshold `2*3^{L-1}` in the
contrapositive of eq. (4) grows exponentially in `L` while the observed valuation
does not grow at all over this range, **this proves `S(t) != 0` for every `t` coprime
to 3, at every `L` tested, for the `R_{j-1,j}` family** -- the exponential sum never
vanishes exactly, at least in the range checked.

## Honest scope: this is real, but it is not the magnitude bound GAP A needs

This rules out exact vanishing (a zero-set statement), not smallness of `|S(t)|`. It
is a genuine partial result on GAP A -- new to this project (25+ prior rounds never
found this specific Frobenius-mod-3 reduction) -- but Codex's own confidence rating
for it supplying the actual needed magnitude bound was honest and low (0.25).
Extending the u-adic valuation machinery from "stays small" to an actual quantitative
magnitude bound on `|S(t)|` is unsolved; this is the natural next question if this
lead is picked up further.

## Status

Verified finding, recorded 2026-07-31. Fed back into round 2 of the ongoing Codex
consultation cycle (see `HYPOTHESES.md`/`notes/H-003.md` for the corresponding entry).
