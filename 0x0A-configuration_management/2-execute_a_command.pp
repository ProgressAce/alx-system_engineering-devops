exec { 'kill process':
  command => '/usr/bin/pkill -KILL killmenow'
#  path    => ['/usr/bin/pkill']
}
