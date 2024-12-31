# Author: Nick Quinn
# Description: Solution for day 7 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/7
# Interpreter: Python 3.12
import numbers

from icecream import ic
from itertools import permutations, combinations_with_replacement, combinations

def parse_file(file_name: str) -> dict:
    equations = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip().split(":")
            result = int(line[0])
            numbers = [int(n) for n in line[1].strip().split(" ")]
            equations[result] = numbers

    return equations

def calculate_line(line: list, line_result: int) -> int:
    if len(line) == 1:
        return line[0]

    line_sum = line[0]
    last_operator = line[1]
    for i, c in enumerate(line[2:]):
        if c == "*" or c == "+":
            last_operator = c
            continue

        if last_operator == "+":
            line_sum += c

        if last_operator == "*":
            line_sum *= c

        if line_sum > line_result:
            return line_sum

    return line_sum

def is_valid(equation_result: int, numbers: list) -> bool:
    # NOTE: While this works, it's very inefficient for large datasets.
    perms = combinations_with_replacement("+*", len(numbers) - 1)
    all_perms = []
    for p in perms:
        more_perms = set(permutations(p, len(p)))
        for mp in more_perms:
            all_perms.append(mp)

    for n in range(0, len(numbers) * 2 - 1):
        if n % 2 != 0:
            numbers.insert(n, "+")

    for operators in all_perms:
        operators = list(operators)
        last_operator = 0
        for i, n in enumerate(numbers):
            if i % 2 != 0:
                numbers[i] = operators[last_operator]
                last_operator += 1

        if calculate_line(numbers, equation_result) == equation_result:
            return True

    return False

def find_sum_of_valid_equations(filename: str) -> int:
    equations = parse_file(filename)

    valid_sum = 0
    for i, equation_result in enumerate(equations):
        if is_valid(equation_result, equations[equation_result]):
            valid_sum += equation_result

        print(f"Finished {i} / {len(equations)} equations")

    return valid_sum

# Tests
test, expected_result = [1, "+", 1, "*", 2], 4
result = calculate_line(test, 4)
assert result == expected_result, f"Expected result to be {expected_result}, but got {result}"

result = find_sum_of_valid_equations("day-7-test-input.txt")
print(f"TEST 1: {result}")
assert(result == 3749)

result = find_sum_of_valid_equations("day-7-input.txt")
print(f"PART 1: {result}")