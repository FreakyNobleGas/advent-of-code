# Author: Nick Quinn
# Description: Solution for day 8 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/8
# Interpreter: Python 3.12

"""
NOTES:
    - A frequency is denoted by being an alphanumerical character. Both lower and upper case.
    - An anti-node is denoted by #
    - A # occurs at any point that is perfectly in line with two antennas of the same frequency, but only when one of
      the antennas is twice as far away as the other
    - # can overlap with another frequency
"""

from icecream import ic
from collections import defaultdict
import math
from _helper_methods import read_puzzle_input


puzzle_input, puzzle_test_input = read_puzzle_input("8")

"""
    TODO:
        - Build dictionary of coordinates
        - Create function that determines slope between coordinates
        - Create function that predicts # and checks if they are in bounds
        - Create a function that determines the position of the anti-node based on the slope and distance
"""

def is_freq(c: str) -> bool:
    if c.isnumeric() or c.isalpha():
        return True
    return False

def build_coord_map(puzzle_input: dict) -> dict:
    new_dict = lambda: {"freq": [], "anti_node": []}
    freq_map = defaultdict(new_dict)

    for k, v in puzzle_input.items():
        for i, c in enumerate(v):
            c = str(c)
            if is_freq(c):
                freq_map[c]["freq"].append((k, i))

    freq_map["bounds"] = (len(puzzle_input[0]), len(puzzle_input.keys()))

    return freq_map

def calculate_slope(coord_1: tuple, coord_2: tuple) -> tuple:
    x1, y1 = coord_1
    x2, y2 = coord_2

    # return (y2 - y1) / (x2 - x1)
    return x1 - x2, y1 - y2

def calculate_distance(coord_1: tuple, coord_2: tuple) -> tuple:
    # Use the distance formula
    x1, y1 = coord_1
    x2, y2 = coord_2

    # return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return abs(x2 - x1), abs(y2 - y1)

def find_anti_node(coord: tuple, slope: tuple) -> tuple:
    x, y = coord

    # Since the second coord will be in the same direction as the slope, we'll want to go
    # the opposite way
    x_slope = slope[0] * -1
    y_slope = slope[1] * -1

    return x + x_slope, y + y_slope

def find_anti_nodes(freq_map: dict) -> dict:
    for freq in freq_map.keys():
        if freq == "bounds":
            continue

        # Compare each coord to each other.
        for coord1 in freq_map[freq]["freq"]:
            for coord2 in freq_map[freq]["freq"]:
                distance = calculate_distance(coord1, coord2)
                slope = calculate_slope(coord1, coord2)

                node = find_anti_node(coord1, slope)

                freq_map[freq]["anti_node"].append(node)

        freq_map[freq]["anti_node"] = list(set(freq_map[freq]["anti_node"]))

    return freq_map

def print_map(freq_map: dict) -> None:
    coords = []
    for freq in freq_map.keys():
        if freq == "bounds":
            continue

        coords += freq_map[freq]["freq"]
        coords += freq_map[freq]["anti_node"]

    for row in range(0, freq_map["bounds"][1]):
        line = ""
        for col in range(0, freq_map["bounds"][0]):
            c = (row, col)

            if c in coords:
                line += str(c)
            else:
                line += "."
        ic(line)

    ic(coords)


#
# Tests
#
valid_freqs = ["A", "b", "5"]
for f in valid_freqs:
    assert is_freq(f) == True

invalid_freqs = [".", "#", "!"]
for f in invalid_freqs:
    assert is_freq(f) == False

test_coord_map_input = {
    0: "..1",
    1: "A.."
}
expected_coord_map_output = {
    "1": { "freq": [(0,2)], "anti_node": [] },
    "A": { "freq": [(1,0)], "anti_node": [] },
    "bounds": (3,2)
}

assert build_coord_map(test_coord_map_input) == expected_coord_map_output

coord_1 = (1,3)
coord_2 = (2,6)
# assert calculate_slope(coord_1, coord_2) == 3
assert calculate_slope(coord_1, coord_2) == (-1, -3)

# assert calculate_distance(coord_1, coord_2) == math.sqrt(10)
assert calculate_distance(coord_1, coord_2) == (1, 3)

#
# Run Puzzle Inputs
#
freq_map = build_coord_map(puzzle_test_input)
freq_map = find_anti_nodes(freq_map)
ic(freq_map)
print_map(freq_map)