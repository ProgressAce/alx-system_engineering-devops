# Puppet manifest to kill a process named 'killmenow'
exec {'kill process':
  command => '/bin/pkill -KILL killmenow'
}
