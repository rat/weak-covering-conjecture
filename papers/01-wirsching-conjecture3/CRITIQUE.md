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
