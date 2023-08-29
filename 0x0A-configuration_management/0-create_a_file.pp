# Uses a puppet manifest to create a file in /tmp
# the file has 0744 permissions and content placed inside it.
file {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
