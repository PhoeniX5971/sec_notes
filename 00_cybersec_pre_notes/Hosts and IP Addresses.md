# Hosts and IP Addresses
- **Host**: Any device with an IP (PC, server, IoT).  
- **IP Address**:  
  - IPv4: `192.168.1.1` (32-bit, e.g., private ranges `10.0.0.0/8`, `172.16.0.0/12`)  
  - IPv6: `2001:0db8:85a3::` (128-bit, solves IPv4 exhaustion)  
- **Key for Pentesting**:  
  - `nmap -sn 192.168.1.0/24` → Discover live hosts.  
  - Private IPs indicate internal network targets.  