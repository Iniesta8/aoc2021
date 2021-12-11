#!/usr/bin/env python3


from copy import deepcopy


adj_coords = [(-1, 0), (-1, -1), (0, -1), (1, -1),
              (1, 0), (1, 1), (0, 1), (-1, 1)]


def step(grid):
    flashed = set()
    to_flash = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                to_flash.append((x, y))

    while len(to_flash) > 0:
        octo = to_flash.pop()
        for adj in adj_coords:
            xi, yi = octo[0] + adj[0], octo[1] + adj[1]
            if xi < 0 or xi > (len(grid[0])-1) or yi < 0 or yi > (len(grid) - 1):
                continue

            if (xi, yi) not in to_flash and (xi, yi) not in flashed:
                grid[xi][yi] += 1

                if grid[xi][yi] > 9:
                    to_flash.append((xi, yi))

        grid[octo[0]][octo[1]] = 0
        flashed.add((octo[0], octo[1]))

    return grid, len(flashed)


def part1(grid):
    total_flashes = 0
    for _ in range(100):
        grid, flashes = step(grid)
        total_flashes += flashes

    return total_flashes


def part2(grid):
    step_count = 0
    flashes = 0
    while flashes != len(grid) * len(grid[0]):
        step_count += 1
        grid, flashes = step(grid)

    return step_count


if __name__ == "__main__":
    with open("./input") as f:
        grid = [[int(level) for level in line.strip()]
                for line in f.readlines()]

        print(f"part1: {part1(deepcopy(grid))}")
        print(f"part2: {part2(grid)}")
