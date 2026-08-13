# Python Port Scanner

Custom multi-target TCP port scanner built from scratch in Python.

## Features
- Multi-target scanning (comma-separated IPs)
- Custom port range support
- 0.5s socket timeout to handle firewalled hosts

## Usage
```
python3 portscanner.py
```

## Example Usage
```
Enter the targets you want to scan (separated by commas): 192.168.18.241, 192.168.18.242
Enter the range of ports you want to scan: 100

Scanning target[*] 192.168.18.241
port 22 is open
port 80 is open
port 443 is open
```

## Learning Outcomes
- Understood network sockets (`socket.connect_ex`)
- Socket lifecycles and timeouts
- Nested loops for multi-target scanning

## Target tested
Metasploitable2 — 192.168.18.241
