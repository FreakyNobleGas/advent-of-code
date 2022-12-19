# Author: Nick Quinn
# Description: Solution for day 7 of 2022 Advent of Code

def walk_directory(position)
  current_directory = $file_system[:/]
  if position.count > 0
    position.each do |d|
      current_directory = current_directory[d.to_sym]
    end
  end
  current_directory
end

def insert_into_directory(position, key, value)
  current_directory = walk_directory(position)
  current_directory[key.to_sym] = value
end


def calculate_directory_totals(current_level)
  sum = 0
  current_level.each do |k,v|
    if v.is_a?(Hash)
      directory_val = calculate_directory_totals(v)
      $total_bytes[k] = directory_val
      sum += $total_bytes[k]
      $test.append({k => directory_val})
    else
      sum += v.to_i
    end
  end
  sum
end

$file_system = { :/ => {}}
$total_bytes = {}
$test = []
position = Array.new
last_command = nil
index = 1
File.foreach("day-7-input.txt") do |line|
  line = line.chomp.split

  # Command executed in terminal
  if line.first == "$"
    if line[1] == "cd"
      last_command = "cd"
      case line.last
      when "/"
        position = Array.new
      when ".."
        position.pop
      else
        current_directory = walk_directory(position)
        unless current_directory.has_key?(line.last)
          insert_into_directory(position, line.last, {})
        end
        position.append(line.last.to_sym)
      end
    elsif line[1] == "ls"
      last_command = "ls"
    end
    # Output from command in terminal
  elsif last_command == "ls"
    if line.first == "dir"
      # Save directory to filesystem. Ex: { "/": {"d": {}}}
      # file_system[position.last][line[1]] = {}
      insert_into_directory(position, line[1], {})
    else
      # Save file to filesystem. Ex: { "d": [100, "f"] }
      insert_into_directory(position, line.last, line.first)
    end
  end

  #puts "Line #{index}: #{position}"

  index += 1
end

puts "Calculating Directory Totals"
calculate_directory_totals($file_system)
puts "Done!"

tmp = Array.new
all_combinations = Array.new
# $total_bytes.each { |k,v| tmp.append(v) unless v > 100000}
# (1..tmp.count).each { |i|
#   all_combinations.append(tmp.combination(i).to_a)
# }
puts "Calculating Combinations"
$test.each {|val| val.each { |k,v| tmp.append(v) unless v > 100000}}
(1..tmp.count).each { |i|
  puts "Iteration #{i}/#{tmp.count}"
  all_combinations.append(tmp.combination(i).to_a)
}
puts "Done!"

answer = 0
# pp all_combinations
all_combinations.flatten!(1).each do |a|
  sum = a.sum
  if sum > answer and sum <= 100000
    answer = sum
  end
end

puts "Part 1: #{answer}"
puts "Total Bytes #{$total_bytes}"
puts "Test #{$test}"
puts "File System #{$file_system}"