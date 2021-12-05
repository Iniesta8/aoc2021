#!/usr/bin/env python3


def parse_input():
    with open("./input") as f:
        lines = [l.strip() for l in f.readlines()]

        coords = []
        for line in lines:
            src, dst = line.split("->")
            x1, y1 = src.strip().split(",")
            x2, y2 = dst.strip().split(",")
            coords.append([[int(x1), int(y1)], [int(x2), int(y2)]])

        return coords


def get_covered_points_count(coords, part1):
    cps = dict()

    for coord in coords:
        src = coord[0]
        dst = coord[1]

        dv = [dst[0] - src[0], dst[1] - src[1]]

        if part1 and dv[0] != 0 and dv[1] != 0:
            continue

        ndv = [0 if dv[0] == 0 else int(dv[0] /
                                        abs(dv[0])), 0 if dv[1] == 0 else int(dv[1] / abs(dv[1]))]

        n = abs(dv[0]) if dv[0] != 0 else abs(dv[1])
        tmp = list(src)
        while n >= 0:
            tmp_key = (tmp[0], tmp[1])
            if tmp_key not in cps:
                cps[tmp_key] = 1
            else:
                cps[tmp_key] += 1
            tmp[0] += ndv[0]
            tmp[1] += ndv[1]
            n -= 1

    return cps


def solve(coords, p1):
    cps = get_covered_points_count(coords, p1)

    ans = 0
    for c in cps.values():
        if c >= 2:
            ans += 1

    return ans


if __name__ == "__main__":
    coords = parse_input()

    print(f"part1: {solve(coords, True)}")
    print(f"part2: {solve(coords, False)}")
