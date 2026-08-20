# Ethical Hacking Notes
My complete learning journey in ethical hacking

> **Note:** These notes were compiled from various sources (labs, courses, practice).
> All tools were written from scratch as part of the learning process.
> Each concept was validated through hands-on lab exercises.

## 📊 Progress Overview

## 🎯 Learning Roadmap
- [x] Linux Basics
- [x] Networking Fundamentals
- [x] Information Gathering & Reconnaissance
- [x] Scanning & Enumeration
- [x] Vulnerability Analysis
- [x] Exploitation & Gaining Access
- [x] Payload Generation (msfvenom, encoding)
- [x] Post-Exploitation (persistence, privesc)
- [x] Web Application Pentesting (SQLi, XSS, CSRF, Command Injection, Brute Force)
- [x] MITM Attacks (ARP Spoofing, Bettercap)
- [x] Wireless Pentesting (WPA2 Cracking, Aircrack-ng, Hashcat)
- [x] HTB Starting Point (10+ boxes rooted)

### In Progress
- [ ] Active Directory & Lateral Movement
- [ ] Bypassing Endpoint Protection (Defender/Firewall ON)

---
### 🛠️ Projects (Custom Tools)

| Tool | Description | Key Learning |
|------|-------------|--------------|
| [Python Port Scanner](Projects/Python-Port-Scanner/) | Multi-target TCP scanner with custom ranges | Socket programming, `connect_ex()`, timeout handling |
| [Python Backdoor](Projects/Python-Backdoor/) | Reverse shell with JSON communication | Socket server/client, subprocess execution |
| [Python Bruteforcer](Projects/Python-Bruteforcer/) | GET/POST brute force with cookie support | HTTP requests, form data, cookie handling |
| [Python Directory Finder](Projects/Python-Directory-Finder/) | Wordlist-based directory enumeration | HTTP status codes, URL construction |
---

## 🎯 HTB Starting Point Progress (Free Boxes)

### Tier 0 - Foundations (100% Complete)
| Box | Protocol | Key Technique | Status |
|-----|----------|---------------|--------|
| Meow | Telnet | Default credentials (root:blank) | ✅ |
| Fawn | FTP | Anonymous login | ✅ |
| Dancing | SMB | Null session | ✅ |
| Redeemer | Redis | Unauthenticated access | ✅ |

### Tier 1 - Fundamental Exploitation (100% Complete)
| Box | Protocol | Key Technique | Status |
|-----|----------|---------------|--------|
| Appointment | SQL Injection | Login bypass | ✅ |
| Sequel | MySQL | Unauthenticated access | ✅ |
| Crocodile | FTP + Web | Credentials reuse | ✅ |
| Responder | LFI + NTLM | Hash capture + crack | ✅ |
| Three | S3 Bucket + RCE | Subdomain + PHP shell | ✅ |

### Tier 2 - Advanced Exploitation (1 Free Box Complete)
| Box | Protocol | Key Technique | Status |
|-----|----------|---------------|--------|
| Oopsie | Web + IDOR + SUID | IDOR for admin access, PATH Hijacking privesc | ✅ |

---

## 🎯 Other HTB Machines Rooted

| Machine | Difficulty | Protocol | Key Technique | Status |
|---------|------------|----------|---------------|--------|
| **Cap** | Medium | IDOR + PCAP | Wireshark Analysis, cap_setuid privesc | ✅ |

---

## 📊 Summary

| Category | Completed | Status |
|----------|-----------|--------|
| **Tier 0 (Starting Point)** | 4/4 | ✅ |
| **Tier 1 (Starting Point)** | 5/5 | ✅ |
| **Tier 2 (Starting Point)** | 1/4 | ✅ |
| **Other HTB Machines** | Cap | ✅ |

---

## 💡 Key Lessons Learned

### Most Valuable Discoveries
1. **Telnet/FTP/HTTP** transmit credentials in plaintext - always use encrypted protocols
2. **SYN scans** are stealthier because they don't complete the handshake
3. **Modern OS detection** is unreliable due to generic TCP stacks
4. **Stageless payloads** are more reliable than staged ones
5. **Persistence** requires separate module from initial access
6. **CSRF** abuses existing sessions - doesn't steal cookies
7. **WPA2 handshake** contains hashed password - crack offline with wordlists
8. **MITM** works silently - victims have no idea traffic is intercepted

### Common Mistakes & Solutions
- **FatRat payloads** corrupted due to over-obfuscation → Use clean msfvenom
- **Hydra GET forms** failed with cookies → Use Burpsuite Intruder
- **BlueKeep exploit** crashed target → Unstable, <50% success rate
- **rtl8xxxu driver** unstable for monitor mode → Install proper rtl8188eus driver

---

### Fundamentals (10 Modules)
01. [Linux Basics](Fundamentals/01.Linux-Basics.md)
02. [Reconnaissance & Information Gathering](Fundamentals/02.Reconnaissance%20%26%20Information%20Gathering.md)
03. [Scanning & Enumeration](Fundamentals/03.Scanning.md)
04. [Vulnerability Analysis](Fundamentals/04.Vulnerability-Analysis.md)
05. [Exploitation & Gaining Access](Fundamentals/05.Exploitation%20%26%20Gaining-Access.md)
06. [Payloads & Trojans](Fundamentals/06.Gaining-Access%28Virus%2C%20Trojans.%20Payloads.%29.md)
07. [Post-Exploitation](Fundamentals/07.Post-Exploitation.md)
08. [Web Application Pentesting](Fundamentals/08.Web-Application-Pentesting.md)
09. [MITM (Man-In-The-Middle) Attacks](Fundamentals/09.MITM%28Man-In-The-Middle-Attack%29.md)
10. [Wireless Cracking (WPA2)](Fundamentals/10.Wireless-Cracking.md)

---

## 🚀 Next Steps

### Bug Bounty Path (Starting August 2026)
1. **Practice Platforms** - PortSwigger Academy, PentesterLab
2. **Target Programs** - VDPs → HackerOne Beginner → Private Programs
3. **Skills to Develop**
   - Recon automation (subdomain, endpoint discovery)
   - Business logic flaws (price manipulation, 2FA bypass)
   - Modern web (JWT, GraphQL, CORS, SSRF)

*Started: December 2025 (Linux basics) | Ethical Hacking: May 2026 | Current: August 2026*

---

## ⭐ Support

If these notes helped you in your learning journey, consider giving the repo a star — it helps others find it too.

**[⭐ Star this repo](https://github.com/legend017/Ethical-Hacking-Notes)**

## 📫 Connect With Me
- [LinkedIn](https://www.linkedin.com/in/rishi-yadav-543651355/)

> *"Documenting the journey from complete beginner to bug bounty hunter."*
