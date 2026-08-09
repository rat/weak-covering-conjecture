# GAP A pivot, round 4: direct H-011/H-012/H-013 results

Date: 2026-08-08.

This round attacked the three registered local/repair hypotheses directly.  It
produced one exact finite H-012 transition theorem together with two precise
counterexamples to stronger versions, an H-011 witness map and sharply reduced
finite state, and an exact H-013 extension through `l=20`.

## H-012: the requested `(6,10) -> (7,11)` check passes, but strict global
## `Delta j=1` and the universal-witness formulation fail

Direct enumeration used all `C(20,10)=184756` parent witnesses and
`C(22,11)=705432` child witnesses.  The independent checker is
`experiments/E-007-frobenius-mod3-valuation/round4_h012_witness_transition.py`.

Restricting the parent certificate to Durfee depth `d<=4` leaves 60,626
witnesses and still covers all 486 units modulo `3^6`.  Their masks modulo
`3^7` have sizes `3:476, 2:9, 1:1`, so they realize 1,447 of the 1,458 unit
children and leave 11.  At the child budget, the 352,716 witnesses with
`d'<=5` cover all 1,458 units.  Every raw-`F` hole has
`min d'(child) <= max d(parent fiber)+1`; the tight holes are 262, 1216, and
1720.

For the genuine same-diagram normalization

```text
E(alpha) = (alpha_0+1,...,alpha_9+1,0),
F_11(E(alpha)) = 2 F_10(alpha) + 3^10,
```

the 11 missing children are

```text
{74,245,524,875,1055,1064,1253,1496,1685,1820,2002}.
```

All repair.  Their minimum exponent-exchange distances from an actual
canonical parent witness are `1:2, 2:1, 3:7, 4:1`.  More strongly, one can
select a single witness in each parent fiber that serves all three normalized
children; the maximum-of-three radius census over the 486 parents is
`1:462, 2:10, 3:13, 4:1`.

The quantifier "every parent witness repairs with `Delta d<=1`" is false:
53 of the 60,626 parent witnesses fail on 67 child instances.  A concrete
counterexample is raw parent 434 with `d=0` and
`alpha=(9,8,...,0)`.  Its canonical child base is 139 and the three children's
minimum depths are `(0,2,1)`, so child 868 needs `Delta d=2`.  The unique child
requiring `d'=5` is 2002; its canonical parent 272 has old depths 3 and 4, and
only the selectable depth-4 witness gives the required `+1` step.  Thus
coverage plus a depth cap is not induction-closed: a proof must preserve a
"good representative" state.

The unchanged global one-budget-step induction from the covered base `(6,10)`
also fails exactly at `(9,13)->(10,14)`.  Two structurally different exact DPs
(integer fiber counts and a Python-integer support bitset), plus the existing
Rust implementation's image-size check, give

```text
(9,13):  13122/13122 units covered
(10,14): 39364/39366 units covered; holes {37912,47389}
(10,15): 39366/39366 units covered.
```

Explicit `(9,13)` parent witnesses are certified in
`round4_h012_global_falsification.py`.  Therefore a literal `Delta j=1` rule
at every transition is false.  This does not disprove an amortized
`j*(l)<=l+O(1)` theorem: isolated `Delta j=2` steps could be absorbed by a
larger constant or offset by plateau steps.  No persistence theorem for good
witnesses was obtained, so the finite positive result is not yet a proof
sketch of that asymptotic bound.

## H-011: exact boundary witness maps and a sharply reduced state

For every admissible `j`-tuple `A`, the two boundary-safe injections

```text
I_2(A) = (a_0+1,...,a_{j-1}+1,0),
I_4(A) = (a_0+2,...,a_{j-1}+2,0)
```

satisfy `F(I_2(A))=2F(A)+3^j` and `F(I_4(A))=4F(A)+3^j`.  Hence, modulo
`3^m` when `j>=m`,

```text
2 S(m,j) union 4 S(m,j) subseteq S(m,j+1).
```

The visible-prefix extension criterion proves that the reverse inclusion can
fail only in the single doubly saturated corner

```text
a_0=2j+1 and a_{m-1}=j-m+1.
```

Exact computation at every elementary step used by the real transitions
through `l=11` shows the stronger corner containment
`C(m,j) subseteq 4 S(m,j)`, with one small exception at `(m,j)=(4,4)`, residue
38.  Consequently the support equality holds at every tested real transition
from `l=3` through `l=11`; the composed `l=2` transition misses only residue
76.  This is now one precise missing lemma, not an arbitrary support identity:
prove the corner containment uniformly.

The maps also give an explicit witness explanation of defect repair.  If the
old hole is `x` and the budget increment is `delta`, all three lifts of
`2^(-delta)x` already occur at the old budget in every tested case; iterating
`I_2` maps those three witnesses bijectively to the three children of `x`.
This proves the previously observed 49 repairs at `l=2..7` witness by witness
and extends with zero failures through `l=11`: 191 defects and all 573 of their
children.

They also give an unconditional holdout-chain theorem.  If `H(l,j)` is the
unit complement of `S(l,j)`, then

```text
H(l,j+1) subseteq 2 H(l,j) intersect 4 H(l,j).
```

After `t` budget steps, a surviving hole therefore forces `t+1` consecutive
powers-of-2 translates inside `H(l,j)`.  If `R(l,j)` is the longest such
doubling chain, then

```text
j*(l) <= j + R(l,j) <= j + |H(l,j)|.
```

This is a proved finite covering certificate.  A separate exact checker was
rerun here for every budget at `l=5..14`: zero inclusion failures, and the
bound is exactly tight at every tested `j>=l+1`.  The observed
`R(l,l+1)` is only 3 or 4 in that range, but boundedness in `l` is wholly
unproved.  Proving it would give `j*(l)<=l+O(1)`; at present this is a sharper
reformulation of that target, not the desired asymptotic theorem.

For exact mask evolution, multiplication by `mu in {2,4}` acts on the next
digit by

```text
a -> floor(mu*r/3^n) + mu*a (mod 3).
```

Thus the natural exact state is the two predecessor masks at `x/2,x/4` plus
their carries, at most `(8*2)*(8*3)=384` types; only 101 occur across the
tested one-budget transitions.  A bare mask is insufficient, and even one
mask plus its carry is insufficient: the checker contains explicit pairs with
the same reduced state and different next masks.  What remains unproved is
the uniform corner containment (and, equivalently for the repair statement,
why every scaled defect predecessor is full-mask).

The corner has a particularly sharp slack interpretation.  After division by
4 its formal old prefix is
`(2j-1,a_1-2,...,a_{m-1}-2)`: every old boundary condition holds except that
the last visible exponent is exactly one below the extendability threshold.
Thus the missing reverse inclusion is a one-unit tail-slack repair lemma, not
a generic collision problem.  The exceptional first step has `j=m=4`, where
that formal last exponent is `-1`.  A proof still needs bounded carry/gap data
showing that the one-unit deficiency can always be repaired.

Reproduce with
`experiments/E-007-frobenius-mod3-valuation/h011_round4_boundary_state.py`.

## H-013: exact extension and bounded-depth recurrence

The exact holdout sets at budget `j*(l)-1` have sizes 430 at `l=19` and 183 at
`l=20`.  The apparent 4-family and 13-family are two sixth-digit lifts of one
depth-5 cylinder because `13=4^4-3^5`.  Indexed by budget `b=j*(l)-1`, the
dominant classes are

```text
A_b=4^(b-13) mod 3^6,
B_b=A_b-3^5 mod 3^6,
```

and therefore coincide modulo `3^5`.  For `l=17..20`, the complete support of
the holdouts modulo 243 is exactly `4^(b_l-19) S`, where

```text
S={19,28,46,55,73,100,109,127,181,190,208,235}.
```

This is a real four-level bounded-depth recurrence.  The full exact recurrence
is false: only `359/1110, 223/770, 106/430, 29/183` next-level holdouts are
descendants of `4 H_l` over transitions `16->17,...,19->20`.

The two `(10,14)` H-012 holes are exactly `H_10`; both are `4 mod 3^6`.  Thus
H-012's first strict-induction failure is the first small instance of the
H-013 obstruction cylinder, not unrelated noise.

Full tables, validation details, and reproduction commands are in
`notes/H-013.md`; the extractor is
`experiments/E-001-jstar-fast/src/bin/h013_holdouts.rs`.
