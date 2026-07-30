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
