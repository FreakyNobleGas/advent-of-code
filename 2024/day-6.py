# Author: Nick Quinn
# Description: Solution for day 6 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/6
# Interpreter: Python 3.12

from icecream import ic

def generate_map(filename: str) -> dict:
    patrol_map = {}
    guard = ['v', '^', '<', '>']
    patrol_map['in_bounds'] = True
    with open(filename) as f:
        for row_index, line in enumerate(f):
            line = line.strip()
            patrol_map[row_index] = []
            for col_index, c in enumerate(line):
                patrol_map[row_index].append(c)

                if c in guard:
                    patrol_map['starting_pos'] = (row_index, col_index)
                    patrol_map['cur_loc'] = patrol_map['starting_pos']
                patrol_map['col_bounds'] = col_index

            patrol_map['row_bounds'] = row_index

    return patrol_map

def next_location(patrol_map: dict) -> dict:
    cur_loc = patrol_map['cur_loc']
    row = cur_loc[0]
    col = cur_loc[1]
    guard_dir = patrol_map[row][col]

    # Update the current location based on the direction the guard is facing
    # Moving Up
    if guard_dir == '^':
        next_loc = (row - 1, col)
        next_dir = '>'
    # Moving Right
    elif guard_dir == ">":
        next_loc = (row, col + 1)
        next_dir = 'v'
    # Moving Left
    elif guard_dir == "<":
        next_loc = (row, col - 1)
        next_dir = '^'
    # Moving Down
    else:
        next_loc = (row + 1, col)
        next_dir = '<'

    # Check for out of bounds (upper limit)
    if next_loc[0] > patrol_map['col_bounds'] or next_loc[1] > patrol_map['row_bounds']:
        patrol_map['in_bounds'] = False
        patrol_map[row][col] = 'x'

    # Check for out of bounds (lower limit)
    elif next_loc[0] < 0 or next_loc[1] < 0:
        patrol_map['in_bounds'] = False
        patrol_map[row][col] = 'x'

    # Replace old guard location with x and new loc with the same direction.
    elif patrol_map[next_loc[0]][next_loc[1]] != '#':
        patrol_map[next_loc[0]][next_loc[1]] = guard_dir
        patrol_map['cur_loc'] = next_loc
        patrol_map[row][col] = 'x'

    # Check if obstruction is in new location. If yes, then turn 90 degrees and update guard_dir.
    else:
        patrol_map[row][col] = next_dir

    return patrol_map


    # return distance moved
def predict_path(filename: str) -> int:
    patrol_map = generate_map(filename)

    while patrol_map['in_bounds']:
        patrol_map = next_location(patrol_map)

    # Count the x's
    count = 0
    for row_index in range(0, patrol_map['row_bounds'] + 1):
        count += patrol_map[row_index].count('x')

    return count

result = predict_path("day-6-test-input.txt")
print(f"TEST 1: {result}")
assert(result == 41)

result = predict_path("day-6-input.txt")
print(f"PART 1: {result}")