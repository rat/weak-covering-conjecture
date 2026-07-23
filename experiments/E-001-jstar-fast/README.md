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
./target/release/jstar-fast size <l> <j>            # single image_size(l,j) call, for
                                                     # testing/debugging one attempt in isolation
```

Running `l>=21` uses noticeably more memory (l=21 peaks around 27-28 GiB) and, from l=22 on, more
than physical RAM (see notes/H-001.md, "l=22 reached via swap"); this machine now has a 1.8TiB
swap partition specifically for that.

## Checkpointing (added 2026-07-23)

A multi-hour `run`/`size` call (l>=22) periodically saves the live DP `state` array to
`checkpoints/state_l{l}_j{j}.bin` (overwritten in place each save, not temp+rename: at l=23 a
second copy would need more disk than this machine has free) with an FNV-1a checksum trailer; a
save killed mid-write leaves an invalid checksum, which is detected and discarded on the next
start rather than trusted, per this project's honesty rules. `find_j_star` also logs each
confirmed-not-covering `j` to `checkpoints/progress_l{l}.txt` so a restart doesn't redo already-
settled j's. Simply re-running the same `run`/`size` command resumes automatically from whatever
checkpoints exist; nothing else to pass on the command line.

Save interval defaults to 600s, override with `WCC_CHECKPOINT_SECS=<seconds>` (0 checkpoints
after every single `v` step - very slow, only useful for testing resume itself, not production).
Verified end-to-end (2026-07-23): killed a `size 18 18` call with `-9` mid-run, confirmed the
checkpoint file was the exact expected byte size before resuming, then confirmed the resumed run's
final `image_size` matched a separate uninterrupted baseline run exactly (248594244, both runs).

Known residual risk: because saves overwrite in place (no temp+rename), a kill that lands *during*
a save's write window can lose that checkpoint too, not just progress since the last one - the
window is small at l<=21 (well under a megabyte-scale write) but could be minutes wide at l=23's
~263GiB per checkpoint. Not eliminated in this pass; would need the invertible-residue packing
optimization (analyzed but not implemented, see notes/H-001.md) to shrink checkpoints enough for
real temp+rename on this disk's free space.

## Status

See HYPOTHESES.md (H-001) and notes/H-001.md in the repository root for the full checklist and
the honest benchmark/memory history, including why l=21 needed no swap, l=22 and l=23 do, and how
l=22 was actually reached.
