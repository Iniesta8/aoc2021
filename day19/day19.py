#!/usr/bin/env python3


from dataclasses import dataclass, field
from itertools import combinations


def parse_input():
    with open("./input") as f:
        data = f.read().split("\n\n")
    scanners = []
    for i, b in enumerate(data):
        s = Scanner(i)
        for l in b.split("\n"):
            if l.startswith("---"):
                continue
            s.add_beacon(tuple(int(c) for c in l.split(",")))
        scanners.append(s)

    return scanners


@dataclass
class Scanner:
    num: int
    pos: tuple() = None
    beacons: set() = field(default_factory=set)

    def add_beacon(self, new_beacon):
        self.beacons.add(new_beacon)

    def __str__(self):
        return f"--- scanner {self.num} ----\n" + \
            "\n".join(str(b) for b in self.beacons) + "\n"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.num) + hash(sum([hash(b) for b in self.beacons])) \
            + hash(self.pos)

    def rotate_x(self):
        s = Scanner(self.num)
        for beacon in self.beacons:
            x, y, z = beacon
            s.add_beacon((x, -z, y))
        return s

    def rotate_y(self):
        s = Scanner(self.num)
        for beacon in self.beacons:
            x, y, z = beacon
            s.add_beacon((z, y, -x))
        return s

    def rotate_z(self):
        s = Scanner(self.num)
        for beacon in self.beacons:
            x, y, z = beacon
            s.add_beacon((y, -x, z))
        return s


def calc_manhattan_distance(a, b):
    return sum(abs(ai - bi) for ai, bi, in zip(a, b))


def calc_direction(a, b):
    return (b[0] - a[0], b[1] - a[1], b[2] - a[2])


def get_directions(scanner: Scanner):
    dirs = {}
    for ba in scanner.beacons:
        for bb in scanner.beacons:
            if ba == bb:
                continue
            dirs[calc_direction(ba, bb)] = ba

    return dirs


def get_orientations(scanner: Scanner):
    scanner_orientations = set()

    scanner_orientations.add(scanner)
    old_length = len(scanner_orientations)
    length = 0

    while True:
        for ori in set(scanner_orientations):
            scanner_orientations.add(ori.rotate_x())
            scanner_orientations.add(ori.rotate_y())
            scanner_orientations.add(ori.rotate_z())

        length = len(scanner_orientations)
        if length == old_length:
            break

        old_length = length

    return scanner_orientations


def __common_beacons(a, b):
    dirs_a = get_directions(a)
    dirs_b = get_directions(b)

    common_beacons = set()
    for dir_a, ba in dirs_a.items():
        if dir_a in dirs_b:
            common_beacons.add((ba, dirs_b[dir_a]))

    return common_beacons


def get_common_beacons(fixed_scanner, scanner):
    for ori in get_orientations(scanner):
        common_beacons = __common_beacons(fixed_scanner, ori)
        if len(common_beacons) >= 12:
            return (ori, common_beacons)


def solve(scanners):
    scanners[0].pos = (0, 0, 0)
    fixed_scanners = [scanners[0]]
    not_fixed_scanners = scanners[1:]

    while len(not_fixed_scanners) > 0:
        new_known_scanner = None
        remove_scanner = None

        for not_fixed_scanner in not_fixed_scanners:
            for fixed_scanner in fixed_scanners:
                overlap_info = get_common_beacons(
                    fixed_scanner, not_fixed_scanner)
                if overlap_info:
                    ori, common_beacons = overlap_info
                    print(
                        f"Known scanner {fixed_scanner.num:>2} and scanner {not_fixed_scanner.num}")
                    fixed_pos, new_pos = common_beacons.pop()
                    shift = calc_direction(fixed_pos, new_pos)
                    remove_scanner = not_fixed_scanner
                    new_known_scanner = Scanner(not_fixed_scanner.num, shift)
                    new_known_scanner.beacons = set(
                        [calc_direction(shift, b) for b in ori.beacons])
                    break

        if new_known_scanner:
            print(
                f"Position of scanner {new_known_scanner.num} detected: {new_known_scanner.pos}")
            fixed_scanners.append(new_known_scanner)
        if remove_scanner:
            not_fixed_scanners.remove(remove_scanner)

    beacons = set()
    for fixed_scanner in fixed_scanners:
        print(
            f"Position of scanner {fixed_scanner.num} is {fixed_scanner.pos}")
        beacons |= fixed_scanner.beacons

    max_distance = 0
    for (a, b) in combinations(fixed_scanners, 2):
        max_distance = max(max_distance, calc_manhattan_distance(a.pos, b.pos))

    return len(beacons), max_distance


if __name__ == "__main__":
    scanners = parse_input()

    num_beacons, max_scanner_distance = solve(scanners)

    print(f"part1: {num_beacons}")
    print(f"part2: {max_scanner_distance}")
