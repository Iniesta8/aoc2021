#!/usr/bin/env python3


def parse_input():
    with open("./input") as f:
        return [(int(c)) for c in f.read().strip().split(",")]


def part1(init_pos):
    init_pos.sort()
    median = init_pos[len(init_pos)//2]

    return sum(abs(c - median) for c in init_pos)


def part2(init_pos):
    mean = sum(init_pos)//len(init_pos)

    def calc_costs(src, dst):
        dist = abs(dst - src)
        return sum(range(dist + 1))

    return sum(calc_costs(c, mean) for c in init_pos)


if __name__ == "__main__":
    init_pos = parse_input()

    print(f"part1: {part1(init_pos)}")
    print(f"part2: {part2(init_pos)}")
