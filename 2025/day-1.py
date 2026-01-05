# Author: Nick Quinn
# Description: Solution for day 1 of 2025 Advent of Code
# Problem Link: https://adventofcode.com/2025/day/1
# Interpreter: Python 3.14

from _helper_methods import read_puzzle_input, run_test
from icecream import ic
from typing import Iterable

real_input, test_input = read_puzzle_input("1")
real_input, test_input = real_input.values(), test_input.values()


def main_part_1(input: Iterable[str]) -> int:
    location = 50
    result = 0

    for instruct in input:
        distance_to_move = int(instruct[1:])

        # L moves dial to lower numbers
        if instruct.startswith("L"):
            distance_to_move *= -1

        location = (location + distance_to_move) % 100
        if location == 0:
            result += 1

    return result


def main_part_2(input: Iterable[str]) -> int:
    location = 50
    result = 0

    for instruct in input:
        distance_to_move = int(instruct[1:])

        if distance_to_move > 100:
            result += int(distance_to_move / 100)
            distance_to_move %= 100

        # L moves dial to lower numbers
        if instruct.startswith("L"):
            distance_to_move *= -1

        old_location = location
        location += distance_to_move

        if old_location != 0:
            if location < 0 or location > 100:
                result += 1

        location %= 100

        if location == 0:
            result += 1

    return result


#
# PART 1
#
test_result = main_part_1(test_input)
expected_result = 3
assert (
    main_part_1(test_input) == expected_result
), f"Expected {test_result} to be {expected_result}"

ic(f"Answer Part 1: {main_part_1(real_input)}")

#
# PART 2
#


def run_test_part_2(input: list, expected_result: int):
    test_result = main_part_2(input)
    assert (
        test_result == expected_result
    ), f"Expected {test_result} to be {expected_result}"


run_test(test_input, 6, main_part_2)
run_test(["L51"], 1, main_part_2)
run_test(["L51", "R1"], 2, main_part_2)
run_test(["L50", "L99", "L1"], 2, main_part_2)

ic(f"Answer Part 2: {main_part_2(real_input)}")
