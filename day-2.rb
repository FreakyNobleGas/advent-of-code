# Author: Nick Quinn
# Description: Solution for day 2 of 2022 Advent of Code

# Part 1
# A, X Rock
# B, Y Paper
# C, Z Scissors

LOST = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

# Part 1
score = 0
File.foreach("day-2-input.txt") do |line|
  line = line.chomp.split

  case line.first
  when "A"
    case line.last
    when "X"
      score += ROCK + DRAW
    when "Y"
      score += PAPER + WIN
    else
      score += SCISSORS + LOST
    end
  when "B"
    case line.last
    when "X"
      score += ROCK + LOST
    when "Y"
      score += PAPER + DRAW
    else
      score += SCISSORS + WIN
    end
  else
    case line.last
    when "X"
      score += ROCK + WIN
    when "Y"
      score += PAPER + LOST
    else
      score += SCISSORS + DRAW
    end
  end
end

puts "Part 1: " + score.to_s

# Part 2
# X means LOST
# Y means DRAW
# Z means WIN
score = 0
File.foreach("day-2-input.txt") do |line|
  line = line.chomp.split

  case line.last
  when "X"
    case line.first
    when "A"
      score += SCISSORS
    when "B"
      score += ROCK
    else
      score += PAPER
    end
    score += LOST
  when "Y"
    case line.first
    when "A"
      score += ROCK
    when "B"
      score += PAPER
    else
      score += SCISSORS
    end
    score += DRAW
  else
    case line.first
    when "A"
      score += PAPER
    when "B"
      score += SCISSORS
    else
      score += ROCK
    end
    score += WIN
  end
end

puts "Part 2: " + score.to_s
