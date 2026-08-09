# E-008: primitive exceptional-frequency counts

For

\[
S_l(t)=\sum_{2m-1\geq a_0>\cdots>a_{m-1}\geq0}
e\!\left(\frac{t\sum_i2^{a_i}3^i}{3^l}\right),
\qquad T_m={2m\choose m},
\]

`count_spectrum.py` constructs the exact residue histogram by compiled tuple
enumeration and obtains the complete spectrum with one FFT.  It restricts the
reported counts to primitive frequencies, `t % 3 != 0`.  Histogram mass and
Parseval are checked on every run; requested fixed thresholds must be more than
`1e-10` from every computed coefficient.  A separate direct-sum check at
`l=m=4` matched five selected FFT coefficients and the entire histogram.

The main scale below is the first-order cardinality threshold

\[
m=\left\lceil \log_4(3)l+\tfrac12\log_4 l\right\rceil,
\]

for which `T_m / 3^l` stays of constant order (up to the unavoidable rounding
sawtooth).

| l | m | max abs(S)/T | primitive L1 | N(.02) | N(.01) | N(.005) | N(.002) | N(.001) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | .073955 | 5.05 | 118 | 158 | 162 | 162 | 162 |
| 6 | 6 | .051100 | 7.09 | 120 | 314 | 426 | 468 | 480 |
| 7 | 7 | .038866 | 10.77 | 48 | 356 | 848 | 1,336 | 1,434 |
| 8 | 8 | .031065 | 16.06 | 8 | 160 | 1,064 | 2,906 | 3,914 |
| 9 | 8 | .061434 | 49.99 | 42 | 552 | 3,090 | 9,360 | 11,888 |
| 10 | 9 | .038702 | 73.80 | 16 | 186 | 1,678 | 13,138 | 26,754 |
| 11 | 10 | .024672 | 108.95 | 4 | 76 | 680 | 9,644 | 37,350 |
| 12 | 11 | .017680 | 160.77 | 0 | 42 | 258 | 4,408 | 29,072 |
| 13 | 12 | .013860 | 237.05 | 0 | 12 | 114 | 1,838 | 14,268 |
| 14 | 13 | .010344 | 349.14 | 0 | 4 | 48 | 820 | 6,344 |
| 15 | 13 | .034834 | 1,646.07 | 6 | 74 | 694 | 10,234 | 72,100 |
| 16 | 14 | .027176 | 2,420.90 | 4 | 34 | 302 | 4,786 | 33,808 |
| 17 | 15 | .020059 | 3,557.97 | 2 | 8 | 136 | 2,278 | 16,376 |
| 18 | 16 | .016413 | 5,226.01 | 0 | 6 | 70 | 1,088 | 8,014 |

Here `N(eta)` means the number of primitive `t` with `|S_l(t)|/T_m > eta`.
Fixed-height spikes are sparse and sawtoothed, but this does **not** make the
Fourier L1 mass sparse.  At the square-root threshold the counts are
exponential:

| l | primitive count | N(1/sqrt(T)) | N(2/sqrt(T)) | N(4/sqrt(T)) | N(8/sqrt(T)) |
|---:|---:|---:|---:|---:|---:|
| 15 | 9,565,938 | 1,242,404 | 259,614 | 39,468 | 5,452 |
| 16 | 28,697,814 | 3,489,454 | 751,232 | 120,134 | 17,728 |
| 17 | 86,093,442 | 9,820,962 | 2,169,356 | 365,230 | 55,572 |
| 18 | 258,280,326 | 27,686,418 | 6,273,550 | 1,098,900 | 174,306 |

The stable positive proportions in the second table explain the coexistence of
few fixed-height resonances with a rapidly growing L1 norm.  This is numerical
evidence, not an asymptotic theorem.

Example commands:

```bash
python3 count_spectrum.py --l-min 5 --l-max 18 --scale counting
python3 count_spectrum.py --l-min 5 --l-max 18 --scale counting \
  --thresholds .01 .001 --rms-multipliers .5 1 2 4 8
python3 count_spectrum.py --l-min 5 --l-max 16 --scale plus2
```

## Round-3 inverse-Fourier diagnostics

`analyze_inverse.py` computes the exact hit-count histogram `N_l(z)`, checks
that an FFT followed by an inverse FFT recovers every integer count, and
compares the actual signed primitive-frequency sum with its `L1`, `L2`, iid
occupancy, and phase-scramble benchmarks.  The relevant exact identity is

\[
 \sum_{3\nmid t}S_l(t)e(-tz/3^l)
 =3^{l-1}\bigl(3N_l(z)-N_{l-1}(z\bmod 3^{l-1})\bigr).
\]

Here `N_{l-1}` uses the same tuple parameter `m` and only reduces the
modulus by a factor of three.

Thus primitive-frequency cancellation measures imbalance among the three
lifts of one parent; it is not a separate deviation-from-the-global-mean
quantity.

At the largest full inverse FFT run, `(l,m)=(18,16)`, the transform recovered
all `387,420,489` direct histogram counts after rounding, with maximum real
error `2.85e-14`.  On the unit residues:

| quantity | exact value |
|---|---:|
| mean hit count | 2.32724032569 |
| zero hit count | 83,864,386 |
| iid-uniform expected zeros | 25,199,022.39 |
| primitive triangle envelope (`L1/q`) | 8,108.12797 counts |
| actual largest primitive lift deviation | 17 counts |
| primitive RMS deviation (`L2/q`) | 0.851082552 counts |
| actual max/RMS | 19.9746 |
| iid-Gaussian extreme heuristic | 6.3982 |

There is already a factor `476.95` of cancellation relative to the primitive
triangle envelope.  It does not produce coverage: almost one third of the
unit residues are still holes, and the extreme lift imbalance is much heavier
than a generic Gaussian-phase heuristic.

Generic independent occupancy would become relevant to uniform covering near
the coupon-collector scale

\[
m=\left\lceil \log_4(3)l+\tfrac32\log_4 l\right\rceil,
\]

where the mean hit count is of order `log(3^l)`.  At `l=15`, this gives
`m=15`, unit mean `16.2156` versus `log(2*3^14)=16.0737`.  An iid-uniform
occupancy model has only `0.8677` expected empty units, while the exact
histogram has `842,318` empty units.  This result was computed independently
twice.  It rules out the generic-occupancy model at the scale where that model
would actually predict covering, not just at the constant-mean scale.

A higher-occupancy check makes the non-generic clustering much sharper.  For
fixed `l=14`:

| m | mean hits per unit | actual zeros | iid-uniform expected zeros | Fano factor |
|---:|---:|---:|---:|---:|
| 14 | 12.5811 | 352,200 | 10.9575 | 21.4689 |
| 15 | 48.6468 | 112,071 | 2.3799e-15 | 85.7979 |
| 16 | 188.5065 | 18,895 | 4.3279e-76 | 344.1548 |

At `(l,m)=(14,16)`, the actual primitive max/RMS ratio is `15.7867`.
Eight conjugate-symmetric phase scrambles preserving every primitive
`|S(t)|` gave ratios only in `[5.1076, 5.2355]` (fixed seed `20260808`).
This is numerical evidence that the phases are strongly correlated, but in a
heavy-tailed/overdispersed way rather than in the uniformly helpful way needed
for covering.  Phase scrambling is only a null diagnostic: it does not
preserve nonnegativity or integrality of the inverse transform.

Reproduce the two full diagnostics with:

```bash
python3 analyze_inverse.py --l 18
python3 analyze_inverse.py --l 14 --m 16 --scramble-trials 8
```
