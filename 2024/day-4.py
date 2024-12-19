# Author: Nick Quinn
# Description: Solution for day  of 202 Advent of Code
# Problem Link: https://adventofcode.com/202/day/
# Interpreter: Python 3.12

from icecream import ic


def is_xmas(match) -> int:
    keyword = "XMAS"

    if keyword == match:
        return 1

    rev_match = [c for c in match]
    rev_match.reverse()
    if keyword == "".join(rev_match):
        return 1

    return 0

def search_graph(graph: dict) -> int:
    result = 0
    for index in graph.keys():
        for n, l in enumerate(graph[index]):
            left = n - 3 >= 0
            right = n + 3 <= (len(graph[index]) - 1)
            down = index + 3 <= (len(graph.keys()) - 1)

            # Search right
            if right:
                match = "".join(graph[index][n:n + 4])
                result += is_xmas(match)

            # Search down
            if down:
                match = [str(graph[index + offset][n]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_xmas(match)

            # Search diagonal
            if down and right:
                match = [str(graph[index + offset][n + offset]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_xmas(match)

            if down and left:
                match = [str(graph[index + offset][n - offset]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_xmas(match)

    return result

def find_xmas(file_name: str) -> int:
    graph = {}
    with open(file_name) as f:
        index = 0
        for line in f:
            line = [c for c in line.strip()]
            graph[index] = line
            index += 1

    return search_graph(graph)

def run_and_assert(file_name: str, expected_result: int) -> None:
    result = find_xmas(file_name)
    assert result == expected_result, f"Expected {expected_result}, got {result} for {file_name}"
    print(f"{file_name}: {result}")

run_and_assert('day-4-test-input.txt', 18)
run_and_assert('day-4-test-diag-input.txt', 2)
run_and_assert('day-4-test-horizontal-input.txt', 3)
run_and_assert('day-4-test-vertical-input.txt', 3)

result = find_xmas('day-4-input.txt')
print(f"PART 1: {result}")
assert result == 2639