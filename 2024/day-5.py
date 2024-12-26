# Author: Nick Quinn
# Description: Solution for day 5 of 2024 Advent of Code
# Problem Link: https://adventofcode.com/2024/day/5
# Interpreter: Python 3.12

from icecream import ic
from operator import itemgetter

def combine_rules(rules: dict) -> list:
    combined = []
    # Keep track each rule previously seen
    rule_dict = {}

    for rule in rules.values():
        r = rule.split("|")
        f = r[0]
        s = r[1]
        f_index = -1
        s_index = -1

        if rule_dict.get(f) is None:
            rule_dict[f] = [s]
        else:
            rule_dict[f].append(s)

        # Check if either page number is in the list already
        if f in combined:
            f_index = combined.index(f)
        if s in combined:
            s_index = combined.index(s)

        # If both are in list, then move f before s
        if f_index >= 0 and s_index >= 0:

            if f_index > s_index:
                combined.remove(f)
                combined.insert(s_index, f)

                # check if list is valid
                # for n in combined[:combined.index(f)]:
                #     if n in rule_dict[f]:
                #         ic("f is not in correct spot")
                #         ic(f)
                #         ic(s)
                #         ic(combined)
                #         ic(combined[:combined.index(f)])
                #         ic(rule_dict[f])
                #         ic(s_index)
                #         ic(f_index)

        # If f is in list, but not s, then put s at end
        elif f_index >= 0 and s_index == -1:
            combined.append(s)

        # If s is in list, but not f, then put f at front
        elif f_index == -1 and s_index >= 0:
            combined = [f] + combined

        # If neither are in list, then push both to front
        elif f_index == -1 and s_index == -1:
            # nf_index = -1
            # ns_index = -1
            # for n in rule_dict.keys():
                # if n not in combined:
                #     continue
                #
                # c_index = combined.index(n)
                # ic(n, c_index)
                # Look for f and insert before c_index.

                # Look for s and insert after c_index (check for out of bounds in combined)

            # If f index is -1, then put in front

            # If s index is -1, then put in back

         combined = [f, s] + combined
        else:
            print('unexpected case')
            ic(r)
            ic(combined)


    # Verify correctness
    # for rule in rules.values():
    #     r = rule.split("|")
    #     f = combined.index(r[0])
    #     s = combined.index(r[1])
    #
    #     if f > s:
    #         ic('number is incorrect location')
    #         ic(r)

    combined = [int(n) for n in combined]


    return combined

# Returns the sorted pages
def sort_pages(pages: dict, rules: list) -> int:
    result = 0
    for page in pages.values():
        p_nums = page.split(',')
        s_nums = []
        for n in p_nums:
            s_nums.append((n, rules.index(n)))

        s_nums = sorted(s_nums, key=itemgetter(1))
        result += int(s_nums[len(s_nums) // 2][0])

    return result

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

def validate_page(rules: list, page: list) -> int:
    last_n_seen = -1
    for n in page:
        # Ignore number if it's not in rule
        if n not in rules:
            continue

        index = rules.index(n)
        if last_n_seen == -1:
            last_n_seen = index
        elif last_n_seen > index:
            return 0
        else:
            last_n_seen = index

    return page[len(page) // 2]

def calculate(filename: str) -> int:
    rules, pages = parse_file(filename)
    rules = combine_rules(rules)

    result = 0
    for page in pages.values():
        result += validate_page(rules, page)

    return result


result = calculate("day-5-test-input.txt")
assert(result == 143)
print(f"TEST 1: {result}")

result = calculate("day-5-input.txt")
print(f"PART 1: {result}")