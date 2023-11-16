# Manifest that fixes the server's webstack by allowing nginx to open for files

exec { 'change ulimit -n value':
  command => "/bin/sed -i 's#ULIMIT=\"-n 15\"#ULIMIT=\"-n 500\"#g' /etc/default/nginx",
  notify  => Exec['restart nginx']
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart'
}
