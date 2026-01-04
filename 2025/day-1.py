# Author: Nick Quinn
# Description: Solution for day 1 of 2025 Advent of Code
# Problem Link: https://adventofcode.com/2025/day/1
# Interpreter: Python 3.14

from _helper_methods import read_puzzle_input
from icecream import ic

real_input, test_input = read_puzzle_input("1")


def main(input):
    location = 50
    result = 0

    for instruct in input.values():
        distance_to_move = int(instruct[1:])

        # L moves dial to lower numbers
        if instruct.startswith("L"):
            distance_to_move *= -1

        location = (location + distance_to_move) % 100
        if location == 0:
            result += 1

    return result


test_result = main(test_input)
expected_result = 3
assert (
    main(test_input) == expected_result
), f"Expected {test_result} to be {expected_result}"

ic(f"Answer: {main(real_input)}")
