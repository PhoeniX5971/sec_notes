# Privilege Escalation

## Enumeration

Scan for hostname, running proccesses, kernel version, user accounts, routing...

```bash
hostname
uname -a
ps aux
sudo -l
cat /etc/passwd | cut -d ":" -f 1
```

---

## Kernel Exploitation

Check kernel version.

Check for cve.

If you find cve, get the exp file, make a tmp server on /tmp, host the file, get the file on the victim machine, compile and run.

ggs, you alr a root user. xD


---

## sudo -l

whenever we can get into an interactive shell simply do !sh we got into a root shell.

---

## Linux Capabilities

```bash
getcap -r / 2>/dev/null
```

GFTObins

---

## crontab

check if u have permissions to edit a crontabbed script that's run by root, if yes then just edit it and wait for it to trigger.

---

## SUID

```bash
find / -type f -perm -04000 -ls 2>/dev/null
```

GFTObins

---
