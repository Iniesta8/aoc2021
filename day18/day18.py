#!/usr/bin/env python3

from itertools import permutations


def parse_input():
    with open("./input") as f:
        return [eval(l.strip()) for l in f.readlines()]


def sum_lhs(num, val):
    return num + val if isinstance(num, int) else [num[0], sum_lhs(num[1], val)]


def sum_rhs(num, val):
    return num + val if isinstance(num, int) else [sum_rhs(num[0], val), num[1]]


def try_explode(num, depth):
    if not isinstance(num, list):
        return False, num, 0, 0
    if depth >= 4:
        return True, 0, num[0], num[1]

    exploded, next_num, l, r = try_explode(num[0], depth + 1)
    if exploded:
        new_num = [next_num, sum_rhs(num[1], r)]
        return True, new_num, l, 0

    exploded, next_num, l, r = try_explode(num[1], depth + 1)
    if exploded:
        new_num = [sum_lhs(num[0], l), next_num]
        return True, new_num, 0, r

    return False, num, 0, 0


def try_split(num):
    if isinstance(num, int):
        if num >= 10:
            return [num//2, (num + 1)//2]
        else:
            return num

    left = try_split(num[0])
    if left != num[0]:
        return [left, num[1]]

    right = try_split(num[1])
    return [num[0], right]


def reduce(num):
    while True:
        exploded, num, _, _ = try_explode(num, 0)
        if exploded:
            continue
        prev_num = num
        num = try_split(num)
        if prev_num == num:
            break
    return num


def add(left, right):
    return reduce([left, right])


def magnitude(num):
    if isinstance(num, int):
        return num
    l, r = num[0], num[1]
    return 3 * magnitude(l) + 2 * magnitude(r)


def part1(nums):
    n = nums[0]
    for m in nums[1:]:
        n = add(n, m)
    return magnitude(n)


def part2(nums):
    return max((magnitude(add(a, b)) for a, b in permutations(nums, 2)))


if __name__ == "__main__":
    numbers = parse_input()

    print(f"part1: {part1(numbers)}")
    print(f"part2: {part2(numbers)}")
