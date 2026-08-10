# Paper 02: Wirsching's Weak Covering Conjecture

## Scope

Reports this project's full body of work on Wirsching's 1998 Weak Covering Conjecture (WCC): the
exact computation of `j*(l)` (the smallest budget at which `R_{j-1,j}` covers every unit residue mod
`3^l`) extended past the previous paper's table, an analysis of the growth of
`e(l) := j*(l) - log_4(3)*l`, the best unconditional upper bound on `j*(l)` known to this project,
and a body of new structural results on the covering problem's "holdout sets" (GAP A: a fixed
5-round Claude+Codex+Fable push, 2026-08-08/09) -- a real theorem, a real falsification with an
explicit counterexample, and several further theorems and precisely-characterized open questions.
WCC itself is NOT resolved by this paper; every result below is labeled by what it actually is
(Rule 10b), and the paper says so plainly in the abstract and discussion.

## Results, precisely

1. **Computational extension.** Exact `j*(l)` for `l=1..23` (previous paper: `l=1..20`; this
   project's own extension: `l=21,22,23`, `experiments/E-001-jstar-fast/`, a Rust reimplementation
   of the original Python DP, independently validated against it for `l<=20`). `l=24` was attempted
   three times (2026-07-29 through 2026-08-07) and formally abandoned 2026-08-09 (researcher's
   decision): the last attempt died from an apparent OOM with no surviving kernel-log confirmation;
   not relaunched. The table stops at `l=23`.
2. **Growth-rate analysis of `e(l)`.** Model comparison (bounded / logarithmic / sqrt / slow-linear)
   over the `l=1..23` table (`experiments/E-002-*`), AIC/BIC and a plateau-frequency test; status and
   exact current p-values/dAIC to be pulled fresh from `E-002`'s README before drafting (the last
   recorded figures, `l<=23`, are in `HYPOTHESES.md`'s H-001 row -- confirm they're still current,
   nothing has changed them since 2026-07-30). `e(l)` is proven unbounded via a pigeonhole argument,
   `e(l) >= (1/2)log_4(l) + O(1)` (this project's own result; locate exact source note before citing).
3. **Best unconditional upper bound**: `j*(l) <= (119/104)l + O(1) ~ 1.1442*l`, via a mean-payoff-game
   reformulation of the covering budget (`experiments/E-003-mpg-cylinder/`, `rho_14=9/8` confirmed
   2026-08-01), no Fourier/character-sum machinery -- this project's own original result, not
   borrowed. Should be stated as a clean theorem with a full proof sketch; the actual MPG certificate
   construction needs re-reading before writing this section (notes/H-003.md, the mean-payoff-game
   rounds) to get the proof outline right rather than just citing the bound.
4. **GAP A: why the natural Fourier approach fails, unconditionally.** The exponential sum `S(t)`
   (the Fourier dual of the covering-count problem) is shown to admit no viable magnitude-based proof
   strategy, via three independent, mutually-reinforcing findings: (a) a hard ceiling,
   `j >= 2*log_4(3)*l ~ 1.585*l`, on anything provable by uniform square-root-type cancellation --
   *worse* than the already-proven `1.1442l`, ruling the whole naive approach out cleanly; (b) even
   after removing sparse "major arc" resonances, the Fourier `L^1` mass is dominated by an
   exponentially numerous population of near-average-magnitude coefficients (over 97% of the mass at
   `l=18`), ruling out any sparse-exceptional-set repair; (c) a direct, exact-arithmetic finding that
   coverage failures ("holdout" residues) sit at extremal, highly non-generic conductor-depth cells no
   averaging or moment method can see. A real, checked, on-point connection to Terence Tao's 2011
   blog post on Littlewood-Offord theory and powers of 2 and 3 is part of this section (his own words:
   this class of obstruction needs transcendence theory or new techniques, not existing tools).
5. **A real theorem on the covering problem's holdout sets.** Writing `H(l,j)` for the units mod
   `3^l` NOT covered by `R_{j-1,j}`:
   $$H(l,j+1) \subseteq 2H(l,j) \cap 4H(l,j)$$
   (exponent-shift maps), with corollaries: chain contraction (a doubling chain
   `x,2x,4x,...` of length `t` in `H(l,j+1)` pulls back to length `t+1` in `H(l,j)`) and the
   run-length bootstrap `j*(l) <= j + maxrun(H(l,j))` for `j>=l`, found empirically EXACT (equality)
   at every computed `(l,j)` with `j>=l+1`. Independently re-derived and verified from scratch by
   Claude before being trusted (this session), separately from the two AI legs that found it.
6. **A real falsification, with an explicit counterexample.** The natural stronger conjecture (a
   uniform, bounded-cost local witness-repair rule, this project's own prior hypothesis H-012) is
   false: explicit witness-level counterexamples at two tested budget transitions, and a genuine
   counterexample to even the weaker "strong converse" reading of result 5
   (`1547 in 2H(7,8) cap 4H(7,8)` but `1547 not in H(7,9)`, independently reproduced).
7. **Further exact theorems on the holdout family** (arising while pursuing H-013/H-014): the
   last-holdout set is provably `== 1 mod 3`; an exact near-extinction bijection
   `H(l,j*-1) = 2*{x in H(l,j*-2): x==2 mod 3}`; cross-level inheritance of last holdouts is provably
   `x4`-only; a two-class mod-9 bound `H(l,j*-1) mod 9 subset {4^J, 4^(J+1)}`. The single remaining
   piece of the mod-9 law (excluding `4^J`) and the "corner-redundancy" lemma needed for the
   bootstrap's converse direction are both precisely stated, unproven, and explicitly NOT pursued
   further by this project (researcher's decision, 2026-08-09) -- reported as genuinely open questions
   for the field, not left vague.

## What this paper does NOT claim

WCC itself; the exact growth rate of `j*(l)` or `e(l)`; any bound below `1.1442l`. Every "in-progress
research direction" above is presented as exactly that, with the specific missing lemma named, not
as "future work" boilerplate.

## Source hypotheses

H-001 (computational extension, in-progress -> feeds this paper directly), H-002 (secondary
entropy-count bridge, real quantified gap, likely a brief mention only, not a main result -- confirm
during drafting whether it's in scope at all), H-003/GAP A (backlog as of 2026-08-09, this paper is
its write-up), H-011 (closed-inconclusive), H-012 (closed-refuted), H-013 (backlog, partial
theorems), H-014 (backlog, partial theorems + equivalence result). Full derivation history:
notes/H-001.md, notes/H-002.md, notes/H-003.md (very long; the 2026-08-08 section onward is the GAP
A push), notes/H-013.md, notes/GAP-A-round4.md, notes/GAP-A-round5*.md.

## Structure (draft, revisit once section 2's actual proof text is drafted)

1. Introduction: WCC's statement, its place in Wirsching's 1998 book, relation to the prior paper's
   Section 7 computation, this paper's actual contributions listed plainly.
2. The computation: `R_{j,k}`, `j*(l)`, the `l=1..23` table, methodology (Rust reimplementation,
   validation against the original), what changed for `l=21-23` (swap-assisted, timings), why `l=24`
   was abandoned.
3. `e(l)`'s growth: model comparison, current statistical verdict, honest uncertainty.
4. The mean-payoff-game bound: statement, proof sketch, `1.1442l`.
5. GAP A: the exponential sum, the three-wall impossibility result, the Tao connection.
6. The holdout-set theorems: Theorem 1, the bootstrap, the falsification/counterexample, the
   mod-3/mod-9 laws.
7. Discussion: what's open, precisely (the two named lemmas), why this project stops here, what a
   human number theorist could do with this (per Rule 10, citation-maximizing framing: make the open
   questions genuinely inviting and precise, not a vague "more work is needed").
8. Code and data availability (Rule 12: dedicated repro repo, `https://github.com/faculdade/
   weak-covering-conjecture`, confirmed to exist, not yet populated). **DOI archival plan
   (researcher's explicit instruction, 2026-08-09), same flow as paper 01/H-006**: once the repo is
   fully populated and stable (no further planned changes), create a GitHub Release; Zenodo is
   already linked to the researcher's account, so it should mint a DOI automatically the same way
   it did for `faculdade/wirsching-conjecture3-proof` (`doi:10.5281/zenodo.21854549`) -- but
   re-verify per-repository the Zenodo GitHub toggle is on for this specific repo before assuming
   the webhook fires (paper 01's own experience: account-level linking was NOT sufficient by
   itself, a repo-level toggle at zenodo.org/account/settings/github/ was also required). Cite the
   DOI in this section once minted, not the bare GitHub URL.

## Status

- [x] Outline drafted, 2026-08-09, per the researcher's explicit request and confirmed scope
      (include the GAP A results in this paper, not a separate one).
- [x] E-002 reconfirmed, 2026-08-09: reran `experiment.py` directly, every number matches the
      README exactly (dAIC=16.09, dBIC=15.45, plateau p=0.0426 pooled / ~0.22 tail-only). This IS
      the final dataset (l=1..23) since l=24 is formally abandoned; nothing left to update.
- [x] Mean-payoff-game construction re-read and spot-verified, 2026-08-09: reran `mpg4.py 3 4`,
      matches the README table exactly (`rho_3=2, C_3=5, rho_4=5/3, C_4=19/3`). Proof sketch for
      section 4: `j*(l)` reformulated as a full-information game (state = unit `z`, legal cost `d`
      iff `2^d z==1 mod 3`, transition `T_d(z)=(2^{d+1}z-2)/3`); restricting the policy to see only
      `z mod 3^k` gives a window-k mean-payoff-game relaxation (adversary picks the hidden next
      3-adic digit), whose value `rho_k` gives `j*(l) <= rho_k*l + C_k`, both exact rationals,
      self-certified via matching min-max certificates (Howard strategy improvement); `rho_k` is
      non-increasing in `k`, `rho_13=119/104` is the best computed. **IMPORTANT for citation
      (Rule 10, don't overclaim)**: the general technique (covering-type problems as mean-payoff
      games) is NOT new -- Ehrenfeucht-Mycielski 1979, with a close precedent in Meyerovitch & Young
      (arXiv:2603.21449, 2026, covering radius of sofic shifts). What's new here is the application
      to `j*(l)`, not the framing; cite both precedents, don't present the technique itself as a
      contribution. Also: only `j*(l) <= rho_k*l+C_k` is proven; the reverse direction
      (`inf_k rho_k <= limsup j*(l)/l`, i.e. `rho_k -> log_4(3)`) is an unproven extrapolation, an
      earlier internal draft wrongly asserted it as proven and was corrected -- do not repeat that
      mistake in the paper.
- [x] Dedicated reproducibility repository (Rule 12): `https://github.com/faculdade/weak-covering-conjecture`,
      confirmed to exist 2026-08-09 (`curl` 200, `gh repo view` succeeds). Not yet populated -- no
      code committed there yet; do this before section 8 claims anything is "available" in it.
- [x] arXiv category confirmed: math.NT, 2026-08-09.
- [x] Author/venue/language: same as paper 01 (Renato Augusto Tavares, UFG), English-first
      (main.tex written 2026-08-09, researcher's explicit request); pt-BR deferred to a future
      explicit request (Rule 5).
- [x] Prose drafted, 2026-08-09: main.tex written in full (9 sections + bibliography), compiles
      clean (8 pages, 0 errors, 0 overfull-hbox, 0 undefined refs, 0 em-dashes), all 8 pages
      visually verified page-by-page. Fixed one Rule 12 overclaim found during visual QA: Section 9
      originally stated every computational claim is backed by a script in the repo; corrected to
      state the repo is reserved and will be populated before submission, since it is not yet
      populated (DATA_REPO.md).
- [ ] PDF-only blind critique loop (Codex + Opus 5 max effort as of round 3, replacing Fable per
      researcher's explicit instruction), researcher's explicit request 2026-08-09: round 1 complete
      and fixed (18 findings, 3 critical). Round 2 complete and fixed (15 findings, 4 critical).
      Repro repo populated (Rule 12) between rounds 2 and 3:
      `https://github.com/faculdade/weak-covering-conjecture`, six section-mapped folders, every
      claim re-run and confirmed. Round 3 complete and fixed (13 findings, 4 critical -- the most
      serious was a claim in the mean-payoff-game section that had survived two prior rounds while
      being outright false, caught by Codex via a two-line numeric counterexample; the correct
      correspondence was re-derived with an outside consultation and independently verified by
      computation, 780 cases, before being written in). See CRITIQUE.md for full findings.
      Recompiled clean, 12 pages. A handful of moderate/minor items carried to round 4 (statistical-
      inference-flavored language around the plateau p-value, an unspecified independence model, one
      empirical result upgradeable to proven). The title's "a proven bound" was flagged by both
      round-3 reviewers as an overclaim; researcher confirmed conditional language, title changed to
      "a conditional bound" (2026-08-09).
      Round 4 complete and fixed (15 findings, 2 critical -- both self-inflicted, one from Round 3's
      own fix having the diagonal/off-diagonal direction of Proposition 8 backwards, the other a
      1000x units bug in the occupancy-mean figure inherited from `notes/H-003.md`, now corrected at
      its source too). Closed two real proof gaps rather than just prose: existence of `j*(l)` for
      every `l`, used from the Introduction on but never proven, now has an unconditional proof
      (new Proposition 15, `j*(l) <= 2*3^(l-1)-1`); the one-step width identity used since Round 2
      to derive the last-holdout parity theorem, asserted "exact" with the derivation explicitly
      omitted, now has a full three-case proof (new Lemma 14). Both verified computationally before
      being written in. One Opus finding (a claimed modulus typo) was checked and found false per
      Rule 8c, recorded as such rather than silently dropped. See CRITIQUE.md for the full list.
      Recompiled clean, 12 pages, 0 errors, 0 em-dashes, visually re-verified page by page.
      Three researcher decisions resolved 2026-08-09 before Round 5: (1) bibliography widened,
      three new references read and verified against primary sources (Rule 11) before citing --
      Wirsching's own 2003 follow-up on positive predecessor density (directly on-topic, cited in
      the Introduction), Tao's 2019 "almost bounded values" paper, and Krasikov-Lagarias's
      difference-inequality density bounds (both cited in the Discussion as adjacent, distinct
      approaches); (2) Section 5.3's "cell/local intensity/conductor-depth" language formalized --
      and in the process, a producer-found error surfaced and was fixed (CRITIQUE.md C-62): the
      "e^-23 to e^-100" figure did not reproduce under the only natural reading of the informal
      language it came from, direct recomputation from the exact histogram giving `e^-2` to
      `e^-108` instead. Fixed with a precise definition and the corrected range, backed by a new
      script now in the reproducibility repo (`section5-exponential-sum/local_intensity.py`);
      (3) the l=24 attempt narration kept as is (researcher's explicit choice, real circumstantial
      detail, Rule 9's exception to Rule 5c's usual ban on process narration). 13 pages now.
      Several moderate/minor items carried to Round 5 (Table 3's missing sigma_k/h_k, the cost-1
      repair rule's formal statement, the independence model's formal definition, Table 2's fitted
      slope, the L1-mass computation's exclusion of `t=3^(l-1)`, the mod-9 result's thin l-range,
      ER18's upgradability).
- [x] **Round 5 complete (2026-08-09), the final round under the researcher's 5-round cap.**
      Codex + Opus 5 max effort, fresh context, PDF frozen for both runs. Neither reviewer found a
      critical error; both independently verified large parts of the paper from scratch (Opus
      recomputed all of Table 1/2, several theorems by hand, and all 7 references against primary
      sources) and confirmed the unconditional core sound. 17 findings fixed (2 major
      self-inflicted: the Krasikov-Lagarias citation was mischaracterized despite the correct
      primary-source data sitting in context from the same session's own bibliography work, and the
      reproducibility repo's README still carried the pre-Round-3 title and numbers stale by two
      rounds -- both caught independently by both reviewers, both fixed in the repo, not just the
      paper). Also fixed: Corollary 10's missing `j>=l` hypothesis (verified Theorem 9 fails
      without it), the Introduction's central equivalence claim narrowed to its actually-proven
      direction, a genuine validity boundary in Empirical Result 12 (verified computationally,
      not merely an unchecked range), an undisclosed six-budget gap from the covering threshold in
      Section 5.2, a degenerate boundary case in Section 5.3's just-added local-intensity range, and
      a plateau test computed under an already-refuted null. Two credible new-math leads from Opus
      (a corner-redundancy tightness proof, an Empirical Result 18 upgrade) were deliberately left
      unadded: this is the last round under the cap, so any new mathematics here ships with no
      further review, a different risk category from fixing what a fresh reviewer just checked by
      hand. One Opus finding checked out as not a real overclaim (Section 9's data-availability
      text), recorded as such rather than silently accepted or dropped. Full list in CRITIQUE.md.
      Recompiled clean, 13 pages, 0 errors, 0 em-dashes, visually re-verified page by page.
      **The critique loop is now closed** (5-round cap reached). Per Rule 8/15, Round 5's own fixes
      are unreviewed by any fresh pair of eyes; the mandatory pre-publication check (a genuinely
      independent model, or the researcher) still needs to run before submission, whenever that is
      decided -- this loop does not substitute for it.
- [x] **Post-loop verification, researcher-directed (2026-08-09, Rule 8e), the two leads left
      unadded above.** Both worked out from scratch and verified before being trusted (Rule 11);
      the first proof attempt at corner-redundancy-implies-tightness had a real circularity gap
      (an unjustified width bound), caught and fixed with a cleaner single-step-recursion argument
      before being written into the paper. Corner-redundancy implies Corollary 11's bootstrap is
      tight (new Proposition 22), unconditional at `l=3..13`. The mod-9 two-class containment is
      unconditionally provable from Theorem 16's own proof (new Proposition 18), splitting off a
      narrower Empirical Result 19 (excluding the lower class, still open) whose verified range
      also extended from `l=3..9` to `l=3..16`. Abstract, Empirical Result 12, and the Discussion
      updated to match (Rule 8b). 14 pages now. Verification scripts added to the reproducibility
      repo, all four README files resynced a third time. This is new content added after the
      5-round cap closed; it does not reopen the loop, and the mandatory pre-publication
      independent check above still applies to it.
- [x] **Researcher extended the critique loop to 10 rounds (2026-08-09)**, explicitly to test
      convergence, superseding the earlier 5-round cap.
- [x] **Round 6 complete (2026-08-09), first round under the 10-round extension**, and the first
      round to review Propositions 18/22 (added post-Round-5). Codex + Opus 5 max effort, fresh
      context, PDF frozen. Both independently confirmed the two new propositions are sound (Opus
      reimplemented the paper's objects from scratch and reproduced every number checked). 21
      findings fixed, no critical/major proof-validity errors. The most serious (Opus): "corner-
      redundancy is known to fail at W=2l" was backwards for l=3,4,5,6, where it actually holds;
      fixed, and the correction let Proposition 22's mechanism extend to prove Proposition 20's
      boundary case (j=l+1) at those four levels, a genuine strengthening neither reviewer proposed
      directly. ER13 (cost-1 repair rule) finally given its actual formal definition after being
      flagged as under-specified in three consecutive prior rounds, by reading the underlying script
      directly. One producer-found issue: Rule 5c's antithesis budget (2 per document) had grown to
      13 instances across Rounds 3-6's additions, uncaught since Round 1; cut back to 2. Same
      corner-redundancy-boundary error found and fixed in the reproducibility repo's own README.
      Recompiled clean, 15 pages, 0 errors, 0 em-dashes, visually re-verified. Round 7 next.
- [x] **Round 7 complete (2026-08-09).** Codex + Opus 5 max effort, fresh context, PDF frozen. 26
      findings total (6 Codex, 20 Opus), no critical or major flaw in any formal proof; both
      reviewers independently re-derived or reproduced most of the paper's content, including all
      references against primary sources. Most substantive (Codex): Section 5.3's phase-scramble
      statistic was described as deviation from the global mean, but the underlying script
      (verified directly) actually measures imbalance among the three lifts of each parent
      residue, a different quantity with the same numerical value; fixed, along with the
      overstated "coverage failure is decided by phase structure" conclusion drawn from it.
      Second most substantive (Opus): the near-extinction bijection's forward direction turned out
      provable directly from Theorem 9 + Theorem 16 (same pattern as the post-Round-5 upgrades),
      re-derived, verified computationally, and split into a new Proposition 17 plus a narrower
      Empirical Result 18. A citation-antecedent ambiguity in the Introduction (checked against
      the primary source) was also fixed. Several smaller precision fixes (the 1547
      counterexample's actual target, a `T` notation collision, Section 5.2 excluding the one
      frequency proven largest, Section 9's silence on the l=22 maxrun tool, banned vocabulary,
      a self-contradictory sentence). Three items reviewed and explicitly deferred with reasons
      (Proposition 8's placement, the independence-model/phase-experiment specification, ER13's
      Durfee-depth exposition). Recompiled clean, 15 pages, 0 errors, 0 em-dashes, visually
      re-verified. Reproducibility repo updated (new verification script, all READMEs resynced).
      Round 8 next.
- [x] **Round 8 complete (2026-08-09).** Codex + Opus 5 max effort, fresh context, PDF frozen. 26
      findings total (6 Codex, 20 Opus), no critical or major mathematical error in either report.
      Most consequential (Codex): Round 6's own fix had left a real inconsistency, calling corner-
      redundancy at W=2l both "checked to fail" (l=7..13) and "open" in the same breath, in three
      separate places in the text; fixed throughout, distinguishing the settled negative fact
      (checked to fail, l=7..13) from what is genuinely still open (the converse itself, and
      corner-redundancy beyond l=13). Second (also Codex): a real proof-rigor gap in Proposition 23
      (this session's own addition) -- its <= direction applied a corollary stated only for chains
      of length >=1 to a possibly-empty chain at the proof's final step; fixed by splitting the
      empty and nonempty cases. Opus caught a genuine LaTeX bug in the paper's own most recent text:
      an unbalanced parenthesis in Section 5.2, both a hard typo and unreadable prose; fixed and
      whole-document paren balance verified. Both reviewers pushed the "model comparison and
      plateau test are the same question" observation (first noted Round 4) from "not independent"
      to "literally the same binary fact," now stated that way. Several precision fixes (an
      unexplained numeric constant traced to its actual formula, j*(l)-l displayed for the first
      time, a genuine connecting-clause gap in Theorem 4's proof, range/attribution mismatches, a
      paired dash, two tricolons in a row). One finding partly addressed: the l=21,22,23 table
      values rest on one implementation with no independent cross-check beyond l=20; the text now
      explains the DP's internal self-certification and states the l<=20 cross-check is carried
      forward by inference, not re-established -- an actual independent re-run at l=21 was not
      attempted this round, left as a carried item for its own dedicated pass rather than rushed.
      Two items reviewed and deferred with stated reasons. Recompiled clean, 16 pages, 0 errors,
      0 em-dashes, parenthesis balance verified, visually re-verified. Round 9 next.
- [x] **Round 9 complete (2026-08-09).** Codex + Opus 5 max effort, fresh context, PDF frozen. Opus
      reports re-deriving and checking every proof in Sections 4, 6, 7 line by line plus every
      numeric claim reachable by direct enumeration: nothing wrong there. Two independent major
      findings instead, both in Section 5's framing and Section 4's certification language. Codex:
      Table 3/Theorem 5's "self-certified exactly" language for rho_k rests on an adversary
      lower-bound computation restricted to actions d<=40 (`mpg4.py`'s dcap), not the full period
      the paper's own construction defines; verified against the actual solver source before fixing;
      reworded to scope the "exact" claim to the capped game while confirming the paper's actual
      proven result (Corollary 6's conditional bound) never depended on it. Opus, independently and
      by a different mechanism: Section 5's opening offers `sum|S(t)|<T` as a criterion "hard to
      reach," when it is provably unreachable for every l,j,k (four lines: every element avoids
      residue 0 mod 3, forcing sum_{t!=0}S(t)=-T exactly); verified computationally before rewriting
      Proposition 7 (kept in place, no renumbering) to state the impossibility and a sharper
      localized identity directly, with the old 1.585l threshold demoted to an a-fortiori remark. A
      third result, prompted by but not stated in either report: the covering search's own `j>=l`
      clamp never rules out smaller budgets, closed for real with a new Lemma (No smaller budget
      covers, l=2..23) rather than left as a caveat, independently verified by direct enumeration
      before being added; this is the paper's first numbered result, so everything after it shifts
      by one (no plain-text theorem numbers exist in main.tex, so the ripple is confined to
      CRITIQUE.md, OUTLINE.md and the repro repo). Two Round-8-vintage errors found and fixed, both
      self-inflicted: Proposition 2 does not rule out a bounded j*(l)-l ceiling (a bounded ceiling
      makes e(l) linear, not constant, comfortably above a log floor), and Round 8's own
      strengthening of the model-comparison claim to "the same question... asked in different
      words" overshot; reverted to "not independent." A dozen smaller precision and overclaim fixes
      (statistical language on a deterministic sequence, "any sparse exceptional set" narrowed to
      the one threshold checked, a self-contradicting Remark, a Poisson model reported as "no single
      exponent" instead of falsified, Corollary 6's O(1) replaced by the explicit 33/2, a dangling
      reference, the binomial test's rounded parameter corrected). One citation check (arXiv id)
      verified correct, no change. Recompiled clean, 17 pages (new lemma), 0 errors, 0 em-dashes,
      parenthesis balance verified, visually re-verified. Repro repo: two new verification scripts,
      three READMEs resynced. Two majors from two independently-reasoning reviewers at Round 9 of
      10 means the loop has not converged; Round 10 next.
- **Stopping rule replaced (2026-08-09).** Researcher: stop only after 3 consecutive rounds with
      zero critical/major/moderate findings and minor findings under 3, tracked in CRITIQUE.md's
      new tally table. No fixed round cap. Reason: criticals had already zeroed since Round 5, but
      majors kept recurring on a "no findings from either reviewer" criterion unlikely to ever fire,
      since substantial edits each round reseed fresh surface regardless of correctness.
- [x] **Round 10 complete (2026-08-09).** Codex + Opus 5 max effort. Codex's sandbox failed twice
      (bubblewrap/network-namespace error) before a third attempt succeeded hours later, by which
      point several Opus-driven fixes were already applied, so Codex reviewed a mid-round PDF, not
      the frozen Round 9 one; recorded as a protocol slip, findings counted toward Round 10
      regardless. Combined tally: 0 critical, 1 major, 8 moderate, 8 minor -- not clean, streak
      resets to 0. Major (Codex): the l=21-23 table extension has no independent certification
      beyond "carried forward by inference," deferred twice before; closed with an actual
      from-scratch Python re-implementation (native bignum bitsets), validated exactly against
      Table 1 through l=17, launched at l=21 in the background rather than deferred a third time;
      Section 9 now pins the repro repo's commit hash instead of just its URL. Both reviewers
      re-derived every proof (Lemma 1 through Proposition 24) a second consecutive round with
      nothing found wrong; every finding sits in Section 3's and Section 5's numerical or
      statistical framing. Opus: the paper's own recorded script output already contradicted
      Section 5.2's exceptional-mass figures (12.2/99.7%, not the printed 132/97%, an order of
      magnitude off and understating the paper's own evidence); the "dyadic rationals" framing for
      the largest-magnitude frequencies was wrong (they cluster by 3-adic valuation, not dyadic
      proximity, confirmed by independent FFT computation); a Round-9 addition mislabeled `t=3^(l-1)`
      as dyadic; the phase-scramble ratio was described as "over unit z" when the script computes it
      over all z; several smaller wording and pointer fixes. Codex, beyond the major: proved
      computationally that the plateau test's null was already impossible on the tail alone (the
      13-step total change is confined to {10,11} under any constant-rounding model, but the
      observed change is 12), replacing a p-value against a dead null with a deterministic
      refutation; a real inconsistency in how the mean-payoff certificate's checked condition was
      described; "falsifies the Poisson model outright" walked back to "discarded on that basis"
      without swinging past Round 9's own earlier correction of the same sentence; the phase-scramble
      null's failure to preserve already-proven constraints; three Discussion sentences overstating
      what Section 5 established, the third round a Section 5 overclaim recurred in a different
      spot; AIC/BIC/LOOCV's missing no-sampling caveat; this round's own valuation-ordering claim
      needing a scope and the identity behind it. Recompiled clean, 17 pages, 0 errors, 0 em-dashes,
      parenthesis balance verified, antithesis count back to the 3-item baseline, visually
      re-verified. Repro repo: section3 README resynced for the dropped p-value. l=21 independent
      recomputation still running at round's end; result to follow.
- [x] **Round 11 complete (2026-08-09).** First round under a frozen PDF snapshot (avoids Round 10's
      race). No critical or major findings from either reviewer -- the first round since Round 8
      without a major. Third consecutive round both reviewers re-derived every proof with nothing
      wrong; Opus additionally recomputed most numeric claims from scratch, including an independent
      mean-payoff value iteration over the full uncapped action set at k=3..6, matching Table 3
      exactly. Findings converge on one theme across both reviewers: text stating a computation more
      precisely than the computation establishes. Most consequential: Opus found Round 10's own
      "ordered by valuation" fix was itself still false (explicit counterexamples: interleaved
      valuation classes at l=10, a primitive frequency exceeding a valuation-8 one at l=12),
      independently verified before rewriting into a properly hedged "correlates... but loosely"
      statement; Codex flagged the same passage's missing parameters from a different angle. Both
      reviewers separately caught that the phase-scramble diagnostic's conclusion was largely a
      corollary of a theorem proved two sentences earlier; fixed by stating the exact accounted-for
      factor (sqrt(3/2)) and the residual (~2.5) that theorem doesn't explain. Poisson model
      post-selection caveat added without reversing the conclusion. Several stale cross-references
      from earlier rounds' own edits, and small scoping fixes. l=21 independent verification still
      running (j=21, j=22 confirmed against Table 1 so far). Recompiled clean, 17 pages, 0 errors,
      0 em-dashes, parenthesis balance verified, antithesis at baseline. Combined tally 0/0/7/6: no
      criticals or majors for the first time, but moderate is far from the zero the stopping rule
      needs. Round 12 next.

- [x] **Round 12 complete (2026-08-09).** Frozen PDF snapshot again. Both reviewers independently
      found the same most-severe issue by different routes: Round 11's own fix at the Fourier-
      maximality locus (Section 5.2, "Proposition 8's exact bound already forces it") was itself a
      false, logically invalid inference, a lower bound does not establish maximality. Codex gave an
      explicit numerical counterexample and rated it moderate; Opus found the same counterexample
      independently, rated it major, and noted an internal contradiction with two other sentences in
      the same subsection. Third consecutive round a fix at this exact locus needed a further fix
      (Round 10, then Round 11, now Round 12); fixed by stating the bound is only a lower bound, no
      claim of maximality, with the counterexample inline and the "top pair is largest" claim
      rescoped to only the three levels actually checked. Deletion-first discipline adopted at this
      locus going forward. Remaining findings (all Opus except one rejected Codex minor): a citation-
      attribution ambiguity ([2] vs [1] for the covering-question construction); Theorem 5's caption
      citing a stronger hypothesis (full equality) than its proof uses (one direction only); an intro
      summary dropping a conditionality caveat the abstract carries; an ambiguous lift-construction
      clause in Section 4; a holdout-rarity/phase-scramble pairing, in both the body and the abstract,
      overstating what the magnitude-only holdout diagnostic shows about phase; a Rule 12 discrepancy
      between Section 9 (l=21) and Empirical Result 13 (l=20) resolved by running the verification
      script directly, which showed Section 9 was right and Empirical Result 13 undersold what was
      actually checked. One re-flagged, already-verified-correct detail (the swap-file capacity) was
      re-confirmed against `lsblk` rather than assumed. Fourth consecutive round both reviewers
      re-derived every proof with nothing wrong. Opus flagged, and this round records honestly, that
      its review is not strictly PDF-only (project context is visible to it as a subagent); it
      labeled context-derived claims itself, but Round 13's prompt should say so explicitly. l=21
      independent verification still running; acceptance criterion (j=24 fails, j=25 covers,
      matching Table 1) predeclared in CRITIQUE.md before the result lands. Recompiled clean, 17
      pages, 0 errors, 0 em-dashes, parenthesis balance verified, antithesis at baseline. Combined
      tally 0/1/1/8: the round's only major was in text Round 11 itself wrote, not the paper's
      original content; streak resets to 0. Round 13 next.

- [x] **Round 13 complete (2026-08-09).** First round run under the researcher's standing
      instruction to loop automatically until the stopping criterion is met. The l=21 independent
      verification (running since Round 10) completed: `j*(21)=25` confirmed exactly, matching the
      predeclared criterion; Section 2 now states this explicitly, with `l=22,23` honestly labeled
      inference-only. Both reviewers independently caught the same issue in Section 5.3's phase-
      scramble diagnostic: the `sqrt(3/2)` "residual factor near 2.5" claim compared two ratios
      normalized against non-comparable populations (Codex via a Parseval argument, moderate; Opus
      by constructing a null that actually respects the zero-off-units constraint and showing the
      printed number survives under it, minor). Independently re-verified by building a fresh
      implementation of that constrained null (triples of primitive frequencies forced to sum to
      zero, a rotation-plus-reflection construction derived and checked by hand before coding):
      matched a predeclared acceptance band exactly (`max/RMS_all` mean `6.35`, residual `2.49`).
      Section 5.3 rewritten to cite the constructed null instead of the naive RMS rescaling; script
      checked into the repro repo. Codex's second moderate (l=21-23 lack independent certification)
      resolved at l=21 by the verification above. Four more minor fixes (an overclaimed "typical"
      characterization, a "needs the identity" necessity overclaim, a redundant preserved-property
      list item, an imprecise `1547` counterexample gloss fixed with a minimal mechanism-free
      rewording rather than an unverified taxonomy, two citation-precision items). Opus also caught
      a repository-only `T`-value typo (unrelated to the paper's own correct figure), fixed. Fifth
      consecutive round the combinatorial core re-derived clean; every citation now primary-source
      verified. Two Rule 8e leads registered as H-015, H-016 (not pursued, GAP A/WCC inactive).
      Recompiled clean, 18 pages (up from 17), 0 errors, 0 em-dashes, parenthesis balance verified.
      A process note: the antithesis-count tracking in earlier rounds undercounted due to a
      single-line grep missing line-wrapped instances; true pre-existing count is 6, not the
      previously-tracked 3; one new instance this round was caught and reworded. Combined tally
      0/0/2/6: no criticals or majors, but 2 moderates keeps the streak at 0. Round 14 next.

- [x] **Round 14 complete (2026-08-10).** Both reviewers, asked to look hard at Round 13's freshly
      written constrained-null passage, independently found the same issue: "independently for each
      triple" is ambiguous and, read literally, breaks the conjugate-symmetry relation the paper
      relies on elsewhere. Opus built three explicit null variants and showed only the correct,
      conjugate-paired one reproduces the printed numbers; checked the actual script directly rather
      than trusting either report (conjugate-symmetry error exactly `0.0`, imaginary part at
      floating-point noise) and found the code was already right, only the prose was ambiguous.
      Fixed the wording and added permanent self-checks to the script's own output. Opus's second
      finding: the "coarse local intensity does not by itself pick out which residues resist" claim
      outran its own support (the body's only quantitative check disclaims itself two sentences
      before "shows" reasserts it at full strength three times); ran the aggregate check the paper
      never ran (expected-hole-count under its own model, leave-one-out, finest depth) and
      independently reproduced Opus's exact figures before touching the paper, confirming the model
      predicts as many or more holes than observed at that depth. Checked and rejected one of Opus's
      own stronger claims (lowest-intensity residues always covered) as false at 2 of 3 levels
      tested. Softened the overclaiming language in all three locations it appeared (abstract, body,
      Discussion); added a new script to the repro repo. Three more minor fixes (a near-circular
      proof step in Lemma 1, an overstated citation match for [6], an abstract scoping gap) and one
      rejected finding (already addressed at the same locus in Round 13). Sixth consecutive round
      the combinatorial core re-derived clean. Recompiled clean, 18 pages, 0 errors, 0 em-dashes,
      parenthesis balance verified, antithesis at the corrected 6-item baseline. Combined tally
      0/0/2/4: no criticals or majors, but 2 moderates keeps the streak at 0. Round 15 next.

- [x] **Round 15 complete (2026-08-10).** This loop's first major finding since Round 11. Codex
      caught that Round 14's own fix had smuggled in a new overclaim (Parseval governs the RMS, not
      the maximum, but the text said "so the maximum" too); fixed by stating the max increase is an
      empirical property of the 30 trials, not a deduced consequence. Opus found something more
      consequential: the claim that the phase-scramble diagnostic shows "phase structure beyond"
      local intensity was unsupported, since neither null tried so far carried any local-intensity
      information at all. Opus built a third null (each parent's exact count, split multinomially
      among its three lifts, zero phase information) and found it reproduces or exceeds the actual
      statistic in about 83% of trials. Independently reproduced this before touching the paper
      (matched Opus's figures almost exactly) and added it to Section 5.3 as new, verified content,
      rewriting the "phase structure beyond that" claims in the abstract, body, and Discussion to
      say plainly that the departure does not on its own establish anything about phase. Two more
      moderate fixes in the same section (a dangling reference to draft history, deleted; an
      aggregate-vs-rank conflation, separated into two explicit questions with the honest fit-quality
      caveat) and one in Section 7 (a "tracks within about one unit" claim that turned out nearly
      vacuous since the tracked quantity only takes two values total, verified against this
      project's own H-001 data before fixing). Four more minor items. Seventh consecutive round the
      combinatorial core re-derived clean. Recompiled clean, 19 pages (up from 18), 0 errors, 0
      em-dashes, parenthesis balance verified. Combined tally 0/1/4/6: the major is a genuine
      strengthening of the paper, not a defect, but resets the streak hard regardless. Round 16 next.

- [x] **Round 16 complete (2026-08-10).** Second consecutive major, and the loop catching an
      overreach in its own immediately preceding round's fix rather than anything in the paper's
      original material. Codex found five wording/scoping issues in Round 15's new multinomial-null
      passage (parent-total vs leave-one-out conflation, a wrong-experiment lambda_c citation, a
      categorical exchangeability claim, an overstated "no phase information whatsoever," an
      abstract/Discussion overclaim), all fixed directly. Opus's read of the same passage went
      further: Round 15's headline conclusion, that the multinomial null "removes the basis for
      attributing the departure to phase structure," does not survive a look at absolute units. The
      null's max/RMS ratio matches the actual array's by coincidence, two compensating shortfalls
      (max undershoot 1.46x, RMS undershoot 1.61x) whose quotient happens to land close; in absolute
      terms the null is decisively refuted (actual total energy 2.59x the null's own exact
      expectation, about 1031 of its own standard deviations, absolute maximum never reached across
      many trials). Independently verified every one of these numbers from scratch against the
      actual histogram data before touching the paper. Rewrote Section 5.3 and its abstract and
      Discussion twins to report the null in absolute units before any ratio, concluding the null
      adds to, rather than removes, the case for structure beyond the parent totals. Extended
      multinomial_null.py to print the absolute quantities directly; repro repo README rewritten and
      committed separately (b69d0d3); Section 9's pinned commit bumped. A second Opus finding (M3,
      moderate) caught that Section 4's window-k lift-construction justification named the wrong
      mechanism (safety, not the actual T_d precision-reduction fact); re-derived the correct
      3-part argument from the paper's own definitions, caught and fixed a further notational seam
      via advisor review before finalizing. Eight further minor fixes (Proposition 9's unquantified
      l, an abstract/body register mismatch on Empirical Result 14, an ambiguous "at most budgets"
      phrase, a "levels checked" plural naming a single pair, Section 5.2's self-reference, a
      genuine l=2 gap in Empirical Result 13's stated range checked directly by hand, and an
      unnecessary persistence proviso on the conjecture's forward implication, confirmed via
      advisor consultation) plus one re-flagged item rejected with reason (third occurrence,
      already verified twice before). Eighth consecutive round the combinatorial core re-derived
      clean. New standing discipline adopted: conclusion rewrites wait one round, and ratio
      comparisons against a null get checked in absolute units before the ratio is cited. Recompiled
      clean, 20 pages (up from 19), 0 errors, 0 em-dashes, parenthesis balance 713/713. Combined
      tally 0/1/4/10: second consecutive major resets the streak hard again. Round 17 next.

- [x] **Round 17 complete (2026-08-10).** Codex unavailable all three attempts (environment-level
      sandbox error, not quota); proceeded Opus-only per the standing fallback's evident intent.
      First round since Round 14 with no major finding. Opus independently re-confirmed Round 16's
      substance in full (the energy excess and the Section 4 mechanism both re-derived clean) and
      found four moderate issues, all definitional or scoping gaps in Round 16's own freshly-written
      text rather than a reversal of it. Most substantive: the symbol F used throughout the
      multinomial-null passage was never defined, and under the natural reading the paper's own
      E[sum F^2]=6T claim would be off by 3^26; fixed by adding an explicit definition after
      verifying every printed number is consistent with it. Also removed a sentence narrating the
      paper's own revision history (a Rule 5c violation), fixed a wrong quantity pairing in the
      Discussion (root-mean-square, not total energy), and sharpened the multinomial null's
      conclusion to specifically claim excess energy rather than "extremity," since rescaling the
      null's mean maximum to the actual RMS shows the max/RMS ratio itself is not refuted at all.
      Eight minor items: two index slips in Section 4's Round-16 fix, a genuine factual gap in
      Empirical Result 13 about l=3,4 (resolved by independently rerunning the brute-force
      computation, same approach as l=2 last round), three clarity fixes, and two items needing no
      change (one already correctly scoped, one a self-withdrawn citation concern from the reviewer
      itself). Ninth consecutive round the combinatorial core re-derived clean. Recompiled clean, 20
      pages, 0 errors, 0 em-dashes, parenthesis balance 724/724. Combined tally 0/0/4/8: no major or
      critical, but four moderates keep the streak at 0. Round 18 next.
