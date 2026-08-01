"""
First small-scale run of Codex's fully-specified "mod-3 leading-influence matrix" / barrier-
profile experiment (second lateral cycle, round 2), now that the load-bearing Lucas-diagonal
lemma is independently confirmed (verify_round2_lateral2.py, 2612 checks, all match).

Small scale (l=4, j=j*(4)=7) so witness tuples can be obtained by direct brute-force enumeration
(exact, no reconstruction heuristics needed) alongside the real defect/non-defect classification
from the already-established next-digit mask machinery (rounds 8-9 of the first lateral cycle).
"""
from itertools import combinations, product
from math import comb

def F(alphas):
    return sum(3**i * 2**a for i, a in enumerate(alphas))

def brute_force_witnesses(j, mod):
    """Return dict: residue mod `mod` -> one witness tuple (sorted descending) achieving it."""
    witnesses = {}
    for combo in combinations(range(2 * j), j):
        alphas = tuple(sorted(combo, reverse=True))
        v = F(alphas) % mod
        if v not in witnesses:
            witnesses[v] = alphas
    return witnesses

def all_fiber_members(j, mod, target):
    out = []
    for combo in combinations(range(2 * j), j):
        alphas = tuple(sorted(combo, reverse=True))
        if F(alphas) % mod == target:
            out.append(alphas)
    return out

l = 6
j = 10  # j*(6)
mod_l = 3**l          # 81
mod_l1 = 3**(l + 1)   # 243

print(f"=== l={l}, j=j*(l)={j}: building the old next-digit defect graph ===")
witnesses_l1 = brute_force_witnesses(j, mod_l1)  # residues mod 3^(l+1) -> witness

# mask at level l (as in round 8): for each parent r mod 3^l, which of 3 lifts mod 3^(l+1) occur
masks = {}
for r in range(mod_l):
    if r % 3 == 0:
        continue
    present = set()
    for a in range(3):
        x = r + a * mod_l
        if x in witnesses_l1:
            present.add(a)
    masks[r] = present

defects = []  # (parent, missing_digit, x) for missing children
attained = []
for r, mask in masks.items():
    for a in range(3):
        x = r + a * mod_l
        if x % 3 == 0:
            continue
        if a in mask:
            attained.append(x)
        else:
            defects.append(x)

print(f"  {len(defects)} defect residues (mod {mod_l1}) at this budget, {len(attained)} attained")
print(f"  defect residues: {defects}")

if not defects:
    print("  No defects at this (l,j) -- pick a different l for the demo.")
else:
    defect_x = defects[0]
    # distance-1 "near-defect": a residue mod 3^(l+1) adjacent to a defect. Use the sibling
    # residues of the SAME parent (share mod 3^l) that ARE attained, as the natural graph
    # neighbors in the next-digit state graph.
    parent = defect_x % mod_l
    siblings = [parent + a * mod_l for a in range(3) if (parent + a * mod_l) in witnesses_l1
                and (parent + a * mod_l) != defect_x]
    near_defect_x = siblings[0] if siblings else None
    # a matched non-defect control: an attained residue from a DIFFERENT, fully-attained (mask
    # size 3) parent, for contrast
    control_x = None
    for r, mask in masks.items():
        if len(mask) == 3 and r != parent:
            control_x = r + list(mask)[0] * mod_l
            break

    print(f"\n  defect_x={defect_x} (no witness -- no admissible tuple reaches it at this budget)")
    print(f"  near_defect_x={near_defect_x} (sibling of the defect's parent, distance 1)")
    print(f"  control_x={control_x} (attained, parent has a full mask)")

    def to_jets(alphas):
        eps = [a % 2 for a in alphas]
        n = [a // 2 for a in alphas]
        return eps, n

    def J(eps, n, r):
        total = 0
        for i in range(min(r, len(n) - 1) + 1):
            k = r - i
            if 0 <= k <= n[i]:
                total += (2 ** eps[i]) * comb(n[i], k)
        return total

    inv2 = pow(2, -1, 3)

    def buffered_cells(eps, n, M):
        """(i,m) with digit_m(n_i)==1 and both n_i+3^m, n_i-3^m give an admissible full tuple
        when substituted for alpha_i (all else fixed): here we just require n_i-3^m>=0 and the
        resulting alpha_i +/- 2*3^m keeps alpha strictly between its neighbors."""
        alphas = [eps[i] + 2 * n[i] for i in range(len(n))]
        cells = []
        for i in range(len(n)):
            for m in range(M + 1):
                digit_m = (n[i] // 3**m) % 3
                if digit_m != 1:
                    continue
                if n[i] - 3**m < 0:
                    continue
                lo = alphas[i + 1] if i + 1 < len(alphas) else -1
                hi = alphas[i - 1] if i > 0 else None
                a_plus = alphas[i] + 2 * 3**m
                a_minus = alphas[i] - 2 * 3**m
                ok_plus = (hi is None or a_plus < hi) and a_plus > lo
                ok_minus = (hi is None or a_minus < hi) and a_minus > lo
                if ok_plus and ok_minus:
                    cells.append((i, m))
        return cells

    def L_matrix(eps, n, cells, R):
        rows = list(range(R + 1))
        mat = []
        for r in rows:
            row = []
            for (i, m) in cells:
                n_plus = n[:]; n_plus[i] += 3**m
                n_minus = n[:]; n_minus[i] -= 3**m
                Jp = J(eps, n_plus, r)
                Jm = J(eps, n_minus, r)
                L = ((Jp - Jm) * inv2) % 3
                row.append(L)
            mat.append(row)
        return mat

    def rank_f3(mat):
        # Gaussian elimination over F_3, returns rank
        if not mat or not mat[0]:
            return 0
        M = [row[:] for row in mat]
        rows_n, cols_n = len(M), len(M[0])
        rank = 0
        col = 0
        for col in range(cols_n):
            pivot = None
            for r in range(rank, rows_n):
                if M[r][col] % 3 != 0:
                    pivot = r
                    break
            if pivot is None:
                continue
            M[rank], M[pivot] = M[pivot], M[rank]
            inv = pow(M[rank][col], -1, 3)
            M[rank] = [(x * inv) % 3 for x in M[rank]]
            for r in range(rows_n):
                if r != rank and M[r][col] % 3 != 0:
                    factor = M[r][col]
                    M[r] = [(M[r][k] - factor * M[rank][k]) % 3 for k in range(cols_n)]
            rank += 1
        return rank

    def barrier_profile(label, alphas, M_cutoff=2):
        print(f"\n  --- {label}: alphas={alphas} ---")
        eps, n = to_jets(alphas)
        ell = len(alphas)
        R = (ell - 1) + 3**M_cutoff
        cells = buffered_cells(eps, n, M_cutoff)
        print(f"    {len(cells)} buffered admissible cells (M<={M_cutoff}): {cells}")
        if not cells:
            print("    (no buffered cells at this cutoff -- nothing to analyze)")
            return
        mat = L_matrix(eps, n, cells, R)
        # verify Lucas property for every generated column, as instructed
        for ci, (i, m) in enumerate(cells):
            leading = i + 3**m
            for r in range(R + 1):
                val = mat[r][ci]
                if r < leading and val != 0:
                    print(f"    LUCAS CHECK FAILED col=({i},{m}) r={r}: expected 0, got {val}")
                if r == leading and val != (2**eps[i]) % 3:
                    print(f"    LUCAS CHECK FAILED col=({i},{m}) r={r}: expected {(2**eps[i])%3}, got {val}")
        ranks = []
        for q in range(R + 1):
            sub = [mat[r] for r in range(q + 1)]
            ranks.append(rank_f3(sub))
        deltas = [ranks[0]] + [ranks[k] - ranks[k-1] for k in range(1, len(ranks))]
        print(f"    rank_q sequence (q=0..{R}): {ranks}")
        print(f"    Delta_q sequence:          {deltas}")
        leading_diagonals = {i + 3**m for (i, m) in cells}
        gaps = [r for r in range(R + 1) if r not in leading_diagonals]
        print(f"    leading-gap rows (no buffered cell with i+3^m=r): {gaps}")

    print(f"\n  Note: the defect itself (x={defect_x}) has NO witness tuple by definition (that is")
    print(f"  what makes it a defect); d_defect(x)=0 configurations don't exist as tuples to")
    print(f"  analyze. Comparing distance-1 (near-defect, an attained sibling of a defect) against")
    print(f"  a distance->2 control (attained, from a fully-flexible parent), as Codex specified.")

    if near_defect_x is not None:
        barrier_profile("NEAR-DEFECT (attained sibling of a defect, distance 1)", witnesses_l1[near_defect_x], M_cutoff=1)
    if control_x is not None:
        barrier_profile("CONTROL (attained, full-mask parent, distance >=2 from any defect)", witnesses_l1[control_x], M_cutoff=1)
