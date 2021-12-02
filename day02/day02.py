#!/usr/bin/env python3


def part1(commands):
    hpos = 0
    depth = 0
    for c in commands:
        val = int(c[1])
        dir = c[0]

        if dir == "forward":
            hpos += val
        elif dir == "down":
            depth += val
        elif dir == "up":
            depth -= val

    return hpos * depth


def part2(commands):
    hpos = 0
    depth = 0
    aim = 0
    for c in commands:
        val = int(c[1])
        dir = c[0]

        if dir == "forward":
            hpos += val
            depth += aim * val
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val

    return hpos * depth


if __name__ == "__main__":
    with open("./input") as f:
        commands = [list(l.strip().split(" ")) for l in f.readlines()]

    print(f"part1: {part1(commands)}")
    print(f"part2: {part2(commands)}")
