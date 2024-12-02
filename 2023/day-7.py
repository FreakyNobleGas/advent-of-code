# Author: Nick Quinn
# Description: Solution for day 7 of 2023 Advent of Code
# Problem Link: https://adventofcode.com/2023/day/7
# Interpreter: Python 3.12

from _helper_methods import test_assertion
from math import floor

CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}


def main():
    test()

    result = determine_order(test_data.splitlines())
    print(f"PART 1 TEST: {result}")

    result = determine_order(open("day-7-input.txt", "r").read().splitlines())
    print(f"PART 1: {result}")


def determine_order(lines):
    hands = parse_lines(lines)
    order = []

    for hand in hands:
        hand_value = 0
        cards = hand[0]
        bid = hand[1]
        if is_five_of_kind(cards)[0]:
            hand_value = 7
        elif is_four_of_kind(cards)[0]:
            hand_value = 6
        elif is_full_house(cards):
            hand_value = 5
        elif is_three_of_kind(cards)[0]:
            hand_value = 4
        elif is_two_pair(cards):
            hand_value = 3
        elif is_one_pair(cards):
            hand_value = 2
        elif is_high_card(cards):
            hand_value = 1

        if not order:
            order.append((cards, hand_value, bid))
        else:
            for i in range(0, len(order)):
                curr_hand = order[i][0]
                curr_rank = order[i][1]
                if hand_value > curr_rank:
                    order.insert(i, (cards, hand_value, bid))
                    break
                elif hand_value == curr_rank:
                    if second_order_ruling(cards, curr_hand) == cards:
                        order.insert(i, (cards, hand_value, bid))
                        break

    rank = 1
    result = 0
    for i in reversed(order):
        bid = i[2]
        result += bid * rank
        rank += 1

    return result


def parse_lines(lines):
    data = []
    for line in lines:
        hand, bid = line.split(" ")
        data.append((hand, int(bid)))

    return data


def is_five_of_kind(hand):
    if hand.count(hand[0]) == 5:
        return True, hand[0]

    return False, None


def is_four_of_kind(hand):
    if hand.count(hand[0]) == 4:
        return True, hand[0]

    if hand.count(hand[1]) == 4:
        return True, hand[1]

    return False, None


def is_full_house(hand):
    three_of_a_kind = is_three_of_kind(hand)
    if three_of_a_kind[0]:
        remaining = hand.replace(three_of_a_kind[1], '')
        if is_one_pair(remaining):
            return True

    return False


def is_three_of_kind(hand):
    if hand.count(hand[0]) == 3:
        return True, hand[0]

    if hand.count(hand[1]) == 3:
        return True, hand[1]

    if hand.count(hand[2]) == 3:
        return True, hand[2]

    return False, None


def count_pairs(hand, pairs_needed):
    pairs = 0
    num_of_cards = {}
    for c in hand:
        num_of_cards[c] = num_of_cards.get(c, 0) + 1

    for c in num_of_cards.values():
        pairs += floor(c / 2)

    if pairs == pairs_needed:
        return True

    return False


def is_one_pair(hand):
    return count_pairs(hand, 1)


def is_two_pair(hand):
    return count_pairs(hand, 2)


# Where all cards are distinct.
def is_high_card(hand):
    for c in hand:
        if hand.count(c) > 1:
            return False
    return True


# If tie, then find which has the highest card going left to right in cases of a tie
def second_order_ruling(hand_one, hand_two):
    for i in range(0, len(hand_one)):
        num_one = convert_to_num(hand_one[i])
        num_two = convert_to_num(hand_two[i])
        if num_one > num_two:
            return hand_one
        if num_two > num_one:
            return hand_two

    return None


def convert_to_num(c):
    if not c.isnumeric():
        return CARDS[c]
    return int(c)


def test():
    print("START TESTS")

    name = "is_five_of_kind"
    test_assertion(name, is_five_of_kind("AAAAA"), (True, "A"))
    test_assertion(name, is_five_of_kind("AAAAK"), (False, None))
    test_assertion(name, is_five_of_kind("KAAAA"), (False, None))

    name = "is_four_of_kind"
    test_assertion(name, is_four_of_kind("AAAAA"), (False, None))
    test_assertion(name, is_four_of_kind("AAAAK"), (True, "A"))
    test_assertion(name, is_four_of_kind("KAAAA"), (True, "A"))
    test_assertion(name, is_four_of_kind("KAAQA"), (False, None))

    name = "is_three_of_kind"
    test_assertion(name, is_three_of_kind("AAAAA"), (False, None))
    test_assertion(name, is_three_of_kind("AAAAK"), (False, None))
    test_assertion(name, is_three_of_kind("KAAAA"), (False, None))
    test_assertion(name, is_three_of_kind("KAAQA"), (True, "A"))

    name = "is_one_pair"
    test_assertion(name, is_one_pair("AAAAA"), False)
    test_assertion(name, is_one_pair("AAAAK"), False)
    test_assertion(name, is_one_pair("KAAAA"), False)
    test_assertion(name, is_one_pair("KAAQJ"), True)

    name = "is_two_pair"
    test_assertion(name, is_two_pair("AAAAA"), True)
    test_assertion(name, is_two_pair("AAAAK"), True)
    test_assertion(name, is_two_pair("KAAAA"), True)
    test_assertion(name, is_two_pair("KAAJJ"), True)
    test_assertion(name, is_two_pair("A2345"), False)

    name = "is_full_house"
    test_assertion(name, is_full_house("23332"), True)
    test_assertion(name, is_full_house("AAAAK"), False)
    test_assertion(name, is_full_house("KAAAA"), False)
    test_assertion(name, is_full_house("AAAJJ"), True)
    test_assertion(name, is_full_house("A2345"), False)

    name = "is_high_card"
    test_assertion(name, is_high_card("12345"), True)
    test_assertion(name, is_high_card("AAAAK"), False)
    test_assertion(name, is_high_card("KAAAA"), False)
    test_assertion(name, is_high_card("AAAJJ"), False)
    test_assertion(name, is_high_card("A2345"), True)

    name = "second_order_ruling"
    test_assertion(name, second_order_ruling("12345", "23456"), "23456")
    test_assertion(name, second_order_ruling("AAAAK", "AAAAQ"), "AAAAK")
    test_assertion(name, second_order_ruling("KAAAA", "KAAAA"), None)

    print("FINISHED TESTS")


test_data = '''\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

if __name__ == "__main__":
    main()