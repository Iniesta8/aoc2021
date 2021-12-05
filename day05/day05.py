#!/usr/bin/env python3


def parse_input():
    with open("./input") as f:
        data = [l.strip() for l in f.readlines()]

        lines = []
        for line in data:
            src, dst = line.split("->")
            x1, y1 = src.strip().split(",")
            x2, y2 = dst.strip().split(",")
            lines.append([[int(x1), int(y1)], [int(x2), int(y2)]])

        return lines


def get_covered_points_count(lines, diagonals):
    cpc = dict()

    for l in lines:
        src, dst = l[0], l[1]
        dv_x, dv_y = [dst[0] - src[0], dst[1] - src[1]]

        if diagonals and dv_x != 0 and dv_y != 0:
            continue

        sv_x = 0 if dv_x == 0 else int(dv_x / abs(dv_x))
        sv_y = 0 if dv_y == 0 else int(dv_y / abs(dv_y))
        n = abs(dv_x) if dv_x != 0 else abs(dv_y)
        tmp_x, tmp_y = list(src)
        while n >= 0:
            tmp = (tmp_x, tmp_y)
            cpc[tmp] = cpc.get(tmp, 0) + 1
            tmp_x += sv_x
            tmp_y += sv_y
            n -= 1

    return cpc


def solve(lines, diagonals):
    cpc = get_covered_points_count(lines, diagonals)
    return len([c for c in cpc.values() if c >= 2])


if __name__ == "__main__":
    lines = parse_input()

    print(f"part1: {solve(lines, diagonals=True)}")
    print(f"part2: {solve(lines, diagonals=False)}")
