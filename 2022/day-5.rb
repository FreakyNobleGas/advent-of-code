# Author: Nick Quinn
# Description: Solution for day 5 of 2022 Advent of Code


def build_stacks(line, stacks)
  count = 0
  line.each_char do |c|
    if c.match?(/[[:alpha:]]/)
      stack_index = (count - 1) / 4

      if stacks[stack_index] == nil
        stacks[stack_index] = Array(c)
      else
        stacks[stack_index].append(c)
      end
    end
    count += 1
  end
end

stacks_part_1 = Array.new
stacks_part_2 = Array.new
File.foreach("day-5-input.txt") do |line|
  line = line.chomp

  if line.include?("[")
    build_stacks(line, stacks_part_1)
    stacks_part_2 = Marshal.load(Marshal.dump(stacks_part_1))
  end

  if line.include?("move")
    directions = Array.new
    line.split.each do |c|
        directions.append(c.to_i)
    end

    directions[1].times do
      tmp = stacks_part_1[directions[3] - 1].shift
      stacks_part_1[directions[5] - 1].unshift(tmp)
    end

    tmp2 = stacks_part_2[directions[3] - 1].shift(directions[1])
    stacks_part_2[directions[5] - 1] = tmp2.concat(stacks_part_2[directions[5] - 1])
  end
end

puts "Part 1: #{stacks_part_1.map {|s| s.first}.join}"
puts "Part 2: #{stacks_part_2.map {|s| s.first}.join}"