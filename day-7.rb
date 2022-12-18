# Author: Nick Quinn
# Description: Solution for day 7 of 2022 Advent of Code

def walk_directory(position)
  current_directory = $file_system[:/]
  if position.count > 0
    position.each do |d|
      current_directory = current_directory[d]
    end
  end
  current_directory
end

def insert_into_directory(position, key, value)
  current_directory = walk_directory(position)
  current_directory[key] = value
end

$file_system = { "/": {} }
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
        position.append(line.last)
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

  puts "Line #{index}: #{position}"

  index += 1
end

puts $file_system