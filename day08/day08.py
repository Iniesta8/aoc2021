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
    result = {}

    for entry in entries:
        patterns = [set(p) for p in entry[0]]
        outputs = [set(v) for v in entry[1]]

        five_segments = []
        six_segments = []
        for pat in patterns:
            match len(pat):
                case 2: result[1] = pat
                case 3: result[7] = pat
                case 4: result[4] = pat
                case 7: result[8] = pat
                case 5: five_segments.append(pat)
                case 6: six_segments.append(pat)

        for s in six_segments:
            if not result[1].issubset(s):
                result[6] = s
            elif result[4].issubset(s):
                result[9] = s
            else:
                result[0] = s

        for fs in five_segments:
            if result[1].issubset(fs):
                result[3] = fs
            elif not fs.issubset(result[9]):
                result[2] = fs
            else:
                result[5] = fs

        output = 0
        for outval in outputs:
            for n, s in result.items():
                if s == outval:
                    output = output * 10 + n

        ans += output

    return ans


if __name__ == "__main__":
    entries = parse_input()

    print(f"part1: {part1(entries)}")
    print(f"part2: {part2(entries)}")
