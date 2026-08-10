import socket
target_scan = input("Enter the targets you want to scan(separated by commas)")
port_scan = int(input("Enter the range of ports you want to scan: "))
ip_list = target_scan.split(',')
for target in ip_list:
        target = target.strip()
        print("Scanning target[*]"+target)
        for ports in range(1,port_scan+1):
                phone = socket.socket()
                phone.settimeout(0.5)
                result = phone.connect_ex((target,ports))
                if result == 0:
                        print("port"+str(ports)+"is open")
                else:
                        pass
                phone.close()
