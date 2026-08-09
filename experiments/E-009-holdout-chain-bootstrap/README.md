# E-009: holdout-set doubling maps, the run-length bootstrap, and the witness-level test of H-012

Round 4 of the fixed 5-round GAP A push (2026-08-08). Attacks H-012 directly (prove-or-falsify),
with H-013 extension and H-011 cross-links. Everything below was computed exactly (no sampling)
and every inclusion/bound was checked against the project's independently verified `j*(l)` table.

## Objects

`R_{j-1,j} = { F(alpha) = sum_{i=0}^{j-1} 2^{alpha_i} 3^i : 2j-1 >= alpha_0 > ... > alpha_{j-1} >= 0 }`.
`j*(l)` = least `j` with `R_{j-1,j}` covering all units mod `3^l`.
Holdout set `H(l,j)` = units mod `3^l` NOT covered by `R_{j-1,j}`.
Durfee depth of a witness = `#{ i : alpha_i >= j }` (verified identical to the round-32
partition-Durfee definition; 2000 random trials, exact).
A *doubling chain* of length `k` in a set `S` of units is `x, 2x, 4x, ..., 2^(k-1) x`, all in `S`
(mod `3^l`). `maxrun(S)` = the longest such chain (equals the longest run of consecutive values in
the base-2 discrete-log picture of `S`, since 2 is a primitive root mod `3^l`).

## Theorems (proved this round; elementary, fully verified computationally)

**Lemma 1 (shift maps).** For `j >= l`: if `r` is covered at budget `j`, then `2r` and `4r` are
covered at budget `j+1`. Proof: shift every exponent by 1 (resp. 2), which multiplies `F` by 2
(resp. 4) and stays inside the budget-`(j+1)` range `[0, 2j+1]`; then prepend a new smallest
exponent `b=0` (resp. `b in {0,1}`), adding `2^b 3^j == 0 (mod 3^l)`. The x2 half also follows in
one line from the known rescaling `R_{j-1,j} == 2^(j-l) R_{l-1,j} (mod 3^l)`; in the normalized
coordinates `H'(l,s) = 2^-(j-l) H(l,j)`, `s=j-l`, the pair of maps reads
`H'(s+1) subset H'(s) intersect 2 H'(s)`.

**Theorem 1 (holdout inclusions).** `H(l,j+1) subset 2H(l,j) intersect 4H(l,j)` for `j >= l`.

**Corollary 1 (chain contraction).** If `H(l,j+1)` is nonempty,
`maxrun(H(l,j+1)) <= maxrun(H(l,j)) - 1`. (A chain of length `k` in `H(j+1)` pulls back through
the two maps to the union `x/4, x/2, ..., 2^(k-2) x`, a chain of length `k+1` in `H(j)`.)

**Corollary 2 (run-length bootstrap).** `j*(l) <= j + maxrun(H(l,j))` for every `j >= l`; in
particular `j*(l) <= j + |H(l,j)|`. (Chains of length 0 mean the set is empty.)

Verified exactly at every computable pair: `l=5..16`, all `j` from `l` to `j*(l)`, plus `l=19`
(`j=20,21,22`) and `l=20` (`j=22,23`). Zero violations of either inclusion anywhere
(`verify_witness_maps_and_inclusions.py`, `extend_l15_l16.py`, `holdout_l19.py`, `holdout_l20.py`;
Lemma 1 additionally checked on 500 random witnesses, exact).

## The empirical law: the bootstrap is EXACTLY TIGHT for j >= l+1

At every computed level and every budget `l+1 <= j <= j*(l)`:

    j*(l) = j + maxrun(H(l,j))        [observed equality, 60+ instances, zero exceptions]

including the Delta-j=2 step (`l=10`), the plateau (`l=16`, where `H(16,19)` has 1182 elements yet
`maxrun=1`, which by Corollary 1 *proves* coverage at 20), and `l=19` at four orders of magnitude
larger scale (`|H(19,20)| = 3,195,464`, `maxrun=3`, `j*=23=20+3`). Only the `j=l` column has slack
(maxrun 7-9 vs true remaining budget 4-5). The forward inequality is Corollary 2; the converse
(a maximal chain forcing survival) is NOT proved and is the sharpest new open question this
experiment isolates.

maxrun table (rows `l`, columns `j-l`):

    l:            j=l  l+1  l+2  l+3  l+4  l+5
    5             4    3    2    1    0
    6             5    3    2    1    0
    7             5    3    2    1    0
    8             8    3    2    1    0
    9             8    3    2    1    0
    10            9    4    3    2    1    0
    11            8    4    3    2    1    0
    12            8    4    3    2    1    0
    13            8    4    3    2    1    0
    14            8    4    3    2    1    0
    15            8    4    3    2    1    0
    16            7    3    2    1    0
    19            .    3    2    1(*)  0(*)
    20            .    .    2    1(*)  0(*)

(*) `l=19`: `j*=23`, computed `j=20,21,22`; `l=20`: `j*=24`, computed `j=22,23`; the `j*` column
being 0 is the table's own `j*` value, not recomputed here except where stated.

**Consequence if `maxrun(H(l,l+1))` stays bounded** (observed: 3 or 4 for every `l=5..16` and
`l=19`): `j*(l) <= l + 5` for all `l`, far below the proven `(119/104) l` bound. This does NOT by
itself prove Wirsching's WCC (which needs `e(l) = o(l)`, i.e. `j* = log_4(3) l + o(l)`), but it
would be the strongest covering bound known by a wide margin. Registered as H-014.

## H-012 verdict: falsified as stated, replaced by the weaker true statements

Three independent falsifications of the strong forms:

1. **Universal Delta-j=1 lifting is false from the project's own table**: `j*(9)=13` but
   `j*(10)=15`. Any rule "coverage at `(l,j)` implies coverage at `(l+1,j+1)`" would give
   `j*(10) <= 14`. The failure set of the Delta-j=1 induction at `l=10` is exactly
   `H(10,14) = {37912, 47389}` = H-013's `l=10` holdout pair. H-012 and H-013 study the same object.
2. **Witness-level `Dd<=1` (min Durfee depth) is false at the exact transition Codex specified**,
   `(6,10)->(7,11)`: 100 of 1458 children have `d'_min(child) - d_min(parent) >= 2` (up to +3).
   Same at `(7,11)->(8,12)`: 332 of 4374 violations (`witness_check_6_7.py`, `witness_check_7_8.py`).
   The *stratum-ceiling* version does hold on all data (`D_7=5=D_6+1`, `D_8=5=D_7+0`).
3. **A uniform micro-local repair rule is false**: minimal symmetric-difference edit distance
   between the parent fiber's witnesses and the child fiber's witnesses is 1 for ~95.5% of children
   but reaches 7 (out of a possible 21) already at `l=6`, and again exactly 7 at `l=7`
   (distributions `{1:1392, 3:9, 5:52, 7:5}` and `{1:4205, 3:7, 5:135, 7:27}`). No growth trend
   between the two transitions; boundedness is open.

Lift-mask data reproduces H-011's picture at witness level: 98.35% (l=6) and 98.70% (l=7) of
parents have all 3 children hit directly; 9 resp. 22 missing children.

## H-013: extensions and corrections

`H(l, j*(l)-1)` (the level's last holdout set), computed exactly:

    l=5  {229}                       l=11 {33550}            cls {16}
    l=6  {304,430,565}               l=12 {212932,483148,488494} cls {64,550}
    l=7  9 elts, 8 classes           l=13 {513472}           cls {256}
    l=8  22 elts, 16 classes         l=14 {2532112,2952745,3648211} cls {295}
    l=9  48 elts, 19 classes         l=15 {6357088}          cls {208}
    l=10 {37912,47389}  cls {4}      l=16 1182 elts, 32 classes (plateau)
    l=19 (see holdout_l19 output)    l=20 (see holdout_l20 output)

Corrections/refinements to H-013's registry row:

- The `l=14` "near-miss correction" is wrong: `295 = 4^5 mod 729` EXACTLY (`1024-729`). The x4
  class law `class(l) = 4^(l-9) mod 3^6` is exact at every `l=10..14`, no correction term.
- `l=15` continues the "13-family": `208 = 13*4^2 mod 729` exactly.
- The x4 drift now has a mechanism: it is the shadow of Theorem 1 (`H(l,j+1) subset 4H(l,j)`),
  applied at the level where the budget increments. Element-level genealogy is partial: the chain
  `37912 -(x4 of lift)-> 33550 -(x4 of lift)-> 488494` is exact
  (`33550 = 4*(37912 + 1*3^10) mod 3^11`, `488494 = 4*(33550 + 2*3^11) mod 3^12`), and
  `3648211 = 4*(513472 + 1*3^13) mod 3^14` is exact, but `513472`'s own `/4` pullback (`128368`)
  is a *fresh* defect of `H(13,16)`, not a lift of `H(12,16)`'s elements: the class-level law
  survives level transitions even where the element-level chain breaks.
- At every `l <= 14`, `H(l-1, j*(l)-1)` is empty, so the last holdouts are always children of
  covered parents (pure H-011-type defects, no inherited holes).

## The mod-9 single-class law of last holdouts (found while extending H-013)

Computed after the main tables (same scripts plus the inline check recorded in
`notes/H-003.md`'s round-4 section):

1. **Every element of `H(l, j*(l)-1)` is `== 1 (mod 3)`, at every computed level** (`l=5..20`).
2. **`H(l, j*(l)-1)` occupies a SINGLE class mod 9**, and that class follows
   `class(l+1) = 4^(Delta j*) * class(l) (mod 9)` exactly across every transition `l=5..16`,
   including the Delta-j*=2 step (`x16` at `l=9->10`) and the plateau (`x1` at `l=15->16`), and
   extrapolates correctly to `l=19` (`4^3 == 1 (mod 9)` across `j*(19)-j*(16)=3`).
   Equivalently: every element of `H(l, j*(l)-1)` is `== 4^(j*(l)+1) (mod 9)`.
3. Conditional derivation: mod 9, children of a residue equal the residue (`l >= 2`), so
   same-budget holdouts propagate their class upward in `l`, and Theorem 1 shifts the class by 4
   per budget step. IF the single-class property holds (which is exactly the old rounds-1-16
   "mod-9 clustering" anomaly, now structural), the `4^(Delta j*)` law follows rigorously.
4. An exact characterization one step before extinction, forced by (1) plus the size data:
   elements of `H(j*-1)` are `==1 mod 3`, so their halves are `==2 mod 3`, giving
   `H(j*-1)/2 subset {x in H(j*-2): x==2 mod 3}`; the counts are EQUAL at every computed level,
   hence **`H(l, j*-1) = 2 * { x in H(l, j*-2) : x == 2 (mod 3) }`** exactly (12/12 levels).
   Near extinction the doubling map is not just an inclusion but a bijection onto the mod-3
   minority class, the same phenomenon as the bootstrap tightness.

## Pointwise coverage is NOT monotone in j (found via the l=13 ancestry funnel)

Residue `128368 mod 3^13` is covered at budgets 13 and 14, NOT covered at 15 and 16, covered
again at 17 (`nonmonotone_coverage.py`, with an explicit hand-checkable budget-14 witness).
The mechanism is 0-locking: when every witness of a residue contains exponent 0, no
residue-preserving extension to the next budget exists. Two consequences:

- The folklore "coverage is monotone in j" (assumed by `jstar-fast`'s bisection since H-001
  began) is FALSE pointwise. Full-coverage monotonicity IS true, but its only proof on record
  is this experiment's Theorem 1: `H(l,j)` empty implies `H(l,j+1) subset 2H(l,j)` empty.
  The bisection is sound, for a previously unarticulated reason.
- `128368` is also the "fresh defect" whose x4 image is level 13's final holdout `513472`, and
  its halving orbit `8023*{1,2,4,8}` is the maximal 4-chain of `H(13,14)`: the entire death
  chronology of level 13 is one geometric 2-progression (`513472 = 64 * 8023` exactly, as
  integers). The ancestry funnel demanded by Theorem 1 (`h*2^-s in H(17-t)` for `s in [t,2t]`)
  verifies exactly at every depth `t=1..4`.

## Files

- `verify_witness_maps_and_inclusions.py`: Lemma 1 (500 random exact checks), Theorem 1 and the
  bootstrap for `l=5..14`, all budgets; H-013 blocks. Runtime ~3 s.
- `extend_l15_l16.py`: same for `l=15,16` plus the exact x4 genealogy checks. ~30 s.
- `witness_check_6_7.py`, `witness_check_7_8.py`: exhaustive witness-level H-012 tests
  (enumerating 184756+705432 resp. 705432+2704156 tuples). ~15 s / ~3 min.
- `holdout_l19.py`: numpy bool DP, `3^19` residues, budgets 20,21,22 (~27 GB peak). ~15 min.
- `holdout_l20.py`: bigint-bitset DP, `3^20` residues, budgets 22,23 (~11 GB). ~1 h.

Run from this directory with `python3 <script>`. All scripts print PASS/FAIL-style lines; any
"VIOLATED"/"FALSIFIED" in the output means a claim above failed to reproduce.
