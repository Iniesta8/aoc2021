#!/usr/bin/env python3


error_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

complete_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

char_map = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


def solve(lines):
    error_score = 0
    compl_scores = []
    for line in lines:
        corrupted = False
        score = 0
        stack = []
        for c in line:
            if c in char_map.values():
                stack.append(c)
            elif char_map[c] == stack[-1]:
                stack.pop()
            else:
                # corrupted line
                corrupted = True
                error_score += error_scores[c]
                break
        if not corrupted and len(stack) != 0:
            # incomplete line
            for c in reversed(stack):
                score = score * 5 + complete_scores[c]
            compl_scores.append(score)

    mid = int(len(compl_scores) / 2)
    return error_score, sorted(compl_scores)[mid]


if __name__ == "__main__":
    with open("./input") as f:
        lines = [line.strip() for line in f.readlines()]

        print(f"part1: {solve(lines)[0]}")
        print(f"part2: {solve(lines)[1]}")
