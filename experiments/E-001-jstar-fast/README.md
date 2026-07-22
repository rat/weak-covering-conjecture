# E-001 — Fast reimplementation of the j*(l) covering computation (H-001)

Rust reimplementation of `experiment_wcc.py` (E-098, previous project): computes j*(l), the
smallest j such that R_{j-1,j} covers all invertible residues mod 3^l, using a native `Vec<u64>`
bitset with cyclic rotation (instead of Python arbitrary-precision integers), parallelized
across CPU cores with rayon.

## What was done

- `src/main.rs`: the fast implementation (bitset + rotation DP, same algorithm as E-098,
  parallelized over the independent per-c updates within each exponent step).
- `src/bin/bruteforce.rs`: an independent cross-check using direct enumeration of R_{j-1,j}
  itself (no R_{ell-1,j} reduction, no bitset/rotation trick), for l<=4. Required by this
  project's honesty rules before trusting the fast method.

## Validation (done, both pass)

- `jstar-fast validate`: matches the reference table j*(l) for l=1..7 (`1,4,6,7,9,10,11`) and
  the pointwise check (l=2,j=2: image={1,2,5,7} mod 9, missing {4,8}).
- `bruteforce`: matches the same reference table for l=1..4 via a genuinely different method
  (caught and fixed a real off-by-one bug in the brute-force's own recursion bound during this
  check, see HYPOTHESES.md/notes/H-001.md for the story).
- `jstar-fast run 1 18` (informal, before the l=21-23 benchmark): reproduces j*(l) for l=1..18
  exactly matching the known table from H-114/E-098.

## How to run

```
cargo build --release
./target/release/jstar-fast validate       # reference table + pointwise check
./target/release/bruteforce 4               # independent cross-check, l<=4
./target/release/jstar-fast run <l_start> <l_end>   # production run, prints timing per l
```

## Status

See HYPOTHESES.md (H-001) and notes/H-001.md in the repository root for the full checklist,
honest benchmark results at l=21-23, and the memory-ceiling analysis for the dense-bitset
approach used here.
