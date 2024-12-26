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

def calculate(filename: str) -> int:
    rules, pages = parse_file(filename)
    rules = generate_rule_dict(rules)

    result = 0
    for page in pages.values():
        result += validate_page(rules, page)

    return result


result = calculate("day-5-test-input.txt")
print(f"TEST 1: {result}")
assert(result == 143)

result = calculate("day-5-input.txt")
print(f"PART 1: {result}")
assert(result == 5452)