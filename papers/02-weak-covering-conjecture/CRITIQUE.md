# CRITIQUE: papers/02-weak-covering-conjecture

PDF-only blind critique loop, Codex (`gpt-5.6-sol`) + Fable, fresh context each round, per Rule
8/15. Researcher's explicit request, 2026-08-09, same protocol as papers/01-wirsching-conjecture3.
Originally up to 5 rounds; the researcher extended the cap to 10 rounds on 2026-08-09 after Round 5
closed, specifically to test whether the two reviewers converge (a round returning no further real
findings from either). Iterate until convergence or the round-10 cap, whichever comes first. Full
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
| C-10 | 1 | Repository is empty; every "exact"/"verified" numeric claim in the paper (Table 1 l=21-23, rho_k table, Fourier statistics, holdout counts) is currently unauditable by a reader | major | fixed: repository populated between Round 2 and Round 9 (see the dated narrative below), every section has a script and a README; status corrected here since this row had gone stale |
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
| C-34 | 3 | Empirical Result (soundness)'s witnessing claim, `z in R_{J-1,J} mod 3^l`, was FALSE, not just unproven: Codex found a direct counterexample (l=2, z=4, play costs (0,1), J=1, but 4 is not in R_{0,1} mod 9 = {1,2}), confirmed independently by hand and by a from-scratch computation | critical | fixed: replaced with a correctly-derived Lemma (Grounding), proven by induction and independently verified computationally against every legal play for l=1..4 (780/780 pass), showing the play actually witnesses a *twisted* residue `2^{J+l-1} z_0`, not `z_0` itself; the Empirical Result was restated as the (separately verified, l=1..12) equality `j*(l) = max_z0 min-cost(z0)`, and Theorem 3's proof rewritten to use this correctly (min-cost <= specific policy's cost, not the false direct-witnessing claim) |
| C-35 | 3 | The "full-precision game" (k=l, no adversary) was not a coherent construction: "safety is automatic since z is a unit" is circular (staying a unit is exactly what needs guaranteeing), and computing T_d(z) mod 3^l after division by 3 needs z mod 3^{l+1}, not merely z mod 3^l | critical | fixed as part of C-34's rewrite: the full-precision game is now defined with a shrinking modulus (state z_i modulo 3^{l-i} at step i), matching the actual verified implementation (`step_a_grounding.py`), not the earlier informal "no adversary" description |
| C-36 | 3 | A fixed window-k policy cannot literally inspect z mod 3^k when l<k, despite Theorem 3 claiming the bound for all l (window sizes go up to k=14, but the bound is claimed for every l, including l<14) | major | fixed: added an explicit bridging sentence (fix any lift of z to mod 3^k and run the policy on the lift; safety's own guarantee, built for one hidden digit, extends digit-by-digit to every digit beyond position l) |
| C-37 | 3 | Table 3 calls C_k "explicit" but only lists rho_k; Corollary 4's `+O(1)` cannot be checked by a reader without the actual constant, and (9/8)*23=25.875 < 27=j*(23) shows C_14 must be at least 9/8, worth checking against what's actually stored | moderate | fixed: added a C_k row to Table 3 (all twelve values, from the project's own certificate files; C_14=33/2, consistent with the l=23 check) |
| C-38 | 3 | Abstract states Theorem 8's inclusion backwards: "contained in the union of its double and its quadruple," where the theorem proves an *intersection* (`H(l,j+1) subseteq 2H(l,j) cap 4H(l,j)`), and the "double/quadruple at the next" phrasing reverses which budget contains which | critical | fixed: abstract corrected to "contained in both twice and four times the set left uncovered at the previous budget," matching Theorem 8 exactly |
| C-39 | 3 | Abstract states the mod-3 parity theorem unconditionally ("every last-uncovered residue is == 1 mod 3"), omitting Theorem 12's actual hypothesis j*(l)>=l+1 (which the theorem's own statement flags as failing at l=1) | major | fixed: abstract now reads "...whenever j*(l)>=l+1 (every computed level but one)" |
| C-40 | 3 | The "equivalently" step connecting Wirsching's forcing-form conjecture to j*(l)'s growth rate is not established in general: it requires coverage to persist at every larger budget once reached, which is only proven for j>=l (Theorem 8), not below l, where the conjectured rate would eventually put j*(l) | major | fixed: the Introduction's claim rescoped explicitly to the proven range (j>=l), with an honest note that it is not established below l |
| C-41 | 3 | Section 6's opening claimed `j*(l) > l` at every computed level; false at l=1, where j*(1)=1=l | moderate | fixed: corrected to `j*(l) >= l, with equality only at l=1` |
| C-42 | 3 | Corner-redundancy, as actually checked (W>=2l+1), does not bear on Proposition 17's converse: the only known failures are at the boundary width W=2l, which is exactly j=l+1, Proposition 17's own case; the paper's Discussion claimed proving corner-redundancy "would settle" that converse | major | fixed: both the Section 7 paragraph and the Discussion section rescoped -- corner-redundancy at W>=2l+1 would only make the bootstrap tight for j>=l+2, and does not by itself bear on Proposition 17's j=l+1 case |
| C-43 | 3 | Corollary 10 (run-length bootstrap)'s proof was informal and partly circular: it reasoned "as j decreases from j*(l)," implicitly assuming the quantity being proven | moderate | fixed: rewritten as a genuine proof by contradiction (suppose H(l,j+r) is nonempty for r=maxrun(H(l,j)); iterate Corollary 9 r times starting from a length-1 chain, producing a length-(r+1) chain in H(l,j), contradicting maxrun(H(l,j))=r) |
| C-44 | 3 | Section 5.2 (the l=18 exponential-sum computation) never specifies the covering budget j used, whether the quoted L1 norm (5226) is normalized, or what "primitive" means; Section 5.3 (phase-randomization) gives no levels, counts, trial numbers, or actual ratios, making both unreproducible from the paper text alone | major | fixed: both rewritten with the actual parameters and numbers from the project's own verified computations (Section 5.2: j=16 stated explicitly, L1 defined as the normalized sum over t coprime to 3; Section 5.3: the exact l=10..15 holdout counts, the e^{-23} to e^{-100} probability range, and the (l,m)=(14,16) phase-scramble ratio 15.79 vs [5.11,5.24]) |
| C-45 | 3 | The paper never states the precise link between K(l)'s sub-exponentiality and e(l)'s growth rate, so a reader cannot see what is actually at stake in Section 3's model comparison; in particular, the paper's own best-fitting model (slow-linear) would falsify the conjecture outright if it were the true asymptotic, a consequence never mentioned | moderate | fixed: added the explicit identity `K(l) =~ 4^{e(l)}` after e(l)'s definition (so sub-exponential K(l) is equivalent to e(l)=o(l)), and a remark in Section 3 noting the real stakes of the model comparison, honestly hedged (14 correlated points cannot settle the question) |
| C-46 | 3 | Proposition 7 (the 1/sqrt(3) limit) is stated in a fixed-l, m to infinity regime, off the covering-relevant diagonal (m ~ l log_4 3); its "uniform decay is false" conclusion does not by itself say anything about the diagonal a covering argument would use | minor | fixed: added a scoping remark after the proposition stating the regime explicitly and noting it does not cover the diagonal case |
| — | 3 | Both reviewers independently flagged the title's "A Proven Bound" as an overclaim given the bound is conditional on an empirical (not proven) correspondence | minor | fixed: researcher confirmed conditional language, 2026-08-09; title changed to "a conditional bound" |
| C-47 | 4 | Section 5.3's occupancy mean lambda, `|R_{j*(l)-2,j*(l)-1}|/(2*3^(l-1))`, was stated as "ranging 1.0 to 3.7" for l=10..15; both reviewers independently found this wrong by a factor of exactly 1000 at both endpoints (a units bug); the true values, `binom(2(J-1),J-1)/(2*3^(l-1))`, are 1019 to 3695 | critical | fixed: text corrected to "in the thousands... from 1019 at l=10 to 3695 at l=15"; root-cause note added to `notes/H-003.md` where the wrong figure originated, dated 2026-08-09 |
| C-48 | 4 | Round 3's own fix to Proposition 8 (the 1/sqrt(3) limit) stated it rules out uniform decay only "off the covering-relevant diagonal," but this is backwards: since `t/3^l=1/3` exactly, `l` drops out of `S(3^{l-1})` entirely and the limit holds at every scale m, including the diagonal | critical | fixed: text corrected to state the limit holds along the covering-relevant diagonal too, with the reason (`t/3^l=1/3` exactly, only `V mod 3` matters) |
| C-49 | 4 | The (l,m)=(14,16) phase-randomization diagnostic was described as "well past the covering threshold"; Table 1 gives j*(14)=19, so budget 16 is 3 below the threshold, not past it | major | fixed: corrected to "a budget below the covering threshold j*(14)=19" |
| C-50 | 4 | The K(l)/e(l) asymptotic identity, `K(l) =~ 4^{e(l)}`, dropped the polynomial correction from Stirling's approximation (`binom(2j,j) ~ 4^j/sqrt(pi*j)`, not `~4^j`), making the displayed `=~` relation technically false | moderate | fixed: corrected to `K(l) =~ |R_{j*(l)-1,j*(l)}|/3^l =~ 4^{e(l)}/sqrt(j*(l))`, with a note that a polynomial factor never changes sub-exponentiality, so the downstream equivalence (`K(l)` sub-exponential iff `e(l)=o(l)`) is unaffected |
| C-51 | 4 | Corollary 5 (headline `9/8 l + O(1)` bound) carried no visible conditional marker in its own theorem-environment, even though nearby prose says it depends on the unproven Empirical Result 3; downstream text (Remark 6) then describes it as established | major | fixed: added an explicit `[Conditional on Empirical Result 3]` label to the corollary's own statement |
| C-52 | 4 | Discussion section's "generic cancellation capping out below what combinatorial counting already proves" had the direction backwards: Proposition 7's 1.585l ceiling is worse (above), not below, Corollary 5's 1.125l bound | moderate | fixed: reworded to "generic cancellation unable to match a bound already established here by other means," removing the ambiguous directional language |
| C-53 | 4 | Corollary 9 (chain contraction)'s proof asserted the output's t+1 elements are pairwise distinct without establishing it, even though `maxrun`'s own definition requires pairwise distinctness | major | fixed: added the distinctness argument via 2's order (2*3^(l-1)) modulo 3^l, and the fact that equality would make the input chain the entire unit group, impossible since it sits inside H(l,j+1), the complement of a nonempty image |
| C-54 | 4 | Existence of j*(l) for every l was assumed throughout the paper (used from the Introduction on) but never proven | major | fixed: added Proposition 15 (Existence), an unconditional proof via 2 being a primitive root mod 3^l, giving `j*(l) <= 2*3^(l-1)-1`; verified computationally for l=2,3,4 before writing into the paper; Introduction's first use of j*(l) now forward-references it |
| C-55 | 4 | The one-step width identity `U(l,W+1)=U(l,W) union 2U(l,W) union Corner(l,W+1)` was asserted "exact" with no proof shown (carried from Round 3's "we omit the full derivation" note) | moderate | fixed: given a full three-case proof (new Lemma 14), verified computationally for l=2..5 across several widths before writing into the paper; the downstream Near-extinction bijection (Empirical Result 12) is still left empirical since the further argument pinning beta_1 was not carried through |
| C-56 | 4 | The complement set `K(l,W) := (Z/3^lZ)^* \ U(l,W)` collided notationally with Wirsching's own `K(l)` from the conjecture statement | minor | fixed: renamed to `D(l,W)` throughout |
| C-57 | 4 | The additive character `e(x):=e^{2pi i x}` in eq. (3) was never defined, and visually collides with the unrelated sequence `e(l)` from eq. (2) | minor | fixed: definition added at first use, with an explicit note that it is unrelated to `e(l)` |
| C-58 | 4 | Corner-redundancy's search range, "at every width W>=2l+1 checked exhaustively, l=3,...,13," omitted the upper end of the width range actually checked | minor | fixed: added the explicit upper bound (`W<=j*(l)+l-1`, the largest width the exact table reaches at each level) |
| C-59 | 4 | Banned-vocabulary residue from this paper's own Round 3 fixes: "genuinely linear e(l)" and "a striking anomaly" | minor | fixed: both reworded |
| C-60 | 4 | The AIC/BIC model comparison and the binomial plateau test were presented as two corroborating analyses, but both reduce to different views of the same fourteen-point sequence, not independent evidence | minor | fixed: one sentence added noting they move together, not independently |
| C-61 | 4 | (Addition, not a correction) A constant-e(l) rounding model can only produce increments of 0 or 1 (since log_4(3)<1), yet j*(1)->j*(2) is +3; this refutes a constant e(l) outright with no statistical machinery, a strictly simpler argument than the existing binomial test | minor | fixed: one paragraph added stating this directly, before the statistical tests |
| — | 4 | Opus 5 claimed the safety condition in Section 4 reads "back into a unit modulo 3m"; checked directly against the text, which reads "back into a unit modulo m" | — | verified false per Rule 8c, no change made |
| C-62 | 4 | (Producer-found, not from either reviewer) Section 5.3's "cell/local intensity/conductor-depth" language, requested for formalization by the researcher, was never actually reproducible as a precise statement: "at every resolution r<=10... probability between e^-23 and e^-100" is false under the only natural reading found (residue classes modulo 3^c). Direct recomputation from the exact histogram, l=10..15, depths c=8,9,10, gives hole probability from e^-2 to e^-108, a substantially wider range with a much shallower low end than claimed | major | fixed: sentence replaced with the formal definition (depth-c cell, depth-c local intensity, non-homogeneous Poisson hole probability) and the actually-computed range; the computation is now a script in the reproducibility repo (`section5-exponential-sum/local_intensity.py`) instead of resting on an unreproducible informal note |
| C-63 | 5 | The equivalence "K(l) sub-exponential iff e(l)=o(l)" was stated as a two-way "exactly," but the converse (e(l)=o(l) implying the conjecture) needs coverage to persist below l, which Theorem 9 does not give | major | fixed: reworded to state only the proven direction (conjecture implies K(l) sub-exponential) unconditionally, with the converse explicitly flagged open below l |
| C-64 | 5 | Corollary 10 (Chain contraction)'s statement omitted its "j>=l" hypothesis, though its proof invokes Theorem 9, which needs it; verified Theorem 9 is false without it (l=3,4,5, several j) | major | fixed: hypothesis added to the corollary's own statement |
| C-65 | 5 | Krasikov-Lagarias's paper was mischaracterized as attacking "total stopping time"; both reviewers independently caught this, and the primary source (already fetched this same round for the bibliography) says predecessor-set counting (x^0.84 lower bound), the same broad target as Wirsching's own reduction, by a different mechanism | major | fixed: description corrected, framing changed from "unrelated target" to "same target, different mechanism" |
| C-66 | 5 | The reproducibility repository's README (a live, public artifact) still titled the paper "a proven bound" (pre-Round-3 title) and every theorem/lemma/corollary number across four of its README files was stale after Round 4/5 added two new results | major | fixed: title updated to "a conditional bound"; all numbers resynced to the paper's current numbering in all four affected files |
| C-67 | 5 | The local-intensity range (C-62's fix) is undefined at depth c=l (the cell degenerates to a single point, giving lambda=0 for any holdout by definition); the text did not say c=l was excluded | moderate | fixed: added the c<l restriction explicitly, noting the degenerate case, matching what the underlying computation already excluded |
| C-68 | 5 | Section 5.2's exponential-sum computation is done at (l,j)=(18,16), six budgets below the actual covering threshold j*(18)=22, undisclosed; coverage necessarily fails there regardless of any Fourier-cancellation argument, which the reader was not told | moderate | fixed: added the explicit distance from threshold and the j<l caveat |
| C-69 | 5 | Empirical Result 12's range l+1<=j<=j*(l) was presented only as a compute limit; verified directly (maxrun(H(6,6))=5, maxrun(H(7,7))=5) that the equality genuinely fails at j=l, a validity boundary, not just an unchecked one | moderate | fixed: added the verified j=l failure with both computed instances |
| C-70 | 5 | The abstract stated a constant e(l) model is "disfavored at every statistic checked," omitting the paper's own unconditional theorem (Proposition 1) that a constant model is impossible outright | moderate | fixed: abstract now states the unconditional bound explicitly |
| C-71 | 5 | The abstract conflated two separate diagnostics (the extremal-cell/local-intensity analysis at l=10..15, and the phase-randomization experiment at a different (l,m)=(14,16)) into one causal claim ("shows are decided by") stronger than either individually supports | moderate | fixed: reworded to keep the two diagnostics separate, matching the body's own "both point the same way" scoping |
| C-72 | 5 | The plateau-frequency test's pooled p=0.0426 (all 22 increments) is computed under a null (constant-e(l) rounding, increments in {0,1}) already refuted with certainty by the same table's early increments (of 2 and 3); presenting it as informative, and as independent of the AIC/BIC comparison's 14-point tail, both overstate it | moderate | fixed: pooled figure dropped, kept only the tail-restricted p≈0.22 where the null is not already dead, and corrected the "same fourteen-point sequence" claim (the pooled test actually used all 23 table entries, not the same range as the regression) |
| C-73 | 5 | The window-k policy's finite-precision justification claimed the policy sees the true residue mod 3^k "at every step" whenever l>=k; false for the final k-1 steps of any play, where the true remaining modulus is below 3^k regardless of how large l is | moderate | fixed: generalized the existing l<k lifting argument to cover the final k-1 steps of every play, not just the l<k regime |
| C-74 | 5 | Two passages described the mean-payoff-game bound's conditional status inconsistently ("already established here by other means," "already known by other means") after Corollary 5 was correctly labeled conditional | minor | fixed: both reworded to say "conditionally established"/"conditionally known" |
| C-75 | 5 | Theorem 16 (parity)'s "fails only at l=1" language, and the abstract's echo of it, confused a hypothesis being inapplicable (j*(1)<l+1) with the conclusion itself failing | minor | fixed: reworded to "inapplicable," with a note that this says nothing about whether the conclusion would hold |
| C-76 | 5 | "An earlier stage of this investigation reported..." (process narration, Rule 5c) preceded the x4-cross-level impossibility argument; the math is correct but the framing narrates project history | minor | fixed: reworded to state the impossibility directly, no process narration |
| C-77 | 5 | Empirical Result 13 called all units modulo 3^7/3^8 (1458, 4374) "children (residues newly required for coverage)," which they are not — they are simply every unit at the finer modulus | minor | fixed: reworded to define "child"/"parent" as finer-modulus unit and its reduction, dropping the inaccurate parenthetical |
| C-78 | 5 | "j*(l) is the smallest j>=l with U(l,j+l-1)=full" (right after the new Existence proposition) implicitly assumed no j<l could cover first, which Lemma 14 (needing j>=l itself) cannot rule out | minor | fixed: reworded to state the coincidence holds "at every computed level" (verified, Table 1) rather than as an unconditional identity |
| C-79 | 5 | Proposition 1's "necessary for j>=j*(l)" implicitly used coverage-persistence (not yet proven at that point in the paper) rather than just the definitional fact needed | minor | fixed: narrowed to "necessary at j=j*(l) in particular," which is self-contained |
| — | 5 | Opus flagged Proposition 8 as "subsuming" Proposition 7's barrier without an explicit cross-reference; Opus's corner-redundancy-implies-tightness proof sketch; Opus's suggestion to upgrade Empirical Result 18 to a proposition (both reviewers, across two rounds, converging on compatible derivations); minor symbol reuse of `T`, `m`, `n` across different local contexts (all proof-local, standard practice, not erroneous); Empirical Result 17/18's thin l-range (5..9); Section 9's stored-data range vs. claims elsewhere (checked directly against the repo: Section 9's specific claims about what is stored are each accurate, the apparent mismatch is against claims Section 9 never made) | minor | superseded: the two credible leads (corner-redundancy-implies-tightness, the mod-9 upgrade) were worked out, verified, and added, researcher-directed, see "Post-loop verification" below; the rest remain cosmetic or, on inspection, not actual overclaims |
| — | 5 | Opus's l=24 attempt narration (three failed attempts, described in Section 2) flagged as process narration under Rule 5c | — | rejected: researcher's explicit 2026-08-09 decision to keep this passage, real circumstantial detail supplied by the researcher, Rule 5c Section 9's own exception |
| C-80 | 6 | Both reviewers independently confirmed Propositions 18 and 22 (the two propositions added after Round 5, never previously reviewed) are logically sound; Codex exhaustively spot-checked both, Opus reimplemented the paper's objects from scratch and reproduced every number it checked | — | verified, no change needed; recorded since it is the reason this round's other findings are prose/scope fixes, not proof-validity ones |
| C-81 | 6 | (Opus, the round's most serious finding) "the only known failures at the boundary width W=2l" is false in both directions: direct computation shows corner-redundancy fails at every width from l-1 to 2l-1 in general, and at the specific boundary W=2l it actually HOLDS for l=3,4,5,6, only starting to fail from l=7 | major | fixed: corrected the claim with the actual per-l pattern, verified computationally before writing it in |
| C-82 | 6 | Consequence of C-81, not exploited: since corner-redundancy holds at W=2l for l=3,4,5,6, Proposition 22's mechanism extends to prove Proposition 20's boundary case (j=l+1) at those four levels specifically, previously stated as "empirical only" | moderate | fixed: added as a remark after Proposition 22's proof, verified directly (l=3: 4+2=6, l=4: 5+2=7, l=5: 6+3=9, l=6: 7+3=10) |
| C-83 | 6 | Discussion overstates Proposition 22's range: "tight for every budget j>=l+2" omits the upper bound j<=j*(l), which the proposition itself requires (the equality is false past j*(l), where H is empty) | moderate | fixed in both the Discussion and the abstract |
| C-84 | 6 | ER13 (cost-1 repair rule) still not formally specified after being flagged in three prior rounds: "cheapest witness," "matched by natural containment" do not describe what the underlying script actually computes (a minimum symmetric difference over the FULL witness fiber at each budget, not restricted to minimum-depth witnesses) | moderate | fixed: verified the actual computation in `witness_check_6_7.py`/`witness_check_7_8.py` and rewrote the definition to match exactly |
| C-85 | 6 | Introduction's K(l) ~ 4^e(l)/sqrt(j*(l)) identity calls the correction "a polynomial factor in l" without qualification, but no unconditional polynomial bound on j*(l) is proved (Proposition 15's unconditional bound is exponential) | moderate | fixed: scoped the claim to "at every level actually computed" and cited which bounds are unconditional vs. conditional |
| C-86 | 6 | Section 6's opening states "j>=j*(l) exactly when H(l,j)=empty" as if following from the definition of j*(l) alone; the converse direction actually needs persistence (Theorem 9), justified only two sentences later | moderate | fixed: reordered to state only the one-directional definitional fact first, then the persistence-dependent equivalence, matching what is actually proven at that point |
| C-87 | 6 | ER12's "equality fails at j=l" was stated as if general, but direct computation shows it holds for l=1,...,5 and only fails from l=6; the given justification ("Corollary 10 and 11 both requiring j>=l") does not actually explain the failure, since j=l already satisfies j>=l | moderate | fixed: corrected the range and removed the non-explanatory justification |
| C-88 | 6 | Section 5.2's l=18 computation reports "it says nothing about every l" as its only caveat, when the sharper limitation established earlier in the same paragraph is about the budget j (six below the covering threshold), not the level l | moderate | fixed: added the j-based caveat to the closing sentence |
| C-89 | 6 | Proposition 7 (the 1.585l sqrt-cancellation ceiling) and Proposition 8 (the 1/sqrt(3) limit) were left unreconciled: Proposition 8 shows no fixed C can even satisfy Proposition 7's hypothesis at the frequency t=3^(l-1), a stronger conclusion than "worse than Corollary 5" | moderate | fixed: added an explicit sentence connecting the two |
| C-90 | 6 | l=22's "500 GiB of swap" and l=23's "263 GiB of state" read as directly comparable figures reporting more memory for l=22 than l=23, backwards from the real ~84 GiB vs ~263 GiB state progression (500 GiB was swap capacity added, generously, not the amount used) | moderate | fixed: verified against `notes/H-001.md`'s own figures (84 GiB, 500 GiB capacity, 263 GiB), rewrote both sentences to state actual state size vs. swap capacity as distinct quantities |
| C-91 | 6 | Unparseable sentence describing the l=23 checkpoint/resume mechanism (one sentence conflating the earlier kill, the mechanism's addition, and its non-use) | minor | fixed: split into two sentences |
| C-92 | 6 | Proposition 18 (mod-9 containment) needs l>=2 stated explicitly; beta_1 and "x mod 9" are ill-posed at l=1 | minor | fixed |
| C-93 | 6 | Abstract's "two precisely stated open questions remain" reads as if nothing else in the paper is unproven, when ER 3's correspondence, ER 17's bijection, and Proposition 20's converse are all also left open | minor | fixed: reworded to "two of the questions this work leaves open are named and precisely stated... others are noted where they arise" |
| C-94 | 6 | "the actual primitive-frequency max/RMS ratio is 15.79" never states max/RMS of what | minor | fixed: added "writing N(z) for the exact hit count..." |
| C-95 | 6 | Abstract's "extremal cells" is stronger than the body, which shows only "well below the global mean," not extremality (ranks/quantiles) | minor | fixed in the abstract, matching the body's own more careful phrasing |
| C-96 | 6 | Introduction's roadmap "(Sections 5 and 6)" is outdated: the direct holdout study now spans Sections 5-7 after Propositions 18/22 were added to Section 7 | minor | fixed |
| C-97 | 6 | Corollary 10's element list "x/4, x/2, x, ..., 2^(t-2)x" is degenerate/misleading at t=1, where the correct output is just {x/4, x/2} | minor | fixed: restated as $2^ix$ for $i=-2,\dots,t-2$, correct at every $t\ge1$ including the proof's own use of $t=1$ |
| C-98 | 6 | Proposition 1's cardinality result (`|R_{j-1,j}|=binom(2j,j)`) is essentially Wirsching's own Corollary 1.8 (verified against the primary source), re-derived here with no attribution | minor | fixed: added a one-clause credit |
| C-99 | 6 | Abstract's "capped below even this bound" reads ambiguously (Proposition 7 gives a floor, worse than the 1.125l bound, not an upper cap below it) | minor | fixed: reworded to "cannot beat a threshold worse than this bound" |
| C-100 | 6 | (Producer-found, neither reviewer flagged it) Rule 5c's antithesis budget (at most 2 "P, not Q" / "not merely P but Q" constructions per document) was blown: 13 instances had accumulated across Rounds 3-6's text additions, none re-checked against this specific budget since Round 1 | moderate | fixed: cut to exactly 2 (the mean-payoff-game bound's verified-not-proven status, and the doubling-chain sufficient-not-necessary distinction), the rest rewritten as plain positive statements |
| C-101 | 7 | (Codex) Section 5.3's phase-scramble statistic was described as deviation from the global occupancy mean ("N(z)-mean"); the actual quantity computed (verified against `analyze_inverse.py`) is `3^(l-1)(3N_l(z)-N_{l-1}(z mod 3^(l-1)))`, a measure of imbalance among the three lifts of each parent residue, a different quantity | major | fixed: rewrote with the correct identity, verified against the underlying script before acting |
| C-102 | 7 | (Codex) "coverage failure is decided by phase structure" (Section 5.3 and echoed in the Discussion) overstates what the phase-scramble null diagnostic shows: it compares extremal ratios of a signed transform, not whether valid scrambled models actually contain uncovered residues | moderate | fixed in both locations: reworded to a properly scoped null-diagnostic conclusion |
| C-103 | 7 | (Codex) Introduction's "the natural Fourier approach... is shown to fail" claims a general negative result the body does not establish; only the naive uniform-cancellation version is shown to fail | moderate | fixed |
| C-104 | 7 | (Opus) Introduction's citation to Wirsching 2003 had an ambiguous antecedent, readable as claiming that paper develops the covering-question construction itself, which it does not (verified: no "covering", no R_{j,k}, no WCC in its text); the paper develops the broader predecessor-density route | major | fixed: restructured the sentence so the citation attaches unambiguously to "Wirsching's own route to positive predecessor density" |
| C-105 | 7 | (Opus) ER17 (Near-extinction bijection)'s forward (subset) direction is provable directly from Theorem 9 + Theorem 16, no new machinery, but was labeled "empirically verified only" | moderate | fixed: verified the derivation and computationally at l=2..7, split into a proven Proposition 17 (forward containment) plus a narrower Empirical Result 18 (the reverse containment, still open) |
| C-106 | 7 | (Opus) Empirical Result 3 (the game's worst case) uses a min over each z0's legal plays without establishing the set of legal plays is ever nonempty; a general proof would also need each move's successor to stay a unit at the next modulus, not just the mod-3 legality check | moderate | fixed: added an explicit note that this is empirically confirmed by the l=1..12 verification but not proven in general, naming the actual gap |
| C-107 | 7 | (Opus) The 1547 counterexample paragraph described the falsified claim as "a doubling chain... necessary for survival to that budget," but the actual counterexample refutes a different, more specific statement: the per-witness converse of Theorem 9's set inclusion | moderate | fixed: restated the falsified claim precisely as the per-witness converse, connected explicitly to what Section 7 does and does not prove about the weaker (corner-redundancy) converse |
| C-108 | 7 | (Opus) Section 5.2's L1 mass diagnostic restricts to frequencies coprime to 3, silently excluding t=3^(l-1), the single frequency Proposition 8 proves carries the largest known magnitude | moderate | fixed: added an explicit note about the exclusion and its scope |
| C-109 | 7 | (Opus) Notation collision: T is defined as `\|R_{j,k}\|` at eq. (3) for the general family, then redefined as `\|R_{j-1,j}\|=binom(2j,j)` in Proposition 7's proof for the specific family actually used from there on | moderate | fixed: added a one-clause note that Proposition 7 specializes eq. (3)'s general T, rather than silently reusing the symbol |
| C-110 | 7 | (Opus) Section 9 (data availability) never mentions the separate tool behind the l=22 maxrun computation cited in Empirical Result 12 and Proposition 20's discussion; the stored-dump description (l=5..21) does not cover it | moderate | fixed: added an explicit sentence naming this as a separate, directly runnable tool, not a stored dump |
| C-111 | 7 | (Opus) Abstract advertises the square-root-cancellation threshold (Proposition 7) as a live obstruction while omitting that Proposition 8 shows no constant can even achieve it at one explicit frequency; a reader of the abstract alone gets an incomplete picture. Checked against the current abstract text (Rule 8c) and confirmed the gap was real, not already covered by Round 6's softening | moderate | fixed: added one clause to the abstract stating the premise is refuted outright |
| C-112 | 7 | (Opus) Abstract's "verified at every level checked" (corner-redundancy) is vague; corner-redundancy is verified only for l=3,...,13, while "levels checked" elsewhere in the paper means l up to 20-23 | minor | reviewed: the abstract's surrounding sentence already scopes this to "one further combinatorial property verified at every level checked" without claiming a specific range; judged adequately scoped in context, no change |
| C-113 | 7 | (Opus) Self-contradictory phrasing: "the only increment... at which the covering budget does not increase" (an increment at which nothing increases) | minor | fixed: reworded to "the only step... at which" |
| C-114 | 7 | (Opus) Ambiguous parenthetical after the corrected corner-redundancy boundary claim (Round 6's own fix), readable as contradicting the failure clause it modifies | minor | fixed: reworded for one unambiguous reading |
| C-115 | 7 | (Opus) Banned vocabulary from the project's writing protocol: "precise/precisely" (twice), "substantially" (twice), "not a meaningful test" | minor | fixed: all five reworded |
| C-116 | 7 | (Opus) Abstract's "empirically exact at the remaining budget" understates: at l=3,4,5,6 that budget (j=l+1) is now proven, not merely empirical, per Round 6's Proposition 22 extension | minor | fixed |
| C-117 | 7 | (Opus) Proposition 8 is placed in subsection 5.3 (about holdout cells and phase randomization) though its content (magnitude of S(3^(l-1)), refuting Proposition 7's premise) belongs with 5.1 | minor | deferred: organizational only, not a correctness issue; the content connection between Proposition 7 and 8 is now made explicitly in the text (C-89, Round 6) regardless of section placement; moving a proof block risks new errors for a purely stylistic gain, not attempted this round |
| C-118 | 7 | (Opus) The "independence model" comparison (Section 7, before Lemma 21) and the phase-experiment's population/normalization (Section 5.3) remain under-specified (Bernoulli vs. fixed-cardinality, wraparound, which residues) | minor | deferred: recurring since Round 4, genuine gap but requires either a new formal model definition or new experiments; left as a carried item |
| C-119 | 7 | (Opus) Durfee depth (Empirical Result 13) is defined and used for one clause, never connected to the "cost-1 local repair rule" the result is named after; the Durfee-depth counts and the symmetric-difference repair costs are two separate measurements presented together | minor | deferred: a real structural clarity point, but restructuring ER13's exposition carries more risk than value this late; left as a carried item |
| C-120 | 7 | (Opus) Safety condition's three-lift quantifier ("regardless of which digit the adversary supplies") oversells: for every k>=3 used in this paper, 3^k=0 mod 9 makes the quantifier vacuous in one respect (T_d(x) mod 3 depends only on x mod 9) | minor | deferred: correct but narrow observation, not an error in what's claimed; left as a carried item |
| C-121 | 8 | (Codex) Section 7's corner-redundancy discussion said the property "only becomes an open question from l=7" after describing it as checked to fail at l=7..13; once checked to fail, it is a settled negative fact, not open. Repeated in three places (after Lemma 22, after Proposition 23, and in the Discussion) | major | fixed in all three locations: corrected to distinguish "checked to fail, l=7..13" (settled) from "unchecked beyond l=13" (genuinely open), and from the still-open converse itself |
| C-122 | 8 | (Opus) Section 5.2's exclusion parenthetical had an unbalanced parenthesis (a whole sentence break nested inside an inner paren, with only one closing paren for two opens) and was unreadable as written | moderate | fixed: rewrote as three clean sentences; verified whole-document paren balance afterward |
| C-123 | 8 | (Codex) Proposition 23's proof applies Corollary 10 to "a maximal chain of length maxrun(H(l,j'+1))," but Corollary 10 is stated only for chains of length >=1; at the final telescoping step the set is empty (length 0), so no such chain exists to apply it to | minor | fixed: split into the empty case (trivial, since s>=1 always holds there) and the nonempty case (Corollary 10 applies as stated) |
| C-124 | 8 | (Opus) The "3.9 expected plateaus" figure was presented as an unexplained number from "the earlier manuscript's own table," reading as an empirical measurement rather than the model constant it is (19*(1-log_4(3))) | moderate | fixed: derived the figure explicitly from the constant-rounding model's own math |
| C-125 | 8 | (Opus) j*(l)-l, in {0,2,3,4,5} across the computed range and flat at 4 for l=16..23, the single integer most directly tied to whether e(l) could be linear, was never displayed anywhere in the paper | moderate | fixed: added the explicit sequence as a sentence near Table 1, with a caveat that this flatness is not a proven bound (Proposition 1 already rules out any bounded ceiling in general) |
| C-126 | 8 | (Codex) Theorem 4's proof telescopes a potential inequality along "any l-step play s_0,...,s_l," but the preceding paragraph (connecting a real play against the actual digit sequence to this abstract telescoping) never states that the resulting window-k state sequence is literally such a play, with s_{i+1} the successor of s_i under sigma_k's own chosen move | moderate | fixed: added the missing connecting clause |
| C-127 | 8 | (Codex) "the model comparison and the plateau test are the same question" -- verified: since e(l+1)-e(l) can only take one of two fixed values under the constant model, both diagnostics reduce to the same binary fact, not merely "not independent" as Round 4's earlier fix (C-60) stated | moderate | strengthened: made the equivalence explicit rather than just noting non-independence |
| C-128 | 8 | (Codex) l=21,22,23's "exact" values rest entirely on one Rust implementation, cross-checked against Python only up to l=20; no independent verification exists in the new range | moderate | reviewed and partly addressed: added a sentence explaining the DP's internal self-certification (minimality is inherent to how j*(l) is defined and searched) and stating plainly that l<=20's cross-check is carried forward by inference, not re-established, for l=21-23; an actual independent re-run at l=21 (Opus estimates hours, not days) was not attempted this round -- deferred, see Round 8 narrative |
| C-129 | 8 | (Opus) t=3^(l-1)'s conjugate t=2*3^(l-1) has the identical magnitude by S(3^l-t)=conjugate(S(t)), so calling t=3^(l-1) "the single frequency" carrying the largest magnitude is imprecise | minor | fixed |
| C-130 | 8 | (Opus) "the frequency Proposition 8 shows carries the largest known magnitude" conflates what Proposition 8 proves (an asymptotic value, T/sqrt(3)) with an empirical comparative claim (that this is the largest among all frequencies, observed only at accessible l) | minor | fixed: separated the proven asymptotic value from the empirical "largest observed" claim |
| C-131 | 8 | (Opus) Empirical Result 12's stated compute range (l=5..20) omits l=3,4, which Proposition 23 (added this round's fixes) now proves the same equality for, reading as if those levels were never checked | minor | fixed: added a parenthetical noting l=3,4 are covered by the later proposition instead |
| C-132 | 8 | (Opus) Empirical Result 20 (mod-9 exclusion)'s stated range starts at l=3, but Proposition 19 applies from l=2 and l=2 fits the same pattern (verified directly: H(2,3)={7}, matching 4^(J+1) mod 9 for J=4) | minor | fixed: extended the stated range to l=2..16 |
| C-133 | 8 | (Codex) Corollary 1.8's citation omits the chapter number given for Conjecture 3.9 two lines earlier | minor | fixed |
| C-134 | 8 | (Opus) Section 5's opening states Corollary 5's bound as if unconditional ("Corollary 5's bound, 1.125l, is well above...") one paragraph after Corollary 5's own conditional label | minor | fixed: added "conditional" at this use |
| C-135 | 8 | (Opus) One paired-dash appositive (using "--"), against the project's own ban on paired dashes | minor | fixed: replaced with commas |
| C-136 | 8 | (Opus) Two tricolons in immediate succession in the Discussion's adjacent-areas paragraph, a rhythm marker even though each list's three items are individually real, not padded | minor | fixed: restructured the second list into separate sentences, keeping all three findings |
| C-137 | 8 | (Opus) Proposition 8 sits in subsection 5.3 though its content belongs with 5.1/5.2 | minor | deferred: same reasoning as Round 7's C-117, organizational only |
| C-138 | 8 | (Opus) The corner-redundancy open question is posed at exactly W>=2l+1, precisely where the checked failures stop, with no structural reason given and nothing ruling out failure resuming at larger W for l>13 | minor | reviewed: an honest description of what was actually checked, not a hidden methodological choice; the paper already states the range is "checked exhaustively for l=3,...,13" without claiming any special significance to the boundary beyond that; no change made |
| C-139 | 8 | (Opus) The checkpoint/resume mechanism sentence (Section 2) narrates process with no bearing on any claim, distinct from the l=24 attempts narration the researcher already ruled to keep (that ruling covered the l=24 paragraph specifically, not this one) | minor | fixed in Round 9: the checkpoint/resume sentence and the "generous round figure" aside cut (Opus's Round 9 finding #12 flagged the same paragraph independently); the l=24 paragraph itself is untouched |
| C-140 | 8 | (Opus) The abstract is one long, low-variance block (~450 words) | minor | deferred: a real Rule 5c point (sentence-length variance), but rewriting the abstract's rhythm risks disturbing content already checked claim-by-claim across 8 rounds; left as a carried item for a dedicated abstract pass |
| C-141 | 9 | (Opus) The full-spectrum positivity criterion `sum_{t!=0}|S(t)| < T` that Section 5 opens with is not merely hard to reach, it is unsatisfiable for every l, j, k: since every element of R_{j,k} is a unit mod 3, N(0)=0, so `sum_{t!=0} S(t) = -T` exactly, forcing `sum_{t!=0}|S(t)| >= T` by the triangle inequality | major | fixed: Proposition 7 (label kept, no renumbering ripple beyond the one below) restated as the impossibility itself, with the sharper localized identity `S(3^{l-1})+S(2*3^{l-1})=-T` proven in the same short proof; the old 1.585l threshold computation kept as an a-fortiori remark, not a numbered result; verified independently by the producer both algebraically and by direct computation (six (l,j,k) cases) before writing the fix, per Rule 8c; new script `section5-exponential-sum/unreachable_criterion.py` in the repro repo |
| C-142 | 9 | (Codex) Table 3/Theorem 5's "self-certified ... exactly" language for rho_k rests on an adversary lower-bound computation (`adversary_lower_bound()` in `mpg4.py`) that, like the policy search, is restricted to actions `d<=dcap=40`, not the full period `d<2*3^k` (9,565,938 at k=14); "upper bound equals lower bound" only certifies rho_k exactly for the capped game | major | fixed: reworded to state plainly that the upper bound (all Corollary 6 needs) does not depend on the cap, while the "exact game value" framing is scoped to d<=40; verified independently against the actual solver source (`mpg3.py`'s `build_actions`, `mpg4.py`'s `solve`) and every stored certificate's actual max `d` used (11 at k=14, well under 40) before writing the fix, per Rule 8c; repro repo's section4 README updated with the same scoping |
| C-143 | 9 | (Codex) Section 2's own Round-8-vintage sentence claimed Proposition 2 (unboundedness, `e(l)>=log_2(l)/4-O(1)`) "already rules out any bounded ceiling in general" for `j*(l)-l`; false, since a bounded ceiling makes `e(l)` grow linearly, which a logarithmic lower bound does not touch | moderate | fixed: corrected to state nothing here rules out the ceiling persisting, and spelled out what persistence would actually imply (linear e(l), exponential K(l), falsifying the conjecture under the persistence proviso) |
| C-144 | 9 | (Codex) Round 8's own strengthening of C-60 to "which growth model best fits e(l)" and "how often does j*(l) plateau" being "the same question... asked in different words" overshot: the free-intercept OLS constant model and the constant-rounding model are different objects | moderate | fixed: reverted to "not independent checks" (the original, weaker claim), with the two models explicitly distinguished; also corrected the plateau test's binomial parameter, which had used a rounded `3.9/19` instead of the exact `1-log_4(3)`, changing the reported p-value from 0.22 to the correct 0.214 |
| C-145 | 9 | (Codex) Table 1's "certifies coverage and its absence internally, by construction" does not cover budgets `j<l`: the production search clamps `j_start.max(ell)` (verified against `src/main.rs`), so it never tries smaller j; nothing in the paper ruled out some `j<l` also covering | moderate | fixed as an upgrade, not just a caveat: new Lemma 1 ("No smaller budget covers") proves `j*(l)>=l` outright for `l=2,...,23` from a reduction argument (coverage mod `3^L` at budget `j` implies coverage mod `3^j` for `j<=L`) plus Table 1's own already-computed strict rows; new script `section2-jstar-computation/no_smaller_budget.py`, independent direct enumeration, l=2..13 |
| C-146 | 9 | (Codex + Opus) "Statistically indistinguishable" and similar language applied to Table 2's AIC/BIC/LOOCV comparison overstates the inferential basis for a deterministic, exact integer sequence with no sampling model | moderate | fixed: reworded to "not distinguished... by these criteria" in the abstract and in Section 3, matching the paper's own existing "no sampling interpretation" caveat elsewhere |
| C-147 | 9 | (Codex + Opus) Abstract's "outside any sparse exceptional set" overclaims relative to Section 5.2, which checks one fixed magnitude threshold at one accessible level, not every possible threshold | moderate | fixed: reworded to "the sparse exceptional set a fixed magnitude threshold defines" |
| C-148 | 9 | (Opus) Remark (the rho_k=L+A/k fit) states the fit "is not evidence of any specific limit," then closes by claiming "there is evidence in the course of this work that the window relaxation may carry an irreducible gap above the true rate" — self-contradictory, and no such evidence appears anywhere else in the paper | moderate | fixed: the unsupported closing clause cut; verified first that no such evidence exists elsewhere in the paper (Rule 11), so the claim could not be relocated, only removed |
| C-149 | 9 | (Opus) Section 5.3 assigns hole probabilities down to `e^{-108}` to holdout residues that actually occurred, then reports this as "no single exponent characterizes it" rather than stating the non-homogeneous Poisson model is flatly falsified | moderate | fixed: reworded to state the falsification outright, keeping the surviving descriptive claim (holdouts sit in low-intensity cells) separate from the failed probabilistic model |
| C-150 | 9 | (Opus) Abstract's "one further combinatorial property verified at every level checked" does not tell a reader that "checked" stops at l=13 against a table running to l=23 | moderate | fixed: reworded to name the range explicitly, `l=3,...,13` against a table to `l=23` |
| C-151 | 9 | (Opus) Proposition 9 (formerly 8, the `1/sqrt(3)` limit) is stated "for every fixed l>=1" though its own proof shows `l` drops out entirely (only `V mod 3` matters) | minor | fixed: parameter dropped from the statement; the post-proof paragraph restructured to show the proposition sharpening Proposition 7's new exact bound `|S(3^{l-1})|>=T/2` to the precise ratio `1/sqrt(3)`, instead of re-deriving a refutation Proposition 7 now already gives |
| C-152 | 9 | (Opus) Empirical Result 21 (mod-9 exclusion) references "extending the previous computational range, l=3,...,9," but no such range is established anywhere else in the paper | minor | fixed: dangling parenthetical cut |
| C-153 | 9 | (Opus) §4's "the twelve specific policies actually exhibited... in Table 3" overstates what the table shows (rho_k, C_k only, not the policies themselves, which are thousands of state-to-move entries stored in the repro repo) | minor | fixed: reworded to "whose resulting (rho_k,C_k) are reported in Table 3, each independently checked as described in Section 9" |
| C-154 | 9 | (Opus) The corner-redundancy paragraph's "narrower width from l-1 up to 2l" is self-contradictory (2l is not narrower than 2l) and leaves unclear what the l=3..6 boundary check actually covers | minor | fixed: reworded to state the sub-`2l` range and its non-dependence on any proof in the paper explicitly |
| C-155 | 9 | (Opus) Corollary 6 states `j*(l) <= (9/8)l + O(1)` though the exact constant `C_14=33/2` is already in Table 3 two lines above | minor | fixed: corollary now states the explicit `+33/2` |
| C-156 | 9 | (Opus) Bibliography check for [6] (Meyerovitch-Young, arXiv:2603.21449): title, authors, and topic (covering radius, rationality/computability, sofic shifts) confirmed against the arXiv abstract page directly | minor | verified correct, no change needed; recorded per Rule 8c since the critique raised a factual claim (possible citation error) that turned out not to hold |
| C-157 | 9 | (Opus) Notation collisions on several load-bearing symbols: `e(x)` (character) vs `e(l)` (excess), `S(t)`/`\|\|S\|\|_1` vs exponent sets `S`, `S'`, `J` as total play cost (Section 4) vs `J:=j*(l)` (Propositions 18, 20), `m` as `3^k` (Section 4) vs family index `R_{m-1,m}` (Proposition 9) vs `J-1-l+beta_1` (Proposition 20) | minor | deferred: real, but a full symbol audit risks touching load-bearing proof text this late in the loop; `e(x)`/`e(l)` is already flagged in-text (line "unrelated to the sequence e(l)"); left as a carried item |
| — | 9 | (Opus, independent finding, distinct model from Codex) Sections 4, 6 and 7's proofs re-derived and checked line by line, including every numeric claim reachable by direct enumeration (Table 1, the 1547 counterexample, maxrun values, corner-redundancy at every checked l); no error found | — | confirms the loop is catching real things in Sections 2, 3 and 5's framing while the combinatorial core (Sections 4, 6, 7) continues to hold up under independent re-derivation |

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

### Round 3 (Codex on `gpt-5.6-sol` + Opus 5 at maximum reasoning effort, 2026-08-09)

Fable is replaced by Opus 5 at maximum effort as the second reviewer, per the researcher's explicit
instruction this round, "todas as proximas rodadas use o opus 5 no esforço maximo. esqueça o fable
por enquanto." Opus 5 needed two retries: its first two attempts each exceeded the harness's
64,000-output-token limit in a single response (thinking plus text) before producing a report; the
third attempt succeeded by writing brief per-section scratch notes to disk between reasoning steps,
then composing a capped, ranked final report from those notes. This staged-notes pattern is the
working invocation for Opus 5 as a critique-loop reviewer going forward.

The reproducibility repository (`faculdade/weak-covering-conjecture`) was populated between Round 2
and Round 3 (a background agent mirrored the six section-relevant experiments, regenerated five
missing mean-payoff-game certificates, and re-ran every check, all before Round 3's reviewers read
the PDF), addressing a finding both reviewers had raised in Round 1 and Round 2 and that both raised
again independently in Round 3 before the population had propagated to their read of the PDF (a
process note, not a live finding: see below).

One process bug this round: because editing happened while Codex's review was still running, part of
its report reads a slightly earlier state of `main.tex` than what Round 2 actually finished on;
nothing material was lost, since every item Codex raised was checked against the current text before
acting, and any already-fixed item was simply not re-fixed. Starting with Round 4, the PDF is frozen
for the full duration of both reviewers' runs.

Round 3's single most serious finding, from Codex, is that Round 1 and Round 2's own restructuring of
the mean-payoff-game section had never actually been checked against a concrete example: the claimed
witnessing statement (a legal $l$-step play of cost $J$ witnesses $z\in R_{J-1,J}\bmod3^l$) is
**false**, not merely unproven, refuted by a two-line counterexample ($l=2$, $z=4$, play $(0,1)$,
$J=1$: $4\notin R_{0,1}\bmod9=\{1,2\}$). This had survived two prior rounds of critique because
neither reviewer, nor the producer, had tried an actual numeric example against the claim as printed;
it took Codex running a short Python check to surface. Independently re-deriving the real
correspondence (with help from an outside consultation, per Rule 11b, given the stakes and the
project's own history of getting exactly this kind of multi-parameter index substitution wrong) found
that a legal play actually witnesses a *twisted* residue, $2^{J+l-1}z_0$, not $z_0$ itself; this was
proven by induction (a genuine symbol-by-symbol proof, not another computational assertion) and
independently checked against every legal play for $l=1,\dots,4$ (780 cases, zero exceptions) before
being written into the paper. The corrected logical chain needed for Theorem 3 turns out not to
depend on this twisted-witness fact at all: it only needs the separately-verified equality
$j^*(l)=\max_{z_0}\min(\text{cost})$ (matching the project's own `step_a_grounding.py`, independently
re-verified here for $l=1,\dots,8$) plus the observation that any specific policy's realized cost
upper-bounds the true minimum. The twisted-witness lemma is kept in the paper as genuine, verified
context connecting the game to Section 7's $U(l,W)$ formalism, but is explicitly flagged as not
itself establishing the soundness identity, avoiding a second version of the same overclaim.

Both reviewers independently found the abstract had drifted from the body on two claims (Theorem 8's
inclusion stated as a union instead of an intersection, and the parity theorem stated without its
$j^*(l)\ge l+1$ hypothesis) exactly the Rule 8b failure mode CLAUDE.md names as the project's most
validated lesson, here on a paper that had already been through two rounds of critique and an
explicit Rule 8b pass each time. Both fixes are one-sentence corrections, but the fact that they
survived two prior "abstract re-check" passes is itself worth recording: a correction to a proof's
internal machinery (Theorem 3's restructuring in Round 2) does not automatically prompt a re-read of
an *unrelated* abstract sentence (Theorem 8's phrasing) that a Round 8b pass did not think to
re-examine, since it had not itself changed. The lesson for future rounds: a full-abstract read
against the current body, not just against what changed, is the safer default once more than one
round has passed.

Also fixed this round, each independently checked before acting: the game's action set was asserted
finite without a real finiteness argument (added, via a periodicity/domination fact); the window-$k$
policy's applicability to $l<k$ was asserted without an argument (added, one sentence); Table 3
claimed an "explicit $C_k$" that the table never printed (added, from the project's own certificate
files, cross-checked against $j^*(23)$); Corollary 10's proof reasoned informally "as $j$ decreases
from $j^*(l)$," which reads as assuming the quantity being proven (rewritten as a genuine proof by
contradiction); Sections 5.2 and 5.3 reported percentages and probabilities with no stated budget,
normalization, or actual counts (rewritten with the real parameters and numbers, pulled from the
project's own verified experiment records, `experiments/E-008-exceptional-frequencies/README.md` and
`notes/H-003.md`'s Round 3 section); the corner-redundancy discussion claimed proving it would settle
Proposition 17's converse, when the only known failures sit exactly at Proposition 17's own budget
(rescoped in both the body and the Discussion); the paper never stated the precise link between
$K(l)$'s sub-exponentiality and $e(l)=o(l)$, leaving the growth-model comparison's real stakes
unstated (added); and Proposition 7's statement and proof disagreed on the error term ($O(\log l)$
in the statement, $O(1)$ in the proof; tightened to match the proof).

Not yet addressed, carried to Round 4: residual statistical-inference-flavored language around the
plateau-frequency test's $p=0.0426$ threshold (both reviewers, moderate); the independence model in
Section 7 is described but not formally specified (Codex, moderate); Empirical Result 16's two-class
containment is provable by the same mechanism as Theorem 14 and could be upgraded from empirical to
proven (Opus, moderate, a strict improvement rather than a correction); the one-step width recursion
is asserted exact without a proof (Opus, moderate); the title's "a proven bound" is flagged by both
reviewers as an overclaim given the bound is conditional -- not changed unilaterally, flagged to the
researcher instead. Recompiled clean (12 pages, 0 errors, 0 warnings, 0 em-dashes) and visually
re-verified, page by page, for every edited section.

## Round 4 (2026-08-09)

Same protocol, both reviewers at maximum reasoning effort, model swap from Fable to Opus 5 per the
researcher's explicit instruction (Fable set aside for now). Opus 5 needed the same staged-notes
pattern established late in Round 3 (per-section scratch notes to a fixed file, then one capped
summary from the notes) to avoid the 64k-output-token failure that had hit it twice before; this is
now the working invocation for Opus 5 as a reviewer.

The most serious finding was self-inflicted: Round 3's own fix to Proposition 8 had the
diagonal/off-diagonal direction backwards (C-48), and the occupancy-mean figure it corrected in
Section 5.3 that same round carried a units bug from the project's own notes, off by exactly 1000 at
both endpoints, caught independently by both reviewers (C-47). Both are now fixed, and the second is
also corrected at its source in `notes/H-003.md`, dated, so a future session reading that file does
not re-import the wrong number. Two rounds in a row where a genuine finding turned out to be
introduced or inherited by the previous round's own fix, not a pre-existing defect, is worth flagging
plainly: fixing at this speed has a measurable rate of introducing new small errors, which is exactly
why every finding here was independently re-derived or re-computed (Rule 8c) before being written in,
not taken on the reviewers' word.

The most substantial addition this round was not a correction but a closed gap: Codex found that
`j*(l)`'s existence for every `l` is used from the Introduction onward but never proven anywhere in
the paper (C-54). This is provable unconditionally, using the elementary fact (already used elsewhere
in the paper) that 2 is a primitive root modulo `3^l`: a single base unit at width `l-1`, propagated
by repeated doubling, sweeps out the entire unit group within `2*3^(l-1)` steps. Verified
computationally for `l=2,3,4` before writing it in as a new Proposition 15, giving the explicit
(very weak, but unconditional) bound `j*(l) <= 2*3^(l-1)-1`. The same pass closed a second, related
gap Opus had separately flagged (C-55): the one-step width identity used to derive Theorem 16's parity
result had been asserted "exact" with the derivation explicitly omitted since Round 2; it turned out
to be a short three-case argument (reusing the same shift construction as the existence proof),
verified computationally for `l=2..5` before being written in as Lemma 14. The downstream Near-
extinction bijection (Empirical Result 12) is deliberately left empirical, since the further step
pinning the second-highest exponent was not carried through; upgrading only what was actually proven,
not the whole neighborhood of a fix, follows Rule 8d.

Also fixed this round: Corollary 9's proof asserted a distinctness fact it needed but never
established (C-53), closed with the same order-of-2 fact used in the existence proof, plus the
observation that the input chain reaching the full unit group would contradict it sitting inside a
proper complement; Corollary 5's headline bound carried no visible conditional marker on the
statement itself despite depending on an unproven Empirical Result (C-51); the K(l)/e(l) asymptotic
identity dropped a polynomial correction from Stirling's approximation, technically false as displayed
though the downstream sub-exponentiality equivalence survives it (C-50); a phase-randomization
diagnostic was described as "well past the covering threshold" when it is actually three budgets
below it (C-49); the Discussion's summary of how Proposition 7 compares to Corollary 5 had the
direction backwards (C-52); a leftover symbol collision between the width-recursion's complement set
and Wirsching's own `K(l)` (C-56), and an undefined additive character notation that visually
collides with the unrelated sequence `e(l)` (C-57), were both cleaned up; corner-redundancy's checked
width range was missing its upper bound (C-58); two Rule 5c banned words introduced by this paper's
own Round 3 fixes were caught and reworded (C-59). Opus separately noted the AIC/BIC model comparison
and the binomial plateau test are not independent evidence, both being different views of the same
fourteen-point sequence (C-60), and pointed out a strictly simpler, non-statistical refutation of a
constant `e(l)`: a constant-rounding model can only produce increments of 0 or 1, but the table's own
first two entries jump by 3 (C-61); both added.

One Opus finding did not survive Rule 8c verification: a claim that the safety condition's modulus
was misstated as "$3m$" in the text, checked directly against the actual wording ("modulo $m$"), and
found to be simply wrong. Recorded as verified-false rather than silently dropped.

Not yet addressed, carried to Round 5 or flagged to the researcher as a scoping decision rather than a
producer fix: Table 3 does not include the sigma_k/h_k values behind each certified policy, only
rho_k and C_k (Codex, moderate); the cost-1 local repair rule's falsification (Empirical Result 13)
is not given a fully formal statement with domain and cost function (Codex, moderate); Empirical
Result 16 (mod-9 two-class bound) remains a candidate for upgrading to a proposition, both reviewers
having now supplied compatible derivations across two rounds (Codex, moderate, carried from Round 3);
the "independence model" in the Discussion (maxrun's typical value under a density-matched random
model) is described but never formally specified or tabulated (Codex/Opus, moderate); Table 2 gives
model-comparison statistics but no fitted slope coefficients, the number that most directly bears on
whether K(l) is exponential (Opus, moderate); Section 5.2's L1-mass computation restricts to
frequencies coprime to 3, excluding `t=3^(l-1)` itself, which Proposition 7 proves carries the largest
known magnitude (Opus, moderate); that same computation runs six budgets below the actual covering
threshold at its one computed level, a gap only partly caveated in the text (Opus, minor); the
Grounding Lemma, since Theorem 3's proof no longer needs it, is arguably inert content rather than
load-bearing math (Opus, minor, a judgment call rather than a defect); the mod-9 empirical results are
verified only to l=9, thin against the exact table now running to l=23 (Opus, minor); the deposited
holdout data stops at l=21 while Section 7 quotes measurements through l=22 (Opus, minor); and the
bibliography, at four references, is thin for a paper reopening an active 1998 conjecture (Opus,
minor) -- widening it means reading and verifying each new reference against its primary source
(Rule 11) before it goes in, a scope decision for the researcher, not a unilateral producer add.
Recompiled clean (12 pages, 0 errors, 0 warnings, 0 em-dashes) and visually re-verified, page by page,
for every edited section.

## Round 5 (2026-08-09, final round under the 5-round cap)

Before launching Round 5, three researcher decisions carried from Round 4 were resolved: the
bibliography was widened by three references, each read and verified against its primary source
(Wirsching's own 2003 follow-up, Tao's 2019 paper, Krasikov-Lagarias); Section 5.3's informal
"cell/local intensity/conductor-depth" language was formalized, which surfaced a real,
producer-found error (C-62: the previously stated numeric range did not reproduce under any
natural reading, corrected via direct recomputation, now backed by a script in the reproducibility
repo); and the l=24 narration paragraph was kept as is, the researcher's explicit choice. This work
is recorded in the table above under Round 4 (C-62) since it closed Round 4's own carried items,
even though it happened just before Round 5 launched.

Round 5 itself: same protocol, Codex and Opus 5 at maximum effort, fresh context, no memory of any
prior round, PDF frozen for both runs' full duration. Opus used the staged-notes pattern; both
reviewers independently verified substantial parts of the paper from scratch rather than trusting
the text (Opus recomputed all 23 values of `e(l)`, `j*(l)` for `l=1..7` from a brute-force
implementation, every entry of Table 2, all binomial p-values, several theorems and lemmas by hand,
and all seven bibliography entries against primary sources; Codex read end to end and traced every
proof). Both reported no critical findings and confirmed the unconditional core mathematics is
sound; the issues found were hypothesis-placement, framing, and consistency problems, several of
them introduced by this project's own Round 4/5 fix passes rather than pre-existing.

The two most consequential findings, both independently caught by both reviewers: Krasikov and
Lagarias's paper (added to the bibliography earlier this same round) was mischaracterized in the
Discussion as targeting "total stopping time," when the primary source already fetched for that
citation says predecessor-set counting, the paper's own actual territory -- a wrong recollection
that leaked past the correct data sitting in context, corrected to state the shared target
honestly (C-65); and the reproducibility repository's own README, a live public artifact, still
carried the paper's pre-Round-3 title ("a proven bound") and theorem numbers stale by two rounds of
additions, meaning a reader who actually followed the paper's own link would see a stronger,
mismatched paper (C-66). Both are now fixed in the repository, not just the paper.

Corollary 10 (Chain contraction) was missing its own "for j>=l" hypothesis despite its proof
needing Theorem 9's identical requirement; verified directly (Theorem 9 fails at l=3,4,5 for
several j<l) before fixing (C-64). The Introduction's central equivalence claim, "K(l)
sub-exponential is exactly e(l)=o(l)," was two-directional where only one direction is actually
established without persistence below l; narrowed to the proven direction, converse flagged open
(C-63). Several precision fixes followed the same pattern of an unstated boundary or an implicit
assumption not yet available at the point it was used: Empirical Result 12's range turned out to be
a genuine validity boundary (equality fails at j=l, verified computationally: `maxrun(H(6,6))=5`,
`maxrun(H(7,7))=5`, not just an unchecked one), Section 5.2's exponential-sum computation sat six
budgets below the actual covering threshold undisclosed, the local-intensity range from the
just-finished 5.3 formalization was undefined at its own boundary depth `c=l`, and the plateau test
computed a pooled p-value under a null already refuted with certainty by the same table it was
tested against.

Not added this round, deliberately: Opus supplied a short proof sketch for the corner-redundancy
implies-tightness implication, and both reviewers, across two rounds now, have converged on
compatible derivations for upgrading Empirical Result 18 from empirical to proven. Both are
credible leads, but this is the last round under the researcher's 5-round cap, meaning any new
mathematics added here ships with no further review. Per the same caution that governs every
correction in this loop (verify before acting, keep corrections scoped), new proofs were judged a
different category of risk than fixing what a fresh reviewer just checked by hand, and were left
as documented open items instead of rushed in unreviewed. One Opus finding (Section 9's stored-data
range not covering every level mentioned elsewhere) was checked directly against the reproducibility
repository's actual contents and found to not be a real overclaim: Section 9's specific claims each
hold up against what is actually there; the apparent gaps are against claims Section 9 itself never
made. Recorded as such rather than silently accepted or silently dropped.

Recompiled clean (13 pages, 0 errors, 0 warnings, 0 em-dashes) and visually re-verified, page by
page, for every edited section. This is the final round under the researcher's explicit "up to 5
rounds" instruction; no further critique round is planned. Every entry in the status table above
now reads `fixed`, `deferred` with a stated reason, or `rejected` with a stated reason, per Rule
8/15 -- none left `open`. Per Rule 8/15's own logic, Round 5's fixes are themselves unreviewed by any
fresh pair of eyes; the mandatory pre-publication check (Rule 8, a genuinely independent model or
the researcher) should still run on this post-fix PDF before submission, whenever that is decided,
separately from and not satisfied by this critique loop.

## Post-loop verification, researcher-directed, 2026-08-09 (Rule 8e)

After Round 5 closed, the researcher explicitly asked for the two deferred leads (Opus's
corner-redundancy-implies-tightness sketch, and the mod-9 two-class upgrade both reviewers had
converged on across rounds) to actually be worked out rather than left as unpursued remarks. This
is Rule 8e's own discipline: a lead surfaced by a critic trying to break the paper gets a real,
bounded look, not a hunch-based dismissal.

Both derivations checked out, independently re-derived from scratch (not copied from either
reviewer's sketch) and verified computationally before being trusted, per Rule 11:

**Corner-redundancy implies tightness.** Corner-redundancy at a width is equivalent, via the
multiplication-by-2 bijection commuting with complementation and intersection, to the exact set
identity `D(l,W+1) = D(l,W) cap 2*D(l,W)`, sharpening Theorem 9's inclusion to an identity at that
width. The first proof attempt, chaining a single fixed maximal chain forward budget by budget,
had a real gap: it asserted the widths used stay within the hypothesized range without actually
establishing this, since the chain length `r=maxrun(H(l,j))` was not yet known to be bounded at
that point in the argument, making the width bound circular. Caught before being trusted, not after
committing it. The fix uses a cleaner single-step recursion instead: `maxrun(H(l,j'+1)) =
maxrun(H(l,j'))-1` whenever `H(l,j')` is nonempty and corner-redundancy holds at that width (`<=`
unconditional, from Corollary 10; `>=` from the same equality), then telescopes this over the fixed,
already-known number of steps from `j` to `j*(l)` (no dependence on `r` at all), landing on
`maxrun(H(l,j*(l)))=0` and hence `j*(l)=j+maxrun(H(l,j))` exactly. Verified computationally three
ways: the `D`-level set identity directly (l=3..7), the exact single-step recursion end to end
(l=3..8, every `(l,j)` with `l+2<=j<=j*(l)`, zero exceptions), and against the actual `H`/`maxrun`
data. Unconditional at `l=3..13`, where corner-redundancy is independently verified at every width
the argument uses; conditional on corner-redundancy in general. Added as Proposition 22.

**Mod-9 two-class containment.** Re-derivation confirmed the containment needs nothing beyond
Theorem 16's own proof (which already pins the extremal witness's top exponent) substituted into
the `H`-via-`D` shift identity, plus the elementary fact that `3*2^k mod 9` only ever takes two
values, regardless of the second-highest exponent `beta_1`'s actual value: no new machinery, and
critically, the containment does not require pinning `beta_1`, only its parity's effect. Verified
algebraically for `J=1..14` and directly against the exact holdout sets at `l=3,4` (the two levels
outside the project's existing `mod9_class_law.py` script, which independently covers `l=5..16` and
was run to extend the previously-cited computational range for the still-open exclusion claim from
`l=3..9` to `l=3..16`, zero exceptions either way). Split into a proven Proposition 18 (the
containment) and a narrower Empirical Result 19 (excluding the lower class `4^J`, still open,
sharpened: it is now explicit that the open question is about which parity of `beta_1` actually
occurs, not about the containment itself).

Both added to the paper (new Proposition 18, Proposition 22; Empirical Result 18 relabeled
Empirical Result 19 and narrowed to just the exclusion claim), with the abstract, Empirical Result
12, and the Discussion's two-named-questions paragraph updated to match (Rule 8b). Recompiled clean
(14 pages, 0 errors, 0 em-dashes), visually re-verified. Verification scripts
(`corner_redundancy_tightness.py`, `mod9_containment_proof_check.py`) added to the reproducibility
repository; all four affected README files (top level, `section4`, `section6`, `section7`) resynced
to the new numbering a third time.

This work happened after Round 5 closed and is therefore itself unreviewed by any of the loop's
fresh reviewers; it does not reopen the loop or count toward the 5-round cap, and does not change
the standing recommendation that a genuinely independent check should still run before submission.

## Round 6 (2026-08-09), first round under the researcher's extended 10-round cap

The researcher asked explicitly for the loop to continue past the original 5-round cap, up to 10
rounds, specifically to see whether the two reviewers converge. Round 6 is the first round under
this extension, and the first to review the two propositions (18 and 22) added after Round 5 closed;
neither had been seen by any reviewer before this round.

Both reviewers independently confirmed Propositions 18 and 22 are logically sound: Codex exhaustively
spot-checked both proofs and found no gap; Opus reimplemented the paper's core objects from scratch
(not using the project's own code) and reproduced every number it checked, including both new
propositions' identities on small exhaustive cases. Neither reviewer found a critical or major
proof-validity error. This round's findings are prose, scope, and consistency issues, not defects in
the two new results themselves.

The most serious finding (Opus) was a real factual error in the paper's own prose about corner-
redundancy's boundary behavior: the claim that corner-redundancy is "known to fail" at the boundary
width W=2l turned out to be backwards for four of the levels it was checked at. Direct computation
(verified independently before acting, per Rule 8c) shows corner-redundancy actually HOLDS at W=2l
for l=3,4,5,6, and only starts failing there from l=7. This was not just a wording fix: since
Proposition 22's proof mechanism only needs corner-redundancy at the widths it actually uses, the
corrected fact means the proposition's argument extends cleanly to prove Proposition 20's previously
"empirical only" boundary case (j=l+1) at exactly those four levels, verified directly. Neither
reviewer proposed this extension; it fell out of chasing down why the original "known to fail" claim
did not match a direct check.

Several other findings followed a similar pattern: a paper-level claim stated more strongly, or with
a less precise justification, than what the underlying computation or proof actually supports (the
Discussion's missing upper bound on Proposition 22's range, the Introduction's unqualified "polynomial
factor" claim, ER12's "equality fails at j=l" stated as if general when it only starts at l=6, Section
5.2's caveat naming the wrong variable). ER13 (the cost-1 repair rule falsification) was finally given
its actual formal definition after being flagged as under-specified in three consecutive prior rounds;
the fix required reading the underlying script (`witness_check_6_7.py`) directly rather than guessing
at what "cheapest witness" and "natural containment" were meant to describe, since the actual
computation turned out to be a plain minimum symmetric difference over the full witness fiber, not
the vaguer description the paper had carried since Round 1.

One finding was producer-found, not from either reviewer: a Rule 5c compliance check (the antithesis
budget, "at most two 'P, not Q' constructions per document") had not been re-run since Round 1, and
13 such constructions had accumulated across Rounds 3-6's text additions. Cut to exactly 2.

Recompiled clean (15 pages, 0 errors, 0 em-dashes, cite/bibitem check clean) and visually
re-verified. Full findings list above, C-80 through C-100, all resolved (fixed or verified-no-change).
Proceeding to Round 7.

## Round 7 (2026-08-09)

Same protocol, fresh context, PDF frozen (15 pages, post-Round-6). Codex found 6 issues, all
moderate/minor, no critical or major flaw in any formal proof, and confirmed the conditional
$9l/8+O(1)$ bound is consistently labeled conditional throughout. Opus found 20 issues, also no
critical or major mathematical error in any proof; it independently re-derived or reproduced all 23
values of `e(l)`, both fits in Remark 6, Propositions 7, 8, 15, 17 (new this round), 18, 22, Theorems
9 and 16, Corollaries 10 and 11, Lemmas 14 and 21, and every cited reference against its primary
source, including re-checking the local copy of Wirsching's book for both citations used.

The most substantive finding (Codex) was a real misidentification: Section 5.3's phase-scramble
statistic was described as measuring deviation from the global occupancy mean, but the actual
quantity the underlying script computes (verified directly against `analyze_inverse.py` before
acting, Rule 8c) is a measure of imbalance among the three lifts of each parent residue, a
genuinely different object with the same numerical value. Fixed with the correct identity. The
paper's "coverage failure is decided by phase structure" conclusion, in both Section 5.3 and the
Discussion, was also overstated relative to what a null diagnostic on that statistic actually shows,
and was rescoped in both places.

The second substantive finding (Opus) turned into a real proof upgrade, following the same pattern
as the post-Round-5 work: the forward (subset) direction of Empirical Result 17 (near-extinction
bijection) is directly provable by combining Theorem 9 and Theorem 16, no new machinery. Re-derived,
verified computationally at l=2..7 before writing in, and split into a proven Proposition 17 plus a
narrower Empirical Result 18 for the still-open reverse direction.

A citation-clarity issue (Opus) was also caught and fixed: the Introduction's sentence introducing
Wirsching's 2003 paper had an ambiguous antecedent, readable as claiming that paper develops the
covering-question construction itself (verified against the primary source: it does not contain
"covering," `R_{j,k}`, or WCC anywhere) rather than the broader predecessor-density route it
actually develops. Restructured so the citation attaches unambiguously to the correct antecedent.

Several smaller precision fixes followed the by-now-familiar pattern of a claim stated more broadly
than its own justification supports: the Introduction's "shown to fail" for the Fourier approach
(only the naive uniform-cancellation version is shown to fail), the 1547 counterexample's stated
target (it refutes a specific per-witness converse, not the general "chain length is necessary for
survival" claim the surrounding prose named), Section 5.2's L1 diagnostic silently excluding the one
frequency proven to carry the largest magnitude, a genuine `T` notation collision between the
general and specialized exponential-sum setups, and Section 9's silence on where the l=22
`maxrun` computation actually lives. A handful of banned-vocabulary instances ("precise/precisely,"
"substantially," "not a meaningful test") were also caught and fixed, along with a self-contradictory
sentence ("the only increment... at which the budget does not increase").

Three findings were reviewed and deferred rather than fixed: Proposition 8's subsection placement
(organizational only, the content connection is already made in text), the independence-model and
phase-experiment population definitions (recurring since Round 4, needs a real model specification
this project has not written), and Empirical Result 13's Durfee-depth exposition (a real structural
clarity gap, judged lower value than the risk of restructuring it this late). All three carried
forward as open items, not silently dropped.

Recompiled clean (15 pages, 0 errors, 0 em-dashes, cite/bibitem check clean) and visually
re-verified. Full findings list above, C-101 through C-120, resolved (fixed, verified-no-change, or
deferred with a stated reason). Proceeding to Round 8.

## Round 8 (2026-08-09)

Same protocol, fresh context, PDF frozen (16 pages after this round's fixes; 15 going in). Codex
found 6 issues, Opus found 20, no critical or major mathematical error in either report; both
independently re-derived or reproduced most of the paper's content, including all 23 values of
`e(l)`, all of Table 2, every proof line by line, and every reference against its primary source.

The most consequential finding (Codex) was a real logical inconsistency introduced by Round 6's own
fix: the paper described corner-redundancy at the boundary width `W=2l` as "checked to fail" for
`l=7,...,13` in one sentence, then called it "an open question from `l=7`" a few sentences later.
Once checked to fail, a property is a settled negative fact, not an open one; what actually remains
open is Proposition 20's own converse, a different question the failure does not resolve either
way. This conflation had propagated into three separate places in the text (after Lemma 22, after
Proposition 23, and in the Discussion); all three fixed, with the genuinely open question (the
converse, plus corner-redundancy beyond `l=13`, which is truly unchecked) now stated separately from
the settled fact (corner-redundancy's failure at `l=7,...,13`).

The second consequential finding (also Codex) was a small but real proof-rigor gap in Proposition 23
(added this session, after Round 5): its "$\le$" direction applies Corollary 10 to "a maximal chain
of length `maxrun(H(l,j'+1))`," but Corollary 10 is stated only for chains of length at least 1; at
the proof's final telescoping step the relevant set is empty. Fixed by splitting into the trivial
empty case and the nonempty case where Corollary 10 applies as stated.

Opus caught a genuine LaTeX bug in Round 8's own recent text: Section 5.2's parenthetical about
excluded frequencies had an unbalanced parenthesis, with a full sentence break nested inside an
inner paren and only one closing paren for two opens, both a hard typo and unreadable prose. Fixed
by splitting into three clean sentences and verifying whole-document parenthesis balance afterward.

Both reviewers, independently, pushed the "model comparison and the plateau test measure the same
thing" observation (first noted in Round 4, C-60, as "not independent") further: since
`e(l+1)-e(l)` can only take one of two fixed values under the constant-rounding null, the two
diagnostics are not just correlated but reduce to the same binary fact restated in two languages.
Made explicit rather than just noting non-independence.

Several smaller precision fixes followed familiar patterns: an unexplained numeric constant (`3.9`
plateaus) turned out to be a directly derivable model quantity, not an empirical figure; `j*(l)-l`,
arguably the single integer most tied to whether `e(l)` could turn out linear, was never displayed
anywhere in the paper and is now one sentence near Table 1; Theorem 4's proof had a genuine, narrow
connecting-clause gap between the real-play construction and the abstract telescoping argument, now
bridged; and several range/attribution mismatches (Empirical Result 12 and 20's stated ranges not
matching what later propositions actually cover, a missing chapter number in a citation, a dropped
conditional tag, a paired dash, two tricolons in immediate succession).

One finding (Codex) was reviewed and only partly addressed: the three newest table values,
`j*(21),j*(22),j*(23)`, rest entirely on one Rust implementation, cross-checked against an
independent Python implementation only up to `l=20`. The text now explains the DP's internal
self-certification (finding the smallest full-coverage budget inherently checks both coverage there
and its absence one budget earlier) and states plainly that the `l<=20` cross-check is carried
forward by inference, not re-established, for the three new levels. An actual independent re-run at
`l=21`, which Opus estimated at hours rather than days, was not attempted this round; left as a
carried item rather than rushed into the same pass that just fixed a proof-rigor gap and a
parenthesis-balance bug, on the view that verification work deserves its own dedicated pass, not a
few spare minutes at the end of a text-fixing round.

Two items reviewed and deferred with reasons rather than fixed: the corner-redundancy open question
being posed at exactly `W>=2l+1` (checked directly against the paper's own text, this is an honest
description of what was checked, not a hidden methodological choice, so no change was made) and the
abstract's low sentence-length variance (a real Rule 5c point, but rewriting the abstract's rhythm
this late risks disturbing content already checked claim by claim across eight rounds).

Recompiled clean (16 pages, 0 errors, 0 em-dashes, parenthesis balance verified, cite/bibitem check
clean) and visually re-verified. Full findings list above, C-121 through C-140, resolved (fixed,
verified-no-change, partly addressed, or deferred with a stated reason). Proceeding to Round 9.

### Round 9 (Codex on `gpt-5.6-sol` + Opus 5 max effort, 2026-08-09)

Both reports read only the compiled `main.pdf`. Opus's report includes an explicit statement that
it re-derived and checked, line by line, every proof in Sections 4, 6 and 7, plus every numeric
claim reachable by direct enumeration; nothing there was found wrong. Both major findings this
round sit in Section 5's Fourier framing and Section 4's certification language, not in the
combinatorial core.

Codex's major finding: Table 3 and Theorem 5's proof describe rho_k as "self-certified... exactly"
via a matching adversary lower bound, but that lower-bound computation, like the policy search
itself, is restricted to actions `d<=40` (`mpg4.py`'s default `dcap`), not the full period `d<2*3^k`
the paper's own action-set derivation establishes (9,565,938 representatives at k=14). Restricting
the minimizer's options in a lower-bound computation can only inflate the value found, so "upper
bound equals lower bound" within the capped game does not, by itself, certify rho_k as the value of
the unrestricted game. Verified against the actual solver source before writing anything: `mpg3.py`'s
`build_actions` does cap at `d<=dcap`, and every stored certificate's policy stays far under the cap
regardless (max `d` used is 11 at k=14, against a cap of 40), which is suggestive but not a proof
that the cap is harmless. What the paper actually needs, Corollary 6's `j*(l)<=(9/8)l+33/2`, only
needs one certified legal, safe policy to exist, which a capped-search policy still is when read as
a policy in the full game that happens never to choose a move past `d=40`; that direction was never
at risk. Fixed by rewording the framing to state the upper bound's independence from the cap
explicitly and scoping the "exact" claim to the capped game, in both the paper and the repro repo's
section 4 README. A rigorous route to closing the gap for good exists (any move with `d` past
`rho+range(h)` is automatically safe for the lower bound too, so only a bounded prefix of the full
action set needs checking) but needs one solver change the stored certificates do not currently
support; logged as a follow-up rather than attempted this round.

Opus's major finding, independent of Codex's and caught by a different mechanism entirely: Section
5's opening motivation offers `sum_{t!=0}|S(t)| < T` as the natural sufficient condition for
covering, then spends three subsections on why it is hard to reach. It is not hard to reach. It is
impossible, for every `l`, `j`, `k`, and the four-line reason was sitting one page away the whole
time: every element of `R_{j,k}` reduces to `2^{a_0} mod 3`, so none of them is divisible by 3,
so `N(0)=0`, so `sum_t S(t)=0`, so `sum_{t!=0}S(t)=-T` exactly, so `sum_{t!=0}|S(t)|>=T` by the
triangle inequality, always. Verified independently before touching the proof: computed `S(t)` and
`N(0)` directly for six small `(l,j,k)` and confirmed the exact identity to machine precision, then
found the sharper, localized form of the same fact (`S(3^{l-1})+S(2*3^{l-1})=-T` exactly, so
`Re S(3^{l-1})=-T/2` exactly) and verified that too before writing it into the paper. Proposition 7
now states the impossibility and its sharper form directly; the old 1.585l threshold survives as an
a-fortiori remark (already worse than Corollary 6's bound, on top of resting on an unreachable
premise), not as a numbered claim in its own right, so nothing downstream renumbers. Proposition 9
(the `1/sqrt(3)` limit, formerly 8) is now framed as sharpening Proposition 7's exact bound to a
precise ratio, rather than independently re-deriving a refutation Proposition 7 already gives; its
statement also dropped an unused parameter `l` Opus flagged separately.

A third item does not originate with either reviewer's report but follows directly from Codex's
observation that the covering search's own `j_start.max(ell)` clamp (`src/main.rs`) never tries
`j<l`: nothing in the paper had actually ruled out some smaller budget covering at a given level,
only observed that none had been found to. Closed with a genuinely new result, not a caveat: a
reduction argument (coverage modulo `3^L` at budget `j` forces coverage modulo `3^j` for any `j<=L`,
since reducing a full set of units stays a full set of units) plus Table 1's own already-computed
strict rows rules out every `j<l` at every level `l=2,...,23`, proving `j*(l)>=l` outright rather
than only within the range the search happens to try. New Lemma 1, independently verified by direct
enumeration (`no_smaller_budget.py`, l=2..13, a third code path alongside the DP and `bruteforce`)
before being added, per the researcher's standing "verify a lead properly, not on a hunch" rule.
Adding a new numbered result before every other one in the paper renumbers everything after it; the
document contains no plain-text theorem-number references outside `\ref`, so this ripple is confined
to `CRITIQUE.md`, `OUTLINE.md` and the repro repo, not to `main.tex` itself.

Two Round-8-vintage sentences turned out to be wrong on inspection, both self-inflicted, both from
the same round: Section 2's claim that Proposition 2 "already rules out any bounded ceiling in
general" for `j*(l)-l` is false (a bounded ceiling makes `e(l)` grow linearly, comfortably above a
logarithmic floor, not below it), and Round 8's own strengthening of the model-comparison
observation to "the same question... asked in different words" overshot what the free-intercept OLS
constant model and the constant-rounding model actually share. Both reverted to accurate, narrower
statements. The plateau test's binomial parameter was also using a rounded intermediate (`3.9/19`)
instead of the exact `1-log_4(3)`, changing the reported p-value from 0.22 to 0.214; corrected while
in that paragraph.

The rest split evenly between the two reports: an abstract that stated `e(l)`'s growth-model
comparison in language ("statistically indistinguishable") that presupposes a sampling model a
deterministic sequence does not have, an "outside any sparse exceptional set" claim broader than the
one fixed threshold Section 5.2 actually checks, a self-contradicting Remark that first says a fit
"is not evidence of any specific limit" and then claims unstated evidence for one anyway, a
Poisson-model paragraph that assigns `e^{-108}` to an event that occurred and calls the result "no
single exponent characterizes it" instead of saying the model is falsified, an abstract sentence
that lets "verified at every level checked" read as covering the whole table instead of the `l=13`
stopping point it actually has, and a handful of smaller wording, labeling and citation-precision
points (Corollary 6 now states the explicit `33/2` instead of `O(1)`; a dangling reference to an
undefined "previous computational range" cut; the corner-redundancy paragraph's self-contradictory
width range reworded; the checkpoint/resume narration Round 8 deferred as C-139 removed). One
citation-accuracy claim (Meyerovitch-Young's arXiv identifier) was checked directly against the
arXiv abstract page and confirmed correct, recorded per Rule 8c since a critique raising a factual
claim deserves the same verification whether it turns out right or wrong. One item (a symbol-
collision audit across `e(x)`/`e(l)`, `S`/exponent-set `S`, `J`, and `m`) reviewed and deferred:
real, but a full audit risks touching load-bearing proof text this late in a ten-round loop for a
purely notational gain.

Recompiled clean (17 pages, up from 16 with the new lemma, 0 errors, 0 undefined references, 0
em-dashes, parenthesis balance 618/618, cite/bibitem check clean) and visually re-verified the
changed pages. Repro repo updated: `section2-jstar-computation/no_smaller_budget.py` and
`section5-exponential-sum/unreachable_criterion.py` added, both section READMEs and the
`section4-mean-payoff-game/README.md` resynced for the dcap scoping and the new constant. Full
findings list above, C-141 through C-157, resolved (fixed, verified-no-change, or deferred with a
stated reason). Two independent reviewers, at Round 9 of a ten-round cap, still each found a major,
previously unnoticed issue, by two different mechanisms (Codex from reading the solver's own
described action set against what the code actually searches; Opus from re-deriving Section 5's
opening identity from first principles rather than trusting the surrounding prose). The loop is not
converging yet. Proceeding to Round 10, the last round under the researcher's extension.
