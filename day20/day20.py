#!/usr/bin/env python3


from collections import defaultdict


def parse_input():
    with open("./input") as f:
        data = f.read().split("\n\n")
        algorithm = [c for c in data[0].strip()]

        input_image = defaultdict(lambda: '.')
        for i, l in enumerate(data[1].split("\n")):
            for j, c in enumerate(l.strip()):
                if c == '#':
                    input_image[(i, j)] = c

        return input_image, algorithm


def print_image(image):
    min_i = min(image, key=lambda p: p[0])[0]
    max_i = max(image, key=lambda p: p[0])[0]
    min_j = min(image, key=lambda p: p[1])[1]
    max_j = max(image, key=lambda p: p[1])[1]

    for ii in range(min_i, max_i + 1):
        for jj in range(min_j, max_j + 1):
            print(image[(ii, jj)], end="")
        print()


def get_output_pixel(input_image, algorithm, input_pixel):
    ix, ij = input_pixel

    index_str = ""
    for ii in [ix - 1, ix, ix + 1]:
        for jj in [ij - 1, ij, ij + 1]:
            index_str += '1' if input_image[(ii, jj)] == '#' else '0'

    index = int(index_str, 2)
    return algorithm[index]


def enhance_image(input_image, algorithm):
    new_image = input_image.copy()

    min_i = min(input_image, key=lambda p: p[0])[0] - 1
    max_i = max(input_image, key=lambda p: p[0])[0] + 1
    min_j = min(input_image, key=lambda p: p[1])[1] - 1
    max_j = max(input_image, key=lambda p: p[1])[1] + 1

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            output_pixel = get_output_pixel(input_image, algorithm, (i, j))
            new_image[(i, j)] = output_pixel

    if new_image.default_factory() == '.':
        new_image.default_factory = lambda: algorithm[0]
    else:
        new_image.default_factory = lambda: algorithm[-1]

    return new_image


def count_lit_pixels(image):
    return sum(1 for p in image.values() if p == '#')


def solve(image, algorithm, rounds):
    for _ in range(rounds):
        image = enhance_image(image, algorithm)

    return count_lit_pixels(image)


if __name__ == "__main__":
    input_image, algorithm = parse_input()

    print(f"part1: {solve(input_image, algorithm, 2)}")
    print(f"part2: {solve(input_image, algorithm, 50)}")
