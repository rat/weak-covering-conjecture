# Formula (A): a uniform saddlepoint proof

This note supplies the missing written proof of formula (A). It is
self-contained; no numerical experiment is used in any estimate. The
deliberately loose constants make the displayed threshold ineffective, but
they make every quantifier uniform in the phase.

Let U_j be independent uniform random variables on [0,1], and put

~~~
X = sum_(j>=1) (2/3^j) U_j,
ell(z) = log((1-exp(-z))/z)       (Re z>0),
K(s) = sum_(j>=1) ell(2s/3^j).
~~~

The logarithm is the analytic branch which is real on (0,infinity). Thus
K(s)=log E exp(-sX). Write

~~~
t(s) = -K'(s),
V(s) = s^2 K''(s),
phi_sp(t(s)) = exp(K(s)+s t(s))/sqrt(2*pi*K''(s)).
~~~

Thus phi_sp is the quantity called phi_saddle in the statement of formula
(A); the shorter symbol is used only to keep the displayed estimates narrow.

All differentiations of K below are justified term by term.  Indeed, on
every compact subset of Re z>0 the functions ell(cz), c=2/3^j, and all their
derivatives form normally convergent series: for the finitely many terms with
c|z|>1 there is nothing to prove, while for the others (1.4) below gives
ell(w)=-w/2+O(w^2), ell'(w)=-1/2+O(w), and ell^(n)(w)=O_n(1) for
n>=2.  The resulting bounds are summable in c and c^2, respectively.
Also K''(s)>0, since it is the variance of X under its exp(-sX) tilt.

The theorem proved below is the following quantitative form of formula (A).

**Theorem.** For s>0, write, uniquely,

~~~
2s = rho*3^N,       N=floor(log_3(2s)),       1 <= rho < 3.
~~~

For every integer N>=2000, uniformly for 1<=rho<3,

~~~
| phi(t(s))/phi_sp(t(s)) - 1 |
<= 304 N^(-1/2) + 3369 N^(-1)
 + 2 N^(-1/10) exp(-N^(1/5)/4)
 + 9 N^(-1/10) exp(-N^(1/5)/8).                            (A.1)
~~~

In particular, phi(t(s))=phi_sp(t(s)) (1+o(1)) as s tends to infinity,
uniformly in rho (and hence uniformly through all positive real s).

The proof has four ingredients: a one-factor complex-derivative lemma, the
phase-uniform variance bounds, exact inversion, and a central/tail split.

## 1. One-factor estimates, including the off-real-axis lemma

For n>=2 define the derivative-normalized functions

~~~
kappa_n(z) = (-1)^n z^n ell^(n)(z),       Re z>0.                         (1.1)
~~~

The signs are only a convention. On the positive real axis kappa_2 is the
variance contribution used below.

**Lemma 1 (uniform complex one-factor bounds).** If b>0 and |y|<=1, then

~~~
|kappa_2(b(1+i y))| <= 3,
|kappa_3(b(1+i y))| <= 63,
|kappa_4(b(1+i y))| <= 785.                                  (1.2)
~~~

Moreover, if 0<b<=1/sqrt(2), then

~~~
|kappa_2(b(1+i y))| <= (4/5) b^2,
|kappa_3(b(1+i y))| <= (12/5) b^2,
|kappa_4(b(1+i y))| <= (48/5) b^2.                            (1.3)
~~~

(2026-08-04 critique fix: the `n=2` line read `(2/5)b^2`, but the Cauchy-estimate argument
actually used gives `4A*b^2 = (4/5)b^2` (`A<=1/2`), not `2A*b^2`. Corrected here; this line was
never load-bearing downstream (V comes from Lemma 2, not from this bound), so no other constant in
this file changes.)

Consequently sup_(b>0, |y|<=1)|kappa_n(b(1+i y))| is finite for
n=2,3,4. This is the boundedness-off-the-real-axis assertion which the
earlier proof sketches used but did not state.

*Proof.* Set

~~~
H(z) = log(sinh(z/2)/(z/2)),       so ell(z)=-z/2+H(z).          (1.4)
~~~

For |z|<=2, the canonical product for sinh and
|log(1+w)|<=-log(1-|w|) give

~~~
|H(z)| <= sum_(m>=1) -log(1-1/(pi^2 m^2))
        = -log(sin(1)) =: A < 1/5.                             (1.5)
~~~

Here the last equality is Euler's sine product. If |w|<=1, the circle
|z-w|=1 lies in |z|<=2, so Cauchy's estimate gives

~~~
|H^(n)(w)| <= n! A.                                             (1.6)
~~~

For w=b(1+i y) with b<=1/sqrt(2), we have |w|<=1; since
ell^(n)=H^(n) for n>=2, (1.6), |w|<=sqrt(2)b, and sqrt(2)b<=1
yield respectively

~~~
2A b^2,       12A b^2,       48A b^2,
~~~

which are bounded by the three quantities in (1.3). For the last inequality
in (1.5), the alternating sine series gives sin(1)>=5/6 and
-log(5/6)=log(6/5)<1/5.

It remains to handle b>=1/sqrt(2). Put
x=w/2=a(1+i y), where a=b/2>=a_0:=1/(2sqrt(2)). Direct
differentiation of (1.4) gives

~~~
kappa_2(w) = 1-x^2 csch^2(x),
kappa_3(w) = 2-2x^3 csch^2(x)coth(x),
kappa_4(w) = 6-4x^4 csch^2(x)coth^2(x)-2x^4 csch^4(x).          (1.7)
~~~

The required separation from the poles is explicit:

~~~
|sinh(a+iay)|^2 = sinh^2(a)+sin^2(ay) >= sinh^2(a).             (1.8)
~~~

Also |cosh(a+iay)|<=cosh(a) and |x|<=sqrt(2)a. The second formula
in (1.7) is therefore bounded in modulus by

~~~
2 + 2 T_3,
T_3 = 27 sqrt(2) exp(-3) * (1+q_0)/(1-q_0)^3,
q_0=exp(-1/sqrt(2)).                                           (1.9)
~~~

Indeed,

~~~
|x^3 csch^2(x)coth(x)|
<= 8 sqrt(2) a^3 exp(-2a)(1+exp(-2a))/(1-exp(-2a))^3,
~~~

and we use a^3 exp(-2a)<=27 exp(-3)/8 and a>=a_0. The elementary
series estimates e>8/3 and exp(1/sqrt(2))>2 give exp(-3)<1/16 and
q_0<1/2. Here e>8/3 is the sum of the terms through 1/3!, while
exp(1/sqrt(2))>2 follows from its terms through degree three:
5/4+13/(12sqrt(2))>2 because 13^2>2*9^2. Hence T_3<243/8, so
2+2T_3<63.
Similarly the two nonconstant terms in the third formula in (1.7) are at
most

~~~
T_41 = 16*(16 exp(-4))*(1+q_0)^2/(1-q_0)^4,
T_42 = 64 exp(-4)/(1-q_0)^4,                                  (1.10)
~~~

respectively. This uses a^4 exp(-2a)<=16 exp(-4) and
a^4 exp(-4a)<=exp(-4). Since exp(-4)<1/50 and q_0<1/2,
T_41<4608/25 and T_42<512/25. Therefore

~~~
6+4T_41+2T_42 < 19606/25 < 785.                               (1.11)
~~~

Finally, the first formula in (1.7), (1.8), and sinh(a)>=a give
|kappa_2(w)|<=1+2a^2/sinh^2(a)<=3. This proves (1.2) and the
lemma. Notice that (1.8), rather than an unproved appeal to continuity,
is what excludes approach to any pole 2*pi*i*k. ∎

For later reference, define

~~~
v(b)=kappa_2(b)=1-(b/2)^2 csch^2(b/2),       b>0.               (1.12)
~~~

It satisfies 0<v(b)<1. It is also b^2 Var_b(U), where U has
density proportional to exp(-bu) on [0,1]; hence

~~~
v(b)<=b^2/4.                                                    (1.13)
~~~

## 2. Uniform phase bookkeeping

Put

~~~
b_j=2s/3^j=rho*3^(N-j),       V=V(s)=sum_(j>=1)v(b_j).           (2.1)
~~~

The following estimates are uniform in rho.

**Lemma 2 (variance and derivative sums).** For every N>=1,

~~~
N-5 <= V <= N+9/32.                                            (2.2)
~~~

For |y|<=1 and N>=2,

~~~
|s^3 K'''(s(1+i y))| <= 95N,
|s^4 K''''(s(1+i y))| <= 1179N.                                (2.3)
~~~

*Proof.* For the lower bound, the first N values are
b=rho*3^k, 0<=k<N, and

~~~
1-v(b) = b^2 exp(-b)/(1-exp(-b))^2.                             (2.4)
~~~

For k=0, b^2 exp(-b)<=4 exp(-2). For k>=1, use
rho*3^k>=3^k>=2k+1 and x^2 exp(-x/2)<=16 exp(-2) to obtain

~~~
sum_(k>=1) b^2 exp(-b) <= 16 exp(-5/2)/(exp(1)-1).
~~~

Since b>=1 in (2.4), the total deficit of the first N terms is at
most

~~~
C_- := [4 exp(-2)+16 exp(-5/2)/(exp(1)-1)]/(1-exp(-1))^2
     < 5.                                                       (2.5)
~~~

For an entirely rational verification of this last displayed bound, use
e>8/3. Then the denominator factor is at most 64/25, while the two terms
in its numerator are at most 9/16 and 27/20, respectively. Their product
is 612/125<5.

The omitted terms are positive, proving the lower bound. For the upper
bound, the first N terms are below one by (1.12). On j>N, (1.13)
and rho<3 give

~~~
sum_(j>N) v(b_j) <= (1/4) sum_(m>=1)(3*3^(-m))^2 = 9/32,
~~~

which proves (2.2).

For the derivative bounds, termwise differentiation gives, for n>=2,

~~~
|s^n K^(n)(s(1+i y))|
<= sum_(j>=1)|kappa_n(b_j(1+i y))|.                             (2.6)
~~~

Indeed, the j-th term on the left before taking absolute values is
`b_j^n ell^(n)(b_j(1+i y))=(-1)^n kappa_n(b_j(1+i y))/(1+i y)^n`,
and `|1+i y|>=1`.

There are N terms with j<=N, and one further term. Bound these by
(1.2). For j>=N+2, use (1.3) and

~~~
sum_(j>=N+2)b_j^2 <= sum_(m>=2)(3*3^(-m))^2=1/8.                (2.7)
~~~

The simple rational bounds in (1.2)--(1.3) make the right side of (2.6)
at most

~~~
3N+16/5,       63N+633/10,       785N+3931/5.                  (2.8)
~~~

for n=2,3,4, respectively. The latter two are at most 95N and
1179N for every N>=2, proving (2.3). This explicit 1179N, not an
unverified claim such as a 6N bound, is all that the proof uses. ∎

Here is the corrected phase-rescaling statement. It is not needed for the
coarse bounds above, but records precisely the stronger fact without the
incorrect exponentially-small remainder from an earlier sketch. The series

~~~
C_V(rho) = sum_(k<=-1)v(rho*3^k) + sum_(k>=0)(v(rho*3^k)-1)     (2.9)
~~~

converges absolutely and uniformly for 1<=rho<3, by (1.13) on the first
sum and (2.4)--(2.5) on the second. Reindexing (2.1) gives exactly

~~~
V = N+C_V(rho)+R_N(rho),
0 <= R_N(rho) <= 6 (rho*3^N)^2 exp(-rho*3^N).                   (2.10)
~~~

To verify the last bound, write B=rho*3^N>=1. Formula (2.4) shows that
R_N is no more than (1-exp(-1))^(-2) B^2 exp(-B) times

~~~
1 + 9 exp(-2)/(1-9 exp(-6)).                                   (2.11)
~~~

Indeed, after the k=0 term, consecutive terms have ratio at most
9 exp(-6). For a rational check, e>8/3 gives
9 exp(-6)<6561/262144<1/39 and exp(-2)<9/64. Therefore the product
of (2.11) with (1-exp(-1))^(-2) is less than
(64/25)*(1+(81/64)*(39/38))=5591/950<6. Thus the remainder is of order
(rho*3^N)^2 exp(-rho*3^N), as required; it is not merely
O(exp(-rho*3^N)).

## 3. Exact inversion and the large-frequency estimate

The law of X has a continuous density phi: the convolution of its first
two uniform summands has a continuous compactly supported density, and
convolution with the remaining probability law preserves continuity. For
fixed s, exponentially tilt that law by exp(-sX). Its characteristic
function at frequency sy is

~~~
exp(K(s(1+i y))-K(s)).                                         (3.1)
~~~

For one factor of (3.1), its modulus is

~~~
|1-exp(-b)exp(-iby)| / ((1-exp(-b))*sqrt(1+y^2)).               (3.2)
~~~

It is at most one, since it is the modulus of the characteristic function of
a variable in [0,1] under its one-factor exponential tilt. Also, by the
triangle inequality, it is at most

~~~
coth(b/2)/sqrt(1+y^2).                                         (3.3)
~~~

We will use (3.3) only for the first N factors, whose arguments are
rho,3rho,...,3^(N-1)rho and are all at least one.

**Lemma 3 (the coth product).** If b_0>=1, then

~~~
sum_(k>=0) log coth(3^k b_0/2) <= 3 exp(-b_0).                 (3.4)
~~~

*Proof.* Let q=exp(-b_0)<=exp(-1). The identity
log coth(x/2)=2 atanh(exp(-x)), the integral bound
atanh(u)<=u/(1-u^2), and 3^k>=2k+1 give

~~~
sum_(k>=0) log coth(3^k b_0/2)
<= 2 sum_(k>=0) q^(3^k)/(1-q^(2*3^k))
<= 2q/(1-q^2)^2
<= 2q/(1-exp(-2))^2 < 3q.                                    (3.5)
~~~

For the final strict inequality, e>8/3 gives exp(-2)<9/64, so its
coefficient is at most 2*(64/55)^2=8192/3025<3.

The hypothesis b_0>=1 is sufficient for the displayed numerical constant (not necessary: the
critique found the bound still holds, with a different constant, down to b_0=0.7; it fails by
b_0=0.3), and has now been stated explicitly. Only b_0=rho>=1 is ever used in this proof, so
sufficiency is all that's needed. ∎

It follows from (3.2)--(3.4), retaining (3.3) on the selected N factors
and the bound one on all the others, that for every real y,

~~~
|exp(K(s(1+i y))-K(s))|
<= exp(3/e) (1+y^2)^(-N/2).                                   (3.6)
~~~

For N>=2, this proves integrability of the tilted characteristic function;
ordinary Fourier inversion is therefore valid at every t. At the saddle,
put

~~~
F(y)=K(s(1+i y))-K(s)+i s y t(s).                              (3.7)
~~~

After the change of variable u=sy, inversion becomes

~~~
phi(t(s))/phi_sp(t(s))
= sqrt(V/(2*pi)) integral_R exp(F(y)) dy.                      (3.8)
~~~

The linear term of F vanishes because t(s)=-K'(s).

Set a=N^(-2/5). The contribution of |y|>a in (3.8), using (3.6), is at
most

~~~
E_tail = 2 exp(3/e) sqrt(V/(2*pi))
         /[a(N-1)] * (1+a^2)^(-(N-2)/2).                       (3.9)
~~~

For completeness, the elementary integral inequality used here is

~~~
integral_a^infinity (1+y^2)^(-N/2) dy
<= (1/[a(N-1)])(1+a^2)^(-(N-2)/2),                            (3.10)
~~~

obtained by differentiating (1+y^2)^(-(N-1)/2) and using
sqrt(1+y^2)/y<=sqrt(1+a^2)/a for y>=a.

For N>=4, (2.2), 1/(N-1)<=2/N, and
log(1+a^2)>=a^2/2 give the simpler completely explicit form

~~~
E_tail <= 9 N^(-1/10) exp(-N^(1/5)/8).                         (3.11)
~~~

For a rational check on the constant, e>8/3 and e<3 imply
exp(3/e)<exp(9/8)<3^(9/8)<4, while 1/sqrt(2*pi)<1/2. Thus its
coefficient is less than 9. The upper bound e<3 follows directly from the
series for e: after the terms 1+1+1/2, its remaining terms are strictly
bounded by the geometric tail 1/2+1/4+...=1.

## 4. Central arc and assembly

We now use the fourth derivative, retaining the cubic term. By (2.3) and
Taylor's formula along the real line in the variable y,

~~~
F(y) = -V y^2/2 - i C y^3/6 + R_4(y),
C=s^3 K'''(s),
|C|<=95N,       |R_4(y)|<=1179N |y|^4/24                       (4.1)
~~~

for |y|<=a. Crucially, the remainder in (4.1) is the *integral* remainder

~~~
R_4(y) = y^4/3! * integral_0^1 (1-u)^3 F^(4)(uy) du,            (4.2)
~~~

not a complex-variable Lagrange remainder. Formula (4.2) is valid because
the analytic function F is restricted to the real segment from 0 to y.

For N>=2000, (2.2) gives V>=N/2, and

~~~
1179N a^2/24 = (1179/24)N^(1/5) <= N/8 <= V/4.                 (4.3)
~~~

The only numerical threshold used here is exact: the first inequality follows
from N^(4/5)>=393, which holds at N=2000 since

~~~
2000^4=16000000000000 > 9374815985193=393^5.
~~~

Thus, throughout the central arc,

~~~
Re F(y) <= -V y^2/4.                                           (4.4)
~~~

Let G(y)=-Vy^2/2. The integral form of the exponential difference and
(4.1), (4.4) imply

~~~
|exp(F(y))-exp(G(y))|
<= exp(-Vy^2/4) (95N |y|^3/6 + 1179N |y|^4/24).                (4.5)
~~~

Extending this nonnegative majorant from [-a,a] to the whole real line and
using the exact Gaussian moments gives

~~~
sqrt(V/(2*pi)) integral_(-a)^a |exp(F)-exp(G)| dy
<= 8(95N)/(3 sqrt(2*pi)V^(3/2)) + 1179N/(sqrt(2)V^2)
<= 304 N^(-1/2)+3369 N^(-1).                                 (4.6)
~~~

The two moment evaluations are

~~~
integral_R |y|^3 exp(-Vy^2/4) dy = 16/V^2,
integral_R y^4 exp(-Vy^2/4) dy = 24 sqrt(pi)/V^(5/2).
~~~

In the final inequality in (4.6) we used V>=N/2; its two constants are
respectively 1520/(3sqrt(pi))<304 and 2358sqrt(2)<3369.
For example, these follow from sqrt(pi)>sqrt(3)>5/3 and
sqrt(2)<10/7.

Finally, the normalized Gaussian omitted outside the central arc is bounded
by the standard one-sided integration-by-parts estimate:

~~~
sqrt(V/(2*pi)) integral_(|y|>a) exp(-Vy^2/2) dy
<= sqrt(2/pi) exp(-Va^2/2)/(a sqrt(V))
<= 2 N^(-1/10) exp(-N^(1/5)/4).                               (4.7)
~~~

Combining (3.8), (3.11), (4.6), and (4.7) proves (A.1).
Every bound from Lemma 1 onward is a supremum over the entire interval
1<=rho<3; therefore the threshold N>=2000 is independent of rho.
This establishes the claimed uniform o(1). ∎

## Independent numerical audit (not used in the proof)

experiments/E-006-phi-asymptotic/verify_formula_a_constants.py evaluates at
80 decimal digits the elementary bounds in (1.11), (2.5), (3.5), and the
integer check in (4.3). It also compares the closed forms in (1.7) with
independent numerical differentiation at a grid of complex points. The
largest observed disagreement is below 1.8e-80. The existing
round14_rho_uniformity_check.py separately checks the phase rescaling
numerically; neither script is an input to the theorem.
