# Puppet manifest to make changes to my ssh client config file
# - disable need for password authentication
# - the sought after private key will be found in ~/.ssh
file_line {'password authenticity':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line {'identitiy key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}
