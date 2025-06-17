# RSA

## Generation

- Pick P & Q such that P & Q are secret large prime numbers.
- Public model N = P x Q
- PHI = (P - 1) (Q - 1)
- Public exponent E such that 1 < E < PHI, relatively prime to PHI (no common factors).
- Private exponent D = inv(E) mod PHI
- Public Key = (N, E)
- Private Key = (N, D)

---
## Application

- Key size = Size of N
- RSA may cipher/decipher only data size < N
- Encrypt C = P^E mod N
- Decrypt P = C^D mod N
- (X^D)^E mod N = (X^E)^D mod N

Complexity depends on the number of bits with value 1 in E and D, most commonly used: 3, 17, 65537.

---
