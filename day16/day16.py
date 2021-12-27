#!/usr/bin/env python3


import math


def parse_input():
    with open("./input") as f:
        data = ""
        for c in f.read().strip():
            data += f'{int(c, 16):0>4b}'
        return data


class BITS_Decoder:
    def __init__(self, data):
        self.data = data
        self.rp = 0
        self.version_sum = 0

    def fetch(self, n):
        fetched = self.data[self.rp:self.rp + n]
        self.rp += n
        return fetched

    def decode_packet(self):
        while self.rp < len(self.data):
            self.version_sum += int(self.fetch(3), 2)
            type_id = int(self.fetch(3), 2)
            if type_id == 4:
                return self.decode_literal_value()
            return self.decode_operator(type_id)

    def decode_literal_value(self):
        val = ""
        last_part = False
        while not last_part:
            if self.fetch(1) == '0':
                last_part = True
            val += self.fetch(4)
        return int(val, 2)

    def decode_operator(self, type_id):
        subpacket_results = []
        length_type_id = self.fetch(1)

        # decode sub-packets
        if length_type_id == '0':
            len_subpackets = int(self.fetch(15), 2)
            end = self.rp + len_subpackets
            while self.rp < end:
                subpacket_results.append(self.decode_packet())
        else:
            num_subpackets = int(self.fetch(11), 2)
            packet_count = 0
            while packet_count < num_subpackets:
                subpacket_results.append(self.decode_packet())
                packet_count += 1

        match type_id:
            case 0: return sum(subpacket_results)
            case 1: return math.prod(subpacket_results)
            case 2: return min(subpacket_results)
            case 3: return max(subpacket_results)
            case 5: return subpacket_results[0] > subpacket_results[1]
            case 6: return subpacket_results[0] < subpacket_results[1]
            case 7: return subpacket_results[0] == subpacket_results[1]


def decode_transmission(data):
    decoder = BITS_Decoder(data)
    val = decoder.decode_packet()
    return decoder.version_sum, val


def main():
    data = parse_input()

    print(f"part1: {decode_transmission(data)[0]}")
    print(f"part2: {decode_transmission(data)[1]}")


if __name__ == "__main__":
    main()
