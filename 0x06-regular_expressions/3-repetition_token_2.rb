#!/usr/bin/env ruby
# matches h-b-t(1 to many)-n
puts ARGV[0].scan(/hbt+n/).join
