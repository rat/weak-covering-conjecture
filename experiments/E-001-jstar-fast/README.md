# E-001: Fast reimplementation of the j*(l) covering computation (H-001)

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
./target/release/jstar-fast size <l> <j>            # single image_size(l,j) call, for
                                                     # testing/debugging one attempt in isolation
```

Running `l>=21` uses noticeably more memory (l=21 peaks around 27-28 GiB) and, from l=22 on, more
than physical RAM (see notes/H-001.md, "l=22 reached via swap"); this machine now has a 1.8TiB
swap partition specifically for that.

## Checkpointing (added 2026-07-23, removed 2026-07-27)

l=23's run added full-state checkpoint/resume (`checkpoints/state_l{l}_j{j}.bin`,
FNV-1a-checksummed) after an unprotected first attempt was lost to a `systemd-oomd` policy kill.
It worked and was verified correct, but turned out to dominate wall time once the state reached
hundreds of GiB (each save took over an hour). Once `systemd-oomd` was disabled at the root cause
(rather than just buffered against), the checkpoint mechanism was removed entirely, see
notes/H-001.md "Plan for l=24 onward" for the reasoning and trade-off. `run`/`size` now always
computes an attempt start-to-finish in one pass; killing the process loses that attempt's
progress, there is no resume.

The lightweight `checkpoints/progress_l{l}.txt` log (one line per `j` already confirmed not
covering, so `find_j_star` doesn't redo a settled `j` after a restart) was kept, since it costs
nothing (a few bytes per line, not a state dump).

**Correction to an earlier plan**: session notes at one point proposed also switching `state` to
a "packed/bitset" representation to save memory, on the assumption the existing representation
wasn't already bit-packed. That assumption was wrong: `state` was already `Vec<BigBitset>` with
`BigBitset.words: Vec<u64>`, i.e. exactly 1 bit per residue, `(ell+1)` full `3^ell`-bit bitsets
held at once (verified directly in the code and against every observed memory/checkpoint size).
Total memory is `(l+1) * 3^l / 8` bytes exactly; this `(l+1)` factor is structural to the
rotation-DP algorithm itself, not a representation inefficiency. There was no bitset conversion
to do, and none was done.

## Status

See HYPOTHESES.md (H-001) and notes/H-001.md in the repository root for the full checklist and
the honest benchmark/memory history: why l=21 needed no swap, l=22 and l=23 did, how l=22 was
reached, and l=23's result (j*(23)=27, e(23)=8.773, ~104h wall time).
