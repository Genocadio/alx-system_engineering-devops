#!/usr/bin/env ruby
if ARGV.length == 1
  input_text = ARGV[0]
  regex = /\bSchool\b/i
  matches = input_text.scan(regex)
  if matches.empty?
    puts "No occurrences of 'School' found."
  else
    puts "Occurrences of 'School' found: #{matches.join(', ')}"
  end
else
  puts "Please provide one argument with the input text."
end
