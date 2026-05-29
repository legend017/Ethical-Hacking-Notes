# Cap - HTB Starting Point

## What I Did
- Found IDOR by changing /data/1 to /data/0
- Downloaded user 0 PCAP file
- Analyzed with Wireshark, found username and password
- Used FTP to get user flag, SSH for shell access
- Used Python (cap_setuid) for root privilege escalation

## Flags
- User: 7be8201e27bda90475bdc28e51d07956
- Root: c065d68bdc3276290c734f6da87f5121

## What I Learned
- IDOR: Changing URL parameters can expose others' data
- PCAP files contain plaintext credentials
- Wireshark TCP streams can hide trailing spaces
- Linux capabilities can be abused for root access
