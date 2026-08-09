# GAP A round 5: secondary closure draft

Date: 2026-08-09.  This file is deliberately separate from the hypothesis
registry and the main round-5 summary.

## Setup and an exact fixed-term recurrence

Put

```text
A_l(j) = R_{l-1,j} mod 3^l,
K_l(j) = (Z/3^l Z)^x \ A_l(j).
```

For `j>=l`, the standard reduction gives

```text
H(l,j) = 2^(j-l) K_l(j).
```

Increasing `j` by one merely makes the new largest exponent available.  Splitting
the `l`-subsets according to whether they contain it gives the exact recurrence

```text
A_l(j+1) = A_l(j) union (2^(l+j) + 3 A_(l-1)(j+1))       (mod 3^l).       (1)
```

In particular `K_l(j+1) subset K_l(j)`, and every element removed from `K_l(j)`
at this step is congruent to `2^(l+j) mod 3`.  This is the fixed-term-coordinate
version of the full-width-witness obstruction.

## Two unconditional near-extinction theorems

Let `J=j*(l)` and assume `J>l` (as in every nontrivial level here).  Since
`K_l(J)=empty` but `K_l(J-1)` is nonempty, every member of `K_l(J-1)` is removed
in the last transition.  Applying (1) with new top exponent

```text
N = l+J-1
```

gives

```text
K_l(J-1) subset {r : r == 2^N (mod 3)}.
```

Multiplication by the normalization factor `2^(J-1-l)` proves, without any
empirical assumption,

```text
H(l,J-1) subset {h : h == 1 (mod 3)}.                    (2)
```

This proves the mod-3 half of the observed last-holdout law for every `l`.

There is also an exact equality one step farther back.  At the transition
`J-2 -> J-1`, only normalized residues congruent to `2^(l+J-2) mod 3` can be
newly covered.  The opposite class therefore persists automatically.  Conversely,
(2) says every normalized last holdout lies in precisely that opposite class.
Undoing the normalization yields

```text
H(l,J-1) = 2 * {x in H(l,J-2) : x == 2 (mod 3)}.         (3)
```

Thus the round-4 count equality/bijection was not a coincidence: (3) is a theorem.
No run-length-converse assumption is used.

## Exactly what remains in the mod-9 single-class law

Recurrence (1) also gives an unconditional two-class theorem.  A normalized
last hole has a new full-width representation

```text
r = 2^N + 3q,       q in A_(l-1)(J).
```

Modulo 9, `q` is `2^a mod 3`, where `a` is the next exponent below `N` in that
witness.  According as `a` has the same or opposite parity as `N`,

```text
r == 2^(N+2) or 2^(N+4) (mod 9).
```

Returning to the original coordinates proves

```text
H(l,J-1) mod 9 subset {4^J, 4^(J+1)}.                    (4)
```

The observed single-class law says that only the second class occurs.  Therefore
the entire unexplained content is now the exclusion of `4^J`; it is equivalent
to proving that every last-step full-width witness relevant to a previous hole
has second exponent of parity opposite to its top exponent.

A sharper candidate lemma emerged from the exact data.  At a general budget
`j`, put `N=l+j` (the exponent that becomes available at the next step).  Once
`j-l>=3`, the *whole normalized holdout set*, not merely the holes covered next,
avoids the class `2^(N+2) mod 9`.  Equivalently, in the original coordinates,

```text
all x == 4^(j+1) (mod 9) are covered by R_(j-1,j), for j>=l+3.       (5?)
```

This cylinder-covering statement was checked exactly through `l=15`.  It
implies in particular that the newly covered normalized holes at `j -> j+1`
can occupy only the second of the two a priori classes

```text
2^(N+2), 2^(N+4) (mod 9).
```

The other class really does occur at smaller slack, so the unrestricted
statement is false.  Proving (5?) would imply the
single-class law whenever the last transition is in that range (with the finitely
many smaller-slack levels handled directly).  I did not find a valid witness
transformation proving this lemma: attempts to lower the full-width top exponent
create a carry/collision at the next rank, exactly the previously identified
full-width obstruction.  This is a genuine reduction, not a proof of the mod-9
law.

The class relation can also be viewed dynamically.  If a hypothetical last hole
lay in the first class `2^(N+2)`, the holdout inclusion forces its half to be a
hole one step earlier; (2) forces that half to die at the penultimate transition,
where it lies in that transition's first (same-parity) class.  Hence excluding the
first class among penultimate newly covered holes suffices to exclude it among
last holes.  Again, exact data support this after slack three, but no uniform
repair proof is known.

## The run-length converse is false without the `j>=l+1` restriction

There is a small exact counterexample to the unrestricted claim that a doubling
chain of length `t+1` at budget `j` forces survival to budget `j+t`:

```text
l=6, j=6, q=729,
187, 374, 19, 38, 76
```

is a five-element doubling chain modulo 729 contained in `H(6,6)`, while
`H(6,10)=empty` (`j*(6)=10`).  Thus a 5-chain does not force survival four steps.
Equivalently, `maxrun(H(6,6))=5` but the remaining lifetime is only 4.

This does not falsify the narrower empirical equality for `j>=l+1`; the same
exact computations still give equality in every such tested case.  A useful
one-step partial converse *is* provable from (1): if a normalized holdout set
contains two consecutive powers of 2, one of them is in the mod-3 class that
cannot be newly covered at the next step, so the next holdout set is nonempty.
Longer chains do not iterate into comparably long chains: the automatically
surviving elements are every other member and need not remain adjacent.  This is
why (1) alone does not prove the full empirical equality.

There is a sharper pointwise failure even at `j=l+1`: the reverse of the proved
set inclusion is false.  At `l=7`, `j=8`, and modulus 2187, put `y=1547`.  Then

```text
y/4 = 2027 in H(7,8),
y/2 = 1867 in H(7,8),
2*2027 = 1867,  2*1867 = 1547                 (mod 2187),
```

but `y` is covered at budget 9.  Thus

```text
y in 2H(7,8) intersection 4H(7,8),
y notin H(7,9).
```

Exhaustive enumeration of all `C(18,9)=48620` budget-9 tuples finds exactly two
witnesses for `y`:

```text
(17,12,11,9,5,3,2,1,0)
(17,14,10,6,5,4,2,1,0).
```

Both hit both boundaries (`a_0=17`, `a_8=0`).  This independently confirms that
the obstruction to reversing the exponent-shift maps is exactly the doubly
saturated/full-width witness case.  It decisively falsifies equality in the
one-step holdout inclusion, even in the empirical-tightness range.  It does not
falsify the weaker existential statement `maxrun(H(l,j)) = j*(l)-j`: other holes
can, and here do, survive.

## Reproduction

Run

```bash
python3 experiments/E-009-holdout-chain-bootstrap/round5_secondary_closure.py
```

The checker verifies (2), (3), (4), the observed choice of the second mod-9
class for `l=2..14`, all computed slack-at-least-three cylinder/transition instances in
that range, the explicit `l=6` converse counterexample, and the exhaustive
`l=7,j=8` reverse-inclusion counterexample.  A separate exact run extended the
candidate cylinder and transition checks through `l=15`; they also passed.
