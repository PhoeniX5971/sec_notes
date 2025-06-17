# Random Number Generators

## True Random Number Generators

Using noise devices and such, however it is not efficient.

## Pseudo Random Number Generators

Uses an algorithm or a hardware device that generates a sequence of random bits, starting from an initial value called a seed.

The seed is usually TRN.

PRN sequence repeats periodically, should be very long, and it's periodicity depends on the size of the internal state model.

In C lang, openssl offers a set of functions that allow for creating randomly generated numbers. Example usage:

```cpp
#include <openssl/rand.h>
#include <stdio.h>

int main() {
	unsigned char buffer[4];
	unsigned int random_number = 0;

	RAND_bytes(buffer, sizeof(buffer));

	for (int i = 0; i < 10; i++) {
		random_number = (random_number << 8) | buffer[i];
	}
	printf("Random number: %u\n", random_number);
	return 0;
}
```

---
 