# 🔍 Python Network Port Scanner

A fast, threaded command-line port scanner built in Python.  
This project was built for educational purposes to understand how network reconnaissance works and how tools like nmap operate under the hood.

---

## How It Works

Every service running on a computer listens on a specific **port**. A port scanner probes a target machine to find which ports are open — revealing what services are running and potential attack surfaces.

```
Port 22  → SSH
Port 80  → HTTP
Port 443 → HTTPS
Port 21  → FTP
Port 3306→ MySQL
```

### The Scanning Process
1. A **socket** attempts to connect to each port on the target
2. If the connection succeeds (`result == 0`) — the port is **open**
3. If it fails or times out — the port is **closed or filtered**

### Why Threading?
A sequential scanner waits up to 1 second per port — scanning 1,000 ports could take **16 minutes**. This scanner uses **threading** to scan all ports simultaneously, reducing that to a few seconds.

```
Sequential:  [port 1] → [port 2] → [port 3] → ...  (slow)
Threaded:    [port 1]
             [port 2]  ← simultaneously → (fast)
             [port 3]
```

### Project Structure
```
port-scanner/
├── port_scanner.py   # Main script
├── .gitignore
├── LICENSE           # MIT
└── README.md
```

---

## Example Output

```
=============================================
         Python Network Port Scanner
         For Educational Use Only
=============================================

  Enter target IP or hostname : scanme.nmap.org
  Enter start port            : 1
  Enter end port              : 100

  [*] Target   : scanme.nmap.org
  [*] Resolved : 45.33.32.156
  [*] Scanning ports 1 - 100...

  [+] Port 22    is OPEN
  [+] Port 80    is OPEN

  [*] Scan complete in 1.84 seconds.
```

---

## ⚠️ Disclaimer & Ethical Use

This tool was built **strictly for educational purposes** to demonstrate:
- How network reconnaissance works
- How port scanning identifies open services
- How threading improves performance in network tools

**Only use this tool on systems you own or have explicit permission to scan.**  
Scanning systems without authorisation is illegal in most countries.  
The author takes no responsibility for misuse of this tool.

A safe, legal target to practice on: `scanme.nmap.org` — provided by the nmap project specifically for this purpose.

---

## What I Learned Building This

- How sockets work and how network connections are made in Python
- What ports are and how services are exposed on a network
- How threading works and why it dramatically improves performance
- How thread locks prevent race conditions in concurrent programs
- How real tools like nmap perform reconnaissance
- Python concepts: threading, sockets, error handling, timeouts

---

*Built as part of a personal cybersecurity learning portfolio.*
