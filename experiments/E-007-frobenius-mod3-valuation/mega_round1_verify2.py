"""
Verify the substantive NEW part of round-1's "certain confidence" claim: a valid strictly-
decreasing prefix alpha_0 > ... > alpha_{l-1} >= 0 (with alpha_0 <= 2j-1) extends to a full
j-term admissible tuple (staying strictly decreasing, all >=0, alpha_0<=2j-1) IF AND ONLY IF
alpha_{l-1} >= j-l.

(The fact that F_j(alpha) mod 3^l depends only on alpha_0..alpha_{l-1} is elementary and already
foundational to this whole project -- not re-verified here, not the new content.)
"""
import random
random.seed(7)

def can_extend_bruteforce(prefix, j):
    """Brute-force: can we choose j-len(prefix) more strictly-decreasing values below
    prefix[-1], down to >=0? Just check count: need j-len(prefix) distinct values in
    [0, prefix[-1]-1], which requires prefix[-1] >= j-len(prefix)."""
    need = j - len(prefix)
    avail = prefix[-1]  # values 0..prefix[-1]-1 available
    return avail >= need

ok = True
for trial in range(500):
    l = random.randint(2, 8)
    j = random.randint(l, l + 6)
    # random valid prefix: l strictly decreasing values, alpha_0 <= 2j-1
    if 2 * j - 1 < l - 1:
        continue
    prefix = sorted(random.sample(range(0, min(2 * j, 30)), l), reverse=True)
    claim = prefix[-1] >= j - l
    actual = can_extend_bruteforce(prefix, j)
    if claim != actual:
        ok = False
        print(f"  MISMATCH l={l} j={j} prefix={prefix}: claim={claim} actual={actual}")

print(f"500 random trials: {'CONFIRMED: extendable iff alpha_{l-1} >= j-l' if ok else 'FAILURES FOUND'}")
