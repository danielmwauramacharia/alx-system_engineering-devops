# A Puppet manifest to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command   => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path      => ['/bin', '/usr/bin'],
  unless    => "grep -q 'phpp' ${file_to_edit}",
  logoutput => true,  # Log the output for debugging purposes
  notify    => Service['apache2'],  # Notify Apache service to restart if file changes
}

# Restart Apache to apply changes
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Exec['replace_line'],
}
