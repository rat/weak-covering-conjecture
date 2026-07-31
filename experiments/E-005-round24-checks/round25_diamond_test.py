"""
Tests Codex's round-25 item 6 ("abelian slack-transport network"): adjacent rank moves
s_i -> s_i+1 in the exponent representation (value = sum_i 2^{s_i} 3^{i-1}, s_1>...>s_l>=0).
Codex's own stated go/no-go: "Enumerate all local two-move diamonds. If they are confluent
[...], invoke the least-action formalism of abelian networks [...] If the diamond test fails,
this route should be abandoned."

Result: FAILS. In ~25% of random adjacent-rank pairs tested (4995/20000), the two orders of
applying "increment rank i" then "increment rank i+1" are not both legal or both illegal --
one order succeeds, the other doesn't, because incrementing the lower-index rank first frees
up room (moves it further from the higher-index rank) that the higher-index rank then needs
to increment into, but not vice versa. Concrete verified example: s=[11,10,6,5,4,2],
incrementing rank 2 (6->7) then rank 3 (5->6) succeeds; incrementing rank 3 first (5->6)
immediately collides with rank 2's unchanged value (6>=6, illegal).

Per Codex's own explicit condition, this closes item 6: the moves are not confluent, so the
abelian-networks / chip-firing reduction does not apply as proposed.
"""
import random


def legal_increment(s, i, maxexp):
    news = s[:]
    news[i] += 1
    if i == 0:
        if news[i] > maxexp:
            return None
    else:
        if news[i] >= s[i - 1]:
            return None
    return news


def run(n_trials=20000, seed=1):
    random.seed(seed)
    both_legal = 0
    order_dependent = 0
    example = None
    for _ in range(n_trials):
        l = random.randint(3, 8)
        maxexp = l + random.randint(2, 10)
        s = sorted(random.sample(range(0, maxexp + 1), l), reverse=True)
        i = random.randint(0, l - 2)
        j = i + 1

        sA1 = legal_increment(s, i, maxexp)
        legalA2 = sA1 is not None and legal_increment(sA1, j, maxexp) is not None

        sB1 = legal_increment(s, j, maxexp)
        legalB2 = sB1 is not None and legal_increment(sB1, i, maxexp) is not None

        if legalA2 and legalB2:
            both_legal += 1
        if legalA2 != legalB2 and example is None:
            example = (s, i, j, maxexp, legalA2, legalB2)
        if legalA2 != legalB2:
            order_dependent += 1

    return dict(trials=n_trials, both_legal=both_legal, order_dependent=order_dependent,
                example=example)


if __name__ == "__main__":
    r = run()
    print(f"trials={r['trials']} both_orders_legal={r['both_legal']} "
          f"order_dependent={r['order_dependent']}")
    print("example:", r["example"])
