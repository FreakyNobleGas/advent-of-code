# Author: Nick Quinn
# Description: Solution for day 3 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/3
# Interpreter: Python 3.12

import re

def parse_instructions(instructions: str) -> list[str]:
    # Look for patterns of "mul(123,123)". Numbers can be between 1 and 3 digits.
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

def calculate_instructions(instructions: list[str]):
    result = 0
    for instruction in instructions:
        # Remove the non-number parts of the string
        instruction = instruction.replace("mul(", "").replace(")", "")
        first = int(instruction.split(",")[0])
        second = int(instruction.split(",")[1])
        result += first * second

    return result

def find_mul_instructions(file_name) -> int:
    result = 0
    with open(file_name) as f:
        for line in f:
            instructions = line.strip()
            instructions = parse_instructions(instructions)
            result += calculate_instructions(instructions)

    return result


result = find_mul_instructions('day-3-test-input.txt')
print(f"TEST 1: {result}")
assert result == 161

result = find_mul_instructions('day-3-input.txt')
print(f"PART 1: {result}")
assert result == 160672468