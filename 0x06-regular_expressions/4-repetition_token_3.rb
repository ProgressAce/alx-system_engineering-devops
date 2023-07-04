#!/usr/bin/env ruby
# matches h-b-t(0 to many)-n
puts ARGV[0].scan(/hbt*n/).join
