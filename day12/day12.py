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
    ans = 0
    stack = list([("start", set(["start"]), "")])

    while stack:
        cave, visited_smalls, twice_small = stack.pop()
        if cave == "end":
            ans += 1
            continue
        for next_cave in graph[cave]:
            if next_cave not in visited_smalls:
                new_smalls = set(visited_smalls)
                if next_cave.islower():
                    new_smalls.add(next_cave)
                stack.append((next_cave, new_smalls, twice_small))
            elif next_cave in visited_smalls:
                if p2:
                    if next_cave not in ["start", "end"] and twice_small == "":
                        stack.append((next_cave, visited_smalls, next_cave))
                else:
                    continue

    return ans


def main():
    graph = parse_data()

    print(f"part1: {solve(graph, False)}")
    print(f"part2: {solve(graph, True)}")


if __name__ == "__main__":
    main()
