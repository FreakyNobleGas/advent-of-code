#! /bin/bash

# Author: Nick Quinn
# Description: Simple script to generate files for the next AoC problem
# Link: https://adventofcode.com/
# Usage: bash ./generate-new-day.sh

curr_year=$(date +%Y)
cd "./$curr_year" || exit 1

# Go through the list of file and extract the problem from the file name so we know which
# problem is next.
for f in day-*.py; do
  last_problem=${f#day-} # remove prefix
  last_problem=${last_problem%.py} # remove suffix
done

# Check if this is the first problem of the year as the base case. Otherwise, add 1 to the last
# problem number.
if [[ "$last_problem" == '*' ]]; then
  next_problem=1
else
  next_problem=$(($last_problem + 1))
fi

problem_file_name="day-$next_problem.py"
solution_file_name="day-$next_problem-input.txt"
test_solution_file_name="day-$next_problem-test-input.txt"

# Create the files
touch $problem_file_name
touch $solution_file_name
touch $test_solution_file_name

# Insert header
cat << EOF >> $problem_file_name
# Author: Nick Quinn
# Description: Solution for day $next_problem of $curr_year Advent of Code
# Problem Link: https://adventofcode.com/$curr_year/day/$next_problem
# Interpreter: Python 3.12
EOF

# Add files to Git
cd ..
git add "$curr_year/$problem_file_name" "$curr_year/$solution_file_name" "$curr_year/$test_solution_file_name"