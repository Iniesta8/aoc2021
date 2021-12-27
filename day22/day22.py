#!/usr/bin/env python3


def parse_reboot_step(reboot_step, bounds):
    new_state, coords = reboot_step.strip().split()
    xr, yr, zr = coords.split(",")
    xr, yr, zr = xr[2:], yr[2:], zr[2:]

    x1, x2 = (int(xi) for xi in xr.split(".."))
    y1, y2 = (int(yi) for yi in yr.split(".."))
    z1, z2 = (int(zi) for zi in zr.split(".."))

    if bounds:
        lb, ub = bounds

        if (x1 < lb and x2 < lb) or (x1 > ub and x2 > ub):
            return None
        x1, x2 = max(x1, lb), min(x2, ub)

        if (y1 < lb and y2 < lb) or (y1 > ub and y2 > ub):
            return None
        y1, y2 = max(y1, lb), min(y2, ub)

        if (z1 < lb and z2 < lb) or (z1 > ub and z2 > ub):
            return None
        z1, z2 = max(z1, lb), min(z2, ub)

    return x1, x2, y1, y2, z1, z2, new_state


def split_existing_cube(existing_cube, new_cube):
    new_cubes = []

    x1a, x2a, y1a, y2a, z1a, z2a, s = existing_cube
    x1b, x2b, y1b, y2b, z1b, z2b, _ = new_cube

    if x1a < x1b:
        new_cubes.append((x1a, x1b - 1, y1a, y2a, z1a, z2a, s))
        x1a = x1b
    if x2a > x2b:
        new_cubes.append((x2b + 1, x2a, y1a, y2a, z1a, z2a, s))
        x2a = x2b
    if y1a < y1b:
        new_cubes.append((x1a, x2a, y1a, y1b - 1, z1a, z2a, s))
        y1a = y1b
    if y2a > y2b:
        new_cubes.append((x1a, x2a, y2b + 1, y2a, z1a, z2a, s))
        y2a = y2b
    if z1a < z1b:
        new_cubes.append((x1a, x2a, y1a, y2a, z1a, z1b - 1, s))
        z1a = z1b
    if z2a > z2b:
        new_cubes.append((x1a, x2a, y1a, y2a, z2b + 1, z2a, s))
        z2a = z2b

    return new_cubes


def overlap(cube_a, cube_b):
    x1a, x2a, y1a, y2a, z1a, z2a, _ = cube_a
    x1b, x2b, y1b, y2b, z1b, z2b, _ = cube_b

    x_overlap = x2a >= x1b and x1a <= x2b
    y_overlap = y2a >= y1b and y1a <= y2b
    z_overlap = z2a >= z1b and z1a <= z2b

    return x_overlap and y_overlap and z_overlap


def count_cubes_by_state(cubes, state):
    count = 0
    for cube in cubes:
        x1, x2, y1, y2, z1, z2, s = cube
        if s == state:
            count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

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

            created_cubes = split_existing_cube(existing_cube, new_cube)
            new_cubes.extend(created_cubes)

        new_cubes.append(new_cube)
        cubes = new_cubes

    return count_cubes_by_state(cubes, "on")


def main():
    with open("./input") as f:
        reboot_steps = f.readlines()

    print(f"part1: {solve(reboot_steps, (-50, 50))}")
    print(f"part2: {solve(reboot_steps)}")


if __name__ == "__main__":
    main()
