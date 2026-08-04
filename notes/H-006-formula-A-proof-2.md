# Formula (A): a second, independent uniform saddlepoint proof (sharper, effective constants)

This note is a second, independently-produced written proof of formula (A), built without reading
`H-006-formula-A-proof.md` (the first proof) first (both were produced in parallel with no
knowledge of each other, then cross-checked; see the "Independent cross-validation" section at the
end of this file). It uses the same core mechanism as the first proof (central/tail split of the
tilted Fourier inversion integral, bounded via off-real-axis derivative-normalized cumulant
functions), but with tighter constants that make the stated threshold actually effective, not just
formally valid: the error bound in this file is already below 1 at `N=17` and below `0.03` by
`N=1000`, unlike the first proof's threshold (`N>=2000`), whose own bound does not drop below 1
until `N` is around 387,930 (both are correct proofs; only the practical strength of the constants
differs). Recording both is worth more than picking one: independent agreement on the underlying
mechanism, with substantially different constants, is stronger evidence than either proof alone.

## 0. Setup and statement

`U_1,U_2,...` iid uniform on `[0,1]`, `X = sum_{j>=1} (2/3^j) U_j` in `[0,1]`, `phi` its density
(Rvachev `h_3` / Wirsching's Elka function up to translation). For `s>0`,

```
K(s) = log E[e^{-sX}] = sum_{j>=1} g(2s/3^j),   g(b) = log((1-e^{-b})/b),
t(s) = -K'(s),   phi_saddle(t(s)) = exp(K(s)+s t(s))/sqrt(2 pi K''(s)).
```

**Theorem.** Write `N = floor(log_3(2s))`, `rho = 2s/3^N in [1,3)`. For every `s` with `N >= 17`
(i.e. `s >= 3^17/2 = 64570081.5`),

```
| phi(t(s))/phi_saddle(t(s)) - 1 | <= E(N),
```

with `E` explicit (Section 6 below), strictly decreasing on `[17,infinity)`, `E(17) = 0.9901`,
`E(N) <= 4.1 N^{-1/2}` for all `N >= 17`, and `E(N) ~ 0.742358 N^{-1/2}`. Every constant is free of
`rho`, so the threshold is `rho`-free and (A) holds uniformly in the phase. Since `t(s)` decreases
strictly from `1/2` to `0` (proven in `H-006-envelope.md`, Section 3), this is
`phi(t) = phi_saddle(t)(1+o(1))` as `t -> 0+`, with rate `O((log(1/t))^{-1/2})`.

## 1. Notation

On `H = {Re w > 0}`, `(1-e^{-w})/w` is analytic and non-vanishing (its zeros `w in 2 pi i Z` all lie
off `H`; `w=0` is removable with value 1), and `H` is simply connected, so a unique analytic `g` with
`exp g = (1-e^{-w})/w`, real on `(0,infinity)`, exists. Set

```
kappa_n(w) = (-1)^n w^n g^{(n)}(w).                                    (1)
```

`kappa_n(b)` is `b^n` times the `n`-th cumulant of `V` with density `b e^{-bv}/(1-e^{-b})` on
`[0,1]`. With `x = w/2`,

```
kappa_1 = 1 - w/(e^w-1),  kappa_2 = 1 - x^2/sinh^2 x,
kappa_3 = 2 - 2x^3 cosh x/sinh^3 x,  kappa_4 = 6 + 2x^4(1-3coth^2 x)/sinh^2 x.   (2)
```

(Checked against numerical differentiation of `g` to 40 digits at real and complex points.) From
`g(w)+w/2 = sum_{k>=1} B_{2k} w^{2k}/(2k(2k)!)` on `|w|<2 pi`,

```
kappa_n(w) = (-1)^n sum_{k>=ceil(n/2)} B_{2k} w^{2k}/(2k(2k-n)!),   n>=2.        (3)
```

So `kappa_2 = w^2/12+O(w^4)`, `kappa_3 = w^4/120+O(w^6)`, `kappa_4 = -w^4/120+O(w^6)`, and
`kappa_n(w)=O(w^2)` for `n>=2`. With `s = rho 3^N/2` and `b_j = 2s/3^j`,

```
{b_j : j>=1} = {rho 3^m : m <= N-1},    b_j >= 1  <=>  m = N-j >= 0.             (4)
```

Exactly `N` of the `b_j` are `>= 1`, the smallest being `rho`; the rest are geometric below 1. This
is the single structural fact making every constant `rho`-free. Put `V_n = sum_j kappa_n(b_j) = s^n
(n`-th cumulant of `X_s)`; `V_2 = s^2 K''(s)`.

## 2. Lemma 1 (boundedness off the real axis)

**Lemma 1.** For `w = b(1+iu)`, `b>0`, `|u| <= a <= 1`, with `e(r)=r^2/sinh^2 r`,
`f(r)=r^3 cosh r/sinh^3 r`:

```
|kappa_2(w)| <= 1 + (1+a^2) e(b/2),   |kappa_3(w)| <= 2 + 2(1+a^2)^{3/2} f(b/2).  (6)
```

`e` and `f` are strictly decreasing with `e(0+)=f(0+)=1`, so `M_2 <= 3` and `M_3 <= 2+2^{5/2} =
7.657` over the whole sector `|Im w| <= Re w`; in particular both are finite.

*Proof.* `|sinh z|^2 = sinh^2(Re z)+sin^2(Im z) >= sinh^2(Re z)` and
`|cosh z|^2 = sinh^2(Re z)+cos^2(Im z) <= cosh^2(Re z)`. The first is the analytic content:
`w/2` never approaches a pole `pi i k` of `csch`, because `Re(w/2)=b/2>0`. With
`|w/2|^2 = (b/2)^2(1+u^2)`, (2) gives (6). `e` decreases since `sinh r/r = sum r^{2k}/(2k+1)!`
increases. For `f`: `f'/f = 3/r + tanh r - 3 coth r`, so `f' < 0` is equivalent to
`3(coth r - 1/r) > tanh r`. Three regions. (i) `0<r<sqrt2`: both `coth r - 1/r = r/3 - r^3/45 + ...`
and `tanh r = r - r^3/3 + 2r^5/15 - ...` are alternating with decreasing terms on `0<r<pi/2`, so
`3(coth r-1/r) >= r - r^3/15` and `tanh r <= r - r^3/3 + 2r^5/15`; the difference is
`(4/15)r^3 - (2/15)r^5 > 0` exactly when `r^2<2`. (ii) `sqrt2 <= r <= 2`:
`(d/dr)(coth r - 1/r) = 1/r^2 - csch^2 r > 0` since `sinh r > r`, so the left side is at least its
value `1.2526` at `r=1.41`, while the right side is at most `tanh 2 = 0.9640`. (iii) `r>=2`:
`coth r > 1` gives left side `> 1.5 > 1 > tanh r`. Hence `f` decreases and `f<1`, which is
Lazarevic's inequality `(sinh r/r)^3 > cosh r`. Taking `a=1` gives the two sups. QED

*Numerical remark (not used in the proof, corrects a value recorded elsewhere in the project).* The
true sups over `|u|<=1`, all attained at `u=1`, are `M_2 = 1.4752976` (b=4.0761),
`M_3 = 4.2843291` (b=4.7914), `M_4 = 19.967293` (b=5.4054). The value `M_4 = 19.959` recorded
earlier in `notes/H-006.md` is wrong; the correct value is `19.96729`.

**Lemma 1'.** For `|w| <= 2`: `|kappa_2(w)| <= 0.114|w|^2` and `|kappa_3(w)| <= 0.0119|w|^4`.

*Proof.* `kappa_2/w^2` and `kappa_3/w^4` are analytic on `|w|<2pi` by (3), so it suffices to bound
them on `|w|=2` (maximum principle). Using the exact `|B_{2k}| = 2(2k)! zeta(2k)/(2pi)^{2k}`,
`zeta(2k)<=zeta(2)` for `k>=1` and `<=zeta(4)` for `k>=2`, and `u = |w|^2/(4pi^2)`:

```
|kappa_2| <= 2 zeta(2)[2u/(1-u)^2 - u/(1-u)],
|kappa_3| <= 2 zeta(4)[4u(1+u)/(1-u)^3 - 6u/(1-u)^2 + 2u/(1-u)].
```

At `|w|=2`, `u = 1/pi^2 = 0.1013212`, these equal `0.4545522` and `0.1899113`; dividing by `4` and
`16` gives `0.1136381` and `0.0118695`. QED

## 3. Lemma 2 (variance)

**Lemma 2.** For all `rho in [1,3)`, `N>=1`:

```
N - A <= V_2 <= N + 0.1283,     A := sum_{m>=0} e(3^m/2) = 1.4269413069.          (9)
```

*Proof.* `kappa_2(b) = 1 - e(b/2) in (0,1)`. Dropping the positive `m<0` terms,
`V_2 >= N - sum_{m>=0} e(rho 3^m/2)`, largest at `rho=1` since `e` decreases; that is `N-A`. Upper:
the `N` terms with `m>=0` are `<1`, and for `m<=-1`, `rho 3^m < 1 < 2` so Lemma 1' gives
`sum_{m>=1} 0.114 (rho 3^{-m})^2 = 0.114 rho^2/8 <= 0.1283`. QED

*Remark (corrected remainder).* Exactly, `V_2 = N + C_V(rho) - sum_{m>=N} e(rho 3^m/2)` with the
exact identity `e(b/2) = b^2 e^{-b}/(1-e^{-b})^2`. The remainder is `O((rho 3^N)^2 e^{-rho 3^N}) =
O((2s)^2 e^{-2s})`, **not** `O(e^{-rho 3^N})` as stated in an earlier round's write-up. Numerically
`C_V(1) = -1.4165764974`, matching the recorded value, and `V_2 - N` is constant in `N` to 40 digits
by `N=5`.

## 4. Lemma 3 (tail) and existence of `phi`

**Lemma 3a.** If `b_0 >= 1` and `b_k = 3^k b_0`, then `sum_{k>=0} log coth(b_k/2) <= 2.627 e^{-b_0}
<= 3 e^{-b_0}`.

*Proof.* `log coth(x/2) = 2 artanh(e^{-x}) <= 2e^{-x}/(1-e^{-2x})`. With `q = e^{-b_0} <= e^{-1}`,
the sum is at most `(2/(1-q^2)) sum_k q^{3^k} <= (2/(1-q^2)) q(1+q^2+q^8+q^{26}+...) <= 2.31298 *
1.13565 q = 2.62675 q`. QED

The hypothesis `b_0 >= 1` is used here for a clean numerical constant; it is **sufficient**, not
necessary in the strictest sense (the same-shaped bound, with a different constant, still holds
down to `b_0=0.7`, and fails by `b_0=0.3`), and in this proof `b_0=rho>=1` always, so sufficiency is
all that's needed.

**Lemma 3b.** With `Lambda(y) := K(s(1+iy)) - K(s) + i s y t(s) = sum_j lambda_j(y)`,
`lambda_j(y) := g(b_j(1+iy)) - g(b_j) + iy kappa_1(b_j)`, for all real `y`:

```
|exp(Lambda(y))| <= exp(3 e^{-rho}) (1+y^2)^{-N/2} <= 3.0152 (1+y^2)^{-N/2}.     (12)
```

*Proof.* `K(s(1+iy)) = sum_j g(b_j(1+iy))` since `s` enters each factor multiplicatively (the series
converges locally uniformly because `g(w) = -w/2+O(w^2)`). And `t(s) = -(1/s) sum_j b_j g'(b_j) =
V_1/s`, so `i s y t(s) = iy V_1`, exactly cancelling the first-order terms. Since `kappa_1(b_j)` is
real, `|exp(lambda_j(y))| = |1-e^{-b_j}e^{-i b_j y}|/((1-e^{-b_j})sqrt(1+y^2)) =: m_j(y)`, which is
the modulus of a characteristic function, hence `<= 1`. For the `N` indices with `b_j >= 1`, use
`|1-e^{-b}e^{-i th}| <= 1+e^{-b}` and `(1+e^{-b})/(1-e^{-b}) = coth(b/2)` to get
`m_j(y) <= coth(b_j/2)/sqrt(1+y^2)`. By (4) those `b_j` are `rho, 3rho, ..., 3^{N-1}rho`, geometric
of ratio 3 starting at `b_0 = rho >= 1`, so Lemma 3a applies. QED

**Proposition 4 (existence and inversion).** `X` has a continuous density: the first two summands
convolve to a continuous compactly supported density, and convolution preserves continuity. For
`N>=3`, the tilted law `P_s(dx) = e^{-sx}P(dx)/e^{K(s)}` has characteristic function
`exp(K(s-iv)-K(s))` of modulus `<= 3.0152(1+v^2/s^2)^{-N/2}`, integrable, so Fourier inversion is
valid; `P` and `P_s` are mutually absolutely continuous with density `e^{K(s)+sx}`, and at
`x = t(s) = E[X_s]`,

```
R(s) := phi(t(s))/phi_saddle(t(s)) = sqrt(V_2/(2 pi)) integral_R exp(Lambda(y)) dy.  (15)
```

`R(s)` is real since `Lambda(-y) = conj(Lambda(y))`. The theorem is `R(s) -> 1`.

## 5. Lemma 4 (Taylor, integral remainder)

With `h(u) = g(b(1+iu))`, `lambda_j(y) = h(y)-h(0)-y h'(0)`. `h` is a complex-valued function of a
real variable, so Taylor's theorem is used in **integral** form,

```
h(y) = h(0)+h'(0)y+h''(0)y^2/2 + (1/2) integral_0^y (y-u)^2 h'''(u) du.           (16)
```

The **Lagrange form is invalid here** (it fails already for `u -> e^{iu}` on `[0,2pi]`). Since
`h''(0) = -kappa_2(b)` and `h'''(u) = (ib)^3 g'''(b(1+iu))`, i.e. `|h'''(u)| = |kappa_3(w)|/(1+u^2)^
{3/2}` with `w=b(1+iu)`,

```
|lambda_j(y) + kappa_2(b_j)y^2/2| <= (|y|^3/6) sup_{|u|<=|y|}|h_j'''(u)|.         (17)
```

**Lemma 4.** For `a in (0,1]`, `rho in [1,3)`, `N>=1`:

```
S := sum_j sup_{|u|<=a} |h_j'''(u)| <= 2N + 2F + 0.0171 = 2N + 3.7442,
F := sum_{m>=0} f(3^m/2) = 1.8635631489.                                          (19)
```

*Proof.* By (18) and Lemma 1, `|h_j'''(u)| <= [2 + 2(1+u^2)^{3/2}f(b_j/2)]/(1+u^2)^{3/2} <= 2 +
2f(b_j/2)`. Summing over the `N` indices with `b_j>=1` gives `2N + 2 sum_{m=0}^{N-1} f(rho 3^m/2)
<= 2N+2F` (`f` decreasing, `rho>=1`). For the rest, `b_j<1` so `|w| <= sqrt2 < 2` and Lemma 1'
gives `|h_j'''| <= 0.0119 sqrt2 b_j^4`, summing to `0.0119 sqrt2 (81/80) = 0.01704`. QED

Hence, summing (17),

```
|Lambda(y) + V_2 y^2/2| <= B|y|^3,  B := S/6 <= (2N+3.7442)/6,  |y| <= a.         (20)
```

## 6. Proof of the theorem

Take `a = a_N = N^{-1/3}` (the endpoint `alpha=1/3` is admissible and optimal here; see Remark 7.5).
Split `R(s) = C + T` at `|y| = a`.

**Central.** With `E(y) := Lambda(y)+V_2y^2/2`, `|E(y)| <= B a^3 =: eps = 1/3 + 0.6240/N <= 0.3701`
for `N>=17`. Using `|e^z-1| <= |z|e^{|z|}` and `integral_R e^{-V y^2/2}|y|^3 dy = 4/V^2`,

```
|C - sqrt(V_2/2pi) integral_{|y|<=a} e^{-V_2 y^2/2} dy| <= 4 e^{eps} B/(sqrt(2pi) V_2^{3/2}) =: e_1.  (23)
```

The remaining Gaussian piece is exact: it equals `1 - (2/sqrt(2pi)) integral_c^inf e^{-v^2/2}dv`
with `c = a sqrt(V_2)`, and `integral_c^inf e^{-v^2/2}dv <= e^{-c^2/2}/c`, so `|C-1| <= e_1 + e_2`,
`e_2 := (2/sqrt(2pi))e^{-c^2/2}/c`.

**Tail.** By Lemma 3b and `integral_a^inf (1+y^2)^{-N/2}dy <= (1/a) integral_a^inf y(1+y^2)^{-N/2}dy
= (1+a^2)^{-(N-2)/2}/(a(N-2))`,

```
|T| <= 2 * 3.0152 * sqrt(V_2/(2pi)) (1+a^2)^{-(N-2)/2}/(a(N-2)) =: e_3,           (26)
```

where the *upper* bound `V_2 <= N+0.1283` is the one used. `e_3` decays like
`N^{-1/6}exp(-N^{1/3}/2)`, which needs `a >> N^{-1/2}`, i.e. the exponent `1/3 < 1/2`.

**Assembly.** `|R(s)-1| <= e_1+e_2+e_3 =: E(N)`, explicitly with `V_lo = N-1.4270`,
`V_up = N+0.1283`, `B = (2N+3.7442)/6`, `eps = B/N`, `c = a sqrt(V_lo)`:

```
   N        E(N)       e_1       e_2       e_3
  17     0.99005   0.23649   0.16011   0.59345
  20     0.86951   0.20928   0.14250   0.51773
  30     0.63252   0.15817   0.10561   0.36874
 100     0.23906   0.07776   0.03786   0.12344
1000     0.03062   0.02358   0.00171   0.00532
10^4     0.00744   0.00743   0.00000   0.00000
```

`E` is strictly decreasing for `N>=17`, `sup_{N>=17} sqrt(N)E(N) = 4.0821`, and
`sqrt(N)E(N) -> 4e^{1/3}/(3 sqrt(2pi)) = 0.742358`. Every constant (`A`, `F`, the two Bernoulli
ceilings, `e^{3/e}`) is a supremum over `b>0` or a sum over one full 3-adic orbit, hence `rho`-free
by construction. QED

## 7. Remarks

**7.1 True rate.** (23) discards the parity of the cubic term (`integral_R e^{-V_2y^2/2} i y^3
V_3/6 dy = 0`). Carrying (16) to fourth order gives the Edgeworth form
`R = 1 + V_4/(8V_2^2) - 5V_3^2/(24V_2^3) + O(N^{-3/2})`; since `V_3 = 2N+O(1)` and `V_4 = 6N+O(1)`
by the argument of Lemma 2, this is `R = 1 - 1/(12N) + O(N^{-3/2})`, independently reproducing the
`-1/12` measured in earlier rounds. This is checked numerically but the fourth-order remainder is
not written out here, so it is a remark, not part of the theorem. Formula (A) needs only `o(1)`.

**7.2 Why uniformity is structural.** For `b>>1` the tilted `V_j -> Exp(1)` with cumulants
`(n-1)!`; exactly `N` of the `b_j` are `>=1`. So `X_s` is asymptotically `Gamma(N,1)`, whose exact
saddlepoint-at-the-mean ratio is the Stirling correction `1 - 1/(12N)+O(N^{-2})`. `rho` shifts only
`O(1)` cumulant corrections, hence enters at order `N^{-2}`.

**7.5 `alpha=1/3` is admissible.** The exponent need only satisfy `1/3 <= alpha < 1/2`; the
endpoint works because `eps = B a^3` need not tend to 0, only stay bounded, since it enters solely
through `e^{eps}`. That choice minimises the tail terms and is what makes `N_0 = 17` rather than
astronomically large.

**7.6 Numerical verification.** `R(s)` computed from the defining product via (15) by numerical
quadrature. `N(R-1)` converges to `-1/12` at every phase tested (`rho=1.0,1.5,2.0,2.9`),
reproducing recorded values exactly (`-0.0530, -0.0664, -0.0705` at `N=7,10,12`). Each inequality
checked directly over thousands of grid points (worst-case ratios all strictly below 1).

**7.7 Corrections to values recorded elsewhere in the project.** `sum_j sup|kappa_4| <= 6N` is
false (`6.7653 N` at `rho=2,N=10`); irrelevant, only `O(N)` is needed. The `V` remainder is
`O((rho 3^N)^2 e^{-rho 3^N})`. The coth bound needs `b_0>=1`. `kappa_n(b)=O(b^4)` for all `n` is
false at `n=1,2`; `O(b^2)` for `n>=2` is correct and sufficient. `M_4 = 19.96729`, not `19.959`.

## Independent cross-validation, 2026-08-04

This proof and `H-006-formula-A-proof.md` were produced independently (no knowledge of each other)
and cross-checked, then both reviewed together by a fresh-context adversarial critic. The critic
found: no mathematical gap in either; one real, non-load-bearing defect in the first proof's Lemma
1 (a Cauchy-estimate constant, since fixed there); confirmed this proof's substantially tighter,
practically effective threshold (`N>=17`, error `<=4.1/sqrt(N)`, versus the first proof's `N>=2000`,
whose own bound does not fall below 1 until `N` is around 387,930); and reproduced all reported
numerics independently (its own scripts, not reused from either proof).

**Honest calibration, per the critic's own explicit note, worth preserving rather than smoothing
over**: having two write-ups overstates their independence. Both use the same core mechanism
(same `kappa_n` convention, same tilted-inversion identity, same `coth`-tail approach on the same
`rho`-free threshold set, same structural reason for uniformity), differing mainly in constants and
the central/tail cutoff exponent. The confidence this proof (and the companion file) deserve comes
from the critic's own from-scratch, independent re-derivation of every lemma and every numerical
constant, not merely from two agents agreeing. Per this project's Rule 8/11b, the mandatory
pre-publication check for a result this load-bearing should still go to a genuinely independent
reviewer (a different model vendor, or the researcher), since every review so far, including this
cross-check, shares one model family's blind spots.
