#!/usr/bin/env python3


def parse_data():
    with open("./input") as f:
        raw_points, raw_folds = f.read().split("\n\n")

        points = set()
        for p in raw_points.split("\n"):
            x, y = p.strip().split(",")
            points.add((int(x), int(y)))

        folds = []
        for f in raw_folds.strip().split("\n"):
            fold_along = f.strip().split()[-1]
            t, pos = fold_along.split("=")
            folds.append((t, int(pos)))

        return points, folds


def find_pos_after_fold(point, fold):
    line = fold[1]
    x, y = point
    if fold[0] == "x":  # fold left
        if x < line:
            return point
        x = 2 * line - x
        return x, y

    # else fold up
    if y < line:
        return point
    y = 2 * line - y
    return x, y


def do_fold(points, fold):
    new_points = set()
    for p in points:
        np = find_pos_after_fold(p, fold)
        new_points.add(np)

    return new_points


def print_points(points):
    max_x = max(points, key=lambda item: item[0])[0]
    max_y = max(points, key=lambda item: item[1])[1]

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part1(points, folds):
    return len(do_fold(points, folds[0]))


def part2(points, folds):
    new_points = points
    for f in folds:
        new_points = do_fold(new_points, f)

    print_points(new_points)


def main():
    points, folds = parse_data()

    print(f"part1: {part1(points, folds)}")
    print("part2:")
    part2(points, folds)


if __name__ == "__main__":
    main()
