# Author: Nick Quinn
# Description: Solution for day 6 of 2022 Advent of Code

def find_unique_consecutive_characters(data, num_of_unique)
  buffer = Array.new(data[0..(num_of_unique - 1)])
  data[num_of_unique..].map.each_with_index do |c, i|
    buffer.shift(1)
    buffer.push(c)

    if buffer.uniq.count == num_of_unique
      return i + num_of_unique + 1

    end
  end
end

data = File.read("day-6-input.txt").chomp.split("")

puts "Part 1: #{find_unique_consecutive_characters(data, 4)}"
puts "Part 2: #{find_unique_consecutive_characters(data, 14)}"