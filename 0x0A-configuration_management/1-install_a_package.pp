# ensures installation of version 2.1.0 flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3
}
