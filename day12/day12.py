#!/usr/bin/env python3


from collections import defaultdict


def parse_data():
    graph = defaultdict(list)

    with open("./input") as f:
        for line in f.readlines():
            src, dst = line.strip().split("-")
            graph[src].append(dst)
            graph[dst].append(src)

        return graph


def solve(graph, p2):
    sum = 0
    stack = list([("start", set(["start"]), "")])

    while stack:
        cave, visited_smalls, twice_small = stack.pop()
        if cave == "end":
            sum += 1
            continue
        for next in graph[cave]:
            if next not in visited_smalls:
                new_smalls = set(visited_smalls)
                if next.islower():
                    new_smalls.add(next)
                stack.append((next, new_smalls, twice_small))
            elif next in visited_smalls:
                if p2:
                    if next not in ["start", "end"] and twice_small == "":
                        stack.append((next, visited_smalls, next))
                else:
                    continue

    return sum


if __name__ == "__main__":
    graph = parse_data()

    print(f"part1: {solve(graph, False)}")
    print(f"part2: {solve(graph, True)}")
