#!/usr/bin/env python3


def parse_reboot_step(reboot_step, bounds):
    new_state, coords = reboot_step.strip().split()
    xr, yr, zr = coords.split(",")
    xr, yr, zr = xr[2:], yr[2:], zr[2:]

    xl, xh = (int(xi) for xi in xr.split(".."))
    yl, yh = (int(yi) for yi in yr.split(".."))
    zl, zh = (int(zi) for zi in zr.split(".."))

    if bounds:
        lb, ub = bounds

        if (xl < lb and xh < lb) or (xl > ub and xh > ub):
            return None
        xl = max(xl, lb)
        xh = min(xh, ub)

        if (yl < lb and yh < lb) or (yl > ub and yh > ub):
            return None
        yl = max(yl, lb)
        yh = min(yh, ub)

        if (zl < lb and zh < lb) or (zl > ub and zh > ub):
            return None
        zl = max(zl, lb)
        zh = min(zh, ub)

    return xl, xh, yl, yh, zl, zh, new_state


def split_cube(existing_cube, intersect):
    new_cubes = []

    xlc, xhc, ylc, yhc, zlc, zhc, sc = existing_cube
    xli, xhi, yli, yhi, zli, zhi, _ = intersect

    if xlc < xli:
        new_cube = (xlc, xli - 1, ylc, yhc, zlc, zhc, sc)
        xlc = xli
        new_cubes.append(new_cube)
    if xhc > xhi:
        new_cube = (xhi + 1, xhc, ylc, yhc, zlc, zhc, sc)
        xhc = xhi
        new_cubes.append(new_cube)
    if ylc < yli:
        new_cube = (xlc, xhc, ylc, yli - 1, zlc, zhc, sc)
        ylc = yli
        new_cubes.append(new_cube)
    if yhc > yhi:
        new_cube = (xlc, xhc, yhi + 1, yhc, zlc, zhc, sc)
        yhc = yhi
        new_cubes.append(new_cube)
    if zlc < zli:
        new_cube = (xlc, xhc, ylc, yhc, zlc, zli - 1, sc)
        zlc = zli
        new_cubes.append(new_cube)
    if zhc > zhi:
        new_cube = (xlc, xhc, ylc, yhc, zhi + 1, zhc, sc)
        zhc = zhi
        new_cubes.append(new_cube)

    return new_cubes


def overlap(a, b):
    xla, xha, yla, yha, zla, zha, _ = a
    xlb, xhb, ylb, yhb, zlb, zhb, _ = b

    x_overlap = xha >= xlb and xla <= xhb
    y_overlap = yha >= ylb and yla <= yhb
    z_overlap = zha >= zlb and zla <= zhb

    return x_overlap and y_overlap and z_overlap


def count_cubes_by_state(cubes, state):
    count = 0
    for cube in cubes:
        xlc, xhc, ylc, yhc, zlc, zhc, sc = cube
        if sc == state:
            count += (xhc - xlc + 1) * (yhc - ylc + 1) * (zhc - zlc + 1)

    return count


def solve(reboot_steps, bounds=None):
    cubes = []

    for step in reboot_steps:
        new_cube = parse_reboot_step(step, bounds)
        if not new_cube:
            continue

        if len(cubes) == 0:
            cubes.append(new_cube)
            continue

        new_cubes = []
        for existing_cube in cubes:
            if not overlap(existing_cube, new_cube):
                new_cubes.append(existing_cube)
                continue

            created_cubes = split_cube(existing_cube, new_cube)
            new_cubes.extend(created_cubes)

        new_cubes.append(new_cube)
        cubes = new_cubes

    return count_cubes_by_state(cubes, "on")


if __name__ == "__main__":
    with open("./input") as f:
        reboot_steps = f.readlines()

    print(f"part1: {solve(reboot_steps, (-50, 50))}")
    print(f"part2: {solve(reboot_steps)}")
