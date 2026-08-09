# GAP A round 5: theoretical attack on H-014 (draft)

Date: 2026-08-09.

Scope: this is a separate proof draft for the final GAP A round.  It does not
edit the hypothesis registry or the round summary.  The target was

\[
   \operatorname{maxrun} H(l,l+1)=O(1).
\]

No uniform constant bound, and no counterexample family, was obtained.  The
main positive result is an exact restricted-width reformulation which makes
the previously informal "full-width witness" obstruction precise.  Two
additional elementary lemmas give an exact description of lift defects and a
strong necessary bottom-boundary condition for any defect.  Together they
isolate a concrete missing lemma rather than merely restating H-014.

## 1. Why this route was selected

The computation is being extended independently in this round.  For the
theoretical leg, the most direct route is to invert multiplication by powers
of 2 at fixed budget.  This is the converse direction which failed in round
4 only at witnesses touching both sides of the exponent window.  It also
attacks maxrun itself, whereas the mod-9 law concerns only the last nonempty
holdout set and does not currently propagate back to budget `l+1`.

Write

\[
 \mathcal R_{l,j}:=R_{l-1,j}\pmod {3^l}
 =\left\{\sum_{i=0}^{l-1}3^i2^{a_i}:
 0\leq a_{l-1}<\cdots<a_0\leq l+j-1\right\}.
\]

For `j >= l`, deleting the terms divisible by `3^l` and then translating all
remaining exponents gives the standard exact identity

\[
 R_{j-1,j}=2^{j-l}\mathcal R_{l,j}\pmod {3^l}.                 \tag{1}
\]

Indeed, the first `l` entries of a `j`-tuple have last exponent at least
`j-l`; subtracting `j-l` gives the displayed `l`-tuple.  Conversely, shift
such an `l`-tuple by `j-l` and append `j-l-1,\ldots,0`.  Thus multiplication
by `2^{j-l}` is a bijection on units and only translates the discrete-log
picture.  In particular maxrun for `H(l,l+1)` equals maxrun for the complement
of

\[
 \mathcal R_{l,l+1}
 =\left\{\sum_{i=0}^{l-1}3^i2^{a_i}:0\leq a_{l-1}<\cdots<a_0\leq2l\right\}.
                                                                  \tag{2}
\]

## 2. Exact restricted-width reformulation of H-014

For `l >= 2` and `C >= 0`, define

\[
 \mathcal W_{l,C}:=\left\{\sum_{i=0}^{l-1}3^i2^{b_i}:
 0\leq b_{l-1}<\cdots<b_0\leq2l+C,\quad b_0-b_{l-1}\leq2l\right\}
 \pmod {3^l}.                                                    \tag{3}
\]

### Theorem 2.1 (window-width equivalence)

For every `l` and `C`,

\[
 \operatorname{maxrun}H(l,l+1)\leq C
 \quad\Longleftrightarrow\quad
 \mathcal W_{l,C}=(\mathbb Z/3^l\mathbb Z)^\times.              \tag{4}
\]

Consequently H-014 is exactly the assertion that a fixed `C` makes the
restricted-width family (3) cover at every level.

**Proof.**  Let `S=\mathcal R_{l,l+1}` and let `H` be its unit complement.  A
block `x,2x,\ldots,2^C x` is not wholly contained in `H` exactly when

\[
 x\in\bigcup_{r=0}^C2^{-r}S.
\]

Thus maxrun(H) is at most `C` iff this union is every unit.  Multiplication by
`2^C` changes the union to

\[
 \bigcup_{s=0}^C2^sS.                                          \tag{5}
\]

The `s`th set in (5) consists of the tuples whose exponents all lie in the
width-`2l` window `[s,s+2l]`.  A tuple in `[0,2l+C]` lies in one of these
windows iff its span is at most `2l`: if its endpoints are `m <= M`, an
admissible window origin is any integer

\[
 \max(0,M-2l)\leq s\leq\min(C,m),
\]

and this interval is nonempty precisely under the bounds in (3).  Therefore
the union (5) is exactly `W_{l,C}`.  Equation (1) transfers the statement back
to the project's unnormalized `H(l,l+1)`.  This proves (4).  \(\square\)

As an indexing sanity check (not as evidence in place of the proof), direct
enumeration at every `l=2,...,7` and `C=0,...,4` gave exact equality between
the union (5) and (3).

### What "full-width" now means exactly

The unrestricted family with the same outer exponent box is

\[
 \mathcal R_{l,l+C+1}=R_{l-1,l+C+1},\qquad b_0\leq2l+C.
\]

The only tuples removed in `W_{l,C}` are those with
`b_0-b_{l-1} >= 2l+1`.  Hence a proof that
`R_{l-1,l+C+1}` covers is not enough for H-014: one must prove that every
residue has a covering witness which is not full-width.  Conversely, that
single witness-selection statement is sufficient.  This is the exact form of
the obstruction mentioned informally in round 4.

There are two related but distinct boundary notions here.  In the **single
one-budget-step** reverse-inclusion argument of round 4, the only tuple not
pulled back by either elementary inverse is the doubly saturated corner (both
absolute endpoints are hit).  The obstruction in (3) is the **iterated
`C`-shift** version: a tuple is bad when no translate of its whole exponent
set fits back into `[0,2l]`, equivalently when its span is greater than `2l`.
For `C=1` these coincide, because a tuple in `[0,2l+1]` of span `2l+1` must
hit both endpoints.  For `C>1`, width greater than `2l` is a union of several
boundary layers and need not hit both outer endpoints `0` and `2l+C`.

It also shows that H-014 is stronger than the numerical conclusion
`j*(l) <= l+C+1`.  The latter permits a residue to be covered only by
full-width witnesses; (4) does not.

The excluded witnesses are not a negligible boundary family.  The total
number of `l`-tuples in the unrestricted box is
`binom(2l+C+1,l)`.  The number excluded from `W_{l,C}` is exactly

\[
 E_{l,C}=\sum_{h=1}^C(C+1-h)\binom{2l+h-1}{l-2}.                \tag{6}
\]

To see this, put `b_0-b_{l-1}=2l+h`; there are `C+1-h` choices of
the two endpoints and `binom(2l+h-1,l-2)` choices of the interior entries.
For fixed `C`, division by the total and elementary factorial cancellation
give

\[
 \frac{E_{l,C}}{\binom{2l+C+1}{l}}
 \longrightarrow
 \sum_{h=1}^C\frac{C+1-h}{2^{C-h+2}}
 =1-\frac{C+2}{2^{C+1}}.                                      \tag{7}
\]

For the observed candidate `C=4`, the full-width tuples approach `13/16` of
the unrestricted witness domain.  This count says nothing by itself about
the image modulo `3^l`, but it rules out treating full-width witnesses as an
asymptotically sparse error term.

## 3. Exact lift-mask formula from prefix witnesses

The next lemma describes precisely how a level-`l` defect can occur in (2).
For a decreasing `(l-1)`-tuple

\[
 A=(a_0>\cdots>a_{l-2}),\qquad 0\leq a_{l-2},\quad a_0\leq2l,
\]

put

\[
 P(A)=\sum_{i=0}^{l-2}3^i2^{a_i}.
\]

Fix a parent residue `p mod 3^(l-1)` and write

\[
 P(A)\equiv p+\delta(A)3^{l-1}\pmod {3^l},\qquad
 \delta(A)\in\mathbb Z/3\mathbb Z                              \tag{8}
\]

for every prefix witness `A` of `p`.

### Lemma 3.1 (exact child mask)

The child digits of `p` covered by (2) are exactly

\[
 \bigcup_{A:a_{l-2}=1}\{\delta(A)+1\}
 \quad\cup\quad
 \bigcup_{A:a_{l-2}\geq2}
       \bigl((\mathbb Z/3\mathbb Z)\setminus\{\delta(A)\}\bigr).       \tag{9}
\]

Prefixes with last exponent zero do not extend.

**Proof.**  Every full `l`-tuple is uniquely a prefix `A` followed by an
exponent `b<a_{l-2}`.  Its new term is `3^(l-1)2^b`, so its child digit is
`delta(A)+2^b mod 3`.  If `a_(l-2)=1`, only `b=0` is available.  If
`a_(l-2)>=2`, exponents `b=0,1` are both available and `2^b mod 3` runs
through `1,2`; further choices add no new digit.  This gives (9), and every
tuple has been included.  \(\square\)

Two useful consequences are immediate.

1. If one parent fiber contains two prefixes of minimum at least 2 with
   different `delta`, all three children are covered.
2. If a child `p+e3^(l-1)` is a hole, every prefix of minimum at least 2 has
   `delta=e`.  Thus a defect forces exact one-digit rigidity across the entire
   extendable prefix fiber, not merely a low witness count.

There is also a chain version.  Suppose `y,2y,4y` are all holes and let `A`
be any prefix witness of `y mod 3^(l-1)`.  If

\[
 a_0+\max(0,2-a_{l-2})\leq2l,                                 \tag{10}
\]

then

\[
 P(A)\equiv y\pmod {3^l}.                                     \tag{11}
\]

Indeed, choose `k=max(0,2-a_(l-2))`, so `k in {0,1,2}`.  Shifting all
exponents of `A` by `k` gives a valid prefix of `2^k y`, with minimum at
least 2 by (10).  Since that member of the three-chain is a hole, (9) forces
`2^kP(A)=2^ky mod 3^l`; cancellation of the unit `2^k` gives (11).

This is a rigorous necessary condition for a three-chain.  It does not yet
bound chains: fibers satisfying this rigidity do occur in the data.

## 4. Bottom-slack repair and what a five-chain would force

The round-31 revise-then-append calculation gives a particularly sharp
criterion here.

### Lemma 4.1 (minimum-4 prefix repairs every child)

If a parent `p mod 3^(l-1)` has a prefix witness
`A=(a_0>...>a_(l-2))` with `a_0<=2l` and `a_(l-2)>=4`, then all three
children of `p` modulo `3^l` lie in (2).

**Proof.**  Put `a=a_(l-2)-2`, so `a>=2`, and let
`c=a_(l-3)` (the case `l=2` can be checked separately).  Replacing the last
prefix exponent `a+2` by `a` does not change its value modulo `3^(l-1)`,
because

\[
 3^{l-2}(2^{a+2}-2^a)=3^{l-1}2^a.
\]

Also `c>a+2`.  For `d,b in {0,1}`, use the full tuple

\[
 (a_0,\ldots,a_{l-3},a+2d,b).
\]

It is strictly decreasing, stays under the same top bound, and relative to
the revised prefix its new high digit is

\[
 2^a d+2^b\pmod3,                                              \tag{12}
\]

since `4^d=1+3d mod 9`.  As `d,b` vary over `{0,1}`, (12) takes all three
values modulo 3 (whether `2^a` is 1 or 2).  Hence all children are covered.
\(\square\)

This argument was also exhaustively sanity-checked for every eligible prefix
at `l=3,...,8`; the four constructed tuples gave digit set `{0,1,2}` in every
case.  The proof itself is exact and does not depend on that check.

### Corollary 4.2 (necessary condition for a five-chain)

If

\[
 y,2y,4y,8y,16y\in H(l,l+1)
\]

in normalized coordinates, then `y mod 3^(l-1)` is not represented by any
`(l-1)`-tuple with maximum exponent at most `2l-4`.  Equivalently,

\[
 y\bmod3^{l-1}\notin R_{l-2,l-2}.                              \tag{13}
\]

**Proof.**  If such a prefix existed, shift all its exponents by 4.  Its
maximum would be at most `2l`, its minimum would be at least 4, and it would
witness the parent of `16y`.  Lemma 4.1 would cover all of that parent's
children, including `16y`, a contradiction.  The exponent cap in
`R_{l-2,l-2}` is `(l-2)+(l-2)=2l-4`.  \(\square\)

Sliding the five-term window also shows that a run of length `L` in
`H(l,l+1)` projects to a run of length `L-4` in the unit complement of
`R_{l-2,l-2}` modulo `3^(l-1)`.

This is a genuine descent statement, but it does not close H-014.  The lower
family in (13) is below its covering threshold (the project's verified values
have `j*(l-1)>l-2`), so its complement is large.  A proof still needs an
arithmetic reason that those lower holes cannot line up with the rigid
one-digit fibers in Lemma 3.1 through repeated doubling.

## 5. The precise missing lemma

The most useful exact closure target exposed by this attempt is either of the
following equivalent-strength forms.

* **Restricted-width coverage:** prove that some fixed `C` makes
  `W_{l,C}` cover every unit for every `l` (Theorem 2.1).
* **Uniform anti-rigidity:** prove that no power-of-two orbit can contain an
  arbitrarily long sequence of child fibers all satisfying the one-digit
  rigidity in Lemma 3.1 together with the bottom-boundary obstruction in
  Lemma 4.1.

The first is the clean global statement; the second identifies the local
mechanism that must be ruled out.  Neither follows from tuple counts, from
the already-proved `119/104` bound, or from ordinary coverage at budget
`l+C+1`, because all three allow a residue to rely only on full-width
witnesses.  Formula (7) shows why simply discarding those witnesses cannot be
justified by a negligible-exception estimate.

## 6. Calibrated verdict

This theoretical pass neither proves nor refutes H-014.  It does prove that
H-014 is a restricted-width witness-selection theorem and gives exact local
certificates which every long chain would have to satisfy.  A constant bound
now looks comparable in difficulty to proving `l+O(1)` coverage **plus** a
non-full-width representative theorem; it is not an automatic corollary of
an `l+O(1)` bound.  The flat computed ceiling remains strong evidence, but a
proof appears to require new control of complete prefix fibers (their three
adic lift digits and endpoint slack), not another manipulation of the two
shift inclusions alone.
