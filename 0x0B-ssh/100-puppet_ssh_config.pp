$config_content = 'Host
    IdentityFile ~/.ssh/school
    PasswordAuthentication no'

file { 'ssh client config':
  ensure  => 'present',
  path    => '/root/.ssh/config',
  content => $config_content
}
