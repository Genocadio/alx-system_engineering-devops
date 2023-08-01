#!/usr/bin/env ruby

def find_school_occurrences(input_text)
  # Regular expression to match "School" (case-insensitive)
  regex = /\bSchool\b/i

  # Find all occurrences of "School" in the input_text using the regular expression
  matches = input_text.scan(regex)

  # Return the matched occurrences as an array
  matches
end

# Check if the script is executed with an argument
if ARGV.length == 1
  input_text = ARGV[0]

  # Call the method to find occurrences of "School"
  occurrences = find_school_occurrences(input_text)

  if occurrences.empty?
    puts "No occurrences of 'School' found."
  else
    puts "Occurrences of 'School' found: #{occurrences.join(', ')}"
  end
else
  puts "Please provide one argument with the input text."
end
