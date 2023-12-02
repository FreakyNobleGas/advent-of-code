# Author: Nick Quinn
# Description: Solution for day 1 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/1
# Interpreter: Python 3.12

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    test()

    data = open("day-1-input.txt", "r").read()
    vals = calculate_calibration_vals(data)

    result = 0
    for val in vals:
        result += val

    print(result)


def all_digits():
    all = []
    for key, value in DIGITS.items():
        all.extend([key, value])

    return all


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


def find_all_numbers(line):
    first_digit_index = -1
    first_digit = None
    for digit in all_digits():
        index = line.find(str(digit))
        if index == -1:
            continue

        if first_digit_index == -1 or index < first_digit_index:
            first_digit = digit
            first_digit_index = index

    last_digit_index = -1
    last_digit = None
    for digit in all_digits():
        index = line.rfind(str(digit))
        if index == -1:
            continue

        if last_digit_index == -1 or index > last_digit_index:
            last_digit = digit
            last_digit_index = index

    if isinstance(first_digit, str):
        first_digit = DIGITS[first_digit]

    if isinstance(last_digit, str):
        last_digit = DIGITS[last_digit]

    return combine_digits(first_digit, last_digit)


def combine_digits(first, last):
    return (first * 10) + last


def calculate_calibration_vals(data, part_one = False):
    lines = data.split("\n")
    vals = []

    for line in lines:
        if len(line.strip()) > 0:
            if part_one:
                first = find_first_num(line)
                last = find_last_num(line)
                val = combine_digits(first, last)

                vals.append(val)
            else:
                vals.append(find_all_numbers(line))

    return vals


# Tests
test_data = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet\
"""


def test_assertion(name, result, expect):
    assert result == expect, f"{name} should be {expect}, but is {result}"


def test():
    name = "find_first_num"
    test_assertion(name, find_first_num("treb7uchet"), 7)
    test_assertion(name, find_first_num("pqr3stu8vwx"), 3)
    test_assertion(name, find_first_num("1abc2"), 1)
    test_assertion(name, find_first_num("3fiveone"), 3)

    name = "find_last_num"
    test_assertion(name, find_last_num("treb7uchet"), 7)
    test_assertion(name, find_last_num("pqr3stu8vwx"), 8)
    test_assertion(name, find_last_num("1abc2"), 2)
    test_assertion(name, find_last_num("3fiveone"), 3)

    name = "combine_digits"
    test_assertion(name, combine_digits(8, 7), 87)
    test_assertion(name, combine_digits(7, 7), 77)

    name = "calculate_calibration_vals"
    test_assertion(name, calculate_calibration_vals(test_data, True), [12, 38, 15, 77])

    name = "find_all_numbers"
    test_assertion(name, find_all_numbers("xtwone3four"), 24)
    test_assertion(name, find_all_numbers("zoneight234"), 14)
    test_assertion(name, find_all_numbers("4nineeightseven2"), 42)


if __name__ == "__main__":
    main()
