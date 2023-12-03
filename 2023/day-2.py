# Author: Nick Quinn
# Description: Solution for day 2 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/2
# Interpreter: Python 3.12

import re


def main():
    bag = {"red": 12, "green": 13, "blue": 14}

    result = parse_part_one_data(test_data, bag)
    assert result == 8, f"PART 1: Test scenario should have been 8, but is {result}"
    print("TEST DONE\n")

    data = open("day-2-input.txt", "r").read()
    result = parse_part_one_data(data, bag)
    print(f"PART ONE: {result}")

    result = parse_part_two_data(test_data)
    assert (
            result == 2286
    ), f"PART 2: Test scenario should have been 2286, but is {result}"
    print("TEST DONE\n")

    data = open("day-2-input.txt", "r").read()
    result = parse_part_two_data(data)
    print(f"PART TWO: {result}")


def parse_part_two_data(data):
    total_power = 0

    data = data.split("\n")
    for line in data:
        line = line.replace(" ", "").lower()
        highest_num_cubes = {"red": 1, "blue": 1, "green": 1}

        rounds = line.split(":")[1].split(";")
        for round in rounds:
            cubes_drawn = round.split(",")
            for cubes in cubes_drawn:
                num_of_cubes = int(re.findall("[0-9]+", cubes)[0])
                color = determine_color(cubes)

                if num_of_cubes > highest_num_cubes[color]:
                    highest_num_cubes[color] = num_of_cubes

        total_power += (
                highest_num_cubes["red"]
                * highest_num_cubes["blue"]
                * highest_num_cubes["green"]
        )

    return total_power


def parse_part_one_data(data, bag):
    id_total = 0

    data = data.split("\n")
    for line in data:
        line = line.replace(" ", "").lower()
        game = line.split(":")[0]
        id = int(re.findall("[0-9]+", game)[0])
        possible = {"red": True, "blue": True, "green": True}

        rounds = line.split(":")[1].split(";")
        for round in rounds:
            cubes_drawn = round.split(",")
            for cubes in cubes_drawn:
                num_of_cubes = int(re.findall("[0-9]+", cubes)[0])
                color = determine_color(cubes)

                if num_of_cubes > bag[color]:
                    possible[color] = False

        if False not in possible.values():
            id_total = id_total + id

    return id_total


def determine_color(cubes):
    colors = ["blue", "red", "green"]
    for color in colors:
        if cubes.find(color) > -1:
            return color

    raise ValueError(f"ERROR: No colors found in string {cubes}!")


test_data = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\
"""

if __name__ == "__main__":
    main()