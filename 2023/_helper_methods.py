# Author: Nick Quinn
# Description: Common methods that I've created to be used in the 2023 Advent of Code problems
# Link: https://adventofcode.com/2023/
# Interpreter: Python 3.12


def extract_numbers(s):
    nums = []
    num = ""
    for c in s:
        if c.isnumeric():
            num += c
        elif num != "":
            nums.append(int(num))
            num = ""

    # If number the last character in string
    if num.isnumeric():
        nums.append(int(num))

    return nums


def is_symbol(c):
    if not c.isnumeric() and c != ".":
        return True

    return False


def find_first_num(line):
    for char in line:
        if char.isnumeric():
            return int(char)

    raise ValueError(f"ERROR: No number in line {line}")


def find_last_num(line):
    index = -1
    end = len(line) * -1

    while index >= end:
        if line[index].isnumeric():
            return int(line[index])

        index = index - 1

    raise ValueError(f"ERROR: No number in line {line}")