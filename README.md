# Ethical Hacking Notes
My learning journey in ethical hacking.

## 🔥 Currently Working On
- MITM Attacks
- Wireless Pentesting

## 🎯 Learning Roadmap
- [x] Linux Basics
- [x] Networking Fundamentals
- [x] Information Gathering
- [x] Vulnerability Analysis
- [x] Initial Exploitation & Payloads (with encoding)
- [x] Post-Exploitation (persistence, privesc)
- [x] Web Application Pentesting (SQLi, XSS, CSRF, Command Injection, Brute Force)
- [ ] Full OWASP Top 10 (2021)
- [ ] Active Directory & Lateral Movement
- [ ] Bypassing Endpoint Protection (Defender/Firewall ON)
- [ ] MITM Attacks
- [ ] Wireless Pentesting
- [x] CTF Challenges

## 🛠️ Tools Built
* **[simple-port-scanner](./simple-port-scanner.py)** - A multi-target TCP port scanner written from scratch in Python.
  * **Features:** Supports comma-separated target inputs, handles custom port ranges, and utilizes a `0.5s` socket timeout to efficiently bypass firewalled hosts without freezing.
  * **Learning Outcomes:** Understood network sockets (`socket.connect_ex`), socket lifecycles, and nested Python loops.

* **[Python-Backdoor](./Python-Backdoor/)** - A custom reverse shell built from scratch in Python.
  * **Features:** Command execution, directory traversal, JSON-based communication for reliable data transfer.
  * **Learning Outcomes:** Understood socket programming (server/client model), subprocess execution, JSON encoding/decoding over sockets.

## HTB Starting Point Progress
| Box | Protocol | Key Technique | Status |
|-----|----------|---------------|--------|
| Meow | Telnet | Default credentials | ✅ Rooted |
| Fawn | FTP | Anonymous login | ✅ Rooted |
| Dancing | SMB | Null session | ✅ Rooted |
| Redeemer | Redis | Unauthenticated access | ✅ Rooted |
| Appointment | SQL Injection | Login bypass | ✅ Rooted |
| Sequel | MySQL | Unauthenticated access | ✅ Rooted |
| Crocodile | FTP + Web | Credentials reuse | ✅ Rooted |
| Responder | LFI + NTLM Hash | Hash capture + crack | ✅ Rooted |
| Three | S3 Bucket + RCE | Subdomain + PHP shell | ✅ Rooted |
| Cap | IDOR + PCAP | Wireshark + privesc | ✅ Rooted |

## 📖 Table of Contents
1. [Linux Basics](1.Linux-Basics.md)
2. [Reconnaissance & Information Gathering](2.Reconnaissance%20%26%20Information%20Gathering.md)
3. [Scanning](3.Scanning.md)
4. [Vulnerability Analysis](5.Vulnerability-Analysis.md)
5. [Exploitation & Gaining Access](6.Exploitation%20%26%20Gaining-Access.md)
6. [Payloads & Trojans](7.Gaining-Access%28Virus%2C%20Trojans.%20Payloads.%29.md)
7. [Post-Exploitation](8.Post-Exploitation.md)
8. [Web Application Pentesting](9.Web-Application-Pentesting.md)

## Started: May 2026
