#!/usr/bin/env ruby
# the regex matches a 10 digit phone number
puts ARGV[0].scan(/\A\d{10}\Z/).join
