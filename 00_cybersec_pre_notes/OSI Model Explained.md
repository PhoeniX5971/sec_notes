# OSI Model Explained
## Layer 7: Application Layer
- **Function**: Human-network interface (HTTP, FTP, SMTP)
- **Attack**: 
  - SQLi, XSS target this layer

## Layer 6: Presentation Layer
- **Function**: Data translation (encryption, compression)
- **Example**: 
  - TLS/SSL handshake occurs here
  - JPEG/MPEG encoding
- **Attack**: Heartbleed (TLS memory leak)

## Layer 5: Session Layer
- **Function**: Manages connections (establish/maintain/terminate)
- **Protocols**: 
  - NetBIOS (Windows file sharing)
  - PPTP (obsolete VPN)

## Layer 4: Transport Layer
- **Function**: End-to-end communication (TCP/UDP)
- **Key Info**:
  - TCP: 3-way handshake (SYN→SYN-ACK→ACK)
  - UDP: No ACK (used in DNS/VoIP)
- **Attack**: SYN Flood (DoS)

## Layer 3: Network Layer
- **Function**: Logical addressing/routing (IP, ICMP)
- **Devices**: Routers

## Layer 2: Data Link Layer
- **Function**: Physical addressing (MAC), error detection
- **Protocols**: 
  - ARP (IP→MAC resolution)
  - VLAN tagging (802.1Q)
- **Attack**: ARP spoofing

## Layer 1: Physical Layer
- **Function**: Raw bit transmission (cables, WiFi radio)
- **Examples**: 
  - Ethernet (RJ45), Fiber (SFP)
  - Hub operates here
- **Attack**: Cable tapping