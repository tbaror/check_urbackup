# check_urbackup

Simple script to check Urbackup backup status ,based on https://github.com/uroni/urbackup-server-python-web-api-wrapper
You will need to have Pythone3.x installed and pip3 install urbackup-server-web-api-wrapper prior to usage.

usage: check_urbackup.py [-h] [--version] [--host HOST] [--user USER]
                         [--password PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show agent version
  --host HOST, -ho HOST
                        host name or IP
  --user USER, -u USER  User name for Urbackup server
  --password PASSWORD, -p PASSWORD
                        user password for Urbackup server
