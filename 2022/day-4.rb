# Author: Nick Quinn
# Description: Solution for day 4 of 2022 Advent of Code

num_dup_sections_part_1, num_dup_sections_part_2 = 0, 0
File.foreach("day-4-input.txt") do |line|
  line = line.chomp
  elfArray = line.split(",").map do |e|
    e.split("-").map(&:to_i)
  end

  elfOneSection = Array(elfArray.first.first..elfArray.first.last)
  elfTwoSection = Array(elfArray.last.first..elfArray.last.last)
  if (elfOneSection - elfTwoSection).empty?
    num_dup_sections_part_1 += 1
  elsif (elfTwoSection - elfOneSection).empty?
    num_dup_sections_part_1 += 1
  end

  if elfOneSection.intersect?(elfTwoSection)
    num_dup_sections_part_2 += 1
  end
end

puts "Part 1: #{num_dup_sections_part_1}"
puts "Part 2: #{num_dup_sections_part_2}"