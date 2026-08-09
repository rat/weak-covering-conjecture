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
