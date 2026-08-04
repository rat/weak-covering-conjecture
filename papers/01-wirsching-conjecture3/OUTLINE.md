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
- [ ] reproducibility repo populated and every script verified to actually run
- [ ] critique round complete, every finding fixed or rejected with reason
- [ ] pt-BR version (main-pt.tex): deferred, only on the researcher's explicit request

## Target venue

arXiv preprint (math.NT or math.DS) first; journal not yet decided (per this project's CLAUDE.md
Section 1). English only for now, per researcher's explicit instruction (2026-08-04).
