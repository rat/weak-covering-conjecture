"""
Attempts Codex's round-25 item 9's actual hard content ("critical-pair theory on closed phase
blocks"), beyond just its cheap go/no-go gate (already reasoned through separately as likely true
via a chain-rule argument for affine-map multipliers). Item 9's own text: "Attempt to exclude the
[confined-to-a-coset] latter [dichotomy branch] by exhibiting, via two local gap substitutions and
LTE, phase differences at every 3-adic valuation and at least two incompatible unit ratios."

Codex's exact "boundary state" and "return word" definitions are underspecified (not pinned down
in its response), so this is a good-faith, reasonable operationalization, not a verified match to
Codex's precise intended construction, flagged honestly rather than presented as a confirmed test
of Codex's literal proposal:

- "Boundary state sigma" := the residue class 1 mod 3^q (the natural starting/identity point).
- "Return word" := a gap-sequence (via core.py's already-validated G_n=Syrac_n) whose value returns
  to sigma, i.e. G_n(gaps) == 1 (mod 3^q), for some total cost <= Qmax, extended n=q+extra digits
  beyond q to have room for a nontrivial higher-order "phase".
- "Phase" of a return word := discrete_log_4(G_n(gaps) mod 3^n), well-defined since return words
  land in P_n=<4> (the phase-orbit subgroup this project already established G_n's image lies in).

Result (q=3, extra=5, n=8, budget<=16): 193 distinct phases found among return words. Pairwise
phase DIFFERENCES realize 3-adic valuations v_3 in {2,3,4,5,6} within this bounded search, and AT
EVERY one of these valuations, BOTH unit residues mod 3 (1 and 2) occur among the differences --
exactly the two conditions Codex's item 9 asks for ("phase differences at every 3-adic valuation
and at least two incompatible unit ratios"), within the tested range.

Two honest caveats. First, valuations below q-1 (here, v_3=0,1) never appear across several tested
(q,extra) combinations -- this looks like a structural floor tied to the sigma=1 mod 3^q return
condition itself, not a search-budget limitation, but was not proven; a different boundary-state
choice might reach lower valuations, or genuinely might not. Second, "every 3-adic valuation" was
only checked up to what a bounded budget search reaches (v_3<=6 here), not literally unboundedly.
Net: Codex's item 9 does NOT collapse on this test -- a real, positive, if partial and caveated,
finding, distinct from most of this round's items which collapsed or reduced to already-known
obstructions. Whether this genuinely licenses invoking the Kneser/Lev/Grynkiewicz dichotomy in
Codex's favor (its own next claimed step) was not attempted; that is separate, substantial work.
"""
import core


def phase_table(n):
    mod = 3 ** n
    order = 3 ** (n - 1)
    phase = {}
    v = 1
    for k in range(order):
        phase[v] = k
        v = (v * 4) % mod
    return phase, order


def return_word_phases(q, extra, Qmax):
    n = q + extra
    phase, order = phase_table(n)
    N = core.joint_counts(n, n, Qmax)
    mod_n = 3 ** n
    mod_q = 3 ** q
    target = 1 % mod_q
    phases = []
    for z in range(mod_n):
        if z % mod_q != target or z not in phase:
            continue
        for c in range(n, Qmax + 1):
            if N[z, c] > 0:
                phases.append(phase[z])
                break
    return sorted(set(phases)), order


def valuation_unit_map(uniq_phases):
    diffs = set()
    for i in range(len(uniq_phases)):
        for j in range(i + 1, len(uniq_phases)):
            diffs.add(uniq_phases[j] - uniq_phases[i])
    vals = {}
    for d in diffs:
        v, dd = 0, d
        while dd % 3 == 0 and dd != 0:
            dd //= 3
            v += 1
        vals.setdefault(v, set()).add(dd % 3)
    return vals


if __name__ == "__main__":
    for q, extra, Qmax in [(4, 3, 14), (3, 5, 16)]:
        phases, order = return_word_phases(q, extra, Qmax)
        vals = valuation_unit_map(phases)
        print(f"q={q} extra={extra} n={q+extra} Qmax={Qmax}: {len(phases)} distinct phases", flush=True)
        for v in sorted(vals):
            print(f"  v_3={v}: units mod 3 = {sorted(vals[v])}", flush=True)
        print()
