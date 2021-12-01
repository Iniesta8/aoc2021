#!/usr/bin/env python3


def solve(depths, wsize):
    ans = 0
    l = 1
    last = sum(depths[0:wsize])

    for r in range(wsize, len(depths)):
        next_win = last - depths[l-1] + depths[r]
        if next_win > last:
            ans += 1
        last = next_win
        l += 1

    return ans


if __name__ == "__main__":
    with open("./input") as f:
        depths = [int(d) for d in f.readlines()]

    print(f"part1: {solve(depths, 1)}")
    print(f"part2: {solve(depths, 3)}")
