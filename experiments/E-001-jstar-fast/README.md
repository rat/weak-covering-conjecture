# E-001 — Fast reimplementation of the j*(l) covering computation (H-001)

Rust reimplementation of `experiment_wcc.py` (E-098, previous project): computes j*(l), the
smallest j such that R_{j-1,j} covers all invertible residues mod 3^l, using a native `Vec<u64>`
bitset with cyclic rotation (instead of Python arbitrary-precision integers), parallelized
across CPU cores with rayon.

## What was done

- `src/main.rs`: the fast implementation (bitset + rotation DP, same algorithm as E-098). The
  count-index `c` loop within each exponent step runs sequentially, matching the original
  single-threaded algorithm's own correctness argument exactly (no snapshot trick needed);
  parallelism is instead applied *inside* each individual `shl`/`shr`/`or_assign` call, splitting
  the `Vec<u64>` word array into chunks via rayon (each output word depends on at most two fixed
  input words, so this needs no cross-thread synchronization). An earlier version instead
  parallelized across different `c` values directly (collecting all rotated bitsets for a step
  before merging); that version worked but held up to `l` extra full-size bitsets alive at once,
  which is what caused a near-OOM at l=21 before being rewritten to the current approach (see
  notes/H-001.md for the full story). The current approach keeps only one extra full-size
  temporary alive at a time.
- `src/bin/bruteforce.rs`: an independent cross-check using direct enumeration of R_{j-1,j}
  itself (no R_{ell-1,j} reduction, no bitset/rotation trick), for l<=4 only (the only range
  where full enumeration is tractable). Required by this project's honesty rules before trusting
  the fast method; note this does NOT cover l=5 and above, where the only verification is
  agreement with the previous paper's independently-run Python implementation of the same
  algorithm (l=5..20) or, at l=21, no second method at all (see notes/H-001.md).

## Validation (done, both pass, under both `cargo build` and `cargo build --release`)

- `jstar-fast validate`: matches the reference table j*(l) for l=1..7 (`1,4,6,7,9,10,11`) and
  the pointwise check (l=2,j=2: image={1,2,5,7} mod 9, missing {4,8}).
- `bruteforce`: matches the same reference table for l=1..4 via a genuinely different method
  (caught and fixed a real off-by-one bug in the brute-force's own recursion bound during this
  check, see HYPOTHESES.md/notes/H-001.md for the story).
- `jstar-fast run 1 21`: reproduces j*(l) for l=1..20 exactly matching the known table from
  H-114/E-098, plus l=21 (j*=25), which is new data not in the previous table.

## How to run

```
cargo build --release
./target/release/jstar-fast validate       # reference table + pointwise check
./target/release/bruteforce 4               # independent cross-check, l<=4
./target/release/jstar-fast run <l_start> <l_end>   # production run, prints timing per l
```

Running `l>=21` uses noticeably more memory (l=21 peaks around 27-28 GiB); see notes/H-001.md
before running l=22, which does not fit on a 62GB machine even with the packing optimization
derived there.

## Status

See HYPOTHESES.md (H-001) and notes/H-001.md in the repository root for the full checklist,
the honest benchmark history (including a memory estimate that was wrong twice before landing on
the current numbers), and why l=21 is this hardware's ceiling.
