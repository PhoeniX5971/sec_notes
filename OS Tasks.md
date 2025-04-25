# Task 1: What are `awk`, `sed`, `curl`, and `wget` commands?

## `awk` – Pattern Scanning and Processing

**`awk`** is a powerful text-processing language used to manipulate and analyze structured text (like tables, logs, and CSVs).

### Basic Syntax

`awk 'pattern {action}' file`

### Common Use Cases

- Print specific columns from a file:
    `awk '{print $1, $3}' data.txt`
    
- Filter lines with a condition:
    `awk '$2 > 50' file.txt`
    
- Use field separator (like commas):
    `awk -F, '{print $1}' data.csv`
    

### Key Concepts

- `$0` = whole line
    
- `$1`, `$2`, ... = columns
    
- `NR` = current line number
    
- `BEGIN {}` and `END {}` blocks for setup and teardown
    

---

## `sed` – Stream Editor

**`sed`** is a command-line utility for parsing and transforming text in a stream or file.

### Basic Syntax

`sed 's/pattern/replacement/' file`

### Common Use Cases

- Replace first occurrence of "cat" with "dog":
    `sed 's/cat/dog/' file.txt`
    
- Replace globally on each line:
    `sed 's/cat/dog/g' file.txt`
    
- Delete lines:
    `sed '/pattern/d' file.txt`
    

### Notes

- `-i` modifies files in-place (be cautious):
    `sed -i 's/foo/bar/g' file.txt`
    

---

## `curl` – Client URL

**`curl`** is a command-line tool to transfer data to or from a server using protocols like HTTP, HTTPS, FTP, etc.

### Common Use Cases

- Fetch a webpage:
    `curl https://example.com`
    
- Save output to file:
    `curl -o index.html https://example.com`
    
- Send POST request:
    `curl -X POST -d "username=user&password=pass" https://site.com/login`
    
- Add headers:
    `curl -H "Authorization: Bearer TOKEN" https://api.com/data`
    

---

## `wget` – Web Get

**`wget`** is used to **download files** from the web non-interactively.

### Common Use Cases

- Download a file:
    `wget https://example.com/file.zip`
    
- Download in background:
    `wget -b https://example.com/file.zip`
    
- Mirror an entire website:
    `wget --mirror -p --convert-links -P ./local-dir https://site.com`
    

### `wget` vs `curl`

- `wget` is better for bulk or recursive downloading.
    
- `curl` is better for APIs and fine-grained control.
    

---

# Task 2: Linux File Permissions

## File Permissions in Linux

Linux permissions control **who can read, write, or execute** files and directories.

Every file has **three levels of access**:

1. **Owner (user)**
    
2. **Group**
    
3. **Others (world)**
    

Each level has **three permission types**:

- `r` = read
    
- `w` = write
    
- `x` = execute
    

---

## Viewing Permissions

Run:

`ls -l`

Example output:

`-rwxr-xr-- 1 user group 1234 Apr 25 10:00 script.sh`

Breakdown:

- `-` → regular file
    
- `rwx` → owner: can read/write/execute
    
- `r-x` → group: can read/execute
    
- `r--` → others: can read only
    

---

## Changing Permissions

### `chmod` – Change Mode

Change file permissions.

- **Symbolic mode**:
```bash
chmod u+x file.sh   # add execute for owner
chmod g-w file.sh   # remove write for group
chmod o=r file.sh   # others can only read

    ```

- **Numeric mode**:
    
    - `r = 4`, `w = 2`, `x = 1`
        
    - Add values to get total permission
        
    `chmod 755 file.sh`
    
    Meaning:
    
    - Owner: 7 (4+2+1 = rwx)
        
    - Group: 5 (4+0+1 = r-x)
        
    - Others: 5 (4+0+1 = r-x)
        

---

## Changing Ownership

### `chown` – Change Owner

```bash
chown user file.txt         # Change owner
chown user:group file.txt   # Change owner and group
```

### `chgrp` – Change Group

`chgrp group file.txt`

---

## Directory Permissions

- `r` → list contents (`ls`)
    
- `w` → create/delete files
    
- `x` → access (enter the directory)
    

Example:

`chmod 700 private_dir`

Only the owner can read/write/enter.

---

## Summary Table

|Symbol|Meaning|Binary|Decimal|
|---|---|---|---|
|`r`|Read|100|4|
|`w`|Write|010|2|
|`x`|Execute|001|1|
|`-`|No permission|000|0|

|Role|Description|
|---|---|
|u|User (owner)|
|g|Group|
|o|Others|
|a|All (user + group + others)|
