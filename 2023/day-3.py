# Author: Nick Quinn
# Description: Solution for day 3 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/3
# Interpreter: Python 3.12

from _helper_methods import is_symbol

global GEARS
GEARS = {}


def main():
    global GEARS

    lines = test_data.splitlines()
    num_positions = create_mapping(lines)
    sum = find_nums_near_symbols(num_positions, lines)
    print(f"TEST 1: {sum}")

    result = 0
    for key, value in GEARS.items():
        if value["count"] == 2:
            result += value["num"]

    print(f"TEST 2: {result}")

    GEARS = {}

    lines = open("day-3-input.txt", "r").read().splitlines()
    num_positions = create_mapping(lines)
    sum = find_nums_near_symbols(num_positions, lines)
    print(f"PART 1: {sum}")

    result = 0
    for key, value in GEARS.items():
        if value["count"] == 2:
            result += value["num"]

    print(f"PART 2: {result}")


def check_if_gear(lines, i, j, num):
    if lines[i][j] == "*":
        key = f"{i}{j}"

        if key in GEARS:
            GEARS[key]["num"] *= num
            GEARS[key]["count"] += 1
        else:
            GEARS[key] = {"num": num, "count": 1}


def find_nums_near_symbols(num_positions, lines):
    sum = 0
    lines_len = len(lines)
    for num in num_positions:
        for i in range(num["line"] - 1, num["line"] + 2):
            if i >= 0 and i < lines_len:
                for j in range(num["first"] - 1, num["last"] + 2):
                    if j >= 0 and j < len(lines[num["line"]]):
                        if is_symbol(lines[i][j]):
                            sum += int(num["num"])
                            check_if_gear(lines, i, j, int(num["num"]))

                            break

    return sum


def create_mapping(data):
    num_positions = []

    for i, line in enumerate(data):
        num = ""
        start = -1
        num_found = False
        for j, c in enumerate(line):
            if c.isnumeric():
                num += c
                if start == -1:
                    start = j
                num_found = True
                if j == len(line) - 1:
                    num_positions.append(
                        {"line": i, "first": start, "last": j - 1, "num": num}
                    )
            else:
                if num_found:
                    end = j - 1
                    num_found = False
                    num_positions.append(
                        {"line": i, "first": start, "last": end, "num": num}
                    )
                    start = -1
                    num = ""
                else:
                    continue

    return num_positions


test_data = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

if __name__ == "__main__":
    main()