# manifest that configures the ssh local client config file
$config_content = 'Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no'

# configuring the ssh client config file
file { 'ssh client config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => $config_content
}
