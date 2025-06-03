# ARP Poisoning

A **MAN IN THE MIDDLE** attack.

Say two devices are connected in a network.

Device A:
IP: 192.168.101.5
MAC: aa:aa:aa:aa:aa:aa

Device B:
IP: 192.168.101.10
MAC: bb:bb:bb:bb:bb:bb

When communicating in the same network, those two devices would reach each other through mac addresses. Those mac addresses would be pointed to with arp, where the ip addresses would be connected to their appropriate mac addresses.

So in a normal communication A would send to B like this:

| Sender   | aa:aa:aa:aa:aa:aa     |
| -------- | --------------------- |
| Receiver | bb:bb:bb:bb:bb:bb     |
| Payload  | password: hello_there |

A simple message containing the password.

Now our hacker with the following addresses:

IP: 192.168.101.20
MAC: dd:dd:dd:dd:dd:dd

Would actually go in the middle of this networks.
Basically, A wants to send the message we saw above to B again.

Our hacker would trick both devices, where he would tell device A that the hacker himself is B, and tell B that the hacker himself is A.

Basically:

## For A

Supposed table:

| IP             | MAC               | Device |
| -------------- | ----------------- | ------ |
| 192.168.101.5  | aa:aa:aa:aa:aa:aa | A      |
| 192.168.101.10 | bb:bb:bb:bb:bb:bb | B      |
| 192.168.101.20 | dd:dd:dd:dd:dd:dd | Hacker |

After hacker does his stuffs:

 - Device A would be tricked to think that:

| IP             | MAC               | Device                 |
| -------------- | ----------------- | ---------------------- |
| 192.168.101.5  | aa:aa:aa:aa:aa:aa | A                      |
| 192.168.101.10 | dd:dd:dd:dd:dd:dd | Fake B (Actual Hacker) |
| 192.168.101.20 | dd:dd:dd:dd:dd:dd | Hacker                 |
- Device B would be tricked to think that:

| IP             | MAC               | Device                 |
| -------------- | ----------------- | ---------------------- |
| 192.168.101.5  | dd:dd:dd:dd:dd:dd | Fake A (Actual Hacker) |
| 192.168.101.10 | bb:bb:bb:bb:bb:bb | B                      |
| 192.168.101.20 | dd:dd:dd:dd:dd:dd | Hacker                 |

So when A sends to B it send to the hacker and when B sends to A it sends to the hacker.

---
## Bettercap

```bash

net.probe on
Net.recon on


echo 1 > /proc/sys/net/ipv4/ip_forward
echo 0 > /proc/sys/net/ipv4/conf/all/send_redirection

bettercap -eval "set arp.spoof.targets 192.168.0.108 192.168.0.1; set arp.spoof.fullduplex true; set arp.spoof.interval 10; arp.spoof on; net.sniff on"

```

---
