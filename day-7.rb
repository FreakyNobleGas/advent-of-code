# Author: Nick Quinn
# Description: Solution for day 7 of 2022 Advent of Code

def generate_directory_key(position)
  if position.count == 0
    return :/
  end

  key = ""
  position.each do |p|
    key += "/#{p}"
  end
  key.to_sym
end

def insert_into_file_system(directory, file, value)
  unless $file_system.has_key?(directory)
    create_new_directory(directory)
  end
  dir = $file_system[directory]
  value = value.to_i
  dir[file] = value
end

def create_new_directory(key)
  $file_system[key] = { "_total": 0 }
end

# Get value from directory
def get_directory_value(directory)
  tmp = $file_system[directory]
  total = 0
  tmp.each { |k,v| total += v unless k == :_total }
  insert_into_file_system(directory, :_total, total)
  total
end

def calculate_directory_totals(position)
  total = 0
  pp position
  if position.count > 0
    ((position.count)..0).each do |p|
      parent_directory = generate_directory_key(position[0..p])
      # puts parent_directory
      total += get_directory_value(parent_directory)
      insert_into_file_system(parent_directory, :_total, total)
    end
  end

  total += get_directory_value(:/)
  insert_into_file_system(:/, :_total, total)
end

def reset_position
  Array.new
end

$file_system = { "/": {"_total": 0} }
position = reset_position
last_command = nil
index = 1
File.foreach("day-7-input.txt") do |line|
  line = line.chomp.split

  # Command executed in terminal
  if line.first == "$"
    command = line[1]
    if command == "cd"
      last_command = "cd"
      case line.last
      when "/"
        position = reset_position
      when ".."
        position.pop
      else
        position.append(line.last.to_sym)
      end
    elsif command == "ls"
      last_command = "ls"
    else
      puts "ERROR: Unknown command '#{command}'"
    end
    # Output from command in terminal
  elsif last_command == "ls"
    if line.first != "dir"
      insert_into_file_system(generate_directory_key(position), line.last, line.first)
      calculate_directory_totals(position)
    end
    # if line.first == "dir"
    #   # Save directory to filesystem. Ex: { "/": {"d": {}}}
    #   # file_system[position.last][line[1]] = {}
    #   insert_into_directory(position, line[1], {})
    # else
    #   # Save file to filesystem. Ex: { "d": [100, "f"] }
    #   insert_into_directory(position, line.last, line.first)
    # end
  else
    puts "ERROR: Last command was not ls"
  end

  #puts "Line #{index}: #{position}"
  index += 1
end

puts "File System:"
pp $file_system

# puts "Calculating Directory Totals"
# calculate_directory_totals($file_system)
# puts "Done!"

# tmp = Array.new
# all_combinations = Array.new
# $total_bytes.each { |k,v| tmp.append(v) unless v > 100000}
# (1..tmp.count).each { |i|
#   all_combinations.append(tmp.combination(i).to_a)
# }

# puts "Calculating Combinations"
# $test.each {|val| val.each { |k,v| tmp.append(v) unless v > 100000}}
# (1..tmp.count).each { |i|
#   puts "Iteration #{i}/#{tmp.count}"
#   all_combinations.append(tmp.combination(i).to_a)
# }
# puts "Done!"

# answer = 0
# all_combinations.flatten!(1).each do |a|
#   sum = a.sum
#   if sum > answer and sum <= 100000
#     answer = sum
#   end
# end

# puts "Part 1: #{answer}"