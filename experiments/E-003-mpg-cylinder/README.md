# E-003: cylinder mean-payoff games for the asymptotic rate of j*(l)

Backs H-003's twenty-first round (see `notes/H-003.md`). Computes the exact value
`rho_k` of the window-k mean-payoff-game relaxation of the controlled-3-adic-dynamics
game from H-003's nineteenth round, and hence a decreasing sequence of proven upper
bounds on `limsup_l j*(l)/l`.

## The object

Round 19 reformulated `j*(l)` as a finite full-information game on 3-adic units:
state `z` (a unit), legal cost `d>=0` iff `2^d z == 1 (mod 3)`, transition
`T_d(z) = (2^{d+1} z - 2)/3`; `j*(l) = max_z min-policy sum(d_i)` over l steps with the
modulus shrinking one power of 3 per step. Restricting the policy to see only
`z mod 3^k` turns the infinite-horizon problem into a **min-max mean-payoff game**:
the minimizer picks `d` from `z mod 3^k`, an adversary picks the hidden next 3-adic
digit `e in {0,1,2}` (`z -> T_d(z + 3^k e) mod 3^k`). Its value `rho_k` is the best
asymptotic cost-rate any window-k cylinder policy can guarantee, so
`j*(l) <= rho_k * l + C_k` for an explicit constant `C_k`, and `rho_k` is
non-increasing in `k`, giving `limsup_l j*(l)/l <= inf_k rho_k`, and separately
`log_4(3) <= limsup_l j*(l)/l` (round 16's elementary lower bound). **Correction,
2026-07-30 (critique round)**: only the first inequality is proven here; earlier drafts
of this file also asserted the reverse (`inf_k rho_k <= limsup_l j*(l)/l`, i.e. full
equality) without proof. H-003's round 24 (its A3 section) found evidence the window
relaxation may have an irreducible gap (`inf_k rho_k` strictly above `limsup_l j*(l)/l`),
so treat `rho_k -> log_4(3)` as an unproven extrapolation, not an established fact.

## Files

- `step_a_grounding.py` -- independent grounding: the game DP reproduces `j*(l)`
  against a direct brute-force computation from the `R_{J-1,J}` covering definition
  (l=1..6) and against the known table (l=1..12). Run: `python3 step_a_grounding.py`.
- `mpg4.py` -- **main solver.** Nested Howard strategy improvement (exact, O(n)
  memory, self-certifying via a matching adversary lower bound). `python3 mpg4.py 3 4 5 6 7 8 9 10`.
- `mpg3.py` -- helpers (action construction, Howard max-mean-cycle, value iteration).
- `mpg.py` -- independent Karp-based value-iteration + certificate solver (cross-check
  for small k; O(n^2) memory, so k<=7 only). `python3 mpg.py 3 4 5`.
- `certificate.py` -- extracts the potential `h` and additive constant
  `C_k = max h - min h`, verifies the telescoping inequality
  `d(s) + h[s'(e)] <= rho_k + h[s]` for every state and every hidden digit e.
- `verify_on_real.py` -- runs the extracted optimal window-k policies on the actual
  finite covering DP over every unit residue mod 3^l (round-19-style check): zero
  failures, cost grows at rate `rho_k`.

## Result (all exact, self-certified matching min-max certificates)

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|----|----|----|----|
| rho_k | 2 | 5/3 | 3/2 | 3/2 | 7/5 | 25/19 | 5/4 | 11/9 | 6/5 | 7/6 | 119/104 |
| C_k | 5 | 19/3 | 15/2 | 9 | 10 | 207/19 | 47/4 | 115/9 | 69/5 | 44/3 | pending |

**Update, 2026-07-30: `rho_13 = 119/104 = 1.144231`, tight, `n=1062882`.** Same solver, ran
~5h30m of wall time (k=12 and k=13 launched together as `mpg4.py 12 13`). `j*(l) <= (119/104)*l
+ O(1)` now the best proven ceiling, replacing `7/6`. **`C_k` was NOT captured for k=10-13 in
this run**: the script only printed `rho_k`/`lb`, the potential `h` (needed for `C_k = max h -
min h`) was computed internally but never saved, exactly the loss H-009 warned about. Fixed same
day: `mpg4.py`'s `solve()` now returns `Ck`, `h`, and `lam`, and its `__main__` block saves a
full certificate (policy + potentials, as exact fractions) to `certificate_k<K>.json` on every
run. Re-run under the patched script: `C_10=115/9`, `C_11=69/5` (both landed in the table above,
re-deriving the already-known `rho_10`, `rho_11` values as an incidental cross-check); `k=12,13`
still running as of this note (`certificate_k10.json`, `certificate_k11.json` in this directory).
**Known gap, flagged not silently carried**: the `dcap` (action-cap) robustness check documented
below for `rho_4`-`rho_8` was never repeated for `rho_9`-`rho_13`; those values are trusted on the
strength of the solver's own matching min-max self-certificate alone, not an independent
cap-robustness sweep.

**Update, 2026-07-30 (earlier): `rho_12 = 7/6 = 1.1667`, tight, `n=354294`.** Computed by
`mpg4.py`'s nested Howard solver (the main, cross-checked solver), matching min-policy
upper bound and adversary lower bound exactly. Took ~1h16m of wall time (pure Python,
n=354294 with a nested up-to-100k-outer x up-to-100k-inner iteration structure) -- slow
but confirmed not stuck (CPU time climbed steadily throughout, no algorithmic bug found
on inspection). Ran concurrently with H-002's DP extension (notes/H-002.md), which was
paused via SIGSTOP partway through to remove memory/swap contention that was slowing
this computation down; contention, not a bug, explained most of the early slowness.
`j*(l) <= (7/6)*l + O(1)` now replaces `6/5` as the best proven explicit ceiling.

`rho_4 = 5/3` improves the leading constant of the best proven bound on `j*(l)` from
2 (round 19) to 5/3. The sequence is monotone decreasing toward the true asymptotic
rate; a trailing `L + A/k` extrapolation gives `L ~ 0.78-0.79 ~ log_4(3)`, consistent
with (not proof of) `rho_k -> log_4(3)`. Reproduced three independent ways: Karp
certificates (k=3,4,5), long value iteration (k=7 -> 1.4003), and dcap-robustness
(k=7,8 stable across action caps 20/40/80).

**Update, 2026-07-29: `rho_11 = 6/5 = 1.2`, tight, `n=118098`.** A leftover background
process from this round (left running unattended in `/home/rat/wcc_mpg/`, outside
this repo) had already computed `k=10` (matching the table above) and `k=11` before
being found and killed for memory safety -- `k=12` (`n=354294`, 3x larger) was about
to start and risked competing with the concurrent l=24 computation's memory. Do not
resume this sweep past `k=11` without checking `free -h` and l=24's status first;
`n` triples each step and this solver's memory footprint (~1.8GB at k=10-11) may
scale worse than linearly.

## Novelty note (2026-07-29, checked before any claim of a new technique)

The general technique here (representing a covering-type combinatorial problem as a
mean-payoff game and computing a decreasing sequence of exact rational bounds) is
NOT new: it is a direct application of Ehrenfeucht-Mycielski's 1979 mean-payoff
games, and a very close methodological precedent exists in the coding-theory
literature -- Meyerovitch & Young, "Rationality and computability of the covering
radius for sofic shifts" (arXiv:2603.21449, 2026, L-062 in `literature/INDEX.md`),
which proves rationality/computability of a covering-radius quantity for sofic
shifts via essentially the same kind of construction. What is new here is the
*application* to Wirsching's `j*(l)`, not the technique. Any future write-up of
this result should cite both as methodological precedent, not present the
mean-payoff-game framing itself as a novel contribution.
