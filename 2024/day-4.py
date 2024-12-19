# Author: Nick Quinn
# Description: Solution for day  of 202 Advent of Code
# Problem Link: https://adventofcode.com/202/day/
# Interpreter: Python 3.12

from icecream import ic


def is_match(match: str, keyword: str) -> int:
    if keyword == match:
        return 1

    rev_match = [c for c in match]
    rev_match.reverse()
    if keyword == "".join(rev_match):
        return 1

    return 0

def search_graph_for_xmas(graph: dict) -> int:
    result = 0
    keyword = "XMAS"
    for index in graph.keys():
        for n, l in enumerate(graph[index]):
            left = n - 3 >= 0
            right = n + 3 <= (len(graph[index]) - 1)
            down = index + 3 <= (len(graph.keys()) - 1)

            # Search right
            if right:
                match = "".join(graph[index][n:n + 4])
                result += is_match(match, keyword)

            # Search down
            if down:
                match = [str(graph[index + offset][n]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_match(match, keyword)

            # Search diagonal
            if down and right:
                match = [str(graph[index + offset][n + offset]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_match(match, keyword)

            if down and left:
                match = [str(graph[index + offset][n - offset]) for offset in range(1, 4)]
                match = [graph[index][n]] + match
                match = "".join(match)
                result += is_match(match, keyword)

    return result

def search_graph_for_mas(graph: dict):
    result = 0
    keyword = "MAS"
    for index in graph.keys():
        for n, l in enumerate(graph[index]):
            left = n - 1 >= 0
            right = n + 1 <= (len(graph[index]) - 1)
            down = index + 1 <= (len(graph.keys()) - 1)
            up = index - 1 >= 0

            # A will be the start point
            if l != "A":
                continue

            if up and down and left and right:
                first = f"{graph[index+1][n-1]}A{graph[index-1][n+1]}"
                second = f"{graph[index+1][n+1]}A{graph[index-1][n-1]}"
                if is_match(first, keyword) == 1 and is_match(second, keyword) == 1:
                    result += 1

    return result


def convert_to_graph(file_name: str) -> dict:
    graph = {}
    with open(file_name) as f:
        index = 0
        for line in f:
            line = [c for c in line.strip()]
            graph[index] = line
            index += 1

    return graph

def find_xmas(file_name: str) -> int:
    graph = convert_to_graph(file_name)
    return search_graph_for_xmas(graph)

def find_mas(file_name: str) -> int:
    graph = convert_to_graph(file_name)
    return search_graph_for_mas(graph)

def run_and_assert_xmas(file_name: str, expected_result: int) -> None:
    result = find_xmas(file_name)
    assert result == expected_result, f"Expected {expected_result}, got {result} for {file_name}"
    print(f"{file_name}: {result}")

def run_and_assert_mas(file_name: str, expected_result: int) -> None:
    result = find_mas(file_name)
    assert result == expected_result, f"Expected {expected_result}, got {result} for {file_name}"
    print(f"{file_name}: {result}")

run_and_assert_xmas('day-4-test-input.txt', 18)
run_and_assert_xmas('day-4-test-diag-input.txt', 2)
run_and_assert_xmas('day-4-test-horizontal-input.txt', 3)
run_and_assert_xmas('day-4-test-vertical-input.txt', 3)

result = find_xmas('day-4-input.txt')
print(f"PART 1: {result}")
assert result == 2639

run_and_assert_mas('day-4-test-x-input.txt', 2)

result = find_mas('day-4-input.txt')
print(f"PART 2: {result}")