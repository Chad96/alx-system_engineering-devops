#!/usr/bin/env ruby

# Check if the argument matches the regular expression
if ARGV[0] =~ /School/
    # Print the matched string
    puts ARGV[0]
  else
    # Print an empty string if no match is found
    puts ""
  end
  