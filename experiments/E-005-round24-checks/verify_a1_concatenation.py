"""
A1 check (H-003 round 24, GAP A item 1): does Codex's concatenation identity
  G(uv) = G(u) + 3^r * 2^{-A(u)} * G(v)
hold as literally stated, with A(u) the cost of the prefix u alone?

Result: no (0/5000 random trials). The correct identity needs the offset to include
the connecting gap between u and v (the first gap of what should be "v"), not just
u's own internal cost. Verified both forms below against 5000 random (l, r, gaps)
triples using exact Fraction arithmetic (no modular reduction, so this tests the
underlying algebraic identity directly, independent of any residue-class subtlety).
"""
from fractions import Fraction as Fr
import random


def G(gaps, l):
    """gaps = (a_2,...,a_l), each integer >= 1; l terms total (rank 1..l)."""
    c = 0
    tot = Fr(0)
    for i in range(1, l + 1):
        if i >= 2:
            c += gaps[i - 2]
        tot += Fr(3) ** (i - 1) * Fr(1, 2) ** c
    return tot


def check(seed=1, n=5000):
    random.seed(seed)
    n_literal_ok = n_corrected_ok = 0
    for _ in range(n):
        l = random.randint(3, 10)
        r = random.randint(1, l - 1)
        gaps = [random.randint(1, 5) for _ in range(l - 1)]  # a_2..a_l
        G_full = G(gaps, l)

        u_gaps = gaps[: r - 1]
        G_u = G(u_gaps, r)
        v_gaps = gaps[r:]                 # drops the connecting gap gaps[r-1] = a_{r+1}
        G_v = G(v_gaps, l - r)
        join_gap = gaps[r - 1]
        c_r = sum(gaps[: r - 1])          # cost of u alone (Codex's literal "A(u)")
        c_r1 = c_r + join_gap             # cost through the connecting gap (the correction)

        literal = G_u + Fr(3) ** r * Fr(1, 2) ** c_r * G_v
        corrected = G_u + Fr(3) ** r * Fr(1, 2) ** c_r1 * G_v

        n_literal_ok += (G_full == literal)
        n_corrected_ok += (G_full == corrected)
    return n_literal_ok, n_corrected_ok, n


if __name__ == "__main__":
    lit, corr, n = check()
    print(f"literal formula (A(u) = cost of u alone) matches:      {lit}/{n}")
    print(f"corrected formula (A(u) must include the join gap):    {corr}/{n}")
    assert lit == 0 and corr == n, "unexpected result, re-check by hand before trusting this script"
