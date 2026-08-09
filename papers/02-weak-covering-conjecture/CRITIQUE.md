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
