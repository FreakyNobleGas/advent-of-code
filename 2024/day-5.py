# Author: Nick Quinn
# Description: Solution for day 5 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/5
# Interpreter: Python 3.12

from icecream import ic

def generate_rule_dict(rules: dict) -> dict:
    # Keep track each rule previously seen
    rule_dict = {}

    for rule in rules.values():
        r = rule.split("|")
        f = int(r[0])
        s = int(r[1])

        if rule_dict.get(f) is None:
            rule_dict[f] = [s]
        else:
            rule_dict[f].append(s)

    return rule_dict

def parse_file(filename: str) -> (dict, dict):
    rules = {}
    pages = {}
    with open(filename) as f:
        index = 0
        is_rules = True
        for line in f:
            line = line.strip()
            if line == "":
                index = 0
                is_rules = False
                continue

            if is_rules:
                rules[index] = line
            else:
                line = line.split(',')
                line = [int(n) for n in line]
                pages[index] = line

            index += 1

    return rules, pages

def validate_page(rules_dict: dict, page: list) -> int:
    for index, num in enumerate(page):
        # Skip any number that doesn't have a rule.
        # Start with the second number since we need 2 numbers for a comparison.
        if num not in rules_dict.keys() or index == 0:
            continue

        rules = rules_dict[num]

        for n in page[:index]:
            if n in rules:
                return 0

    return page[len(page) // 2]

def fix_page(rules: dict, page: list) -> int:

    for rule_num in rules.keys():
        # Keep a copy of the current page so we can reinsert a number if it's
        # already in the correct position
        page_copy = page.copy()

        if rule_num not in page:
            continue

        # Find the number of occurrences
        count = page.count(rule_num)

        # Break if the page is all the same number
        if count == len(page):
            break

        # Remove all occurrences of the number so we can accurately track the index
        for n in range(0, count):
            page.remove(rule_num)

        # Find optimal location for number which is the index before the first occurrence of a number in
        # its rule list
        optimal_index = -1
        for index, n in enumerate(page):
            if n in rules[rule_num]:
                optimal_index = index
                break

        # Continue if we haven't found any violations
        if optimal_index == -1:
            # NOTE: This does not account for adding more than 1 rule num.
            page.insert(page_copy.index(rule_num) + 1, rule_num)
            continue

        # Insert rule num at optimal index
        for n in range(0, count):
            page.insert(optimal_index, rule_num)

    # assert that validate method returns non-zero
    assert(validate_page(rules, page) != 0)

    return page[len(page) // 2]

def calculate_part_1(filename: str) -> int:
    rules, pages = parse_file(filename)
    rules = generate_rule_dict(rules)

    result = 0
    for page in pages.values():
        result += validate_page(rules, page)

    return result

def calculate_part_2(filename: str) -> int:
    rules, pages = parse_file(filename)
    rules = generate_rule_dict(rules)

    incorrect_pages = []
    for page in pages.values():
        if validate_page(rules, page) == 0:
            incorrect_pages.append(page)

    if filename == "day-5-test-input.txt":
        assert len(incorrect_pages) == 3

    result = 0
    for page in incorrect_pages:
        result += fix_page(rules, page)

    return result

result = calculate_part_1("day-5-test-input.txt")
print(f"TEST 1: {result}")
assert(result == 143)

result = calculate_part_1("day-5-input.txt")
print(f"PART 1: {result}")
assert(result == 5452)

result = calculate_part_2("day-5-test-input.txt")
print(f"TEST 2: {result}")
assert(result == 123)

result = calculate_part_2("day-5-input.txt")
print(f"PART 2: {result}")
assert(result == 4598)