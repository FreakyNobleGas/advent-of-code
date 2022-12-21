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
def calculate_directory_value(directory)
  tmp = $file_system[directory]
  total = 0
  tmp.each { |k,v| total += v unless k == :_total }
  total
end

def get_directory_value(directory)
  $file_system[directory][:_total]
end

def calculate_directory_totals
  all_paths = Array.new
  $file_system.each do |k,_|
    insert_into_file_system(k, :_total, calculate_directory_value(k))
    all_paths.append(k.to_s)
  end
  all_paths.reverse!

  last_directory = ""
  last_total = 0
  all_paths.each do |d|
    if last_directory.include?(d) and d != "/"
    last_total += get_directory_value(last_directory.to_sym) + get_directory_value(d.to_sym)
    insert_into_file_system(d.to_sym, :_total, last_total)

    else
      last_total = 0
    end

    if d.length == 2
      tmp = get_directory_value(d.to_sym) + get_directory_value(:/)
      insert_into_file_system(:/, :_total, tmp)
    end
    last_directory = d
  end
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
    end
  else
    puts "ERROR: Last command was not ls"
  end

  index += 1
end
calculate_directory_totals

puts "File System:"
pp $file_system

answer = 0
$file_system.each do |k,v|
  if v[:_total] <= 100000
    answer += v[:_total]
  end
end
puts "Part 1: #{answer}"