#!/usr/bin/env python3


from copy import deepcopy


def parse_input():
    with open("./input") as f:
        rows = f.readlines()
    return [[c for c in r.strip()] for r in rows]


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()


def step(grid):
    global N, M
    changed = False

    new_grid = deepcopy(grid)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '>':
                if grid[i][(j + 1) % M] == '.':
                    changed = True
                    new_grid[i][(j + 1) % M] = c
                    new_grid[i][j] = '.'

    final_grid = deepcopy(new_grid)
    for i, r in enumerate(new_grid):
        for j, c in enumerate(r):
            if c == 'v':
                if new_grid[(i + 1) % N][j] == '.':
                    changed = True
                    final_grid[(i + 1) % N][j] = c
                    final_grid[i][j] = '.'

    return changed, final_grid


def solve(grid):
    step_count = 0
    changed = True

    while changed:
        step_count += 1
        changed, grid = step(deepcopy(grid))

    return step_count


if __name__ == "__main__":
    grid = parse_input()

    N = len(grid)
    M = len(grid[0])

    print(f"part1: {solve(grid)}")
