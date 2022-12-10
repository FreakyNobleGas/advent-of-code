# Author: Nick Quinn
# Description: Solution for day 3 of 2022 Advent of Code

def get_score_from_ascii(c)
  if c > 96
    c - 96
  else
    c - 38
  end
end

score = 0
File.foreach("day-3-input.txt") do |line|
  line = line.chomp.split('')
  mid_index = line.length / 2

  ruckOne = line[0..mid_index - 1]
  ruckTwo = line[mid_index..line.length - 1]

  asciiChar = ruckOne.intersection(ruckTwo).first.ord

  score += get_score_from_ascii(asciiChar)

end

puts "Part 1: #{score.to_s}"


# Part two
score = 0
f = File.readlines("day-3-input.txt")

group = []
f.each_with_index do |line, i|
  line = line.chomp.split('')
  elf_num = i % 3
  group.insert(elf_num, line)

  # Calculate group total
  if elf_num == 2
    asciiChar = group.first.intersection(group.at(1)).intersection(group.at(2)).first.ord

    score += get_score_from_ascii(asciiChar)
  end
end

puts "Part 2: #{score}"