# Classes of Attacks

## Overview

### Basic Problems

- Network Insecurity
- Weak Authentication
- Services Full of Bugs

---

## Replay

An attack where a valid message is intercepted and sent again.

### Counter Measures

**Counter**: Implementing a counter that is sent with the message to confirm that the request is sent correctly.
**Weakness**: After a couple of messages the attacker will understand the sequence and use it.

**Timestamp + Lifetime**: Sending the time of the request with it and making it only effective for short period of time.

---

## IP Spoofing

Forging the source network address.

### Counter Measures

**NEVER USE ADDRESS BASED AUTHN**

---

## Packet Sniffing

Read the packets addressed to another node.

### Counter Measures

Encryption of the packet payload.

---

## DoS

Keep a host busy so it can't provide services.

Be it from buffer overflow, syn attack, ping flooding, mail/log saturation...

### Counter Measures
Monitor requests and oversize servers.

---

## DDoS

Distributed DoS.

Over the network.

### Counter Measures

Monitor, human confirmation...

---

## Shadow/Fake Server

Could be through:

- Intercepting and then spoofing, impersonating the server.
- DNS.

### Counter Measures
Server authentication.

---
