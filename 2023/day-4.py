# Author: Nick Quinn
# Description: Solution for day 4 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/4
# Interpreter: Python 3.12

from _helper_methods import extract_numbers


def main():
    data = test_data.splitlines()
    total_points, total_scratchcards = calculate_lottery_ticket_total(data)
    print(f"PART 1 TEST: {total_points}")
    print(f"PART 2 TEST: {total_scratchcards}")

    data = open("day-4-input.txt", "r").read().splitlines()
    total_points, total_scratchcards = calculate_lottery_ticket_total(data)
    print(f"PART 1: {total_points}")
    print(f"PART 2: {total_scratchcards}")


def calculate_lottery_ticket_total(data):
    total_points = 0
    total_scratchcards = 0

    scratchcards = {}
    for match_num in range(0, len(data)):
        scratchcards[match_num + 1] = 1

    for match in data:
        card_index = match.find(":")
        card_num = extract_numbers(match[0:card_index])[0]

        winning_nums_index = match.find("|")
        winning_nums = extract_numbers(match[card_index:winning_nums_index])

        scratch_off_nums = extract_numbers(match[winning_nums_index:])

        match_result = 0
        nums_matched_count = 0
        num_copies = scratchcards[card_num]
        for num in scratch_off_nums:
            if num in winning_nums:
                # Base case
                if match_result == 0:
                    match_result += 1
                else:
                    match_result *= 2

                nums_matched_count += 1

                scratchcards[card_num + nums_matched_count] += num_copies

        total_scratchcards += num_copies
        total_points += match_result

    return total_points, total_scratchcards


test_data = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

if __name__ == "__main__":
    main()