# Fix server issue of limited open file access for user holberton

exec { 'holberton hard limit':
  command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 100000/g" /etc/security/limits.conf'
}

exec { 'holberton soft limit':
  command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 100000/g" /etc/security/limits.conf'
}
