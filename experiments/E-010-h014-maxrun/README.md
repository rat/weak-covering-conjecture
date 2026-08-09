# E-010: exact H-014 maxrun extension through level 22

Round 5 of the fixed GAP A push (2026-08-09).  This experiment computes

```text
maxrun(H(ell,ell+1)),
H(ell,j) = units mod 3^ell not represented by R_{j-1,j},
```

exactly.  It extends the prior complete range through `ell=22`.  There is no
violation of the empirically suggested ceiling 4 in this range.  Finite data,
of course, cannot prove or refute the asymptotic boundedness assertion H-014.

## Exact result

The `actual chain` column is in the original `H(ell,ell+1)` coordinates, not
the reduced DP coordinates.  Each displayed list is a certificate: consecutive
entries differ by multiplication by 2 modulo `3^ell`, and all are holdouts.

| ell | j | `|H(ell,j)|` | maxrun | one actual maximal chain |
|---:|---:|---:|---:|:---|
| 1 | 2 | 0 | 0 | empty |
| 2 | 3 | 1 | 1 | 7 |
| 3 | 4 | 3 | 2 | 1, 2 |
| 4 | 5 | 10 | 2 | 58, 35 |
| 5 | 6 | 28 | 3 | 151, 59, 118 |
| 6 | 7 | 77 | 3 | 118, 236, 472 |
| 7 | 8 | 208 | 3 | 76, 152, 304 |
| 8 | 9 | 552 | 3 | 430, 860, 1720 |
| 9 | 10 | 1,430 | 3 | 262, 524, 1048 |
| 10 | 11 | 3,628 | 4 | 37498, 15947, 31894, 4739 |
| 11 | 12 | 8,957 | 4 | 149992, 122837, 68527, 137054 |
| 12 | 13 | 21,423 | 4 | 468718, 405995, 280549, 29657 |
| 13 | 14 | 49,807 | 4 | 8023, 16046, 32092, 64184 |
| 14 | 15 | 112,071 | 4 | 1167145, 2334290, 4668580, 4554191 |
| 15 | 16 | 243,529 | 4 | 7273783, 198659, 397318, 794636 |
| 16 | 17 | 505,049 | 3 | 2290, 4580, 9160 |
| 17 | 18 | 997,201 | 3 | 218266, 436532, 873064 |
| 18 | 19 | 1,851,056 | 3 | 237376, 474752, 949504 |
| 19 | 20 | 3,195,464 | 3 | 98518, 197036, 394072 |
| 20 | 21 | 5,044,358 | 3 | 46326418, 92652836, 185305672 |
| 21 | 22 | 7,156,001 | 3 | 524791360, 1049582720, 2099165440 |
| 22 | 23 | 8,951,079 | 3 | 1563565306, 3127130612, 6254261224 |

Thus the sequence for `ell=1..22` is

```text
0,1, 2,2, 3,3,3,3,3, 4,4,4,4,4,4, 3,3,3,3,3,3,3.
```

This is exact finite evidence, not a proof that maxrun is uniformly bounded.

## Algorithm and exactness

For `j>=ell`, the already verified reduction is

```text
R_{j-1,j} = 2^(j-ell) R_{ell-1,j} (mod 3^ell).
```

Here `j=ell+1`, so the code computes `R_{ell-1,ell+1}` by the same
descending-exponent 0/1 DP and cyclic bitset shifts used by E-001 and E-009.
Multiplication by the common factor 2 preserves every doubling-chain length.
The extractor scales its chain back by 2 before reporting the `actual_chain`.

The memory optimization is representation-only.  Low DP layers retain one
residue per exponent subset (duplicates are harmless); higher layers use packed
bitsets.  A transition either appends the exact translated sparse list, inserts
its entries into a packed target, or ORs an exact cyclic shift of one packed
bitset into another.  The final image is checked by

```text
image_size + holdout_count = 2*3^(ell-1).
```

The final scan visits every missing unit.  A run begins exactly when its half
is covered, and the scan follows repeated doubling until coverage resumes.
It also verifies the displayed chain and its two covered boundary neighbors.

## Validation

`verify_small.py` independently enumerates the **original** `R_{j-1,j}` tuples
with Python combinations for every `ell=1..10`.  Its complete holdout counts
and maxruns agree with the reduced Rust DP in all ten cases.  Runtime was
2.63 s and peak RSS 13,464 KiB.

The packed-only setting (`sparse_cutoff=0`) is a second state representation.
It exactly reproduced the hybrid results at the two largest practical checks:

```text
ell=19: image=771645514, |H|=3195464, maxrun=3, reduced start=49259
ell=20: image=2319478576, |H|=5044358, maxrun=3, reduced start=23163209
```

The `ell=19` holdout count also matches E-009's earlier independent NumPy
computation exactly.

## Reproduction and resources

From this directory:

```bash
cargo build --release
python3 verify_small.py
target/release/h014-maxrun 20 7
target/release/h014-maxrun 21 7
target/release/h014-maxrun 22 8 --progress
```

The large runs used all 16 logical CPUs on the round-5 host:

| ell | sparse cutoff | wall time | DP+scan time | peak RSS | swaps | major faults |
|---:|---:|---:|---:|---:|---:|---:|
| 19 | 7 | 3.56 s | 3.402 s | 1,714,252 KiB | 0 | 0 |
| 20 | 7 | 11.86 s | 11.339 s | 5,547,952 KiB | 0 | 0 |
| 21 | 7 | 40.67 s | 38.920 s | 17,894,680 KiB | 0 | 0 |
| 22 | 8 | 131.81 s | 126.436 s | 53,714,376 KiB | 0 | 0 |

The host has 62 GiB physical RAM.  At `ell=23`, the modulus is
`94,143,178,827`; one packed layer alone is about 10.96 GiB, and the current
exact kernel needs many simultaneous layers.  The naive scale-up is well over
physical memory and would become a swap-heavy, qualitatively different run.
It was deliberately not launched.  Reaching 23--30 requires another state
compression or a structural argument; extrapolating the observed ceiling is
not an exact result.
