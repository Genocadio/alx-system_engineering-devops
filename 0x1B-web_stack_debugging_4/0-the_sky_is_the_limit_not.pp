# replaces the first occurrence of "15" with "4096

# Increase the ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# nginx restart
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

