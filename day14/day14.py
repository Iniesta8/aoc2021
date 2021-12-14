#!/usr/bin/env python3


from collections import Counter


def parse_input():
    with open("./input") as f:
        template, rules_raw = f.read().split("\n\n")
        rules = {}
        for rule in rules_raw.split("\n"):
            l, r = rule.split("->")
            rules[l.strip()] = r.strip()

        return template, rules


def step(rules, char_counter, pair_counter):
    for p, c in Counter(pair_counter).items():
        if c > 0 and p in rules:
            lp = p[0] + rules[p]
            rp = rules[p] + p[1]

            pair_counter[p] -= c
            pair_counter[lp] += c
            pair_counter[rp] += c
            char_counter[rules[p]] += c

    return char_counter, pair_counter


def solve(template, rules, rounds):
    char_counter = Counter(template)
    pair_counter = Counter([template[i:i+2]
                            for i in range(len(template) + 1)])
    for _ in range(rounds):
        char_counter, pair_counter = step(rules, char_counter, pair_counter)

    mc = char_counter.most_common(1)
    lc = char_counter.most_common()[:-2:-1]

    return mc[0][1] - lc[0][1]


if __name__ == "__main__":
    template, rules = parse_input()

    print(f"part1: {solve(template, rules, 10)}")
    print(f"part2: {solve(template, rules, 40)}")
