#fix bad "phpp" extentions to "php" in "wp-setting.php".
{ 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}

