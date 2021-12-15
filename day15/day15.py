#!/usr/bin/env python3

import heapq


def parse_input():
    with open("./input") as f:
        grid = [[int(level) for level in line.strip()]
                for line in f.readlines()]

        return grid


def solve(grid, n):
    N = len(grid)
    M = len(grid[0])
    rows = N * n
    cols = M * n

    costs = {}
    pq = [(0, 0, 0)]
    visited = set()

    def get_cost(r, c):
        return ((grid[r % N][c % M] + (r // N) + (c // M)) - 1) % 9 + 1

    while pq:
        cost, r, c = heapq.heappop(pq)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        costs[(r, c)] = cost

        if (r, c) == (rows - 1,  cols - 1):
            # distination reached
            break

        for (dr, dc) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            rr, cc = r + dr, c + dc
            if not (0 <= rr < rows and 0 <= cc < cols):
                continue
            heapq.heappush(pq, (cost + get_cost(rr, cc), rr, cc))

    return costs[(rows - 1, cols - 1)]


if __name__ == "__main__":
    grid = parse_input()

    print(f"part1: {solve(grid, 1)}")
    print(f"part2: {solve(grid, 5)}")
