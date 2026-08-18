# Python Directory Finder
Custom directory enumeration tool built from scratch in Python.

## Features
- Custom wordlist support
- Status code display (200, 301, 403)

## Usage
python3 dir-finder.py

## Example Usage
python3 dir-finder.py

````
┌──(kali㉿kali)-[~]
└─$ /usr/bin/python /home/kali/Downloads/12.py                                                       

Enter the url: http://192.168.18.243/dvwa
Enter the path to directory list: /usr/share/wordlists/dirb/common.txt
[*] Scanning:http://192.168.18.243/dvwa
[+] [200] Found Directory: http://192.168.18.243/dvwa/
[+] [200] Found Directory: http://192.168.18.243/dvwa/about
[+] [200] Found Directory: http://192.168.18.243/dvwa/config
[+] [200] Found Directory: http://192.168.18.243/dvwa/docs
[+] [200] Found Directory: http://192.168.18.243/dvwa/external
[+] [200] Found Directory: http://192.168.18.243/dvwa/favicon.ico
[+] [200] Found Directory: http://192.168.18.243/dvwa/index
[+] [200] Found Directory: http://192.168.18.243/dvwa/index.php
[+] [200] Found Directory: http://192.168.18.243/dvwa/instructions
[+] [200] Found Directory: http://192.168.18.243/dvwa/login
[+] [200] Found Directory: http://192.168.18.243/dvwa/logout
[+] [200] Found Directory: http://192.168.18.243/dvwa/php.ini
[+] [200] Found Directory: http://192.168.18.243/dvwa/phpinfo
[+] [200] Found Directory: http://192.168.18.243/dvwa/phpinfo.php
[+] [200] Found Directory: http://192.168.18.243/dvwa/README
[+] [200] Found Directory: http://192.168.18.243/dvwa/robots
[+] [200] Found Directory: http://192.168.18.243/dvwa/robots.txt
[+] [200] Found Directory: http://192.168.18.243/dvwa/security
[+] [200] Found Directory: http://192.168.18.243/dvwa/setup
````
## Target tested
DVWA on Metasploitable2
