"""
Independent verification of the round-23 literature finding (H-003):

  (A) Reproduce Toguchi's table (Zenodo 10.5281/zenodo.20490181) of
      M_n = max_k |psi_n(k)| and k*(n) = argmax, for n <= 9, by TWO
      independent routes: the dual-space recursion, and a forward
      construction of the full distribution P_n followed by a DFT.

  (B) Verify the object identity between Tao's Syrac(Z/3^n Z) and this
      project's R_{l-1,j}: both are unit multiples of the same core sum
      G = sum_{i=1}^{l} 3^{i-1} 2^{-(a_2+...+a_i)} over gap tuples a_j >= 1.
      Checked against the project's own ground-truth checkpoint
      (l=2, j=2 -> {1,2,5,7} mod 9).

  (C) Verify that psi_n is an exact convex combination of normalized
      "layer sums" L_{B,u}/|T_B|, where L_{B,u} is (up to a unit twist of the
      frequency) exactly this project's budget-constrained exponential sum
      S(t). This is the bridge that lets Toguchi's measured M_n be read as a
      lower bound on the project's own S(t).

  (D) Compare the measured M_n against the two thresholds that matter:
      square-root cancellation (~|T_B|^{-1/2} ~ 2^{-n}) and the decay the
      L^1 Fourier covering criterion actually needs (~3^{-n}).

Deliberately tiny: n <= 9 means arrays of at most 2*3^8 = 13122 complex
entries. Safe to run next to the memory-committed jstar/mpg jobs.
"""
import cmath
import math
from itertools import combinations

TOGUCHI = {  # n: (M_n, k*(n)) transcribed from Table 1 of the preprint
    1: (5.77350e-1, 0), 2: (3.77924e-1, 2), 3: (2.52237e-1, 3),
    4: (1.76999e-1, 4), 5: (1.29274e-1, 5), 6: (9.61064e-2, 6),
    7: (7.58700e-2, 8), 8: (6.08907e-2, 9), 9: (4.80262e-2, 10),
}


def psi_via_distribution(n, atrunc=200):
    """Route 1: build the exact distribution of Syrac(Z/3^n Z) by Tao's
    Lemma 1.12 recursion  Syrac_{n+1} = 2^{-a} (3 Syrac_n + 1),  a ~ Geom(2),
    then DFT it.  Returns dict k -> psi_n(k) for k in [0, 2*3^{n-1})."""
    mod = 3
    # level 1: Syrac_1 = 2^{-a_1} mod 3
    P = {}
    inv2 = pow(2, -1, 3)
    for a in range(1, atrunc + 1):
        P[pow(inv2, a, 3)] = P.get(pow(inv2, a, 3), 0.0) + 2.0 ** -a
    for lev in range(1, n):
        mod3 = 3 ** (lev + 1)
        inv2 = pow(2, -1, mod3)
        Q = {}
        for x, p in P.items():
            base = (3 * x + 1) % mod3
            for a in range(1, atrunc + 1):
                w = 2.0 ** -a
                if p * w < 1e-30:
                    break
                y = (base * pow(inv2, a, mod3)) % mod3
                Q[y] = Q.get(y, 0.0) + p * w
        P = Q
        mod = mod3
    tot = sum(P.values())
    assert abs(tot - 1.0) < 1e-9, tot
    M = 3 ** n
    out = {}
    for k in range(2 * 3 ** (n - 1)):
        xi = pow(2, k, M)
        s = 0j
        for x, p in P.items():
            s += p * cmath.exp(-2j * math.pi * (xi * x % M) / M)
        out[k] = s
    return out


def psi_via_dual_recursion(n, atrunc=90):
    """Route 2: the dual-space recursion, eq. (4) of the preprint."""
    M1 = 3
    psi = {}
    for k in range(2 * 3 ** 0):
        xi = pow(2, k, M1)
        s = 0j
        inv2 = pow(2, -1, M1)
        for a in range(1, atrunc + 1):
            x = pow(inv2, a, M1)
            s += 2.0 ** -a * cmath.exp(-2j * math.pi * (xi * x % M1) / M1)
        psi[k] = s
    for lev in range(1, n):
        Mn = 3 ** (lev + 1)
        per_old = 2 * 3 ** (lev - 1)
        new = {}
        for k in range(2 * 3 ** lev):
            s = 0j
            for a in range(1, atrunc + 1):
                w = 2.0 ** -a
                if w < 1e-28:
                    break
                # 2^{k-a} mod 3^{lev+1}, valid for negative exponents too
                e = (k - a) % (2 * 3 ** lev)
                phase = cmath.exp(-2j * math.pi * pow(2, e, Mn) / Mn)
                s += w * phase * psi[(k - a) % per_old]
            new[k] = s
        psi = new
    return psi


def core_G(gaps, l, mod):
    """G = sum_{i=1}^{l} 3^{i-1} 2^{-(a_2+...+a_i)}  (mod 3^l).
    gaps = (a_2,...,a_l), each >= 1."""
    inv2 = pow(2, -1, mod)
    tot, c = 0, 0
    for i in range(1, l + 1):
        if i >= 2:
            c += gaps[i - 2]
        tot = (tot + pow(3, i - 1, mod) * pow(inv2, c, mod)) % mod
    return tot


def R_direct(l, j):
    """R_{l-1,j} mod 3^l, straight from Wirsching's definition as used in
    the project (l-subsets of {0,...,l+j-1}, weight 3^{i-1} by rank)."""
    mod = 3 ** l
    out = set()
    for S in combinations(range(l + j), l):
        s = sorted(S, reverse=True)
        out.add(sum(pow(2, a, mod) * pow(3, i, mod) for i, a in enumerate(s)) % mod)
    return out


def R_via_core(l, j):
    """Same set rebuilt as { 2^{s_l+B} * G(gaps) }, the form that makes the
    identity with Tao's Syrac explicit."""
    mod = 3 ** l
    N = l + j
    out = set()

    def rec(gaps, B):
        if len(gaps) == l - 1:
            G = core_G(tuple(gaps), l, mod)
            for u in range(B, N):
                out.add(pow(2, u, mod) * G % mod)
            return
        for a in range(1, N):
            if B + a <= N - 1:
                rec(gaps + [a], B + a)
    rec([], 0)
    return out


def layer_decomposition(n, k, atrunc=60):
    """(C) psi_n(2^k) rebuilt as sum over (B,u) of w_{B,u} * L_{B,u}/|T_B|,
    with w summing to 1.  Returns (rebuilt value, total weight, list of
    (B, weight_B, max_u normalized |L|))."""
    mod = 3 ** n
    xi = pow(2, k, mod)
    inv2 = pow(2, -1, mod)
    # enumerate gap tuples (a_2..a_n) grouped by total B
    layers = {}

    def rec(gaps, B):
        if len(gaps) == n - 1:
            layers.setdefault(B, []).append(tuple(gaps))
            return
        if B > atrunc:
            return
        for a in range(1, atrunc + 1):
            if B + a <= atrunc:
                rec(gaps + [a], B + a)
    rec([], 0)

    total, wsum = 0j, 0.0
    per_layer = []
    for B, tuples in sorted(layers.items()):
        assert len(tuples) == math.comb(B - 1, n - 2) if n >= 2 else True
        best = 0.0
        Lsum = 0j
        for a1 in range(1, atrunc + 1):
            w_u = 2.0 ** -a1
            L = 0j
            for g in tuples:
                G = core_G(g, n, mod)
                val = G * pow(inv2, a1, mod) % mod
                L += cmath.exp(-2j * math.pi * (xi * val % mod) / mod)
            best = max(best, abs(L) / len(tuples))
            Lsum += w_u * L
        w_B = 2.0 ** -B
        total += w_B * Lsum
        wsum += w_B * len(tuples)
        per_layer.append((B, w_B * len(tuples), best))
    return total, wsum, per_layer


if __name__ == "__main__":
    print("=" * 78)
    print("(A) Independent reproduction of Toguchi Table 1  (M_n, k*(n))")
    print("=" * 78)
    print(f"{'n':>2} {'M_n (route1)':>14} {'M_n (route2)':>14} {'M_n paper':>12}"
          f" {'k* r1':>6} {'k* r2':>6} {'k* paper':>8}  ok")
    for n in range(1, 10):
        p1 = psi_via_distribution(n)
        p2 = psi_via_dual_recursion(n)
        half = 3 ** (n - 1)
        m1 = max(range(half), key=lambda k: abs(p1[k]))
        m2 = max(range(half), key=lambda k: abs(p2[k]))
        M1, M2 = abs(p1[m1]), abs(p2[m2])
        Mp, kp = TOGUCHI[n]
        ok = (abs(M1 - Mp) / Mp < 2e-5) and (abs(M2 - Mp) / Mp < 2e-5) \
             and m1 == kp and m2 == kp
        print(f"{n:>2} {M1:>14.7e} {M2:>14.7e} {Mp:>12.5e}"
              f" {m1:>6} {m2:>6} {kp:>8}  {'YES' if ok else '*** NO ***'}")

    print()
    print("=" * 78)
    print("(B) Object identity: R_{l-1,j} mod 3^l  ==  { 2^{s_l+B} * G(gaps) }")
    print("=" * 78)
    for (l, j) in [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3), (4, 5)]:
        A, Bs = R_direct(l, j), R_via_core(l, j)
        print(f"  l={l} j={j}: |R_direct|={len(A):>4} |R_via_core|={len(Bs):>4}"
              f"  identical={A == Bs}")
    print(f"  ground-truth checkpoint l=2,j=2 -> {sorted(R_direct(2, 2))}"
          f"   (project README expects [1, 2, 5, 7])")

    print()
    print("=" * 78)
    print("(C) psi_n as an exact convex combination of normalized layer sums")
    print("=" * 78)
    for n in (3, 4, 5):
        p2 = psi_via_dual_recursion(n)
        k = max(range(3 ** (n - 1)), key=lambda kk: abs(p2[kk]))
        rebuilt, wsum, per = layer_decomposition(n, k)
        print(f"  n={n} k*={k}: psi={abs(p2[k]):.10f}  rebuilt={abs(rebuilt):.10f}"
              f"  total weight={wsum:.10f}  match={abs(abs(rebuilt)-abs(p2[k]))<1e-8}")
        top = sorted(per, key=lambda t: -t[1])[:4]
        print("     dominant layers (B, weight, max_u |L_{B,u}|/|T_B|): "
              + ", ".join(f"({B}, {w:.4f}, {m:.4f})" for B, w, m in top))
        print(f"     degenerate layer B={n-1}: weight={2.0**-(n-1):.5f}"
              f" (exponentially small, so it cannot carry a polynomially large psi)")

    print()
    print("=" * 78)
    print("(D) What the measured extremal coefficient means for the Fourier route")
    print("=" * 78)
    print(f"{'n':>3} {'M_n measured':>14} {'sqrt-canc ~2^-n':>16} {'ratio':>10}"
          f" {'need 3^-n':>12} {'ratio':>12}")
    ALL = dict(TOGUCHI)
    ALL.update({10: (3.82783e-2, 12), 15: (1.62845e-2, 18), 21: (7.87213e-3, 28)})
    for n in sorted(ALL):
        M = ALL[n][0]
        sq, need = 2.0 ** -n, 3.0 ** -n
        print(f"{n:>3} {M:>14.5e} {sq:>16.3e} {M/sq:>10.1f} {need:>12.3e} {M/need:>12.3e}")
    print()
    print("  L^1 Fourier covering criterion needs sum_{xi!=0}|S(xi)| < T, i.e. the")
    print("  NORMALIZED extremal coefficient below ~3^-l. Even perfect square-root")
    print("  cancellation (|S|~sqrt(T)) only gives T >~ 3^{2l}, i.e.")
    print(f"    j >= 2*log_4(3)*l = {2*math.log(3)/math.log(4):.7f} * l")
    print("  versus the already-proven elementary MPG bound j*(l) <= (5/3) l =")
    print(f"    {5/3:.7f} * l   (round 21), and the conjectured truth log_4(3)*l =")
    print(f"    {math.log(3)/math.log(4):.7f} * l")
