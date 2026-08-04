# H-006: envelope/stationarity lemma

**Status, stated precisely (per the 2026-08-04 adversarial critique of this file): this lemma
itself is a closed, verified derivation. But it is not by itself an unconditional result, and
nothing below should be read as one.** It rests on two different kinds of prior input, at two
different levels of rigor, and conflating them is exactly the mistake an earlier draft of this
file made:

- Fully PROVEN and rigorous: the exact recurrence/product for `K`, the `Q+H` decomposition, the
  Fourier formula for `H` and its certified `H'`/`H''` bounds, and the exact `P`--Berg--Kruppel
  comparison. This lemma's own derivation (sections 1-4 below) is also fully proven, given those.
- **NOT yet proven, still an unwritten (though three-ways independently verified) proof sketch**:
  formula (A) itself (`phi(t(s))=phi_saddle(t(s))*(1+o(1))` uniformly as `t->0+`). Every
  consequence below that mentions `phi` (as opposed to `phi_saddle`) is conditional on formula (A)
  in this sense. See notes/H-006.md's "Formula (A) uniform in rho: mathematical content CLOSED"
  section for formula (A)'s own status; "closed" there means "referee-checkable correct proof
  sketch, not yet a written proof," not "proven."

Two corrections to the informal formulation are important.  The smooth saddle
is a large *local* minimum, not a global `argmin` on `R`; and
`g(w*)-g(w0)` is negative, not positive.

Put `t=e^{-tau}`, `L(w)=K(e^w)`, and

```
g_tau(w)  = L(w) + exp(w-tau),
g0_tau(w) = Q(w) + exp(w-tau),
B(w)      = w/c-a,             a=1/2-log(2)/c.
```

## 1. Exact differentiable remainder

Let

```
d(w) = log(1-exp(-2*exp(w))).
```

The exact recurrence and the defining quadratic give

```
(L-Q)(w+c)-(L-Q)(w) = d(w).                                                  (1)
```

Consequently define

```
H(w) := (L-Q)(w) + sum_(k>=0) d(w+k*c),
E(w) := -sum_(k>=0) d(w+k*c).
```

Then `H` is exactly `c`-periodic by (1), and, exactly,

```
L(w) = Q(w)+H(w)+E(w).                                                        (2)
```

On every half-line bounded away from minus infinity, the sum and all its
derivatives converge normally.  In particular, for each fixed `j>=0`,

```
E^(j)(w) = O_j(exp(j*w-2*exp(w))).                                           (3)
```

Thus no derivative of an unspecified `o(1)` is taken below.

Here is a completely explicit local version.  Set

```
C0=(1-exp(-2))^(-1),       x=exp(w-1) >= 1.
```

For `|u-w|<=1`, direct differentiation of `d`, followed by
`3^k>=1+2k`, gives

```
|E(u)|   <= eps0(w) := C0*exp(-2*x)/(1-exp(-4*x)),
|E'(u)|  <= eps1(w) := 2*C0*x*exp(-2*x)/(1-3*exp(-4*x)),
|E''(u)| <= eps2(w) := (2*C0+4*C0^2)*x^2*exp(-2*x)/(1-9*exp(-4*x)).           (4)
```

All three are doubly exponentially small in `w`.

## 2. Bounds on the periodic perturbation

For `m!=0`, the already-established coefficient formula is

```
Hhat(m) = -(2^(i*alpha*m)/c)*Gamma(-i*alpha*m)*zeta(1-i*alpha*m),
alpha=2*pi/c.
```

The preceding note's coefficient bound says

```
|Hhat(m)| <= A*q^m*m^(-1/2)*(log(alpha*m+1)+C).                              (5)
```

It proves absolute and uniform convergence after one or two differentiations.
More explicitly, put `D=log(1+alpha)+C`.  Since
`log(1+alpha*m)<=m*log(1+alpha)`, for `j=1,2`,

```
2*sum_(m>=1) (alpha*m)^j |Hhat(m)|
 <= 2*alpha^j*A*D*sum_(m>=1)m^3*q^m
  = 2*alpha^j*A*D*q*(1+4*q+q^2)/(1-q)^4.                                   (6)
```

Outward-rounded Arb evaluation of this elementary expression gives the
sufficient rigorous bounds

```
||H'||_infinity < 0.007,                 ||H''||_infinity < 0.04.           (7)
```

The independently certified sharper `||H'||_infinity <= 0.00119774723156`
may replace `0.007`, but the proof does not need it.

## 3. True and smooth stationary points

For `0<t<1/2`, let `w*(tau)=log(r*(tau))`, where `r*` is the unique solution
of

```
t = -K'(r*).                                                                 (8)
```

Equivalently, `w*` is the unique global minimizer of `g_tau`: strict convexity
of `K` makes `-K'(s)` decrease strictly from `1/2` to `0`, while
`g_tau'(w)=exp(w)*(t+K'(exp(w)))` changes sign once.  At that point,

```
g_tau''(w*) = L''(w*)-L'(w*) = r*^2*K''(r*) =: V(r*).                        (9)
```

Let `w0=w0(tau)` be the *large* solution of

```
g0_tau'(w0)=0,       exp(w0-tau)=B0,       B0:=B(w0)>1/c.                   (10)
```

Equivalently,

```
tau=w0-log(B0),
B0=-W_{-1}(-c*exp(c*a-tau))/c.
```

It is a local minimum because `g0_tau''(w0)=B0-1/c>0`.  It is not a global
minimum: `Q(w)->-infinity` as `w->-infinity`.

At `w0`, equations (2) and (10) yield

```
g_tau'(w0)=H'(w0)+E'(w0).
```

Define

```
eta1 = 0.007+eps1(w0),       eta2 = 0.04+eps2(w0),
mu   = B0/e - 1/c - eta2,
nu   = e*B0 - 1/c + eta2.
```

(2026-08-04 critique fix: `nu` had a `+1/c` sign slip in an earlier draft; corrected to `-1/c`. It
was still a valid, if looser, upper bound either way, so nothing downstream changes.)

For sufficiently large `tau` (concretely: `beta>=3`, i.e. `tau>=2.06`, suffices for `mu>0` and
`delta<=1` with these constants), Equations
(2), (4), and (7) show that on `[w0-1,w0+1]`,

```
mu <= g_tau''(u) <= nu.                                                      (11)
```

Since `|g_tau'(w0)|<=eta1`, the derivative has opposite signs at
`w0-delta` and `w0+delta`.  The zero is `w*`, and hence

```
|w*-w0| <= delta = 2*eta1/mu = O(1/B0).                                     (12)
```

This is the rigorous `O(1/W)` statement.  It uses a derived `H''` bound, not
an assumption.

Taylor's theorem about the true stationary point gives the correctly signed
form of the informal envelope formula:

```
g_tau(w*)-g_tau(w0) = -g_tau''(xi)*(w*-w0)^2/2 <= 0                          (13)
```

for some `xi` between the two saddle locations.  Thus

```
0 <= g_tau(w0)-g_tau(w*) <= nu*delta^2/2
                             = 2*nu*eta1^2/mu^2 = O(1/B0).                  (14)
```

Moreover, (9)--(12) imply

```
V(r*) = B0-1/c+O(1).                                                         (15)
```

So (14) is exactly `O(V(r*)*(w*-w0)^2)`.  Since
`tau=w0-log(B0)`, `B0/tau -> 1/c`; both (12) and (14) are `O(1/tau)`.

## 4. Normalized envelope estimate

The log true saddle approximation is

```
S(tau) = g_tau(w*) + w* - log(2*pi*V(r*))/2.                                (16)
```

The exact normalized smooth saddle is the already-defined expression

```
P(tau) = Q(w0)+B0+w0-log(2*pi*(B0-1/c))/2.                                  (17)
```

Set `D0=B0*(exp(delta)-1)+eta2`.  From (11)--(12),
`|V(r*)-(B0-1/c)|<=D0`.  For `beta` past the same small threshold as above,
`D0<=(B0-1/c)/2`.  Combining (2), (4), (14), and
`|log(1+x)|<=2|x|` for `|x|<=1/2`, gives the explicit bound

```
|S(tau)-P(tau)-H(w0)|
 <= eps0(w0) + 2*nu*eta1^2/mu^2 + delta + D0/(B0-1/c).                       (18)
```

Every term on the right was explicitly defined above.  It is `O(1/B0)`, hence
`O(1/tau)`.  This establishes the desired stationary/envelope replacement.

## 5. Consequences (all conditional on formula (A), see the status note at the top of this file)

Formula (A), in its uniform form (itself a referee-checkable proof sketch, not yet a written
proof; see notes/H-006.md), states
`log(phi(e^{-tau}))-S(tau)=o(1)`.  Together with (18), it proves

```
log(phi(e^{-tau})) = P(tau)+H(w0(tau))+o(1).                                (19)
```

The envelope part of the error is actually `O(1/tau)`; with only the
qualitative form of formula (A), the total residual is `O(1/tau)+o_A(1)`.

For Wirsching's class, write `z_l=lambda_l*l*3^(-l)` where
`lambda_l=1+O_delta(l^(-1/2))` uniformly.  Substituting
`tau_l=-log(z_l)` in (10) gives

```
w0(tau_l) = l*c-log(lambda_l)+O(1/l).                                      (20)
```

Thus `H(w0(tau_l))->H(0)` uniformly.  Combining (19) with the already-proved
`P(tau)-log(phi0_BK(e^{-tau}))=O(log(tau)^2/tau)` yields

```
phi(z_l)/phi0_BK(z_l) -> exp(H(0))                                         (21)
```

uniformly on Wirsching's phase-locked class.  **Conditional on formula (A)** (stated precisely at
the top of this file: a three-ways independently verified, referee-checkable proof sketch, not yet
a written proof), this proves literal Conjecture 3 under Berg--Kruppel's prefactor-normalized
convention.  The corresponding bare-normalization limit is `exp(C_P+H(0))`. This lemma (sections
1-4 above) is itself unconditional and fully proven; the word "proves" in this paragraph inherits
its conditional status entirely from formula (A), not from anything in this file.

## Independent audit

`experiments/E-006-phi-asymptotic/verify_envelope_step.py` is a new standalone
audit: it imports none of the prior saddle/Fourier evaluators, computes the
defining Laplace product directly, reconstructs `H` with (2), and uses Arb on
(6).  It independently reproduces
`H(0)=-0.6271309330515259783...` and
`H(log(3/2))=-0.6267537427705819925...`, as well as the rigorous convenient
bounds in (7).  At `tau=20,40,80,160` it finds `B0*(w*-w0)` bounded by about
`1.2e-3` in magnitude and `B0*(g(w*)-g(w0))` negative with magnitude below
`8.2e-7`, in accord with (12)--(14).
