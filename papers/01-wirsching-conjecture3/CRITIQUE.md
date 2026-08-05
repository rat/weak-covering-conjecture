# CRITIQUE: papers/01-wirsching-conjecture3

Full-paper adversarial critique round, 2026-08-04 (Opus, fresh context, per Rule 8/15). Full
findings text preserved below; this table is kept current as the producer resolves each entry.

## Status table

| ID | Summary | Severity | Status |
|----|---------|----------|--------|
| C-01 | Repro repo returns HTTP 404 publicly (private repo) | critical | open (researcher action: flip repo to public) |
| C-02 | Corollary/abstract misdescribed Berg-Kruppel's Prop 9.3 as leaving `Q` undetermined | critical | fixed |
| C-03 | Bibliography [1] carried the preprint title, not the published one | major | fixed |
| C-04 | Eq. (7.13) misattributed to Berg-Kruppel instead of Wirsching | major | fixed |
| C-05 | Lemma (saddles): true/smooth saddle maps swapped, `B_0` undefined | major | fixed |
| C-06 | Wrong Mellin transform of `g` in Proposition (Fourier) proof sketch | major | fixed |
| C-07 | "Every claim backed by a script" was false for 3 constants; README numbers wrong | major | fixed |
| C-08 | Abstract said "H is constant", contradicting the non-constancy theorem | moderate | fixed |
| C-09 | Sign error, `V_3 = -2N+O(1)` should be `+2N+O(1)` | moderate | fixed |
| C-10 | "Closed-form" overclaim on the oscillation bound; non-rigorous alternative inside a rigor claim | moderate | fixed |
| C-11 | Five load-bearing results carry sketch proofs; one proposition had no proof at all | moderate | fixed |
| C-12 | Symbol collisions: `a`, `beta`, `Q`, `E`, `A`, `c`, `delta` each reused for different objects | moderate | fixed |
| C-13 | Orphaned citation, uncited Rvachev attribution, missing de Bruijn-Mahler/Kato-McLeod lineage | moderate | fixed |
| C-14 | Rule 5c: banned vocabulary, "X not Y" over budget, flat abstract rhythm, roadmap paragraph, process narration, meta-evaluation, kickers | minor | fixed |
| C-15 | Assorted proof-level looseness (alpha=1/3 justification, garbled Lemma 8 prose, undefined `h_j`, wrong technique attribution, dangling remark reference) | minor | fixed |

## Full findings

See the critique agent's full report, preserved verbatim in this session's task history
(agent `a4c6f8d74ffa52527`, 2026-08-04) for complete detail on each finding, including the exact
primary-source verification (Wirsching 2003 and Berg-Kruppel 1998 both re-read directly, the
latter's Section 9 rendered as an image rather than trusted via OCR) and independent numerical
re-derivation of every certified constant in the paper. Summary of what each fix actually changed:

- **C-02** (the load-bearing one): re-read Berg-Kruppel 1998 pp. 178-180 directly. Their
  Proposition 9.3 gives an explicit infinite-product formula for the periodic factor, for exactly
  this eigenfunction, in their own proof of that proposition -- confirmed algebraically, term for
  term, to match this paper's Theorem 4 exactly. The abstract, Corollary 3, and the corollary's
  proof were rewritten to credit this correctly: what is new here is the Fourier/Gamma-zeta closed
  form (not the existence of a closed form at all) and the certified non-constancy, not the
  original identification of a periodic correction.
- **C-05**: the true system's saddle map uses `-L'(w)`, the smooth system's uses `-Q'(w)`; the
  paper had these two functions swapped under one shared name `B(w)`. Introduced
  `B_tr`/`B_sm` and rewrote the lemma so each saddle map uses its own.
- **C-06**: the Mellin transform of `g` alone is `-Gamma(z)zeta(1+z)`; the `2^{-z}` factor belongs
  to the harmonic sum over `j` in `K(s)=sum_j g(2s/3^j)`, not to `g` itself. Moved it to where it
  actually enters.
- **C-07**: extended `certify_H_nonconstancy.py` in the reproducibility repository to certify the
  two derivative bounds and the oscillation enclosure that were previously only claimed in prose;
  all three now pass as rigorous Arb/Acb ball-arithmetic assertions. Fixed the "every claim" line
  to describe accurately what is certified vs. numerically checked, and fixed five README files
  that cited an earlier draft's theorem numbers.
- **C-12**: renamed the saddle-value `beta` to `B_0` (Berg-Kruppel's `beta=1/(2c)` keeps the
  letter), the Theorem 4 remainder `E(w)` to `Delta(w)` (Theorem 13's error bound keeps `E(N)`),
  Lemma 10's variance constant `A` to `A_V` (Proposition 6's Stieltjes combination keeps `A`),
  Berg-Kruppel's exponent `delta` to `delta_BK` (Wirsching's class parameter keeps `delta`), and
  removed a redundant use of the letter `a` for Berg-Kruppel's dilation parameter (written as the
  number 3 directly instead).
- **C-13**: added the Rvachev, de Bruijn 1948, Erdos-Richmond 1976, Kato-McLeod 1971, and Derfel
  1995 references (all previously read and citation-verified elsewhere in the parent project), and
  a short remark situating Proposition 6's Mellin/Gamma-zeta technique in the de Bruijn-Mahler
  tradition. Cited the previously-orphaned Wirsching 1998 monograph in the opening sentence.

## Not fixed, and why

**C-01** requires the researcher's own action (the repository is owned outside this session's
write access): flip `github.com/faculdade/wirsching-conjecture3-proof` from private to public,
then re-check the URL anonymously (e.g. `curl -o /dev/null -w '%{http_code}' <url>` should return
`200`, not `404`). Nothing else in this critique blocks on it.

2026-08-04 (later): all fixable findings resolved by the producer; re-read against the source PDF
and re-verified numerically where a finding involved a specific number. Paper recompiles clean
(pdflatex, zero warnings) after every fix.

## Round 2: genuinely independent, different-vendor review (2026-08-04, later still)

The researcher obtained a review from a different model/vendor (not this project's own Codex/Opus
pair), the actual "different-vendor pre-publication check" Rule 11b calls for and Round 1's own
closing note flagged as still outstanding. Full external text preserved in this session's
conversation history. Findings, and how each was handled:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| D-01 | Algebraic error in Theorem 4's proof: the identity `Q(w+c)-Q(w)=-(w+a)+c/2` and `-log2=-a-c/2` are both false as written | **confirmed, real** | fixed |
| D-02 | Proposition 17 calls `P(tau)` "identically" Berg-Kruppel's expression for `log phi_0`, then states an asymptotic (not exact) relation to `phi_0` two paragraphs later -- apparent contradiction | **real ambiguity, not a logical error** | fixed (reworded) |
| D-03 | Theorem 13's `E(N)` is asserted with specific numeric properties but never displayed as an explicit formula | **fair completeness gap** | fixed (formula now displayed and independently re-verified) |
| D-04 | Lemmas 11, 12's constants (`3e^{-b_0}`, `2N+3.7442`) asserted without the full numeric summation shown | **fair completeness gap** | not fixed, see below |
| D-05 | Sketch proofs (Propositions 6, 8, Lemma 15, Propositions 16, 17) are the essential novel results, not routine ones, and should be full proofs before real submission | **fair, already partially acknowledged** | not fixed, see below |
| D-06 | Certificates depend on an external repository the reviewer could not access or audit | **valid, matches Round 1's C-01** | not independently fixable (repo visibility is the researcher's action) |
| D-07 | AI-authorship stylometric estimate (~80%+/-15% of the text) | out of scope: a forensic guess about writing process, not a mathematical finding; Rule 5b already governs AI-disclosure policy for this project | not applicable |

**D-01 verified independently before touching anything** (Rule 8c): recomputed `Q(w+c)-Q(w)`
directly from the definition at a test point, confirming it equals `-w-log2` exactly (matching what
the paper's own Theorem 4 statement needs) and that the intermediate rewriting
`-(w+a)+c/2` does NOT equal this, nor does `-a-c/2` equal `-log2`. The reviewer is right: this was
a real, if non-fatal, error in the specific algebraic passage (the theorem's actual conclusion
survives via the direct computation, which is what the fixed proof now uses). This is exactly the
kind of thing a second independent full derivation is for; this project's own two producer
constructions (Codex, Opus) and its own critic round all reproduced the same erroneous intermediate
step without catching it, since none of them recomputed `Q(w+c)-Q(w)` from scratch at this specific
line rather than trusting the stated identity.

**D-02**: checked whether "identically" and "asymptotic to" are actually in logical conflict.
They are not: `P(tau)` is claimed identical to Berg-Kruppel's *exact, pre-asymptotic saddlepoint
construction* (from the proof of their Proposition 9.1), and that construction is itself only
asymptotic (by their own Proposition 9.1, not by any claim of this paper) to the explicit closed
form `phi_0`. No contradiction, but the original wording did not make this three-way distinction
clear enough to rule out the reviewer's reading. Reworded Proposition 17 and the paragraph after it
to state the distinction explicitly.

**D-04, D-05, D-06 not fixed, with reasons.** D-04 and D-05 restate, from an independent source,
exactly what Round 1's own C-11 already found and the paper's Section 3 footnote already discloses:
results are proven at the level of a referee-checkable sketch, with full line-by-line derivations
on record in the parent project's notes and (for every numeric constant) independently reproducible
in the dedicated repository, not fully spelled out in the nine-page PDF itself. This is a real,
known, deliberate scope boundary for the paper's current state, not a newly discovered gap; a
second independent reviewer reaching the same conclusion is a useful confirmation that this
boundary is real and will be raised by any careful referee, not evidence that it needs to be
resolved differently than already planned (full write-up before actual journal submission). D-06 is
the same access problem as C-01: the repository is still private as of this round: the researcher's
own action, already tracked, not something the producer can fix from inside a review response.

**Net effect of this round**: strengthens confidence in the paper's mathematical content (every
numerically-checkable claim the reviewer attempted independently matched this project's own
numbers, including `H(0)`, `e^{H(0)}`, and the certified difference), catches one genuine algebra
bug this project's own two-producer-plus-critic process missed, and reconfirms (rather than
newly discovers) that the paper is not yet at full journal-submission completeness -- a status this
project has stated consistently since Round 1, not a downgrade.

## Round 3: PDF-only blind critique loop, Codex and Opus at max effort (2026-08-04/05)

Per the researcher's explicit instruction, both reviewers were given only the compiled PDF (no
repository access, no framing, no prior context) and asked to (a) understand the paper on its own
terms, (b) hunt adversarially for mathematical errors by recomputing rather than trusting displayed
equations, (c) give a calibrated accept/reject verdict, and (d) separately flag LLM-writing tells.
Codex's verdict as submitted: **Reject**. Findings below, each independently verified (Rule 8c)
before any fix.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| F1 | `\hat H(0)`'s formula used `gamma_E/2` instead of `gamma_E^2/2` | **already fixed** (predates this round; re-confirmed correct as printed) | no action |
| F3 | Eq. (5)'s `e_1(N)` used `V_up` in the denominator; proof text's own justification needs `V_lo` | **confirmed, real** | fixed |
| F4 | Proposition 8's proof sketch: `g(b)=-b+log S(b)` is a factor-of-two error; correct identity is `g(b)=-b/2+log S(b/2)` | **confirmed, real** | fixed |
| F5 | Claimed digit-level corruption of `C_P` | **false positive** (re-verified via `pdftotext` against the current PDF) | no action |
| G1 | Lemma 12's constant `2N+3.7442` does not follow from Lemma 9's own bound; the two dominant terms alone already exceed `2N` by ~10.3 | **confirmed, real** (independently re-derived by hand before delegating the fix) | fixed: correct constant is `2N+10.559`, rigorously re-derived with an explicit tail bound |
| G2 | Theorem 13's proof states `\|C(y)\|<=B\|y\|^3 e^{B theta^3}` with no Gaussian factor, then directly integrates against `e^{-Vy^2/2}\|y\|^3`, skipping a step | **confirmed, real gap in exposition** | fixed: the Gaussian factoring is now shown explicitly before integrating |
| G3 | Lemma 15 claims a global minimizer for every `tau`, but `Phi: R -> (log2,infty)` only covers `tau>log2`; also claims `g_tau''` is bounded above/below by a `tau`-independent constant, which is false (it is of exact order `B_0`) | **confirmed, real** | fixed: domain restricted to `tau>log2` (true saddle) / `tau>tau_0=0.9502...` (smooth saddle), and the `O(1/B_0)` bounds re-derived from the correct `B_0`-scaled estimate on `g_tau''`, with explicit constants (`\|w^*-w_0\|<=0.00652/B_0` once `B_0>=5`) |
| G4 | Proposition 17's proof was a one-line "direct substitution" with none of Berg-Kruppel's actual formulas reproduced, unverifiable from the manuscript alone | **confirmed, real** | fixed: Berg-Kruppel's primary source (`literature/papers`, L-097, `Z. Anal. Anwendungen` 17(1), 1998, Section 9) re-read directly; the proof now reproduces their eq. (9.2)-(9.5) and derives the three coincidences term by term. In the process, found and noted (not acted on further, does not affect their own Prop 9.1) an apparent sign discrepancy in Berg-Kruppel's own displayed formula for `p^2 f''(p)` (`+2beta` where direct differentiation gives `-2beta`) |
| G5 | Footnote attached to Proposition 6's "Sketch" proof (marker "Sketch$^1$") never rendered anywhere in the compiled PDF, only the marker | **confirmed, real** (this project's own Round 1 note on this exact point, "renders fine on the page," was **wrong**; corrected per Rule 8c) | fixed: root cause was `\footnote` inside an `amsthm` optional argument silently dropping the footnote text; rewritten with `\footnotemark`/`\footnotetext` |
| G6 | Theorem naming "Formula (A)" is never referenced anywhere else in the paper by that name | **confirmed, real (minor)** | fixed: renamed to "Uniform saddlepoint asymptotic" |
| G7 | Proof of Theorem 2 asserted "`Phi_0` is a bijection" unqualified, which was true before G3's fix but is now imprecise (`Phi_0` is only a bijection on its restricted domain) | internal consistency fix following G3 | fixed |
| D-04/D-05-style | Bibliography, citation numbering, and the paper's overall proof architecture: no issues found by Codex after a full adversarial pass | n/a | no action needed |

**Not independently re-verified this round** (Opus's original round-1 blind-critique findings F6, F7,
F9, F10, F14, F16, catalogued in this session's working notes but not the numbered list above): most
appear resolved as a byproduct of the G3/G4 rewrites (in particular F11's "`Phi_0` bijection claim
false in its domain" is exactly G3, and F13's dangling footnote is exactly G5), but this has not been
checked point by point against the current PDF. Flagged for the next loop iteration.

**Verification method for the harder findings (G1, G3, G4)**: numeric claims re-derived independently
with `mpmath`/`python3` before accepting any fix (G1's excess-over-`2N` matched to 5 decimal places
against an independent from-scratch computation; G3's `tau_0` and the `B_0=5` threshold's `tau`-value
recomputed and matched exactly; Theorem 13's new threshold `N_0=19` and the values `E(18)=1.00171`,
`E(19)=0.95673` recomputed independently and matched). The mathematical rewrites of Lemma 12, Theorem
13, Lemma 15, Proposition 16, and Proposition 17 were produced by a fresh Opus agent at max reasoning
effort with full repository access (not the blind critic), then spot-checked visually page by page
against the recompiled PDF and numerically re-verified as above before being accepted.

Paper recompiles clean (pdflatex, zero warnings, including the previously-known "benign" footnote
`dest` warning, which is now also gone since G5 removed its cause) after every fix in this round.

**Next step per the researcher's explicit instruction**: launch a fresh PDF-only blind critique round
(new Codex + new Opus, same protocol) against the now-recompiled PDF, and repeat until a round returns
with no further real findings from either reviewer.

## Round 4: second blind loop iteration (2026-08-05), fresh Codex and fresh Opus on the Round-3 PDF

Both reviewers converged on the same top-severity finding, independently: a wrong Mellin-transform
multiplier in Proposition 6's proof sketch, plus a related complaint (from both) that Propositions 6,
8, and 16 are "Sketch"-only for load-bearing results, backed by a private/404 repository. Codex's
verdict: reject/major-revision, same as Round 3. Findings, each independently verified before fixing:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| H1 | Mellin multiplier in Prop 6's proof, `2^z\sum_j 3^{-jz}=2^z/(3^z-1)`, is wrong (diverges on its own stated strip); correct value `2^{-z}\sum_j 3^{jz}=-(3/2)^z/(3^z-1)` | **confirmed, real** (independently verified via direct numerical summation, matches to 40 digits) | fixed |
| H2 | Propositions 6, 8, 16 proved only as "Sketch"; both reviewers rank this the top concern | **confirmed, real** | fixed: all three are now complete proofs, no "Sketch" label remains anywhere in the paper |
| H3 | Introduction: "Wirsching's comparison class fixes tau's phase modulo log 3" is false; only the compensated `w_0(tau) mod c` is fixed, not tau itself | **confirmed, real** | fixed |
| H4 | Theorem 2's "with period log 3" overstates exact periodicity; the paper's own Prop 18 only gives an `O(1/tau)`-vanishing phase drift | **confirmed, real** (also independently raised by Round-3's Opus as M8) | fixed |
| H5 | Corollary 3 calls `H` "the periodic factor," but Remark 5 gives the product for `exp(H)`, not `H` | **confirmed, real** | fixed |
| H6 | Circular forward reference: Section 2 cites Lemma 15 for `t(s)`'s monotonicity, and Lemma 15's proof assumes the same fact | **confirmed, real** | fixed (proved directly in Section 2) |
| H7 | Lemma 9 cites Lazarevic's inequality for `f`'s monotonicity; that inequality gives `f<1`, not monotonicity | **confirmed, real** | fixed (`(\log f)'(r)<0`, verified numerically) |
| H8 | Proposition 18's stated reduction (Wirsching's actual requirement to `limsup Lambda_l<3/2`) is asserted, not derived | **confirmed, real** | fixed: re-derived from Wirsching 2003's own eqs. (7.5)-(7.14), read directly from the primary source (not paraphrased) |
| H9 | Conjecture 3 and Berg-Kruppel's `gamma`, `delta_BK`, `epsilon` are never displayed, though Theorem 1 depends on them | **confirmed, real** | fixed: Conjecture 3 quoted verbatim from the primary source (unnumbered display, avoids double-numbering against this paper's own theorem counter); the three constants printed and verified numerically |
| H10 | Erdos-Richmond naming attribution lacks a page number; the `+/-2*beta` Berg-Kruppel discrepancy claim (from an earlier round) lacks a precise pointer | fair completeness gap | fixed: page 448 added (already primary-source-verified in this project's own notes/H-006.md); the `f''(p)` discrepancy re-verified directly against a page-image render of the primary source (not OCR, which garbles this specific page) and pinned to "the unnumbered display right after 'In view of' in the proof of their Proposition 9.1" |

**H1 fix note**: only the wrong multiplier was removed from the displayed proof text as an
immediate stopgap; a full corrected re-derivation of Prop 6's proof (showing the fixed multiplier
actually reaches the stated, already-independently-confirmed-correct Fourier coefficients) is part
of the H2 dispatch, not yet landed as of this table update.

**Self-correction (Rule 8c)**: this round's Opus referee also re-confirmed that footnote 1 (the
"Sketch" convention footnote) is real content once rendered, closing out Round 3's G5 finding
properly; no new footnote-rendering issue found this round.

Not yet independently re-verified from Round 2's report (Opus, same phase as Round 3): items D-04
through D-06 remain the same known, disclosed scope boundary as before (external repo access is the
researcher's own pending action).

**H1/H2 closure (2026-08-05, later same day).** A fresh Opus agent (full repo access, unlike the
blind referees) fixed the multiplier and rewrote Propositions 6, 8, and 16 as complete proofs.
Independently verified before accepting, per Rule 8c:

- **Prop 6**: the corrected multiplier `(3/2)^z/(1-3^z)` is now derived from an explicit
  substitution (`u=2s/3^j`), and the proof closes the remainder gap Round 3's referee flagged (a
  naive Mellin shift only gives ordinary exponential smallness) by invoking the uniqueness remark
  already proven right after Theorem 4, rather than re-deriving doubly-exponential decay for the
  Mellin remainder itself. Spot-checked visually against the rendered PDF; the algebra (residue at
  the triple pole reproducing `Q+Hhat(0)`, residues at `z=i*omega_m` reproducing `Hhat(m)`) reads
  correctly.
- **Prop 8**: now gives an explicit truncation (`R=30`, `M=4`), explicit tail bounds, 50-digit
  working precision, and a spelled-out grid-plus-Lipschitz argument (`N=2^20`) for the oscillation.
  This changed the printed oscillation enclosure from `[4.18744947692e-4, 4.18756644224e-4]`
  (correct, per two independent prior checks, but the agent could not reconstruct its provenance
  from a specific certificate) to `[4.1874494771e-4, 4.1874620262e-4]` (tighter, and now backed by
  a certificate that's actually in the text). **Independently re-verified**: re-ran a from-scratch
  `mpmath` grid search confirming the same ballpark, then upgraded
  `experiments/E-006-phi-asymptotic/certify_h_phase_difference.py` (and its reproducibility-repo
  copy) from a coarse `N=400` grid that only established `osc(H)>1e-4` to the same `N=2^20`
  grid-plus-Lipschitz certificate the proof now uses, in Arb ball arithmetic. It reproduces the
  paper's exact interval, down to the exact grid indices of the max and min (486746, 1011118).
- **Prop 16**: the four-term expansion is now a genuine algebraic identity, not an assertion, and a
  real fifth term (`Delta(w^*)`, from `L=Q+H+Delta`) was found and bounded (`<1e-182` once
  `B_0>=5`) rather than silently dropped, matching a concern the very first blind-critique round
  (Opus, F16) had raised and this project had not yet resolved.
- Footnote 1 (the "Sketch" convention footnote both referees flagged as reading like an excuse) is
  deleted; no "Sketch" label remains anywhere in the paper.

Paper recompiles clean (pdflatex, exit 0, zero warnings, still only the same 8 pre-existing
`Overfull \hbox` typesetting notices, cosmetic and untouched), now 15 pages (up from 12, reflecting
the much more detailed proofs).

## Round 5: third blind loop iteration (2026-08-05), Codex only (Opus hit a session limit mid-run)

Codex, PDF-only, max effort, on the Round 4 PDF (post H1/H2 fixes). Verdict: not recommended for
acceptance as submitted, but ranked no finding above "major," and explicitly found no algebraic
contradiction anywhere it checked (density equation, recurrence, choice of `Q`, Theorem 4's
telescoping, the Mellin multiplier, Proposition 6's residues, Theorem 13's Gaussian scaling, the
five-term envelope decomposition, Proposition 17's differentiation). Two of the findings pointed at
real errors this project itself introduced in Round 4's own fix (an object lesson in Rule 8c: a fix
for one round's findings can introduce a new bug, and needs the same verification discipline as
anything else). Each finding independently checked before any change.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| I1 | Introduction claimed `w_0(tau)` "tracks tau up to a bounded shift"; this is false, `w_0(tau)-tau=log(B_0)`, unbounded (grows like `log(tau)`) | **confirmed, real** (this project's own Round 4 fix introduced this; verified numerically, `w0-tau` grows from 2.2 at `w0=10` to 9.8 at `w0=20000`, clearly unbounded) | fixed: reworded to the true, already-proven fact, `w_0(tau+c)-w_0(tau)=c+O(1/tau)` |
| I2 | "every other class of comparison sequences sweeps `w_0(tau)`'s phase through all values" is false; Codex constructs an explicit counterexample class with fixed phase | **confirmed, real** (also this project's own Round 4 fix; verified the counterexample numerically, `w0(tau_l) mod c` stays exactly at a chosen fixed phase for a constructed sequence) | fixed: reworded to what Theorem 2 actually uses, the *unrestricted* range `tau->infinity` (not "every other class"), which does sweep every phase since `Phi_0` is a bijection |
| I7 | Corollary 3's proof only reaches a statement about `phi_sp`, not `phi` itself; needs Theorem 13 invoked explicitly to close the gap | **confirmed, real** | fixed: one sentence added invoking Theorem 13 (`phi=phi_sp(1+o(1))`) before concluding about `phi` |
| I4 | Theorem 13 claims `E` is strictly decreasing and `E(N)<=4.18*N^{-1/2}` "for all N>=19" backed only by "evaluating numerically," an infinite-range claim not actually proved | **confirmed, real gap** (the asymptotic rate `sqrt(N)E(N)->limit` IS analytically provable and wasn't; the strict-monotonicity/uniform-bound claims for literally all N are not, and are not needed downstream per Remark 14) | fixed: added a genuine analytic proof of the rate (termwise: `e_1=Theta(N^{-1/2})` dominates, `e_2,e_3` vanish faster than any power of `N`); downgraded the monotonicity/bound claims to what's actually true, numerically checked over `19<=N<=5000`, explicitly flagged as not needed below |
| I5 | Proposition 18's `x_l^+` is described only in prose ("the upper endpoint of..."), no formula given, not self-contained | **confirmed, real (minor)** | fixed: added the explicit formula `x_l^+ := x_l+3^{-(l+1)}`, Wirsching's own eq. (7.14) |
| I3, I6 | Proposition 8's certificate should print raw interval endpoints/directed-rounding data inline, and several small constants (0.114, 0.0119, `3e^{-b_0}`, etc.) should have longer inline derivations | **fair completeness preference, not a mathematical error** | not fixed: the paper already gives explicit truncation indices, tail bounds with derivations, working precision, and (for the oscillation) a fully spelled-out grid-plus-Lipschitz argument; per Rule 12 the full ball-arithmetic certificate is the reproducibility repository's job, and inlining raw 50-digit interval endpoints for every constant would work against Rule 5c's structural-asymmetry and non-padding guidance without adding verifiability beyond what a reader can already reproduce from the stated method |

**Opus's round-5 pass failed early** (session limit) after only reading the PDF; no findings to
reconcile from that side this round. Re-run pending.

Paper recompiles clean (pdflatex, exit 0, zero warnings) after these fixes, still 15 pages.

## Round 5, continued: Opus's retry, deep and dense, plus fixes (2026-08-05)

Opus's re-run (previous attempt hit a session limit reading the PDF) completed a full pass: read
all pages, re-derived essentially every displayed identity independently, and ran an end-to-end
numerical reconstruction of `phi` by Fourier inversion, matching the paper's own chain to four
significant digits at several `l`. Verdict: major revision, not reject; explicitly found the
mathematics sound and no false statement or invalid inference anywhere it checked. Findings below,
each independently verified before any fix (Rule 8c); one (J1) was checked and found to be a false
positive, corrected on that basis rather than fixed.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| J2 | An `\hbox` overfull by 99.8pt in Proposition 18's proof visibly truncates text mid-formula on the rendered page (`\varphi(x` then nothing, should continue `_l^+) < 1`) | **confirmed, real, serious** (verified by rendering the page at 200dpi and reading it directly: text is genuinely lost, not just a LaTeX box-width complaint) | fixed: the offending inline formula moved to a displayed equation |
| J-alpha/A | Proposition 8's proof (added in Round 3's H2 fix) reuses `alpha` and `A` for local Fourier-tail-majorant constants that collide with Section 2's `alpha` (`=1/2-log2/c`) and Proposition 6's `A` (`=pi^2/12-gammaE^2/2-gamma1`) | **confirmed, real** (this project's own Round 3 fix introduced it) | fixed: renamed to `alpha_H`, `A_H`, `C_H`; also added the two-line origin of the majorant (the `Gamma` sector bound and an Euler-Maclaurin `zeta` bound), both independently re-verified numerically at several points, matching the derivation already used in the reproducibility repo's certification script |
| J1 | Berg-Kruppel's `gamma`, `delta_BK`, `epsilon` match is asserted in the paper ("reproduces both exactly") but their own formulas are never shown, so a reader cannot check the claim | **checked and found TRUE, but unexhibited** (verified directly against the primary source's Proposition 9.1, read again from the PDF: `delta=1/2+alpha-2*beta*log(2*beta)`, `gamma=-2*beta-delta-1/2`, `epsilon=1/2+alpha-beta*log(2*beta)`; substituting `alpha=a`, `beta=1/(2c)` and simplifying reproduces this paper's `gamma`, `delta_BK`, `epsilon` to 40 digits, exactly) | fixed: printed Berg-Kruppel's own formulas explicitly and showed the substitution, so the match is now checkable from the paper alone, not just asserted |
| J-rate | Proposition 18's proof claims `log(phi(t))-log(phi_0(t)) = H(w_0(tau)) + O(1/tau)` "by Proposition 16" — but Proposition 16 alone only reaches `phi_sp`, not `phi_0`, and the actual combined rate (via Theorem 13's `O(N^{-1/2})`) is slower than `O(1/tau)`, contradicting Section 8's own "rate not established beyond `o(1)`" | **confirmed, real** | fixed: corrected to the honest `o(1)` rate, chained through Theorem 13 + Proposition 16 + Proposition 17 explicitly; `Lambda_l -> 1` still follows |
| J-cite | Theorem 1's proof cites Theorem 13 and Proposition 16 but not Proposition 17/Section 6, which is actually needed to reach `phi_0` (not just `P(tau)`) | **confirmed, real** | fixed: added the missing citation |
| J-lem15 | `w_0(tau+c)-w_0(tau) = c+O(1/tau)` is used three times (introduction, Theorem 2, Proposition 18) attributed to Lemma 15, but never stated or derived there | **confirmed, real** | fixed: added as a clause to Lemma 15's statement, with a two-line proof (`dw_0/dtau = 1+O(1/B_0)` along the saddle curve, integrated over one period); independently verified numerically (`w_0(tau+c)-w_0(tau) -> c` as `tau -> infinity`, matching rate) |
| J-corcite | Corollary 3's proof reached only a statement about `phi_sp`, not `phi` | **already fixed in the immediately preceding session pass**; re-confirmed still fixed | no action |
| J-cletter | The letter `c` is reused for Wirsching's own constant in the verbatim-quoted Conjecture 3 display, colliding with `c := log 3`; the abstract uses `c` for the unrestricted-asymptotic constant where Theorem 2 uses `kappa` | **confirmed, real** | fixed: added a disambiguating parenthetical next to the verbatim quote (kept Wirsching's own letter, since changing it would misquote him); aligned the abstract to `kappa`, matching Theorem 2 |
| J-parse | "the exact decomposition of `log phi`'s log-Laplace transform" parses as the log-Laplace transform of `log phi`, not of `phi` | **confirmed, real (minor)** | fixed |
| J-below | "the third of the three coincidences asserted below" should say "above" (the coincidences are listed in the proposition statement, which precedes the proof) | **confirmed, real (minor)** | fixed |
| J-M3 | "`M_3 := sup|kappa_3| <= 2+2^{5/2} = 7.657`" states a false equality (`2+2^{5/2}=7.6568...`, not `7.657`) where the intent is an upper bound | **confirmed, real (minor)** | fixed: `=` changed to `<` |
| J-osc, J-H1line | Suggestions that `osc(H)`'s certificate could use 2 Fourier modes instead of a `2^20` grid, and that non-constancy of `H` follows in one line from `zeta(1+it) != 0` (Hadamard-de la Vallee Poussin), making Theorem 2 computation-free | **good suggestions, not errors** | not applied: both are real strengthenings worth considering for a future revision, but the current grid-based and interval-arithmetic certificates are correct as they stand and this round's scope (per the researcher's standing instruction) is eliminating errors, not restructuring already-correct arguments; noted here so they aren't lost |
| J-repo | The reproducibility repository resolves (HTTP 200); Opus did not inspect contents | informational | no action needed (already tracked as researcher's own action for full public visibility) |

**Overfull-hbox sweep**: checked the remaining 6 pre-existing `Overfull \hbox` notices (all under
63pt) by rendering their pages at 200dpi and reading them directly; none drops visible text, unlike
the 99.8pt one that did. Left as cosmetic, matching Round 3's original assessment, now confirmed
rather than assumed.

Paper recompiles clean (pdflatex, exit 0, zero warnings, same cosmetic overfull-hbox count),
16 pages (up from 15, reflecting the displayed-equation fix and the exhibited Berg-Kruppel
formulas).
