"""
Independent verification of Codex's concrete R_{2,3} mod 27 calculation (second
consultation cycle, round 4, /home/rat/.claude/jobs/a8d2d60e/tmp/codex_stuck2_round4_out.txt),
used as a worked example for the GAP A pressure-gap transfer-matrix proposal.

R_{j,k} := { sum_{i=0}^j 2^{alpha_i}*3^i : j+k >= alpha_0 > alpha_1 > ... > alpha_j >= 0 }.
For R_{2,3}: j=2, k=3, so 3 exponents (i=0,1,2) drawn from domain {0,...,j+k}={0,...,5}.

Codex claimed, from its own hand derivation of the exact block-update recursion
C_{a+1,r} = C_{a,r} UNION (2^a + 3*C_{a,r-1}) mod M:

    R_{2,3} mod 27 = {2, 4, 8, 10, 11, 17, 19, 20, 22, 23, 26}   (11 distinct residues
                                                                    from C(6,3)=20 tuples)
"""
from itertools import combinations

J, K, M = 2, 3, 27
domain = range(0, J + K + 1)  # {0,...,5}
num_exponents = J + 1  # 3

residues = set()
count = 0
for combo in combinations(domain, num_exponents):
    a = sorted(combo, reverse=True)  # a_0 > a_1 > a_2
    val = sum(2 ** a[i] * 3 ** i for i in range(num_exponents))
    residues.add(val % M)
    count += 1

CLAIMED = {2, 4, 8, 10, 11, 17, 19, 20, 22, 23, 26}

if __name__ == "__main__":
    print(f"total tuples: {count}  (expect C(6,3)=20)")
    print(f"distinct residues mod {M}: {sorted(residues)}")
    print(f"num distinct residues: {len(residues)}  (expect 11)")
    print(f"Codex claimed: {sorted(CLAIMED)}")
    print(f"exact match: {residues == CLAIMED}")
