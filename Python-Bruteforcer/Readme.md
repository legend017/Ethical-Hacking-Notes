# Python Bruteforcer
Custom brute force tool built from scratch in Python.

## Features
- Supports GET and POST methods
- Cookie support for authenticated pages
- Custom wordlist support
- Success detection via failure message

## Usage
python3 Bruteforcer.py

## Example Usage
This example uses POST method (no cookie needed):
python3 Bruteforcer.py
┌──(kali㉿kali)-[~/Desktop/bruteforcer]
└─$ python3 bruteforce.py
 ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____ ____  
| __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|  _ \ 
|  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _| | |_) |
| |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___|  _ < 
|____/|_| \_\\___/  |_| |_____|_|   \___/|_| \_\\____|_____|_| \_\
                                                                  

Enter the url: http://192.168.18.243/dvwa/login.php
Enter the username: admin
Enter the path of pass file: /home/kali/passwords.txt
Enter the error msg when login failed: Login failed
Enter the cookie value(OPTIONAL): 
[+] Starting Bruteforcing!
[+] Username: admin
[*] Trying 7 passwords
[-] password failed:root
[-] password failed:password123
[-] password failed:pass
[+] Password Found:password

## Target tested
DVWA on Metasploitable2
