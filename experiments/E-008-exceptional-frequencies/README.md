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
