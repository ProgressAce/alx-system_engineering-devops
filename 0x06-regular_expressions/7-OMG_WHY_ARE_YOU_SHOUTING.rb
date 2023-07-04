#!/usr/bin/env ruby
# regex that only matches letters in caps
puts ARGV[0].scan(/[A-Z]+/).join
