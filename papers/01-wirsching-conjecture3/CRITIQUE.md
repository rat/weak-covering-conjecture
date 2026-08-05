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
