# Author: Nick Quinn
# Description: Solution for day 1 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/1
# Interpreter: Python 3.12

def parse_ids(file_name) -> (list, list):
    # Parse input
    left_ids = []
    right_ids = []
    with open(file_name) as f:
        for line in f:
            ids = line.strip().split("   ")
            left_ids.append(int(ids[0]))
            right_ids.append(int(ids[1]))

    return left_ids, right_ids

def calculate_total_distance(file_name) -> int:
    left_ids, right_ids = parse_ids(file_name)

    # Sort Lists
    left_ids.sort()
    right_ids.sort()

    total_distance = 0
    for left_id, right_id in zip(left_ids, right_ids):
        total_distance += abs(left_id - right_id)

    return total_distance

def calculate_similarity(file_name) -> int:
    left_ids, right_ids = parse_ids(file_name)

    total_similarity = 0
    for left_id in left_ids:
        similarity = 0
        for right_id in right_ids:
            if left_id == right_id:
                similarity += 1

        total_similarity += (left_id * similarity)

    return total_similarity

test_distance = calculate_total_distance('day-1-test-input.txt')
print(f"TEST 1: {test_distance}")
assert test_distance == 11

total_distance = calculate_total_distance('day-1-input.txt')
print(f"PART 1: {total_distance}")
assert total_distance == 1197984

test_similarity = calculate_similarity('day-1-test-input.txt')
print(f"TEST 2: {test_similarity}")
assert test_similarity == 31

test_similarity = calculate_similarity('day-1-input.txt')
print(f"PART 2: {test_similarity}")
assert test_similarity == 23387399