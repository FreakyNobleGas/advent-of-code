# Author: Nick Quinn
# Description: Solution for day 1 of 2022 Advent of Code

calories = [-1,-1,-1]
tmp = -1
File.foreach("day-1-input.txt") do |line|
  line = line.chomp.to_i

  if line.eql?(0)
    calories.each_with_index do |elf, i|
      if elf < tmp
        calories.insert(i, tmp)
        calories.delete_at(3)
        break
      end
    end

    tmp = 0
  else
    tmp += line
  end
end

puts "Part 1 " + calories.first.to_s
puts "Part 2 " + calories.sum.to_s