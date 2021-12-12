#!/usr/bin/env python3


from collections import defaultdict


def parse_data():
    graph = defaultdict(set)

    with open("./input") as f:
        for line in f.readlines():
            src, dst = line.strip().split("-")
            graph[src].add(dst)
            graph[dst].add(src)

        return graph


def solve(graph, p2):
    def dfs(graph, path, visited_caves, next_cave,
            possible_paths, p2, twice_small=""):
        if next_cave == "end":
            path.append(next_cave)
            visited_caves.add(next_cave)
            possible_paths.append(path)
            return
        if next_cave in visited_caves and next_cave.islower():
            if p2:
                if next_cave == "start":
                    return
                if twice_small == "":
                    twice_small = next_cave
                else:
                    return
            else:
                return

        path.append(next_cave)
        visited_caves.add(next_cave)
        for next in graph[next_cave]:
            dfs(graph, list(path), set(visited_caves),
                next, possible_paths, p2, twice_small)

    possible_paths = []
    dfs(graph, [],  set(), "start", possible_paths, p2)

    return len(possible_paths)


if __name__ == "__main__":
    graph = parse_data()

    print(f"part1: {solve(graph, False)}")
    print(f"part2: {solve(graph, True)}")
