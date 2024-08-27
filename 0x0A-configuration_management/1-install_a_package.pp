# Install Python 3.8 using apt (for Debian/Ubuntu systems)
package { 'python3.8':
  ensure   => 'installed',
  provider => 'apt',
}

# Install pip3 (package manager for Python3)
package { 'python3-pip':
  ensure   => 'installed',
  provider => 'apt',
  require  => Package['python3.8'],
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Install Werkzeug using pip3
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['Flask'],
}

