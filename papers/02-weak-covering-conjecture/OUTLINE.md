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
