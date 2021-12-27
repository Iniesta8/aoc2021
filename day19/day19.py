#!/usr/bin/env python3


from dataclasses import dataclass, field
from itertools import combinations
from functools import lru_cache


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
    directions: dict() = None

    def add_beacon(self, new_beacon):
        self.beacons.add(new_beacon)

    def __str__(self):
        return f"--- scanner {self.num} ----\n" + \
            "\n".join(str(b) for b in self.beacons) + "\n"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.num)

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

    def get_directions(self):
        if self.directions:
            return self.directions
        dirs = {}
        for ba in self.beacons:
            for bb in self.beacons:
                if ba == bb:
                    continue
                dirs[calc_direction(ba, bb)] = ba
        self.directions = dirs
        return dirs

    @lru_cache
    def get_orientations(self):
        scanner_orientations = set()

        scanner_orientations.add(self)
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

    def get_common_beacons(self, other):
        for ori in other.get_orientations():
            dirs_a = self.get_directions()
            dirs_b = ori.get_directions()

            common_beacons = set()
            for dir_a, ba in dirs_a.items():
                if dir_a in dirs_b:
                    common_beacons.add((ba, dirs_b[dir_a]))

            if len(common_beacons) >= 12:
                return (ori, common_beacons)

    def calc_manhattan_distance(self, other):
        return sum(abs(ai - bi) for ai, bi, in zip(self.pos, other.pos))


@lru_cache
def calc_direction(a, b):
    return (b[0] - a[0], b[1] - a[1], b[2] - a[2])


def solve(scanners):
    scanners[0].pos = (0, 0, 0)
    fixed_scanners = [scanners[0]]
    not_fixed_scanners = scanners[1:]

    while len(not_fixed_scanners) > 0:
        new_fixed_scanner = None
        remove_scanner = None

        for not_fixed_scanner in not_fixed_scanners:
            for fixed_scanner in fixed_scanners:
                overlap_info = fixed_scanner.get_common_beacons(
                    not_fixed_scanner)
                if overlap_info:
                    ori, common_beacons = overlap_info
                    print(
                        f"Scanner {fixed_scanner.num} and scanner" \
                        f"{not_fixed_scanner.num} have overlapping beacons")
                    fixed_pos, new_pos = common_beacons.pop()
                    shift = calc_direction(fixed_pos, new_pos)
                    remove_scanner = not_fixed_scanner
                    new_fixed_scanner = Scanner(not_fixed_scanner.num, shift)
                    new_fixed_scanner.beacons = set(
                        calc_direction(shift, b) for b in ori.beacons)
                    break

        if new_fixed_scanner:
            print(
                f"Position of scanner {new_fixed_scanner.num} detected")
            fixed_scanners.append(new_fixed_scanner)
        if remove_scanner:
            not_fixed_scanners.remove(remove_scanner)

    print("\nFinal scanner positions:")
    beacons = set()
    for fixed_scanner in fixed_scanners:
        print(
            f"Scanner {fixed_scanner.num:>2}: {fixed_scanner.pos}")
        beacons |= fixed_scanner.beacons
    print()

    max_distance = max(a.calc_manhattan_distance(b)
                       for (a, b) in combinations(fixed_scanners, 2))

    return len(beacons), max_distance


def main():
    scanners = parse_input()

    num_beacons, max_scanner_distance = solve(scanners)

    print(f"part1: {num_beacons}")
    print(f"part2: {max_scanner_distance}")


if __name__ == "__main__":
    main()
