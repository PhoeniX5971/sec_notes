# How to Install – AES JPG Brute Force Decryption Tool

## Installation Instructions

### 1. Clone or download the script directory to your local machine.

### 2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

_(On Windows use: `venv\Scripts\activate` instead)_

> You will need to reactivate with the `source venv/bin/activate` each time you start a new session.

### 3. Install required packages:

```bash
pip install -r requirements.txt
```

### 4. Run the tool:

```bash
python decryptor.py -in <encrypted_file> -d <digits> [other options...]
```

---

### To deactivate the virtual environment when done:

```bash
deactivate
```
