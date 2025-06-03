# Port Scanning and Discovery

## Nmap

```bash
nmap -T 5 <ip_addr> -p 80
```

**-T**: scanning speed. 0 very slow, 5 very fast...
**-p**: specific port only, separate with ","
**-v**: verbose
**-d**: raise debug level
**-iL**: supply text file with ip addresses
**-oN**: add to output file
**-sP**: check if alive
**-F**: top 100 ports
**--top-ports**: top n ports
**--script vuln***: scans for all vulns with scripts

```bash
nmap -sV -p- 10.10.10.10
```

`-p-` scans all ports
`-sV` attempts to detect service version

```bash
nmap -A -p- 10.10.10.10
```

`-A` aggressive scan that includes os detection, version detection, script scanning, and traceroute on all ports.

---
