#!/usr/bin/env python3


def part1(commands):
    hpos = 0
    depth = 0
    for c in commands:
        val = int(c[1])
        d = c[0]

        if d == "forward":
            hpos += val
        elif d == "down":
            depth += val
        elif d == "up":
            depth -= val

    return hpos * depth


def part2(commands):
    hpos = 0
    depth = 0
    aim = 0
    for c in commands:
        val = int(c[1])
        d = c[0]

        if d == "forward":
            hpos += val
            depth += aim * val
        elif d == "down":
            aim += val
        elif d == "up":
            aim -= val

    return hpos * depth


def main():
    with open("./input") as f:
        commands = [list(l.strip().split(" ")) for l in f.readlines()]

    print(f"part1: {part1(commands)}")
    print(f"part2: {part2(commands)}")


if __name__ == "__main__":
    main()
