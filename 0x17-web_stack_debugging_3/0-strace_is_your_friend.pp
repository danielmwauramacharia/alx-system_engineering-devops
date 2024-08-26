# A Puppet manifest to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command   => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path      => ['/bin', '/usr/bin'],
  unless    => "grep -q 'phpp' ${file_to_edit}",
  logoutput => true,  # Log the output for debugging purposes
}
