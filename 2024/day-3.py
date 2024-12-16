# Author: Nick Quinn
# Description: Solution for day 3 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/3
# Interpreter: Python 3.12

import re
from icecream import ic

# TODO: The part 2 of this problem is not working properly. There appears to be an edge case that I'm missing,
#       but I'm not having a lot of fun trying to figure it out and decided to just move on. The method
#       parse_instructions_with_words() seems to be closer to the answer.

def parse_instructions(instructions: str) -> list[str]:
    # Look for patterns of "mul(123,123)". Numbers can be between 1 and 3 digits.
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

def remove_disabled_instructions(instructions: str) -> list[str]:
    disabled = "don\'t()"
    enabled = "do()"
    new_instructions = ""

    search = ""
    enable_instruction = True
    for c in instructions:
        search += c
        if search.endswith(disabled):
            enable_instruction = False
            new_instructions = new_instructions[:-6]

        if search.endswith(enabled):
            enable_instruction = True
            new_instructions += "do("

        if enable_instruction:
            new_instructions += c

    # i = 0
    # while True:
    #     next_disabled = instructions[i:].find(disabled)
    #     if next_disabled == -1:
    #         new_instructions += instructions[i:]
    #         break
    #
    #     next_enabled = instructions[next_disabled:].find(enabled)
    #     if next_enabled == -1:
    #         break
    #
    #     new_instructions += instructions[i:next_disabled]
    #     assert instructions[i:next_disabled].find(disabled) == -1
    #
    #     i += next_enabled + next_disabled
    #
    #     if i >= len(instructions):
    #         break

    return parse_instructions(new_instructions)


def parse_instructions_with_words(instructions: str) -> list[str]:
    # Look for patterns of "mul(123,123)". Numbers can be between 1 and 3 digits.
    pattern = r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))'
    result = re.findall(pattern, instructions)

    # Words include do() and don't(). If do(), then mul(X,Y) is enabled, otherwise it is disabled.
    result_without_words = []
    enabled = True
    for r in result:
        c = None
        # Loop through tuples and find index with a value
        for t in r:
            if t != '':
                assert c is None
                c = t
                break

        assert c is not None, ic(result)

        if c == 'don\'t()':
            enabled = False
        elif c == 'do()':
            enabled = True
        elif enabled:
            result_without_words.append(c)
        else:
            continue

    # ic(result_without_words)
    return result_without_words

def calculate_instructions(instructions: list[str]):
    result = 0
    for instruction in instructions:
        # Remove the non-number parts of the string
        instruction = instruction.replace("mul(", "").replace(")", "")
        first = int(instruction.split(",")[0])
        second = int(instruction.split(",")[1])
        result += first * second

    return result


def find_mul_instructions(file_name: str, is_part_one: bool) -> int:
    result = 0
    with open(file_name) as f:
        for line in f:
            instructions = line.strip()
            if is_part_one:
                instructions = parse_instructions(instructions)
            else:
                instructions = parse_instructions_with_words(instructions)

            result += calculate_instructions(instructions)

    return result


result = find_mul_instructions('day-3-test-input.txt', True)
print(f"TEST 1: {result}")
assert result == 161

result = find_mul_instructions('day-3-input.txt', True)
print(f"PART 1: {result}")
assert result == 160672468

result = find_mul_instructions('day-3-test-input-2.txt', False)
print(f"TEST 2: {result}")
assert result == 48

result = find_mul_instructions('day-3-input.txt', False)
print(f"PART 2: {result}")