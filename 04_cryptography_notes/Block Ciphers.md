# Block Ciphers

**DES** key of size 64 bits. 16 hex characters. Each 2 chars are 1 byte, each byte is 8 bits so 64 in total. (56 key with 8 parity)

---
**ECB** Electronic Code Block

Literally divided into blocks, each of proper size.
Those blocks can be differentiated and ordered, thus u might fall into known plain text attacks. 

---
CBC Chaining blocks together.
Not parallel, order not shown.

Pick IV, xor it with p1 and encrypt with key get c1, encrypt c1 with p2 using key get c2...

---
To fill in shorter ones u can add block padding

---
