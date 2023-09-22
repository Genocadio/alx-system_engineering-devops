# kill  process

exec { 'killmenow':
  command => 'pkill -f killmenow',
}