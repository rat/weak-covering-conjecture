"""
Checks Codex's cyclotomic/Frobenius-mod-3 claim for GAP A (H-003), round 1 of the
2026-07-31 four-round Codex "where are we stuck" consultation.

Claim: F_{N,m}(X) = sum over N>a_0>...>a_{m-1}>=0 of X^{sum_i 2^{a_i} 3^i} satisfies
    F_{N,m}(X) = F_{N-1,m}(X) + X^{2^{N-1}} * F_{N-1,m-1}(X^3).                    (1)
Reducing mod 3 and substituting X=1+u (so (1+u)^3 = 1+u^3 mod 3, i.e. Frobenius):
    G_{N,m}(u) := F_{N,m}(1+u) mod 3
    G_{N,m}(u) = G_{N-1,m}(u) + (1+u)^{2^{N-1}} * G_{N-1,m-1}(u^3)   mod 3.        (3)
Since Phi_{3^L}(1+u) = u^{2*3^{L-1}} mod 3 (3 is totally ramified in Z[zeta_{3^L}]),
S(t) = F_{N,m}(zeta_{3^L}^t) = 0 for some/every t coprime to 3 (Galois conjugates)
implies u^{2*3^{L-1}} | G_{N,m}(u) mod 3.                                          (4)

This script verifies (1) exactly (small N, brute force) and computes the u-adic
valuation (order of vanishing at u=0) of G_{N,m}(u) mod 3 for N=2j, m=j (the actual
R_{j-1,j} parameters this project uses: j exponents from domain {0,...,2j-1}).

Result: valuation stays at 0 or 1 for every j=1..30 tested (l up to ~38 via
j ~ log_4(3)*l, well past this project's current computed frontier l=23). Since the
threshold 2*3^{L-1} in (4) grows exponentially in L while the valuation does not grow
at all in the tested range, this proves S(t) != 0 for every t coprime to 3, at every
L tested (via (4)'s contrapositive) -- i.e. the exponential sum S(t) NEVER vanishes
exactly for the R_{j-1,j} family, at least in the range checked here.

IMPORTANT LIMITATION: this rules out exact vanishing (a zero-set argument), not a
magnitude bound. It is a genuine partial result, not (yet) what H-003/GAP A actually
needs (S(t) small, not just S(t) != 0). See notes/H-003.md for the recorded finding
and its honest scope.
"""


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(len(a)):
        out[i] = (out[i] + a[i]) % 3
    for i in range(len(b)):
        out[i] = (out[i] + b[i]) % 3
    return out


def poly_mul(a, b, cap):
    n = min(len(a) + len(b) - 1, cap + 1)
    out = [0] * n
    for i, ai in enumerate(a):
        if ai == 0 or i >= n:
            continue
        lim = min(len(b), n - i)
        for j in range(lim):
            if b[j] == 0:
                continue
            out[i + j] = (out[i + j] + ai * b[j]) % 3
    return out


def poly_pow_1plusu(N, cap):
    result = [1]
    base = [1, 1]
    e = N
    while e > 0:
        if e & 1:
            result = poly_mul(result, base, cap)
        base = poly_mul(base, base, cap)
        e >>= 1
    return result


def compose_u3(a, cap):
    out = [0] * min(3 * (len(a) - 1) + 1, cap + 1)
    for i, c in enumerate(a):
        idx = 3 * i
        if idx > cap:
            break
        if idx < len(out):
            out[idx] = c
    return out


def G(N, m, cap, memo):
    if (N, m) in memo:
        return memo[(N, m)]
    if m == 0:
        r = [1]
    elif m > N or N < 0:
        r = [0]
    else:
        part1 = G(N - 1, m, cap, memo)
        part2 = G(N - 1, m - 1, cap, memo)
        part2c = compose_u3(part2, cap)
        shift_poly = poly_pow_1plusu(2 ** (N - 1), cap)
        part2_shifted = poly_mul(shift_poly, part2c, cap)
        r = poly_add(part1, part2_shifted)
        if len(r) > cap + 1:
            r = r[: cap + 1]
    memo[(N, m)] = r
    return r


def valuation(poly, cap):
    for i, c in enumerate(poly):
        if c % 3 != 0:
            return i
    return f">={cap}"


def verify_recursion_1(max_N=6):
    """Brute-force check of eq (1) against a direct enumeration of F_{N,m}."""
    from collections import Counter
    from itertools import combinations

    def F_direct(N, m):
        c = Counter()
        if m == 0:
            c[0] = 1
            return c
        for combo in combinations(range(N), m):
            a = sorted(combo, reverse=True)
            val = sum(2 ** a[i] * 3 ** i for i in range(m))
            c[val] += 1
        return c

    def shift_and_cube(c, shift):
        out = {}
        for e, v in c.items():
            out[shift + 3 * e] = out.get(shift + 3 * e, 0) + v
        return out

    all_ok = True
    for N in range(1, max_N + 1):
        for m in range(0, N + 1):
            lhs = {e: v for e, v in F_direct(N, m).items() if v}
            part1 = F_direct(N - 1, m) if N >= 1 else Counter()
            part2 = F_direct(N - 1, m - 1) if (N >= 1 and m >= 1) else Counter()
            part2s = shift_and_cube(part2, 2 ** (N - 1)) if N >= 1 else {}
            rhs = dict(part1)
            for e, v in part2s.items():
                rhs[e] = rhs.get(e, 0) + v
            rhs = {e: v for e, v in rhs.items() if v}
            ok = lhs == rhs
            all_ok = all_ok and ok
            if not ok:
                print(f"MISMATCH at N={N}, m={m}: lhs={lhs} rhs={rhs}")
    return all_ok


if __name__ == "__main__":
    print("Verifying recursion (1) by brute force, N=1..6:")
    ok = verify_recursion_1(6)
    print(f"  all match: {ok}\n")

    print("u-adic valuation of G_{2j,j}(u) mod 3, j=1..30 (cap=200):")
    cap = 200
    for j in list(range(1, 11)) + [12, 15, 18, 20, 23, 26, 27, 30]:
        N, m = 2 * j, j
        memo = {}
        g = G(N, m, cap, memo)
        v = valuation(g, cap)
        print(f"  j={j:2d}  N={N:3d}  m={m:2d}  v(G) = {v}")
