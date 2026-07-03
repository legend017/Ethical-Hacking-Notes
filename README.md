# Ethical Hacking Notes

My learning journey in ethical hacking.

## 🎯 Learning Roadmap
- [x] Linux Basics
- [ ] Networking Fundamentals
- [x] Information Gathering
- [x] Vulnerability Analysis
- [x] Initial Exploitation & Payloads (with encoding)
- [x] Post-Exploitation (persistence, privesc)
- [ ] Active Directory & Lateral Movement
- [ ] Web Application Pentesting (OWASP Top 10)
- [ ] Bypassing Endpoint Protection (Defender/Firewall ON)
- [ ] Web App Hacking
- [x] CTF Challenges

## 🛠️ Tools Built
* **[simple-port-scanner](./simple-port-scanner.py)** - A multi-target TCP port scanner written from scratch in Python.
  * **Features:** Supports comma-separated target inputs, handles custom port ranges, and utilizes a `0.5s` socket timeout to efficiently bypass firewalled hosts without freezing.
  * **Learning Outcomes:** understood network sockets (`socket.connect_ex`), socket lifecycles, and nested Python loops.
 
## HTB Starting Point Progress

## HTB Starting Point Progress

| Box | Protocol | Status |
|-----|----------|--------|
| Meow | Telnet | ✅ Rooted |
| Fawn | FTP | ✅ Rooted |
| Dancing | SMB | ✅ Rooted |
| Redeemer | Redis | ✅ Rooted |
| Appointment | SQL Injection | ✅ Rooted |
| Sequel | MySQL | ✅ Rooted |
| Crocodile | FTP + Web | ✅ Rooted |
| Responder | LFI + NTLM Hash | ✅ Rooted |
| Three | S3 Bucket + RCE | ✅ Rooted |
| Cap | IDOR + PCAP | ✅ Rooted |

## 📖 Table of Contents
1. [Linux Basics](1.Linux-Basics.md)
2. [Reconnaissance & Information Gathering](2.Reconnaissance%20%26%20Information%20Gathering.md)
3. [Scanning](3.Scanning.md)
4. [Vulnerability Analysis](5.Vulnerability-Analysis.md)
5. [Exploitation & Gaining Access](6.Exploitation%20%26%20Gaining-Access.md)
6. [Payloads & Trojans](7.Gaining-Access%28Virus%2C%20Trojans.%20Payloads.%29.md)
7. [Post-Exploitation](8.Post-Exploitation.md)
8. [HTB Machine Write-ups](https://github.com/legend017/Ethical-Hacking-Notes#-htb-machine-write-ups)

## Started: May 2026
