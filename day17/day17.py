#!/usr/bin/env python3

def parse_input():
    with open("./input") as f:
        data = f.read().strip().split(": ")
        xrange, yrange = data[1].split(", ")

        x1, x2 = (int(x) for x in xrange[2:].split(".."))
        y1, y2 = (int(y) for y in yrange[2:].split(".."))

        return x1, x2, y1, y2


def step(pos, velocity):
    x, y = pos
    vx, vy = velocity

    x += vx
    y += vy

    if vx != 0:
        vx += (-1) if x > 0 else 1
    vy -= 1

    return x, y, (vx, vy)


def simulate(init_pos, init_velocity, target_area):
    t_x1, t_x2, t_y1, t_y2 = target_area
    pos_x, pos_y = init_pos
    velocity = init_velocity
    highest_y = pos_y

    while True:
        pos_x, pos_y, velocity = step((pos_x, pos_y), velocity)
        if pos_y > highest_y:
            highest_y = pos_y

        if t_x1 <= pos_x <= t_x2 and t_y1 <= pos_y <= t_y2:
            # in target area
            return (pos_x, pos_y), init_velocity, highest_y
        if pos_x > t_x2 or pos_y < t_y1:
            return None


def solve(target_area):
    results = []
    _, t_x2, t_y1, _ = target_area

    for vx in range(t_x2 + 1):
        for vy in range(t_y1 - 1, -t_y1 + 1):
            res = simulate((0, 0), (vx, vy), target_area)
            if res:
                results.append(res)

    highest_y = max(results, key=lambda res: res[2])[2]

    return highest_y, len(results)


if __name__ == "__main__":
    target_area = parse_input()

    print(f"part1: {solve(target_area)[0]}")
    print(f"part2: {solve(target_area)[1]}")
