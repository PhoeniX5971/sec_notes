## Scenario: Host A (192.168.1.2) → Host B (10.0.0.5)

### Step 1: L3 Check
```bash
Host A Routing Table:
Destination     Gateway         Genmask         Flags
0.0.0.0        192.168.1.1     0.0.0.0         UG
192.168.1.0    0.0.0.0         255.255.255.0   U
```

- **Action**: B's IP (10.0.0.5) ≠ local network → send to gateway (192.168.1.1)

> This is a routing table, it shows all routes that the table can take, since address B isn't on this network, then it must be sent through the gateway, regardless if the Host B actually exist within the connected network, after the packet is sent through the Gateway, if the Host B doesn't exist the packet would just be discarded later, however for now the packet will be sent out.

### Step 2: ARP Resolution
```bash
Host A ARP Cache (before):
Address         HWtype          HWaddress
192.168.1.1    ether           (incomplete)
```

- **Action**: ARP broadcast "Who has 192.168.1.1?"
- **Switch**: Floods ARP to all ports (Unicast Flood)

### Step 3: Gateway Response
```bash
Host A ARP Cache (after):
Address         HWtype          HWaddress
192.168.1.1    ether           aa:bb:cc:dd:ee:ff
```

> Step 2 and 3 show arp tables, those are present in switches too, they basically point layer 3 (network layer) addresses (ip address) to their corresponding HWaddresses (physical address, mac address, it has many names), since the routing table says to send it via the gateway (192.168.1.1), and we do not know to whom this **ip** address belongs (not present in the arp table as you can see in step two where it shows incomplete), thus we will do a **unicast flood**, which basically sends to all connected devices a "Who has 192.168.1.1" message, when the router, aka. the holder of 192.168.1.1 receives this message, it will send a response that it is the owner, this response contains the **mac** address of the router, thus we can now add it to the arp table, and then send the actual packet that we want to send to Host B there.

### Step 4: Router Processing
```bash
Router Routing Table:
Network         Next Hop        Interface
10.0.0.0/24     203.0.113.1    eth1
```

- **Action**: Encapsulates packet with new L2 header (src MAC: router, dst MAC: next hop)
- 
### Step 5: NAT Translation
```bash
NAT Table:
Internal IP:Port → External IP:Port
192.168.1.2:54321 → 203.0.113.5:60000
```

## Visual Flow
```
Host A → Switch (CAM table lookup) → Router (Routing table) → Internet → Dest Network
```

## Key Tables Summary

|Table|Location|Command to View|Purpose|
|---|---|---|---|
|Routing Table|Hosts/Routers|`netstat -rn` (Linux)|Path selection|
|ARP Cache|Hosts|`arp -a`|IP → MAC mappings|
|CAM Table|Switches|`show mac-address-table` (Cisco)|MAC → Port mappings|
|NAT Table|Routers|`show ip nat translations`|IP/Port translation|
![[tmp_network_traffic_visial.svg]]