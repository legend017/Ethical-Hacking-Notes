# Python Backdoor

Custom reverse shell built from scratch in Python.

## Features
- Command execution on target machine
- Directory traversal (cd handling)
- JSON-based communication for reliable data transfer

## Usage
Run on attacker (Kali):
python3 server.py

Run on victim:
python3 backdoor.py

## Learning Outcomes
- Understood reverse shell concept (victim calls back to attacker)
- Socket programming (server/client model)
- subprocess execution and output capture
- JSON encoding/decoding over sockets
- Why cd requires os.chdir() instead of subprocess

## Target tested
Windows 10 VM
