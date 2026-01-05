# Author: Nick Quinn
# Description: Common methods that I've created to be used in the 2025 Advent of Code problems
# Link: https://adventofcode.com/2025/
# Interpreter: Python 3.12


from typing import Callable, Iterable, Tuple, Dict


def read_file(file_name: str) -> dict:
    puzzle = {}
    with open(file_name) as f:
        for i, l in enumerate(f):
            puzzle[i] = l.strip()

    return puzzle


def read_puzzle_input(day: str) -> Tuple[Dict[str, str], Dict[str, str]]:
    return read_file(f"day-{day}-input.txt"), read_file(f"day-{day}-test-input.txt")


def run_test(input: Iterable[str], expected_result: int, func: Callable):
    test_result = func(input)
    assert (
        test_result == expected_result
    ), f"Expected {test_result} to be {expected_result}"
