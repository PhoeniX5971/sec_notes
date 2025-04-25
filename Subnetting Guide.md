## What is Subnetting?

Subnetting is the method of dividing a single IP network into multiple smaller logical networks, called subnets. It's used to:

- Improve network performance by reducing broadcast traffic.
    
- Enhance security by isolating segments.
    
- Optimize IP address usage and management.
    
- Support custom network topologies.
    

Instead of wasting a large range of IPs on a small group of devices, subnetting helps you slice and allocate just enough for each group.

---

## Understanding IP Addresses

An IPv4 address is 32 bits long, split into four 8-bit sections (octets), usually written in decimal:

Example:  
192.168.10.5 → binary: 11000000.10101000.00001010.00000101

Every IP address has two parts:

- **Network portion**: Identifies the subnet the device belongs to.
    
- **Host portion**: Identifies the individual device in that subnet.
    

The split between those two is controlled by the **subnet mask** or **CIDR prefix**.

---

## What is a Subnet Mask?

A subnet mask tells us **how many bits are used for the network** and **how many are left for hosts**.

For example, a subnet mask of:

- 255.255.255.0 → 24 bits for the network → `/24` in CIDR notation.
    
- 255.255.255.192 → 26 bits for the network → `/26` in CIDR.
    

The higher the CIDR value, the **smaller** the subnet (fewer hosts, more subnets).

---

## Key Formulas

- **Usable hosts** = 2^(32 - subnet bits) - 2  
    (We subtract 2: one for the network address and one for broadcast.)
    
- **Block size** = 256 - value of the subnet mask octet where subnetting happens  
    (Used to find the step between each subnet.)
    

---

## Subnetting Step-by-Step

### Goal: Subnet 192.168.10.0/24 into smaller networks

1. **Decide how many subnets or hosts you need.**
    
    Example: Need 4 subnets? → 2² = 4 → Borrow 2 bits.
    
2. **Borrow bits from the host portion.**
    
    From /24, borrow 2 bits → /26 (i.e. now 26 bits are for the network).
    
3. **Calculate new subnet mask.**
    
    /26 → 255.255.255.192
    
4. **Calculate block size.**
    
    256 - 192 = 64 → Each subnet increases by 64.
    
5. **List the subnets.**

| Subnet | Network Address | Host Range                      | Broadcast Address |
| ------ | --------------- | ------------------------------- | ----------------- |
| 1      | 192.168.10.0    | 192.168.10.1 - 192.168.10.62    | 192.168.10.63     |
| 2      | 192.168.10.64   | 192.168.10.65 - 192.168.10.126  | 192.168.10.127    |
| 3      | 192.168.10.128  | 192.168.10.129 - 192.168.10.190 | 192.168.10.191    |
| 4      | 192.168.10.192  | 192.168.10.193 - 192.168.10.254 | 192.168.10.255    |

    Usable hosts per subnet = 2^(6) - 2 = 62

## More Examples

### Example 1: Subnet 10.0.0.0/24 into 8 subnets

- 8 subnets = 2³ → borrow 3 bits → /27
    
- /27 = 255.255.255.224 → block size = 32
    
- Subnets:
    
    - 10.0.0.0 → 10.0.0.1 - 10.0.0.30 → broadcast 10.0.0.31
        
    - 10.0.0.32 → 10.0.0.33 - 10.0.0.62 → broadcast 10.0.0.63
        
    - ... and so on


### Example 2: Find the subnet and host range of 192.168.1.77/28

- /28 = 255.255.255.240 → block size = 16
- Subnets: 192.168.1.0, 192.168.1.16, ..., 192.168.1.112
- 77 falls in the subnet starting at 192.168.1.64
- Host range: 192.168.1.65 - 192.168.1.78
- Broadcast: 192.168.1.79

---

## CIDR & Subnet Mask Cheat Sheet

|CIDR|Subnet Mask|Hosts|Block Size|
|---|---|---|---|
|/30|255.255.255.252|2|4|
|/29|255.255.255.248|6|8|
|/28|255.255.255.240|14|16|
|/27|255.255.255.224|30|32|
|/26|255.255.255.192|62|64|
|/25|255.255.255.128|126|128|
|/24|255.255.255.0|254|256|
|/23|255.255.254.0|510|512|
|/22|255.255.252.0|1022|1024|

---

## Tools You Can Use

- `ipcalc` (Linux CLI)
- `sipcalc`
- Online calculators: [Subnet Calculator (Online)](https://www.subnet-calculator.com), cidr.xyz
- Practice manually for exams or certs like CCNA

---

## Quick Tips

- Always subtract 2 from total hosts (network + broadcast).
- If subnetting feels hard, remember: it's all just binary math.
- Get comfortable converting between decimal and binary.
- Block size helps you quickly jump between subnet ranges.