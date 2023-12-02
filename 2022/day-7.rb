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

  index += 1
end

calculate_directory_totals($file_system)

answer = 0
$test.each {|val| val.each { |k,v| answer += v unless v > 100000}}
puts "Part 1: #{answer}"