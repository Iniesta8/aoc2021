#!/usr/bin/env python3

from functools import cache


def parse_input():
    with open("./input") as f:
        lines = f.readlines()

    instruction_blocks = []
    new_block = []
    for line in lines:
        instr = line.strip().split(" ")
        if instr[0] == "inp":
            if len(new_block) > 0:
                instruction_blocks.append(new_block)
            new_block = []
        else:
            new_block.append(instr)

    instruction_blocks.append(new_block)
    return instruction_blocks


def process(instr_idx, w, z):
    variables = [w, 0, 0, z]
    var_indices = "wxyz"

    for instr in instructions[instr_idx]:
        op, a, b = instr
        var_idx = var_indices.index(a)

        b_val = variables[var_indices.index(b)] if b.isalpha() else int(b)

        match op:
            case "add":
                variables[var_idx] += b_val
            case "mul":
                variables[var_idx] *= b_val
            case "div":
                assert b_val != 0
                variables[var_idx] = int(variables[var_idx] / b_val)
            case "mod":
                assert variables[var_idx] >= 0 and b_val > 0
                variables[var_idx] = variables[var_idx] % b_val
            case "eql":
                variables[var_idx] = 1 if variables[var_idx] == b_val else 0

    return variables[var_indices.index("z")]


min_model_num = ""
max_model_num = ""


def part1():
    @cache
    def find_model_num(idx, cur_z):
        if cur_z >= 1000000:
            return False

        global max_model_num
        if idx == len(instructions):
            if cur_z == 0:
                return True
            return False

        for w in range(9, 0, -1):
            max_model_num += str(w)
            if find_model_num(idx + 1, process(idx, w, cur_z)):
                return True
            max_model_num = max_model_num[:-1]
        return False

    find_model_num(0, 0)


def part2():
    @cache
    def find_model_num(idx, cur_z):
        if cur_z >= 1000000:
            return False

        global min_model_num
        if idx == len(instructions):
            if cur_z == 0:
                return True
            return False

        for w in range(1, 10):
            min_model_num += str(w)
            if find_model_num(idx + 1, process(idx, w, cur_z)):
                return True
            min_model_num = min_model_num[:-1]
        return False

    find_model_num(0, 0)


if __name__ == "__main__":
    instructions = parse_input()

    part1()
    part2()

    print(f"part1: {max_model_num}")
    print(f"part2: {min_model_num}")
