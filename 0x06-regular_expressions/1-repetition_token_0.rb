#!/usr/bin/env ruby
# matches h-b-t(2 to 5)-n
puts ARGV[0].scan(/hbt{2,5}n/).join
