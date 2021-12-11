#!/usr/bin/env python3


from copy import deepcopy


adj_coords = [(-1, 0), (-1, -1), (0, -1), (1, -1),
              (1, 0), (1, 1), (0, 1), (-1, 1)]


def step(grid):
    flashed = set()
    to_flash = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                to_flash.append((i, j))

    while len(to_flash) > 0:
        octo = to_flash.pop()
        for adj in adj_coords:
            ii, ji = octo[0] + adj[0], octo[1] + adj[1]
            if ii < 0 or ii > (len(grid)-1) or ji < 0 or ji > (len(grid[0]) - 1):
                continue

            if (ii, ji) not in to_flash and (ii, ji) not in flashed:
                grid[ii][ji] += 1

                if grid[ii][ji] > 9:
                    to_flash.append((ii, ji))

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
