# CRITIQUE: papers/01-wirsching-conjecture3

Full-paper adversarial critique round, 2026-08-04 (Opus, fresh context, per Rule 8/15). Full
findings text preserved below; this table is kept current as the producer resolves each entry.

## Status table

| ID | Summary | Severity | Status |
|----|---------|----------|--------|
| C-01 | Repro repo returns HTTP 404 publicly (private repo) | critical | fixed (researcher made the repo public, 2026-08-05; verified `curl` returns 200) |
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

**C-01**: resolved 2026-08-05. The researcher made `github.com/faculdade/wirsching-conjecture3-proof`
public; re-checked anonymously with `curl -o /dev/null -w '%{http_code}' <url>`, returns `200`.
Nothing else in this critique was blocked on it.

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
| D-06 | Certificates depend on an external repository the reviewer could not access or audit | **valid, matches Round 1's C-01** | fixed 2026-08-05, same as C-01 (repo now public) |
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

**D-04, D-05 not fixed, with reasons.** D-04 and D-05 restate, from an independent source,
exactly what Round 1's own C-11 already found (superseded later: Round 5 converted Propositions 6,
8, and 16 from sketches to complete proofs, closing the main substance of D-05). D-04's remaining
piece (Lemmas 11-12's constants shown with full derivations, not just "bounding the first few
terms") was subsequently addressed as part of that same complete-proof conversion. D-06 and C-01
are both now fixed (2026-08-05, repository made public).

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

## Round 6: fourth blind loop iteration (2026-08-05), Codex (Opus hit a session limit again)

Codex, PDF-only, max effort, on the Round 5 PDF. Verdict: not recommended for acceptance as
submitted, but again found no sign/algebra contradiction anywhere it checked (the recurrence,
Mellin residues, saddlepoint integral, envelope decomposition, and final phase arguments all
checked out). Most findings restated Round 3-5's already-settled "certification lives in the
repository, per Rule 12" scope decision and were not reopened (Rule 8d: don't re-litigate settled
material without new evidence). Two findings were new and real, independently verified before
fixing:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| K1 | Lemma 15 asserts `\|Delta'\|,\|Delta''\|<=1e-60` "from Theorem 4's bound on Delta^(j)", but Theorem 4 only states an `O_j(...)` asymptotic notation, which supplies no explicit constant or threshold; the numeric claim does not actually follow from what's cited | **confirmed, real** | fixed: derived explicit bounds directly from Delta's own definition (termwise differentiation, an elementary bound on `d/dx[x/(e^x-1)]`, geometric-tail domination), independently verified numerically at several points; **caught and fixed a sign error of my own in the first draft of this derivation before it reached the paper** (`Delta'(w)` is a sum of negative terms, not positive; verified against a direct numerical derivative before finalizing) |
| K2 | The introduction calls Wirsching's Conjecture 3 quotation "verbatim" while admitting a notation substitution (`delta_5` to `delta`) two lines later, which is a contradiction in terms | **confirmed, real (minor)** | fixed: reworded to "with notation normalized", not "verbatim" |
| K3 | (raised again) "the collision of letters is unavoidable" (Proposition 17) is false; renaming is straightforward | **confirmed, real (minor), already flagged in Round 5 as a suggestion, not fixed then** | fixed this round: reworded to state the two objects are different and BK's `a` is simply not reused, without the false "unavoidable" claim (a full rename of this paper's own long-standing `a` was judged out of proportion to the finding; the false claim itself is what's fixed) |
| K4 | Proposition 17's Berg-Kruppel sign-discrepancy claim ("their own displayed formula... reads...") lacks a page number, a "serious bibliographic claim" per Codex | **confirmed, real (minor)**, already page-located in this project's own working notes | fixed: added "p. 179 of [2]", confirmed directly against the primary-source PDF's own printed page number (not the PDF-extraction page index, which differs) |
| K-repo | Restates that "certified" bounds, Proposition 8's grid computation, and Theorem 13's unused monotonicity claim are not literally displayed in the 16-page PDF | **same finding as Round 3-5's repeated "repository vs. inline" scope question** | not reopened: Rule 12's division of labor (paper states the method and the provable analytic bounds; the reproducibility repository carries the actual interval-arithmetic computation) was already explicitly decided in Round 5's table; no new argument or evidence given this round to revisit it |
| K-nonconst | Suggests proving `H` non-constant via `zeta(1+it)!=0` instead of numerically | **same suggestion as Round 5's J-H1line** | not applied, same reasoning: a genuine strengthening for a future revision, not an error, out of this round's scope |

**Opus's round-6 pass failed again on a session limit** (this time partway through independently
re-deriving Proposition 8's numbers, which it had already confirmed match before stopping). Its
partial results (H(0), H(log 3/2), their difference, and `e^{H(0)}` all independently reproduced
correctly) are consistent with, not contradictory to, everything fixed so far. Full re-run pending
if the researcher wants another blind pass; per the researcher's standing instruction the loop
continues until a round returns with no further confirmed findings from either reviewer.

Paper recompiles clean, 16 pages.

## Round 6, continued: Opus's retry, deepest pass so far (2026-08-05, later)

Opus's re-run completed a full pass: recomputed essentially every printed constant at 35-70
digits, confirmed the end-to-end numerical chain (Proposition 6's Fourier series against the
elementary formula (6), agreement to 50 digits; the Section 5-6 envelope/identification chain
against direct numerical evaluation of phi at tau=10..80), and rendered every page at 400dpi to
check for margin overruns after the previous round's lost-text bug. **Recommendation: accept
after minor-to-moderate revision** -- explicitly found no error damaging either main theorem, and
confirmed as correct essentially everything it checked (Theorem 4, Proposition 6, Lemmas 9-12,
Proposition 17, Theorems 1-2, Proposition 18's reduction arithmetic, the bibliography). Findings,
each independently verified before any fix:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| L1 | Eq. (4) (`sup|H'|`, `sup|H''|`) stated as "certified" with zero proof, while Prop 8 three paragraphs later gives a fully explicit majorant for the same kind of sum -- an inconsistent rigor level, and (4) is used in 5 downstream places | **confirmed, real** | fixed: moved the majorant (previously derived only inside Prop 8's proof) to right after Remark 7, used it to prove (4) explicitly (exact head sum m=1..6 plus a certified geometric-polynomial tail bound), verified numerically (bound matches to all printed digits); Prop 8's proof simplified to cite the now-established majorant instead of re-deriving it |
| L2 | The reflection `x -> 1-x` in "this is Wirsching's density up to the reflection..." is left genuinely ambiguous: a reader cannot tell from the manuscript whether the reflection is vacuous or actually changes which end of the support is analyzed near `t->0` | **confirmed, real** | fixed: added the one-line proof that the reflection is vacuous (`X` and `1-X` are equidistributed, since `1-U_j ~ U_j` and `sum 2*3^{-j}=1`), verified directly |
| L3 | "This is the largest of the five" (Prop 16's `T_3`) is false against the paper's own printed bounds: `T_4`'s bound exceeds `T_3`'s at every `B_0`, confirmed both symbolically and by direct numerical evaluation of all four terms at several `tau` | **confirmed, real** | fixed: sentence deleted (nothing depends on the claim) |
| L4 | The `e_2` derivation's displayed intermediate, "the truncated Gaussian tail `2*int (1/sqrt(2pi)) e^{-Vy^2/2} dy`", is missing the `sqrt(V)` prefactor; as literally written it would integrate to a different, wrong expression (`theta*V` in the denominator instead of `theta*sqrt(V)`) | **confirmed, real** | fixed: added the missing `sqrt(V/2pi)` prefactor and the explicit substitution step, re-verified the resulting expression matches the already-correct (8) |
| L5 | Corollary 3's proof paragraph ("this is precisely Berg and Kruppel's own Proposition 9.1 ... not an independent asymptotic claim about `P` itself") mischaracterizes the paper's own argument: the coefficient-matching derivation just given IS an independent verification, using nothing from [2] beyond the printed `phi_0` formula | **confirmed, real** | fixed: reworded to state plainly that the coefficients of `P` reproduce `gamma`, `delta_BK`, `epsilon` exactly, removing the self-undermining disclaimer |
| L6-L9 | Assorted notation/reference fixes: Section 2's Berg-Kruppel truncated equation used `d` for the dilation parameter where Section 6 uses `a` for the same object (inconsistent); Remark 5's `a`, `b`, `alpha` (Berg-Kruppel's own, `a=3, b=3/2`) were never disambiguated from this paper's identically-named objects, unlike the later, already-fixed collision note in Proposition 17; `N_0` used in Theorem 13's proof but never defined anywhere; Lemma 12's statement used `h_j` without defining it (only the proof did); Theorem 1 left `delta` unquantified; Remark 7 cited `\eqref{eq:Hexact}` (the definition of `H`) as `phi_0`'s "companion asymptotic", a stale/wrong cross-reference | **all confirmed, real (minor)** | fixed: Section 2 now uses `a` consistently with an upfront disambiguation note; Remark 5 gets an explicit "their `a,b,alpha` are unrelated to this paper's" parenthetical; `N_0` reference replaced with a direct statement of what `E(18)`, `E(19)` show; `h_j` now defined in Lemma 12's own statement; Theorem 1 now reads "For every `delta>0`"; Remark 7's cross-reference fixed to point at Section 2 |
| L10 | Remark 14 says both "gives the Edgeworth correction ... `O(N^{-3/2})`" and, two sentences later, "we do not prove the remainder term here" -- a direct contradiction | **confirmed, real (minor)** | fixed: "gives" softened to "suggests", with an added opening clause that a sharper rate is plausible but not established |
| L11 | The Introduction's account of what Berg-Kruppel's own paper leaves open ("left open both the exact multiplicative constant...") is imprecise relative to the abstract's separate, more accurate account (they give the periodic factor as an explicit product but never evaluate it) | **confirmed, real (minor)** | fixed: reworded to state both facts precisely and consistently with the abstract |
| L12-margins | Six lines identified by rendering every page at 400dpi and measuring ink bounding boxes against the 539pt text-block edge; two were serious enough to look broken in print (Prop 17's statement, 41pt over; Lemma 11's statement, 30pt over), confirmed by direct visual inspection; **no content was actually lost in any of the six** (this round's specific ask, given Round 5's real lost-text bug) | **2 confirmed worth fixing, 4 cosmetic** | the 2 display-worthy overruns (Prop 17's integral, Lemma 11's sum bound) converted to displayed equations; the remaining 4 (including one still at 62pt per the recompiled log) visually confirmed to lose no content and left as is, matching Round 5's original judgment on this exact category of warning |

Every fix independently verified before being made: L1's bound re-derived numerically and matched
to all printed digits; L2's symmetry claim re-derived and checked; L3 and L4 checked by direct
symbolic and numerical recomputation before touching the text. Visual re-inspection at 150-200dpi
confirms every touched page renders cleanly with no truncation, including the two newly-displayed
equations.

Paper recompiles clean (pdflatex, exit 0, zero warnings), still 16 pages, overfull-hbox count down
from 6 to 3, none losing content.

## Round 7: fifth blind loop iteration (2026-08-05), Opus first pass complete

Opus, PDF-only, max effort, on the Round 6 PDF. **Verdict: Accept after minor-to-moderate
revision** -- the strongest verdict yet in this loop, and explicitly found no mathematical error
anywhere it checked (an extensive list: Theorem 4, Proposition 6 including the full residue
computation, Lemmas 9-12, the derivation of e1/e2/e3, Lemma 15, Proposition 16's five-term
decomposition, Proposition 17, the series reversion, Proposition 18's reduction). Ran an
independent end-to-end numerical check (direct Fourier inversion of phi, no saddlepoint, compared
against the paper's own chain) confirming the full constant chain reproduces the true density.
Findings, each independently verified before fixing (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| M1 | The identification of `phi` with Wirsching's invariant density is asserted with no citation locator, while every other citation in the paper is pinpointed to an equation or page number | **confirmed, real, most severe finding of this round** | fixed: located the exact primary-source match (re-read `[1]`'s Section 6 directly) -- Wirsching's own equation (6.1) defines `(W_3 f)(x) := (3/2)*int_{3x-2}^{3x} f`, identical to this paper's displayed integral equation, and his Corollary 7 characterizes `phi` as the unique `L^1_loc` solution with `supp subset [0,1]`, `int=1`, `W_3 phi = phi` -- both now cited explicitly by equation/corollary number |
| M2 | Proposition 8's stated truncation-tail range (`s<=3/2`) does not cover the two oscillation-grid evaluation points actually used later in the same proof (`s approx 1.665` and `s approx 2.885`) | **confirmed, real** (verified numerically: both grid points exceed 3/2) | fixed: extended the range to `s<=3` (covers both points), recomputed the tail bound (`4.43e-30`, still negligible) |
| M3 | Remark 5 claims the Fourier series "is what lets us certify non-constancy," but Proposition 8's actual primary computation uses the elementary formula (7), which is algebraically the same object as Berg-Kruppel's product (verified: `exp(H)=e^{-Q}e^L e^{-Delta}` matches Remark 5's own product identity term for term) -- an overclaim the paper's own proof contradicts | **confirmed, real** | fixed: reworded Remark 5 to state accurately what the Fourier series contributes instead (the derivative bounds (5)), and noted explicitly that Prop 8's primary computation is, in substance, an evaluation of Berg-Kruppel's own product |
| M4 | Discussion's "the class on which the weaker statement holds is exactly the one phase... at which the ratio converges" is false: every phase admits some sequence along which the ratio converges to `e^{H(theta)}`, not just phase 0 | **confirmed, real** | fixed: reworded to state what's actually special about phase 0 (it's the one Wirsching's own class happens to fix) |
| M5 | Remark 5's disclaimer "their `a,b,alpha` are unrelated to this paper's identically-named objects" is wrong for `alpha`: Section 2 imports Berg-Kruppel's `alpha` verbatim, and Proposition 17 proves it equals this paper's `a` -- the disclaimer tells the reader the opposite of what's needed to verify the display | **confirmed, real** | fixed: corrected the disclaimer to except `alpha` explicitly, with a forward pointer to Proposition 17's identification |
| M6 | "Certified"/"rigorously" language for Proposition 8 doesn't distinguish which specific computations are ball arithmetic vs. floating point | fair completeness observation, matches Round 5's D-04/D-05-style finding | not fixed, same reasoning as before (Rule 12 division of labor) |
| M7 | Theorem 2's "periodic up to an `O(1/tau)`-vanishing phase drift" invites a wrong reading: the *per-period* drift vanishes, but the *cumulative* drift `w_0(tau)-tau` grows like `log(tau)`, unbounded | **confirmed, real** | fixed: reworded to state precisely that `H` is periodic in the saddle variable `w_0(tau)`, whose successive-period increment tends to `c` even though `w_0(tau)` itself drifts unboundedly from `tau` |
| M8 | Two issues in Theorem 13: (a) "confirming N>=19 is where the stated bound first takes hold" should say "first becomes non-vacuous"; (b) "neither fact is used below, where only `E(19)<1` and `E(N)->0` are needed" -- `E(19)<1` itself is not actually used anywhere downstream, only `E(N)->0` | **both confirmed, real (minor)** | fixed |
| M9 | Proposition 18 quotes Wirsching's (7.13) at `x_l` but applies it at `x_l^+ = x_l + 3^{-(l+1)}`, with no justification that the substitution is valid | **confirmed, real (minor)** | fixed: added the one-line justification (`x_l^+/x_l -> 1`, `phi_0'/phi_0` slowly varying near `x_l`) |
| M10 | The reproducibility repository is unverifiable at review time (a referee cannot confirm contents); suggests an archived DOI snapshot | fair suggestion, out of scope for text fixes | not fixed (repo-archival is a researcher action, not a text fix) |
| M11 | The Introduction's roadmap says "Section 3... proves Proposition 6 and Corollary 3", but Corollary 3 is proved in Section 6, not Section 3 | **confirmed, real (minor)** | fixed |
| T1 | Severe margin overrun on page 10 (61pt, within 11pt of the physical page edge) -- confirmed by direct ink-bounding-box measurement, no content lost but looks broken in print | **confirmed** | fixed: converted the offending inline chain to a displayed equation |
| T2, T3 | Two smaller overruns (page 13, 8.6pt; page 6, 4.8pt), neither losing content | **confirmed, cosmetic** | not fixed, same judgment as Round 5/6's remaining cosmetic overfull-hbox cases |

**Independent numerical verification highlights this round**: `hat H(0)` agrees to 30 digits with
the numerically-integrated period-mean of `H`; Proposition 6's Fourier series agrees with the
elementary formula (7) to 40 digits at four points; the `2^20`-grid argmax/argmin indices
(486746, 1011118) independently reproduced by a fresh sweep; and, most substantively, an
end-to-end check computing `phi` by direct numerical Fourier inversion (bypassing the saddlepoint
machinery entirely) for `N=6..14`, `rho=1,2`, confirming the full Section 4-6 constant chain
(including the `O(tau^{-1}log^2 tau)` rate of Section 6) reproduces the true density.

Codex's parallel round-7 report received; findings pending review (see next entry in this file, or
a subsequent commit, once processed).

Paper recompiles clean, 16 pages, overfull-hbox count down from 3 to 2.

## Round 7, continued: Codex's report processed (2026-08-05, later)

Codex, PDF-only, max effort, on the same Round 6 PDF Opus reviewed above. Verdict: reject
("not yet a rigorous, self-contained proof"), primarily restating the repository-vs-inline
certification question already settled across Rounds 3-7 (Rule 12) and the citation-locator
concern already fixed this round via Opus's M1/M3. One finding was new and required direct
verification (Rule 8c) before any action, and turned out to be a false positive:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| N1 | "a real quantity, since `Lambda(-y) = Lambda(y)`" -- claimed to be mathematically false (the correct identity is `Lambda(-y) = conjugate(Lambda(y))`) | **FALSE POSITIVE**, confirmed by direct inspection: rendering the actual PDF page at 250dpi shows the identity is printed with a visible overline, `Lambda(-y) = \overline{Lambda(y)}`, exactly the correct statement. Codex's own tool use (`pdftotext`) strips overline diacritics, so its extracted text read "Lambda(-y) = Lambda(y)" with no indication a bar was ever there -- a text-extraction artifact, not a paper defect. Independently re-derived the correct identity from the definition of `Lambda` and confirmed it numerically (`Lambda(-0.7) = conj(Lambda(0.7))`, matches to 30 digits; `Lambda(-0.7) != Lambda(0.7)`, confirmed different) | no action; recorded per Rule 8c as a reviewed-and-discarded finding |
| N2 | "Full optimization" (Proposition 8) mischaracterizes the actual method, a grid search plus a Lipschitz enclosure | **confirmed, real (minor, also independently raised by Round 6's M6-adjacent language)** | fixed: reworded to "a grid search with a Lipschitz enclosure" |
| N3-N7 | Restatements of: certification living in the repository rather than inline (Rule 12, settled); the Wirsching/Berg-Kruppel identification needing a locator (fixed this round via Opus's M1, M3, M5 before Codex's report was read); Lemma 9's monotonicity "asserted"; Lemma 11's tail bound "not displayed"; Theorem 13's `E(N)` monotonicity claim | no new confirmed findings beyond what Opus's pass already fixed or what Rounds 3-7 already settled as out of scope | no action |

This is the first round where a critique-loop finding was checked and found to be a pure
text-extraction artifact rather than either a real defect or a misreading of real content (compare
Round 3's F5, which was a false positive about digit corruption, not about a rendering-vs-extraction
mismatch). Recorded here per Rule 8c's instruction to keep a plain record of mistaken critiques,
not just correct ones -- a lesson worth carrying into any future PDF-only review: overline/diacritic
marks are invisible to `pdftotext` and must be checked against the rendered page, not the extracted
text, exactly as the loop's own prompt already instructs for margin truncation.

Paper recompiles clean, 16 pages, unchanged overfull-hbox count (2, both cosmetic).

## Round 8: sixth blind loop iteration (2026-08-05/06), Opus and Codex both complete

Opus, PDF-only, max effort, on the Round 7 PDF (explicitly instructed to verify overline/conjugate
identities and margin overruns against rendered page images, not extracted text, per Round 7's
false-positive lesson). Verdict: **accept with minor revisions**, no mathematical error found
anywhere it checked, including three independent end-to-end numerical confirmations (Proposition
16's `O(1/tau)` rate; Theorem 13 reconfirmed by exact tilted-Fourier-inversion quadrature,
bypassing the saddlepoint machinery entirely; Remark 14's Edgeworth rate `N(R-1) -> -1/12`).
Findings, each independently verified before fixing (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| O1 | Two lines overrun the text margin (p. 6, ~5.4pt on an inline radical; p. 14, ~9pt on a displayed equation chain), confirmed by ink-bounding-box measurement, no content lost | **confirmed** | fixed: both converted to standalone displayed equations |
| O2 | Theorem 2 is true only conditional on Proposition 8's certified bound, but nothing in the theorem statement says so | **confirmed, real** | fixed: added "Conditional on the certified bound of Proposition 8" to the theorem statement |
| O3 | Theorem 1's value `e^{H(0)}=0.534122...` depends on a specific normalization of `phi_0`; Conjecture 3 itself only asserts existence of some constant, so the *value* (not the *truth*) is normalization-dependent, and nothing says so | **confirmed, real** | fixed: added a clarifying sentence to Theorem 1 |
| O4 | Proposition 8's certificate is rigor-uneven: the primary computation (50-digit floating point) and the Fourier-series cross-check (Arb ball arithmetic) are both called "certified" with no distinction; unclear what arithmetic the `2^20`-point oscillation grid sweep itself used | **confirmed, real** | fixed: added explicit labels distinguishing the floating-point route from the interval-arithmetic route at each step, and clarified that only the two located extremal points (not the full sweep) were re-confirmed in ball arithmetic |
| O5 | Two literature claims (the Berg-Kruppel p.179 sign discrepancy; Remark 7's "established... as generic across this whole class") flagged as unverifiable by a PDF-only reviewer without access to the cited sources | **already independently verified in Round 6/7 against the actual primary-source PDF** (the sign discrepancy; page number confirmed against the paper's own printed page number) | no action beyond what's already done; noted for completeness |
| O6 (Theorem 2 fragment) | "...without bound; with amplitude bounded below by a positive, certified constant." is a dangling sentence fragment after the semicolon | **confirmed, real (minor)** | fixed as part of the O2 rewording |
| O7 | Garbled parenthetical in Theorem 2's proof: "(since Phi_0 restricted to (ca+1,infty) is a bijection onto (tau_0,infty), and tau -> tau mod c composed with that inverse is onto one period once tau is large)" -- conclusion correct, wording doesn't parse cleanly | **confirmed, real (minor)** | fixed: rewritten using the standard fact that a continuous, strictly increasing, unbounded function hits every residue class mod c infinitely often |
| O8 | Discussion's "every phase swept by H admits some sequence along which the ratio converges" (added in Round 7 to fix a different false claim) was itself asserted with no proof | **confirmed, real (minor)** | fixed: added the explicit one-line construction (`tau_l := Phi_0(theta+lc)`, giving `w_0(tau_l)=theta+lc` exactly), verified the construction is correct |
| O9 | Proposition 16's closing "Each bound is an absolute constant over `B_0`, or smaller" is false for `T_4`, whose own displayed bound uses `B_0-1/c` in the denominator, not `B_0` (verified numerically: `T_4` bound exceeds `const/B_0` at every tested `B_0`) | **confirmed, real (minor)** | fixed: reworded to `O(1/B_0)` with an explicit note on why `T_4` still qualifies |
| O10-O13 | Minor/editorial: "Corollary 3" mislabeled (should be Proposition/Remark); notation `x_l` vs `z_l`; Lemma 9's local constants looser than necessary; one remaining en dash used as punctuation rather than a name-compound | noted, judged editorial/cosmetic | not fixed (out of scope for an error-elimination pass; Corollary 3's relabeling in particular would touch many cross-references for a purely naming concern) |

Codex, PDF-only, max effort, same PDF. **Verdict: Reject as submitted.** Unlike Opus, Codex did not
converge with the accept verdict; its findings are, checked one by one, entirely a restatement of
the repository-vs-inline certification question already settled across Rounds 3-8 (Rule 12's
division of labor: the paper states the method and the provable analytic bounds, the
reproducibility repository carries the actual interval-arithmetic computation) plus the same
"archive the repo with a DOI" suggestion already logged (Round 7's M10) as a researcher action, not
a text fix. Specifically: "certified bounds (5) are not proved in the manuscript", "Proposition 8
is an assertion of a computation, not a proof", "Theorem 13 contains many unshown numerical
inequalities", and "Section 9 does not cure the lack of proof" are four restatements of one
objection already addressed by this project's standing position (stated explicitly in Round 3's
D-04/D-05 entry and reaffirmed every round since: full line-by-line interval-arithmetic derivations
live in the dedicated reproducibility repository per Rule 12, not spelled out inline in a
16-page PDF). Codex's own "What I checked successfully" section independently reproduces `H(0)`,
`H(log 3/2)`, the Mellin transform, the zero-mode residue, and every symbolic identity it attempted
— finding, in its own words, "no decisive algebraic contradiction in the central analytic
argument." No new confirmed mathematical or presentation finding beyond what Opus's pass and this
table already cover; not reopened without new evidence, per Rule 8d.

**Net effect of this round**: Opus, explicitly checking for the specific false-positive pattern
that misled Codex in Round 7 (overline/conjugate marks lost in text extraction), found zero new
mathematical errors and gave the loop's second consecutive "accept" verdict, after fixing ten
genuine presentation/labeling findings. Codex's disagreement is a scope disagreement about where
rigor should live (inline vs. repository), not a newly discovered defect, and repeats a question
this project decided explicitly and consistently since Round 3.

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices for the first
time in this loop), 17 pages.

## Round 9: seventh blind loop iteration (2026-08-06), Opus and Codex both complete

Opus, PDF-only, max effort, on the Round 8 PDF (the shared prompt file was updated after Round 8
with explicit overline/margin-checking instructions, which this run confirms working as intended:
Opus explicitly re-tested the prior round's false-positive pattern and found `pdftotext` was *also*
silently transposing digits in fractions on this PDF, e.g. rendering `9/2` as `29` -- caught before
it became a false finding). Verdict: **essentially a rigorous proof, one labeling contradiction
must be resolved**; found no new mathematical error, confirmed with an independent end-to-end
saddlepoint test and two nontrivial identity checks (Remark 5's Berg-Kruppel product matching
`exp(H)` term for term; Wirsching's own eq. (7.13) reproduced from this paper's `phi_0`). Findings,
each independently verified before fixing (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| P1 | Theorem 2's "Conditional on the certified bound of Proposition 8" (added in Round 8 to address a different reviewer's concern) now contradicts the abstract's "certify rigorously", Proposition 8's own "Rigorously,", and Section 8's "a certified, positive amplitude" -- four places asserting or implying unconditional rigor, one asserting conditionality | **confirmed, real, self-inflicted in Round 8** | fixed: removed "Conditional on..."; Proposition 8's non-constancy claim genuinely is proved unconditionally (via Arb ball arithmetic on the two-point difference alone), so Theorem 2 now cites it as such |
| P2 | Proposition 8's sentence "this step is rigorous regardless of how the grid values themselves are evaluated" is true only for the *lower* bound of the `osc(H)` enclosure; the *upper* bound additionally requires the computed grid extrema not to be underestimates, which is not independently certified for the full `2^20`-point sweep (only the two located extremal points are Arb-verified) | **confirmed, real**; also independently noted that the enclosure's upper endpoint is never used anywhere else in the paper | fixed: rewrote to scope the "regardless of arithmetic" claim correctly to the lower-bound direction (the one Theorem 2 actually uses), and stated plainly that the upper bound isn't independently certified for the full sweep |
| P3 | Symbol collision: `g` denotes both this paper's own log-kernel `g(b)=log((1-e^{-b})/b)` (used throughout) and, in three separate places, Berg-Kruppel's generic family-member solution to their functional equation -- once on the very same page as the paper's own `g` is defined | **confirmed, real**, the worst of several flagged collisions (`S`, `theta`, `h` also collide 3-4 ways each, but renaming all of them was judged out of proportion to an error-elimination pass; `g` was fixed as the one on directly adjacent text to the paper's own definition) | fixed: renamed Berg-Kruppel's generic family-member function to `psi` in all three occurrences (Section 2, twice, and Proposition 17's proof) |
| P4 | Proposition 17's proof, "Laplace transforming gives `lambda*p*G(p) = G(p/a)`", drops the boundary term from `L[psi'](p) = p*G(p) - psi(0)` without comment | **confirmed, real (minor)** | fixed: added a parenthetical noting the boundary term vanishes since the relevant solutions are supported on `[0,infinity)` with `psi(0)=0` |
| P5 | Section 4's "uniformly over every phase of `s` modulo `3^Z`" does not parse as written | **confirmed, real (minor)** | fixed: replaced with the actual object used, `rho := 2s/3^N in [1,3)` |
| P6 | Two unused numerical claims sit inside Theorem 13's *statement* rather than a remark (`E` strictly decreasing on `[19,5000]`, and `E(19)<1` itself, both explicitly flagged in the same sentence as "not used below") | fair presentation observation | not fixed this round (moving theorem-statement content to a remark is a larger structural edit than the scope of this pass; logged for a future pass) |
| P7 | Introduced a stray `--` (en dash) parenthetical aside while fixing P2, against this project's Rule 3/5c no-dash convention; the only such instance in the 17-page document | **self-caught before commit** (Rule 8c: verify one's own fix, not just the referee's original finding) | fixed: replaced with parentheses, matching the paper's own established style |
| G (literature, unverifiable from the PDF alone) | The claimed erratum in Berg-Kruppel [2] p. 179; the term "Elka functions" attributed to Wirsching | **erratum already independently verified against the actual primary-source PDF in Round 6/7**; "Elka functions" not reconfirmed this round | no action needed for the erratum (already done); "Elka functions" terminology flagged for a future literature-verification pass, not blocking |

Codex, PDF-only, max effort, launched in parallel against the same Round 8 PDF (before P1-P7 above
were applied). Explicitly re-confirmed page 9's `Lambda(-y)=overline{Lambda(y)}` is correctly
printed with the bar visible, and confirmed no inline formula runs off the margin on any of the 17
pages -- both items 5-6 of the shared prompt working as intended for Codex as well as Opus. Verdict:
**Reject**. Five findings, each independently verified before acting (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Q1 | Proposition 8's grid-rigor claim overclaims for the upper-bound direction of the `osc(H)` enclosure | same finding as P2 above | already fixed by P2; re-checked against the post-fix text, confirmed resolved |
| Q2a | Theorem 2's "Conditional on..." contradicts the paper's unconditional-rigor claims elsewhere | same finding as P1 above | already fixed by P1; re-checked against the post-fix text, confirmed resolved |
| Q2b | Restates the repository-vs-inline certification scope question | not a new defect | no action (Rule 8d): this scope question was settled explicitly in Round 3 and re-affirmed in Round 8; nothing in Codex's Round 9 report gives new evidence against that decision |
| Q3 | Lemma 9's proof asserts `(log f)'(r) = 3/r + tanh(r) - 3coth(r) < 0` for `r>0` without proof (the parenthetical about Lazarevic's inequality explicitly notes it gives `f<1` but "not this monotonicity by itself") | **confirmed, real**; independently re-derived: substituting `u=2r` gives `2r sinh(r) cosh(r) (log f)'(r) = F(u) := 3 sinh(u) - u cosh(u) - 2u`, and `F(0)=F'(0)=F''(0)=0` while `F'''(u) = -u sinh(u) < 0` for `u>0`, so three successive integrations from `0` give `F(u)<0` for all `u>0`; checked numerically against direct evaluation of `(log f)'(r)` from `r=10^{-10}` to `r=10^5`, sign matches throughout | fixed: replaced the bare assertion with the full elementary proof (the `u`-substitution identity and the triple-integration argument) |
| Q4 | Proposition 18's proof asserts `phi_0'/phi_0` is "continuous and slowly varying near `x_l`" to justify transferring eq. (7.13) from `x_l` to `x_l^+` with an `o(1)` correction, without an actual rate calculation, as suggested by the reviewer (`x_l^+/x_l = 1+O(1/l)` combined with a bound on `(phi_0'/phi_0)(x_l^+)/(phi_0'/phi_0)(x_l)`) | **confirmed, real**; independently derived from `phi_0`'s explicit closed form (Section 2): writing `v=log t`, `phi_0'(t)/phi_0(t) = B(v)/t` with `B(v)=gamma+delta_BK/v-2*beta*(v-log(-v))*(1-1/v)`; as `v -> -infinity`, `B(v) ~ -2*beta*v` while `B'(v) -> -2*beta`, so `(log B)'(v) -> 0` and `(log[phi_0'/phi_0])'(v) -> -1`, bounded; since `v(x_l^+)-v(x_l) = O(1/l)`, the mean value theorem gives the needed `phi_0'(x_l^+)/phi_0(x_l^+) = phi_0'(x_l)/phi_0(x_l)*(1+O(1/l))` directly; checked numerically with the paper's own certified constants (`gamma=-1.8649...`, `delta_BK=0.4547...`, `beta=1/(2 log 3)`) for `l` up to 320, confirming the relative change decays like `1/(3l)` as predicted | fixed: replaced "continuous and slowly varying" with the full derivation (the `B(v)` closed form, its asymptotics, and the mean-value-theorem transfer) |
| Q5 | Restates already-verified Berg-Kruppel identification concerns | same finding as G above | no action needed (already resolved in Round 6/7) |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), 17 pages.
Both new proofs (Lemma 9, page 8; Proposition 18, page 16) visually spot-checked via rendered PNG:
no truncation, no margin overflow.

**Net effect of this round**: two genuinely new mathematical gaps found and closed with complete
elementary proofs (Q3, Q4), both independently re-derived and numerically checked before writing
into the paper; the remaining three Codex findings were either already resolved by this round's
Opus-driven fixes or restate settled ground. No open findings remain from Round 9.

## Round 10: eighth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 9 PDF. Opus verdict: **accept
after minor revision**, explicitly reporting zero mathematical error found after re-deriving or
recomputing roughly sixty of the paper's constants (`H` reproduced three independent ways to 25
digits) and confirming no margin overflow or truncation on any of 17 rendered pages. Codex verdict:
**reject, major revision required**, centered on one finding both reviewers reached independently.
Findings, each independently verified before acting (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| R1 (Opus B, Codex #1, both independently) | Proposition 8's *statement* still asserted a two-sided "certified bound" `osc(H) in [D, D+M_1h]`, while the *proof* (fixed in Round 9) already conceded the upper endpoint is not independently certified for the full `2^20`-point sweep -- the statement and proof disagreed with each other | **confirmed, real, and Round 9's fix was incomplete**: it fixed the proof's wording but not the proposition's own statement, so the same defect kept resurfacing under two more independent reviewers | fixed properly this time: rewrote the proposition to assert only the certified one-sided bound `osc(H) >= 4.1874494771e-4`; rewrote the proof with a strictly stronger argument, `D := H(w_486746) - H(w_1011118)` is a difference of two individually Arb-certified point values, so `D <= osc(H)` holds unconditionally (trivially, since `H` at any two fixed domain points is `<= sup H` and `>= inf H` respectively), independent of whether the floating-point grid search actually located the true argmax/argmin; the (now explicitly non-certified, unused) upper bound is kept only as a parenthetical remark |
| R2 (Opus A, new) | The Fourier-coefficient majorant (eq. 4) rests on `\|zeta(1-i*omega)\| <= log(omega+1) + C_H`, stated as "the Euler-Maclaurin bound" with no derivation or citation, and this constant propagates into essentially every "certified" claim in the paper (eq. 5's derivative bounds, Proposition 8, Lemma 15, Proposition 16) | **confirmed, real gap**: an asserted-not-proved classical-sounding inequality is exactly the highest-yield failure mode both reviewers' general LLM-tics catalogues warn about | fixed: supplied a complete elementary proof from the classical (uncentered) Euler-Maclaurin/Euler-summation formula for zeta, with `N := floor(omega)`; the provable constant is `C_H := 1 + 1/alpha_H + (alpha_H/(alpha_H-1))*sqrt(1+1/alpha_H^2) ~ 2.405` (a valid but not optimal constant, larger than the paper's original unproved `~2.182`); verified numerically against `mpmath.zeta` up to `omega=10^6` with wide margin; the two downstream tail-sum numbers that depend on `C_H`'s value were recomputed and updated (`9.05e-20 -> 9.41e-20` for `m>4`, `2.71e-43 -> 2.80e-43` for `m>10`, `3.7e-19 -> 3.8e-19` for the two-point difference bound); eq. (5)'s printed 17-digit `sup\|H'\|`, `sup\|H''\|` bounds are unaffected at that precision since the tail's contribution is many orders below the printed digits either way |
| R3 (Codex #3, new) | Proposition 18's proof uses `tau_l` in `log Lambda_l = H(w_0(tau_l - c)) - H(w_0(tau_l)) + o(1)` without ever defining it within the proposition (it is defined earlier, inside Theorem 1's proof, for a different sequence) | **confirmed, real**; the intended definition is `tau_l := -log(x_l^+)`, matching the pattern used throughout the paper (`tau = -log t`) applied at `t = x_l^+` | fixed: added the explicit definition at the start of the "For the value of Lambda_l" paragraph |
| R4 (Opus D, new) | Proposition 17's proof says "the third of the three coincidences asserted in the proposition above. The other two are the chain rule: ..." but the two "chain rule" identities that follow are not among the proposition's three actual claims (`f=Q(log p)`, the saddle location, the `P(tau)` formula) -- a broken/confusing cross-reference | **confirmed, real**: the chain-rule identities are a consistency check on the *first* claim (`f(p)=Q(log p)` also matching at the level of first and second derivatives), not separate propositional claims | fixed: reworded to "the first of the proposition's three claims... This is an identity in y, not merely a value match: the chain rule... confirms it also at the level of Q' and Q''" |
| R5 (Opus E, new) | Section 2's parenthetical calling Berg-Kruppel's dilation-3, lambda=2/3 functional equation (already displayed with 3 substituted in) "their generic family member" is self-contradictory (it is a specific member, not the generic one), and "distinct from this paper's own `g` introduced below" refers to a symbol (`g`) not present in that sentence, since Round 9 already renamed this exact object to `psi` | **confirmed, real**; a leftover from before Round 9's `g`->`psi` rename that became stale and confusing once the rename made the warning's referent disappear | fixed: deleted the now-incorrect/stale parenthetical entirely |
| R6 (Opus F, new) | The abstract states the paper's scope without the caveat the Discussion section already states plainly ("Conjectures 1 and 2... are untouched here, and the full theorem is not established by this paper") -- a reader scanning only the abstract could overestimate what is resolved | fair presentation observation, not a mathematical error | fixed: added "This settles Conjecture 3 alone; Wirsching's other two conjectures, and positive predecessor density itself, remain open." to the abstract's final sentence; matches the Discussion's own wording (Rule 8b re-check) |
| R7 (Opus + Codex, both independently, writing review) | Two sentences flagged as the clearest LLM-writing tells in the manuscript by *both* independent reviewers: "Neither statement had been settled. This paper settles both, in opposite directions." (subject-is-the-paper, promotional cadence) and "The two routes agreeing to 18 digits is itself strong evidence the floating-point route's own error estimate is not being violated by an unmodeled effect." (Rule 5c meta-honesty/confidence-auditing, banned outright) | **real, per Rule 5c**, and the convergent independent flagging from two different reviewers is exactly the signal Rule 8/15 says to trust | fixed: deleted the "This paper settles both" framing (theorems now speak for themselves); deleted the meta-honesty sentence entirely (the Arb-certified route is already fully rigorous on its own and needs no "evidence" framing); also reworded "The two theorems have a single common source" (same subject-is-the-paper pattern) to "A single computation underlies both theorems" |
| R8 (Opus I, minor) | `M_2`, `M_3` defined in Lemma 9's statement and never referenced again anywhere in the paper | **confirmed, real, minor** | fixed: dropped the unused names, kept the numeric bounds themselves (`sup\|kappa_2\|<=3`, `sup\|kappa_3\|<=2+2^{5/2}`) |
| R9 (Opus C, Codex writing review, both) | 8 further unflagged symbol collisions beyond the `g` fixed in Round 9 (`S`, `f`, `e`, `Lambda`, `N`, `D`, `R`, `M`, `h`, `theta`, `B`, each reused 2-4 times for unrelated objects), and both reviewers separately flag the defensive-parenthetical pattern used to manage existing collisions as the single most legible LLM signature in the paper | **confirmed as real presentation debt**, but out of proportion to fix in one pass (renaming 8+ symbols across a 17-page document under time pressure risks introducing new errors) | not fixed this round; logged here for a future dedicated pass, per Rule 8e (every path a critique surfaces gets tracked) |
| R10 (Codex #2, restates settled ground) | Repeats the repository-vs-inline certification scope question, and criticizes the reproducibility repo as an "unversioned GitHub URL" without a commit hash or archived artifact | not a new defect | no action (Rule 8d): the scope question was settled explicitly in Round 3 and re-affirmed in Round 8; a versioned/archived-artifact convention is a repo-tooling question for `papers/01-wirsching-conjecture3/DATA_REPO.md`, not a paper-text defect, and is out of scope for this critique loop |
| R11 (Codex #4, restates settled ground) | Prose repeatedly calls numerical work "exact," "rigorous," "certified" in places the reviewer felt overclaim | mostly addressed already by R1/R2's rigor-scoping fixes; no further specific instance identified beyond those | no separate action; covered by R1, R2 |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), 17 pages.
All five edited passages (zeta-bound proof p.6, Proposition 8 p.8, Proposition 17 p.14,
Proposition 18 p.16, abstract p.1) visually spot-checked via rendered PNG: no truncation, no
margin overflow, and the mathematics reads correctly.

**Net effect of this round**: the Proposition 8 statement-vs-proof mismatch had now been flagged,
independently, by three different reviewer passes across two rounds (Opus and Codex in Round 9,
Opus and Codex again in Round 10) -- Round 9 only fixed the proof paragraph, not the proposition's
own statement, so the underlying defect kept resurfacing. This round fixes it properly, with a
strictly stronger argument than either reviewer asked for (the lower-bound direction is now
unconditionally rigorous, not merely "safely far from the floating-point error margin"). It also
closes a genuine, previously-unnoticed gap (the uncited zeta bound underlying every "certified"
numerical claim in the paper) and three smaller real defects (undefined `tau_l`, a broken
cross-reference, a stale notation parenthetical), plus two Rule 5c writing-tell fixes independently
flagged by both reviewers. One item (the broader symbol-collision cleanup) is deliberately deferred
to a future round rather than rushed. Per the researcher's explicit instruction, Round 11 is not
launched automatically; the loop pauses here pending authorization.

## Round 11: ninth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 10 PDF. Opus verdict: **accept
after minor revision**, reporting no substantive mathematical error after recomputing essentially
every constant in the paper (including a 40-digit cross-check of Berg-Kruppel's `C_P` two
independent ways) and confirming the abstract, both theorem statements, Corollary 3, and Section 8
agree with each other clause by clause. Codex verdict: **would not recommend acceptance as
submitted**, centered on the same repository/certificate-reproducibility scope question raised in
prior rounds (Rule 8d: already settled, no new action), plus one specific overclaim both reviewers
independently converged on. Findings, each independently verified before acting (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| S1 (Opus F1, Codex #2, both independently) | Section 8's Discussion stated as fact "`H(0) - min H = 5.25e-6` against a total oscillation of `4.19e-4`", but Proposition 8 explicitly disclaims certifying the grid search's located extrema ("this search is only a heuristic... not itself part of the certificate"); the Discussion quietly used the uncertified `min H` as if proven | **confirmed, real**: two independent reviewers converged on the exact same sentence in the exact same section, the strongest possible signal under Rule 8/15; the underlying number itself is correct (verified: `H(0) - H(w_1011118) = 5.2523e-6` from the two Arb-certified point values already in Proposition 8's proof), only the label "min H" and "total oscillation" overclaimed | fixed: reworded to "the smallest of the two values of H certified in Proposition 8: `H(0) - H(w_1011118) = 5.25e-6`, against a certified oscillation of at least `4.19e-4`", with an explicit parenthetical that whether `w_1011118` is the true minimizer is not certified |
| S2 (Opus F2, new) | Lemma 15's proof states `2e*eta_0 = 4.9859...` as an approximate equality; recomputing `2*e*0.9170912` (the paper's own stated bound on `eta_0`) gives `4.98582...`, so the printed digit is wrong (should round to `4.9858`, not `4.9859`) | **confirmed, real, minor**: independently recomputed, `2*e*eta_0 = 4.985824...`, printed value's 4th decimal digit is off by one | fixed: changed the false equality `= 4.9859...` to the true, still-sufficient inequality `<= 4.9859` (the argument only ever needed `2*e*eta_0 <= 5`, so the weaker true statement costs nothing) |
| S3 (Opus F3, new) | Proposition 8's proof states the `\|m\|<=10` truncation's discarded modes are bounded by `2.80e-43`, but this is the one-sided majorant tail (`m>10` only); the actual pointwise truncation error also includes the `-m` modes, so should be `2x2.80e-43` -- inconsistent with the adjacent `\|m\|<=4` computation two paragraphs earlier, which correctly doubles for both signs | **confirmed, real, minor**: the search this bounds is explicitly "only a heuristic... not part of the certificate," so nothing downstream depended on the stale number, but the internal inconsistency between two adjacent computations was real | fixed: `2.80e-43` -> `2x2.80e-43 = 5.60e-43`, with a clause naming why (`m` and `-m` combined) |
| S4 (Opus F4, new) | `tau_l` is defined with two different meanings in two different proofs (Theorem 1's proof: `tau_l = -log z_l`; Proposition 18's proof, added in Round 10: `tau_l := -log x_l^+`) -- harmless since each proof is self-contained, but notable given how obsessively this paper otherwise flags every other symbol collision | **confirmed, real, cosmetic**: consistent with the paper's own established convention of flagging collisions rather than silently allowing them | fixed: added "(locally to this proof only, distinct from the `tau_l` of Theorem 1's proof)" at the point of Proposition 18's definition |
| S5 (Opus F6, new) | Lemma 9's proof: "the first excludes the poles of `coth`, since `Re(w/2)=b/2>0` never approaches `pi*i*k`" compares a real quantity (`b/2`) to a purely imaginary one (`pi*i*k`), a category mismatch in the prose even though the underlying point is correct | **confirmed, real, cosmetic** | fixed: reworded to state the actual inequality being used, `\|sinh(w/2)\| >= sinh(b/2) > 0`, excluding the poles, before noting `Re(w/2)=b/2>0` |
| S6 (Codex #1, restates settled ground) | Repeats that the reproducibility repository is "not a proof artifact contained in the submission" and asks for a version-pinned archived supplement with exact interval outputs, library versions, and commit hashes, rather than a mutable GitHub URL | not a new defect | no action (Rule 8d): this is the same repository-vs-inline certification scope question settled explicitly in Round 3 and re-affirmed in Rounds 8 and 10 |
| S7 (Codex #3, restates settled ground) | Lists several "direct evaluation" claims (Theorem 13's `E(19)<1`, Lemmas 9-12's constants, Lemma 15's numerical estimates) as proof gaps without reproducible interval data shown inline | same underlying scope question as S6 | no separate action; covered by S6's disposition |
| Opus F5, F7, F8, F9 (minor/out of scope) | F5: Theorem 13's `N>=19` hypothesis and Lemma 11's `N>=3` claim are both stronger than what their proofs actually use. F7: the reproducibility repo's org name ("faculdade") reads like a placeholder to a blind reviewer with no repo access. F8: pointers into Wirsching 2003 and Berg-Kruppel 1998 cannot be checked from the PDF alone by a blind reviewer (already independently re-verified against the primary sources in Round 6/7, per this project's own records, which a PDF-only reviewer cannot see). F9: the abstract leads with the certification result rather than naming the saddlepoint transfer of Sections 4-6, which Remark 5/Corollary 3 concede is the more novel contribution | none confirmed as defects requiring a text fix this round | not acted on: F5 is true but harmless (weakening one's own hypothesis costs nothing but isn't an error); F7 is a repo-naming question outside this critique loop's scope; F8 is already resolved (Round 6/7) but invisible to a blind PDF-only reviewer by design; F9 is a framing preference, not a correctness issue -- logged here in case a future round converges on the same point |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), 17 pages.
All four edited passages (Lemma 9 p.9, Lemma 15 p.12, Proposition 8 p.8, Proposition 18 p.16,
Discussion p.17) visually spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: the one substantive finding (S1) was independently reached by both
reviewers reading the same sentence in the same section, the clearest possible instance of the
convergent-signal pattern Rule 8/15 exists to catch; both Opus and Codex explicitly stated they
found no error in the paper's mathematical core after extensive independent recomputation. The
remaining fixes are small (a wrong digit, a doubling inconsistency, a harmless notation collision,
an imprecise sentence), and two reviewer requests restate the already-settled repository-scope
question from Round 3. Per the researcher's explicit instruction, Round 12 is not launched
automatically; the loop pauses here pending authorization.

## Round 12: tenth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 11 PDF. Opus verdict: **accept
after minor revision**, again reporting no substantive mathematical error after re-deriving
Proposition 6's Mellin residues from scratch and independently confirming every one of 40+ numeric
bounds. Codex verdict: **would not recommend acceptance**, citing two claimed mathematical errors
as "major"/"moderate" findings. **Both of Codex's central findings turned out to be false
positives**, caught and discarded per Rule 8c before any text was touched; see below. Genuine
findings, each independently verified before acting:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| T1 (Codex #1, FALSE POSITIVE) | Claimed the printed bound `\|Gamma(-i*omega)\| <= 3*pi/omega * e^{-pi*omega/2}` (p. 7) does not follow from `\|Gamma(-i*omega)\|=sqrt(pi/(omega*sinh(pi*omega)))` and `sinh(x)>=e^x/3`, and is false for large omega, since the correct bound has a square root: `sqrt(3*pi/omega)`. | **FALSE POSITIVE, confirmed by direct inspection**: rendered p. 7 at 200dpi shows the bound printed exactly as `\|Gamma(-i*omega_m)\| <= sqrt(3*pi/omega_m) * e^{-pi*omega_m/2}`, with the square root radical clearly visible. `main.tex` itself has always had `\sqrt{3\pi/\omega_m}` at this location. `pdftotext` silently drops the radical sign (a new extraction-artifact pattern, distinct from the overline-dropping one found in earlier rounds), producing flat text that reads as the false, radical-free version Codex quoted | no action on the paper; **the shared review prompt was updated** (new item 7) so future rounds check for this specific pattern before reporting it |
| T2 (Codex #3, FALSE POSITIVE) | Claimed Proposition 16's `T4` estimate on p. 13 prints `0.00652*e^{0.00652}/5` (dividing the whole exponential term by 5), which does not follow from `\|w*-w_0\|<=0.00652/B_0` at `B_0>=5`; the correct substitution would keep the `/5` inside the exponent | **FALSE POSITIVE, confirmed by direct inspection**: rendered p. 13 at 200dpi shows `0.00652 e^{0.00652/5}`, with `0.00652/5` clearly inside the exponent's superscript, exactly the correct substitution (using the worst case `B_0=5` inside `e^{0.00652/B_0}`). Verified numerically too: `0.00652*e^(0.00652/5) = 0.0065285...`, which combined with `sup\|H''\|` gives `0.01338 < 0.0135` exactly as the paper concludes; Codex's misreading (`0.0013125...`) would not even have been inconsistent with `<0.0135`, so the "error" was purely a misreading, not a math check that failed | no action on the paper; **the shared review prompt was updated** (new item 8) covering this "fraction flattened out of a superscript" pattern |
| U1 (Opus F1, new, real, self-inflicted) | The Discussion (added in Round 11) says "against a certified oscillation of at least `4.19e-4`", but the only proven fact is `osc(H) >= 4.1874494771e-4`, which is *less than* `4.19e-4`; rounding a proven lower bound *up* makes the claim unjustified (need `osc(H)>=4.19e-4` to be proven, and it isn't) | **confirmed, real, and my own error**: introduced in my own Round 11 rewrite of this sentence, caught by a fresh Opus reviewer one round later | fixed: `4.19e-4` -> `4.18e-4` (verified `4.18e-4 <= 4.1874494771e-4`, so this direction is safe) |
| U2 (Opus F3, new, real, minor) | Proposition 18's proof (p. 16) uses `\to` (a limit arrow) to introduce `(2/3)*Lambda_l*(1+o(1))`, but the right-hand side still depends on `l` through `Lambda_l`, so it isn't a limit in the usual sense; an equality is the accurate statement | **confirmed, real, cosmetic** | fixed: `\to` replaced with `=` |
| U3 (Opus F2, new, real, minor) | Lemma 15 states and proves `0 <= g_tau(w_0)-g_tau(w*) <= 5.77e-5/B_0`, a claim never used anywhere else in the paper; its numeric proximity to Proposition 16's *different* `T1` bound (`5.78e-5/B_0`, for the smooth system, not the true one) one page later reads like a typo of the same quantity when it is not | **confirmed, real**: grepped the whole document, `g_tau(w_0)-g_tau(w*)` appears only in Lemma 15's own statement and proof, never cited downstream (Proposition 16's `T1` is bounded independently, from `g_{0,tau}`, not this clause) | fixed: deleted the unused clause from Lemma 15's statement and the corresponding paragraph from its proof, consistent with how unused `M_2, M_3` were handled in Round 10 |
| Opus F5, F6, F7, F8, F9, F10, F12, F13, F14 (minor/deferred) | Further symbol collisions (12 more listed); undefined "Elka functions" term; p.1 quote lacks a page locus; two different loci given for the same Berg-Kruppel constants; abstract's "smooth part plus H" elides the doubly-exponential remainder `Delta`; one overclaimed "exactly"; an unsupported priority claim ("neither statement had been settled"); a theorem statement that names its own proof mechanism inline; and a genuine strengthening opportunity (Proposition 18's argument doesn't actually need Conjecture 3 at all, only the phase-independent shift estimate) | none confirmed as requiring a text fix this round | not acted on: F5 restates the already-deferred (Round 10/11) symbol-collision cleanup; F6-F10, F12, F13 are minor presentation points logged here in case a future round converges on the same ones; F14 is a real, interesting observation but is a suggested strengthening, not a defect, and changing what a proof claims to establish is a bigger edit than this pass's scope |
| Codex #2, #4, #5 (restates settled ground) | Repeats the repository-vs-inline certification scope question (#2, #4) and asks for documentary support for the claimed Berg-Kruppel sign-error correction (#5) | not new defects | no action (Rule 8d): #2/#4 restate the scope question settled since Round 3; #5 restates a concern already addressed (the paper's own differentiation was independently re-verified as correct in this round's checking too, by both reviewers) |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), still 17
pages (U3's deletion reflowed the Discussion from p.17 onto p.16, with no change in page count).
All three edited passages (Lemma 15 p.12, Proposition 18 p.16, Discussion p.16) visually
spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: the most valuable outcome was catching two independent false
positives before touching the paper at all, both traced to genuine new `pdftotext` extraction
failure modes (dropped square-root radicals, flattened exponent fractions) rather than to real
defects; the shared review prompt was updated so future rounds check for both before reporting.
Separately, a real rounding-direction error introduced in this project's own Round 11 fix was
caught and corrected (U1), along with two small cosmetic issues (U2, U3). Both reviewers again
found no error in the paper's mathematical core after extensive independent re-derivation. Per the
researcher's explicit instruction, Round 13 is not launched automatically; the loop pauses here
pending authorization.

## Round 13: eleventh blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 12 PDF. Opus verdict: **accept
after minor-to-moderate revision**, again reporting no mathematical error after re-deriving every
identity by hand, recomputing ~25 constants to 40-80 digits, reproducing Proposition 8's grid
search exactly, confirming Berg-Kruppel's product identity to 60 digits, and validating the whole
transform-to-density chain end-to-end via independent numerical Fourier inversion. Codex verdict:
**major revision, not rigorous as a standalone submission**, entirely on the repository/certificate
reproducibility question already settled since Round 3 (Rule 8d, no action) plus one convergent
point with Opus. Findings, each independently verified before acting (Rule 8c):

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| V1 (Opus F1, MAJOR, new) | The identification `varphi_0 = ` Berg-Kruppel's (9.6) is used throughout but never cited to the specific place in Wirsching [1] where he makes that identification himself; every other imported fact from [1] is pinned to an equation number, making this omission conspicuous. Without it, Theorem 1 proves a true statement about *a* comparison function, not necessarily Wirsching's Conjecture 3 as he stated it | **confirmed as a real citation gap, but the underlying identification is correct**: checked directly against the primary source (Wirsching 2003, cached at `/tmp/posden.txt` from earlier primary-source verification work in this project), his own equation (7.11) defines `varphi_0 := g_0`'s asymptotic form and explicitly cites Berg-Kruppel [1 in his numbering] by name at exactly that point, matching this paper's own eq. (9.6) reproduction of Berg-Kruppel's formula term for term | fixed: added an explicit citation to Wirsching's equation (7.11) at the point `varphi_0` is first introduced in the Introduction, stating plainly that the identification is Wirsching's own choice, not a substitution made in this paper |
| V2 (Opus F6, Codex #3, both independently, convergent) | The abstract says the log-Laplace transform "decomposes as a smooth part plus a periodic correction H", but the actual exact decomposition (Theorem 4) is three terms, `L = Q + H + Delta`, with `Delta` doubly exponentially small but not zero | **confirmed, real**: two independent reviewers converged on the same abstract sentence | fixed: abstract now says "decomposes as a smooth part, a periodic correction H, and a doubly exponentially small remainder" |
| V3 (Opus F5 in Round 12, repeated as F5 in Round 13) | Theorem 13's *statement* contains an unproved, explicitly-unused numerical range claim ("E is also strictly decreasing and satisfies E(N)<=4.18*N^(-1/2) throughout 19<=N<=5000 (checked directly in the accompanying repository); neither fact...is used below") -- flagged once in Round 12 and deferred, flagged again by the same reviewer type in Round 13 | **confirmed, real, and now flagged twice across two rounds**, past the threshold this project uses for acting on a deferred item | fixed: moved the sentence out of the theorem environment into its own remark immediately following, consistent with how Theorem 2's proof-mechanism content was already kept out of theorem statements elsewhere |
| V4 (Opus F3, new, minor) | Theorem 13's proof locally defines `c := theta_N*sqrt(V)` on p. 11, colliding with the globally fixed `c := log 3` used throughout the rest of the paper and on the same page | **confirmed, real**: an actual, if harmless, symbol collision reusing a globally-fixed letter, notable because the paper otherwise flags every other collision explicitly | fixed: renamed the local constant to `c_0`, with an explicit note that it is distinct from `c:=log3` |
| Opus F2 (MAJOR), Codex #1/#2 (restates settled ground) | Repository/certificate reproducibility: the Arb ball arithmetic certificates behind Proposition 8, eq. (5), and Theorem 13's constant chain are not shown inline or archived with a DOI, only linked via a mutable GitHub URL | not a new defect | no action (Rule 8d): this is the same repository-vs-inline certification scope question settled explicitly in Round 3 and reaffirmed in Rounds 8, 10, 11, and 12; both reviewers independently reproduced every one of the certified numbers themselves and reported no doubt about their correctness |
| Opus F4, F7-F12 (minor/deferred) | Theorem 1 doesn't explicitly state uniformity of its o(1) error terms over the class (true but implicit from the rate bounds already given); Theorem statements (2, 17, 18) cite their own proof mechanism inline; Proposition 17 miscounts its own claims as "three" when a fourth (the Y-log Y saddle equation) is also asserted; one punctuational dash; Corollary 3 and Remark 5 state the same fact twice; "de Bruijn-Mahler phenomenon" may not be an established term; the oscillation of Theorem 2 is asymptotically real but numerically unreachable at any computable t | none confirmed as requiring a text fix this round | not acted on: logged here in case a future round converges on the same points, consistent with this project's practice of prioritizing convergent/repeated findings over first-time minor ones |
| Codex #4 (minor, not acted on) | The integral display `varphi(x) = (3/2)*int_{3x-2}^{3x} varphi` omits the dummy variable and differential | not confirmed as an error; standard shorthand also used in Wirsching's own primary source for the same kind of display | no action: stylistic preference, not incorrect as printed |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), still 17
pages. All four edited passages (abstract/introduction p.1, Theorem 13/new Remark 14 p.11, the
`c_0` rename p.11) visually spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: the most substantive fix was closing a genuine citation gap (V1)
flagged by Opus as the paper's single most severe finding; verifying it required going back to the
primary source (Wirsching 2003) rather than trusting the reviewer's framing, which confirmed the
underlying mathematics was already correct (this project's own literature notes, `L-002.md`, had
already located and read the exact passage, Wirsching's eq. 7.11) and that the fix was purely a
missing citation, not a hidden error. Two reviewers converged independently on the abstract's
`Delta`-dropping overclaim (V2), and one item deferred once in Round 12 was flagged again and
finally fixed (V3). Per the researcher's explicit instruction, Round 14 is not launched
automatically; the loop pauses here pending authorization.

## Round 14: twelfth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 13 PDF. Opus verdict: **minor
revision**, again reporting no mathematical error after re-deriving every identity by hand and
recomputing ~30 constants, plus three checks the paper itself omits (Berg-Kruppel's product
confirmed to 48 digits, the saddlepoint bridge validated end-to-end over `tau=20..20000`, and
`R(s)` recomputed by direct quadrature). Codex verdict: **major revision**, centered again on the
repository/certificate scope question. Findings, each independently verified before acting:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| W1 (Opus finding 1, MAJOR, partially addressed) | Asked that Conjecture 3, the `A-tilde_delta` definition, Wirsching's (7.5), and Berg-Kruppel's `f''` display all be quoted verbatim from the primary sources, since Theorem 1's entire content rests on these transcriptions being accurate | **checked against the actual primary source** (`wirsching2003-posden.pdf`, archived this session): Conjecture 3 is already displayed verbatim in a `\begin{conjecture}` block (since Round 4); (7.5), (7.12), (7.13) are already displayed as formulas with equation numbers; Berg-Kruppel's `f''` display is already quoted verbatim with a page number (since Round 3). The one real gap was `A-tilde_delta`'s definition, given only in paraphrase; **read Wirsching's actual (1.5) and (3.2)** (`A_delta := {(k_l): \|l-k_l\|<=delta*sqrt(l)}`, and `A-tilde_delta` translating a 3-adic digit sum into this class) and confirmed the paper's paraphrase (`\|3^l*x_l\rfloor=k_l` with the same inequality) is an exact match, not just a plausible restatement | no text change: the paraphrase was independently verified as faithful to the primary source, which is a stronger form of closure than adding more verbatim blocks; logged here as the specific check performed, per Rule 11 |
| W2 (Opus finding 3, MODERATE, new, real) | The series reversion `Y-log Y=tau+r -> Y=tau+log(tau)+r+(log(tau)+r)/tau+O(tau^{-2}log^2(tau))` on p.15 is asserted with no derivation, and the paper never explains why an `O(tau^{-2}log^2 tau)` error in `Y` becomes the weaker `O(tau^{-1}log^2 tau)` error in `P(tau)` two lines later | **confirmed, real gap**: independently re-derived the reversion (one iteration of `Y=W+log Y`, `W:=tau+r`, plus `log W = log tau + O(1/tau)`) and the error-amplification mechanism (`P`'s leading term in `Y` is `-Y^2/(2c)`, so `dP/dY = -Y/c+O(1)` turns an `O(tau^{-2}log^2 tau)` input error into an `O(tau^{-1}log^2 tau)` output error, exactly the rate printed) | fixed: added both derivations inline, compactly, matching the paper's existing density |
| W3 (Codex finding 3 + Opus finding 7 item, convergent, real) | Codex read "neither fact, nor `E(19)<1` itself, is used anywhere in this paper" (a remark) against Theorem 13's own statement, which still asserted `E(19)<1` as part of the theorem, and flagged this as an internal contradiction; Opus separately flagged the `N>=19` hypothesis as decorative, since nothing in the proof requires it | **confirmed, real** (not a contradiction of truth, but a genuine confusion of exposition: asserting a fact in a theorem and then saying it's unused two sentences later, without connecting the two, reads exactly as inconsistent as Codex described) | fixed: moved `E(19)<1` out of Theorem 13's statement into the existing remark (joining the other two already-flagged "proved but unused" facts), and added one sentence explaining why `N>=19` is still kept as the hypothesis (it's where the bound first becomes informative, i.e. `<1`, not because the proof needs it) |
| W4 (Opus finding 5 + Codex finding 4, convergent, real) | Corollary 3 bundles two claims of very different depth: that `e^H` equals Berg-Kruppel's product *as a function* (pure algebra, Remark 5, no saddlepoint machinery needed) and that this function is genuinely the periodic factor multiplying `phi`'s own asymptotic (needs the full Theorem 13 + Propositions 17-18 chain). Both reviewers independently flagged this as unclear, and Codex separately noted the identification "is not cleanly derived" | **confirmed, real**: verified by tracing which downstream results each half of Corollary 3 actually depends on; Remark 5's algebraic identity depends on nothing but Theorem 4, while Corollary 3 itself depends on the full chain | fixed: added one clause to Corollary 3's own statement explicitly separating the two parts and pointing to where each is proved; added the missing `\label` to Remark 5 (it had none) to make the new cross-reference possible |
| W5 (Opus finding 4, minor, real) | An `a` collision in Theorem 13's proof: the generic bound `int_a^infty (1+y^2)^{-N/2} dy <= ... at a=theta_N` reuses `a`, which is both `Q`'s linear coefficient and Berg-Kruppel's dilation parameter elsewhere in the paper | **confirmed, real, minor**: a genuine third meaning of `a` in a paper that otherwise flags every other collision explicitly | fixed: renamed the generic integration-bound variable to `u` |
| W6 (Opus finding 7, minor, real x3) | (a) "the decomposition ... is unique" overstates what's proved (only `H`, given `Q`, is uniquely determined); (b) "the smallest of the two values" is a grammar error for a comparison of two things; (c) "the saddlepoint bridge of Sections 4 and 5" omits Section 6, which is where `log(phi_0)` actually enters | all three **confirmed, real, minor** | fixed: (a) reworded to "Given Q, H is uniquely determined by..."; (b) "smallest" -> "smaller"; (c) added Section 6 to the cross-reference |
| Opus finding 7 (Lagrange parenthetical) | Flagged "(the Lagrange form is invalid for a complex-valued function of a real variable)" in Lemma 12 as over-explaining a trivial fact to a specialist audience | **considered, disagreed with the finding**: this is not a textbook-trivia aside but a specific, easy-to-get-wrong technical justification for why the proof uses the integral form of Taylor's theorem rather than the more familiar Lagrange form; cutting it would remove real content, not padding | not fixed: kept as is, with reasoning recorded per Rule 8c (a critique finding can be wrong, and this one, on reflection, is) |
| Opus finding 6 (abstract "in 1998") | Suggested the abstract's "gave this correction... as an infinite product in 1998" should specify "in the proof of their Proposition 9.3" | **considered, not applied**: Corollary 3 and Remark 5 already give this precise locator; adding it to the abstract as well would be the kind of over-qualification Rule 5c's checklist warns against in the highest-risk section of the paper | not fixed |
| Opus finding 2 (MAJOR) + Codex finding 1 (MAJOR), both reviewers, again | Print the actual Arb ball enclosures behind Proposition 8 and eq. (5) inline (Opus specifically: the four enclosures for `Hhat(1)..Hhat(4)`), replace "exactly" with "with rigorous enclosures", archive the repository with a DOI instead of a mutable URL | not a new defect, but the concrete sub-ask was genuine and actionable | **partially fixed, researcher-directed** (see post-round addendum below): the four `Hhat(m)` enclosures are now printed inline with a full recombination showing they reproduce the already-certified interval, and "exactly" was corrected. The DOI-archiving half of the ask is explicitly left open by the researcher's own choice, not deferred under Rule 8d this time; this is no longer a "no action" row |
| Codex finding 2 (MODERATE, restates settled ground) | Lemma 9, 11, 12's numerical constants (0.114, 0.0119, the `Sigma` tail bound, etc.) are asserted rather than shown as full derivations | not a new defect | no action: this is a milder restatement of the same repository/rigor-level scope question as above; the derivations that exist in the paper (truncation + tail bound + numerical evaluation) are the level of detail this project's papers use throughout, consistent with Rule 12 |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), still 17
pages. All edited passages (Corollary 3 / intro p.2, Theorem 4's uniqueness remark p.4, Theorem
13's `E(19)` remark and `u`-rename p.11, the series reversion p.15, the Discussion's "smaller" p.17)
visually spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: one finding (W1) was resolved by going back to the actual primary
source and verifying the paper's paraphrase directly, closing it more strongly than a text edit
would have; two more (W2, the series reversion; W3/W4, convergent findings from both reviewers)
were genuine gaps, now fixed. One finding (the Lagrange parenthetical) was considered and rejected
as wrong after independent judgment, per Rule 8c cutting both ways. The repository/certificate
question was raised again, and this time, per the researcher's explicit direction, partially acted
on (see below) rather than deferred again.

**Post-round addendum (researcher-directed, same session)**: the researcher was shown a plain-language
explanation of the repository/certificate disagreement and chose the middle option: act on Opus's
specific, concrete sub-ask (print the four Arb ball enclosures behind Proposition 8's Fourier-series
route) without the larger infrastructure change (DOI-archiving the repository). Computed
$\hat H(1),\ldots,\hat H(4)$ independently in `python-flint` (Arb bindings) at 250-bit working
precision; cross-checked all four against the earlier, lower-precision values an Opus subagent had
independently computed in Round 12 (agreement to the ~10 digits that round's numbers were given to);
verified the four enclosures reproduce the already-printed $H(0)-H(\log(3/2))$ interval directly
(summing them gives $-0.0003771902809439858148\ldots$, matching the paper's floating-point value to
19 digits, with ball radius $<10^{-70}$). Inserted the four enclosures inline in Proposition 8's
proof, plus one clause explaining the direct recombination; also fixed the imprecise "summing the
first six terms exactly" (Opus's finding 2(a) from Round 14's report, not previously tabled) to "with
rigorous ball enclosures". Recompiled clean (zero warnings), paper grew from 17 to 18 pages (expected,
given the added content, not a defect). This closes the single most concrete, repeatedly-actionable
piece of the repository/certificate finding; the larger DOI-archiving ask remains open, by the
researcher's own choice, not a lapse in follow-through.

Per Rule 12, also mirrored this into the public reproducibility repository (cloned to a scratch
directory, since it wasn't checked out locally): `certify_H_nonconstancy.py` (which already computed
and summed these same four coefficients, previously without printing the raw complex values) now
prints `Hhat(1)..Hhat(4)` explicitly at 100-decimal precision, immediately reproducing all digits
printed in the paper; re-ran the script end to end and confirmed the pre-existing summed-difference
certificate (`D_4 = -0.0003771902809439858148...`) matches this session's independent computation
to every printed digit, a strong cross-check from a script written in an earlier, unrelated session.
README updated to describe the new output. Committed and pushed to
`github.com/faculdade/wirsching-conjecture3-proof` (confirmed public, HTTP 200, after push).

Per the researcher's explicit instruction, Round 15 is not launched automatically; the loop pauses
here pending authorization.

## Round 15: thirteenth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 14 PDF (post-addendum, with the
four Arb enclosures already inline). Opus verdict: **accept after minor revision**, again reporting
the mathematics correct after extensive independent re-derivation (Berg-Kruppel's product confirmed
to 57 digits, Proposition 17 validated end-to-end numerically). Codex verdict: **reject**, again
centered on the repository/certificate scope question (Rule 8d, no new action; see below), plus one
finding that was genuinely new and serious. Findings, each independently verified before acting:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| X1 (Opus finding F1, MODERATE, new, real, self-inflicted) | The series reversion added in Round 14 (`Y-log Y=tau+r` reverted to `Y=tau+log(tau)+r+(log(tau)+r)/tau+O(tau^{-2}log^2 tau)`) claimed this followed from "one iteration of `Y=W+log Y`", but a single iteration only achieves `O(log(W)/W)` accuracy -- one order too coarse, off by a factor of `tau` from the claimed final error, and the discarded term is actually the same size as the term being kept | **confirmed, real, and my own error introduced in Round 14**: independently re-derived the reversion from scratch and verified numerically against the exact root of `Y-log Y=tau+r` (via Newton's method) at `tau=50,100,...,10^6`; one iteration's error decays like `log(tau)/tau` (e.g. `0.077` at `tau=50`), while a correct second-order expansion (retaining the `log(W)/W` term inside the first correction) reproduces the paper's already-correct final formula with error matching `O(tau^{-2}log^2 tau)` to high precision | fixed: rewrote the derivation to include the missing intermediate step (`delta=log(W)/W+O(log^2 W/W^2)`), explicitly, so the algebra now actually supports the stated final rate |
| X2 (Codex finding 3, Opus finding F8, convergent, real) | Theorem 1's proof states `lambda_l := 3^l x_l/l -> 1` at rate `O(delta/sqrt(l))`, but the floor in `A-tilde_delta`'s definition (`floor(3^l x_l)=k_l`) contributes an extra `O(1/l)` term the stated rate omits | **confirmed, real**: `\|3^l x_l - k_l\|<1` combined with `\|l-k_l\|<=delta*sqrt(l)` gives `\|3^l x_l - l\| < 1+delta*sqrt(l)`, so the correct rate is `O(1/l)+O(delta/sqrt(l))`, not just the second term; independently verified both reviewers reached the same finding from different angles | fixed: added the missing `\|3^l x_l - k_l\|<1` step and corrected the stated rate |
| X3 (Opus finding F6, minor, real) | Theorem 2's statement said the stronger asymptotic fails "by Proposition 8's unconditionally proved non-constancy of H", but the actual proof (p. 16) additionally needs Theorem 13, Proposition 17, and Lemma 16 -- the theorem statement misattributed its own proof to a single result | **confirmed, real** | fixed: removed the "by Proposition 8's..." clause from the theorem statement entirely (the mechanism belongs in the proof, which already states it correctly) |
| X4 (Opus finding F7, minor, real) | "so `w_0(tau_l) mod c -> 0`" is imprecise: in real-number arithmetic, `mod c` conventionally returns a value in `[0,c)`, so if `w_0(tau_l)` approaches a multiple of `c` from below, the literal `mod c` value approaches `c`, not `0` -- the intended meaning is convergence in `R/cZ`, not literal modular reduction | **confirmed, real, precision issue**: the underlying mathematical claim (continuity of `H` gives `H(w_0(tau_l)) -> H(0)`) is unaffected, since `H` is periodic and the true content is "the nearest multiple of c" | fixed: replaced with `dist(w_0(tau_l), c*Z) -> 0`, with one added sentence making explicit that the argument doesn't depend on the sign of the deviation from the nearest multiple |
| X5 (Opus finding F13, minor, real, and a re-opened prior "fixed" item) | A single en-dash used as appositive punctuation on p. 3 ("`W_3 phi = phi -- his invariant density`"), which momentarily misparses as a subtraction right after a chain of equalities. This exact issue was logged as fixed in this project's very first critique round (Round 1/2 era), but the dash was still present in the compiled PDF | **confirmed, real**: grepped the full source and found the `--` still there, contradicting the earlier "fixed" status | fixed properly this time: replaced with a comma; grepped again after the fix to confirm zero remaining punctuational dashes anywhere in the 18-page document (only legitimate name-compound and numeric-range dashes remain) |
| X6 (Opus finding F15, minor, real) | Section 2 calls `lambda*psi'(t)=3(psi(3t)-psi(3t-2))` "Berg and Kruppel's family of functional equations", but the display has the dilation hard-coded as 3, so it isn't a family (a family needs a free parameter) | **confirmed, real**: consistent with how the paper correctly uses a free `a` for the *truncated* equation two paragraphs later | fixed: generalized the display to `a(psi(at)-psi(at-2))` and reworded "family... member of" to "at dilation parameter a=3 and lambda=2/3, an instance of" |
| Opus finding F2 (MAJOR) + Codex finding 1 (MAJOR), both reviewers, again | Repository/certificate scope question: print full ball enclosures inline, archive with a DOI | not a new defect | no action beyond what was already done this session (Rule 8d): the four `Hhat(m)` enclosures were already added earlier this session per the researcher's explicit direction; the remaining DOI-archiving ask remains open by the researcher's own choice, not a fresh deferral |
| Opus finding F3 (MODERATE) + Codex finding 2 (MODERATE), convergent, restates settled ground | Both ask that Lemma 9's `0.114`/`0.0119`, Lemma 11's tail bound, Lemma 12's `Sigma` tail, and Theorem 13's `E(18)`/`E(19)` be shown as full derivations rather than "the first few terms"/"directly evaluating" | not a new defect | no action: this is the same repository/rigor-level scope question, already covered by Rule 12's division of labor; every one of these specific numbers was independently re-verified by both reviewers themselves this round (Opus explicitly lists all of them as checked and correct in its own report) |
| Opus finding F4 (minor, appendix request) | Restate Wirsching's (7.5), (7.12), (7.13) and the `A-tilde_delta` definition verbatim in an appendix, for a reader without [1] open | considered, not applied | not fixed: (7.5), (7.12), (7.13) are already displayed as formulas with equation numbers at their point of use (not relegated to an appendix); `A-tilde_delta`'s definition is already given in prose matching the primary source, independently verified against it in Round 14. An appendix duplicating material already present at point of use would be redundant, not more rigorous |
| Opus finding F9, F10, F11, F14 (minor/deferred) | `epsilon_1`'s definition carries an unnecessary supremum; four symbol collisions (`f`, `S`, `B`, `g`) apologized for elsewhere but not for these specific instances; the `T_4` underbrace sign convention in eq. (12) is visually ambiguous; two small citation-precision points about [2] | none confirmed as requiring a fix this round | not acted on: minor presentation points, logged here in case a future round converges on the same ones, consistent with this project's practice of prioritizing convergent/repeated findings |
| Codex finding 4 | The running header reads "2RENATO AUGUSTO TAVARES" with no space between page number and name | **checked directly**: rendered page 2 at 300dpi shows "2" and "RENATO AUGUSTO TAVARES" with clearly visible whitespace between them; this is a `pdftotext` extraction artifact (the page-number/header spacing collapses in text extraction the same way other whitespace-sensitive layout has in prior rounds), not a real typesetting defect | **FALSE POSITIVE**, no action; consistent with this project's practice of rendering to confirm before acting on any finding that could be an extraction artifact |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), 18 pages
(unchanged from the post-addendum count). All edited passages (the dash fix and "family" rewording
p.3, Theorem 2's statement p.2, the `mod c` fix and Theorem 1's rate fix p.16, the series reversion
p.15) visually spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: the most consequential finding (X1) was a genuine error introduced in
this project's own Round 14 fix, caught by a fresh Opus reviewer one round later -- the series
reversion's stated final rate was correct, but the one-line derivation offered for it was
insufficient by exactly one order in the asymptotic expansion, verified numerically against an
independent Newton's-method solve of the underlying equation before touching the text. A second
finding (X2) was reached independently by both reviewers from different angles. A third (X5)
exposed that an item this project logged as "fixed" in an early round had in fact not been fixed;
the dash was still in the source. One reviewer request (Codex's header-spacing complaint) was
checked and confirmed to be a text-extraction artifact, not a real defect. The repository/certificate
question was raised again but not re-litigated, since it was already substantively addressed earlier
in this same session per the researcher's direction.

## Round 16: fourteenth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 15 PDF. Opus verdict: **accept
after minor revision**, headlined "I found no mathematical error" after extensive independent
re-derivation (every printed constant reproduced, including two tight inequalities checked to
high precision; the two-route agreement on `H` to ~10^-35). Codex verdict: **major revision**,
again centered on the repository/certificate scope question (Rule 8d, no new action), plus one
genuinely new finding. Findings, each independently verified before acting:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Y1 (Codex finding #2, MODERATE, new, real) | Corollary 3 claims `e^H` agrees with Berg-Kruppel's infinite product "as proved in Remark 5 below by pure algebra", but Remark 5 only asserts the conclusion (`this is the same object as Q, L, and Delta recombine into`) without showing the term-by-term index correspondence between the two products and `e^L`, `e^{-Delta}` | **confirmed as a real exposition gap, and independently re-derived the missing algebra from scratch before writing anything**: with `s=e^w=a^t`, `a^{t-k}/b = 2s/3^{k+1}` (reindex `j:=k+1`) reproduces `K`'s defining series exactly as `e^{L(w)}`; `a^{t+l}/b = 2s*3^{l-1}` (reindex `k:=l-1`) reproduces `e^{-Delta(w)}` exactly via eq. (2); and `-Q(w) = c(t^2/2 - a*t)` with `e^c=a=3` reproduces the prefactor `a^{t^2/2-alpha*t}` exactly once `alpha=a`. All three match precisely -- the identity is correct, only the derivation was missing | fixed: added the three-part index-matching computation inline in Remark 5, in the paper's existing dense style |
| Y2 (Opus finding M2, minor, real) | Theorem 2's statement invoked "whose successive-period increment `w_0(tau+c)-w_0(tau)` tends to `c` (Lemma 16) even though `w_0(tau)` itself drifts away from `tau` without bound" as part of the mechanism, but the actual proof (checked directly) uses only that `w_0` is continuous, strictly increasing, and unbounded -- the increment-tends-to-`c` fact plays no role in this particular proof | **confirmed, real**: read Theorem 2's proof line by line; it never invokes the increment fact, only monotonicity+continuity+unboundedness | fixed: replaced the misattributed clause with what the proof actually uses ("whose phase modulo `c` sweeps every value infinitely often") |
| Y3 (Opus finding M3, minor, real) | Proposition 18's proof says "the first of the proposition's three claims", but the proposition's statement contains four assertions (`f(p)=Q(log p)`, the saddle location, the `P(tau)` formula, and the `Y-log Y=tau+r` reformulation), and the proof does establish the fourth one too | **confirmed, real**: counted the proposition's own statement, four distinct assertions, all proved | fixed: "three claims" -> "four claims" |
| Y4 (Opus finding M6, minor, real) | Section 2 asserts `phi` is `C^infty` with no proof anywhere in the paper and no downstream use; the property the paper actually proves and uses is continuity (Lemma 11) | **confirmed, real**: grepped the full document, `C^infty` appears exactly once, unused and unproved | fixed: removed the unproved `C^infty` claim, replaced with "continuous (by Lemma 11 below)", forward-referencing the lemma that actually proves it |
| Codex finding #4 / Opus finding M7 (both, convergent) | The claimed Berg-Kruppel `f''(p)` sign discrepancy (`+2beta` in their printed source vs. `-2beta` from direct differentiation) needs verification against the actual 1998 page; Opus explicitly said "I cannot check what Berg-Kruppel printed" | **verified fresh this round, going beyond what either reviewer could do**: rendered p.179 of `literature/papers/bergkruppel1998.pdf` (archived earlier this session) at 300dpi and read the display directly: "f(p) = alpha ln p - beta ln^2 p, f'(p) = (1/p)(alpha-2beta ln p), f''(p) = (1/p^2)(2beta ln p + 2beta - alpha)" -- confirms the paper's quotation character-for-character, and independently re-differentiated `f` by hand to confirm the paper's own computation (`2beta ln p - 2beta - alpha`) is correct, so the sign discrepancy is real | no text change needed: the citation was already accurate and precisely located (page, proposition, "the unnumbered display right after 'In view of'"); this closes the verification gap both reviewers flagged without altering the paper |
| Opus finding M1 (MAJOR) + Codex finding #1 (MAJOR), both reviewers, again | Repository/certificate scope question, again | not a new defect | no action (Rule 8d): already substantively addressed earlier this same session (the four `Hhat(m)` enclosures were added per the researcher's explicit direction); further action remains the researcher's choice |
| Codex finding #3, restates settled ground | Lemma 9/10/11/16's numerical constants asserted without displayed derivation | not a new defect | no action: same repository/rigor-level scope question, Rule 12 |
| Opus findings M4, M5 (minor/deferred) | (M4) eq. (5)'s tail-bound derivation cites Proposition 8's proof for a shared closed-form sum while Proposition 8 also cites eq. (5), reading like circularity though none exists; (M5) Lemma 11 states integrability for `N>=3` when `N>=2` would already suffice | neither confirmed as requiring a fix this round | not acted on: M4 is a presentational forward/backward-reference concern with no actual circularity (both derive from eq. (4) independently); M5 is a harmless over-conservative statement, logged in case a future round converges on either |

Paper recompiles clean (pdflatex, exit 0, zero warnings, zero overfull-hbox notices), 18 pages
(unchanged). All edited passages (Theorem 2's statement p.2, the `C^infty`/continuity fix p.3,
Remark 5's new algebra p.4, Proposition 18's "four claims" p.14) visually spot-checked via rendered
PNG: no truncation, no margin overflow.

**Net effect of this round**: both reviewers again reported no mathematical error in the paper's
core after extensive independent re-derivation -- a second consecutive round with that outcome, a
meaningful signal the loop is converging. The one new, genuine finding (Y1) was a real exposition
gap in a passage this project's own earlier rounds had accepted at face value; the missing algebra
was independently re-derived from scratch and confirmed correct before being written into the text.
A second genuine gap (Codex/Opus's shared concern about the unverifiable Berg-Kruppel citation) was
closed for good this round by rendering the actual 1998 source page directly, something no prior
round had the archived PDF to do. Three further minor real findings (Y2-Y4) were fixed.

## Round 17: fifteenth blind loop iteration (2026-08-06), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round 16 PDF. The Opus subagent
failed once mid-round on a monthly spend limit (an account-level constraint, not a loop decision);
relaunched successfully on the researcher's explicit direction to retry. Opus verdict: **accept
after minor revision**, again "no mathematical errors" after re-deriving everything and an
end-to-end Fourier-inversion test confirming Proposition 17's `O(1/tau)` and Proposition 18's
`O(tau^-1*log^2(tau))` rates numerically. Codex verdict: **reject**, again centered on the
repository/certificate scope question (Rule 8d, no new action), plus two genuinely new findings
this time, both independently verified before acting.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Z1 (Opus finding F3, MODERATE, new, real) | Proposition 8's proof (p.8) writes "the four-mode sum ... reproduces `H(0)-H(log(3/2)) = -0.0003771902809439858148...` directly", but this equality is false as stated: the printed 19+ digits belong to the *four-mode partial sum*, not to the true difference, which only agrees with the partial sum to about 19 significant digits before diverging (confirmed independently: true value via 200-mode sum is `...985834733...` vs. the printed `...985814833...`, differing at the 20th digit) | **confirmed, real, and independently re-verified with a fresh Arb computation at 300-bit precision** before touching the text (matches Opus's own independently-computed digits exactly) | fixed: reworded so the displayed equality is honestly between the four-mode sum and its own value (`the four-mode sum ... = -0.000377...8148...`), then derived the correct enclosure `H(0)-H(log(3/2)) in [-0.0003771902809439861948, -0.0003771902809439854348]` from the four-mode sum plus the already-stated tail bound, computed with Python's `Decimal` (not by hand, to avoid exactly the kind of digit-arithmetic slip this finding itself was about) and cross-checked to be correctly nested inside the paper's already-published outer interval before being written in |
| Z2 (Codex finding #5, moderate, new, real) | Section 2 (p.3) says Berg-Kruppel's comparison function "solves the truncated equation", implying an exact solution, while every other place in the paper (introduction p.1, Proposition 19's proof p.16) correctly calls it "the asymptotic solution" -- an internal inconsistency in how the paper describes the same object | **confirmed, real**: grepped all four occurrences of "asymptotic solution" vs. the one "solves"; three of four already use the careful phrasing, this was the outlier | fixed: "solves the truncated equation" -> "is the asymptotic solution of the truncated equation", matching the paper's own established (and correct) usage elsewhere |
| Z3 (Codex finding #4, moderate, new, real) | Remark 14 (now the E(N) remark, p.11-12) says checking `E(18)>=1` and `E(19)<1` "confirms N>=19 is where the bound first becomes non-vacuous" -- but two data points don't establish monotonicity for all `N<19`, so "first" is an overclaim from the stated justification alone | **confirmed as a real logical gap, though the underlying claim happens to be true**: independently computed `E(N)` for `N=3..25` from the paper's own formula (9) before touching the text, confirmed strictly decreasing throughout (so "first" is factually correct), but the paper's stated justification (checking only two points) doesn't establish this without an unstated monotonicity argument for `N<19` | fixed: softened to "the bound `E(N)<1` is non-vacuous at `N=19` (whether some smaller `N` also gives `E(N)<1` is immaterial to what follows and is not checked)", removing the overclaimed "first" without needing to prove monotonicity on `[3,19)` (which is unused anywhere in the paper) |
| Opus finding F1 (MAJOR) + Codex finding #? (restates settled ground, repository/certificate scope) | Same scope question as every recent round: print full ball enclosures inline / archive with DOI | not a new defect | no action beyond what was already done in Round 14 (Rule 8d) |
| Codex findings #1, #2, #3, #6 (restates settled ground) | Proposition 8 and eq. (5) "outsourced to unshown computation"; Lemma 11's tail bound "does not prove its headline bound"; general "numerical precision asserted without derivation" | not new defects | no action: same repository/rigor-level scope question, Rule 12; Codex's own suggested repair for Lemma 11 was read and is a reasonable elementary argument, but adding it is exactly the kind of inline-certification expansion this project's Rule 12 has repeatedly declined for this class of finding |

Paper recompiles clean (pdflatex, exit 0, zero warnings -- one benign underfull-vbox notice on p.13
from a shifted page break, visually confirmed harmless), 18 pages (unchanged). All edited passages
(Proposition 8's four-mode-sum wording p.8, `phi_0`'s "asymptotic solution" wording p.3, the `E(19)`
remark p.12) visually spot-checked via rendered PNG: no truncation, no margin overflow.

**Net effect of this round**: the most substantive finding (Z1) was a genuine mathematical
imprecision -- an equality sign asserting something false at the 20th decimal digit -- caught by a
fresh Opus reviewer and independently re-verified with a fresh high-precision computation before
any text was touched; correcting it required deriving a new enclosure interval, done with exact
decimal arithmetic rather than by hand specifically to avoid introducing a new digit-transcription
error while fixing an old one. Both of Codex's new findings (Z2, Z3) were real, if smaller: one
wording inconsistency and one overclaimed "first" that happened to be true but wasn't justified by
what the text actually checked. Per the researcher's explicit instruction, Round 18 is not launched
automatically; the loop pauses here pending authorization.

## Post-Round-17 addendum: front-matter formatting (researcher-directed, outside the critique loop)

Not a critique-loop finding; a formatting request from the researcher, who asked specifically for
the standard arXiv preprint front-matter order: title, author, institution/email/ORCID, abstract,
then body. Contact email changed from `dr.renatotavares@gmail.com` to `rat@discente.ufg.br` per the
researcher's explicit instruction (also updated in `CLAUDE.md`'s Section 1). Institution, email, and
ORCID (previously absent from the paper entirely) now appear on page 1, between the author name and
the abstract, rather than only at the very end of the document (`amsart`'s default placement for
`\address`/`\email`). Two dead ends along the way, recorded for future reference: (1) embedding line
breaks and formatting commands directly inside `\author{...}` caused a fatal `TeX capacity exceeded`
compile error, because `amsart` reuses `\author`'s content verbatim in the running head -- the
working fix was a separate `\begin{center}` block, using `\par` rather than `\\` for line breaks;
(2) placing that block right after `\maketitle` puts it after the abstract (since `amsart`'s
`\maketitle` bundles title+author+abstract as one atomic unit when the abstract environment
precedes it) -- the working fix was moving the `\begin{abstract}...\end{abstract}` environment to
*after* `\maketitle` instead, which `amsart` accepts with only a benign advisory warning ("Abstract
should precede \maketitle"), not an error, and renders identically. Recompiled clean, verified the
institution/email/ORCID block appears exactly once (page 1 only, no duplicate at the end) and in the
requested order, visually spot-checked via rendered PNG.

Same session, immediately after: the researcher noticed the keywords and MSC classification were
still rendering in `amsart`'s default location, a small-print footnote at the bottom of page 1, and
asked for the arXiv convention instead (both directly below the abstract, in the body text, not a
footnote). Removed the `\subjclass`/`\keywords` preamble macros (their footnote is generated
automatically by `amsart`'s `\maketitle`, with no supported option to relocate it) and replaced them
with two plain `\noindent\textbf{...}` lines placed right after `\end{abstract}`: "Keywords:" and
"2020 Mathematics Subject Classification:", each followed by the same content as before. Recompiled
clean (pdflatex, exit 0, one benign advisory only), confirmed via `pdftotext` that both lines now
appear exactly once, in normal body text directly under the abstract, with no leftover footnote
anywhere in the document, and visually spot-checked via rendered PNG.

Same session, immediately after: the researcher noticed a large vertical gap between the author
name and the institution/email/ORCID block on page 1. Cause: `amsart`'s `\maketitle` reserves
vertical space for a `\date` field (empty here, but the space is still inserted), stacked on top
of the manual `\begin{center}` block's own default top skip. Added `\vspace{-2.5em}` between
`\maketitle` and the `\begin{center}` block to remove the reserved gap. Recompiled clean, visually
confirmed the name, institution, email, and ORCID now sit close together with normal single-block
spacing.

Same session, immediately after: the researcher asked whether the keywords and MSC codes actually
match the paper's content. Checked the keywords by grepping each term against the body text (all
five are genuinely used, not decorative: "atomic function" against Rvachev's `h_3` at line 190,
"Mellin transform" against Section 6's residue-calculus derivation, etc.). Checked the four MSC
codes against the primary source (the official MSC2020 PDF, `msc2020.org/MSC_2020.pdf`, fetched and
`pdftotext`-extracted rather than trusted from memory, per Rule 11), not just the paper's own
citation: `11B83` "Special sequences and polynomials" (confirmed, by web search, as the conventional
code used across arXiv for Collatz/3x+1 papers despite the literal title not naming the problem),
`39B22` "Functional equations for real functions" (correct, matches `phi`'s and Berg-Kruppel's
real-valued functional equations), `11M06` "$\zeta(s)$ and $L(s,\chi)$" (correct, `zeta(1+z)` is
load-bearing in `H`'s closed-form Fourier coefficients) all checked out. `30D05` "Functional
equations in the complex plane, iteration and composition of analytic functions of one complex
variable" did not: this is a complex-dynamics code (Schroder/Bottcher-type iteration equations), and
grepping the paper for "iterat"/"composition of" found no such content anywhere. Replaced with two
codes that actually match the paper's two central analytic techniques: `44A15` (Mellin transform,
already one of the paper's own keywords, matching Section 6's meromorphic-continuation-and-residues
argument) and `41A60` (asymptotic approximations/steepest descent, matching Section 4's uniform
saddlepoint approximation, which explicitly bounds cumulant functions off the real axis via the
maximum-modulus principle). Recompiled clean, confirmed via `pdftotext` the five codes now print
correctly on page 1.

## Round 18: sixteenth blind loop iteration (2026-08-07), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the front-matter-corrected PDF. **Codex
verdict: major revision**, centered entirely on the same repository/certificate scope question
raised every round since Round 3 (Rule 8d, not reopened), plus a genuine, independently-verified
style catch. **Opus verdict: accept after minor revision** -- again "no mathematical error" after
recomputing essentially every printed constant (a full table of ~30 independent recomputations, all
matching), but the densest and most substantive prose/rigor-presentation review of the loop so far,
including two findings (M2 below) that required real mathematical work, not just wording, to close
honestly.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Own finding (not from either reviewer): overfull hbox with genuinely lost text, p.8 | Rendering every page myself to spot-check the round's other fixes, found `Overfull \hbox (99.8852pt too wide)` at the `H(0)-H(log(3/2))` interval display: `99.8852pt` past the normal margin puts the tail of the line (the closing `4348]` and the following `; this route alone certifies...`) past the physical page edge (468pt text block + 99.9pt = 567.9pt from the left margin, i.e. past the 612pt page width entirely), not just into the margin whitespace. Confirmed by cropping a 300dpi render of the exact region: the line visibly stops mid-number. Neither Codex nor Opus this round found any overfull line anywhere (both explicitly checked and reported none), so this is a real miss on both sides, most likely introduced by Round 17's own fix, which lengthened this exact interval | **confirmed, real, lost text on the printed page** | fixed: converted the inline interval statement to a displayed equation (`\[ H(0)-H(\log\frac32) \in [\ldots] ; \]`), matching the fix pattern used for Round 6's J2. Recompiled: zero `Overfull \hbox` warnings anywhere in the document (previously just this one), visually confirmed the full interval and following clause now render intact |
| Opus H3 (high) | Proposition 8's *stronger* oscillation bound (`D = 4.187449477152e-4`, the number Theorem 2's `1.0004188` actually depends on) states no ball radius, unlike the weaker bound four paragraphs earlier which explicitly gives `<1e-70` | **confirmed, real presentation gap**; independently recomputed `D` from scratch with a fresh Arb (`python-flint`) implementation of formula (7) at the paper's own stated precision (250-bit, `R=30`, `M=4`) before touching anything: got `D` matching the printed digits exactly, with ball radius `<10^{-70}$}`, i.e. the same order as the weaker bound | fixed: added `(ball radius $<10^{-70}$, same $250$-bit precision and $R=30$, $M=4$ truncation as above)` right after `D`'s value |
| Opus M2 (moderate, the most substantial finding this round) | Theorem 1's proof asserts `w_0(tau_l) = lc - log(lambda_l) + O(1/l)` "by Lemma 16's defining equation" -- but Lemma 16 only states `tau = Phi_0(w_0)` and `Phi_0' = 1-1/(c*B_sm)`, neither of which gives this asymptotic rate directly | **confirmed, real, and non-trivial to close correctly**: a naive one-term inversion of `Phi_0` gives only `O(log(tau)/tau)` error, one order too coarse for the claimed `O(1/l)`. Verified this by hand, found a sign error in my own first attempt (caught by re-deriving symbolically and cross-checking numerically), then delegated an independent re-derivation to a fresh Opus subagent per Rule 11b (a subtle multi-step asymptotic substitution, exactly the class of error this project's own `feedback_multiparameter_index_errors.md` warns about). The independent derivation confirmed: substituting `tau=tau_l` into Section 6's already-proven two-term reversion formula, `w_0(tau)=tau+log(tau/c)+(log(tau)+r)/tau+O(tau^-2*log^2(tau))`, the `O(log(l)/l)` pieces from the two terms cancel exactly, leaving the claimed `O(1/l)` (in fact `~-a/l` for a specific constant, sharper than what the paper asserts), confirmed both symbolically and by direct 50-80 digit numerical root-finding at `l` up to `10^12` | fixed: replaced the bare citation with a description of the actual cancellation mechanism (Section 6's reversion, noting explicitly that the naive one-term truncation is one order too coarse), without asserting the specific numeric coefficient (not needed for the paper's own qualitative `O(1/l)` claim, and the safest thing to commit to print given how easy this computation is to get a sign wrong on) |
| Opus M1 (moderate) | Theorem 13 states `N>=19` as a hypothesis; the remark immediately after says "nothing in the proof strictly requires it" and "neither this fact ... is used anywhere in this paper" -- a theorem carrying a hypothesis its own next sentence calls unnecessary | **confirmed, real internal tension** (the hypothesis itself is fine, it is only where the bound becomes informative; the phrasing overstated the tension) | fixed: reworded to state plainly that `N>=19` is the threshold where `E(N)<1` first holds, without the self-undermining "though nothing... requires it" hedge |
| Opus M5 (moderate) | The paper's own erratum against Berg-Kr\"uppel's p.179 formula for `f''(p)` (a `+2beta` vs `-2beta` sign) asserts "their Proposition 9.1 is unaffected... but the exact expression used here is not" without saying by how much, or why it is safe | **confirmed, real, fair completeness gap**; independently verified the claim by direct computation: the `+-2beta` discrepancy is exactly `2/c` (since `2*beta=1/c`), which shifts the `-1/2*log(2*pi*(B_0-1/c))` term in `P(tau)` by `O(1/B_0)`, vanishing as `B_0 -> infinity` | fixed: added the one-clause quantitative justification |
| Opus M6 (minor) | "matching the floating-point value above to 19 digits" is ambiguous: could mean 19 significant digits (wrong; the paper's own printed strings agree for exactly 16) or 19 decimal places (right) | **confirmed, real ambiguity**; independently re-checked digit by digit against both printed strings before fixing: agreement holds through the 19th digit after the decimal point, equivalently the leading 16 significant digits | fixed: "to 19 digits" -> "to 19 decimal places (16 significant digits)" |
| Opus H2 | The reproducibility repository organization name `faculdade` "looks like a placeholder" (a giveaway the URL was never replaced with a real one) | **checked and found false**: `curl` confirms the repository still returns HTTP 200; `faculdade` is this project's actual, deliberately-chosen public per-paper-repro-repo organization (see this project's own repo-visibility-policy memory), not a stub | no action, logged as a verified false positive (Rule 8c) |
| Opus M3, M4 and the floor-bracket/Remark-15 minors | Title "correction to..." reads as "amendment of" Berg-Kruppel's result, in tension with Corollary 3's attribution; the Introduction's account of what Berg-Kruppel left open reads slightly stronger than Corollary 3's own two-part accounting; `k_l` re-introduced as "a sequence of integers" when `\lfloor\cdot\rfloor` is automatically an integer; Remark 15's Edgeworth/Stirling-correction sentence stated as fact under a governing "suggests" | **checked, all four judged not to be real defects**: "correction" is standard terminology in exactly this literature (already cited via the de Bruijn-Mahler-Erdos-Richmond tradition in Remark 7), and Corollary 3 already disambiguates; the Introduction's "never evaluate it" refers to certifying non-constancy, not to the product's mere existence, consistent with Corollary 3; `k_l` is reused later (Theorem 1's proof, line ~1119) so naming it is not vacuous; Remark 15's disputed sentence is grammatically inside the "suggests" clause and the remark is already bookended by two explicit not-established disclaimers | not applied, reasoning logged here per Rule 8c |
| Codex's major/moderate findings (repo/certificate rigor, numerical inequalities without shown arithmetic) | Same repository-vs-inline scope question as every round since Round 3 | not new | no action, Rule 8d and Rule 12's already-settled division of labor |
| Codex's writing-tells section (independently corroborated by Opus's own, much larger, tells section) | Flagged "genuinely" (a Rule 5c banned word) and quoted "The load-bearing one is Conjecture 3" as a specific LLM tell -- both independently confirmed via grep and via Opus's own separate report, which flagged the exact same "load-bearing" sentence unprompted | **confirmed, real Rule 5c violations** | fixed: "genuinely" removed (line 156); "The load-bearing one is Conjecture 3" reworded to "The rest of the argument depends on Conjecture 3" |
| Own follow-up Rule 5c sweep, triggered by Opus's writing-tells section | Beyond the two items above: a banned-adverb "Precisely," transition; "runnable script" (corporate-register word Opus separately flagged); a third `not X, ...` antithesis construction over Rule 5c's budget of two; a mechanical section-by-section roadmap paragraph, redundant with the abstract/introduction already stating the same structure at the same granularity | all independently confirmed by direct grep against the current text before editing | fixed: "Precisely," deleted; "runnable" dropped; the weakest `not X` instance ("not by some correctable technical looseness") cut, leaving two; the roadmap paragraph compressed from six sentences (one per section) to one, pointing only to where `H`'s construction and the saddlepoint transfer live |
| Own check of Opus's `own`/`exactly`/`rather than` tallies and notation-collision-parenthetical complaint | Opus counted `own` 24x, `exactly` 31x, flagged several long notation-disambiguation parentheticals as a "models cannot cheaply rename, so they annotate instead" tell | counts independently reproduced (22 and 32 respectively, close enough); judged a full purge or a symbol-renaming pass to be disproportionate for an error-elimination round and to carry real risk of introducing a new error this late in a heavily-verified paper | not applied, logged here rather than silently dropped (Rule 8e) |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox` warnings anywhere in the document,
one pre-existing cosmetic `Underfull \vbox` badness notice), still 18 pages. All edited passages
(front matter roadmap p.2, Section 4 opening p.9, Prop 8's stronger bound p.8, the `N>=19` remark
p.9-10, the Berg-Kr\"uppel erratum p.15, the `w_0(tau_l)` derivation p.16) visually spot-checked via
rendered PNG, including a 300dpi crop of the newly-fixed overfull line specifically confirming no
text is lost.

**Net effect of this round**: zero new mathematical errors found by either reviewer for the third
round running (Round 16 was the first with this property); the loop's signal has now fully shifted
from correctness to presentation and prose, exactly the category-shift this project's own analysis
of the loop's convergence predicted several rounds ago. The one genuinely new mathematical
substance this round (M2's `w_0(tau_l)` asymptotic) turned out to be correct as stated in the paper,
but required real, careful, independently-verified work to confirm rather than just reword --
including catching and correcting a sign error in my own first attempt at the derivation before it
reached the paper, exactly the failure mode this project's own memory on multi-parameter asymptotic
substitutions warns about. The overfull-hbox lost-text catch was found by neither fresh reviewer,
only by directly rendering and visually re-checking every page myself; both reviewers' explicit
"checked, none found" claims on this exact failure mode were therefore wrong this round, a useful
data point on the limits of even careful automated bounding-box checks. Per the researcher's
standing instruction, Round 19 is not launched automatically; the loop pauses here pending
authorization.

## Round 19: seventeenth blind loop iteration (2026-08-07), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round-18 PDF; the reviewer prompt was
extended with an explicit instruction to check for lines running past the physical page edge, given
Round 18's own overfull-hbox miss. Opus's first attempt failed on the same monthly spend limit as
Round 17; relaunched with an identical prompt per that round's established recovery pattern, without
waiting for explicit re-authorization (a session-continuity judgment call, not a new standing
instruction). **Codex verdict: major revision**, mostly the same repository/certificate scope
question as every round since Round 3, plus one genuinely new finding that caught an error in this
project's own Round-18 fix. **Opus verdict: correct and complete proof, subject to five revision
items**, again zero mathematical errors after recomputing essentially every printed constant and
running, for the first time, an end-to-end numerical decomposition of the full proof chain
(Theorem 13 + Proposition 17 + Proposition 18's three error terms, tracked separately at six values
of tau) to confirm each behaves as claimed.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex #2 (major, catches this project's own Round-18 error) | Round 18 added "(ball radius $<10^{-70}$...)" to Proposition 8's stronger oscillation bound `D`, copying the weaker bound's radius without checking it applies. Codex correctly points out `<10^{-70}$}` can only be the Arb rounding radius of the truncated 35-term expression, not a valid enclosure of the true `D`: the `R=30` truncation's own analytic tail is far larger (`4.43e-30`, established two paragraphs earlier for the same `s<=3` range) | **confirmed, real; my own Round-18 addition was wrong** | fixed: independently recomputed the properly widened enclosure two ways -- (a) via the direct formula-(7) route, widening each `H` evaluation by the stated `R=30` tail bound (`4.43e-30`), giving a combined radius `~8.86e-30`; (b) via the Fourier route already used in the same sentence, truncated at `\|m\|<=10` with its own stated majorant tail (`5.60e-43` per point), giving a much tighter combined radius `~1.12e-42`. Used the tighter, already-justified Fourier bound: `D`'s radius is now stated as `<1.2e-42`, with the Arb rounding correctly identified as the smaller, non-dominant contribution |
| Codex #5 (minor) | Remark 5's inline derivation is split by a page break directly after an `=` sign (page 4 to page 5); no math lost, but an awkward break | **confirmed, real, cosmetic** | fixed: converted the tail of the inline chain to a short displayed equation, which now sits entirely on page 5 |
| Codex writing-tells: "unmotivated hyper-specificity ... verified independently by direct numerical solution ... at l up to 10^12 ... reads as confidence-signalling" | Flags a parenthetical this project's own Round-18 M2 fix added | **confirmed, real Rule 5c violation** (the "meta-honesty" family this project's own protocol bans) | fixed: removed the parenthetical; the mathematical claim stands on the algebra already shown, without a self-referential verification note |
| Opus R2 (moderate) | Theorem 1's proof only ever uses `lambda_l -> 1`, i.e. `\|l-k_l\|=o(l)`; Wirsching's specific `O(sqrt l)` bound in the comparison class is never used at that strength | **confirmed, real, cheap strengthening**; independently re-checked against the proof's actual logic (every step from `lambda_l->1` onward only needs `-log(lambda_l)->0`) before writing anything | fixed: added a remark immediately after Theorem 1's proof stating the weaker sufficient condition explicitly, without altering the theorem statement itself (which stays literally Wirsching's own class, for fidelity to Conjecture 3 as stated) |
| Opus R3 (major, partial) | Suggests labeling Theorem 2 explicitly as computer-assisted at its statement, since its positive-amplitude conclusion rests on Proposition 8's numerical certificate | **agreed, matches this project's own Rule 10b** (label every result by what it actually is) | fixed: added one sentence to Theorem 2's statement identifying the amplitude's positivity as a computer-assisted, interval-arithmetic result, not a hand proof. The rest of R3 (archive the repo with a DOI, state exact Arb/dependency versions inline) restates the repository-vs-inline scope question settled since Round 3; not reopened (Rule 8d) |
| Opus R7 (minor, real) | "dominated ... by a geometric series in `3^{-k}` inside the exponent" is confusingly worded; the exponent's growth is `3^{+k}`, not `3^{-k}` | **confirmed ambiguous, real wording issue** (the underlying math was always correct; only the English description was unclear about which series was being compared to which) | fixed: reworded to state the actual mechanism directly (terms decay doubly exponentially in `k`, faster than any fixed geometric rate), without the ambiguous "geometric series in `3^{-k}`" phrase |
| Opus R7 (minor) | `z_l` (Conjecture 3's own variable) and `x_l` (the class definition's variable) are used side by side without ever stating they're the same object | **confirmed, real, cheap clarity fix** (verified algebraically: `z_l := lambda_l*l*3^{-l} = (3^l*x_l/l)*l*3^{-l} = x_l` exactly) | fixed: added "$= x_l$" at the point `z_l` is first introduced in Theorem 1's proof, with a one-clause note that this bridges Wirsching's own two notations rather than introducing a new one |
| Opus R7 (checked, FALSE POSITIVE) | "The two `1/z` terms cancel against each other and [gives] `Gamma(z)zeta(1+z) = 1/z^2+A+O(z)`" is wrong, they claim: the `1/z` terms don't cancel, they produce the `z^{-2}` term | **checked and found FALSE** (Rule 8c): hand-expanded `Gamma(z)zeta(1+z)` from the stated Laurent series of each factor. The `z^{-2}` term comes from multiplying the two **leading** `1/z` coefficients (`1/z * 1/z`); "the two `1/z` terms" the paper's sentence refers to are the two **cross** terms (`gamma_E/z` from one factor times the other's constant term, and vice versa), which do cancel exactly, leaving no `z^{-1}` term in the product, exactly as needed. Verified the final constant `A = pi^2/12 - gamma_E^2/2 - gamma_1` term by term by hand before concluding the paper was right and the reviewer had conflated two different pairs of terms | not applied; recorded here per Rule 8c so a "wrong critique, verified wrong" outcome isn't silently discarded |
| Opus R4 (moderate) | Section 8 should name Proposition 18 (not Theorem 13) as the actual bottleneck on the overall convergence rate, and should say explicitly that Theorem 2's oscillation is far too slow to observe at any computationally reachable `t`, backed by Opus's own six-point numerical decomposition (residual still `~0.05` at `tau=195`, `120x` the certified amplitude) | **plausible, not independently verified this round** | not applied: a good, specific suggestion, but confirming Opus's own quantitative claim would need reproducing its full three-stage numerical decomposition, more verification work than this round's remaining scope; logged here rather than acted on without checking (Rule 8c) or silently dropped (Rule 8e) |
| Opus R1 (major) | Reproduce Wirsching's and Berg-Kruppel's imported equations as verbatim displayed quotations with page numbers, matching how the Conjecture-3 quotation on p.1 is already handled; separately, add the paper's own numerical reproduction of Wirsching's (7.12)/(7.13) limits (already spot-checked by Opus, `4.5->4.5`, `0.637->0.667`-ish trending to `2/3`) as corroborating evidence the imported normalization is faithful | **good suggestions, not applied this round**: a substantive literature/exposition addition (multiple verbatim quotations, primary-source re-verification per Rule 11) beyond what a single round can responsibly complete | logged for a future round, not silently dropped |
| Opus R6 (moderate) | Bibliography is pre-2003 only; suggests adding Flajolet-Gourdon-Dumas 1995 ("Mellin transforms and asymptotics: harmonic sums") as the standard reference for Proposition 6's exact technique, plus post-2003 Collatz-predecessor-density literature | **plausible, not verified this round** (Rule 11 requires reading the actual source before citing it; not done this round) | not applied, logged for a future literature-search pass |
| Opus R5 (moderate) | Detailed notation-collision table: `S`, `g`, `f`, `e`, `B`, `h`, `theta` each carry 2-4 distinct meanings across different sections, most entirely unflagged (unlike the handful the paper already disambiguates) | **accurate as a catalogue**; Opus's own recommended fix is renaming, not more annotation | not applied: a symbol-renaming pass across an 18-page, heavily-verified paper carries real risk of introducing a new error this late in the loop, for a readability gain rather than a correctness one; same judgment as Round 18's parallel notation-collision finding |
| Codex #1, #3, #4 / Opus R3's DOI-archiving part (restates settled ground) | Repository/certificate rigor, deferred numerical assertions, external-attribution documentation | same scope question as every round since Round 3 | not reopened, Rule 8d and Rule 12's already-settled division of labor |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox` warnings, one pre-existing cosmetic
`Underfull \vbox` notice), still 18 pages. All edited passages (Theorem 4's proof p.4, Remark 5's
displayed identity p.4-5, Theorem 2's statement p.2, Proposition 8's `D` radius p.8, Theorem 1's
proof and new remark p.16) visually spot-checked via rendered PNG.

**Net effect of this round**: zero new mathematical errors found by either reviewer for the fourth
round running, and for the first time a fresh reviewer's own verdict text states plainly "this is a
correct and complete proof" (Opus), subject only to presentation items. The most consequential
finding was Codex catching a real mistake in this project's own previous round's fix (the `D` radius
claim), a direct, useful instance of the loop verifying not just the paper but its own prior
corrections. One Opus finding (the `1/z` terms claim) was independently checked and found wrong,
recorded rather than discarded per Rule 8c. Two independent reviewers across Rounds 18-19 have now
separately flagged the reproducibility repository's organization name (`faculdade`) as reading like
a placeholder; it is not (verified live, matches this project's deliberate repo-naming policy), but
raising it with the researcher directly (outside this critique loop) seems worthwhile given it has
now come up twice from fresh eyes. Per the researcher's standing instruction, the next round is not
launched automatically; the loop pauses here pending authorization. A Round 20 wakeup was already
scheduled by the researcher for later today.

## Round 20: eighteenth blind loop iteration (2026-08-07), Opus and Codex both complete

Both launched in parallel, PDF-only, max effort, against the Round-19 PDF. Opus's first attempt
failed again on the monthly spend limit; relaunched immediately per the now-established recovery
pattern. Notably, Opus's relaunched pass detected that the PDF on disk changed mid-review (this
project edited the file live while Opus was reading it), re-checked its findings against the
updated version, and correctly attributed one finding (M2 below) to that edit specifically rather
than to the original submission. **Codex verdict: do not accept yet**, same repository/certificate
scope question as every round plus two genuinely new findings. **Opus verdict: correct proof
modulo six external claims**, the strongest and most detailed report of the loop so far (70 tool
calls, an hour and a half), including one real regression this project introduced in Round 20's own
earlier edits (M2), one real methodological improvement to Proposition 8 (m5), and dense,
substantive style feedback.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex #2 (moderate) | Round 18's M1 fix ("becomes informative, `E(N)<1`, exactly at `N=19`") reintroduced the exact overclaim Round 17 had already fixed away from ("exactly"/"first" is not established by checking only two adjacent points) | **confirmed, real regression**: my own Round-18 edit undid Round 17's Z3 fix without noticing, exactly the failure mode Rule 8b exists to catch | fixed: restored the "(whether some smaller `N` also gives `E(N)<1` is immaterial to what follows and is not checked)" disclaimer Round 17 had established, while keeping Round 18's separate, legitimate concern (removing the self-undermining "though nothing in the proof strictly requires it" hedge) |
| Codex #2 (moderate) | `e^{H(0)}=0.534122...` in Theorem 1's statement should be labelled numerical unless certified | **fair**; checked whether Proposition 8 certifies `H(0)` alone (it does not -- only the difference `H(0)-H(log(3/2))` is certified in ball arithmetic) | fixed: Theorem 1 now states `e^{H(0)}` is a well-defined real number regardless of its decimal expansion, with the printed digits explicitly labelled a floating-point evaluation, distinct from the nearby certified difference |
| Codex writing-tells: "not a hand proof" flagged as a pre-emptive negation | Restates Round 19's own M2 finding almost verbatim, about text this project added in Round 19 | **confirmed, real** | fixed: reworded Theorem 2's computer-assisted label to drop the trailing "not a hand proof" clause |
| Opus M2 (major, catches this project's own Round-20 error) | Round 20's own edit to Theorem 1 (adding the "not `H(0)` itself in isolation" hedge) was not propagated to Section 8's discussion, which still called `H(0)-H(w_{1011118})` one of "the two values of `H` certified in Proposition 8" -- a claim Proposition 8 never makes (it certifies two *different* combinations), now directly contradicting Theorem 1's own new hedge | **confirmed, real; caught by Opus noticing the file changed mid-review and re-checking against the new version** -- exactly the Rule 8b failure mode (a correction landing in one place, a stale claim surviving elsewhere), this time inside a single round rather than across rounds | fixed: reworded Section 8 to say this difference is *computed from* Proposition 8's printed values (a floating-point combination), not itself a certified enclosure; independently verified the value ($5.25\times10^{-6}$) is still numerically correct |
| Opus M3 (major) | Proposition 8's stronger-bound paragraph has an internally incoherent error budget: "40 digits" (`~1e-40` radius) stated alongside a `<1e-70` per-evaluation radius claim, and a radius attributed only to the Fourier route while the text says the value came "from (7) and from the Fourier series alike" | **confirmed, real inconsistency**, partly predating this round, partly introduced by Round 19's own radius fix | fixed: precision restated as "250-bit" (consistent with the `<1e-70` claim); reworded to state plainly that the certified enclosure uses only the Fourier route, with the formula-(7) route serving as an independent cross-check, not a source of the stated radius |
| (surfaced while fixing M3, not from either reviewer) | The rewritten M3 passage claimed the two computation routes "agree to over 70 digits" | **checked and found wrong before it reached the paper**: independently recomputed `H` at both grid points via both routes (Arb ball arithmetic for formula (7), `mpmath` for the Fourier series) and found they agree to only about 30 digits, limited by formula (7)'s own already-established `R=30` truncation tail (`4.43e-30`), not by anything wrong with either route | fixed before committing: reworded to "about 30 digits, consistent with (7)'s own `R=30` truncation tail bound above" |
| Opus m5 (moderate, the most substantial finding this round) | Proposition 8's upper bound on `osc(H)` currently rests on an uncertified Lipschitz argument, explicitly caveated as depending on the heuristic grid search not having missed the true extrema anywhere among `2^20` points. Opus proposes a two-line replacement: decompose `H` into its leading Fourier mode plus a remainder bounded by the already-established majorant, giving a fully rigorous, unconditional two-sided enclosure with no search needed | **confirmed correct and independently reproduced**: recomputed `4\|Ĥ(1)\|` and `Σ_{m≥2}\|Ĥ(m)\|` from scratch (reusing only already-certified quantities already printed earlier in the same proof: `Ĥ(1)` through `Ĥ(4)` in ball arithmetic, and the `m>4` majorant tail bound), getting `osc(H) <= 4.187981e-4`, matching Opus's numbers to the digits given | fixed: replaced the uncertified Lipschitz argument with this rigorous upper bound, keeping the existing grid-search-located points for the (excellent, already-certified) lower bound. Proposition 8 now states a genuine two-sided interval, `4.1874494771e-4 <= osc(H) <= 4.187981e-4`, with no uncertified step anywhere in its proof |
| Opus m6 (minor) | The parenthetical "(whether some smaller `N` also gives `E(N)<1` is immaterial...)" appeared twice verbatim, in the Remark after Theorem 13 and again inside the proof | **confirmed, real duplication**, introduced by this project's own Round-18/20 edits to the same passage | fixed: trimmed the in-proof repetition, pointing back to the Remark instead |
| Opus m8 (minor) | "The rest of the argument depends on Conjecture 3" (this project's own Round-18 rewording, replacing "The load-bearing one is...") reads as claiming Wirsching's *entire remaining* argument depends only on Conjecture 3, contradicting the immediately preceding sentence, which says positive predecessor density needs all three conjectures | **confirmed, real regression from Round 18's own style fix**: fixing one problem (informal register) introduced a different, factually imprecise claim | fixed: reworded to "Of these three, this paper settles Conjecture 3," accurate and no longer overclaiming |
| Opus m11 (minor) | Suggests stating the oscillation's relative size (`~0.042%`), since a reader could otherwise picture a visible effect and be confused why no numerical experiment on `phi` would ever show it | **good, cheap, low-risk addition** | fixed: added one clause to Theorem 2's proof stating the relative size and why no direct numerical check could find it |
| Opus M1 (major) | Six specific external claims (Wirsching's (1.5),(3.2),(7.5),(7.11),(7.13),(7.14); Berg-Kruppel's Prop. 9.1/9.3 and the p.179 sign) are load-bearing and unverifiable from the PDF alone; recommends re-verifying each symbol-by-symbol against the primary sources before submission | **not independently re-verified this round**: this project's own working notes record these as already checked against primary sources earlier in the project, but a fresh, focused re-verification pass was judged too large for this round | logged for a dedicated future pass, not silently dropped (Rule 8e) |
| Opus M4 (moderate) | Proposition 18's statement should carry the `+/-2*beta` Berg-Kruppel sign-discrepancy caveat directly, not bury it in the proof; and the proof's own sentence structure ("the exact expression used here is not [unaffected]... which vanishes as `B_0->infinity`") reads self-contradictory | **fair, not applied this round**: moving content from a proof into a proposition statement is a real structural change or the paper's existing convention (already used for other subtle points), weighed against this round's remaining scope | logged for a future round |
| Opus m7 (moderate) | Missing citation: Flajolet-Gourdon-Dumas 1995 ("Mellin transforms and asymptotics: harmonic sums") as the standard reference for Proposition 6's technique; "the de Bruijn-Mahler phenomenon" may not be a standard name | **plausible, not verified this round** (Rule 11 requires reading the actual source before citing it) | not applied, logged for a future literature pass |
| Opus m9 (moderate), m10 (moderate), n12-n17 (minor) | Notation-collision table (`a`, `c` collisions patched with disclaimers); promote the paper's real central lemma `(star)` to a numbered, once-proved proposition instead of re-deriving it four times; several small wording/precision notes | **same judgment as Rounds 18-19's parallel findings**: renaming and restructuring carry real risk this late in the loop for a readability gain, not a correctness one | not applied, logged |
| Codex #1 / Opus M1's DOI-archiving parts (restates settled ground) | Repository/certificate rigor | same scope question as every round since Round 3 | not reopened, Rule 8d and Rule 12's already-settled division of labor |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox` warnings), now 19 pages (up from 18,
reflecting Proposition 8's new rigorous upper-bound argument). All edited passages (Theorem 1 and 2
p.1-2, Proposition 8's full stronger-bound paragraph p.8-9, the `N>=19` remark, Section 8's `H`
value p.17-18) visually spot-checked via rendered PNG and `pdftotext`.

**Net effect of this round**: zero new errors in the paper's actual mathematics (Opus: "I found no
mathematical error in any proof... I tried hard"), but the densest and most consequential
presentation-and-rigor round yet: one real regression this project introduced in an earlier round
(Codex's N=19 catch), one real regression this project introduced *within this same round* (Opus's
M2, caught only because Opus noticed the file changed mid-review and re-checked), one incoherent
error-budget statement partly of this project's own making (M3), and one genuine strengthening of
the paper's own mathematics (m5: Proposition 8 no longer has an uncertified step anywhere). Three
of these four are self-inflicted, all introduced while fixing something else -- a concrete
demonstration of why Rule 8b's re-check discipline matters even within, not just across, rounds. Per
the researcher's standing instruction, the next round is not launched automatically; the loop pauses
here pending authorization.

## Round 21: nineteenth blind loop iteration (2026-08-07), Codex only, researcher's explicit request

The researcher asked for a Codex-only round this time (same protocol, max effort), to see what a
single reviewer alone still finds, before deciding whether to continue with both models. Verdict:
major revision, not acceptance. No new mathematical error found ("I do not find an outright
algebraic disproof... I recomputed the main recurrence, Mellin transform, residue calculation,
saddle equations, series reversion, phase-locking argument, and the transfer to phi/phi_0"), for the
fifth round running (Round 17 onward). Findings:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex writing-tells | Flags this project's own Round-20 addition to Theorem 2's proof ("small enough that no direct numerical evaluation of phi at any computationally reachable t could have found it") as "an unproved, theatrical computational claim" | **confirmed, real**: the paper never actually establishes how large `tau` needs to be for the effect to become numerically visible, or that this pushes `t` below any standard floating-point range; the clause asserted a plausible-sounding but unproven claim | fixed: deleted the clause, kept the verified relative-size fact (`0.042%`) that motivated adding it |
| Major (restates settled ground) | Repository/certificate not self-contained, same as every round since Round 3 | not new | not reopened, Rule 8d |
| Medium (restates settled ground) | Several constants (Lemma 9's `0.114`/`0.0119`, Lemma 11's `3e^{-b_0}`, Lemma 12's numeric tail, Remark 14's `E(18)`/`E(19)`) "announced, not derived" | same repository-vs-inline scope question raised in nearly every round since Round 3-5 | not reopened, Rule 8d |
| Minor | Novelty/priority claims ("neither statement had been settled before", "Fourier series is new") need a literature argument, not just assertion | same category as Round 20's Opus M1/m7 | not applied this round, same reasoning already logged |
| **Recurring across three separate rounds now (5-6, and again this round): analytic, non-numerical proof of `H`'s non-constancy** | `Hhat(1) = -(2^{i*omega_1}/c) * Gamma(-i*omega_1) * zeta(1-i*omega_1)`; `Gamma` has no zeros, and by the classical zero-free theorem for `zeta` on `Re(s)=1`, `zeta(1-i*omega_1) != 0`, so `Hhat(1) != 0` unconditionally, no computation needed, which alone proves `H` non-constant (only the *quantitative* oscillation bound would still need Proposition 8's numerics) | plausible and mathematically clean, but not implemented or independently verified this round | **flagged directly to the researcher this round** rather than silently deferred again, since three independent fresh reviewers proposing the same strengthening is a stronger signal than Rule 8e's usual bar for a first look |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox` warnings), still 19 pages.

**Net effect of this round**: consistent with the pattern since Round 16, a single reviewer alone
still returns zero new mathematical errors, still returns the same recurring repository/certificate
scope complaint, and this time also caught a real problem in this project's own immediately
preceding edit (an unproven "theatrical" claim added in Round 20, now removed). Per the researcher's
explicit instruction, Opus was not run this round; the loop pauses here, and the researcher will say
when to resume with both reviewers.

## Post-Round-21 addendum: analytic (non-numerical) proof of H's non-constancy

Researcher-directed implementation, not a critique-loop finding on its own: the researcher asked to
implement the recurring suggestion flagged at the end of Round 21 (also raised independently in
Rounds 5 and 6), that `H`'s non-constancy follows unconditionally from the classical zero-free
theorem for `zeta` on `Re(s)=1`, with no computer-assisted computation needed at all for the
qualitative claim.

Verified before writing anything into the paper: `Hhat(1) = -(2^{i*omega_1}/c) * Gamma(-i*omega_1)
* zeta(1-i*omega_1)` is a product of three factors, each individually nonzero (`2^{i*omega_1}` on
the unit circle; `Gamma` has no zeros anywhere and `-i*omega_1` is not one of its poles since
`omega_1 != 0` is real; `1-i*omega_1` lies on `Re(s)=1` with `omega_1 != 0`, where the classical
Hadamard-de la Vallee Poussin zero-free theorem gives `zeta(1-i*omega_1) != 0`), so `Hhat(1) != 0`
unconditionally, and a periodic function with one nonzero Fourier coefficient at `m != 0` cannot be
constant. The primary-source citation was verified before use, per Rule 11 (not taken from memory):
fetched Titchmarsh's *The Theory of the Riemann Zeta-Function* (2nd ed., revised D. R. Heath-Brown,
Oxford University Press, 1986) directly and located the exact statement as Theorem 3.8 ("There is a
constant `A` such that `zeta(s)` is not zero for `sigma >= 1 - A/log(t)`, `t > t_0`"), the classical
zero-free region whose boundary case `sigma=1` is exactly the fact needed.

Added as a new opening paragraph of Proposition 8's proof ("Non-constancy first, unconditionally"),
before the existing numerical certificate, which now serves only to establish `H`'s *quantitative*
oscillation size (still genuinely computer-assisted, unaffected). Updated, per Rule 8b's discipline
applied proactively this time rather than after a later round catches it: the abstract (now states
non-constancy follows from the zero-free theorem directly, with only the exact oscillation size
certified), Proposition 8's own statement (states the two claims, analytic and computational,
separately), and Theorem 2's closing sentence (the amplitude's *positivity* is now attributed to the
classical theorem; only its *explicit numeric size* remains labeled computer-assisted). Added
Titchmarsh 1986 as a new bibliography entry, `[9]`.

Recompiled clean (pdflatex, exit 0, zero `Overfull \hbox`, no undefined-citation warning), 19 pages
(unchanged from Round 20). Visually spot-checked the new proof paragraph, the updated abstract, and
the updated Theorem 2 statement via rendered PNG.

## Round 22: twentieth blind loop iteration (2026-08-08), Opus and Codex both complete

Researcher's instruction this round: loop continuously until convergence, no more per-round pauses.

The researcher explicitly switched the loop from per-round authorization to continuous: run Codex
and Opus (max effort, same protocol) repeatedly, without pausing for a go-ahead each time, until the
review converges. This round's prompt also added an explicit item 8 asking both reviewers to check
the new zero-free-theorem argument from the post-Round-21 addendum. Both verdicts moved further
toward acceptance: **Codex: not yet acceptable, but "the mathematical core... deserving serious
consideration"** (verdict unchanged in substance from prior rounds, still centered on the
repository/certificate question); **Opus: accept after minor revision**, explicitly confirming the
zero-free-theorem argument is correct, and for the first time finding and fixing two genuinely new,
independently-verified errors (not just presentation gaps) in addition to a substantial style pass.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex (moderate, new) | Abstract's "we certify its exact oscillation rigorously" overclaims: Proposition 8 gives a two-sided *enclosure*, not the exact value, and the paper's own grid search only finds candidate extrema | **confirmed, real overclaim**; this was the researcher-directed Post-Round-21 addendum's own new wording, not older text | fixed: "certify its exact oscillation rigorously" -> "rigorously enclose its oscillation" |
| Opus F1 (must-fix, real numerical error) | "the ratio swings by at least 0.042%" (Round 20's own addition) is false: `e^{osc(H)}-1 >= e^{4.1874494771e-4}-1 = 0.0418833...%`, which is **less than** 0.042%, not at least it -- a lower bound rounded the wrong way | **confirmed, real; independently recomputed before fixing** (`math.exp(4.1874494771e-4)-1 = 0.00041883...`, confirming `0.042%` is not implied) | fixed: `0.042%` -> `0.0418%`, safely below the true value |
| Opus F2 (must-fix, real notational contradiction) | Section 2 promises "the two [meanings of] `a` never appear in the same formula except in Section 6" -- but Remark 5 (Section 3) prints `-Q(w) = w^2/(2c) - aw = c(t^2/2-at)` (this paper's own `a`) directly alongside `a^{t^2/2-alpha*t}` (Berg-Kruppel's `a=3`) in the same display, breaking the promise inside the one section it's supposed to hold | **confirmed, real**: independently re-derived both expansions by hand before touching anything; the equation is mathematically correct once the two `a`'s are correctly disambiguated, but the notation genuinely violates the paper's own stated convention, exactly where a careless reader would get confused | fixed: replaced Berg-Kruppel's dilation-parameter symbol with the literal number `3` throughout Remark 5 (it was already specialized to that value in this exact remark), eliminating the collision entirely rather than adding a fourth disclaimer; Section 2's original promise is now literally true again, no longer needing its own edit |
| Opus F3 (moderate) | Same "exact oscillation" overclaim, independently found; also flags Proposition 8's title "Certified non-constancy" as stale now that non-constancy is proved analytically, not certified | same as Codex's finding above (already fixed) for the first half | fixed: retitled the proposition "Non-constancy and certified oscillation"; also updated a forward-reference in the front-matter roadmap that used the same stale phrasing |
| Opus F4 (real exposition gap) | Theorem 13's parameter `N` and Sections 5-6's parameter `tau` are combined into one `o(1)` in every downstream proof without ever stating that `N -> infinity` exactly when `tau -> infinity` (in fact `N ~ tau/c`), or that `tau_l -> infinity` uniformly on the comparison class | **confirmed, real, correct once verified**: derived `N ~ w*/c ~ tau/c` from already-established facts (`s=e^{w*}`, Lemma 16's `w*=w_0+O(1/B_0)`, `w_0=c(B_0+a)`) before writing anything | fixed: added one linking paragraph at the start of Section 7, stated once rather than repeated in each of the four proofs that need it |
| Opus F6 (checked, no change needed) | Questions whether the zero-free-theorem citation should be Titchmarsh's Theorem 3.1 rather than 3.8 | **re-verified against the primary source (re-fetched, since the earlier local copy was gone) and found the original citation correct**: paragraph 3.1 is unnumbered historical prose introducing the 1896 Hadamard-de la Vallee Poussin result; the first formally numbered theorem in the chapter is 3.5, and Theorem 3.8 is the actual quantitative zero-free region theorem that implies the fact used. Theorem 3.8 is the more precise, appropriate citation | not changed; Opus's doubt was a plausible but, on inspection, mistaken recollection -- recorded per Rule 8c |
| Opus F8 (five minor items, all confirmed real) | (a) "independently from (7) and from the Fourier series" parses as independent of both, contradicting the next clause; (b) `4\|Hhat(1)\| = 4.187449303e-4` is a truncation of the true value (`4.1874493033e-4`), not a valid upper bound, though the final rounding absorbs the gap; (c) `gamma, delta_BK, epsilon` attributed to "their Proposition 9.1" in Section 2 but to "equations following (9.6)" in Section 6; (d) Section 8 says "the two values of H" where Proposition 8's proof prints four | all independently checked before fixing (the truncation direction for (b) confirmed via `Decimal` arithmetic) | fixed: (a) added a comma; (b) rounded up to `4.187449304e-4`, a verified safe upper bound; (c) Section 2 no longer names a specific proposition number it can't independently confirm matches; (d) reworded to name the specific point (`w_1011118`) as one of four |
| Codex, Opus (restates settled ground) | Repository/certificate not self-contained, load-bearing external quotations from [1]/[2] need verbatim reproduction, org name `faculdade` still reads as a placeholder | same as every round since Round 3 | not reopened, Rule 8d; the verbatim-quotation appendix (Opus F5) remains logged from Round 20/21 as a good, not-yet-actioned suggestion |
| Opus's item 8 check (researcher-requested) | Verify the new zero-free-theorem non-constancy argument | **explicitly confirmed correct**: "The move to an analytic proof of `Hhat(1)!=0` was the right one... the argument (three factors, each nonzero, the third by Hadamard-de la Vallee Poussin...) is correct" | no action needed, independent confirmation recorded |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox`), still 19 pages. All edited passages
(Remark 5 p.5, Section 7's opening p.16-17, Theorem 2's proof p.17, Section 8 p.18) visually
spot-checked via rendered PNG.

**Net effect of this round**: the first round where a reviewer's overall verdict reached "accept
after minor revision" without conditioning it on unimplemented items (Opus), and the first round to
independently confirm the previous round's own new mathematical content (the zero-free-theorem
argument) rather than just not objecting to it. Two real, if narrow, errors were caught and fixed
(F1's rounding direction, F2's notational contradiction), both introduced in this project's own
recent rounds while fixing something else, continuing the pattern flagged in Round 20. Per the
researcher's new standing instruction, the loop continues automatically to the next round rather
than pausing for authorization; starting next round, the second reviewer slot switches from Opus to
Fable per the researcher's explicit instruction.

## Round 23: twenty-first blind loop iteration (2026-08-08), Codex and Fable both complete -- the
## loop's convergence signal

First round with Fable (Claude Fable 5) as the second reviewer, replacing Opus per the researcher's
instruction. **Both reviewers found zero new mathematical errors and reached essentially
acceptance-level verdicts.** Codex: "I do not recommend rejection on mathematical grounds: I found
no fatal proof error... I would recommend acceptance after [the] reproducibility repair." Fable,
independently: "As submitted, this is a rigorous proof of what it claims... Nothing else. I found no
mathematical error to fix."

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex #1, #2 (restates settled ground) | Repository/certificate not self-contained; several constants (Lemma 9, Lemma 11, Remark 14) "announced, not shown" | same scope question as every round since Round 3 | not reopened, Rule 8d |
| Fable #1 (restates settled ground) | Load-bearing external quotations from [1]/[2] need independent verification against the physical sources, particularly the self-flagged Berg-Kruppel sign discrepancy | same as Round 20/21/22's Opus F5, F1 | not reopened this round; still logged as a genuine future task, not dropped |
| Fable #2 (cosmetic, considered) | `e^{H(0)}=0.534122...` embedded directly in Theorem 1's statement; suggests moving the numeral to a remark, keeping the theorem's boxed text free of any uncertified decimal | fair stylistic preference, not an error (Fable's own words: "the caveat is honest and correctly worded") | not applied: restructuring where a value lives (statement vs. remark) this late, for a labeling choice that's already honestly caveated, was judged not worth the risk of a fresh edit for a purely cosmetic gain |
| Fable #3 (cosmetic, considered) | `Lambda` reused for two unrelated objects (Lemma 11's `Lambda(y)` remainder function, Proposition 20's `Lambda_l` ratio sequence) | fair catalogue entry, but Fable's own assessment: "context... makes them unambiguous" | not applied, same renaming-risk judgment as every prior round's parallel notation findings |
| Codex, Fable (both, LLM-writing review) | Recurring "X, not Y" antithesis density (~10 instances each independently counted), pseudo-heading proof-transition phrases ("Non-constancy first, unconditionally," "For the quantitative bound," etc.) | accurate catalogues, no new items beyond what's already been weighed in Rounds 18-22 | not applied further; both reviewers explicitly noted the paper is otherwise unusually clean by the project's own Rule 5c checklist (zero em dashes, zero stock transitions, genuine sentence-length variance, asymmetric section lengths) |

Paper unchanged this round -- no edits were made. Both reviewers' full numerical-reproduction tables
(each independently recomputing 15-20+ constants to matching precision, including the Round 22
fixes) are preserved in this session's conversation history; every value checked out.

**This round is the loop's convergence signal.** Per the standing protocol (this file's own opening
paragraphs, "continue until a round returns with no further real findings from either reviewer"):
two independent reviewers, on two different model families neither of which had seen any prior
round's report, both converged on (a) zero new mathematical findings, (b) the same single
recurring, already-settled scope question (repository archival, Rule 8d), and (c) only cosmetic,
optional style notes explicitly labeled as such by the reviewers themselves. Both gave
acceptance-level verdicts unconditionally on the mathematics. Recommendation: pause the loop here
and report convergence to the researcher, rather than continuing to spend further rounds
re-surfacing the same repository-archival request the project has declined on the same grounds
(Rule 12's division of labor) in every round since Round 3.

## Round 24: twenty-second blind loop iteration (2026-08-08), one more round "to be sure", Codex on
## `gpt-5.6-sol` and Fable both complete

Researcher's explicit request after Round 23's convergence report: one more round to confirm,
this time with Codex switched to a specific, stronger model (`gpt-5.6-sol`, via `-m gpt-5.6-sol`,
replacing the CLI's `gpt-5.6-terra` default; confirmed working with a throwaway test call first).
**Fable: another zero-findings, essentially-accept verdict**, including a self-caught false
positive (a fraction/exponent-grouping misread in Theorem 13's `e_3(N)` formula, caught and
corrected before reporting, exactly the kind of extraction pitfall the shared prompt warns about).
**Codex (`sol`): "no fatal mathematical error... recommend revision, not rejection"**, same
repository/certificate scope question as every round, plus one new, genuinely real completeness
gap.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex-sol #5 (real gap, confirmed) | Proposition 20's proof states `H(w_0(tau-c))-H(w_0(tau))=O(1/tau)` immediately after establishing only `w_0(tau-c)-w_0(tau)+c=O(1/tau)` -- i.e. `w_0(tau-c)` and `w_0(tau)` themselves differ by roughly `-c`, not by something small, so applying `H`'s Lipschitz bound directly (without first using `H`'s own periodicity to shift the argument back by `c`) would give the wrong conclusion | **confirmed, real**: independently re-derived the missing step (`H(w_0(tau-c))=H(w_0(tau-c)+c)` by periodicity, then Lipschitz continuity applies since `w_0(tau-c)+c=w_0(tau)+O(1/tau)`) before touching the text; without this intermediate step the displayed conclusion does not follow from what precedes it | fixed: inserted the periodicity step explicitly into the proof, matching the analogous already-explicit pattern used elsewhere in the paper |
| Codex-sol #4 (fair, not applied) | The Section 6 series reversion's error term is asserted before the quantity it bounds (`delta`) is shown to be controlled; suggests a monotonicity estimate to make it fully rigorous rather than "merely formal" | same category as Round 18/19/20's repeated "show more of the arithmetic" requests | not applied, Rule 8d: the underlying algebra was independently re-verified correct by three separate reviewers across rounds 20-24; this is a presentation-depth preference, not an identified gap |
| Codex-sol #6 (restates settled ground) | `e^{H(0)}=0.534122...` in Theorem 1 should be enclosed or moved to a remark | same as Round 22's Fable-independent finding #2, already considered and left as-is (already honestly caveated in the statement) | not reopened |
| Codex-sol #1-3, Fable (restates settled ground) | Repository/certificate archival, Lemma 11/Remark 14 arithmetic not shown, external-quotation verification | same scope questions as every round since Round 3 | not reopened this round -- **but see below: the researcher has asked to resolve the repository-archival and citation-verification items directly, once this round's findings were processed** |

Paper recompiles clean (pdflatex, exit 0, zero `Overfull \hbox`), still 19 pages. The edited passage
(Proposition 20's proof, p.18) visually spot-checked via rendered PNG.

**Net effect of this round**: confirms Round 23's convergence signal rather than overturning it --
one genuine, narrow completeness gap found and fixed (the missing periodicity step), everything
else recurring or already-settled. Two different Codex models (`terra` in Round 23, `sol` in this
round) and Fable across two consecutive rounds have now all independently reached essentially the
same verdict: no mathematical errors, only the same standing repository/citation-verification
items. The researcher has now asked to resolve those two remaining items directly (repository
archival with an immutable identifier, and verification of the load-bearing Wirsching/Berg-Kruppel
quotations against primary sources) rather than continuing to run further blind-critique rounds
against them, since neither is a finding a PDF-only reviewer can actually resolve.

## Post-Round-24 addendum: primary-source citation verification and repository archival

Researcher-directed follow-up to Round 24's convergence report, resolving the two items no
PDF-only reviewer could check (Rule 8e: these were surfaced repeatedly across many rounds --
Opus's Round 20 M1, Round 22 F5, Fable's Round 23 finding #1 -- but never actually resolved).

**Repository sync and pinning.** The reproducibility repository (`github.com/faculdade/
wirsching-conjecture3-proof`) had drifted out of sync with the paper across many rounds of
revision: stale theorem/proposition numbers throughout every README (`Theorem 3`->13,
`Proposition 6/8/9`->8/17/18, `Corollary 2`->3, etc.), and `section3-periodic-correction`'s
oscillation certificate still used the pre-Round-20 grid-plus-Lipschitz upper-bound method rather
than the paper's current, fully-rigorous leading-Fourier-mode method. Fixed: every README updated
to the current numbering; `certify_H_nonconstancy.py`'s `certify_oscillation` function rewritten to
match Proposition 8's current proof exactly (kept the grid-search lower bound `D=4.187449477152e-4`,
replaced the upper-bound method with `4|Hhat(1)|+4*sum_{m>=2}|Hhat(m)|`, giving `osc(H)<=4.187981e-4`).
Every script in the repository re-run and its output independently re-verified against the current
paper before committing (commit `f8248c3`, pushed). The paper's own citation of the repository
(Section 9) is now pinned to that exact commit, so the reference cannot silently drift again if the
repository's default branch changes later. Full DOI archival via Zenodo's GitHub integration is in
progress, pending the researcher creating an actual GitHub Release (the Zenodo webhook fires on
release creation, not on a bare tag push); confirmed via the GitHub API that no release currently
exists.

**Primary-source citation verification**, delegated to a dedicated agent with both primary sources
already local (`literature/papers/wirsching2003-posden.pdf`, `bergkruppel1998.pdf`) and a specific
checklist of every load-bearing equation number, quotation, and the claimed Berg-Kruppel sign
erratum. Full findings:

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| **The Berg-Kruppel sign discrepancy** | The paper's Proposition 18 proof claims BK's own p.179 display for `p^2*f''(p)` reads `+2*beta` where direct differentiation gives `-2*beta` | **CONFIRMED, read at 900dpi from the actual page image, unambiguous** ("the sign before the second `2*beta` is unambiguously a plus, full cross stroke"). Corroborated by an independent second slip found on BK's own next page (a `/a` that should read `/ln(a)` in their own eq. (9.4) specialization) | no paper change needed -- the existing erratum claim was already correct, now independently confirmed against the primary source rather than resting on this project's own re-derivation alone |
| Conjecture 3's exact statement, the verbatim quotation, equations (1.5), (3.2), (6.1), (7.11), (7.12), (7.13), Corollary 7, the `delta_5` notation | All checked directly against Wirsching 2003 | **all confirmed exact matches** (one is a legitimate paraphrase, (7.5), rendered as `<1` instead of the source's `<=1-mu<1`; mathematically equivalent, not a transcription) | no changes needed |
| Berg-Kruppel's (9.1)-(9.7), Proposition 9.1's three constant formulas, Proposition 9.3's infinite product, their closing "expect...bounded" remark | All checked directly against Berg-Kruppel 1998, read from page images (OCR scan) | **all confirmed exact matches**, several also independently re-verified numerically to 34+ digits | no changes needed |
| **Citation error, real**: `x_l^+ := x_l + 3^{-(l+1)}` attributed to Wirsching's "equation (7.14)" | (7.14) is actually a different statement (about auxiliary sequences `x-hat_l`, `y-hat_l`); the actual definition is unnumbered prose on his p.16, immediately before (7.14) | **confirmed real miscitation**, value itself correct, only the equation-number attribution wrong | fixed: reworded to cite "his own definition, unnumbered prose on p.16... immediately before his equation (7.14)" |
| **Citation error, real, most consequential**: the Titchmarsh citation for the zeta zero-free-theorem non-constancy proof pointed to "Theorem 3.8" | Theorem 3.8 is the *quantitative zero-free region* (`sigma>=1-A/log(t)`, `t>t0`, an unspecified threshold), not literally the `Re(s)=1` non-vanishing the paper needs at the specific point `t=omega_1`; the actual result is unnumbered material in Chapter III, section 3.1-3.3 | **confirmed real miscitation, this project's own Round-21 OCR-based re-verification of this exact citation was wrong** -- it concluded 3.8 was correct because it's "the actual numbered theorem," without recognizing 3.8 is a strictly stronger, different statement than what's cited it for | fixed: citation changed to "Chapter III, sections 3.1-3.3," with a clause distinguishing it from Theorem 3.8 explicitly, so a future reader isn't misled the same way this project's own earlier check was |
| **Wording, real**: Discussion mischaracterizes Wirsching's Conjectures 1 and 2 ("pointwise-versus-average transfer for the Elka functions", "uniformity-near-a-singularity... for S_infinity") | Conjecture 1 is about the *generators* `g_l(k,a)` vs. their Haar average (substituted for the Elka functions specifically to enable normalization), not the Elka functions themselves; Conjecture 2 is a uniform lower bound on a ratio of `W_3`-iterates along the comparison class, not a "near-a-singularity" statement | **confirmed real, both since these two conjectures were never Wirsching-verified against the primary source in any earlier round** | fixed: reworded both descriptions to match the primary source |
| Residual gap, disclosed rather than resolved | All Wirsching equation numbers were verified against the Bielefeld preprint (`wirsching2003-posden.pdf`, headed "preliminary version"); the bibliographic details match the published DCDS 9(3):771-787 article via Lagarias's annotated bibliography, but the published article itself is paywalled and no open copy was found, so a numbering shift between preprint and published version cannot be fully ruled out | genuine, disclosed limitation | not resolved this round; the researcher may have institutional journal access to check the published version directly, which neither this project's agents nor its literature folder currently have |
| Four minor wording nits (unmarked quotation elision, "their equation (7.12)" for a Wirsching-numbered equation, Corollary 3 saying "from Proposition 9.3" where the product is in that proposition's proof) | all confirmed accurate as fair nits, explicitly not requiring correction per the verifying agent's own assessment | one applied anyway (cheap): "citing [2] by name at that point" -> "naming [2] in the sentence introducing it," since the by-name mention is one sentence earlier, not literally at that point | three left as-is, matching the verifying agent's own "no correction strictly required" judgment |

Recompiled clean (pdflatex, exit 0, zero `Overfull \hbox`, no undefined-citation warnings), still 19
pages. All four textual fixes (Titchmarsh citation, (7.14) miscitation, Discussion's Conjecture 1/2
wording, the repository commit-pin) visually spot-checked via rendered PNG and `pdftotext`.

**Net effect**: this closes the single largest category of finding this critique loop's own PDF-only
methodology could never resolve on its own (Rule 8e: every one of these had been surfaced and
flagged across at least three separate earlier rounds without ever being checked against a primary
source). The paper's most consequential external claim -- the Berg-Kruppel sign erratum, an
accusation against a published, cited, living author's paper -- is now independently confirmed
correct at the page-image level, not just re-derived from this project's own algebra. Two real
miscitations were found and fixed, including one (the Titchmarsh reference) that this project's own
earlier verification pass (Round 21, working from OCR-extracted text rather than rendered page
images) had gotten wrong itself -- recorded here per Rule 8c rather than left uncorrected.

## Post-Round-24 addendum, continued: DOI archival completed

Full resolution of the repository-archival item, completed with the researcher's own account
actions plus this session's tooling work:

- Installed and authenticated the `gh` CLI (researcher's own GitHub token, confirmed `push`/`admin`
  scope on the `faculdade` org's repository).
- Created a first GitHub Release (`v1.0`, commit `f8248c3`); checked via the GitHub API afterward
  that no Zenodo webhook existed on the repository yet (`hooks` endpoint returned `[]`), meaning the
  Zenodo-GitHub link exists at the account level but had not yet been toggled on for this specific,
  organization-owned repository -- exactly the gap Zenodo's classic GitHub integration requires the
  researcher to close manually, one repository at a time, at `zenodo.org/account/settings/github/`.
- Researcher toggled the repository on; a webhook then appeared (confirmed via the API: `active:
  true`, `events: ["release"]`, pointed at Zenodo's receiver endpoint). Created a second release
  (`v1.0.1`, same commit) to trigger archival, since Zenodo only catches releases created after the
  toggle, not retroactively.
- Confirmed the resulting Zenodo record directly via its public API:
  `doi:10.5281/zenodo.21854549` (concept DOI `10.5281/zenodo.21854548`), title matching the
  repository and release, `access_right: open`.
- **Caught and fixed a metadata problem before citing the DOI**: the record's author field initially
  read "Renato Tavares, Meta Prime Sistemas" (pulled from the researcher's Zenodo account profile
  default), not matching the paper's actual affiliation (Universidade Federal de Goias) or its
  ORCID. Flagged to the researcher before using the DOI anywhere; researcher corrected it on
  Zenodo's side; **re-verified via the API afterward** (not just taken on the researcher's word) --
  the record now reads `Tavares, Renato Augusto / Universidade Federal de Goias /
  0009-0002-0196-3311`, matching the paper's own front matter exactly.
- Updated the paper's Section 9 to cite the DOI (replacing the earlier commit-pin-only citation),
  and `DATA_REPO.md` to record both the commit and the DOI. Recompiled clean, visually confirmed the
  DOI renders as a live link on the References page.

This closes the repository-archival item in full: the reproducibility repository is now
independently, permanently archived, correctly attributed, and cited by DOI in the paper itself, not
just by a mutable GitHub URL or an unlinked commit hash.

## Round 25: twenty-third blind loop iteration (2026-08-08), Codex on `gpt-5.6-sol` and Fable both
## complete, requested by the researcher as a confirming round after the DOI/citation work landed

Researcher's explicit ask: one more round with both reviewers at their strongest configuration
(`gpt-5.6-sol`, Fable), specifically also checking whether the Post-Round-24 addendum's fixes (the
Titchmarsh citation, the DOI-cited repository) read sensibly to a fresh reviewer. **Neither reviewer
found a mathematical error.** Fable: "As submitted, this reads as a rigorous, complete proof of
Theorem 1, Theorem 2, and Proposition 20," after independently re-deriving nearly every identity in
the paper (Theorem 4's recurrence and telescoping, Proposition 6's full Mellin derivation and residue
computations, the analytic non-constancy argument, Proposition 18's algebra including the
Berg-Kruppel sign-discrepancy bookkeeping, the delta_BK/gamma/epsilon series-reversion
identification, Lemmas 9-12's local bounds, and the oscillation certificate arithmetic), and
explicitly confirmed the Titchmarsh fix "reads sensibly and is used consistently with how the text
describes it." Codex (`sol`): "I found no mathematical reason to reject the two principal
theorems... the analytic core is sound," after an independent full-paper re-derivation covering the
same ground plus a direct rendered-page check for clipped formulas (none found: text-block edges
measured at 540.002-540.006pt against a 612pt page width, roughly 70pt of clearance everywhere) and
independent numerical recomputation of every constant it checked (all matched, including the
tail-sum values, the Fourier-mode sums, `H(0)-H(log(3/2))`, `H(w_486746)-H(w_1011118)`, and
`E(18)`, `E(19)`).

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Fable-1 (real, minor completeness gap) | Page 3 asserts phi is "constant, equal to 3/2, on the middle third [1/3,2/3]" with no proof or citation (continuity is separately attributed to Lemma 11, but constancy itself was bare) | **confirmed, real**: a two-line consequence of the already-stated functional equation, support, and normalization, independently re-derived before writing anything (for `x in [1/3,2/3]`, `3x-2<=0` and `3x>=1`, so with `supp phi subset [0,1]` the functional equation's integral collapses to `int_0^1 phi=1`, giving `phi(x)=3/2`) | fixed: the two-line derivation added inline |
| Fable-2 (LLM-writing tell, real) | Lemma 16's statement uses "Moreover", the paper's one surviving stock transition word | **confirmed** | fixed: "Moreover" -> "Also" |
| Codex-sol #1 (fair, real rigor gap, same category as prior rounds' repository-scope findings but with a specific, fixable target) | Lemma 11's proof says "bounding the resulting series by its first few terms gives the stated constant," which is not actually a proof of a bound uniform in every `b_0>=1`; Codex supplied a specific, checkable derivation | **confirmed, real**: independently re-verified Codex's own derivation before using it (`q:=e^{-b_0}`, denominator bounded below by `1-q^2` uniformly using `q^{2*3^k}<=q^2`; numerator bounded via `3^k>=2k+1` giving `sum q^{3^k}<=q/(1-q^2)`; combining and using `q<=e^{-1}` for the final numeric inequality) -- checks out at every step | fixed: Lemma 11's proof rewritten with the full explicit derivation, replacing the "first few terms" hand-wave |
| Codex-sol #2 (fair, minor, real) | `Phi_0(w)=w-log(B_sm(w))` is introduced without stating it needs `B_sm(w)>0`, i.e. `w>ca`; later uses are all safely on `w>ca+1`, so nothing breaks, but the domain should be given where the function is defined | **confirmed, real (minor)** | fixed: added "the latter defined for `w>ca` where `B_sm(w)>0`" at the definition |
| Codex-sol #3 (fair, addressable) | The paper's novelty claim ("is new") for Proposition 6's Fourier series is a literature claim, not something the displayed mathematics proves by itself; asks for either a literature comparison or a softened claim | **fair**; checked against this project's own prior literature work (`notes/H-006.md`, `HYPOTHESES.md` H-002 cross-link, 2026-07-31: "no post-2003 Berg-Kruppel paper resolving the relevant near-0 phi-asymptotic was found") before deciding how to phrase this, per Rule 11 -- a real search was done and found nothing giving a closed Fourier form, so the claim is verified, not invented, but was previously unstated in the paper itself | fixed: added one footnote (not scattered hedging, per Rule 5c's "concentrate the uncertainty") at the first "is new," stating the search was performed and what it covered |
| Codex-sol #4 (fair, addressable) | Section 9 describes the certificates as "certified" without specifying the software, precision, or that the printed run output is the certificate; asks for this to be made explicit rather than left implicit in the linked repository | **fair**, and cheap to state accurately: checked the actual precision settings used in the repository's own scripts (`ctx.dps=100` in `certify_H_nonconstancy.py`, `ctx.dps=90` in `verify_envelope_lemma.py`) before writing a number, rather than guessing one | fixed: one sentence added to Section 9 naming `python-flint`/Arb, the 90-100 decimal digit working precision, and that each script prints its input balls and final enclosure |
| Codex-sol #5 (restates settled ground, formalize-the-repo-as-supplementary-material) | Recommends the archived repository be made "formally part of the submission" (e.g. journal supplementary material) rather than just linked and DOI-cited | already substantively addressed (DOI-archived, immutable, cited by commit and DOI in Section 9, Post-Round-24 addendum) | not further changed: whether a specific journal requires supplementary-material submission (as opposed to a cited, permanent DOI) is a venue-specific submission-mechanics question for when a venue is chosen, not a paper-content gap |
| Codex-sol #6 (restates settled ground) | Several numerical inequalities (Lemma 9's local bounds, Remark 14's `E(N)` monotonicity/bound over `19<=N<=5000`, the `<1e-45` rounding-accumulation claim on p.8) are asserted with the derivation or check pointed at the repository rather than shown inline | same "repository vs. inline" scope question raised and settled in Rounds 3-24 (most recently Round 5's I3/I6, Round 6's K-repo) | not reopened, Rule 8d: no new argument given this round beyond what was already weighed; the one item from this same family that WAS a genuine gap (Lemma 11, not a numeric assertion but a missing uniform-tail argument) is fixed above as Codex-sol #1 |
| Codex-sol, Fable (both, LLM-writing review) | Recurring "X, not Y" antithesis and defensive-parenthetical density, "Wirsching's own"/"their own" repeated attribution phrasing, aphoristic structural-insight sentences ("This single structural fact is the source of every phase-independent constant below") | accurate catalogues, same style family already weighed in Rounds 18-23 | not applied further this round: the specific new item found (Fable-2's "Moreover") is fixed above; the recurring "own" attribution phrasing is a deliberate, repeated choice to keep every borrowed object's origin unambiguous in a paper that borrows heavily from two external sources, not an accidental tic, and was judged not worth another rewrite pass for a cosmetic style preference already logged |

**Verification method**: every finding acted on this round was independently re-derived or
re-checked before touching the text, per Rule 8c -- Codex-sol #1's tail-bound algebra recomputed
step by step (the `q^{2\cdot3^k}\le q^2` bound, the `3^k\ge2k+1` bound, and the final `q\le e^{-1}`
numeric threshold all checked directly); Codex-sol #3's novelty claim checked against this project's
own prior, dated literature-search record rather than assumed; Codex-sol #4's precision numbers
pulled from the actual repository scripts rather than estimated. Fable-1's derivation re-derived from
the already-stated functional equation before being added to the text.

Recompiled clean (pdflatex, exit 0, zero `Overfull \hbox`, no undefined-citation warnings), still 19
pages, zero em dashes. All five edited passages (the footnote on Corollary 3, Lemma 11's proof, Lemma
16's statement, Lemma 16's domain clause, Section 9) visually spot-checked via rendered PNG at
150dpi.

**Net effect of this round**: two independent reviewers, both at their strongest available
configuration, found zero mathematical errors after a full adversarial re-derivation of the paper's
entire analytic core, and both explicitly confirmed the Post-Round-24 citation and archival fixes
read correctly to a fresh reader. One real (if minor) completeness gap was closed (Lemma 11's tail
bound now has an actual uniform proof instead of a hand-wave), one genuine LLM-writing tell was
removed, and two small, cheap rigor/transparency additions were made (Phi_0's domain, Section 9's
precision statement, the novelty footnote). Every remaining open item across all 25 rounds is the
same repository-vs-inline documentation-depth question, raised and settled the same way since Round
3. This is the strongest convergence signal yet: the two most capable configurations available in
this loop (Codex on its top model, Fable) both independently reached essentially the same verdict as
every reviewer since Round 22, with no new severity-escalating finding.

## Round 26: twenty-fourth blind loop iteration (2026-08-08), Codex on `gpt-5.6-sol` and Fable both
## complete, one more confirming round at the researcher's request

Researcher's explicit ask after Round 25: "one more round just to be sure." Both reviewers again
found zero fatal mathematical errors after a full independent re-derivation of the paper's analytic
core (Fable: "I found no computational or logical error in the machinery underpinning Theorems 1 and
2," after re-deriving Proposition 6's Mellin/residue computation from scratch and independently
testing the Theorem 13 + Proposition 17 + Proposition 18 chain numerically out to tau~433; Codex-sol:
"I found no gap in the Mellin analysis, the saddle-point transfer, the uniformity argument, or the
phase analysis," recommending "revise, then accept subject to verification of the archived interval
computations and the quotations from [1] and [2]"). This round produced this loop's first genuine,
if minor, mathematical slip caught in the paper's own already-displayed prose (not just an exposition
gap), a real self-inflicted precision-documentation inconsistency from Round 25's own fix, and two
findings that checked out as false or already-resolved rather than real.

| ID | Summary | Verdict | Status |
|----|---------|---------|--------|
| Codex-sol #2 (real, minor mathematical error, new) | Remark 15 (Edgeworth heuristic) says "the `b_j>=1` summands behave asymptotically like independent `Exp(1)` variables, so `X` under its tilt is asymptotically `Gamma(N,1)`-distributed" -- but it is `sX = sum_j b_jU_j` that approaches `Gamma(N,1)`, not `X` itself | **confirmed, real**: checked by dimensional analysis against Lemma 10 before touching the text (`Var(X)` under the tilt is `K''(s)=V/s^2~N/s^2`, matching `Gamma(N,1)`'s variance `N` only after scaling by `s`, i.e. for `sX`, not for `X` unless `s=1`) | fixed: "the `b_j>=1` summands of `sX=sum_j b_jU_j`... so `sX` under its tilt is asymptotically `Gamma(N,1)`-distributed" |
| Codex-sol #1 (moderate, real, self-inflicted by this project's own Round 25 fix) | Section 9 (added last round) states the repository's scripts run at "90 to 100 decimal digits," while Proposition 8's own proof (pre-existing text) twice states "`250`-bit working precision" for the same certified values; `250` bits is about `75` decimal digits, not `90`-`100`, an internal inconsistency between two places both claiming to describe the same computation's precision | **confirmed, real, introduced by this project's own Round 25 addition**: checked which is actually higher before writing a fix (`100` decimal digits `~332` bits `> 250` bits), so the archived repository is a strictly higher-precision independent reproduction, not a weaker one, but nothing in the paper said so | fixed: Section 9 now states the repository's precision in both digits and bits, and explicitly says it exceeds the `250`-bit figure quoted in Proposition 8's proof, reconciling the two rather than leaving them looking contradictory |
| Codex-sol #3 (minor, real, cheap) | The end of Theorem 2's proof writes `limsup/liminf >= e^{osc(H)} >= 1.0004188` with the limiting variable and the ratio's operand left implicit | **confirmed, real (minor)** | fixed: introduced `Psi(t):=phi(t)/phi_0(t)` and wrote `limsup_{t->0+}Psi(t) / liminf_{t->0+}Psi(t) >= e^{osc(H)}` explicitly, with a clause spelling out what the inequality means |
| Codex-sol #4 (restates settled ground) | Remark 14's `E(N)` monotonicity/bound claim over `19<=N<=5000` is "checked directly in the accompanying repository" rather than proved or given as a machine-verified interval; suggests removing it, proving it, or stating an exact certified interval | same scope question raised and settled in Rounds 3-25 (most recently Round 25's own Codex-sol #6) | not reopened, Rule 8d: the claim is already honestly labeled as unproved and explicitly flagged as unused ("though only `E(N)->0`... is used"), no new argument given |
| Fable-1 (checked, found already correct, not a real defect) | Discussion's "Elka functions" (`substituted for the Elka functions themselves`) is unfamiliar, undefined terminology with no citation pointer; recommends confirming it against Wirsching's own text or glossing it | **checked against this project's own prior primary-source read** (`literature/notes/L-002.md`, Wirsching 1998's own book, read in full: "Elka functions" is his own term, `e_l(k,a)`, defined in Section II.4) -- genuine terminology, not a transcription slip, but the paper gave no citation pointer for it | fixed anyway, cheaply: added "`, defined in [3], Section II.4,`" at the term's only occurrence, closing the gap Fable correctly identified even though the term itself was already right |
| Fable-2 (checked, false positive) | Quotes the abstract as reading "a classical zero-free theorem for zeta shows H directly that it is not constant," flagging garbled word order | **checked directly against the compiled PDF and the source**: the actual text reads "...shows directly that it is not constant" (no "H" before "directly"); Fable's quotation does not match the manuscript | not changed: the text was already correct, this is a misquotation by the reviewer, not a defect, recorded per Rule 8c rather than silently discarded |
| Fable-3 (already resolved, re-confirmed) | Recommends re-confirming the Berg-Kruppel `+2beta`/`-2beta` sign discrepancy directly against the primary source before publication | **already done**: Post-Round-24 addendum confirmed this directly at 900dpi against a rendered page image of [2] p.179 | no action needed, already-verified ground |
| Codex-sol, Fable (both, LLM-writing review) | Recurring "own"/"exactly" density (Codex-sol counts ~29/~35 occurrences), meta-commentary sentences describing the proof's own architecture, "not X but Y" contrasts, page 19's "the constant chain behind Theorem 13" reading as software-workflow language | accurate catalogues, same style family weighed repeatedly since Round 18; Codex-sol explicitly separates this from the mathematics ("the mathematical core looks as though it has been repeatedly checked and repaired") | not applied further: no specific new instance was flagged as a concrete, isolated tell the way Round 25's "Moreover" was; the repeated "own" attribution phrasing remains a deliberate choice (see Round 25's own reasoning) and the general density complaint is noted, not actioned, absent a specific sentence to fix |

**Verification method**: Codex-sol #2 checked by an independent dimensional argument (`Var(X)` under the
tilt versus `Gamma(N,1)`'s variance) before editing; Codex-sol #1 checked by converting both stated
precisions to a common unit (bits) before writing the reconciling sentence, confirming the repository
is the higher-precision side rather than assuming it; Fable-1 checked against this project's own
already-completed primary-source read of Wirsching's 1998 book (not re-read from scratch, since
`literature/notes/L-002.md` already recorded a full read with the exact section number); Fable-2
checked by direct comparison against the compiled PDF's actual text before declining to change
anything, per Rule 8c.

Recompiled clean (pdflatex, exit 0, zero `Overfull \hbox`, no undefined-citation warnings), still 19
pages, zero em dashes. All four edited passages (the Elka citation in Section 8, Remark 15's `sX`
fix, Theorem 2's proof, Section 9's precision reconciliation) visually spot-checked via rendered PNG
at 150dpi.

**Net effect of this round**: the first round to catch a real error in the paper's own prior-round
output rather than only in long-standing text (Codex-sol #1, a precision-documentation inconsistency
this project introduced in Round 25 while fixing something else, the same self-correcting pattern
flagged in Rounds 20 and 22), plus one genuine minor mathematical slip in an explicitly
non-load-bearing heuristic remark (Codex-sol #2, `X` vs `sX` in the Gamma-law analogy). Neither
finding touches Theorem 1, Theorem 2, or Proposition 20's actual proofs. Both reviewers' overall
verdicts remain at "no fatal error, revise for documentation/citation-verification reasons" (Codex-sol)
and "rigorous proof of what it claims" (Fable), matching every round since Round 22. Two reviewer
findings (Fable-2's misquoted abstract sentence, Fable-3's already-settled sign-discrepancy request)
checked out as not requiring any change. The recurring repository-documentation-depth question is the
only item that has now survived unchanged across every one of 26 rounds since Round 3.
