#!/usr/bin/env python3


def parse_input():
    with open("./input") as f:
        entries = []
        for line in f.readlines():
            patterns, outvals = line.split("|")
            entries.append((patterns.strip().split(), outvals.strip().split()))

        return entries


def part1(entries):
    ans = 0
    for entry in entries:
        for outval in entry[1]:
            if len(outval) in [2, 3, 4, 7]:
                ans += 1

    return ans


def part2(entries):
    ans = 0
    result = [set() for i in range(10)]

    for entry in entries:
        patterns = entry[0]

        five_segments = []
        six_segments = []
        for pat in patterns:
            match len(pat):
                case 2: result[1] = set(pat)
                case 3: result[7] = set(pat)
                case 4: result[4] = set(pat)
                case 7: result[8] = set(pat)
                case 5: five_segments.append(set(pat))
                case 6: six_segments.append(set(pat))

        for s in six_segments:
            if not result[1].issubset(s):
                result[6] = set(s)
            elif result[4].issubset(s):
                result[9] = set(s)
            else:
                result[0] = set(s)

        for fs in five_segments:
            if result[1].issubset(fs):
                result[3] = set(fs)
            elif not set(fs).issubset(result[9]):
                result[2] = set(fs)
            else:
                result[5] = set(fs)

        outputs = [set(vals) for vals in entry[1]]

        output_str = ""
        for outval in outputs:
            for n, s in enumerate(result):
                if s == outval:
                    output_str += str(n)

        ans += int(output_str)

    return ans


if __name__ == "__main__":
    entries = parse_input()

    print(f"part1: {part1(entries)}")
    print(f"part2: {part2(entries)}")
