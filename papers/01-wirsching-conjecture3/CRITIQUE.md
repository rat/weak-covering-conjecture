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
