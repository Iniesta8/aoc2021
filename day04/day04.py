#!/usr/bin/env python3


def parse_input():
    boards = []
    with open("./input") as f:
        numbers = [int(n) for n in f.readline().strip().split(',')]
        lines = [line.strip() for line in f if line != '\n']

        count = 0
        board = []
        for l in lines:
            row = [int(r) for r in l.split()]

            board.append(row)
            count += 1

            if count == len(row):
                boards.append(board)
                count = 0
                board = []

    return numbers, boards


def print_board(board):
    for row in board:
        print(row)


def board_won(board):
    for row in board:
        if all([e == 'X' for e in row]):
            return True

    for j in range(0, len(board[0])):
        if all([row[j] == 'X' for row in board]):
            return True

    return False


def calc_score(board, winning_num):
    score = 0

    for row in board:
        for e in row:
            if e != 'X':
                score += e

    return score * winning_num


def mark_number(board, num):
    for i, row in enumerate(board):
        for j, e in enumerate(row):
            if e == num:
                board[i][j] = 'X'


def part1(boards, nums):
    for cur_num in nums:
        for b in boards:
            mark_number(b, cur_num)

            if board_won(b):
                return calc_score(b, cur_num)


def part2(boards, nums):
    won_boards = set()

    for cur_num in nums:
        for i, b in enumerate(boards):

            if i in won_boards:
                continue

            mark_number(b, cur_num)

            if board_won(b):
                won_boards.add(i)
                if len(won_boards) == len(boards):
                    return calc_score(b, cur_num)


if __name__ == "__main__":
    nums, boards = parse_input()

    print(f"part1: {part1(boards, nums)}")
    print(f"part2: {part2(boards, nums)}")
