# SQL Injection (SQLi) – Notes

## What is SQLi?

**SQL Injection** is a vulnerability that occurs when user input is **unsafely** included in SQL queries, allowing attackers to:

- Read or modify the database
- Bypass login/authentication
- Dump sensitive data
- Execute administrative operations

---

## How it works

Untrusted input is **injected directly** into an SQL query:

```sql
SELECT * FROM users WHERE username = 'admin' AND password = 'pass';
```

If unsanitized, attacker inputs:

```sql
' OR 1=1 --
```

Query becomes:

```sql
SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = '';
```

Always true → Authentication bypassed.

---

# Types of SQL Injection

---

## 1. **Classic / In-band SQLi**

Direct results in the browser/app.

### a. **Error-based**

- Forces the database to generate errors that leak data.
    
- Example:
    
```sql
' AND extractvalue(1, concat(0x7e, version())) --
```
    

### b. **Union-based**

- Uses `UNION` to combine results from multiple queries.

- Example:

```sql
' UNION SELECT null, username, password FROM users --
```


---

## 2. **Blind SQLi**

App doesn’t show errors, but you infer behavior from responses.

### a. **Boolean-based**

- Send payloads that change the logic and observe differences.Z
- Example:

 ```sql
 ' AND 1=1 --  (returns normal)    ' AND 1=2 --  (returns blank/error)
 ```


### b. **Time-based**

- Uses delays (e.g., `SLEEP(5)`) to detect if the query ran.

- Example:

```sql
  ' OR IF(1=1, SLEEP(5), 0) --
```

---

## 3. **Out-of-Band SQLi**

- Uses **external interactions** (DNS, HTTP) to exfiltrate data.
- Only possible if DB supports external calls (e.g., `LOAD_FILE`, `xp_dirtree` on MSSQL).

---

## 4. **Second-Order SQLi**

- Injection is stored in the database and executed later in a different query.    
- Happens when an app stores unsafe input and reuses it insecurely.

---

# Prevention

| Technique                    | Description                                  |
| ---------------------------- | -------------------------------------------- |
| Prepared statements / ORM    | Use parameterized queries (no string concat) |
| Input validation             | Whitelist expected input types               |
| Escaping user input          | Escape dangerous characters (fallback only)  |
| Principle of Least Privilege | DB users should have only needed access      |
| Web Application Firewalls    | Can detect/stop some SQLi attempts           |

---

# Real-world SQLi payloads (basic)

|Goal|Payload|
|---|---|
|Bypass login|`' OR 1=1 --`|
|Detect blind SQLi|`' AND 1=1 --` vs `' AND 1=2 --`|
|Time-based detection|`' OR SLEEP(5) --`|
|Extract DB name|`' UNION SELECT database(), null --`|
|Dump all users|`' UNION SELECT user, password FROM users --`|

---

# Tools for testing:

- `sqlmap` (automated SQLi tool)
- `Burp Suite`
- `requestbin` (for OOB testing)
- Custom scripts with curl/python

---

# Don't forget:

SQLi is **one of the most dangerous and common web vulnerabilities** (OWASP Top 10).

Always use **prepared statements** (e.g., `cursor.execute("SELECT * FROM users WHERE id = ?", [user_id])`)

---

# Mitigation

Simply encode data, use prepared statements and validate inputs.

---
