#!/usr/bin/env python3

MAX_TIMER_VAL = 8


def parse_input():
    with open("./input") as f:
        data = [(int(s)) for s in f.read().strip().split(",")]
        initial_state = [0] * (MAX_TIMER_VAL + 1)
        for timer in data:
            initial_state[timer] += 1

        return initial_state


def solve(initial_state, days):
    state = list(initial_state)
    for _ in range(days):
        new_spawns = state[0]
        for i in range(1, MAX_TIMER_VAL + 1):
            state[i-1] = state[i]
        state[6] += new_spawns
        state[8] = new_spawns

    return sum(state)


if __name__ == "__main__":
    initial_state = parse_input()

    print(f"part1: {solve(initial_state, days=80)}")
    print(f"part2: {solve(initial_state, days=256)}")
