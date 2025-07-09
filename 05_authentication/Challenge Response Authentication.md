# Challenge Response Authentication

![[Pasted image 20250617234726.png]]

---

Challenge must be:
- Non repeatable
- Non invertable

---

## Symmetric CRA

1. Share secret key over some secure channel/using encryption (diffie-hellman and such)
2.  Server send nonce to user
3. User sends the solution back to server

---

## Symmetric CRA Attack

1. Intruder sends a Nonce to Bob to solve
2. Bob sends the solution and sends a nonce for the intruder to solve
3. Intruder starts a new session and sends the nonce he got back to Bob
4. Bob solves the nonce and sends back to second session
5. Intruder takes this answer and sends it back to Bob
6. violla, intruder is in ggs.

---

## Asymmetric CRA

1. User sends certificate with their public key
2. Server sends encrypted nonce will the user's public key, only the owner of the secret key can get back the actual thing, thus intruders can't use this
3. User sends the response in plain text back, yes can be sniffed, but it is not repeatable so is fine

---
## MFA/2FA

Apply another layer of security.

One of the layers should be non reusable (just like email verification pins and such)

---

## OTP

One time password

1. Finish first auth
2. Server sends request for OTP
3. User sends OTP and gets access

---
## S/Key System

1. Secret is generated
2. Secret is hashed P1=hash(secret)
3. $$P_n = Hash(P_{n-1})$$
4. Server would store Pn at first
5. Auth would happen by sending Pn-1 (the one before last)
6. Server then verifies the identity if hash works, and discards Pn, and sets the hash value to Pn-1
7. Now we need to send the one just before that until we get back to the secret, then we redo the entire thing

---

## Time-Based OTP

One time password made using both secret and time.

Requires:
- Time sync between server and client
- Window time slot

> Messing with the time can allow different attacks, like DoS by changing the time, or even guessing the password by moving the time forwards and storing the generated OTP.

---

## OOB OTP

Out of bound OTP

1. Server auth req
2. UID + Puid
3. OTP on a different channel (just like using sms)

---
