# Author: Nick Quinn
# Description: Solution for day 5 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/5
# Interpreter: Python 3.12


def main():
    data = parse_data(test_data.splitlines())
    smallest_location = find_smallest_location(data)
    print(f"PART 1 TEST: {smallest_location}")

    data = parse_data(open("day-5-input.txt", "r").read().splitlines())
    smallest_location = find_smallest_location(data)
    print(f"PART 1: {smallest_location}")

    # NOTE: Part 2 isn't completed. It's currently implemented with a brute force
    # approach that takes too long to complete and also gives the incorrect answer
    # for the real input case.
    data = parse_data(test_data.splitlines())
    data = transform_from_pairs(data)
    smallest_location = find_smallest_location(data)
    print(f"PART 2 TEST: {smallest_location}")

    data = parse_data(open("day-5-input.txt", "r").read().splitlines())
    data = transform_from_pairs(data)
    smallest_location = find_smallest_location(data)
    print(f"PART 2: {smallest_location}")


def transform_from_pairs(data):
    seeds = data.get("seeds")[0]
    smallest_number = None

    curr_seed = None
    total_seeds = 0
    for i, s in enumerate(seeds):
        if i % 2 == 0:
            curr_seed = s
        else:
            print(f"ADDING RANGE FROM {curr_seed} to {curr_seed + s}")
            for j in range(curr_seed, curr_seed + s):
                total_seeds += 1

    curr_seed = None
    count = 0
    for i, s in enumerate(seeds):
        if i % 2 == 0:
            curr_seed = s
        else:
            for j in range(curr_seed, curr_seed + s):
                seed = j
                smallest_number = find_new_location_for_seed(
                    seed, smallest_number, data
                )
                count += 1
                print(
                    f"Progress {count / total_seeds}% COUNT: {count}, TOTAL: {total_seeds}"
                )

    return data


def calculate_movement(position, rows):
    location = position
    for row in rows:
        dest = row[0]
        start = row[1]
        range = row[2]

        if start <= position <= start + range:
            location = (dest - start) + position
            break

    return location


def find_new_location_for_seed(seed, smallest_number, data):
    position = seed
    for key in data.keys():
        if key != "seeds":
            position = calculate_movement(position, data.get(key))

    if smallest_number is None or position < smallest_number:
        smallest_number = position

    return smallest_number


def find_smallest_location(data):
    smallest_number = None

    for seed in data["seeds"][0]:
        smallest_number = find_new_location_for_seed(seed, smallest_number, data)

    return smallest_number


def parse_data(data):
    result = {
        "seeds": [],
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    curr_key = None
    for line in data:
        key = line.split(" ")[0].split(":")[0]
        if result.get(key) is not None:
            curr_key = key

        if curr_key is not None:
            tokens = line.split(" ")
            col_nums = []
            for token in tokens:
                if token.isnumeric():
                    col_nums.append(int(token))

            if col_nums:
                result[curr_key].append(col_nums)

    return result


"""
Maps:
1st Column -> Dest Start
2nd Column -> Source Start
3rd Column -> Range for both column 1 & 2

seed soil
79   81
14   14
55   57
13   13
"""

test_data = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

if __name__ == "__main__":
    main()