# Scanning Notes

## 1. TCP (Transmission Control Protocol)
- Transfers data in the form of packets
- Uses three-way handshake:
  - **SYN** — Sender sends synchronize packet to receiver
  - **SYN-ACK** — Receiver receives the packet and acknowledges it
  - **ACK** — Sender acknowledges and the connection is formed

## 2. UDP (User Datagram Protocol)
- Also transfers data in the form of packets
- Used where fast data transmission is required (video games, streaming sites)
- No handshake — faster but less reliable than TCP

---

## 3. Host Discovery

| Tool | Command | Notes |
|------|---------|-------|
| **arp** | `sudo arp -a` | Not very reliable — sometimes shows hosts, sometimes not |
| **netdiscover** | `sudo netdiscover` | More reliable tool for discovering hosts on local network |
| **nmap ping sweep** | `nmap -sn <target>` | Does not scan ports — only checks if host is up |

---

## 4. Scan Types

### SYN Scan (Stealth Scan)
- Full handshake is **not** completed
- Sends: SYN → receives SYN-ACK → sends RST (reset/break connection)
- System does not log the connection — user will not know they were scanned
- Command: `nmap -sS <target>`
- `-s` = scan, `S` = SYN

### TCP Connect Scan
- Full three-way handshake is completed
- Noisier — system logs the connection
- User can detect they were scanned
- Leaves more traces, easily detectable
- Command: `nmap -sT <target>`

### UDP Scan
- Takes more time than other scans
- Should not be avoided — vulnerable services sometimes run on UDP
- Command: `nmap -sU <target>`

| Scan Type | Handshake | Stealth Level | Speed |
|-----------|-----------|---------------|-------|
| SYN (`-sS`) | Incomplete (RST) | High | Fast |
| TCP Connect (`-sT`) | Complete | Low | Fast |
| UDP (`-sU`) | N/A | Medium | Slow |

---

## 5. Useful Nmap Commands

| Task | Command |
|------|---------|
| Scan single port | `nmap -sS -p 80 <target>` |
| Full port scan (all 65535) | `nmap -sS -p- <target>` |
| Scan entire subnet | `nmap -sS 192.168.20.240/24` |
| OS detection | `nmap -O <target>` |
| Service version detection | `nmap -sV <target>` |
| Higher version accuracy | `nmap -sV --version-intensity 9 <target>` |
| Aggressive scan (OS + version + scripts) | `nmap -A <target>` |

> ⚠️ `-A` should not be used on targets without permission. It's loud.

---

## 6. Firewall

- A network security system that constantly monitors incoming and outgoing packets
- When unknown/malicious packets are sent, the firewall drops them
- During scanning, if the result shows **"filtered"** — the port is protected by a firewall

### Bypassing the Firewall

| Technique | Command | How It Works |
|-----------|---------|--------------|
| **Decoys** | `nmap -D <fake_ip1>,<fake_ip2>,<target>` | Hides your real IP among fake IPs |
| **Fragmentation** | `nmap -f <target>` | Splits packets into very small pieces — harder for firewall to detect (may crash target system) |

---

## 7. Lab Discoveries

### My Router
- Port 80 open (HTTP admin panel)
- Port 23 filtered (Telnet blocked — firewall working correctly)
- Everything else closed/filtered

### OS Detection on My Laptop
- `nmap -O` showed **"too many fingerprints match"**
- Modern operating systems have generic TCP stacks
- Firewalls normalize TCP behavior — no unique quirks for Nmap to identify

### Wireshark Protocol Analysis

| Protocol | Port | What I Saw |
|----------|------|------------|
| **Telnet** | 23 | Every keystroke sent as a separate packet. Username and password visible in plaintext in TCP stream. |
| **FTP** | 21 | USER and PASS commands visible. File contents transferred in plaintext. |
| **HTTP** | 80 | URLs, form submissions, and credentials all readable. |

> **Lesson:** Any unencrypted protocol broadcasts data to anyone on the network.

### simple-port-scanner Discovery
- `connect_ex()` returns `0` when a port is open
- Scanner runs fast on Kali Linux, but slow on Windows
- Windows limits half-open connections and silently drops packets on closed ports
