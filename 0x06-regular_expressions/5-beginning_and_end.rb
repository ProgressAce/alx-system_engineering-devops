#!/usr/bin/env ruby
# matches a string that starts with h and ends with n,
# with any one char in between
puts ARGV[0].scan(/\Ah.n\Z/).join
