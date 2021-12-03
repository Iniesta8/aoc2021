#!/usr/bin/env python3


def create_filter(data, what, when_even):
    n = len(data)
    ones = [0] * len(data[0])

    for e in data:
        for i, b in enumerate(e):
            if b == '1':
                ones[i] += 1

    f = ""
    for c in ones:
        if c > n/2:
            f += '1' if what == "most" else '0'
        elif c == n/2:
            f += when_even
        else:
            f += '0' if what == "most" else '1'

    return f


def part1(data):
    mc = create_filter(data, "most", "1")
    gamma = int(mc, 2)

    epsilon = ''.join(['1' if i == '0' else '0'
                       for i in mc])

    epsilon = int(epsilon, 2)

    return gamma * epsilon


def part2(data):
    oxy_data = list(data)
    co2_data = list(data)

    for i in range(len(data[0])):
        mcf = create_filter(oxy_data, "most", '1')
        oxy_data = [d for d in oxy_data if d[i] == mcf[i]]
        if len(oxy_data) == 1:
            break

    oxygen = int(oxy_data[0], 2)

    for i in range(len(data[0])):
        lcf = create_filter(co2_data, "least", '0')
        co2_data = [d for d in co2_data if d[i] == lcf[i]]
        if len(co2_data) == 1:
            break

    co2 = int(co2_data[0], 2)

    return oxygen * co2


if __name__ == "__main__":
    with open("./input") as f:
        data = [l.strip() for l in f.readlines()]

    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")
