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
non-increasing in `k` with `inf_k rho_k = limsup_l j*(l)/l >= log_4(3)`.

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

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|----|----|
| rho_k | 2 | 5/3 | 3/2 | 3/2 | 7/5 | 25/19 | 5/4 | 11/9 | 6/5 |
| C_k | 5 | 19/3 | 15/2 | 9 | 10 | 207/19 | 47/4 | -- |

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
