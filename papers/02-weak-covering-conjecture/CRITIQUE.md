# CRITIQUE: papers/02-weak-covering-conjecture

PDF-only blind critique loop, Codex (`gpt-5.6-sol`) + Fable, fresh context each round, per Rule
8/15. Researcher's explicit request, 2026-08-09, same protocol as papers/01-wirsching-conjecture3.
Up to 5 rounds; iterate until a round returns no further real findings from either reviewer. Full
findings text preserved below by round; this table is kept current as the producer resolves each
entry.

## Status table

| ID | Round | Summary | Severity | Status |
|----|-------|---------|----------|--------|
| C-01 | 1 | Introduction states WCC's premise as `|R_{j-1,j} mod 3^l| >= K(l)*3^l`, using the *reduced* count against the *already-bounded* codomain size, making the premise vacuous/impossible; CLAUDE.md's own Section 1 states the real conjecture uses the *unreduced* `|R_{j-1,j}|` | critical | fixed |
| C-02 | 1 | Theorem 2 / Corollary 3 (headline bound): no actual proof given, only a table and a solver assertion; the game's transition `T_0` can map a unit state to `0` (not a unit), so the arena isn't even shown to be closed | critical | fixed: corrected game definition (added the "safe" closure filter from the real E-003 code, which the paper's prose had omitted), full proof via the potential/telescoping argument (also recovered from notes/H-003.md round 21), and the correspondence to the covering problem stated honestly as computationally verified for l=1..6, not claimed as a from-scratch symbolic derivation |
| C-03 | 1 | Proposition 11 ("no bounded Delta d"): the cited evidence (violations up to Delta d=3 and edit-distance 7 at two transitions) only disproves Delta d=1, not the existence of any bound | critical | fixed: downgraded to Empirical Result, claim narrowed to falsifying the cost-1 rule specifically |
| C-04 | 1 | Proposition 16 ("H-014 equivalence"): only sufficiency is proven; the "necessity" step reads the bootstrap inequality in the wrong direction (a lower bound on maxrun, not an upper bound); notes/H-003.md's own Round-5 "final audit" already caught and corrected this exact error, but the correction never reached HYPOTHESES.md or the paper | critical | fixed in the paper (Proposition 16 restated as sufficiency-only) and in HYPOTHESES.md's H-014 row (Rule 8c correction added, dated, with an explicit note that this is the second, independent catch of the same error) |
| C-05 | 1 | Theorem 15 / Section 7 discussion: paper claims `H(l,J-1)` occupies class `4^J` at every checked level; independently re-verified (3 implementations: mine, Fable's, Codex's, l=3..9) that it actually occupies `4^(J+1)`, the reverse; Theorem 15's own subset statement is still correct, only the "which class" discussion and Section 8's open-question framing are backwards | critical | fixed: downgraded to Empirical Result with the corrected class and an explicit note about the earlier reversal; Section 8's open-question framing swapped to match |
| C-06 | 1 | Corollary 8 (chain contraction) is false as printed: verified by hand (l=2, x=7) that `x in H(l,j+1)` does NOT imply `x, 2x in H(l,j)`; the real relation runs backward, `x/4, x/2 in H(l,j)`, shifting the whole chain down by one factor of 2 | major | fixed: restated with the corrected chain (length t+1, base shifted to x/4), proof rewritten, Corollary 9's proof adjusted to use the corrected direction |
| C-07 | 1 | Theorems 12/13/15 (Section 7) are asserted with only an informal paragraph, not a proof; the paragraph's own central claim ("coverage depends on (l,j) only through W=j+l-1") is false as stated (falsified by (l,j)=(2,4) vs (3,3), same W=5, different coverage) | major | fixed: replaced with the correct `U(l,W)` formalism carrying the `2^{j-l}` scaling factor (verified computationally, l=2..5), which resolves the (2,4)-vs-(3,3) counterexample; Theorem 12 given a full, independently-derived proof from this formalism, verified by hand and by computation; Theorems 13/15 downgraded to Empirical Results since their full derivations were not reconstructed here |
| C-08 | 1 | Corollary 14 (x4-only inheritance) uses Theorem 7 across two different moduli (level l+1 vs level l) without ever defining the cross-level reduction it depends on | major | fixed: downgraded to Empirical Result, with an explicit statement that no proof is currently in hand for the cross-level relation |
| C-09 | 1 | Proposition 6: the stated limit `S(3^{l-1})/C(2m,m) -> 1/sqrt(3)` is a real number, but the actual limit is complex (`-1/2 - i*sqrt(3)/6`); only the magnitude is `1/sqrt(3)`. Also the stated hypothesis "as l/m grows" is unused; the limit depends only on `m -> infinity` | major | fixed: added `|.|`, corrected the limiting regime to `m -> infinity` for fixed `l`, proof rewritten with the exact complex value and its derivation (geometric limiting gap distribution) |
| C-10 | 1 | Repository is empty; every "exact"/"verified" numeric claim in the paper (Table 1 l=21-23, rho_k table, Fourier statistics, holdout counts) is currently unauditable by a reader | major | open (Rule 12); Section 9's text was already corrected in an earlier pass to not overclaim; actual population of the repo is still pending, tracked separately |
| C-11 | 1 | Abstract overclaims relative to the body: "proven" bound (no proof given, see C-02), "cannot work" (only one method ruled out, see C-14), "explicit witness-level counterexample" (no witness printed) | major | fixed: abstract rewritten to match the corrected body claim by claim (Rule 8b pass) |
| C-12 | 1 | Section 5's impossibility claims overstated: the `o(T)` vs `o(T/3^l)` rate needed isn't stated near eq. (3); Prop 5's `beta` is undefined; the base-3/base-2 approximation-rate discussion oversells what one computation at l=18 shows; "invisible to any method" is an unsupported universal claim | major | fixed: rate corrected near eq. (3), undefined `beta` dropped from Prop 5's statement, the transcendence-theory "signature" claim removed (kept only the accurate dyadic-clustering observation and the Tao connection), the universal claim scoped down to what the phase-randomization experiment actually shows |
| C-13 | 1 | Proposition 1: cardinality argument omits the injectivity step (why distinct tuples give distinct sums); the asymptotic `~` is inverted into an inequality without a rigorous bound | moderate | fixed: injectivity argument added (2-adic valuation), asymptotic inversion replaced with the explicit bound `C(2n,n)<=4^n/sqrt(3n+1)` combined with the already-proven `j=O(l)` from Corollary 3 |
| C-14 | 1 | "Durfee depth" (Proposition 11) used without definition anywhere in the paper | moderate | fixed: definition added inline before the Empirical Result that uses it |
| C-15 | 1 | Binomial plateau test cites a probability without stating the null model it comes from | moderate | fixed: null model stated explicitly (previous paper's reported 3.9/19 plateau expectation) |
| C-16 | 1 | Remark 4's "rho_k -> 0.78-0.79" extrapolation: Codex's own OLS refit of Table 3 gives ~0.88-0.91, not 0.78-0.79 | moderate | fixed: independently reproduced the OLS fit myself (0.83-0.90 depending on range, including with the new k=14 point), could not reproduce 0.78-0.79 by any method; replaced with the honest, reproducible figure (~0.876, k=10..14) |
| C-17 | 1 | Rule 5c violations: banned vocabulary ("genuine/genuinely" x5, "honestly" x1), antithesis budget blown (~13 "not X"/"rather than" constructions vs budget of 2), several meta-honesty/process-narration sentences (self-audited verification counts, references to an "earlier internal draft", self-correction narration) | minor | fixed: banned vocabulary is now zero occurrences (confirmed by grep); antithesis constructions cut from ~14 to 2; all meta-honesty/process-narration sentences removed as part of the same content rewrites |
| C-18 | 1 | Codex found no error in the bare bibliographic metadata (author/title/venue/year for all 4 references) but flags each citation as *used* beyond what it supports (Ehrenfeucht-Mycielski gives positional determinacy, not the paper's uncited reduction/state-independence argument; Tao's post concerns a different modulus family) | minor | fixed as a side effect of C-02's rewrite (the reduction argument is now given explicitly, not left implicit under the citation) and C-12's rewrite (Tao's post now cited for what it actually supports) |
| — | 1 | rho_14 = 9/8 = 1.125 (better than the paper's headline rho_13 = 119/104) is already computed and self-certified in the project's own records (`experiments/E-003-mpg-cylinder/certificate_k14.json`, confirmed 2026-08-01) but never made it into the paper; the paper is understating its own best result | — | fixed: Table 3, Corollary 3, and every other reference to the headline bound updated to k=14, rho_14=9/8=1.125 |
| C-19 | 2 | Theorem 2 as restructured after Round 1 claimed "for every k>=1"; false at k=1, where a direct counterexample shows no unit state has any safe move at all (the adversary's 3 digit choices span all residues mod 3, including 0) | critical | fixed: theorem restricted to the specific k=3,...,14 for which a certified policy is actually exhibited in Table 3; k=1 is simply not claimed |
| C-20 | 2 | The game's action set (move cost d>=0) is a priori unbounded, so "finite mean-payoff game" was asserted, not established; Ehrenfeucht-Mycielski's theorem needs a finite graph to apply | critical | fixed: added the periodicity/domination argument (2 is a primitive root mod 3^{k+1}, order 2*3^k, so successor states repeat with that period in d and every non-minimal representative is cost-dominated), making the action set genuinely finite by construction |
| C-21 | 2 | Theorem 2's proof leaned on Ehrenfeucht-Mycielski's general existence theorem for rho_k, h, and the optimal policy, which also implicitly assumes rho_k is a single, state-independent value; none of this is actually needed or established for the specific bound used | critical | fixed: proof rewritten to be certificate-based -- for each k=3,...,14 the specific policy, potential, and rho_k are exhibited and checked directly (a finite fact per k), with E-M cited only as motivating context, not as a proof step |
| C-22 | 2 | Empirical Result (soundness)'s second sentence ("the full-precision game's optimal cost equals the least budget covering z") claims an equivalence; only the one-directional "soundness" (play constructs a witness) is actually verified, not the converse "completeness" direction | major | fixed: the equivalence sentence dropped; the full-precision (no-adversary) construction and the window-k relaxation are now stated as two separate objects with an explicit one-sentence bridge, instead of being conflated |
| C-23 | 2 | Equation (4)/(5) (the U(l,W) scaling identity) was stated as "verified computationally" only, yet used as a premise in Theorem 12's (last-holdout parity) proof | critical | fixed: given a full, elementary proof (new Lemma 13: top-l-exponent truncation, extendability iff b_{l-1}>=j-l, shift by j-l) -- upgrades the identity from computationally verified to proven, and with it Theorem 12's foundation |
| C-24 | 2 | Theorem 12 (last-holdout parity) implicitly needs j*(l)>=l+1 for equation (5) to apply at j=j*(l)-1; this is never stated, and fails at l=1 (j*(1)=1) | major | fixed: hypothesis j*(l)>=l+1 made explicit in the theorem statement, with the l=1 failure and the eventual-failure-under-the-conjectured-rate case both noted directly in the statement |
| C-25 | 2 | Proposition 1's injectivity argument subtracts just `2^{a_{j-1}}` to recover the remaining terms, but the actual contributing term is `2^{a_{j-1}}*3^{j-1}`; Codex supplied a concrete counterexample (j=2, exponents {2,0}, V=7) showing the stated subtraction gives the wrong residual valuation | major | fixed: proof corrected to subtract the full term `2^{a_{j-1}}*3^{j-1}` |
| C-26 | 2 | Empirical Result ("$\times4$-only inheritance"): the stated congruence `x == 4*pi_l(x) mod 3^{l+1}` is algebraically impossible whenever `pi_l(x)` is a unit and l>=2 (reduces to `3*pi_l(x) == 0 mod 3^l`); independently checked exhaustively at l=2,...,6 that the antecedent (`pi_l(x)` lying in `H(l,j*(l)-1)`) is never even satisfied, so the claim as printed is vacuous | critical | fixed: withdrawn. Replaced with an honest derivation of the impossibility/vacuousness, both algebraic and via direct enumeration; no cross-level relation between `H(l+1,.)` and `H(l,.)` is claimed by this paper |
| C-27 | 2 | Empirical Result (bootstrap exactness)'s quantifier range "at every (l,j) with j>=l+1" is literally false for j>j*(l), where H(l,j)=empty but the claimed equality would need maxrun(empty)=j*(l)-j, not 0 | major | fixed: range corrected to `l+1<=j<=j*(l)`, with an explicit note about why the equality fails past j*(l) |
| C-28 | 2 | `maxrun(H)` (longest doubling chain) and `maxrun(empty)` were never formally defined (distinctness of chain elements, empty-set convention) | moderate | fixed: definition given explicitly at first use (Corollary 10) |
| C-29 | 2 | Undefined/ambiguous terms: "primitive coefficients" (Section 5.2) used without saying what "primitive" means; "minimum edit distance" (Empirical Result, cost-1 repair) used without defining the metric | moderate | fixed: "primitive" spelled out as `t` coprime to 3; edit distance defined as the minimum number of exponents that differ between a child's and its matched parent's cheapest witness |
| C-30 | 2 | Empirical Result (near-extinction bijection)'s forward reference to "Section 8" for the one-step width recursion is wrong; the recursion is displayed within Section 7 itself, a few paragraphs later | minor | fixed: replaced the wrong section pointer with "stated below" |
| C-31 | 2 | Theorem 7 (doubling inclusion)'s proof said the new smallest exponent 0 is "prepended," which is directionally confusing (0 is the smallest exponent, not the first/top one) | minor | fixed: reworded to "adjoining 0 as the new smallest exponent" |
| C-32 | 2 | Section 6's opening asserts "$j>=j^*(l)$ exactly when $H(l,j)=\emptyset$" for $j\ge l$ without justifying that emptiness persists once reached | minor | fixed: one-line derivation added from Theorem 7 itself (H(l,j)=empty implies H(l,j+1) subseteq 2*empty cap 4*empty = empty) |
| C-33 | 2 | Residual Rule 5c artifacts flagged by Codex's prose pass (hedge-then-affirm phrasing, meta-commentary about verification) | minor | fixed as a side effect of the C-19..C-32 rewrites; re-confirmed by grep afterward: 0 banned-vocabulary hits, 0 em-dashes, antithesis constructions within budget |
| — | 2 | Fable's Round 2 pass (run in parallel with Codex's): Theorem 7's proof had a garbled closing sentence from the Round 1 rewrite; Proposition 5 stated an unspecified constant and error term; the four e(l) growth models lacked explicit functional forms in text; the "safe" move definition left the modulus m implicit; Tao's two quoted sentences were not re-verified against the primary source; Empirical Result (mod-9)'s process-narration parenthetical (referencing the earlier reversal) survived Round 1's Rule 5c pass | major/moderate | fixed, all six, before Codex's report was read (Theorem 7 proof-ending rewritten; Prop 5 given an explicit constant C and O(log l) error term; growth models given explicit functional forms; `m:=3^k` pinned down explicitly; both Tao quotes verified via WebFetch against the primary source, confirmed exact; the parenthetical removed) |

## Full findings

### Round 1 (Codex on `gpt-5.6-sol` + Fable, 2026-08-09)

Both reviewers read only the compiled `main.pdf`, no other project file, per protocol. Full reports
preserved in this session's transcript (Fable's agent report, and Codex's `codex exec` log). Key
overlaps: both independently found Proposition 16's overclaim (C-04) and the Theorem 15 class
reversal (C-05, both computed the exact wrong-vs-right classes and agreed exactly with each other
and with an independent third check by the producer). Codex went further into structural gaps the
paper's proofs don't actually close (C-01, C-02, C-03, C-06, C-07, C-08) that Fable's pass did not
surface; Fable went further into the Rule 5c prose-tell audit and Proposition 6's complex-vs-real
error, which Codex also independently found via direct computation.

Two items were checked and found to be correct as printed, i.e. false alarms avoided: Codex's
initial scratch exploration of the binomial-test p-value used a different (unstated) null than the
paper's actual one; the paper's own reported 0.0426/0.22 reproduce exactly under the null the
project's own E-002 script actually uses (previous paper's 3.9/19 plateau expectation). The general
point (C-15, that the null itself isn't stated in the paper) still stands and is being fixed.

Given the volume and severity of confirmed findings, this round alone requires substantial rewriting
of Sections 1, 4, 6, and 7, not incremental copyedits. Convergence will take more than the originally
estimated 2-3 rounds.

### Round 1 fixes (producer pass, 2026-08-09)

Every C-01 through C-18 item above was independently re-verified before fixing (Rule 8c), not taken
on either reviewer's word: the WCC statement error was confirmed by re-reading main.tex directly;
the Theorem 15 class reversal was confirmed via a from-scratch computation matching Fable's and
Codex's independent computations exactly (l=3..9); the Corollary 8 counterexample was reproduced by
hand (l=2, x=7); the Proposition 6 complex-limit derivation was redone from scratch and matches both
reviewers; the Proposition 16 error was traced to its origin and found to be a *second* occurrence of
a mistake notes/H-003.md's own Round-5 audit had already caught once and that had not propagated to
HYPOTHESES.md or the paper. The MPG proof gap (C-02) required the most work: the actual, closed game
construction was recovered from the working code in experiments/E-003-mpg-cylinder/ (the paper's
prose had silently dropped the "safe" closure filter present in the real implementation), and the
finite-horizon bound was re-derived from the potential/telescoping argument already present in
notes/H-003.md's round-21 section, rather than invented fresh. Sections 1, 3, 4, 5, 6, and 7 were
substantially rewritten; Theorem 12 (last-holdout parity) now carries a complete, independently
verified proof; Theorems 13/15 and Corollary 14 were downgraded to honestly-labeled Empirical
Results rather than left as theorems without a reconstructed proof. A side discovery during the
fix pass (not a critique finding): rho_14=9/8=1.125, already computed and self-certified in this
project's own records since 2026-08-01, is better than the paper's stated headline bound and had
never been incorporated; the paper now states the correct, better bound throughout. Recompiled
clean (9 pages, 0 errors, 0 warnings, 0 em-dashes) and visually re-verified page by page.

HYPOTHESES.md's H-014 row was corrected in the same pass (the false equivalence claim retracted
with a dated Rule 8c note, per protocol for a finding that traces back to already-recorded material).

### Round 2 (Codex on `gpt-5.6-sol` + Fable, 2026-08-09)

Both reviewers again read only the compiled `main.pdf`, fresh context, no memory of Round 1. Fable's
report landed first and was fixed immediately; Codex's report, the longer of the two, arrived while
some of those Fable-driven fixes and one producer-initiated restructuring (making Theorem 2
conditional on a new Empirical Result) were already being written into the document. This is a
process bug, not a reviewer error: a reviewer mid-run can end up reading an intermediate state of the
PDF rather than either the true "before" or the true "after." Two of Codex's items turned out to
already be resolved by the time its report was read (the Corollary-3 forward-reference in
Proposition 1's proof, and part of the "relevant modulus" phrasing in the game definition); these are
not separately listed above since no further action was needed. Starting with Round 3, the PDF is
frozen for the whole duration of a review round; all edits happen between rounds, never during.

Despite that overlap, Round 2 caught something substantially more serious than a copyedit: Round 1's
fix to Theorem 2 (the headline mean-payoff-game bound) had replaced an unproven table-and-assertion
with a proof that leaned on Ehrenfeucht-Mycielski's general existence theorem, which does not
actually apply to the game as defined, because the game's own construction was not yet shown to be
finite, and the theorem's quantifier ("for every k>=1") was directly false at k=1 by an explicit
counterexample. Two independent reviewers, in two different rounds, found two different kinds of
gaps in the same theorem's proof: Round 1 found the theorem had no real proof; Round 2 found the
Round-1 proof's own foundational premises did not hold. This is exactly what running the loop for
multiple rounds is supposed to catch, and it did. The fix this round is certificate-based rather than
existence-theorem-based: for each of the twelve specific k in Table 3, the exact policy, potential,
and value are exhibited and checked directly as a finite fact, so neither the k=1 counterexample nor
the general finiteness question is a burden Theorem 2 itself has to carry.

Codex's report also found a genuine bug in this project's own prior investigation, not just in the
paper's prose: the "$\times4$-only inheritance" empirical claim (carried into the paper from
`notes/H-013.md`) is algebraically impossible as stated whenever the reduced holdout is a unit at
level $l\ge2$, and, checked directly against the exact holdout tables at $l=2,\dots,6$, its
antecedent is never even satisfied. Rather than attempt a hasty reformulation, this was verified
independently (both the algebra and a fresh from-scratch enumeration, matching Codex's finding
exactly) and withdrawn outright, per Rule 8c and per the explicit guidance to withdraw rather than
guess when a finding is confirmed but the correct replacement claim is not in hand.

Every item was independently re-verified before being fixed: the k=1 counterexample by hand; the
order-of-2-mod-$3^{k+1}$ fact (needed for the finite-action-set argument) by direct computation,
$k=0,\dots,5$; the Proposition 1 subtraction bug against Codex's own supplied example; the width
scaling identity's proof by re-deriving it from scratch (matching Codex's own proof sketch); the
Empirical Result 10 quantifier bug by re-reading the corollary it restates; and the $\times4$-only
withdrawal by both an independent algebraic check and a fresh $l=2,\dots,6$ computation.
Recompiled clean (10 pages, 0 errors, 0 warnings, 0 em-dashes) and visually re-verified page by page.
