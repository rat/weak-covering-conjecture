# Paper 01: Wirsching's Conjecture 3

## Scope

Resolves Conjecture 3 from G. J. Wirsching, "On positive predecessor density in 3n+1 dynamics"
(Discrete Contin. Dyn. Syst. 9(3), 2003), one of three conjectures his positive-predecessor-density
argument reduces to (Conjectures 1 and 2 are untouched). Two results:

1. **Theorem A.** Wirsching's Conjecture 3, exactly as stated (restricted to his phase-locked
   comparison class `Ã_δ`), is true: `φ(z_l)/φ₀(z_l) → e^{H(0)}` uniformly on the class.
2. **Theorem B.** The stronger, unrestricted asymptotic `φ(t) ~ c·φ₀(t)` as `t → 0⁺` (the route
   Wirsching's own text proposes and declines) is false: the ratio oscillates with period `log 3`
   in `log(1/t)`, amplitude rigorously bounded away from zero, Fourier coefficients closed-form via
   Γ and ζ.
3. **Corollary.** The periodic correction `H` found here is exactly Berg–Krüppel's own undetermined
   periodic factor `Q` from their 1998 saddlepoint asymptotic (Prop. 9.3), given in closed form for
   the first time.

Both a and b needed for Wirsching's own argument to close no more than a weaker, sufficient
inequality (`limsup Λ_l < 3/2`), verified directly with a large margin.

## Source hypothesis

H-006 in this project's HYPOTHESES.md, status `closed-confirmed`. Full derivation history in
notes/H-006.md, notes/H-006-envelope.md, notes/H-006-formula-A-proof.md,
notes/H-006-formula-A-proof-2.md. Every claim below was independently constructed at least twice
(Codex and a separate Opus run) and reviewed by a fresh-context adversarial critic; see those files
for the full verification record. This paper condenses that record into a single, self-contained,
citable proof.

## Structure

1. Introduction: statement of Theorems A, B, and the Corollary; context (Wirsching's reduction,
   Berg–Krüppel's asymptotic, prior status of Conjecture 3); structure of the paper.
2. Preliminaries: `X`, `φ`, `K(s)`, the exact recurrence, `φ₀`.
3. The periodic correction `H`: exact telescoping identity, Fourier coefficients, certified bounds
   (`H'`, `H''`, `osc(H)`, `H(0) ≠ H(log(3/2))`).
4. Formula (A): the uniform saddlepoint approximation to `φ`. Statement and proof.
5. The envelope lemma: bridging the smooth-saddle system to `φ` itself.
6. The `P`–Berg–Krüppel identity: exact match to their Prop. 9.1, closed-form constant, the
   Corollary.
7. Proof of Theorems A and B; verification of Wirsching's actual requirement.
8. Discussion: scope, what remains open (Conjectures 1, 2), the rate (`O(N^{-1/2})`, not the sharp
   `-1/(12N)`), why Wirsching's retreat to the weaker conjecture was necessary.
9. Code and data availability.
10. Acknowledgments (Rule 5b: AI credited for textual review and translation only).

## Status

- [x] main.tex drafted (2026-08-04), compiles clean (pdflatex, no warnings, 9 pages)
- [x] reproducibility repo populated (2026-08-04): 5 self-contained scripts, one per section with
      a numerical/certified claim, each verified to run clean from a fresh clone
      (git@github.com:faculdade/wirsching-conjecture3-proof.git)
- [x] critique round 1 complete (2026-08-04): 15 findings, all 15 fixed (CRITIQUE.md); the one
      researcher-action item (making the reproducibility repo public) was completed 2026-08-05,
      verified `curl` returns 200
- [x] critique round 2 complete (2026-08-04): independent different-vendor review, 7 findings, 1
      real algebra bug fixed, 2 completeness gaps acknowledged as known scope, repo-access gap same
      as round 1
- [x] critique round 3 complete (2026-08-04/05): PDF-only blind loop, Codex+Opus at max effort,
      Codex's initial verdict was Reject; 7 confirmed real findings fixed (Lemma 12's constant was
      wrong by ~3x and is now rigorously re-derived, Lemma 15's domain and its `g_tau''` bound were
      wrong and are now a full proof with explicit constants, Proposition 17's proof is now a full
      derivation against Berg-Kruppel's primary source instead of "direct substitution", plus a
      real LaTeX footnote-rendering bug and two minor naming/wording issues); paper recompiles
      clean, 12 pages.
- [x] critique rounds 4-6 complete (2026-08-05): PDF-only blind loop continued on Codex+Opus,
      several more real findings fixed per round (wrong Mellin multiplier in Proposition 6,
      Propositions 6/8/16 converted from sketches to complete proofs, a lost-text LaTeX
      overfull-hbox bug, an unjustified O-notation-to-numeric-bound leap in Lemma 15, assorted
      wording/citation-precision fixes); paper now 16 pages, zero warnings. Reproducibility repo
      made public 2026-08-05.
- [x] critique rounds 7-24 complete (2026-08-05/08): loop continued (Opus, then Fable as the
      second reviewer per the researcher's instruction; Codex switched to `gpt-5.6-sol` from
      Round 24), converging at Rounds 23-24 (zero new mathematical errors across two independent
      reviewer passes each). Non-constancy of `H` upgraded from computational to analytic (classical
      zeta zero-free theorem). Every load-bearing citation to Wirsching 2003 and Berg-Kruppel 1998
      verified directly against the primary sources (two real miscitations found and fixed).
      Reproducibility repo DOI-archived via Zenodo (`doi:10.5281/zenodo.21854549`, commit `f8248c3`)
      and cited in Section 9. Paper 19 pages.
- [x] critique rounds 25-27 complete (2026-08-08): two further confirming rounds at both
      reviewers' strongest configuration, plus a dedicated regression check (Round 27) confirming
      Rounds 25-26's own fixes introduced no new error. Full detail in CRITIQUE.md.
- [x] **paper declared final by the researcher, 2026-08-08.** See CRITIQUE.md's closing note and
      papers/INDEX.md.
- [x] pt-BR version (main-pt.tex) written 2026-08-08, on the researcher's explicit request: full
      translation of every prose passage, every equation/label/cross-reference/numeric
      literal/bibliography entry kept identical to main.tex (verified: labels and bibliography keys
      match exactly, every long decimal literal byte-identical); compiles clean, 20 pages, zero
      errors, zero em dashes
- [ ] researcher's own read: still pending, the one item no critique round can substitute for
- [x] **submitted to arXiv, 2026-08-09** (category math.NT, license CC BY 4.0, per the decision
      recorded above). arXiv ID to be filled in here and in `papers/INDEX.md` once assigned.

## Target venue

**Decided (2026-08-08):** arXiv preprint, category `math.NT`, license CC BY 4.0. No target journal
for now; revisit once the preprint is out. English only as of this decision, per the researcher's
standing instruction; the pt-BR version (Rule 5) remains deferred until requested.
