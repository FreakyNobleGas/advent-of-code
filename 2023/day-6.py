# Author: Nick Quinn
# Description: Solution for day 6 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/6
# Interpreter: Python 3.12


from _helper_methods import extract_numbers


def main():
    data = test_data.splitlines()
    print(f"PART 1 TEST: {find_optimal_hold_time(data)}")

    data = real_data.splitlines()
    print(f"PART 1: {find_optimal_hold_time(data)}")

    data = test_data.replace(" ", "").splitlines()
    print(f"PART 2 TEST: {find_optimal_hold_time(data)}")

    data = real_data.replace(" ", "").splitlines()
    print(f"PART 2: {find_optimal_hold_time(data)}")


def find_optimal_hold_time(data):
    times = extract_numbers(data[0])
    distances = extract_numbers(data[1])

    result = 1
    for i in range(0, len(times)):
        time = times[i]
        distance = distances[i]
        minimum_hold_time = None

        # Equation => (Total Time - Hold Time) * Hold Time = Distance
        for hold_time in range(0, time):
            if ((time - hold_time) * hold_time) > distance:
                minimum_hold_time = hold_time
                break

        possible_winning_times = 1
        for _ in range(minimum_hold_time, time - minimum_hold_time):
            possible_winning_times += 1

        result *= possible_winning_times

    return result


test_data = """\
Time:      7  15   30
Distance:  9  40  200
"""

real_data = """\
Time:        59     79     65     75
Distance:   597   1234   1032   1328
"""

if __name__ == "__main__":
    main()