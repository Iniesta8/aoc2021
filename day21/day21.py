#!/usr/bin/env python3


from functools import lru_cache
from itertools import product
from copy import deepcopy
from dataclasses import dataclass


def parse_input():
    with open("./input") as f:
        return [Player(pos=int(p_info.split()[-1]))
                for p_info in f.read().splitlines()]


@dataclass
class Player:
    pos: int
    score: int = 0

    def move(self, rolled):
        self.pos = (self.pos + rolled - 1) % 10 + 1
        self.score += self.pos


@dataclass
class DeterministicDice:
    max_val: int
    val: int = 0
    roll_count: int = 0

    def roll(self):
        self.val = (self.val + 1 - 1) % self.max_val + 1
        self.roll_count += 1
        return self.val


def part1(players):
    dice = DeterministicDice(100)
    turn = 0

    while True:
        player = players[turn]
        rolled = sum(dice.roll() for _ in range(3))
        player.move(rolled)
        if player.score >= 1000:
            return dice.roll_count * players[1 - turn].score
        turn = 1 - turn


def part2(players):

    @lru_cache(maxsize=None)
    def count_wins(positions, scores=(0, 0), turn=0):
        new_positions, new_scores = list(positions), list(scores)
        wins = [0, 0]
        for rolls in product((1, 2, 3), repeat=3):
            rolled = sum(rolls)

            new_positions[turn] = (positions[turn] + rolled - 1) % 10 + 1
            new_scores[turn] = scores[turn] + new_positions[turn]

            if new_scores[turn] >= 21:
                wins[turn] += 1
            else:
                wins_p1, wins_p2 = count_wins(
                    tuple(new_positions), tuple(new_scores), 1 - turn)
                wins[0] += wins_p1
                wins[1] += wins_p2
        return wins

    return max(count_wins((players[0].pos, players[1].pos)))


if __name__ == "__main__":
    players = parse_input()

    print(f"part1: {part1(deepcopy(players))}")
    print(f"part2: {part2(players)}")
