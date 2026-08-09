# GAP A pivot, round 5: final closure

Date: 2026-08-09.

This was the fifth and final round of the fixed GAP A push.  The primary target
was H-014, the proposed uniform bound on doubling runs in `H(l,l+1)`.  The
round deliberately split into an exact computational stress test and a direct
structural attack.  The direct route was chosen because multiplication by 2
translates every exponent and therefore exposes exactly which boundary
witnesses obstruct a converse to the round-4 inclusion theorem.  The mod-9
and converse questions were used only after that route reached its genuine
missing lemma.

## Primary verdict: H-014 survives, but is not proved

The new hybrid sparse/packed exact DP in
`experiments/E-010-h014-maxrun/` computes the complete holdout set and its
longest doubling run.  It extends the exact range from `l=19` through `l=22`:

```text
l                 20         21         22
|H(l,l+1)|   5,044,358  7,156,001  8,951,079
maxrun               3          3          3
```

Across the now-complete range `l=3..22`, maxrun is

```text
2,2, 3,3,3,3,3, 4,4,4,4,4,4, 3,3,3,3,3,3,3.
```

Thus there is no counterexample through `l=22`, and the largest exact value is
still 4.  The `l=22` run took 131.81 seconds and 53,714,376 KiB peak RSS with
no swap.  At `l=23`, one packed layer is already about 10.96 GiB and the
current kernel needs many simultaneous layers; a naive run is well beyond the
host's 62 GiB physical memory.  It was not launched.  Reaching `l=23..30`
requires a qualitatively new state compression, not merely more wall time.

One Round-4 interpretation does not survive calibration.  Using the actual
rapidly falling density `p(l)=|H(l,l+1)|/phi(3^l)`, the iid longest-run scale
`log(phi(3^l))/log(1/p(l))` stays near 3--4 and tracks the observed hump to
within about one.  The earlier `~0.5l` comparison implicitly froze the density
at its small-level value.  This heuristic does not prove random behavior, but
the flat maxrun is no longer evidence by itself for a special anti-clustering
mechanism; the central issue is exponential thinning together with orbit and
bounded-span geometry.

The theoretical attack produced an exact reformulation.  Let

```text
S_l = R_(l-1,l+1) mod 3^l
```

and let `W(l,C)` consist of the `R_(l-1,l+C+1)` witnesses whose exponents lie
in `[0,2l+C]` and have span at most `2l`.  Then

```text
maxrun(H(l,l+1)) <= C  iff  W(l,C) covers every unit mod 3^l.
```

Indeed `W(l,C)` is exactly the union of the `C+1` translates
`S_l,2S_l,...,2^C S_l`.  A missing residue in that union is exactly a chain of
`C+1` consecutive holes after an overall power-of-2 rescaling.  This makes the
round-4 “full-width witness” obstruction precise: ordinary coverage by
`R_(l-1,l+C+1)` is insufficient unless every residue has a witness of span at
most `2l`.  For fixed `C`, the discarded wide tuples are not a sparse boundary
error; their proportion tends to `1-(C+2)/2^(C+1)` (equal to `13/16` for the
observed candidate `C=4`).

Three further exact local results were proved:

1. An exact prefix-fiber formula describes all three lift digits from the
   minimum exponent and the high digit of each prefix witness.  A hole forces
   all prefixes of minimum at least 2 to have the same high digit.
2. A three-chain of holes therefore imposes a one-digit rigidity condition on
   every prefix that can be shifted away from the lower boundary.
3. Any parent prefix with minimum exponent at least 4 can be revised and
   appended to cover all three children.  Consequently a five-chain in
   `H(l,l+1)` descends modulo `3^(l-1)` to a hole of `R_(l-2,l-2)`; more
   generally an `L`-chain descends to an `(L-4)`-chain in that lower
   complement.

These lemmas are real progress but do not bound the descended complement.
The remaining H-014 lemma is a uniform non-full-width witness-selection, or
equivalently a uniform anti-rigidity statement for complete prefix fibers.
No proof or counterexample family was found.

The external Fable leg independently used the same normalized width family
`U(l,W)` and found a useful narrower conjecture.  If

```text
D_l(W+1)=U(l,W+1) \ (U(l,W) union 2U(l,W)),
```

then every value in `D_l(W+1)` comes from a doubly saturated corner.  Exact
enumeration through `l=13` gives `D_l(W+1)=empty` for every `W>=2l+1`; the
only late essential corners occur in the immediately preceding step and have
small but growing counts.  Uniform corner redundancy in this range would make
the holdout erosion recurrence exact from budget `l+2` onward and would prove
the observed bootstrap tightness there.  It remains a finite-data conjecture,
not a theorem.

That leg initially claimed H-014 was equivalent to `j*(l)<=l+O(1)`.  The final
audit corrected this: the bootstrap proves only H-014 implies that covering
bound.  The restricted-width equivalence above shows why the converse does not
follow from ordinary coverage.

Full proof details are in `notes/GAP-A-round5-maxrun-proof-draft.md`; exact
computational details, certificates, validation, and resource use are in
`experiments/E-010-h014-maxrun/README.md`.

## Secondary closure: recurrence, congruences, and converse failures

Put

```text
A_l(j) = R_(l-1,j) mod 3^l,
K_l(j) = units mod 3^l outside A_l(j).
```

Splitting the exponent subsets according to whether they use the newly
available largest exponent gives the exact recurrence

```text
A_l(j+1) = A_l(j) union (2^(l+j) + 3 A_(l-1)(j+1))  (mod 3^l).
```

Together with `H(l,j)=2^(j-l)K_l(j)`, this proves two formerly empirical
near-extinction laws.  If `J=j*(l)>l`, then

```text
H(l,J-1) is contained in 1 mod 3,
H(l,J-1) = 2 * {x in H(l,J-2) : x == 2 mod 3}.
```

It also proves the unconditional two-class bound

```text
H(l,J-1) mod 9 is contained in {4^J, 4^(J+1)}.
```

The observed single-class law is precisely the exclusion of `4^J`.  A clean
sufficient statement is now isolated: every residue `x == 4^(j+1) mod 9` is
covered at budget `j` whenever `j>=l+3`.  This passes every exact case through
`l=15`; smaller slack has genuine counterexamples.  It remains unproved.

An additional exact extractor run reached the last holdouts at `l=21`:
`|H(21,24)|=43`, all in class `7 mod 9 = 4^(25+1) mod 9`; the 43 elements are
exactly the doubles of the class-`8 mod 9` minority in `H(21,23)`.  This
extends the class law and the proved near-extinction equality beyond Round 4's
`l=20` endpoint, but still does not prove the single-class exclusion.

Equivalently, if `W_min(x)` is the first width at which a normalized unit is
covered, every threshold witness has top exponent `W_min`, so
`x==(-1)^W_min mod 3`.  Its second-exponent parity is also determined by
`x mod 9`; the single-class law is exactly the assertion that all residues
with maximal death width share the observed second-exponent parity.  The exact
level recursion

```text
W_min^l(x) = min {W of the required parity :
  W_min^(l-1)((x-2^W)/3) <= W-1}
```

is proved, but does not yet force that extremal parity lock.

The strong converse to the holdout inclusion is false.  Exhaustively, at
`l=7,j=8`,

```text
1547 in 2H(7,8) intersection 4H(7,8), but 1547 not in H(7,9).
```

Its predecessors `2027,1867` form a two-chain of holes, while exhaustive
enumeration of all `C(18,9)=48620` tuples finds exactly two budget-9 witnesses
for 1547, and both touch both exponent boundaries.  The unrestricted lifetime
converse also fails: `H(6,6)` contains the five-chain
`187,374,19,38,76`, although `H(6,10)` is empty.  The narrower existential
equality `j*(l)=j+maxrun(H(l,j))` for `j>=l+1` remains open and still has no
computed exception.

Full details and the exact checker are
`notes/GAP-A-round5-secondary-draft.md` and
`experiments/E-009-holdout-chain-bootstrap/round5_secondary_closure.py`.

## Final calibrated registry verdicts

- **GAP A / H-003:** open.  The best unconditional asymptotic bound remains
  `j*(l) <= (119/104)l+O(1)`.  The round-4 bootstrap and the round-5 recurrence,
  width reformulation, and lift lemmas are citable structural advances, but
  none proves `l+O(1)` coverage or WCC.
- **H-011:** open, substantially sharpened.  Exact shift injections, the
  two-predecessor mask/carry state, the fixed-term recurrence, and the new
  prefix lift-mask formula are proved.  A uniform finite-state defect-repair
  theorem, including control of boundary/full-width fibers, is still absent.
- **H-012:** closed refuted as stated.  Universal `Delta j=1`, uniform
  `Delta d<=1`, and uniform micro-local repair all have explicit
  counterexamples.  The valid replacement is the proved holdout inclusion,
  chain contraction, and run-length bootstrap; those are theorems, not a
  surviving form of H-012.
- **H-013:** open but partly proved.  The exact sets and finite-cylinder laws
  through `l=20` remain empirical at full precision.  The mod-3 last-holdout
  law and the near-extinction pullback equality are now theorems, and mod 9 is
  rigorously narrowed to two classes.  Excluding the first candidate class `4^J`
  uniformly, and explaining the 13-family/sporadic higher-digit alternation,
  remain open.
- **H-014:** open, now explored.  Exact maxrun is at most 4 for every
  `l=3..22`, with no growth yet.  The exact restricted-width equivalence and
  local rigidity/repair lemmas identify the missing theorem, but no uniform
  bound is proved.

Difficulty assessment: the mod-9 single-class step is the narrowest remaining
piece and may plausibly yield to a finite cylinder/repair argument.  The
restricted existential bootstrap converse looks harder because its strongest
setwise form is false.  H-014 is harder still: it asks for uniform control of
complete witness fibers after a non-negligible full-width family is removed.
The exact H-013 higher-digit recurrence and GAP A itself remain the most global
problems; nothing in this five-round push makes either look close to a full
solution.
