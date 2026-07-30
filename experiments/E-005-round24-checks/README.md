# E-005: first-pass numerical checks on H-003's round-24 (gpt-5.6-sol) candidate directions

Backs `notes/H-003.md`'s round-24 follow-up section. Not a paper-bound experiment; a quick,
honest first look at the two GAP A/B items that were directly checkable against existing
validated machinery (A1's concatenation identity, A2/B3's shallow-cylinder occupancy),
before deciding whether either is worth deeper investment.

## Files

- `verify_a1_concatenation.py` -- tests Codex's proposed concatenation identity for the
  low-rank-absorber direction (A1). Result: false as literally stated (0/5000), true once
  corrected to include the connecting ("join") gap between the prefix and suffix (5000/5000).
  Run: `python3 verify_a1_concatenation.py`.
- `shallow_cylinder_occupancy.py` -- computes exact shallow-cylinder occupancy `q_{l,r}`
  (A2's refutation-hunt target, B3's lower-bound-sharpening target) at the true critical
  budget `j=j*(l)`, for every `l=4..23` and `r` up to 12, in under 2 seconds, via a
  reduced-modulus rerun of the same rotation-DP H-002 already validated (mod `3^r` instead
  of mod `3^l`, exact since reduction mod `3^r` only depends on the `r` largest chosen
  exponents). Includes its own sanity check against the full-modulus DP before trusting the
  shortcut. Run: `python3 shallow_cylinder_occupancy.py`.

## Headline finding (preliminary, not yet independently reviewed)

Across every scaling tested (fixed `r`, `r~sqrt(l)`, fixed ratios `r/l~0.33` and `~0.7`, and
`r` up to 12 at the largest available `l=23`), `-log(q_{l,r})` grows roughly linearly in `r`
and is close to independent of `l` once `l` is comfortably larger than `r`. No sign of
`q_{l,r}` decaying exponentially in `l` at any tested scaling. Weighs against A2's
refutation hope in this range; suggestive (not proof) that B3's target bound could be much
stronger than "sub-polynomial" if the pattern extends (`q ~ exp(-c*r)` at `r=l^delta` would
give an `e(l) >= c'*l^delta - O(1)` lower bound, well past the current `(1/4)*log_2(l)`).

**Not confirmed past `l=23`**: a naive attempt to extrapolate `j` for `l>23` (constant
offset on `log_4(3)*l`, and separately the proven-safe `rho_13` bound with a small guessed
constant) undershoots the true `j*(l)` and breaks the covering property itself well before
`l=80` (some shallow cylinder gets zero tuples, `q=0`). A concrete illustration of why
`e(l)` cannot be waved away with a small constant. Extending this analysis past `l=23`
needs a properly justified `j(l)` schedule, not naive extrapolation; deferred.

## Update: the pattern above does not survive a decisive test (Gemini caught this)

Sent to Gemini (`gemini-3.6-flash`, max thinking, independent vendor) as an adversarial review.
It gave 5% confidence the pattern was genuine, predicting that `C(l,r):=-log(q_{l,r})/r` must
roll over (decline) as `r/l -> 1`, since covering is known to hold at `r=l` with a modest,
bounded `e(l)` -- extrapolating the shallow-`r` linear trend to `r=l^delta` would assume the
conclusion. Tested directly: `rollover_test.py` pushes `r` up to 13 (kept small to avoid
competing with concurrent memory-heavy runs) at `l=14,16,18,20,23`, reaching `r/l` up to 0.93.
**`C(l,r)` peaks near `r=2` and declines monotonically at every `l` tested, all the way to the
largest `r/l` reached.** This confirms Gemini's prediction and corrects the headline finding
above: what looked like sustained linear growth was the front end of a concave, decelerating
curve, visible only because the original test never pushed `r` far enough relative to `l`.
Consistent with (not evidence for or against beyond) the mainstream expectation that `e(l)` grows
slowly. This numerical probe is closed; see `notes/H-003.md`'s matching section for full detail
and a methodological note on the failure mode this illustrates (a bounded-range test can look
like a trend simply because it never reaches a known boundary condition).
