# Network Devices

| Device | Layer | Function                 | Security Risk                 |
| ------ | ----- | ------------------------ | ----------------------------- |
| Hub    | L1    | Floods data to all ports | Sniffing (unfiltered traffic) |
| Switch | L2    | Forwards by MAC          | MAC flooding → DoS            |
| Router | L3    | Routes by IP             | Route poisoning attacks       |

## Switch Operations (Steps)  
1. **Learning**: Records MAC → Port in CAM table.  
2. **Forwarding**: Sends frames only to destination port.  
3. **Unicast Flood**: If MAC unknown, floods to all VLAN ports.  
4. **VLANs**: Logically separate networks (e.g., `switchport access vlan 10`).  