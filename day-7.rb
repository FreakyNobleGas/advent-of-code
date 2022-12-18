# Author: Nick Quinn
# Description: Solution for day 7 of 2022 Advent of Code

def walk_directory(file_system, position)
  current_directory = nil
  position.each do |d|
    current_directory = file_system[d]
  end
  current_directory
end

file_system = { "/": {} }
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
        current_directory = walk_directory(file_system, position)
        unless current_directory.has_key(line.last)
          current_directory[line.last] = {}
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
      file_system[position.last][line[1]] = {}
    else
      # Save file to filesystem. Ex: { "d": [100, "f"] }
      if position.last == nil
        file_system["/"][line.last] = line[1]
      else
        file_system[position.last][line.last] = line[1]
      end
    end
  end

  puts "Line #{index}: #{position}"

  index += 1
end

puts file_system