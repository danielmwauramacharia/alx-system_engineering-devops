#killing a process called killmenow
exec { 'kill-killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin'],
}

