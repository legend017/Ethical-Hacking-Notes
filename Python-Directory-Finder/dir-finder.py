import requests
import pyfiglet

banner = pyfiglet.figlet_format("DIR-FINDER")
print(banner)

target = input("Enter the url: ")
dir_list = input("Enter the path to directory list: ")

with open(dir_list, 'r') as f:
    directories = f.readlines()
    print(f"[*] Scanning:{target}")
    for directory in directories:
        directory = directory.strip()
        url = target + '/' + directory
        response = requests.get(url)

        if response:
            print(f"[+] Found Directory: {url}")
