"""
Tests Gemini's round-25 item 6 ("Microcanonical Budget Transfer Operator without Fourier
Characters"): a transfer operator

    (L_z f)(x) = sum_{a=1}^inf z^a f((2^a x - 1)/3) * I[2^a x = 1 mod 3]

parameterized by a fugacity z in (0,1), with no spatial Fourier variable (unlike every closed
transfer-operator attempt in rounds 6/16-18, which all reduced to the character sum S(t)). The
claim: if the spectral gap gamma(z) = 1 - |lambda_2(z)/lambda_1(z)| stays bounded away from 0 as
z -> 1/2 (the fugacity value matching this project's budget rate alpha=log_4(3), since
z=2^{-1/log_4(3)}... actually the natural weight matching a linear budget of rate alpha is
z=2^{-1}, one unit of budget per digit at rate log_2, but the literal operator as written uses
z=1/2 as the point of interest per the item's own text), that gives a CLT for the budget
distribution, hence e(l)=Theta(sqrt(l)). If gamma(z) -> 0, the degeneracy rate would separate
linear from logarithmic backlog.

Approach: truncate x to the low n 3-adic digits (x in [0, 3^n)), a from 1 to A_MAX (z^a negligible
for z<=0.5, A_MAX=48 gives z^48<=3.6e-15). For each x, compute 2^a*x-1 EXACTLY (Python big ints,
no modular wraparound during the check itself) and, when divisible by 3, take y = ((2^a*x-1)//3)
truncated (mod 3^n) as the target state -- the same "fixed digit window" approximation this
project's own game/DP machinery already uses, so this is the fairest finite-rank truncation
available without new theory. Build the resulting sparse-ish n x n matrix M(z) explicitly and
compute its two dominant eigenvalues (numpy, dense since 3^n stays small: n<=8 gives 6561 states)
for a grid of z approaching 1/2.

Result (n=6,7,8, z=0.40,0.45,0.49; n=8's eigvals take ~125s each on this machine, dense LAPACK on
a 6561x6561 matrix, so its z-grid was narrowed to keep runtime bounded):

    z      n=6      n=7      n=8
    0.40   0.0294   0.0220   0.0237
    0.45   0.0432   0.0310   0.0342
    0.49   0.0563   0.0429   0.0468

The gap drops substantially (22-28%) from n=6 to n=7 at every z tested, which would be consistent
with a vanishing gap as truncation size grows (the degenerate branch of item 6's own dichotomy).
But it then PARTIALLY RECOVERS (7-10%) from n=7 to n=8 at every z, not continuing to shrink. Three
points with non-monotonic behavior cannot distinguish "slowly decaying with a finite-size
correction" from "stabilizing at a positive limit" (a real spectral gap surviving truncation,
supporting the CLT branch instead). n=9 (19683 states) would cost roughly 27x longer per eigenvalue
call (~an hour each) under this dense approach, past what a bounded first look should spend without
the researcher's explicit go-ahead. **Recorded honestly as genuinely inconclusive**, not closed
either direction; unlike most of this round's items, this one did not collapse cleanly on contact,
nor did it come out to a confirmed direction.
"""
import numpy as np

A_MAX = 48


def build_matrix(n, z):
    mod = 3 ** n
    M = np.zeros((mod, mod), dtype=np.float64)
    weights = [z ** a for a in range(1, A_MAX + 1)]
    for x in range(mod):
        for a in range(1, A_MAX + 1):
            val = (2 ** a) * x - 1
            if val % 3 != 0:
                continue
            y = (val // 3) % mod
            M[y, x] += weights[a - 1]
    return M


def top_eigs(M, k=4):
    ev = np.linalg.eigvals(M)
    ev = ev[np.argsort(-np.abs(ev))]
    return ev[:k]


if __name__ == "__main__":
    import sys
    for n in [6, 7]:
        print(f"=== n={n} (mod 3^{n}={3**n}) ===", flush=True)
        for z in [0.30, 0.40, 0.45, 0.48, 0.49, 0.499, 0.4999]:
            M = build_matrix(n, z)
            ev = top_eigs(M)
            lam1, lam2 = ev[0], ev[1]
            gap = 1 - abs(lam2) / abs(lam1) if abs(lam1) > 1e-12 else float('nan')
            print(f"  z={z:.4f}  lambda1={lam1:.6f}  lambda2={lam2:.6f}  "
                  f"|lam2/lam1|={abs(lam2)/abs(lam1):.6f}  gap={gap:.6f}", flush=True)
        print(flush=True)
