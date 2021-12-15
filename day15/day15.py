#!/usr/bin/env python3

import heapq

adj_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def parse_input():
    with open("./input") as f:
        grid = [[int(level) for level in line.strip()]
                for line in f.readlines()]

        return grid


def solve(grid, n):
    rows = len(grid) * n
    cols = len(grid[0]) * n

    acc_risks = [[None for _ in range(cols)]
                 for _ in range(rows)]
    queue = [(0, (0, 0))]

    while queue:
        acc_risk, (r, c) = heapq.heappop(queue)

        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        val = grid[r % len(grid)][c % len(grid)] + \
            r // len(grid) + c // len(grid[0])
        while val > 9:
            val -= 9
        new_risk = acc_risk + val

        if acc_risks[r][c] is None or new_risk < acc_risks[r][c]:
            acc_risks[r][c] = new_risk
        else:
            continue

        if (r, c) == (rows - 1,  cols - 1):
            # distination reached
            break

        for adj in adj_dirs:
            rr, cc = r + adj[0], c + adj[1]
            heapq.heappush(queue, (acc_risks[r][c], (rr, cc)))

    return acc_risks[rows - 1][cols - 1] - grid[0][0]


if __name__ == "__main__":
    grid = parse_input()

    print(f"part1: {solve(grid, 1)}")
    print(f"part2: {solve(grid, 5)}")
