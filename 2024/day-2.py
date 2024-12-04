# Author: Nick Quinn
# Description: Solution for day 2 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/2
# Interpreter: Python 3.12

def determine_if_increasing(first: int, second: int) -> bool:
    if first < second:
        return True
    return False

def determine_if_report_is_safe(levels: list) -> bool:
    # Start loop with the 2nd element
    last_level = int(levels[0])
    is_increasing = determine_if_increasing(levels[0], levels[1])
    for level in levels[1:]:
        if level == last_level:
            return False

        level_diff = level - last_level
        if level_diff < 0 and is_increasing:
            return False
        elif level_diff > 0 and not is_increasing:
            return False
        elif abs(level_diff) < 1 or abs(level_diff) > 3:
            return False

        last_level = level

    return True

# TODO Finish part 2.
def find_safe_reports_with_tolerance(levels: list) -> bool:
    last_index = 0
    curr_index = 1
    tolerance = 0

    prev_is_increasing = determine_if_increasing(levels[last_index], levels[curr_index])
    while curr_index < len(levels):
        curr_level = levels[curr_index]
        last_level = levels[last_index]
        level_diff = curr_level - last_level
        # curr_is_increasing = determine_if_increasing(levels[curr_index], levels[last_index])

        if tolerance > 1:
            return False

        if level_diff == 0:
            tolerance += 1
            curr_index += 1
            if curr_index == len(levels) - 1:
                if tolerance > 1:
                    return False
                else:
                    return True
                # prev_is_increasing = determine_if_increasing(levels[curr_index + 1], levels[last_index])
        curr_is_increasing = determine_if_increasing(levels[curr_index], levels[last_index])

        # TODO address -> # 5 3 4 5
        if curr_is_increasing != prev_is_increasing:
            tolerance += 1

        elif abs(level_diff) < 1 or abs(level_diff) > 3:
            tolerance += 1

        # Increment last index if no bad levels are found
        else:
            last_index += 1

        curr_index += 1
        prev_is_increasing = curr_is_increasing


    return True

def find_safe_reports(file_name: str, has_tolerance: bool) -> int:
    safe_reports = 0
    with open(file_name) as f:
        for level in f:
            formatted_report = [int(level) for level in level.strip().split()]
            if has_tolerance:
                is_safe = find_safe_reports_with_tolerance(formatted_report)
            else:
                is_safe = determine_if_report_is_safe(formatted_report)

            if is_safe:
                safe_reports += 1

    return safe_reports

test_levels = find_safe_reports('day-2-test-input.txt', False)
print(f"TEST 1: {test_levels}")
assert test_levels == 2

safe_levels = find_safe_reports('day-2-input.txt', False)
print(f"PART 1: {safe_levels}")
assert safe_levels == 486

test_levels = find_safe_reports('day-2-test-input.txt', True)
print(f"TEST 2: {test_levels}")
assert test_levels == 4

safe_levels = find_safe_reports('day-2-input.txt', True)
print(f"PART 2: {safe_levels}")
# assert safe_levels == 486