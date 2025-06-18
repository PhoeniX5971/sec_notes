# How to Use – AES JPG Brute Force Decryption Tool

This tool attempts to brute-force decrypt an encrypted file (e.g., encrypted JPG) using AES encryption. It checks whether a decrypted version starts with the JPEG magic number (`0xFFD8FF`). If it finds one, it saves the decrypted result.

## Features

- Supports AES encryption: `aes-128-ecb`, `aes-128-cbc`, `aes-256-ecb`, `aes-256-cbc`
    
- Allows brute-forcing key candidates using hex digits or numbers only
    
- Detects success by checking if the decrypted data starts with JPG signature
    
- Supports custom key testing mode
    
- Has optional modes for MSB-first or LSB-first key padding
    

---

## Basic Syntax

```bash
python3 decryptor.py -in <encrypted_file> -d <num_digits> [options]
```

### Required Flags:

- `-in <path>`: The path to the encrypted file.
    
- `-d <digits>`: Number of hex digits to brute-force (from 1 to 32).
    

---

## Optional Flags:

- `--msbytes`: Use Most Significant Bytes first in the key (default: Least Significant).
    
- `--no-letters`: Only use numeric digits (0–9) in key generation; excludes `a–f`.
    
- `--enc`: Specify encryption method. Options:
    
    - `aes-128-ecb` _(default)_
        
    - `aes-128-cbc`
        
    - `aes-256-ecb`
        
    - `aes-256-cbc`
        
- `--test-key <hexkey>`: Skip brute force and try a specific key instead.
    

---

## Examples

### 1. Brute force with 4-digit hex key, using AES-128-ECB:

```bash
python3 decryptor.py -in secret.enc -d 4
```

### 2. Brute force with 6-digit hex key, most-significant-bytes first:

```bash
python3 decryptor.py -in secret.enc -d 6 --msbytes
```

### 3. Brute force using numeric digits only (no letters):

```bash
python3 decryptor.py -in secret.enc -d 4 --no-letters
```

### 4. Brute force using AES-256-CBC:

```bash
python3 decryptor.py -in secret.enc -d 6 --enc aes-256-cbc
```

### 5. Test a specific key manually:

```bash
python3 decryptor.py -in secret.enc -d 0 --test-key deadbeef1234567890abcdef00000000
```

---

## Output

- All successful decryptions are saved inside a `decrypted_output/` directory.
    
- Output filenames follow this format:
    
    ```
    decrypted_<method>_<mode>_<keyportion>.jpg
    ```
    

---

## JPG Detection Logic

The script determines a successful decryption by checking if the output starts with the magic number for JPEG files (`0xFFD8FF`).  
This can be modified to support other file types by adjusting the `is_jpg_file()` function.

### For example, to detect PNG:

Replace:

```python
return len(data) >= 3 and data[:3] == b"\xff\xd8\xff"
```

with:

```python
return data.startswith(b"\x89PNG\r\n\x1a\n")
```

---

## Notes

- This is a brute-force tool — execution time increases exponentially with `-d`.
    
- Try smaller digit counts first, especially when testing or debugging.
    
- You may want to parallelize the brute force process or optimize it further for large keyspaces.
    

---

This tool is useful for:

- CTF challenges
    
- Educational demonstrations on encryption/decryption
    
- Recovery from known small key mistakes (e.g., low-entropy test keys)
    

It is **not** practical for cracking secure full-length AES keys unless you have prior knowledge or constraints.

---

> This tool was generated with the help of AI.

