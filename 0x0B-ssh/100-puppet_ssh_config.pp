#!/usr/bin/env bash
# Using puppet to make changes in the configuration file
file { '/etc/ssh/ssh_config':
  ensure => 'present',
}

file_line { 'No Auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => true,
}

file_line { 'Identity':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
}

