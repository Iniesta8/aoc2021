#!/usr/bin/env python3

import math

adj_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_input():
    with open("./input") as f:
        floor = {}
        for y, line in enumerate(f.readlines()):
            for x, h in enumerate(line.strip()):
                floor[(x, y)] = int(h)

        return floor


def get_low_points(floor):
    low_points = []
    for p, h in floor.items():
        if h == 0:
            low_points.append(p)
            continue
        if h == 9:
            continue
        found_new = True
        for d in adj_dirs:
            adj_coords = (p[0] + d[0], p[1] + d[1])
            if adj_coords in floor:
                if floor[adj_coords] < h:
                    found_new = False
                    break
        if found_new:
            low_points.append(p)

    return low_points


def get_basin(floor, lp, basin):
    if lp not in floor:
        return set()
    if floor[lp] == 9:
        return set()

    basin.add(lp)
    for d in adj_dirs:
        adj_coords = (lp[0] + d[0], lp[1] + d[1])
        if adj_coords not in basin:
            basin |= get_basin(floor, adj_coords, basin)

    return basin


def part1(floor):
    low_points = get_low_points(floor)
    return sum([floor[h] + 1 for h in low_points])


def part2(floor):
    low_points = get_low_points(floor)
    basin_sizes = [len(get_basin(floor, lp, basin=set()))
                   for lp in low_points]

    return math.prod(sorted(basin_sizes)[-3:])


if __name__ == "__main__":
    floor = parse_input()

    print(f"part1: {part1(floor)}")
    print(f"part2: {part2(floor)}")
