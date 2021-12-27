#!/usr/bin/env python3

def parse_input():
    with open("./input") as f:
        return [(int(c)) for c in f.read().strip().split(",")]


def part1(init_pos):
    median = init_pos[len(init_pos)//2]

    return sum(abs(c - median) for c in init_pos)


def part2(init_pos):
    def calc_costs(src, dst):
        dist = abs(dst - src)
        return dist * (dist + 1) // 2

    best = 1e9
    for t in range(init_pos[0], init_pos[-1] + 1):
        costs = 0
        for c in init_pos:
            costs += calc_costs(c, t)
        if costs < best:
            best = costs

    return best


def main():
    init_pos = parse_input()
    init_pos.sort()

    print(f"part1: {part1(init_pos)}")
    print(f"part2: {part2(init_pos)}")


if __name__ == "__main__":
    main()
